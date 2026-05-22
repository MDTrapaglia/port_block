# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4328
- Unique source IPs: 2789
- Unique countries/cities (24h): 416
- Unique destination ports: 2697

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 223 | 5.2% |
| 2 | `27015` | 56 | 1.3% |
| 3 | `22` | 33 | 0.8% |
| 4 | `8080` | 32 | 0.7% |
| 5 | `5060` | 28 | 0.6% |
| 6 | `9200` | 24 | 0.6% |
| 7 | `5900` | 22 | 0.5% |
| 8 | `3389` | 20 | 0.5% |
| 9 | `1433` | 17 | 0.4% |
| 10 | `53` | 17 | 0.4% |
| 11 | `1434` | 16 | 0.4% |
| 12 | `8081` | 16 | 0.4% |
| 13 | `123` | 16 | 0.4% |
| 14 | `161` | 16 | 0.4% |
| 15 | `3306` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3852 | 89.0% |
| 2 | `UDP` | 469 | 10.8% |
| 3 | `47` | 6 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.235` | 68 | 1.6% |
| 2 | `45.33.16.187` | 31 | 0.7% |
| 3 | `143.42.188.111` | 26 | 0.6% |
| 4 | `85.217.149.36` | 21 | 0.5% |
| 5 | `85.217.149.17` | 17 | 0.4% |
| 6 | `68.43.126.168` | 14 | 0.3% |
| 7 | `50.116.30.65` | 14 | 0.3% |
| 8 | `85.217.149.15` | 14 | 0.3% |
| 9 | `85.217.149.48` | 14 | 0.3% |
| 10 | `85.217.149.34` | 13 | 0.3% |
| 11 | `204.76.203.15` | 12 | 0.3% |
| 12 | `52.20.198.190` | 11 | 0.3% |
| 13 | `85.217.149.47` | 11 | 0.3% |
| 14 | `85.217.149.41` | 11 | 0.3% |
| 15 | `205.200.179.20` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3828 | 99.4% |
| 2 | `ACK+PSH` | 15 | 0.4% |
| 3 | `ACK` | 4 | 0.1% |
| 4 | `SYN+ECE+CWR` | 3 | 0.1% |
| 5 | `ACK+FIN+PSH` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4322 | 99.9% |
| 2 | `wlan0` | 6 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `68.43.126.168` -> `23` | 14 | 0.3% |
| 2 | `205.200.179.20` -> `23` | 11 | 0.3% |
| 3 | `199.45.155.84` -> `8080` | 9 | 0.2% |
| 4 | `216.180.246.235` -> `809` | 8 | 0.2% |
| 5 | `216.180.246.235` -> `8042` | 7 | 0.2% |
| 6 | `216.180.246.235` -> `8103` | 7 | 0.2% |
| 7 | `192.168.100.1` -> `68` | 6 | 0.1% |
| 8 | `216.180.246.235` -> `8085` | 6 | 0.1% |
| 9 | `216.180.246.235` -> `61000` | 6 | 0.1% |
| 10 | `216.180.246.235` -> `8013` | 6 | 0.1% |
| 11 | `69.17.52.1` -> `8333` | 5 | 0.1% |
| 12 | `216.180.246.235` -> `9012` | 5 | 0.1% |
| 13 | `216.180.246.235` -> `33034` | 5 | 0.1% |
| 14 | `130.12.180.174` -> `23` | 4 | 0.1% |
| 15 | `209.222.101.194` -> `8188` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-21 04:00:00:00 | 136 | 3.1% |
| 2026-05-21 05:00:00:00 | 179 | 4.1% |
| 2026-05-21 06:00:00:00 | 180 | 4.2% |
| 2026-05-21 07:00:00:00 | 178 | 4.1% |
| 2026-05-21 08:00:00:00 | 182 | 4.2% |
| 2026-05-21 09:00:00:00 | 181 | 4.2% |
| 2026-05-21 10:00:00:00 | 180 | 4.2% |
| 2026-05-21 11:00:00:00 | 178 | 4.1% |
| 2026-05-21 12:00:00:00 | 182 | 4.2% |
| 2026-05-21 13:00:00:00 | 182 | 4.2% |
| 2026-05-21 14:00:00:00 | 178 | 4.1% |
| 2026-05-21 15:00:00:00 | 181 | 4.2% |
| 2026-05-21 16:00:00:00 | 180 | 4.2% |
| 2026-05-21 17:00:00:00 | 179 | 4.1% |
| 2026-05-21 18:00:00:00 | 183 | 4.2% |
| 2026-05-21 19:00:00:00 | 182 | 4.2% |
| 2026-05-21 20:00:00:00 | 180 | 4.2% |
| 2026-05-21 21:00:00:00 | 177 | 4.1% |
| 2026-05-21 22:00:00:00 | 183 | 4.2% |
| 2026-05-21 23:00:00:00 | 179 | 4.1% |
| 2026-05-22 00:00:00:00 | 181 | 4.2% |
| 2026-05-22 01:00:00:00 | 180 | 4.2% |
| 2026-05-22 02:00:00:00 | 180 | 4.2% |
| 2026-05-22 03:00:00:00 | 182 | 4.2% |
| 2026-05-22 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 68 | 23.6% |
| 2 | New York, United States | 55 | 19.1% |
| 3 | Beauharnois, Canada | 46 | 16.0% |
| 4 | Richardson, United States | 45 | 15.6% |
| 5 | Cedar Knolls, United States | 26 | 9.0% |
| 6 | Clinton Township, United States | 14 | 4.9% |
| 7 | Eygelshoven, Netherlands | 12 | 4.2% |
| 8 | Ashburn, United States | 11 | 3.8% |
| 9 | Winnipeg, Canada | 11 | 3.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.235` | 68 | 23.6% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `45.33.16.187` | 31 | 10.8% | United States / Texas / Richardson / Linode | Hosting/Cloud (linode) |
| 3 | `143.42.188.111` | 26 | 9.0% | United States / New Jersey / Cedar Knolls / Linode | Hosting/Cloud (linode) |
| 4 | `85.217.149.36` | 21 | 7.3% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 5 | `85.217.149.17` | 17 | 5.9% | United States / New York / New York / Modat B.V | No apparent signal |
| 6 | `68.43.126.168` | 14 | 4.9% | United States / Michigan / Clinton Township / Comcast Cable Communications, Inc. | No apparent signal |
| 7 | `50.116.30.65` | 14 | 4.9% | United States / Texas / Richardson / Linode | Hosting/Cloud (linode) |
| 8 | `85.217.149.15` | 14 | 4.9% | United States / New York / New York / Modat B.V | No apparent signal |
| 9 | `85.217.149.48` | 14 | 4.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 10 | `85.217.149.34` | 13 | 4.5% | United States / New York / New York / Modat B.V | No apparent signal |
| 11 | `204.76.203.15` | 12 | 4.2% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 12 | `52.20.198.190` | 11 | 3.8% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `85.217.149.47` | 11 | 3.8% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 14 | `85.217.149.41` | 11 | 3.8% | United States / New York / New York / Modat B.V | No apparent signal |
| 15 | `205.200.179.20` | 11 | 3.8% | Canada / Manitoba / Winnipeg / Bell Canada | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.235` | 68 | 45.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `45.33.16.187` | 31 | 20.7% | Hosting/Cloud (linode) | United States / Texas / Richardson / Linode |
| 3 | `143.42.188.111` | 26 | 17.3% | Hosting/Cloud (linode) | United States / New Jersey / Cedar Knolls / Linode |
| 4 | `50.116.30.65` | 14 | 9.3% | Hosting/Cloud (linode) | United States / Texas / Richardson / Linode |
| 5 | `52.20.198.190` | 11 | 7.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
