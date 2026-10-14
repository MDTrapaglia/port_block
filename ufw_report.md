# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4429
- Unique source IPs: 2400
- Unique countries/cities (24h): 306
- Unique destination ports: 2624

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 155 | 3.5% |
| 2 | `22` | 107 | 2.4% |
| 3 | `8080` | 42 | 0.9% |
| 4 | `3389` | 35 | 0.8% |
| 5 | `53` | 32 | 0.7% |
| 6 | `5432` | 27 | 0.6% |
| 7 | `1433` | 23 | 0.5% |
| 8 | `5060` | 22 | 0.5% |
| 9 | `1723` | 20 | 0.5% |
| 10 | `3306` | 19 | 0.4% |
| 11 | `81` | 19 | 0.4% |
| 12 | `1900` | 18 | 0.4% |
| 13 | `389` | 18 | 0.4% |
| 14 | `8888` | 18 | 0.4% |
| 15 | `8443` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4072 | 91.9% |
| 2 | `UDP` | 350 | 7.9% |
| 3 | `47` | 6 | 0.1% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.166` | 84 | 1.9% |
| 2 | `122.191.96.78` | 60 | 1.4% |
| 3 | `151.101.218.13` | 36 | 0.8% |
| 4 | `216.180.246.190` | 28 | 0.6% |
| 5 | `45.198.224.125` | 18 | 0.4% |
| 6 | `85.217.140.23` | 18 | 0.4% |
| 7 | `85.217.140.2` | 17 | 0.4% |
| 8 | `85.217.140.5` | 17 | 0.4% |
| 9 | `85.217.140.27` | 16 | 0.4% |
| 10 | `91.231.89.224` | 15 | 0.3% |
| 11 | `85.217.140.29` | 15 | 0.3% |
| 12 | `79.124.40.162` | 15 | 0.3% |
| 13 | `85.217.140.34` | 14 | 0.3% |
| 14 | `91.230.168.190` | 14 | 0.3% |
| 15 | `217.165.62.74` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3930 | 96.5% |
| 2 | `ACK+FIN+PSH` | 100 | 2.5% |
| 3 | `ACK+PSH` | 25 | 0.6% |
| 4 | `ACK+FIN` | 10 | 0.2% |
| 5 | `SYN+ECE+CWR` | 7 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4429 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `217.165.62.74` -> `23` | 14 | 0.3% |
| 2 | `34.187.120.60` -> `5432` | 11 | 0.2% |
| 3 | `151.101.218.13` -> `3349` | 9 | 0.2% |
| 4 | `216.180.246.166` -> `50101` | 9 | 0.2% |
| 5 | `216.180.246.166` -> `50103` | 8 | 0.2% |
| 6 | `216.180.246.166` -> `50580` | 8 | 0.2% |
| 7 | `45.198.224.125` -> `8080` | 7 | 0.2% |
| 8 | `45.198.224.124` -> `81` | 7 | 0.2% |
| 9 | `45.205.1.160` -> `6036` | 7 | 0.2% |
| 10 | `178.20.210.152` -> `1723` | 7 | 0.2% |
| 11 | `151.101.218.13` -> `5047` | 7 | 0.2% |
| 12 | `2.23.164.81` -> `50770` | 7 | 0.2% |
| 13 | `216.180.246.166` -> `50113` | 7 | 0.2% |
| 14 | `216.180.246.166` -> `50300` | 7 | 0.2% |
| 15 | `45.205.1.163` -> `17000` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-13 04:00:00:00 | 133 | 3.0% |
| 2026-10-13 05:00:00:00 | 181 | 4.1% |
| 2026-10-13 06:00:00:00 | 178 | 4.0% |
| 2026-10-13 07:00:00:00 | 183 | 4.1% |
| 2026-10-13 08:00:00:00 | 180 | 4.1% |
| 2026-10-13 09:00:00:00 | 180 | 4.1% |
| 2026-10-13 10:00:00:00 | 179 | 4.0% |
| 2026-10-13 11:00:00:00 | 199 | 4.5% |
| 2026-10-13 12:00:00:00 | 188 | 4.2% |
| 2026-10-13 13:00:00:00 | 179 | 4.0% |
| 2026-10-13 14:00:00:00 | 181 | 4.1% |
| 2026-10-13 15:00:00:00 | 180 | 4.1% |
| 2026-10-13 16:00:00:00 | 191 | 4.3% |
| 2026-10-13 17:00:00:00 | 190 | 4.3% |
| 2026-10-13 18:00:00:00 | 209 | 4.7% |
| 2026-10-13 19:00:00:00 | 181 | 4.1% |
| 2026-10-13 20:00:00:00 | 179 | 4.0% |
| 2026-10-13 21:00:00:00 | 194 | 4.4% |
| 2026-10-13 22:00:00:00 | 182 | 4.1% |
| 2026-10-13 23:00:00:00 | 196 | 4.4% |
| 2026-10-14 00:00:00:00 | 180 | 4.1% |
| 2026-10-14 01:00:00:00 | 180 | 4.1% |
| 2026-10-14 02:00:00:00 | 182 | 4.1% |
| 2026-10-14 03:00:00:00 | 180 | 4.1% |
| 2026-10-14 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 112 | 29.4% |
| 2 | Gravelines, France | 112 | 29.4% |
| 3 | Wuhan, China | 60 | 15.7% |
| 4 | Buenos Aires, Argentina | 36 | 9.4% |
| 5 | Stockholm, Sweden | 18 | 4.7% |
| 6 | Sopot, Bulgaria | 15 | 3.9% |
| 7 | Hillsboro, United States | 14 | 3.7% |
| 8 | Dubai, United Arab Emirates | 14 | 3.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.166` | 84 | 22.0% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `122.191.96.78` | 60 | 15.7% | China / Hubei / Wuhan / China Unicom Hubei Province Network | No apparent signal |
| 3 | `151.101.218.13` | 36 | 9.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `216.180.246.190` | 28 | 7.3% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 5 | `45.198.224.125` | 18 | 4.7% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 6 | `85.217.140.23` | 18 | 4.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.2` | 17 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.5` | 17 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.27` | 16 | 4.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `91.231.89.224` | 15 | 3.9% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 11 | `85.217.140.29` | 15 | 3.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `79.124.40.162` | 15 | 3.9% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 13 | `85.217.140.34` | 14 | 3.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `91.230.168.190` | 14 | 3.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 15 | `217.165.62.74` | 14 | 3.7% | United Arab Emirates / Dubai / Dubai / Emirates Telecommunications Corporation | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.166` | 84 | 56.8% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `151.101.218.13` | 36 | 24.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `216.180.246.190` | 28 | 18.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
