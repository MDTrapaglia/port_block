# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4370
- Unique source IPs: 2379
- Unique countries/cities (24h): 294
- Unique destination ports: 2616

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 184 | 4.2% |
| 2 | `22` | 89 | 2.0% |
| 3 | `3306` | 34 | 0.8% |
| 4 | `53` | 32 | 0.7% |
| 5 | `8080` | 31 | 0.7% |
| 6 | `5060` | 28 | 0.6% |
| 7 | `3389` | 24 | 0.5% |
| 8 | `8443` | 23 | 0.5% |
| 9 | `1433` | 20 | 0.5% |
| 10 | `123` | 17 | 0.4% |
| 11 | `2222` | 17 | 0.4% |
| 12 | `8081` | 17 | 0.4% |
| 13 | `1900` | 15 | 0.3% |
| 14 | `161` | 15 | 0.3% |
| 15 | `81` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3960 | 90.6% |
| 2 | `UDP` | 401 | 9.2% |
| 3 | `47` | 8 | 0.2% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.74` | 140 | 3.2% |
| 2 | `92.204.138.58` | 89 | 2.0% |
| 3 | `208.87.242.93` | 23 | 0.5% |
| 4 | `108.59.6.97` | 18 | 0.4% |
| 5 | `79.124.59.106` | 16 | 0.4% |
| 6 | `85.217.140.1` | 16 | 0.4% |
| 7 | `91.231.89.224` | 15 | 0.3% |
| 8 | `195.184.76.49` | 15 | 0.3% |
| 9 | `91.231.89.10` | 15 | 0.3% |
| 10 | `195.184.76.71` | 15 | 0.3% |
| 11 | `91.231.89.72` | 14 | 0.3% |
| 12 | `91.231.89.104` | 14 | 0.3% |
| 13 | `195.184.76.62` | 13 | 0.3% |
| 14 | `91.231.89.215` | 13 | 0.3% |
| 15 | `85.217.140.30` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3863 | 97.6% |
| 2 | `ACK+FIN+PSH` | 48 | 1.2% |
| 3 | `ACK+PSH` | 38 | 1.0% |
| 4 | `SYN+ECE+CWR` | 7 | 0.2% |
| 5 | `ACK` | 3 | 0.1% |
| 6 | `ACK+FIN` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4370 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `92.204.138.58` -> `23` | 89 | 2.0% |
| 2 | `216.180.246.74` -> `57432` | 10 | 0.2% |
| 3 | `216.180.246.74` -> `60023` | 10 | 0.2% |
| 4 | `216.180.246.74` -> `60001` | 9 | 0.2% |
| 5 | `45.205.1.160` -> `6036` | 8 | 0.2% |
| 6 | `216.180.246.74` -> `58000` | 8 | 0.2% |
| 7 | `45.198.224.124` -> `81` | 8 | 0.2% |
| 8 | `216.180.246.74` -> `58167` | 8 | 0.2% |
| 9 | `216.180.246.74` -> `58603` | 8 | 0.2% |
| 10 | `216.180.246.74` -> `60006` | 8 | 0.2% |
| 11 | `216.180.246.74` -> `60303` | 8 | 0.2% |
| 12 | `45.205.1.163` -> `17000` | 7 | 0.2% |
| 13 | `216.180.246.74` -> `56575` | 7 | 0.2% |
| 14 | `216.180.246.74` -> `58443` | 7 | 0.2% |
| 15 | `216.180.246.74` -> `60002` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-08 04:00:00:00 | 135 | 3.1% |
| 2026-10-08 05:00:00:00 | 180 | 4.1% |
| 2026-10-08 06:00:00:00 | 180 | 4.1% |
| 2026-10-08 07:00:00:00 | 178 | 4.1% |
| 2026-10-08 08:00:00:00 | 182 | 4.2% |
| 2026-10-08 09:00:00:00 | 180 | 4.1% |
| 2026-10-08 10:00:00:00 | 180 | 4.1% |
| 2026-10-08 11:00:00:00 | 180 | 4.1% |
| 2026-10-08 12:00:00:00 | 180 | 4.1% |
| 2026-10-08 13:00:00:00 | 179 | 4.1% |
| 2026-10-08 14:00:00:00 | 188 | 4.3% |
| 2026-10-08 15:00:00:00 | 181 | 4.1% |
| 2026-10-08 16:00:00:00 | 180 | 4.1% |
| 2026-10-08 17:00:00:00 | 180 | 4.1% |
| 2026-10-08 18:00:00:00 | 177 | 4.1% |
| 2026-10-08 19:00:00:00 | 180 | 4.1% |
| 2026-10-08 20:00:00:00 | 187 | 4.3% |
| 2026-10-08 21:00:00:00 | 180 | 4.1% |
| 2026-10-08 22:00:00:00 | 191 | 4.4% |
| 2026-10-08 23:00:00:00 | 182 | 4.2% |
| 2026-10-09 00:00:00:00 | 180 | 4.1% |
| 2026-10-09 01:00:00:00 | 189 | 4.3% |
| 2026-10-09 02:00:00:00 | 190 | 4.3% |
| 2026-10-09 03:00:00:00 | 183 | 4.2% |
| 2026-10-09 04:00:00:00 | 48 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 140 | 32.6% |
| 2 | Warrenton, United States | 132 | 30.8% |
| 3 | Gravelines, France | 84 | 19.6% |
| 4 | Los Angeles, United States | 23 | 5.4% |
| 5 | Ashburn, United States | 18 | 4.2% |
| 6 | Sopot, Bulgaria | 16 | 3.7% |
| 7 | Paris, France | 16 | 3.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.74` | 140 | 32.6% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `92.204.138.58` | 89 | 20.7% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 3 | `208.87.242.93` | 23 | 5.4% | United States / California / Los Angeles / Psychz Networks | Hosting/Cloud (psychz) |
| 4 | `108.59.6.97` | 18 | 4.2% | United States / Virginia / Ashburn / Leaseweb USA, Inc. | Hosting/Cloud (leaseweb) |
| 5 | `79.124.59.106` | 16 | 3.7% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 6 | `85.217.140.1` | 16 | 3.7% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 7 | `91.231.89.224` | 15 | 3.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 8 | `195.184.76.49` | 15 | 3.5% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 9 | `91.231.89.10` | 15 | 3.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `195.184.76.71` | 15 | 3.5% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 11 | `91.231.89.72` | 14 | 3.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.104` | 14 | 3.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `195.184.76.62` | 13 | 3.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `91.231.89.215` | 13 | 3.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `85.217.140.30` | 13 | 3.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.74` | 140 | 77.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `208.87.242.93` | 23 | 12.7% | Hosting/Cloud (psychz) | United States / California / Los Angeles / Psychz Networks |
| 3 | `108.59.6.97` | 18 | 9.9% | Hosting/Cloud (leaseweb) | United States / Virginia / Ashburn / Leaseweb USA, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
