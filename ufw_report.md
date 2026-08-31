# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4331
- Unique source IPs: 2822
- Unique countries/cities (24h): 458
- Unique destination ports: 2571

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 259 | 6.0% |
| 2 | `22` | 116 | 2.7% |
| 3 | `5060` | 41 | 0.9% |
| 4 | `5555` | 40 | 0.9% |
| 5 | `8080` | 32 | 0.7% |
| 6 | `8443` | 30 | 0.7% |
| 7 | `unknown` | 30 | 0.7% |
| 8 | `53` | 26 | 0.6% |
| 9 | `123` | 25 | 0.6% |
| 10 | `3306` | 22 | 0.5% |
| 11 | `1433` | 21 | 0.5% |
| 12 | `2222` | 20 | 0.5% |
| 13 | `25` | 15 | 0.3% |
| 14 | `1900` | 14 | 0.3% |
| 15 | `8888` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3764 | 86.9% |
| 2 | `UDP` | 537 | 12.4% |
| 3 | `47` | 27 | 0.6% |
| 4 | `4` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `204.76.203.4` | 19 | 0.4% |
| 2 | `18.119.209.50` | 15 | 0.3% |
| 3 | `85.217.140.27` | 14 | 0.3% |
| 4 | `85.217.140.35` | 14 | 0.3% |
| 5 | `151.243.11.240` | 14 | 0.3% |
| 6 | `172.110.223.179` | 14 | 0.3% |
| 7 | `18.190.15.50` | 13 | 0.3% |
| 8 | `85.217.140.33` | 13 | 0.3% |
| 9 | `77.239.124.127` | 13 | 0.3% |
| 10 | `45.194.67.120` | 12 | 0.3% |
| 11 | `85.217.140.30` | 12 | 0.3% |
| 12 | `18.221.179.104` | 11 | 0.3% |
| 13 | `85.217.140.28` | 11 | 0.3% |
| 14 | `85.217.140.20` | 11 | 0.3% |
| 15 | `85.217.140.29` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3733 | 99.2% |
| 2 | `SYN+ECE+CWR` | 14 | 0.4% |
| 3 | `ACK+FIN+PSH` | 9 | 0.2% |
| 4 | `ACK+PSH` | 5 | 0.1% |
| 5 | `ACK+FIN` | 2 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4331 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `172.110.223.179` -> `5060` | 14 | 0.3% |
| 2 | `204.76.203.4` -> `25566` | 8 | 0.2% |
| 3 | `94.154.43.64` -> `123` | 8 | 0.2% |
| 4 | `204.76.203.4` -> `25564` | 7 | 0.2% |
| 5 | `77.239.124.127` -> `23` | 5 | 0.1% |
| 6 | `152.53.148.66` -> `9001` | 5 | 0.1% |
| 7 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 8 | `77.239.124.127` -> `2323` | 5 | 0.1% |
| 9 | `151.101.219.10` -> `44172` | 5 | 0.1% |
| 10 | `66.132.195.107` -> `53` | 5 | 0.1% |
| 11 | `139.19.117.130` -> `22` | 4 | 0.1% |
| 12 | `204.76.203.4` -> `25565` | 4 | 0.1% |
| 13 | `172.64.155.231` -> `53508` | 4 | 0.1% |
| 14 | `180.93.250.126` -> `5938` | 4 | 0.1% |
| 15 | `69.17.52.1` -> `8333` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-08-30 04:00:00:00 | 133 | 3.1% |
| 2026-08-30 05:00:00:00 | 181 | 4.2% |
| 2026-08-30 06:00:00:00 | 179 | 4.1% |
| 2026-08-30 07:00:00:00 | 181 | 4.2% |
| 2026-08-30 08:00:00:00 | 180 | 4.2% |
| 2026-08-30 09:00:00:00 | 191 | 4.4% |
| 2026-08-30 10:00:00:00 | 180 | 4.2% |
| 2026-08-30 11:00:00:00 | 177 | 4.1% |
| 2026-08-30 12:00:00:00 | 183 | 4.2% |
| 2026-08-30 13:00:00:00 | 179 | 4.1% |
| 2026-08-30 14:00:00:00 | 181 | 4.2% |
| 2026-08-30 15:00:00:00 | 180 | 4.2% |
| 2026-08-30 16:00:00:00 | 178 | 4.1% |
| 2026-08-30 17:00:00:00 | 181 | 4.2% |
| 2026-08-30 18:00:00:00 | 179 | 4.1% |
| 2026-08-30 19:00:00:00 | 181 | 4.2% |
| 2026-08-30 20:00:00:00 | 181 | 4.2% |
| 2026-08-30 21:00:00:00 | 181 | 4.2% |
| 2026-08-30 22:00:00:00 | 178 | 4.1% |
| 2026-08-30 23:00:00:00 | 181 | 4.2% |
| 2026-08-31 00:00:00:00 | 181 | 4.2% |
| 2026-08-31 01:00:00:00 | 180 | 4.2% |
| 2026-08-31 02:00:00:00 | 180 | 4.2% |
| 2026-08-31 03:00:00:00 | 180 | 4.2% |
| 2026-08-31 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 86 | 43.7% |
| 2 | Dublin, United States | 39 | 19.8% |
| 3 | Eygelshoven, The Netherlands | 19 | 9.6% |
| 4 | Frankfurt am Main, Germany | 14 | 7.1% |
| 5 | Atlanta, United States | 14 | 7.1% |
| 6 | Amsterdam, The Netherlands | 13 | 6.6% |
| 7 | São Paulo, Brazil | 12 | 6.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `204.76.203.4` | 19 | 9.6% | The Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 2 | `18.119.209.50` | 15 | 7.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 3 | `85.217.140.27` | 14 | 7.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 4 | `85.217.140.35` | 14 | 7.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `151.243.11.240` | 14 | 7.1% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 6 | `172.110.223.179` | 14 | 7.1% | United States / Georgia / Atlanta / Dedires LLC | No apparent signal |
| 7 | `18.190.15.50` | 13 | 6.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `85.217.140.33` | 13 | 6.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `77.239.124.127` | 13 | 6.6% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |
| 10 | `45.194.67.120` | 12 | 6.1% | Brazil / São Paulo / São Paulo / Cloud Innovation Ltd | No apparent signal |
| 11 | `85.217.140.30` | 12 | 6.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `18.221.179.104` | 11 | 5.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `85.217.140.28` | 11 | 5.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `85.217.140.20` | 11 | 5.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `85.217.140.29` | 11 | 5.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `18.119.209.50` | 15 | 38.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 2 | `18.190.15.50` | 13 | 33.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.221.179.104` | 11 | 28.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
