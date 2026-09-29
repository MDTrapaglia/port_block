# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4437
- Unique source IPs: 2362
- Unique countries/cities (24h): 305
- Unique destination ports: 2446

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 146 | 3.3% |
| 2 | `22` | 98 | 2.2% |
| 3 | `53` | 42 | 0.9% |
| 4 | `34567` | 33 | 0.7% |
| 5 | `3389` | 31 | 0.7% |
| 6 | `6036` | 26 | 0.6% |
| 7 | `5060` | 26 | 0.6% |
| 8 | `8443` | 25 | 0.6% |
| 9 | `123` | 23 | 0.5% |
| 10 | `8080` | 22 | 0.5% |
| 11 | `17001` | 20 | 0.5% |
| 12 | `1433` | 20 | 0.5% |
| 13 | `27017` | 18 | 0.4% |
| 14 | `161` | 16 | 0.4% |
| 15 | `5432` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4020 | 90.6% |
| 2 | `UDP` | 406 | 9.2% |
| 3 | `47` | 10 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.152` | 97 | 2.2% |
| 2 | `151.101.218.13` | 27 | 0.6% |
| 3 | `85.217.140.7` | 21 | 0.5% |
| 4 | `85.217.140.35` | 20 | 0.5% |
| 5 | `205.237.105.190` | 19 | 0.4% |
| 6 | `205.237.106.81` | 17 | 0.4% |
| 7 | `85.217.140.5` | 17 | 0.4% |
| 8 | `85.217.140.28` | 15 | 0.3% |
| 9 | `195.184.76.71` | 15 | 0.3% |
| 10 | `85.217.140.33` | 15 | 0.3% |
| 11 | `91.196.152.123` | 15 | 0.3% |
| 12 | `205.237.104.18` | 15 | 0.3% |
| 13 | `85.217.140.23` | 15 | 0.3% |
| 14 | `85.217.140.22` | 15 | 0.3% |
| 15 | `195.184.76.116` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3822 | 95.1% |
| 2 | `ACK+FIN+PSH` | 105 | 2.6% |
| 3 | `ACK+PSH` | 65 | 1.6% |
| 4 | `ACK+FIN` | 17 | 0.4% |
| 5 | `SYN+ECE+CWR` | 11 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4437 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `205.237.105.190` -> `34567` | 19 | 0.4% |
| 2 | `205.237.106.81` -> `6036` | 17 | 0.4% |
| 3 | `205.237.104.18` -> `17001` | 15 | 0.3% |
| 4 | `91.224.92.28` -> `34567` | 11 | 0.2% |
| 5 | `201.20.85.122` -> `6379` | 8 | 0.2% |
| 6 | `211.228.107.231` -> `23` | 8 | 0.2% |
| 7 | `216.180.246.152` -> `7384` | 8 | 0.2% |
| 8 | `216.180.246.152` -> `7546` | 8 | 0.2% |
| 9 | `216.180.246.152` -> `7883` | 8 | 0.2% |
| 10 | `216.180.246.152` -> `7999` | 8 | 0.2% |
| 11 | `178.20.210.152` -> `1723` | 7 | 0.2% |
| 12 | `151.101.218.13` -> `40335` | 7 | 0.2% |
| 13 | `151.101.218.13` -> `41669` | 7 | 0.2% |
| 14 | `170.51.247.34` -> `56262` | 7 | 0.2% |
| 15 | `216.180.246.152` -> `7500` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-28 04:00:00:00 | 135 | 3.0% |
| 2026-09-28 05:00:00:00 | 179 | 4.0% |
| 2026-09-28 06:00:00:00 | 180 | 4.1% |
| 2026-09-28 07:00:00:00 | 180 | 4.1% |
| 2026-09-28 08:00:00:00 | 177 | 4.0% |
| 2026-09-28 09:00:00:00 | 176 | 4.0% |
| 2026-09-28 10:00:00:00 | 176 | 4.0% |
| 2026-09-28 11:00:00:00 | 185 | 4.2% |
| 2026-09-28 12:00:00:00 | 209 | 4.7% |
| 2026-09-28 13:00:00:00 | 180 | 4.1% |
| 2026-09-28 14:00:00:00 | 180 | 4.1% |
| 2026-09-28 15:00:00:00 | 180 | 4.1% |
| 2026-09-28 16:00:00:00 | 204 | 4.6% |
| 2026-09-28 17:00:00:00 | 183 | 4.1% |
| 2026-09-28 18:00:00:00 | 186 | 4.2% |
| 2026-09-28 19:00:00:00 | 193 | 4.3% |
| 2026-09-28 20:00:00:00 | 198 | 4.5% |
| 2026-09-28 21:00:00:00 | 192 | 4.3% |
| 2026-09-28 22:00:00:00 | 179 | 4.0% |
| 2026-09-28 23:00:00:00 | 181 | 4.1% |
| 2026-09-29 00:00:00:00 | 189 | 4.3% |
| 2026-09-29 01:00:00:00 | 180 | 4.1% |
| 2026-09-29 02:00:00:00 | 179 | 4.0% |
| 2026-09-29 03:00:00:00 | 190 | 4.3% |
| 2026-09-29 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 118 | 34.9% |
| 2 | Massy, France | 97 | 28.7% |
| 3 | Paris, France | 51 | 15.1% |
| 4 | Warrenton, United States | 30 | 8.9% |
| 5 | Buenos Aires, Argentina | 27 | 8.0% |
| 6 | Roubaix, France | 15 | 4.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.152` | 97 | 28.7% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `151.101.218.13` | 27 | 8.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `85.217.140.7` | 21 | 6.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 4 | `85.217.140.35` | 20 | 5.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `205.237.105.190` | 19 | 5.6% | France / Île-de-France / Paris / ESTOXY OU | No apparent signal |
| 6 | `205.237.106.81` | 17 | 5.0% | France / Île-de-France / Paris / ESTOXY OU | No apparent signal |
| 7 | `85.217.140.5` | 17 | 5.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.28` | 15 | 4.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `195.184.76.71` | 15 | 4.4% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 10 | `85.217.140.33` | 15 | 4.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `91.196.152.123` | 15 | 4.4% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 12 | `205.237.104.18` | 15 | 4.4% | France / Île-de-France / Paris / ESTOXY OU | No apparent signal |
| 13 | `85.217.140.23` | 15 | 4.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `85.217.140.22` | 15 | 4.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `195.184.76.116` | 15 | 4.4% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.152` | 97 | 78.2% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 27 | 21.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
