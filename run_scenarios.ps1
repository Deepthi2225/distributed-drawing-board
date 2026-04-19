Set-Location "c:\Sem6\cc\CC_project"

$report = "scenario_report_clean.md"
Set-Content -Path $report -Encoding utf8 -Value "# Live Scenario Outputs`nGenerated: $(Get-Date -Format s)`n"

function Add-Section($title) {
    Add-Content -Path $report -Encoding utf8 -Value "`n## $title`n"
    Write-Output "--- $title ---"
}

function Add-Block($label, $text) {
    Add-Content -Path $report -Encoding utf8 -Value "### $label"
    Add-Content -Path $report -Encoding utf8 -Value $text
    Add-Content -Path $report -Encoding utf8 -Value ""
}

function StatusJson($port) {
    return (Invoke-RestMethod ("http://localhost:{0}/status" -f $port) | ConvertTo-Json -Depth 6)
}

Add-Section "Case 1 - Multiple tabs/users"
$gw = StatusJson 8000
$gwLogs = (docker compose logs --tail 80 gateway | Out-String)
Add-Block "Gateway status" $gw
Add-Block "Gateway log tail" $gwLogs

Add-Section "Case 2 - Killing leader"
$s1 = Invoke-RestMethod http://localhost:8001/status
$s2 = Invoke-RestMethod http://localhost:8002/status
$s3 = Invoke-RestMethod http://localhost:8003/status
$leaderBefore = @($s1, $s2, $s3) | Where-Object { $_.role -eq "leader" } | Select-Object -First 1
$killOut = (docker stop $leaderBefore.id | Out-String)
$logsAfterKill = (docker compose logs --since 25s gateway replica1 replica2 replica3 | Out-String)
Add-Block "Leader before kill" ($leaderBefore | ConvertTo-Json -Depth 6)
Add-Block "docker stop output" $killOut
Add-Block "Logs after kill" $logsAfterKill

Add-Section "Case 3 - Automatic failover"
$gwAfterFailover = StatusJson 8000
$r1After = StatusJson 8001
$r2After = StatusJson 8002
$r3After = StatusJson 8003
Add-Block "Gateway status after failover" $gwAfterFailover
Add-Block "Replica1 status" $r1After
Add-Block "Replica2 status" $r2After
Add-Block "Replica3 status" $r3After

Add-Section "Case 4 - Hot-reload replica"
(Get-Item "replica1/main.py").LastWriteTime = Get-Date
$reloadLogs = (docker compose logs --since 20s replica1 | Out-String)
Add-Block "Replica1 logs after touching file" $reloadLogs

Add-Section "Case 5 - Consistent state after restart"
$curr = @(
    (Invoke-RestMethod http://localhost:8001/status),
    (Invoke-RestMethod http://localhost:8002/status),
    (Invoke-RestMethod http://localhost:8003/status)
)
$leader = ($curr | Where-Object { $_.role -eq "leader" } | Select-Object -First 1)
$portMap = @{ replica1 = 8001; replica2 = 8002; replica3 = 8003 }
$leaderPort = $portMap[$leader.id]
$strokeResults = @()
for ($i = 1; $i -le 8; $i++) {
    $payload = @{
        type = "stroke"
        sender = "agent"
        x0 = $i
        y0 = $i
        x1 = ($i + 1)
        y1 = ($i + 1)
        color = "#111111"
        size = 3
    } | ConvertTo-Json

    try {
        $res = Invoke-RestMethod -Method Post -Uri ("http://localhost:{0}/stroke" -f $leaderPort) -ContentType "application/json" -Body $payload
        $strokeResults += ($res | ConvertTo-Json -Compress)
    } catch {
        $strokeResults += "error: $($_.Exception.Message)"
    }
}

$follower = (($curr | Where-Object { $_.id -ne $leader.id }) | Select-Object -First 1).id
$restartOut = (docker restart $follower | Out-String)
$statusPostRestart = @(
    (StatusJson 8001),
    (StatusJson 8002),
    (StatusJson 8003),
    (StatusJson 8000)
) -join "`n`n"
$consistencyLogs = (docker compose logs --since 30s $follower $($leader.id) gateway | Out-String)

Add-Block "Current leader" ($leader | ConvertTo-Json -Depth 6)
Add-Block "Stroke post results" (($strokeResults -join "`n"))
Add-Block "Follower restarted" $restartOut
Add-Block "Statuses after restart" $statusPostRestart
Add-Block "Logs around restart" $consistencyLogs

Add-Section "Case 6 - Chaotic conditions"
$chaos1 = (docker stop replica2 replica3 | Out-String)
$chaos2 = (docker start replica2 replica3 | Out-String)
$chaosLogs = (docker compose logs --since 30s gateway replica1 replica2 replica3 | Out-String)
$finalStatus = @(
    (StatusJson 8000),
    (StatusJson 8001),
    (StatusJson 8002),
    (StatusJson 8003)
) -join "`n`n"

Add-Block "Rapid stop output" $chaos1
Add-Block "Rapid start output" $chaos2
Add-Block "Logs during chaos" $chaosLogs
Add-Block "Final cluster status" $finalStatus

# bring all up
$null = docker start replica1 replica2 replica3

Write-Output "Clean report generated: $report"
