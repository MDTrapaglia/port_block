# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4340
- Unique source IPs: 2642
- Unique countries/cities (24h): 329
- Unique destination ports: 2610

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 155 | 3.6% |
| 2 | `22` | 87 | 2.0% |
| 3 | `8080` | 41 | 0.9% |
| 4 | `1433` | 39 | 0.9% |
| 5 | `53` | 35 | 0.8% |
| 6 | `5060` | 34 | 0.8% |
| 7 | `8443` | 33 | 0.8% |
| 8 | `3389` | 26 | 0.6% |
| 9 | `17000` | 26 | 0.6% |
| 10 | `3306` | 22 | 0.5% |
| 11 | `17001` | 19 | 0.4% |
| 12 | `unknown` | 19 | 0.4% |
| 13 | `21` | 18 | 0.4% |
| 14 | `5432` | 15 | 0.3% |
| 15 | `6379` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3972 | 91.5% |
| 2 | `UDP` | 349 | 8.0% |
| 3 | `47` | 17 | 0.4% |
| 4 | `132` | 1 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.201` | 52 | 1.2% |
| 2 | `45.135.193.159` | 18 | 0.4% |
| 3 | `217.60.76.226` | 17 | 0.4% |
| 4 | `85.217.140.22` | 15 | 0.3% |
| 5 | `85.217.140.30` | 14 | 0.3% |
| 6 | `85.217.140.6` | 14 | 0.3% |
| 7 | `85.217.140.35` | 14 | 0.3% |
| 8 | `172.110.223.173` | 14 | 0.3% |
| 9 | `85.217.140.5` | 14 | 0.3% |
| 10 | `85.217.140.20` | 13 | 0.3% |
| 11 | `85.217.140.7` | 13 | 0.3% |
| 12 | `85.217.140.18` | 12 | 0.3% |
| 13 | `18.217.208.51` | 12 | 0.3% |
| 14 | `85.217.140.28` | 12 | 0.3% |
| 15 | `3.151.116.231` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3920 | 98.7% |
| 2 | `ACK+FIN+PSH` | 18 | 0.5% |
| 3 | `ACK+PSH` | 16 | 0.4% |
| 4 | `SYN+ECE+CWR` | 13 | 0.3% |
| 5 | `ACK+FIN` | 5 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4340 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.201` -> `9003` | 9 | 0.2% |
| 2 | `199.45.155.24` -> `8443` | 8 | 0.2% |
| 3 | `201.20.85.122` -> `6379` | 7 | 0.2% |
| 4 | `151.101.218.13` -> `61902` | 7 | 0.2% |
| 5 | `186.123.1.125` -> `1433` | 7 | 0.2% |
| 6 | `216.180.246.201` -> `9005` | 7 | 0.2% |
| 7 | `216.180.246.201` -> `9009` | 7 | 0.2% |
| 8 | `109.94.173.183` -> `3389` | 6 | 0.1% |
| 9 | `178.20.210.152` -> `1723` | 6 | 0.1% |
| 10 | `89.42.231.200` -> `34567` | 6 | 0.1% |
| 11 | `194.28.89.218` -> `5038` | 6 | 0.1% |
| 12 | `216.180.246.201` -> `9006` | 6 | 0.1% |
| 13 | `216.180.246.201` -> `9008` | 6 | 0.1% |
| 14 | `185.218.86.25` -> `3000` | 5 | 0.1% |
| 15 | `216.180.246.84` -> `8080` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-18 04:00:00:00 | 134 | 3.1% |
| 2026-09-18 05:00:00:00 | 192 | 4.4% |
| 2026-09-18 06:00:00:00 | 191 | 4.4% |
| 2026-09-18 07:00:00:00 | 180 | 4.1% |
| 2026-09-18 08:00:00:00 | 180 | 4.1% |
| 2026-09-18 09:00:00:00 | 180 | 4.1% |
| 2026-09-18 10:00:00:00 | 180 | 4.1% |
| 2026-09-18 11:00:00:00 | 180 | 4.1% |
| 2026-09-18 12:00:00:00 | 179 | 4.1% |
| 2026-09-18 13:00:00:00 | 182 | 4.2% |
| 2026-09-18 14:00:00:00 | 177 | 4.1% |
| 2026-09-18 15:00:00:00 | 183 | 4.2% |
| 2026-09-18 16:00:00:00 | 180 | 4.1% |
| 2026-09-18 17:00:00:00 | 179 | 4.1% |
| 2026-09-18 18:00:00:00 | 178 | 4.1% |
| 2026-09-18 19:00:00:00 | 182 | 4.2% |
| 2026-09-18 20:00:00:00 | 181 | 4.2% |
| 2026-09-18 21:00:00:00 | 179 | 4.1% |
| 2026-09-18 22:00:00:00 | 180 | 4.1% |
| 2026-09-18 23:00:00:00 | 181 | 4.2% |
| 2026-09-19 00:00:00:00 | 180 | 4.1% |
| 2026-09-19 01:00:00:00 | 179 | 4.1% |
| 2026-09-19 02:00:00:00 | 180 | 4.1% |
| 2026-09-19 03:00:00:00 | 179 | 4.1% |
| 2026-09-19 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 121 | 49.4% |
| 2 | Massy, France | 52 | 21.2% |
| 3 | Dublin, United States | 23 | 9.4% |
| 4 | Langen, Germany | 18 | 7.3% |
| 5 | Eygelshoven, The Netherlands | 17 | 6.9% |
| 6 | Hong Kong, Hong Kong | 14 | 5.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.201` | 52 | 21.2% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `45.135.193.159` | 18 | 7.3% | Germany / Hesse / Langen / Pfcloud UG | No apparent signal |
| 3 | `217.60.76.226` | 17 | 6.9% | The Netherlands / Limburg / Eygelshoven / Iryna Ivanenko | No apparent signal |
| 4 | `85.217.140.22` | 15 | 6.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `85.217.140.30` | 14 | 5.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `85.217.140.6` | 14 | 5.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.35` | 14 | 5.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `172.110.223.173` | 14 | 5.7% | Hong Kong / Kowloon / Hong Kong / Dedires LLC | No apparent signal |
| 9 | `85.217.140.5` | 14 | 5.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.20` | 13 | 5.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.7` | 13 | 5.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.18` | 12 | 4.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `18.217.208.51` | 12 | 4.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `85.217.140.28` | 12 | 4.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `3.151.116.231` | 11 | 4.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.201` | 52 | 69.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `18.217.208.51` | 12 | 16.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `3.151.116.231` | 11 | 14.7% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
