# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4458
- Unique source IPs: 2371
- Unique countries/cities (24h): 395
- Unique destination ports: 2390

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 373 | 8.4% |
| 2 | `22` | 88 | 2.0% |
| 3 | `8080` | 32 | 0.7% |
| 4 | `53` | 30 | 0.7% |
| 5 | `1433` | 29 | 0.7% |
| 6 | `3389` | 26 | 0.6% |
| 7 | `8443` | 22 | 0.5% |
| 8 | `123` | 21 | 0.5% |
| 9 | `5060` | 20 | 0.4% |
| 10 | `3306` | 16 | 0.4% |
| 11 | `2000` | 15 | 0.3% |
| 12 | `9443` | 14 | 0.3% |
| 13 | `unknown` | 14 | 0.3% |
| 14 | `1900` | 14 | 0.3% |
| 15 | `12345` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4010 | 90.0% |
| 2 | `UDP` | 434 | 9.7% |
| 3 | `47` | 12 | 0.3% |
| 4 | `41` | 1 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.49` | 175 | 3.9% |
| 2 | `92.204.138.142` | 93 | 2.1% |
| 3 | `100.8.68.220` | 78 | 1.7% |
| 4 | `103.112.69.15` | 73 | 1.6% |
| 5 | `37.112.50.180` | 62 | 1.4% |
| 6 | `151.101.218.13` | 35 | 0.8% |
| 7 | `216.180.246.241` | 23 | 0.5% |
| 8 | `82.147.84.244` | 17 | 0.4% |
| 9 | `85.217.140.22` | 13 | 0.3% |
| 10 | `151.101.218.73` | 13 | 0.3% |
| 11 | `85.217.140.7` | 12 | 0.3% |
| 12 | `85.217.149.37` | 12 | 0.3% |
| 13 | `85.217.140.30` | 12 | 0.3% |
| 14 | `77.239.124.127` | 11 | 0.2% |
| 15 | `85.217.140.27` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3819 | 95.2% |
| 2 | `ACK+FIN+PSH` | 108 | 2.7% |
| 3 | `ACK+PSH` | 45 | 1.1% |
| 4 | `ACK+FIN` | 19 | 0.5% |
| 5 | `ACK+RST` | 10 | 0.2% |
| 6 | `ACK` | 5 | 0.1% |
| 7 | `SYN+ECE+CWR` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4457 | 100.0% |
| 2 | `wlan0` | 1 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `92.204.138.142` -> `23` | 93 | 2.1% |
| 2 | `37.112.50.180` -> `23` | 62 | 1.4% |
| 3 | `216.180.246.241` -> `65432` | 10 | 0.2% |
| 4 | `216.180.246.49` -> `11001` | 9 | 0.2% |
| 5 | `216.180.246.49` -> `11111` | 9 | 0.2% |
| 6 | `216.180.246.49` -> `11323` | 9 | 0.2% |
| 7 | `216.180.246.49` -> `12088` | 9 | 0.2% |
| 8 | `216.180.246.49` -> `12345` | 9 | 0.2% |
| 9 | `216.180.246.49` -> `12999` | 9 | 0.2% |
| 10 | `216.180.246.49` -> `10399` | 8 | 0.2% |
| 11 | `216.180.246.49` -> `11000` | 8 | 0.2% |
| 12 | `216.180.246.49` -> `11005` | 8 | 0.2% |
| 13 | `216.180.246.49` -> `12233` | 8 | 0.2% |
| 14 | `216.180.246.241` -> `65527` | 8 | 0.2% |
| 15 | `151.101.218.13` -> `49868` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-09 04:00:00:00 | 134 | 3.0% |
| 2026-09-09 05:00:00:00 | 178 | 4.0% |
| 2026-09-09 06:00:00:00 | 178 | 4.0% |
| 2026-09-09 07:00:00:00 | 184 | 4.1% |
| 2026-09-09 08:00:00:00 | 180 | 4.0% |
| 2026-09-09 09:00:00:00 | 179 | 4.0% |
| 2026-09-09 10:00:00:00 | 208 | 4.7% |
| 2026-09-09 11:00:00:00 | 179 | 4.0% |
| 2026-09-09 12:00:00:00 | 181 | 4.1% |
| 2026-09-09 13:00:00:00 | 196 | 4.4% |
| 2026-09-09 14:00:00:00 | 179 | 4.0% |
| 2026-09-09 15:00:00:00 | 182 | 4.1% |
| 2026-09-09 16:00:00:00 | 180 | 4.0% |
| 2026-09-09 17:00:00:00 | 180 | 4.0% |
| 2026-09-09 18:00:00:00 | 191 | 4.3% |
| 2026-09-09 19:00:00:00 | 187 | 4.2% |
| 2026-09-09 20:00:00:00 | 183 | 4.1% |
| 2026-09-09 21:00:00:00 | 204 | 4.6% |
| 2026-09-09 22:00:00:00 | 211 | 4.7% |
| 2026-09-09 23:00:00:00 | 199 | 4.5% |
| 2026-09-10 00:00:00:00 | 180 | 4.0% |
| 2026-09-10 01:00:00:00 | 179 | 4.0% |
| 2026-09-10 02:00:00:00 | 179 | 4.0% |
| 2026-09-10 03:00:00:00 | 181 | 4.1% |
| 2026-09-10 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 198 | 30.9% |
| 2 | Warrenton, United States | 93 | 14.5% |
| 3 | Amsterdam, The Netherlands | 84 | 13.1% |
| 4 | Jersey City, United States | 78 | 12.2% |
| 5 | Bryansk, Russia | 62 | 9.7% |
| 6 | Gravelines, France | 48 | 7.5% |
| 7 | Buenos Aires, Argentina | 35 | 5.5% |
| 8 | Novosibirsk, Russia | 17 | 2.7% |
| 9 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 13 | 2.0% |
| 10 | Beauharnois, Canada | 12 | 1.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.49` | 175 | 27.3% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `92.204.138.142` | 93 | 14.5% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 3 | `100.8.68.220` | 78 | 12.2% | United States / New Jersey / Jersey City / Verizon Business | No apparent signal |
| 4 | `103.112.69.15` | 73 | 11.4% | The Netherlands / North Holland / Amsterdam / Retzor, Inc. | No apparent signal |
| 5 | `37.112.50.180` | 62 | 9.7% | Russia / Bryansk Oblast / Bryansk / JSC "ER-Telecom Holding" Bryansk Branch | No apparent signal |
| 6 | `151.101.218.13` | 35 | 5.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `216.180.246.241` | 23 | 3.6% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 8 | `82.147.84.244` | 17 | 2.7% | Russia / Novosibirsk Oblast / Novosibirsk / BAXET | No apparent signal |
| 9 | `85.217.140.22` | 13 | 2.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `151.101.218.73` | 13 | 2.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 11 | `85.217.140.7` | 12 | 1.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.149.37` | 12 | 1.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 13 | `85.217.140.30` | 12 | 1.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `77.239.124.127` | 11 | 1.7% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |
| 15 | `85.217.140.27` | 11 | 1.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.49` | 175 | 71.1% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 35 | 14.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `216.180.246.241` | 23 | 9.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 4 | `151.101.218.73` | 13 | 5.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
