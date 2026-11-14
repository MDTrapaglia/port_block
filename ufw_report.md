# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4455
- Unique source IPs: 2437
- Unique countries/cities (24h): 271
- Unique destination ports: 2673

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 105 | 2.4% |
| 2 | `22` | 87 | 2.0% |
| 3 | `8080` | 43 | 1.0% |
| 4 | `3389` | 43 | 1.0% |
| 5 | `5060` | 42 | 0.9% |
| 6 | `53` | 40 | 0.9% |
| 7 | `5900` | 31 | 0.7% |
| 8 | `1433` | 29 | 0.7% |
| 9 | `8443` | 24 | 0.5% |
| 10 | `8000` | 21 | 0.5% |
| 11 | `3306` | 20 | 0.4% |
| 12 | `161` | 20 | 0.4% |
| 13 | `2222` | 18 | 0.4% |
| 14 | `3000` | 17 | 0.4% |
| 15 | `8081` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4097 | 92.0% |
| 2 | `UDP` | 351 | 7.9% |
| 3 | `47` | 6 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `198.12.85.85` | 221 | 5.0% |
| 2 | `79.124.40.142` | 24 | 0.5% |
| 3 | `151.101.218.13` | 21 | 0.5% |
| 4 | `45.198.224.125` | 18 | 0.4% |
| 5 | `151.101.219.52` | 17 | 0.4% |
| 6 | `91.231.89.130` | 14 | 0.3% |
| 7 | `91.230.168.190` | 13 | 0.3% |
| 8 | `195.184.76.116` | 13 | 0.3% |
| 9 | `195.184.76.175` | 13 | 0.3% |
| 10 | `79.124.62.10` | 13 | 0.3% |
| 11 | `91.231.89.72` | 12 | 0.3% |
| 12 | `91.230.168.129` | 12 | 0.3% |
| 13 | `195.184.76.20` | 12 | 0.3% |
| 14 | `195.184.76.49` | 12 | 0.3% |
| 15 | `151.101.218.73` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3917 | 95.6% |
| 2 | `ACK+FIN+PSH` | 123 | 3.0% |
| 3 | `ACK+PSH` | 33 | 0.8% |
| 4 | `ACK+FIN` | 12 | 0.3% |
| 5 | `SYN+ECE+CWR` | 11 | 0.3% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4455 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `172.110.223.182` -> `5060` | 9 | 0.2% |
| 2 | `62.210.114.99` -> `3389` | 9 | 0.2% |
| 3 | `118.212.132.226` -> `22` | 8 | 0.2% |
| 4 | `45.198.224.125` -> `9090` | 7 | 0.2% |
| 5 | `151.101.217.44` -> `41120` | 7 | 0.2% |
| 6 | `91.224.92.45` -> `34567` | 7 | 0.2% |
| 7 | `100.57.46.251` -> `38864` | 7 | 0.2% |
| 8 | `187.17.224.223` -> `5038` | 6 | 0.1% |
| 9 | `45.198.224.125` -> `8081` | 6 | 0.1% |
| 10 | `170.51.241.170` -> `11075` | 6 | 0.1% |
| 11 | `87.106.120.240` -> `5060` | 6 | 0.1% |
| 12 | `151.101.218.13` -> `12673` | 6 | 0.1% |
| 13 | `151.101.218.13` -> `56270` | 6 | 0.1% |
| 14 | `77.239.124.252` -> `23` | 6 | 0.1% |
| 15 | `178.20.210.152` -> `1723` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-13 04:00:00:00 | 134 | 3.0% |
| 2026-11-13 05:00:00:00 | 180 | 4.0% |
| 2026-11-13 06:00:00:00 | 180 | 4.0% |
| 2026-11-13 07:00:00:00 | 193 | 4.3% |
| 2026-11-13 08:00:00:00 | 185 | 4.2% |
| 2026-11-13 09:00:00:00 | 181 | 4.1% |
| 2026-11-13 10:00:00:00 | 181 | 4.1% |
| 2026-11-13 11:00:00:00 | 196 | 4.4% |
| 2026-11-13 12:00:00:00 | 195 | 4.4% |
| 2026-11-13 13:00:00:00 | 182 | 4.1% |
| 2026-11-13 14:00:00:00 | 181 | 4.1% |
| 2026-11-13 15:00:00:00 | 180 | 4.0% |
| 2026-11-13 16:00:00:00 | 179 | 4.0% |
| 2026-11-13 17:00:00:00 | 192 | 4.3% |
| 2026-11-13 18:00:00:00 | 205 | 4.6% |
| 2026-11-13 19:00:00:00 | 187 | 4.2% |
| 2026-11-13 20:00:00:00 | 187 | 4.2% |
| 2026-11-13 21:00:00:00 | 178 | 4.0% |
| 2026-11-13 22:00:00:00 | 181 | 4.1% |
| 2026-11-13 23:00:00:00 | 211 | 4.7% |
| 2026-11-14 00:00:00:00 | 181 | 4.1% |
| 2026-11-14 01:00:00:00 | 180 | 4.0% |
| 2026-11-14 02:00:00:00 | 179 | 4.0% |
| 2026-11-14 03:00:00:00 | 179 | 4.0% |
| 2026-11-14 04:00:00:00 | 47 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Buffalo, United States | 221 | 51.8% |
| 2 | Warrenton, United States | 50 | 11.7% |
| 3 | Buenos Aires, Argentina | 38 | 8.9% |
| 4 | Gravelines, France | 26 | 6.1% |
| 5 | Hillsboro, United States | 25 | 5.9% |
| 6 | Sopot, Bulgaria | 24 | 5.6% |
| 7 | Stockholm, Sweden | 18 | 4.2% |
| 8 | Victoria, Seychelles | 13 | 3.0% |
| 9 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 12 | 2.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `198.12.85.85` | 221 | 51.8% | United States / New York / Buffalo / Mikhel Francis yap | No apparent signal |
| 2 | `79.124.40.142` | 24 | 5.6% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 3 | `151.101.218.13` | 21 | 4.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `45.198.224.125` | 18 | 4.2% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 5 | `151.101.219.52` | 17 | 4.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `91.231.89.130` | 14 | 3.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `91.230.168.190` | 13 | 3.0% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 8 | `195.184.76.116` | 13 | 3.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 9 | `195.184.76.175` | 13 | 3.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 10 | `79.124.62.10` | 13 | 3.0% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 11 | `91.231.89.72` | 12 | 2.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.230.168.129` | 12 | 2.8% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 13 | `195.184.76.20` | 12 | 2.8% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `195.184.76.49` | 12 | 2.8% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 15 | `151.101.218.73` | 12 | 2.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 21 | 42.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `151.101.219.52` | 17 | 34.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.73` | 12 | 24.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
