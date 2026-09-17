# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4384
- Unique source IPs: 2563
- Unique countries/cities (24h): 403
- Unique destination ports: 2619

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 215 | 4.9% |
| 2 | `22` | 96 | 2.2% |
| 3 | `53` | 41 | 0.9% |
| 4 | `5060` | 37 | 0.8% |
| 5 | `8080` | 37 | 0.8% |
| 6 | `3389` | 28 | 0.6% |
| 7 | `1433` | 25 | 0.6% |
| 8 | `8443` | 23 | 0.5% |
| 9 | `123` | 20 | 0.5% |
| 10 | `21` | 20 | 0.5% |
| 11 | `3306` | 20 | 0.5% |
| 12 | `unknown` | 19 | 0.4% |
| 13 | `2222` | 18 | 0.4% |
| 14 | `5038` | 16 | 0.4% |
| 15 | `8888` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3832 | 87.4% |
| 2 | `UDP` | 533 | 12.2% |
| 3 | `47` | 17 | 0.4% |
| 4 | `4` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.76` | 23 | 0.5% |
| 2 | `85.217.140.19` | 20 | 0.5% |
| 3 | `217.60.76.226` | 16 | 0.4% |
| 4 | `85.217.140.7` | 16 | 0.4% |
| 5 | `148.59.129.127` | 16 | 0.4% |
| 6 | `85.217.140.29` | 16 | 0.4% |
| 7 | `85.217.140.5` | 15 | 0.3% |
| 8 | `85.217.149.37` | 15 | 0.3% |
| 9 | `85.217.140.20` | 14 | 0.3% |
| 10 | `85.217.140.30` | 14 | 0.3% |
| 11 | `85.217.140.35` | 14 | 0.3% |
| 12 | `85.217.140.22` | 14 | 0.3% |
| 13 | `85.217.140.28` | 14 | 0.3% |
| 14 | `85.217.140.6` | 13 | 0.3% |
| 15 | `85.217.140.3` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3732 | 97.4% |
| 2 | `ACK+FIN+PSH` | 58 | 1.5% |
| 3 | `ACK+PSH` | 21 | 0.5% |
| 4 | `SYN+ECE+CWR` | 14 | 0.4% |
| 5 | `ACK+FIN` | 7 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4384 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.76` -> `10398` | 8 | 0.2% |
| 2 | `151.101.218.13` -> `57228` | 7 | 0.2% |
| 3 | `178.20.210.152` -> `1723` | 6 | 0.1% |
| 4 | `216.180.246.195` -> `53` | 6 | 0.1% |
| 5 | `2.22.149.153` -> `56020` | 6 | 0.1% |
| 6 | `151.101.218.13` -> `56534` | 6 | 0.1% |
| 7 | `216.180.246.76` -> `10801` | 6 | 0.1% |
| 8 | `194.28.89.218` -> `5038` | 5 | 0.1% |
| 9 | `186.123.1.125` -> `1433` | 5 | 0.1% |
| 10 | `77.239.124.127` -> `2323` | 5 | 0.1% |
| 11 | `2.22.149.153` -> `58071` | 5 | 0.1% |
| 12 | `151.101.218.73` -> `59241` | 5 | 0.1% |
| 13 | `2.22.149.163` -> `59378` | 5 | 0.1% |
| 14 | `170.51.241.187` -> `57104` | 5 | 0.1% |
| 15 | `151.101.218.73` -> `56904` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-16 04:00:00:00 | 134 | 3.1% |
| 2026-09-16 05:00:00:00 | 179 | 4.1% |
| 2026-09-16 06:00:00:00 | 181 | 4.1% |
| 2026-09-16 07:00:00:00 | 176 | 4.0% |
| 2026-09-16 08:00:00:00 | 184 | 4.2% |
| 2026-09-16 09:00:00:00 | 180 | 4.1% |
| 2026-09-16 10:00:00:00 | 180 | 4.1% |
| 2026-09-16 11:00:00:00 | 179 | 4.1% |
| 2026-09-16 12:00:00:00 | 180 | 4.1% |
| 2026-09-16 13:00:00:00 | 181 | 4.1% |
| 2026-09-16 14:00:00:00 | 180 | 4.1% |
| 2026-09-16 15:00:00:00 | 178 | 4.1% |
| 2026-09-16 16:00:00:00 | 191 | 4.4% |
| 2026-09-16 17:00:00:00 | 177 | 4.0% |
| 2026-09-16 18:00:00:00 | 184 | 4.2% |
| 2026-09-16 19:00:00:00 | 180 | 4.1% |
| 2026-09-16 20:00:00:00 | 181 | 4.1% |
| 2026-09-16 21:00:00:00 | 180 | 4.1% |
| 2026-09-16 22:00:00:00 | 191 | 4.4% |
| 2026-09-16 23:00:00:00 | 192 | 4.4% |
| 2026-09-17 00:00:00:00 | 179 | 4.1% |
| 2026-09-17 01:00:00:00 | 212 | 4.8% |
| 2026-09-17 02:00:00:00 | 180 | 4.1% |
| 2026-09-17 03:00:00:00 | 181 | 4.1% |
| 2026-09-17 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 163 | 70.0% |
| 2 | Massy, France | 23 | 9.9% |
| 3 | Eygelshoven, The Netherlands | 16 | 6.9% |
| 4 | Piscataway, United States | 16 | 6.9% |
| 5 | Beauharnois, Canada | 15 | 6.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.76` | 23 | 9.9% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `85.217.140.19` | 20 | 8.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 3 | `217.60.76.226` | 16 | 6.9% | The Netherlands / Limburg / Eygelshoven / Iryna Ivanenko | No apparent signal |
| 4 | `85.217.140.7` | 16 | 6.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `148.59.129.127` | 16 | 6.9% | United States / New Jersey / Piscataway / Globex Internet Sevices Corporation | No apparent signal |
| 6 | `85.217.140.29` | 16 | 6.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.5` | 15 | 6.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.149.37` | 15 | 6.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 9 | `85.217.140.20` | 14 | 6.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.30` | 14 | 6.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.35` | 14 | 6.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.22` | 14 | 6.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `85.217.140.28` | 14 | 6.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `85.217.140.6` | 13 | 5.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `85.217.140.3` | 13 | 5.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.76` | 23 | 100.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
