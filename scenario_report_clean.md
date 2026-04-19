# Live Scenario Outputs
Generated: 2026-04-19T11:30:17


## Case 1 - Multiple tabs/users

### Gateway status
{
    "clients":  5,
    "leader":  "replica3",
    "committed":  0,
    "replicas":  [
                     "replica1",
                     "replica2",
                     "replica3"
                 ]
}

### Gateway log tail
gateway  | INFO:     Will watch for changes in these directories: ['/app/gateway']
gateway  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
gateway  | INFO:     Started reloader process [1] using WatchFiles
gateway  | INFO:     Started server process [8]
gateway  | INFO:     Waiting for application startup.
gateway  | INFO:     Application startup complete.
gateway  | 2026-04-19 05:55:10,361 [GATEWAY] INFO Leader updated ΓåÆ replica1
gateway  | INFO:     172.18.0.2:56354 - "POST /leader HTTP/1.1" 200 OK
gateway  | 2026-04-19 05:55:30,421 [GATEWAY] INFO Leader updated ΓåÆ replica2
gateway  | INFO:     172.18.0.3:50092 - "POST /leader HTTP/1.1" 200 OK
gateway  | 2026-04-19 05:56:33,315 [GATEWAY] INFO Leader updated ΓåÆ replica3
gateway  | INFO:     172.18.0.4:40416 - "POST /leader HTTP/1.1" 200 OK
gateway  | INFO:     172.18.0.3:53766 - "POST /leader HTTP/1.1" 200 OK
gateway  | 2026-04-19 05:58:39,320 [GATEWAY] INFO Leader updated ΓåÆ replica2
gateway  | 2026-04-19 05:59:42,198 [GATEWAY] INFO Leader updated ΓåÆ replica3
gateway  | INFO:     172.18.0.4:42652 - "POST /leader HTTP/1.1" 200 OK
gateway  | 2026-04-19 06:00:13,652 [GATEWAY] INFO Leader updated ΓåÆ replica1
gateway  | INFO:     172.18.0.2:55196 - "POST /leader HTTP/1.1" 200 OK



## Case 2 - Killing leader

### Leader before kill
{
    "id":  "replica3",
    "role":  "leader",
    "term":  4,
    "leader":  "replica3",
    "log_length":  0,
    "commit_index":  -1,
    "peers":  [
                  "replica1",
                  "replica2"
              ]
}

### docker stop output
replica3


### Logs after kill
gateway  | 2026-04-19 06:00:13,652 [GATEWAY] INFO Leader updated ΓåÆ replica1
gateway  | INFO:     172.18.0.2:55196 - "POST /leader HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44440 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44450 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44464 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44476 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44480 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44490 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44504 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44506 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44522 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44530 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44546 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44560 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:44566 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37796 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37808 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37818 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37820 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37830 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37836 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37842 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37846 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37854 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37870 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37874 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37886 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37896 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37904 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37910 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37924 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37932 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37936 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37938 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37946 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37954 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37962 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37970 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37980 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:37992 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38002 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38014 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38030 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38040 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38042 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38044 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38058 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38066 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38072 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38074 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38080 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38094 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38108 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38124 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38136 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38140 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38150 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38154 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38170 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38184 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38194 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38204 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38212 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38216 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38232 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38240 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38248 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38260 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38264 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38276 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38284 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38298 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38304 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38312 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38314 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40104 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40112 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40122 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40126 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40134 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40136 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40144 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40154 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40156 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40170 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40174 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40176 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40190 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40206 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40212 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40222 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40238 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40244 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40252 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40268 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40270 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40282 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40290 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40302 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40316 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40320 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40330 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40346 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40350 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40358 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40362 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40372 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40384 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40396 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40412 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40418 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | 2026-04-19 06:00:13,644 [REPLICA2] INFO Voted for replica1 in term 6
replica2  | INFO:     172.18.0.2:35684 - "POST /request-vote HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35694 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35698 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35710 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35726 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35732 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35746 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35752 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35764 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35772 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35778 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35788 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35804 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35808 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35810 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35826 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35838 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35850 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35866 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35868 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35880 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35886 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35890 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35894 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35896 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35910 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48272 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48284 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48292 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48308 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48316 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48332 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48338 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48352 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48364 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48378 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48390 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48392 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48400 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48404 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51040 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51044 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51050 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51054 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51060 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51066 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51076 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51082 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51086 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51100 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51110 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51120 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51122 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51056 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51068 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51080 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51084 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51092 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51106 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51118 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51132 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51140 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51146 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51158 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51164 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51174 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51190 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51194 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51208 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51222 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51232 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51246 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51258 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51266 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51270 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51278 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51282 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51298 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51308 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51314 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51330 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51332 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51334 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51346 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51348 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51356 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51362 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51376 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51382 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51386 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51390 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51392 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51396 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51408 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51424 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51434 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51448 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51456 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51470 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51474 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51484 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51492 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51498 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51508 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51510 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51526 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51530 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51544 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51548 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51556 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51568 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51572 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51584 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33958 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33964 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33978 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33994 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34008 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34020 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34022 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34024 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34032 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34036 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34052 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34062 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34074 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34090 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34100 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34116 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34130 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34136 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34140 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34150 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34162 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34172 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34182 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34196 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34210 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34224 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34232 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34242 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34246 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34258 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34272 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34282 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34292 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34300 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34312 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,627 [REPLICA1] INFO Starting election for term 6
replica1  | INFO:     172.18.0.4:34324 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,643 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,644 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,645 [REPLICA1] INFO ≡ƒÅå  Became LEADER for term 6
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO HTTP Request: POST http://gateway:8000/leader "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO Announced leadership to gateway (term=6)
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,681 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,682 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,844 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,845 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,009 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,508 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,509 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,672 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,673 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,838 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,017 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,017 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,180 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,181 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,343 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,344 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,511 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,512 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,674 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,675 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,837 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:54,838 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,002 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,002 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,171 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,839 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,013 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,014 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,176 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,177 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,340 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,341 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,506 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,507 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,674 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,675 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,172 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,840 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,336 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,841 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,336 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,499 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,011 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,499 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,662 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,176 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,663 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,178 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,826 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,827 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,996 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,518 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:55,997 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,519 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,162 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,683 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,163 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,684 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,327 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,846 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,847 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,190 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,192 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,364 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,365 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,529 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,530 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,696 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,697 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,864 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,865 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,328 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,492 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,033 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,492 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,036 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,210 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,662 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,211 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,662 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,384 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,825 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,385 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,825 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,989 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,991 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,714 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,715 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,156 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,156 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,320 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,321 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,492 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,493 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,655 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,655 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,818 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,716 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,819 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,981 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,981 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,148 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,149 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,316 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,316 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,480 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,480 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,643 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,643 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,809 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,810 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,978 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,979 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,143 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,143 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,310 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,311 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,484 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,485 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,650 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,651 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,823 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,824 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,988 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,989 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,154 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,155 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,319 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,319 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,483 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,483 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,653 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,654 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,819 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,820 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,984 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,985 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,149 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,150 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,314 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,315 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,485 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,485 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,655 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,656 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,818 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,818 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,982 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,982 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,150 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,152 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,324 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,325 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,495 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,496 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,664 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,665 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,830 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,830 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,993 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,994 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,165 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,165 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,341 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,343 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,512 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,513 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,685 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,686 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,850 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,852 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,024 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,024 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,189 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,189 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,355 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,356 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,519 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,520 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,686 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,687 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,866 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,866 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,034 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,035 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,206 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,209 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,377 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,377 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,549 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,549 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,720 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,720 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,884 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,885 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,054 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,055 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,222 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,222 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,397 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,398 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,572 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,572 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,740 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,741 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,909 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,910 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,092 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,092 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,261 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,262 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,426 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,426 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,597 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,599 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,764 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,765 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,929 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,930 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,101 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,102 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,281 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,283 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,446 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,447 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,614 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,614 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,777 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,777 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,948 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,948 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,114 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,115 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,280 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,281 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,450 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,450 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,616 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,616 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,790 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,791 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,968 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,969 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,144 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,146 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,309 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,310 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,473 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,474 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,644 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,644 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,816 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,817 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,986 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,986 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,149 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,150 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,316 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,317 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,488 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,489 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,654 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,654 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,078 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,079 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,244 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,246 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,632 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,641 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,642 [REPLICA3] WARNING Stepping down during heartbeat ΓÇö higher term seen
replica3  | INFO:     172.18.0.2:46544 - "POST /request-vote HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46552 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46558 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46560 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46572 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46580 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46588 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46596 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46606 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46612 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46618 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46620 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46624 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46632 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46634 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46644 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46658 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46664 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46680 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46690 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46696 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46700 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46716 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46718 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46726 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46730 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33674 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33676 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33686 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33700 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33702 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33710 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33722 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33732 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33746 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33748 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33752 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33754 - "POST /heartbeat HTTP/1.1" 200 OK



## Case 3 - Automatic failover

### Gateway status after failover
{
    "clients":  5,
    "leader":  "replica3",
    "committed":  0,
    "replicas":  [
                     "replica1",
                     "replica2",
                     "replica3"
                 ]
}

### Replica1 status
{
    "id":  "replica1",
    "role":  "follower",
    "term":  4,
    "leader":  "replica3",
    "log_length":  0,
    "commit_index":  -1,
    "peers":  [
                  "replica2",
                  "replica3"
              ]
}

### Replica2 status
{
    "id":  "replica2",
    "role":  "follower",
    "term":  4,
    "leader":  "replica3",
    "log_length":  0,
    "commit_index":  -1,
    "peers":  [
                  "replica1",
                  "replica3"
              ]
}

### Replica3 status
{
    "id":  "replica3",
    "role":  "leader",
    "term":  4,
    "leader":  "replica3",
    "log_length":  0,
    "commit_index":  -1,
    "peers":  [
                  "replica1",
                  "replica2"
              ]
}


## Case 4 - Hot-reload replica

### Replica1 logs after touching file
replica1  | INFO:     172.18.0.4:51298 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51308 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51314 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51330 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51332 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51334 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51346 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51348 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51356 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51362 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51376 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51382 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51386 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51390 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51392 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51396 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51408 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51424 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51434 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51448 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51456 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51470 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51474 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51484 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51492 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51498 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51508 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51510 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51526 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51530 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51544 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51548 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51556 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51568 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51572 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51584 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33958 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33964 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33978 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33994 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34008 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34020 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34022 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34024 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34032 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34036 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34052 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34062 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34074 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34090 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34100 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34116 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34130 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34136 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34140 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34150 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34162 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34172 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34182 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34196 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34210 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34224 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34232 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34242 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34246 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34258 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34272 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34282 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34292 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34300 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34312 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,627 [REPLICA1] INFO Starting election for term 6
replica1  | INFO:     172.18.0.4:34324 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,643 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,644 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,645 [REPLICA1] INFO ≡ƒÅå  Became LEADER for term 6
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO HTTP Request: POST http://gateway:8000/leader "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO Announced leadership to gateway (term=6)
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,681 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,682 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,844 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,845 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,009 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,508 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,509 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,672 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,673 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,838 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,839 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,013 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,014 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,176 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,177 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,340 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,341 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,506 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,507 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,674 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,675 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,840 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,841 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,011 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,176 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,178 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,518 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,519 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,683 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,684 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,846 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,847 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,190 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,192 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,364 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,365 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,529 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,530 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,696 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,697 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,864 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,865 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,033 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,036 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,210 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,211 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,384 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,385 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,714 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,715 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,716 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:20,827 [REPLICA1] INFO Voted for replica2 in term 7
replica1  | INFO:     172.18.0.3:44628 - "POST /request-vote HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:21,604 [REPLICA1] INFO Starting election for term 8
replica1  | 2026-04-19 06:00:21,620 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/request-vote "HTTP/1.1 200 OK"



## Case 5 - Consistent state after restart

### Current leader
{
    "id":  "replica3",
    "role":  "leader",
    "term":  4,
    "leader":  "replica3",
    "log_length":  0,
    "commit_index":  -1,
    "peers":  [
                  "replica1",
                  "replica2"
              ]
}

### Stroke post results
{"ok":true,"index":0}
{"ok":true,"index":1}
{"ok":true,"index":2}
{"ok":true,"index":3}
{"ok":true,"index":4}
{"ok":true,"index":5}
{"ok":true,"index":6}
{"ok":true,"index":7}

### Follower restarted
replica1


### Statuses after restart
{
    "id":  "replica1",
    "role":  "follower",
    "term":  4,
    "leader":  "replica3",
    "log_length":  8,
    "commit_index":  7,
    "peers":  [
                  "replica2",
                  "replica3"
              ]
}

{
    "id":  "replica2",
    "role":  "follower",
    "term":  4,
    "leader":  "replica3",
    "log_length":  8,
    "commit_index":  7,
    "peers":  [
                  "replica1",
                  "replica3"
              ]
}

{
    "id":  "replica3",
    "role":  "leader",
    "term":  4,
    "leader":  "replica3",
    "log_length":  8,
    "commit_index":  7,
    "peers":  [
                  "replica1",
                  "replica2"
              ]
}

{
    "clients":  5,
    "leader":  "replica3",
    "committed":  8,
    "replicas":  [
                     "replica1",
                     "replica2",
                     "replica3"
                 ]
}

### Logs around restart
replica1  | INFO:     172.18.0.4:51056 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51068 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51080 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51084 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51092 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51106 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51118 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51132 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51140 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51146 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51158 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51164 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51174 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51190 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51194 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51208 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51222 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51232 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51246 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51258 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51266 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51270 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51278 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51282 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51298 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51308 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51314 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51330 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51332 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51334 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51346 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51348 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51356 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51362 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51376 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51382 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51386 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51390 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51392 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51396 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51408 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51424 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51434 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51448 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51456 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51470 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51474 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51484 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51492 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51498 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51508 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51510 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51526 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51530 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51544 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51548 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51556 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51568 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51572 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51584 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33958 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33964 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33978 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33994 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34008 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34020 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34022 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34024 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34032 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34036 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34052 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34062 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34074 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34090 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34100 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34116 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34130 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34136 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34140 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34150 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34162 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34172 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34182 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34196 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34210 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34224 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34232 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34242 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34246 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34258 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34272 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34282 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34292 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34300 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34312 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,627 [REPLICA1] INFO Starting election for term 6
replica1  | INFO:     172.18.0.4:34324 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,643 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,644 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,645 [REPLICA1] INFO ≡ƒÅå  Became LEADER for term 6
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO HTTP Request: POST http://gateway:8000/leader "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO Announced leadership to gateway (term=6)
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,681 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,682 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,844 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,845 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,009 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,508 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,509 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,672 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,673 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,838 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,839 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,013 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,014 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,176 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,177 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,340 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,341 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,506 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,507 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,674 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,675 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,840 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,841 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,011 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,176 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,178 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,518 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,519 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,683 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,684 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,846 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,847 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,190 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,192 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,364 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,365 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,529 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,530 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,696 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,697 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,864 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,865 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,033 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,036 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,210 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,211 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,384 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,385 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,714 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,715 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,716 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:20,827 [REPLICA1] INFO Voted for replica2 in term 7
replica1  | INFO:     172.18.0.3:44628 - "POST /request-vote HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:21,604 [REPLICA1] INFO Starting election for term 8
replica1  | 2026-04-19 06:00:21,620 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/request-vote "HTTP/1.1 200 OK"
replica1  | WARNING:  WatchFiles detected changes in 'replica/main.py'. Reloading...
replica1  | INFO:     Shutting down
replica1  | INFO:     Waiting for application shutdown.
replica1  | INFO:     Application shutdown complete.
replica1  | INFO:     Finished server process [10]
replica1  | INFO:     Started server process [14]
replica1  | INFO:     Waiting for application startup.
replica1  | 2026-04-19 06:00:22,484 [REPLICA1] INFO Starting replica replica1  peers=['replica2', 'replica3']
replica1  | INFO:     Application startup complete.
replica1  | 2026-04-19 06:00:22,636 [REPLICA1] INFO Voted for replica2 in term 9
replica1  | INFO:     172.18.0.3:44638 - "POST /request-vote HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:22,709 [REPLICA1] INFO HTTP Request: GET http://replica2:8002/status "HTTP/1.1 200 OK"
replica1  | INFO:     172.18.0.3:44654 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:23,716 [REPLICA1] WARNING Catch-up failed ΓÇö no leader found
replica1  | INFO:     Will watch for changes in these directories: ['/app/replica']
replica1  | INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
replica1  | INFO:     Started reloader process [8] using WatchFiles
replica3  | 2026-04-19 05:59:56,162 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,163 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,327 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,328 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,492 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,492 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,662 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,662 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,825 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,825 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,989 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:56,991 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,156 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,156 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,320 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,321 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,492 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,493 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,655 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,655 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,818 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,819 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,981 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:57,981 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,148 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,149 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,316 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,316 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,480 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,480 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,643 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,643 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,809 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
gateway   | 2026-04-19 06:00:13,652 [GATEWAY] INFO Leader updated ΓåÆ replica1
replica3  | 2026-04-19 05:59:58,810 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,978 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:58,979 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,143 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
gateway   | INFO:     172.18.0.2:55196 - "POST /leader HTTP/1.1" 200 OK
replica3  | 2026-04-19 05:59:59,143 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,310 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,311 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
gateway   | 2026-04-19 06:00:23,623 [GATEWAY] INFO Leader updated ΓåÆ replica2
replica3  | 2026-04-19 05:59:59,484 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
gateway   | INFO:     172.18.0.3:52108 - "POST /leader HTTP/1.1" 200 OK
replica3  | 2026-04-19 05:59:59,485 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,650 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,651 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,823 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,824 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,988 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 05:59:59,989 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,154 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,155 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,319 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,319 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,483 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,483 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,653 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,654 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,819 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,820 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,984 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:00,985 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,149 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,150 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,314 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,315 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,485 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,485 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,655 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,656 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,818 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,818 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,982 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:01,982 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,150 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,152 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,324 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,325 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,495 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,496 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,664 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,665 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,830 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,830 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,993 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,994 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,165 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,165 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,341 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,343 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,512 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,513 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,685 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,686 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,850 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,852 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,024 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,024 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,189 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,189 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,355 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,356 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,519 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,520 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,686 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,687 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,866 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,866 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,034 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,035 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,206 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,209 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,377 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,377 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,549 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,549 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,720 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,720 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,884 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,885 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,054 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,055 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,222 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,222 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,397 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,398 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,572 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,572 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,740 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,741 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,909 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,910 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,092 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,092 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,261 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,262 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,426 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,426 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,597 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,599 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,764 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,765 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,929 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,930 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,101 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,102 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,281 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,283 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,446 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,447 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,614 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,614 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,777 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,777 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,948 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,948 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,114 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,115 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,280 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,281 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,450 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,450 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,616 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,616 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,790 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,791 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,968 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,969 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,144 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,146 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,309 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,310 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,473 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,474 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,644 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,644 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,816 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,817 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,986 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,986 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,149 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,150 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,316 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,317 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,488 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,489 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,654 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,654 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,078 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,079 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,244 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,246 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,632 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,641 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,642 [REPLICA3] WARNING Stepping down during heartbeat ΓÇö higher term seen
replica3  | INFO:     172.18.0.2:46544 - "POST /request-vote HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46552 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46558 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46560 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46572 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46580 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46588 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46596 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46606 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46612 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46618 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46620 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46624 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46632 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46634 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46644 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46658 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46664 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46680 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46690 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46696 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46700 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46716 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46718 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46726 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46730 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33674 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33676 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33686 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33700 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33702 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33710 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33722 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33732 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33746 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33748 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33752 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33754 - "POST /heartbeat HTTP/1.1" 200 OK



## Case 6 - Chaotic conditions

### Rapid stop output
replica2
replica3


### Rapid start output
replica2
replica3


### Logs during chaos
replica2  | INFO:     172.18.0.4:38094 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38108 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38124 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38136 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38140 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38150 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38154 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38170 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38184 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38194 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38204 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38212 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38216 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38232 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38240 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38248 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38260 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38264 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38276 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38284 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38298 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38304 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38312 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:38314 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40104 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40112 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40122 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40126 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40134 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40136 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40144 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40154 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40156 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40170 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40174 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40176 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40190 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40206 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40212 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40222 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40238 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40244 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40252 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40268 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40270 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40282 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40290 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40302 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40316 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40320 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40330 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40346 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40350 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40358 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40362 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40372 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40384 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40396 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40412 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.4:40418 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | 2026-04-19 06:00:13,644 [REPLICA2] INFO Voted for replica1 in term 6
replica2  | INFO:     172.18.0.2:35684 - "POST /request-vote HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35694 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35698 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35710 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35726 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35732 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35746 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35752 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35764 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35772 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35778 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35788 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35804 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35808 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35810 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35826 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35838 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35850 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35866 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35868 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35880 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35886 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35890 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35894 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35896 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:35910 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48272 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48284 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48292 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48308 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48316 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48332 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48338 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48352 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48364 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48378 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48390 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48392 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48400 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | INFO:     172.18.0.2:48404 - "POST /heartbeat HTTP/1.1" 200 OK
replica2  | 2026-04-19 06:00:20,807 [REPLICA2] INFO Starting election for term 7
replica2  | 2026-04-19 06:00:20,829 [REPLICA2] INFO HTTP Request: POST http://replica1:8001/request-vote "HTTP/1.1 200 OK"
replica2  | INFO:     172.18.0.2:48416 - "POST /request-vote HTTP/1.1" 200 OK
replica2  | 2026-04-19 06:00:21,619 [REPLICA2] INFO Voted for replica1 in term 8
replica2  | 2026-04-19 06:00:21,825 [REPLICA2] INFO Election failed ΓÇö votes=2/3
replica2  | 2026-04-19 06:00:22,595 [REPLICA2] INFO Starting election for term 9
replica2  | 2026-04-19 06:00:22,636 [REPLICA2] INFO HTTP Request: POST http://replica1:8001/request-vote "HTTP/1.1 200 OK"
replica2  | INFO:     172.18.0.2:48424 - "GET /status HTTP/1.1" 200 OK
replica2  | 2026-04-19 06:00:23,615 [REPLICA2] INFO ≡ƒÅå  Became LEADER for term 9
replica2  | 2026-04-19 06:00:23,623 [REPLICA2] INFO HTTP Request: POST http://gateway:8000/leader "HTTP/1.1 200 OK"
replica2  | 2026-04-19 06:00:23,624 [REPLICA2] INFO Announced leadership to gateway (term=9)
replica2  | 2026-04-19 06:00:23,643 [REPLICA2] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica2  | 2026-04-19 06:00:26,989 [REPLICA2] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica2  | INFO:     172.18.0.2:48426 - "GET /sync-log?from_index=0 HTTP/1.1" 200 OK
replica2  | 2026-04-19 06:00:28,139 [REPLICA2] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica2  | INFO:     Will watch for changes in these directories: ['/app/replica']
replica2  | INFO:     Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
replica2  | INFO:     Started reloader process [8] using WatchFiles
replica2  | INFO:     Started server process [10]
replica2  | INFO:     Waiting for application startup.
replica2  | 2026-04-19 06:00:32,578 [REPLICA2] INFO Starting replica replica2  peers=['replica1', 'replica3']
replica2  | INFO:     Application startup complete.
replica3  | 2026-04-19 06:00:02,150 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,152 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,324 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,325 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,495 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,496 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,664 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,665 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,830 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,830 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,993 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:02,994 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,165 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,165 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,341 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,343 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,512 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,513 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,685 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,686 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,850 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:03,852 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,024 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,024 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,189 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,189 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,355 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,356 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,519 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,520 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,686 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,687 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,866 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:04,866 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,034 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,035 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,206 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,209 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,377 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,377 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,549 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,549 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,720 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,720 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,884 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:05,885 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,054 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,055 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,222 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,222 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,397 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,398 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,572 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,572 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,740 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,741 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,909 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:06,910 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,092 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,092 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,261 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,262 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,426 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,426 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,597 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,599 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,764 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,765 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,929 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:07,930 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,101 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,102 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,281 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,283 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,446 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,447 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,614 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,614 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,777 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,777 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,948 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:08,948 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,114 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,115 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,280 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,281 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,450 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,450 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,616 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,616 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,790 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,791 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,968 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:09,969 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,144 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,146 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,309 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,310 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,473 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,474 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,644 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,644 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,816 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,817 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,986 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:10,986 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,149 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,150 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,316 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,317 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,488 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,489 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,654 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:11,654 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,078 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,079 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,244 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:12,246 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,632 [REPLICA3] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,641 [REPLICA3] INFO HTTP Request: POST http://replica1:8001/heartbeat "HTTP/1.1 200 OK"
replica3  | 2026-04-19 06:00:13,642 [REPLICA3] WARNING Stepping down during heartbeat ΓÇö higher term seen
replica3  | INFO:     172.18.0.2:46544 - "POST /request-vote HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46552 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46558 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46560 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46572 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46580 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46588 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46596 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46606 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46612 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46618 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46620 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46624 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46632 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46634 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46644 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46658 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46664 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46680 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46690 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46696 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46700 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46716 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46718 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46726 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:46730 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33674 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33676 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33686 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33700 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33702 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33710 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33722 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33732 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33746 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33748 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33752 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     172.18.0.2:33754 - "POST /heartbeat HTTP/1.1" 200 OK
replica3  | INFO:     Will watch for changes in these directories: ['/app/replica']
replica3  | INFO:     Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit)
replica3  | INFO:     Started reloader process [8] using WatchFiles
gateway   | 2026-04-19 06:00:13,652 [GATEWAY] INFO Leader updated ΓåÆ replica1
gateway   | INFO:     172.18.0.2:55196 - "POST /leader HTTP/1.1" 200 OK
gateway   | 2026-04-19 06:00:23,623 [GATEWAY] INFO Leader updated ΓåÆ replica2
gateway   | INFO:     172.18.0.3:52108 - "POST /leader HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51386 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51390 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51392 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51396 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51408 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51424 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51434 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51448 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51456 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51470 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51474 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51484 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51492 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51498 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51508 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51510 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51526 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51530 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51544 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51548 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51556 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51568 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51572 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:51584 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33958 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33964 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33978 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:33994 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34008 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34020 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34022 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34024 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34032 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34036 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34052 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34062 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34074 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34090 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34100 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34116 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34130 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34136 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34140 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34150 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34162 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34172 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34182 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34196 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34210 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34224 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34232 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34242 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34246 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34258 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34272 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34282 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34292 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34300 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | INFO:     172.18.0.4:34312 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,627 [REPLICA1] INFO Starting election for term 6
replica1  | INFO:     172.18.0.4:34324 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:13,643 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,644 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/request-vote "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,645 [REPLICA1] INFO ≡ƒÅå  Became LEADER for term 6
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO HTTP Request: POST http://gateway:8000/leader "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,653 [REPLICA1] INFO Announced leadership to gateway (term=6)
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,668 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,681 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,682 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,844 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:13,845 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,009 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,180 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,345 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,508 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,509 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,672 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,673 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,838 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:14,839 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,013 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,014 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,176 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,177 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,340 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,341 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,506 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,507 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,674 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,675 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,840 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:15,841 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,010 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,011 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,176 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,178 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,346 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,518 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,519 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,683 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,684 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,846 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:16,847 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,020 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,190 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,192 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,364 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,365 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,529 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,530 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,696 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,697 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,864 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:17,865 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,033 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,036 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,210 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,211 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,384 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,385 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,549 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,714 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,715 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:18,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,047 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,212 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,378 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica3:8003/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,544 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,716 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:19,883 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/heartbeat "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:20,827 [REPLICA1] INFO Voted for replica2 in term 7
replica1  | INFO:     172.18.0.3:44628 - "POST /request-vote HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:21,604 [REPLICA1] INFO Starting election for term 8
replica1  | 2026-04-19 06:00:21,620 [REPLICA1] INFO HTTP Request: POST http://replica2:8002/request-vote "HTTP/1.1 200 OK"
replica1  | WARNING:  WatchFiles detected changes in 'replica/main.py'. Reloading...
replica1  | INFO:     Shutting down
replica1  | INFO:     Waiting for application shutdown.
replica1  | INFO:     Application shutdown complete.
replica1  | INFO:     Finished server process [10]
replica1  | INFO:     Started server process [14]
replica1  | INFO:     Waiting for application startup.
replica1  | 2026-04-19 06:00:22,484 [REPLICA1] INFO Starting replica replica1  peers=['replica2', 'replica3']
replica1  | INFO:     Application startup complete.
replica1  | 2026-04-19 06:00:22,636 [REPLICA1] INFO Voted for replica2 in term 9
replica1  | INFO:     172.18.0.3:44638 - "POST /request-vote HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:22,709 [REPLICA1] INFO HTTP Request: GET http://replica2:8002/status "HTTP/1.1 200 OK"
replica1  | INFO:     172.18.0.3:44654 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:23,716 [REPLICA1] WARNING Catch-up failed ΓÇö no leader found
replica1  | INFO:     Will watch for changes in these directories: ['/app/replica']
replica1  | INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
replica1  | INFO:     Started reloader process [8] using WatchFiles
replica1  | INFO:     Started server process [10]
replica1  | INFO:     Waiting for application startup.
replica1  | 2026-04-19 06:00:26,958 [REPLICA1] INFO Starting replica replica1  peers=['replica2', 'replica3']
replica1  | INFO:     Application startup complete.
replica1  | INFO:     172.18.0.3:44670 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:27,188 [REPLICA1] INFO HTTP Request: GET http://replica2:8002/sync-log?from_index=0 "HTTP/1.1 200 OK"
replica1  | 2026-04-19 06:00:27,189 [REPLICA1] INFO Catch-up: already up to date
replica1  | INFO:     172.18.0.3:43890 - "POST /heartbeat HTTP/1.1" 200 OK
replica1  | 2026-04-19 06:00:29,210 [REPLICA1] INFO Starting election for term 10
replica1  | 2026-04-19 06:00:30,224 [REPLICA1] INFO Election failed ΓÇö votes=1/3
replica1  | 2026-04-19 06:00:30,876 [REPLICA1] INFO Starting election for term 11
replica1  | 2026-04-19 06:00:31,889 [REPLICA1] INFO Election failed ΓÇö votes=1/3
replica1  | 2026-04-19 06:00:32,467 [REPLICA1] INFO Starting election for term 12
replica1  | 2026-04-19 06:00:32,480 [REPLICA1] INFO Election failed ΓÇö votes=1/3


### Final cluster status
{
    "clients":  5,
    "leader":  "replica3",
    "committed":  8,
    "replicas":  [
                     "replica1",
                     "replica2",
                     "replica3"
                 ]
}

{
    "id":  "replica1",
    "role":  "follower",
    "term":  4,
    "leader":  "replica3",
    "log_length":  8,
    "commit_index":  7,
    "peers":  [
                  "replica2",
                  "replica3"
              ]
}

{
    "id":  "replica2",
    "role":  "follower",
    "term":  4,
    "leader":  "replica3",
    "log_length":  8,
    "commit_index":  7,
    "peers":  [
                  "replica1",
                  "replica3"
              ]
}

{
    "id":  "replica3",
    "role":  "leader",
    "term":  4,
    "leader":  "replica3",
    "log_length":  8,
    "commit_index":  7,
    "peers":  [
                  "replica1",
                  "replica2"
              ]
}

