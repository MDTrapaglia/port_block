# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4532
- Unique source IPs: 2598
- Unique countries/cities (24h): 302
- Unique destination ports: 2585

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 137 | 3.0% |
| 2 | `22` | 86 | 1.9% |
| 3 | `8080` | 50 | 1.1% |
| 4 | `53` | 36 | 0.8% |
| 5 | `3389` | 35 | 0.8% |
| 6 | `5060` | 29 | 0.6% |
| 7 | `3306` | 26 | 0.6% |
| 8 | `2000` | 26 | 0.6% |
| 9 | `27017` | 22 | 0.5% |
| 10 | `1433` | 22 | 0.5% |
| 11 | `33435` | 22 | 0.5% |
| 12 | `2222` | 21 | 0.5% |
| 13 | `8443` | 19 | 0.4% |
| 14 | `5432` | 19 | 0.4% |
| 15 | `8000` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4178 | 92.2% |
| 2 | `UDP` | 344 | 7.6% |
| 3 | `47` | 9 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `151.101.218.13` | 70 | 1.5% |
| 2 | `195.184.76.20` | 14 | 0.3% |
| 3 | `91.231.89.0` | 14 | 0.3% |
| 4 | `91.231.89.87` | 14 | 0.3% |
| 5 | `91.231.89.238` | 14 | 0.3% |
| 6 | `18.221.179.104` | 13 | 0.3% |
| 7 | `45.198.224.125` | 13 | 0.3% |
| 8 | `91.231.89.224` | 13 | 0.3% |
| 9 | `91.230.168.142` | 13 | 0.3% |
| 10 | `2.22.149.155` | 13 | 0.3% |
| 11 | `138.226.239.21` | 13 | 0.3% |
| 12 | `151.101.218.73` | 13 | 0.3% |
| 13 | `2.22.149.171` | 13 | 0.3% |
| 14 | `3.131.24.55` | 12 | 0.3% |
| 15 | `18.217.208.51` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3906 | 93.5% |
| 2 | `ACK+FIN+PSH` | 182 | 4.4% |
| 3 | `ACK+PSH` | 51 | 1.2% |
| 4 | `ACK+FIN` | 30 | 0.7% |
| 5 | `SYN+ECE+CWR` | 6 | 0.1% |
| 6 | `ACK` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4532 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `62.210.114.99` -> `3389` | 8 | 0.2% |
| 2 | `151.101.218.13` -> `56624` | 8 | 0.2% |
| 3 | `93.123.109.6` -> `1723` | 7 | 0.2% |
| 4 | `170.51.247.40` -> `12299` | 7 | 0.2% |
| 5 | `151.101.218.13` -> `55040` | 7 | 0.2% |
| 6 | `2.23.164.165` -> `55540` | 7 | 0.2% |
| 7 | `95.100.88.65` -> `55786` | 7 | 0.2% |
| 8 | `32.186.90.189` -> `34478` | 7 | 0.2% |
| 9 | `45.198.224.125` -> `8080` | 6 | 0.1% |
| 10 | `35.212.164.106` -> `33435` | 6 | 0.1% |
| 11 | `95.100.88.59` -> `60860` | 6 | 0.1% |
| 12 | `170.51.247.41` -> `61121` | 6 | 0.1% |
| 13 | `95.100.88.49` -> `61119` | 6 | 0.1% |
| 14 | `45.198.224.125` -> `9090` | 5 | 0.1% |
| 15 | `66.132.195.55` -> `2000` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-29 04:00:00:00 | 133 | 2.9% |
| 2026-10-29 05:00:00:00 | 199 | 4.4% |
| 2026-10-29 06:00:00:00 | 190 | 4.2% |
| 2026-10-29 07:00:00:00 | 185 | 4.1% |
| 2026-10-29 08:00:00:00 | 180 | 4.0% |
| 2026-10-29 09:00:00:00 | 181 | 4.0% |
| 2026-10-29 10:00:00:00 | 180 | 4.0% |
| 2026-10-29 11:00:00:00 | 180 | 4.0% |
| 2026-10-29 12:00:00:00 | 180 | 4.0% |
| 2026-10-29 13:00:00:00 | 179 | 3.9% |
| 2026-10-29 14:00:00:00 | 181 | 4.0% |
| 2026-10-29 15:00:00:00 | 178 | 3.9% |
| 2026-10-29 16:00:00:00 | 232 | 5.1% |
| 2026-10-29 17:00:00:00 | 209 | 4.6% |
| 2026-10-29 18:00:00:00 | 206 | 4.5% |
| 2026-10-29 19:00:00:00 | 198 | 4.4% |
| 2026-10-29 20:00:00:00 | 180 | 4.0% |
| 2026-10-29 21:00:00:00 | 180 | 4.0% |
| 2026-10-29 22:00:00:00 | 181 | 4.0% |
| 2026-10-29 23:00:00:00 | 179 | 3.9% |
| 2026-10-30 00:00:00:00 | 179 | 3.9% |
| 2026-10-30 01:00:00:00 | 191 | 4.2% |
| 2026-10-30 02:00:00:00 | 213 | 4.7% |
| 2026-10-30 03:00:00:00 | 193 | 4.3% |
| 2026-10-30 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Buenos Aires, Argentina | 96 | 37.8% |
| 2 | Gravelines, France | 55 | 21.7% |
| 3 | Dublin, United States | 37 | 14.6% |
| 4 | Warrenton, United States | 14 | 5.5% |
| 5 | Stockholm, Sweden | 13 | 5.1% |
| 6 | Hillsboro, United States | 13 | 5.1% |
| 7 | Port Vila, Vanuatu | 13 | 5.1% |
| 8 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 13 | 5.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 70 | 27.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 2 | `195.184.76.20` | 14 | 5.5% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 3 | `91.231.89.0` | 14 | 5.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 4 | `91.231.89.87` | 14 | 5.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 5 | `91.231.89.238` | 14 | 5.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 6 | `18.221.179.104` | 13 | 5.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `45.198.224.125` | 13 | 5.1% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 8 | `91.231.89.224` | 13 | 5.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `91.230.168.142` | 13 | 5.1% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 10 | `2.22.149.155` | 13 | 5.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 11 | `138.226.239.21` | 13 | 5.1% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 12 | `151.101.218.73` | 13 | 5.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 13 | `2.22.149.171` | 13 | 5.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 14 | `3.131.24.55` | 12 | 4.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `18.217.208.51` | 12 | 4.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 70 | 47.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `18.221.179.104` | 13 | 8.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `2.22.149.155` | 13 | 8.9% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 4 | `151.101.218.73` | 13 | 8.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `2.22.149.171` | 13 | 8.9% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 6 | `3.131.24.55` | 12 | 8.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `18.217.208.51` | 12 | 8.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
