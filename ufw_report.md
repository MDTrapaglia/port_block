# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4365
- Unique source IPs: 2636
- Unique countries/cities (24h): 403
- Unique destination ports: 2699

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 176 | 4.0% |
| 2 | `22` | 88 | 2.0% |
| 3 | `8080` | 36 | 0.8% |
| 4 | `53` | 31 | 0.7% |
| 5 | `5060` | 30 | 0.7% |
| 6 | `3389` | 30 | 0.7% |
| 7 | `1433` | 25 | 0.6% |
| 8 | `unknown` | 22 | 0.5% |
| 9 | `123` | 20 | 0.5% |
| 10 | `2222` | 19 | 0.4% |
| 11 | `8443` | 17 | 0.4% |
| 12 | `3306` | 16 | 0.4% |
| 13 | `8000` | 16 | 0.4% |
| 14 | `161` | 15 | 0.3% |
| 15 | `500` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3878 | 88.8% |
| 2 | `UDP` | 465 | 10.7% |
| 3 | `47` | 20 | 0.5% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `151.101.218.13` | 17 | 0.4% |
| 2 | `85.217.140.23` | 16 | 0.4% |
| 3 | `85.217.140.33` | 15 | 0.3% |
| 4 | `85.217.140.3` | 15 | 0.3% |
| 5 | `85.217.140.19` | 15 | 0.3% |
| 6 | `18.217.208.51` | 14 | 0.3% |
| 7 | `85.217.140.27` | 14 | 0.3% |
| 8 | `85.217.140.28` | 13 | 0.3% |
| 9 | `85.217.140.30` | 13 | 0.3% |
| 10 | `85.217.140.22` | 13 | 0.3% |
| 11 | `85.217.140.1` | 13 | 0.3% |
| 12 | `170.51.241.171` | 13 | 0.3% |
| 13 | `141.98.83.48` | 12 | 0.3% |
| 14 | `77.239.124.127` | 12 | 0.3% |
| 15 | `85.217.140.18` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3795 | 97.9% |
| 2 | `ACK+FIN+PSH` | 39 | 1.0% |
| 3 | `ACK+PSH` | 30 | 0.8% |
| 4 | `SYN+ECE+CWR` | 8 | 0.2% |
| 5 | `ACK+FIN` | 5 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4365 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `170.51.241.171` -> `51531` | 8 | 0.2% |
| 2 | `77.239.124.127` -> `23` | 6 | 0.1% |
| 3 | `216.180.246.226` -> `8080` | 6 | 0.1% |
| 4 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 5 | `194.28.89.218` -> `5038` | 5 | 0.1% |
| 6 | `66.132.172.176` -> `33544` | 5 | 0.1% |
| 7 | `43.169.65.10` -> `51588` | 5 | 0.1% |
| 8 | `151.101.218.13` -> `54751` | 5 | 0.1% |
| 9 | `151.101.218.13` -> `54793` | 5 | 0.1% |
| 10 | `185.218.86.25` -> `3000` | 4 | 0.1% |
| 11 | `187.108.1.142` -> `5038` | 4 | 0.1% |
| 12 | `181.90.153.200` -> `22` | 4 | 0.1% |
| 13 | `77.239.124.127` -> `2323` | 4 | 0.1% |
| 14 | `47.114.57.2` -> `2222` | 4 | 0.1% |
| 15 | `186.123.1.125` -> `1433` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-15 04:00:00:00 | 134 | 3.1% |
| 2026-09-15 05:00:00:00 | 180 | 4.1% |
| 2026-09-15 06:00:00:00 | 180 | 4.1% |
| 2026-09-15 07:00:00:00 | 181 | 4.1% |
| 2026-09-15 08:00:00:00 | 181 | 4.1% |
| 2026-09-15 09:00:00:00 | 179 | 4.1% |
| 2026-09-15 10:00:00:00 | 176 | 4.0% |
| 2026-09-15 11:00:00:00 | 185 | 4.2% |
| 2026-09-15 12:00:00:00 | 177 | 4.1% |
| 2026-09-15 13:00:00:00 | 183 | 4.2% |
| 2026-09-15 14:00:00:00 | 196 | 4.5% |
| 2026-09-15 15:00:00:00 | 178 | 4.1% |
| 2026-09-15 16:00:00:00 | 181 | 4.1% |
| 2026-09-15 17:00:00:00 | 181 | 4.1% |
| 2026-09-15 18:00:00:00 | 177 | 4.1% |
| 2026-09-15 19:00:00:00 | 182 | 4.2% |
| 2026-09-15 20:00:00:00 | 181 | 4.1% |
| 2026-09-15 21:00:00:00 | 197 | 4.5% |
| 2026-09-15 22:00:00:00 | 190 | 4.4% |
| 2026-09-15 23:00:00:00 | 179 | 4.1% |
| 2026-09-16 00:00:00:00 | 182 | 4.2% |
| 2026-09-16 01:00:00:00 | 179 | 4.1% |
| 2026-09-16 02:00:00:00 | 181 | 4.1% |
| 2026-09-16 03:00:00:00 | 178 | 4.1% |
| 2026-09-16 04:00:00:00 | 47 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 126 | 60.9% |
| 2 | Buenos Aires, Argentina | 30 | 14.5% |
| 3 | Dublin, United States | 14 | 6.8% |
| 4 | Paris, France | 13 | 6.3% |
| 5 | Panama City, Panama | 12 | 5.8% |
| 6 | Amsterdam, The Netherlands | 12 | 5.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 17 | 8.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 2 | `85.217.140.23` | 16 | 7.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 3 | `85.217.140.33` | 15 | 7.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 4 | `85.217.140.3` | 15 | 7.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `85.217.140.19` | 15 | 7.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `18.217.208.51` | 14 | 6.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `85.217.140.27` | 14 | 6.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.28` | 13 | 6.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.30` | 13 | 6.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.22` | 13 | 6.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.1` | 13 | 6.3% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 12 | `170.51.241.171` | 13 | 6.3% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 13 | `141.98.83.48` | 12 | 5.8% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 14 | `77.239.124.127` | 12 | 5.8% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |
| 15 | `85.217.140.18` | 12 | 5.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 17 | 39.5% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `18.217.208.51` | 14 | 32.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `141.98.83.48` | 12 | 27.9% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
