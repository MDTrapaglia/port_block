# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4373
- Unique source IPs: 2627
- Unique countries/cities (24h): 403
- Unique destination ports: 2263

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 280 | 6.4% |
| 2 | `7680` | 115 | 2.6% |
| 3 | `22` | 79 | 1.8% |
| 4 | `8080` | 42 | 1.0% |
| 5 | `1433` | 40 | 0.9% |
| 6 | `3389` | 37 | 0.8% |
| 7 | `5060` | 32 | 0.7% |
| 8 | `8081` | 26 | 0.6% |
| 9 | `8443` | 25 | 0.6% |
| 10 | `8083` | 21 | 0.5% |
| 11 | `2222` | 20 | 0.5% |
| 12 | `53` | 20 | 0.5% |
| 13 | `8000` | 19 | 0.4% |
| 14 | `389` | 18 | 0.4% |
| 15 | `3306` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4020 | 91.9% |
| 2 | `UDP` | 347 | 7.9% |
| 3 | `132` | 3 | 0.1% |
| 4 | `47` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.17` | 156 | 3.6% |
| 2 | `86.54.28.190` | 25 | 0.6% |
| 3 | `208.87.243.191` | 21 | 0.5% |
| 4 | `79.124.40.186` | 20 | 0.5% |
| 5 | `151.101.218.13` | 17 | 0.4% |
| 6 | `24.7.116.142` | 17 | 0.4% |
| 7 | `74.244.111.200` | 14 | 0.3% |
| 8 | `91.231.89.215` | 13 | 0.3% |
| 9 | `73.15.217.19` | 13 | 0.3% |
| 10 | `173.34.33.75` | 13 | 0.3% |
| 11 | `79.124.59.82` | 12 | 0.3% |
| 12 | `3.83.245.221` | 12 | 0.3% |
| 13 | `195.184.76.20` | 11 | 0.3% |
| 14 | `18.119.209.50` | 11 | 0.3% |
| 15 | `45.198.224.125` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3924 | 97.6% |
| 2 | `ACK+FIN+PSH` | 39 | 1.0% |
| 3 | `ACK+PSH` | 32 | 0.8% |
| 4 | `ACK+FIN` | 14 | 0.3% |
| 5 | `SYN+ECE+CWR` | 7 | 0.2% |
| 6 | `ACK` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4373 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `24.7.116.142` -> `7680` | 17 | 0.4% |
| 2 | `74.244.111.200` -> `7680` | 14 | 0.3% |
| 3 | `73.15.217.19` -> `7680` | 13 | 0.3% |
| 4 | `173.34.33.75` -> `7680` | 13 | 0.3% |
| 5 | `46.109.32.249` -> `23` | 10 | 0.2% |
| 6 | `216.180.246.17` -> `8040` | 8 | 0.2% |
| 7 | `216.180.246.17` -> `8041` | 8 | 0.2% |
| 8 | `216.180.246.17` -> `8075` | 8 | 0.2% |
| 9 | `216.180.246.17` -> `8099` | 8 | 0.2% |
| 10 | `103.30.11.172` -> `22` | 7 | 0.2% |
| 11 | `216.180.246.17` -> `8080` | 7 | 0.2% |
| 12 | `216.180.246.17` -> `8081` | 7 | 0.2% |
| 13 | `216.180.246.17` -> `8083` | 7 | 0.2% |
| 14 | `216.180.246.17` -> `8086` | 7 | 0.2% |
| 15 | `35.172.2.224` -> `37261` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-26 04:00:00:00 | 134 | 3.1% |
| 2026-11-26 05:00:00:00 | 181 | 4.1% |
| 2026-11-26 06:00:00:00 | 179 | 4.1% |
| 2026-11-26 07:00:00:00 | 181 | 4.1% |
| 2026-11-26 08:00:00:00 | 180 | 4.1% |
| 2026-11-26 09:00:00:00 | 181 | 4.1% |
| 2026-11-26 10:00:00:00 | 179 | 4.1% |
| 2026-11-26 11:00:00:00 | 181 | 4.1% |
| 2026-11-26 12:00:00:00 | 180 | 4.1% |
| 2026-11-26 13:00:00:00 | 178 | 4.1% |
| 2026-11-26 14:00:00:00 | 186 | 4.3% |
| 2026-11-26 15:00:00:00 | 180 | 4.1% |
| 2026-11-26 16:00:00:00 | 179 | 4.1% |
| 2026-11-26 17:00:00:00 | 181 | 4.1% |
| 2026-11-26 18:00:00:00 | 179 | 4.1% |
| 2026-11-26 19:00:00:00 | 189 | 4.3% |
| 2026-11-26 20:00:00:00 | 178 | 4.1% |
| 2026-11-26 21:00:00:00 | 191 | 4.4% |
| 2026-11-26 22:00:00:00 | 181 | 4.1% |
| 2026-11-26 23:00:00:00 | 179 | 4.1% |
| 2026-11-27 00:00:00:00 | 180 | 4.1% |
| 2026-11-27 01:00:00:00 | 196 | 4.5% |
| 2026-11-27 02:00:00:00 | 186 | 4.3% |
| 2026-11-27 03:00:00:00 | 189 | 4.3% |
| 2026-11-27 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 156 | 42.6% |
| 2 | Sopot, Bulgaria | 32 | 8.7% |
| 3 | Amsterdam, The Netherlands | 25 | 6.8% |
| 4 | Los Angeles, United States | 21 | 5.7% |
| 5 | Buenos Aires, Argentina | 17 | 4.6% |
| 6 | Mountain View, United States | 17 | 4.6% |
| 7 | Boise, United States | 14 | 3.8% |
| 8 | Gravelines, France | 13 | 3.6% |
| 9 | San Jose, United States | 13 | 3.6% |
| 10 | Stittsville, Canada | 13 | 3.6% |
| 11 | Ashburn, United States | 12 | 3.3% |
| 12 | Warrenton, United States | 11 | 3.0% |
| 13 | Dublin, United States | 11 | 3.0% |
| 14 | Stockholm, Sweden | 11 | 3.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.17` | 156 | 42.6% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `86.54.28.190` | 25 | 6.8% | The Netherlands / North Holland / Amsterdam / Black HOST Ltd | No apparent signal |
| 3 | `208.87.243.191` | 21 | 5.7% | United States / California / Los Angeles / Psychz Networks | Hosting/Cloud (psychz) |
| 4 | `79.124.40.186` | 20 | 5.5% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 5 | `151.101.218.13` | 17 | 4.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `24.7.116.142` | 17 | 4.6% | United States / California / Mountain View / Comcast Cable Communications | No apparent signal |
| 7 | `74.244.111.200` | 14 | 3.8% | United States / Idaho / Boise / SpaceX Starlink | No apparent signal |
| 8 | `91.231.89.215` | 13 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `73.15.217.19` | 13 | 3.6% | United States / California / San Jose / Comcast IP Services, L.L.C. | No apparent signal |
| 10 | `173.34.33.75` | 13 | 3.6% | Canada / Ontario / Stittsville / Rogers Cable Inc. BLOOR | No apparent signal |
| 11 | `79.124.59.82` | 12 | 3.3% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 12 | `3.83.245.221` | 12 | 3.3% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `195.184.76.20` | 11 | 3.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `18.119.209.50` | 11 | 3.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `45.198.224.125` | 11 | 3.0% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.17` | 156 | 71.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `208.87.243.191` | 21 | 9.7% | Hosting/Cloud (psychz) | United States / California / Los Angeles / Psychz Networks |
| 3 | `151.101.218.13` | 17 | 7.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `3.83.245.221` | 12 | 5.5% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `18.119.209.50` | 11 | 5.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
