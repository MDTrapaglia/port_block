# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4364
- Unique source IPs: 2411
- Unique countries/cities (24h): 305
- Unique destination ports: 2554

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 158 | 3.6% |
| 2 | `22` | 88 | 2.0% |
| 3 | `8080` | 49 | 1.1% |
| 4 | `5060` | 34 | 0.8% |
| 5 | `53` | 30 | 0.7% |
| 6 | `1433` | 29 | 0.7% |
| 7 | `3389` | 27 | 0.6% |
| 8 | `8443` | 25 | 0.6% |
| 9 | `6036` | 22 | 0.5% |
| 10 | `8081` | 20 | 0.5% |
| 11 | `1880` | 19 | 0.4% |
| 12 | `3306` | 18 | 0.4% |
| 13 | `17001` | 18 | 0.4% |
| 14 | `17000` | 17 | 0.4% |
| 15 | `161` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3933 | 90.1% |
| 2 | `UDP` | 415 | 9.5% |
| 3 | `47` | 12 | 0.3% |
| 4 | `41` | 4 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `93.123.101.174` | 74 | 1.7% |
| 2 | `171.224.105.74` | 34 | 0.8% |
| 3 | `62.210.142.166` | 23 | 0.5% |
| 4 | `62.210.142.173` | 21 | 0.5% |
| 5 | `141.98.83.48` | 17 | 0.4% |
| 6 | `94.154.43.163` | 17 | 0.4% |
| 7 | `165.227.207.164` | 16 | 0.4% |
| 8 | `195.178.110.204` | 16 | 0.4% |
| 9 | `85.217.140.3` | 15 | 0.3% |
| 10 | `91.230.168.233` | 15 | 0.3% |
| 11 | `91.230.168.129` | 15 | 0.3% |
| 12 | `91.231.89.0` | 14 | 0.3% |
| 13 | `91.231.89.10` | 14 | 0.3% |
| 14 | `85.217.140.28` | 13 | 0.3% |
| 15 | `91.231.89.224` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3846 | 97.8% |
| 2 | `ACK+FIN+PSH` | 43 | 1.1% |
| 3 | `ACK+PSH` | 17 | 0.4% |
| 4 | `SYN+ECE+CWR` | 14 | 0.4% |
| 5 | `ACK` | 11 | 0.3% |
| 6 | `ACK+FIN` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4364 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `94.154.43.163` -> `1880` | 17 | 0.4% |
| 2 | `62.210.142.173` -> `65432` | 9 | 0.2% |
| 3 | `36.48.147.177` -> `15231` | 8 | 0.2% |
| 4 | `62.210.142.166` -> `1195` | 8 | 0.2% |
| 5 | `167.250.224.25` -> `5038` | 7 | 0.2% |
| 6 | `62.210.142.173` -> `65527` | 7 | 0.2% |
| 7 | `196.244.192.202` -> `22` | 6 | 0.1% |
| 8 | `62.210.142.166` -> `1198` | 6 | 0.1% |
| 9 | `62.210.142.166` -> `1200` | 6 | 0.1% |
| 10 | `141.98.83.48` -> `161` | 5 | 0.1% |
| 11 | `201.20.85.122` -> `6379` | 5 | 0.1% |
| 12 | `45.194.92.105` -> `17001` | 5 | 0.1% |
| 13 | `45.194.92.100` -> `6036` | 5 | 0.1% |
| 14 | `45.194.92.102` -> `17000` | 5 | 0.1% |
| 15 | `62.210.142.173` -> `65535` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-02 04:00:00:00 | 134 | 3.1% |
| 2026-10-02 05:00:00:00 | 179 | 4.1% |
| 2026-10-02 06:00:00:00 | 181 | 4.1% |
| 2026-10-02 07:00:00:00 | 178 | 4.1% |
| 2026-10-02 08:00:00:00 | 183 | 4.2% |
| 2026-10-02 09:00:00:00 | 179 | 4.1% |
| 2026-10-02 10:00:00:00 | 178 | 4.1% |
| 2026-10-02 11:00:00:00 | 180 | 4.1% |
| 2026-10-02 12:00:00:00 | 187 | 4.3% |
| 2026-10-02 13:00:00:00 | 180 | 4.1% |
| 2026-10-02 14:00:00:00 | 180 | 4.1% |
| 2026-10-02 15:00:00:00 | 180 | 4.1% |
| 2026-10-02 16:00:00:00 | 181 | 4.1% |
| 2026-10-02 17:00:00:00 | 179 | 4.1% |
| 2026-10-02 18:00:00:00 | 181 | 4.1% |
| 2026-10-02 19:00:00:00 | 179 | 4.1% |
| 2026-10-02 20:00:00:00 | 188 | 4.3% |
| 2026-10-02 21:00:00:00 | 180 | 4.1% |
| 2026-10-02 22:00:00:00 | 179 | 4.1% |
| 2026-10-02 23:00:00:00 | 193 | 4.4% |
| 2026-10-03 00:00:00:00 | 200 | 4.6% |
| 2026-10-03 01:00:00:00 | 180 | 4.1% |
| 2026-10-03 02:00:00:00 | 176 | 4.0% |
| 2026-10-03 03:00:00:00 | 184 | 4.2% |
| 2026-10-03 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Frankfurt am Main, Germany | 74 | 23.3% |
| 2 | Gravelines, France | 69 | 21.8% |
| 3 | Paris, France | 44 | 13.9% |
| 4 | Hanoi, Vietnam | 34 | 10.7% |
| 5 | Hillsboro, United States | 30 | 9.5% |
| 6 | Panama City, Panama | 17 | 5.4% |
| 7 | Bursa, Turkey | 17 | 5.4% |
| 8 | North Bergen, United States | 16 | 5.0% |
| 9 | Andorra la Vella, Andorra | 16 | 5.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `93.123.101.174` | 74 | 23.3% | Germany / Hesse / Frankfurt am Main / Soulful Hosting LTD | No apparent signal |
| 2 | `171.224.105.74` | 34 | 10.7% | Vietnam / Hanoi / Hanoi / VIETEL | No apparent signal |
| 3 | `62.210.142.166` | 23 | 7.3% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 4 | `62.210.142.173` | 21 | 6.6% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 5 | `141.98.83.48` | 17 | 5.4% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 6 | `94.154.43.163` | 17 | 5.4% | Turkey / Bursa Province / Bursa / FOP Danik Vyacheslav Evgenievich | No apparent signal |
| 7 | `165.227.207.164` | 16 | 5.0% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 8 | `195.178.110.204` | 16 | 5.0% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 9 | `85.217.140.3` | 15 | 4.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `91.230.168.233` | 15 | 4.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 11 | `91.230.168.129` | 15 | 4.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 12 | `91.231.89.0` | 14 | 4.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.231.89.10` | 14 | 4.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `85.217.140.28` | 13 | 4.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `91.231.89.224` | 13 | 4.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.166` | 23 | 29.9% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `62.210.142.173` | 21 | 27.3% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 3 | `141.98.83.48` | 17 | 22.1% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 4 | `165.227.207.164` | 16 | 20.8% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
