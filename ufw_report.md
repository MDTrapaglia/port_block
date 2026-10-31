# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4413
- Unique source IPs: 2486
- Unique countries/cities (24h): 327
- Unique destination ports: 2618

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 176 | 4.0% |
| 2 | `22` | 76 | 1.7% |
| 3 | `8080` | 44 | 1.0% |
| 4 | `3389` | 43 | 1.0% |
| 5 | `5060` | 32 | 0.7% |
| 6 | `7680` | 30 | 0.7% |
| 7 | `53` | 28 | 0.6% |
| 8 | `1433` | 27 | 0.6% |
| 9 | `8081` | 22 | 0.5% |
| 10 | `27017` | 18 | 0.4% |
| 11 | `3128` | 18 | 0.4% |
| 12 | `21` | 18 | 0.4% |
| 13 | `389` | 17 | 0.4% |
| 14 | `1723` | 17 | 0.4% |
| 15 | `8443` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4053 | 91.8% |
| 2 | `UDP` | 351 | 8.0% |
| 3 | `47` | 7 | 0.2% |
| 4 | `41` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `151.101.218.13` | 36 | 0.8% |
| 2 | `172.59.161.153` | 30 | 0.7% |
| 3 | `45.198.224.154` | 24 | 0.5% |
| 4 | `71.6.242.172` | 24 | 0.5% |
| 5 | `49.207.0.145` | 23 | 0.5% |
| 6 | `2.22.149.169` | 19 | 0.4% |
| 7 | `137.184.138.85` | 17 | 0.4% |
| 8 | `91.231.89.104` | 16 | 0.4% |
| 9 | `91.231.89.205` | 15 | 0.3% |
| 10 | `35.169.206.177` | 15 | 0.3% |
| 11 | `91.231.89.150` | 15 | 0.3% |
| 12 | `91.231.89.87` | 15 | 0.3% |
| 13 | `195.184.76.116` | 14 | 0.3% |
| 14 | `91.230.168.129` | 14 | 0.3% |
| 15 | `49.206.196.117` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3902 | 96.3% |
| 2 | `ACK+FIN+PSH` | 83 | 2.0% |
| 3 | `ACK+PSH` | 41 | 1.0% |
| 4 | `SYN+ECE+CWR` | 11 | 0.3% |
| 5 | `ACK+FIN` | 10 | 0.2% |
| 6 | `ACK` | 6 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4413 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `172.59.161.153` -> `7680` | 30 | 0.7% |
| 2 | `49.207.0.145` -> `23` | 23 | 0.5% |
| 3 | `62.210.114.99` -> `3389` | 9 | 0.2% |
| 4 | `177.131.202.201` -> `23` | 8 | 0.2% |
| 5 | `151.101.218.13` -> `4871` | 8 | 0.2% |
| 6 | `154.80.128.163` -> `17000` | 6 | 0.1% |
| 7 | `216.180.246.250` -> `8080` | 6 | 0.1% |
| 8 | `151.101.218.13` -> `6329` | 6 | 0.1% |
| 9 | `187.17.224.223` -> `5038` | 5 | 0.1% |
| 10 | `2.22.149.185` -> `5913` | 5 | 0.1% |
| 11 | `2.23.164.178` -> `57252` | 5 | 0.1% |
| 12 | `93.123.109.6` -> `1723` | 4 | 0.1% |
| 13 | `151.101.218.13` -> `61892` | 4 | 0.1% |
| 14 | `151.101.218.13` -> `62156` | 4 | 0.1% |
| 15 | `2.23.164.90` -> `2571` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-30 04:00:00:00 | 133 | 3.0% |
| 2026-10-30 05:00:00:00 | 181 | 4.1% |
| 2026-10-30 06:00:00:00 | 181 | 4.1% |
| 2026-10-30 07:00:00:00 | 192 | 4.4% |
| 2026-10-30 08:00:00:00 | 191 | 4.3% |
| 2026-10-30 09:00:00:00 | 183 | 4.1% |
| 2026-10-30 10:00:00:00 | 179 | 4.1% |
| 2026-10-30 11:00:00:00 | 180 | 4.1% |
| 2026-10-30 12:00:00:00 | 182 | 4.1% |
| 2026-10-30 13:00:00:00 | 180 | 4.1% |
| 2026-10-30 14:00:00:00 | 181 | 4.1% |
| 2026-10-30 15:00:00:00 | 193 | 4.4% |
| 2026-10-30 16:00:00:00 | 180 | 4.1% |
| 2026-10-30 17:00:00:00 | 180 | 4.1% |
| 2026-10-30 18:00:00:00 | 180 | 4.1% |
| 2026-10-30 19:00:00:00 | 181 | 4.1% |
| 2026-10-30 20:00:00:00 | 180 | 4.1% |
| 2026-10-30 21:00:00:00 | 178 | 4.0% |
| 2026-10-30 22:00:00:00 | 179 | 4.1% |
| 2026-10-30 23:00:00:00 | 194 | 4.4% |
| 2026-10-31 00:00:00:00 | 177 | 4.0% |
| 2026-10-31 01:00:00:00 | 200 | 4.5% |
| 2026-10-31 02:00:00:00 | 179 | 4.1% |
| 2026-10-31 03:00:00:00 | 203 | 4.6% |
| 2026-10-31 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 61 | 21.0% |
| 2 | Buenos Aires, Argentina | 55 | 18.9% |
| 3 | Hyderabad, India | 37 | 12.7% |
| 4 | San Jose, United States | 30 | 10.3% |
| 5 | Stockholm, Sweden | 24 | 8.2% |
| 6 | Boise, United States | 24 | 8.2% |
| 7 | North Bergen, United States | 17 | 5.8% |
| 8 | Ashburn, United States | 15 | 5.2% |
| 9 | Warrenton, United States | 14 | 4.8% |
| 10 | Hillsboro, United States | 14 | 4.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 36 | 12.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 2 | `172.59.161.153` | 30 | 10.3% | United States / California / San Jose / T-Mobile USA, Inc. | Mobile/CGNAT (mobile) |
| 3 | `45.198.224.154` | 24 | 8.2% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 4 | `71.6.242.172` | 24 | 8.2% | United States / Idaho / Boise / Root Evidence, Inc | No apparent signal |
| 5 | `49.207.0.145` | 23 | 7.9% | India / Telangana / Hyderabad / Beam Telecom Pvt Ltd | No apparent signal |
| 6 | `2.22.149.169` | 19 | 6.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 7 | `137.184.138.85` | 17 | 5.8% | United States / New Jersey / North Bergen / Digital Ocean | Hosting/Cloud (digitalocean) |
| 8 | `91.231.89.104` | 16 | 5.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `91.231.89.205` | 15 | 5.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `35.169.206.177` | 15 | 5.2% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 11 | `91.231.89.150` | 15 | 5.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.87` | 15 | 5.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `195.184.76.116` | 14 | 4.8% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `91.230.168.129` | 14 | 4.8% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 15 | `49.206.196.117` | 14 | 4.8% | India / Telangana / Hyderabad / Beam Telecom Pvt Ltd | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 36 | 41.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `2.22.149.169` | 19 | 21.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `137.184.138.85` | 17 | 19.5% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / Digital Ocean |
| 4 | `35.169.206.177` | 15 | 17.2% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
