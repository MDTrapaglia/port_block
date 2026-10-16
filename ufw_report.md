# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4423
- Unique source IPs: 2414
- Unique countries/cities (24h): 290
- Unique destination ports: 2815

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 132 | 3.0% |
| 2 | `22` | 74 | 1.7% |
| 3 | `8080` | 39 | 0.9% |
| 4 | `5060` | 37 | 0.8% |
| 5 | `3389` | 35 | 0.8% |
| 6 | `1433` | 32 | 0.7% |
| 7 | `53` | 24 | 0.5% |
| 8 | `8443` | 23 | 0.5% |
| 9 | `3306` | 20 | 0.5% |
| 10 | `8000` | 20 | 0.5% |
| 11 | `123` | 19 | 0.4% |
| 12 | `8081` | 19 | 0.4% |
| 13 | `161` | 16 | 0.4% |
| 14 | `21` | 15 | 0.3% |
| 15 | `1723` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4080 | 92.2% |
| 2 | `UDP` | 331 | 7.5% |
| 3 | `47` | 9 | 0.2% |
| 4 | `41` | 2 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.235.14.2` | 30 | 0.7% |
| 2 | `151.101.218.73` | 24 | 0.5% |
| 3 | `216.180.246.45` | 23 | 0.5% |
| 4 | `45.198.224.125` | 18 | 0.4% |
| 5 | `85.217.149.37` | 17 | 0.4% |
| 6 | `85.217.140.5` | 17 | 0.4% |
| 7 | `85.217.140.6` | 16 | 0.4% |
| 8 | `91.196.152.123` | 16 | 0.4% |
| 9 | `91.196.152.35` | 16 | 0.4% |
| 10 | `94.183.174.95` | 15 | 0.3% |
| 11 | `91.231.89.0` | 14 | 0.3% |
| 12 | `91.230.168.190` | 14 | 0.3% |
| 13 | `91.231.89.150` | 14 | 0.3% |
| 14 | `85.217.140.28` | 14 | 0.3% |
| 15 | `79.124.59.106` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3943 | 96.6% |
| 2 | `ACK+FIN+PSH` | 87 | 2.1% |
| 3 | `ACK+PSH` | 28 | 0.7% |
| 4 | `ACK+FIN` | 11 | 0.3% |
| 5 | `SYN+ECE+CWR` | 7 | 0.2% |
| 6 | `ACK` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4422 | 100.0% |
| 2 | `wlan0` | 1 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.205.1.163` -> `17000` | 11 | 0.2% |
| 2 | `62.210.114.99` -> `3389` | 9 | 0.2% |
| 3 | `151.101.218.73` -> `15553` | 8 | 0.2% |
| 4 | `45.198.224.125` -> `8081` | 7 | 0.2% |
| 5 | `45.198.224.124` -> `81` | 7 | 0.2% |
| 6 | `45.205.1.160` -> `6036` | 7 | 0.2% |
| 7 | `45.198.224.125` -> `8080` | 7 | 0.2% |
| 8 | `216.180.246.129` -> `161` | 7 | 0.2% |
| 9 | `216.180.246.45` -> `30303` | 7 | 0.2% |
| 10 | `151.101.218.73` -> `58560` | 6 | 0.1% |
| 11 | `186.123.1.125` -> `1433` | 5 | 0.1% |
| 12 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 13 | `83.25.80.66` -> `23` | 5 | 0.1% |
| 14 | `66.132.172.184` -> `110` | 5 | 0.1% |
| 15 | `66.132.172.141` -> `8443` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-15 04:00:00:00 | 140 | 3.2% |
| 2026-10-15 05:00:00:00 | 179 | 4.0% |
| 2026-10-15 06:00:00:00 | 181 | 4.1% |
| 2026-10-15 07:00:00:00 | 177 | 4.0% |
| 2026-10-15 08:00:00:00 | 182 | 4.1% |
| 2026-10-15 09:00:00:00 | 181 | 4.1% |
| 2026-10-15 10:00:00:00 | 180 | 4.1% |
| 2026-10-15 11:00:00:00 | 179 | 4.0% |
| 2026-10-15 12:00:00:00 | 180 | 4.1% |
| 2026-10-15 13:00:00:00 | 181 | 4.1% |
| 2026-10-15 14:00:00:00 | 195 | 4.4% |
| 2026-10-15 15:00:00:00 | 192 | 4.3% |
| 2026-10-15 16:00:00:00 | 179 | 4.0% |
| 2026-10-15 17:00:00:00 | 179 | 4.0% |
| 2026-10-15 18:00:00:00 | 178 | 4.0% |
| 2026-10-15 19:00:00:00 | 183 | 4.1% |
| 2026-10-15 20:00:00:00 | 181 | 4.1% |
| 2026-10-15 21:00:00:00 | 198 | 4.5% |
| 2026-10-15 22:00:00:00 | 189 | 4.3% |
| 2026-10-15 23:00:00:00 | 185 | 4.2% |
| 2026-10-16 00:00:00:00 | 192 | 4.3% |
| 2026-10-16 01:00:00:00 | 191 | 4.3% |
| 2026-10-16 02:00:00:00 | 196 | 4.4% |
| 2026-10-16 03:00:00:00 | 180 | 4.1% |
| 2026-10-16 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 75 | 28.6% |
| 2 | Roubaix, France | 32 | 12.2% |
| 3 | Daule, Ecuador | 30 | 11.5% |
| 4 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 24 | 9.2% |
| 5 | Massy, France | 23 | 8.8% |
| 6 | Stockholm, Sweden | 18 | 6.9% |
| 7 | Beauharnois, Canada | 17 | 6.5% |
| 8 | Hauzenberg, Germany | 15 | 5.7% |
| 9 | Hillsboro, United States | 14 | 5.3% |
| 10 | Sopot, Bulgaria | 14 | 5.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `45.235.14.2` | 30 | 11.5% | Ecuador / Guayas / Daule / Anibal Humberto Enriquez Moncayo(Comunicate) | No apparent signal |
| 2 | `151.101.218.73` | 24 | 9.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `216.180.246.45` | 23 | 8.8% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 4 | `45.198.224.125` | 18 | 6.9% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 5 | `85.217.149.37` | 17 | 6.5% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 6 | `85.217.140.5` | 17 | 6.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.6` | 16 | 6.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `91.196.152.123` | 16 | 6.1% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 9 | `91.196.152.35` | 16 | 6.1% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 10 | `94.183.174.95` | 15 | 5.7% | Germany / Bavaria / Hauzenberg / Pfcloud UG | No apparent signal |
| 11 | `91.231.89.0` | 14 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.230.168.190` | 14 | 5.3% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 13 | `91.231.89.150` | 14 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `85.217.140.28` | 14 | 5.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `79.124.59.106` | 14 | 5.3% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.73` | 24 | 51.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `216.180.246.45` | 23 | 48.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
