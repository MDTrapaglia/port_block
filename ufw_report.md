# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4474
- Unique source IPs: 2301
- Unique countries/cities (24h): 339
- Unique destination ports: 2637

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 114 | 2.5% |
| 2 | `22` | 99 | 2.2% |
| 3 | `8080` | 34 | 0.8% |
| 4 | `1433` | 31 | 0.7% |
| 5 | `5060` | 30 | 0.7% |
| 6 | `8443` | 28 | 0.6% |
| 7 | `3389` | 23 | 0.5% |
| 8 | `81` | 21 | 0.5% |
| 9 | `161` | 20 | 0.4% |
| 10 | `53` | 20 | 0.4% |
| 11 | `1723` | 20 | 0.4% |
| 12 | `3306` | 20 | 0.4% |
| 13 | `9200` | 19 | 0.4% |
| 14 | `8081` | 19 | 0.4% |
| 15 | `9000` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4039 | 90.3% |
| 2 | `UDP` | 427 | 9.5% |
| 3 | `47` | 7 | 0.2% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `151.101.218.13` | 50 | 1.1% |
| 2 | `108.181.20.142` | 34 | 0.8% |
| 3 | `108.181.2.247` | 29 | 0.6% |
| 4 | `216.180.246.74` | 28 | 0.6% |
| 5 | `204.76.203.219` | 22 | 0.5% |
| 6 | `85.217.140.27` | 19 | 0.4% |
| 7 | `195.184.76.175` | 17 | 0.4% |
| 8 | `108.181.9.218` | 17 | 0.4% |
| 9 | `195.184.76.20` | 17 | 0.4% |
| 10 | `91.231.89.72` | 16 | 0.4% |
| 11 | `91.231.89.104` | 16 | 0.4% |
| 12 | `195.184.76.71` | 16 | 0.4% |
| 13 | `142.93.207.96` | 16 | 0.4% |
| 14 | `91.230.168.129` | 15 | 0.3% |
| 15 | `91.231.89.130` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3829 | 94.8% |
| 2 | `ACK+FIN+PSH` | 141 | 3.5% |
| 3 | `ACK+PSH` | 45 | 1.1% |
| 4 | `ACK+FIN` | 19 | 0.5% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4474 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.198.224.124` -> `81` | 10 | 0.2% |
| 2 | `45.205.1.163` -> `17000` | 9 | 0.2% |
| 3 | `170.51.247.42` -> `36991` | 8 | 0.2% |
| 4 | `80.66.83.83` -> `5405` | 7 | 0.2% |
| 5 | `151.101.218.13` -> `38181` | 7 | 0.2% |
| 6 | `151.101.218.13` -> `41649` | 7 | 0.2% |
| 7 | `45.198.224.125` -> `8081` | 6 | 0.1% |
| 8 | `151.101.218.13` -> `61501` | 6 | 0.1% |
| 9 | `151.101.218.13` -> `37859` | 6 | 0.1% |
| 10 | `66.132.195.161` -> `587` | 6 | 0.1% |
| 11 | `184.31.2.82` -> `40323` | 6 | 0.1% |
| 12 | `216.180.246.74` -> `55443` | 6 | 0.1% |
| 13 | `216.180.246.74` -> `55555` | 6 | 0.1% |
| 14 | `45.205.1.160` -> `6036` | 5 | 0.1% |
| 15 | `201.20.85.122` -> `6379` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-07 04:00:00:00 | 135 | 3.0% |
| 2026-10-07 05:00:00:00 | 179 | 4.0% |
| 2026-10-07 06:00:00:00 | 181 | 4.0% |
| 2026-10-07 07:00:00:00 | 180 | 4.0% |
| 2026-10-07 08:00:00:00 | 180 | 4.0% |
| 2026-10-07 09:00:00:00 | 180 | 4.0% |
| 2026-10-07 10:00:00:00 | 176 | 3.9% |
| 2026-10-07 11:00:00:00 | 180 | 4.0% |
| 2026-10-07 12:00:00:00 | 178 | 4.0% |
| 2026-10-07 13:00:00:00 | 180 | 4.0% |
| 2026-10-07 14:00:00:00 | 210 | 4.7% |
| 2026-10-07 15:00:00:00 | 207 | 4.6% |
| 2026-10-07 16:00:00:00 | 227 | 5.1% |
| 2026-10-07 17:00:00:00 | 180 | 4.0% |
| 2026-10-07 18:00:00:00 | 179 | 4.0% |
| 2026-10-07 19:00:00:00 | 196 | 4.4% |
| 2026-10-07 20:00:00:00 | 177 | 4.0% |
| 2026-10-07 21:00:00:00 | 183 | 4.1% |
| 2026-10-07 22:00:00:00 | 182 | 4.1% |
| 2026-10-07 23:00:00:00 | 180 | 4.0% |
| 2026-10-08 00:00:00:00 | 209 | 4.7% |
| 2026-10-08 01:00:00:00 | 179 | 4.0% |
| 2026-10-08 02:00:00:00 | 179 | 4.0% |
| 2026-10-08 03:00:00:00 | 191 | 4.3% |
| 2026-10-08 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Los Angeles, United States | 80 | 24.5% |
| 2 | Gravelines, France | 66 | 20.2% |
| 3 | Buenos Aires, Argentina | 50 | 15.3% |
| 4 | Warrenton, United States | 50 | 15.3% |
| 5 | Massy, France | 28 | 8.6% |
| 6 | Eygelshoven, Netherlands | 22 | 6.7% |
| 7 | North Bergen, United States | 16 | 4.9% |
| 8 | Hillsboro, United States | 15 | 4.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 50 | 15.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 2 | `108.181.20.142` | 34 | 10.4% | United States / California / Los Angeles / TELUS Communications Inc. | Hosting/Cloud (psychz) |
| 3 | `108.181.2.247` | 29 | 8.9% | United States / California / Los Angeles / TELUS Communications Inc. | Hosting/Cloud (psychz) |
| 4 | `216.180.246.74` | 28 | 8.6% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 5 | `204.76.203.219` | 22 | 6.7% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 6 | `85.217.140.27` | 19 | 5.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `195.184.76.175` | 17 | 5.2% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 8 | `108.181.9.218` | 17 | 5.2% | United States / California / Los Angeles / TELUS Communications Inc. | Hosting/Cloud (psychz) |
| 9 | `195.184.76.20` | 17 | 5.2% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 10 | `91.231.89.72` | 16 | 4.9% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 11 | `91.231.89.104` | 16 | 4.9% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `195.184.76.71` | 16 | 4.9% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 13 | `142.93.207.96` | 16 | 4.9% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 14 | `91.230.168.129` | 15 | 4.6% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 15 | `91.231.89.130` | 15 | 4.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 50 | 28.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `108.181.20.142` | 34 | 19.5% | Hosting/Cloud (psychz) | United States / California / Los Angeles / TELUS Communications Inc. |
| 3 | `108.181.2.247` | 29 | 16.7% | Hosting/Cloud (psychz) | United States / California / Los Angeles / TELUS Communications Inc. |
| 4 | `216.180.246.74` | 28 | 16.1% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 5 | `108.181.9.218` | 17 | 9.8% | Hosting/Cloud (psychz) | United States / California / Los Angeles / TELUS Communications Inc. |
| 6 | `142.93.207.96` | 16 | 9.2% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
