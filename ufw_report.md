# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4443
- Unique source IPs: 1847
- Unique countries/cities (24h): 279
- Unique destination ports: 3414

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 75 | 1.7% |
| 2 | `27015` | 50 | 1.1% |
| 3 | `22` | 30 | 0.7% |
| 4 | `5060` | 24 | 0.5% |
| 5 | `53` | 23 | 0.5% |
| 6 | `8080` | 21 | 0.5% |
| 7 | `8081` | 20 | 0.5% |
| 8 | `1433` | 19 | 0.4% |
| 9 | `8888` | 18 | 0.4% |
| 10 | `3389` | 17 | 0.4% |
| 11 | `8443` | 15 | 0.3% |
| 12 | `3306` | 12 | 0.3% |
| 13 | `9200` | 11 | 0.2% |
| 14 | `8082` | 9 | 0.2% |
| 15 | `25` | 8 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4092 | 92.1% |
| 2 | `UDP` | 348 | 7.8% |
| 3 | `47` | 2 | 0.0% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `176.65.139.58` | 1735 | 39.1% |
| 2 | `60.247.168.204` | 56 | 1.3% |
| 3 | `107.174.155.67` | 21 | 0.5% |
| 4 | `111.243.90.72` | 18 | 0.4% |
| 5 | `3.17.233.126` | 16 | 0.4% |
| 6 | `192.241.179.233` | 13 | 0.3% |
| 7 | `151.101.217.44` | 12 | 0.3% |
| 8 | `2.22.149.136` | 10 | 0.2% |
| 9 | `23.64.58.26` | 10 | 0.2% |
| 10 | `3.131.24.55` | 9 | 0.2% |
| 11 | `18.217.208.51` | 9 | 0.2% |
| 12 | `45.194.67.2` | 9 | 0.2% |
| 13 | `151.101.217.230` | 9 | 0.2% |
| 14 | `54.37.128.241` | 9 | 0.2% |
| 15 | `100.28.153.226` | 8 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3946 | 96.4% |
| 2 | `ACK+FIN+PSH` | 89 | 2.2% |
| 3 | `ACK+FIN` | 31 | 0.8% |
| 4 | `ACK+PSH` | 14 | 0.3% |
| 5 | `ACK` | 10 | 0.2% |
| 6 | `SYN+ECE+CWR` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4441 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `107.174.155.67` -> `23` | 21 | 0.5% |
| 2 | `192.241.179.233` -> `23` | 13 | 0.3% |
| 3 | `3.17.233.126` -> `58110` | 7 | 0.2% |
| 4 | `151.101.217.44` -> `59944` | 6 | 0.1% |
| 5 | `151.101.217.230` -> `53238` | 5 | 0.1% |
| 6 | `2.22.149.136` -> `20749` | 5 | 0.1% |
| 7 | `2.23.164.200` -> `58474` | 5 | 0.1% |
| 8 | `151.101.218.13` -> `59028` | 5 | 0.1% |
| 9 | `3.17.233.126` -> `58122` | 5 | 0.1% |
| 10 | `69.17.52.1` -> `8333` | 4 | 0.1% |
| 11 | `185.133.35.61` -> `43206` | 4 | 0.1% |
| 12 | `151.101.217.230` -> `53230` | 4 | 0.1% |
| 13 | `2.22.149.121` -> `21533` | 4 | 0.1% |
| 14 | `104.18.32.47` -> `40544` | 4 | 0.1% |
| 15 | `104.18.94.41` -> `47484` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-05 04:00:00:00 | 134 | 3.0% |
| 2026-06-05 05:00:00:00 | 180 | 4.1% |
| 2026-06-05 06:00:00:00 | 177 | 4.0% |
| 2026-06-05 07:00:00:00 | 184 | 4.1% |
| 2026-06-05 08:00:00:00 | 191 | 4.3% |
| 2026-06-05 09:00:00:00 | 180 | 4.1% |
| 2026-06-05 10:00:00:00 | 180 | 4.1% |
| 2026-06-05 11:00:00:00 | 180 | 4.1% |
| 2026-06-05 12:00:00:00 | 180 | 4.1% |
| 2026-06-05 13:00:00:00 | 180 | 4.1% |
| 2026-06-05 14:00:00:00 | 180 | 4.1% |
| 2026-06-05 15:00:00:00 | 201 | 4.5% |
| 2026-06-05 16:00:00:00 | 180 | 4.1% |
| 2026-06-05 17:00:00:00 | 180 | 4.1% |
| 2026-06-05 18:00:00:00 | 199 | 4.5% |
| 2026-06-05 19:00:00:00 | 180 | 4.1% |
| 2026-06-05 20:00:00:00 | 180 | 4.1% |
| 2026-06-05 21:00:00:00 | 196 | 4.4% |
| 2026-06-05 22:00:00:00 | 191 | 4.3% |
| 2026-06-05 23:00:00:00 | 208 | 4.7% |
| 2026-06-06 00:00:00:00 | 184 | 4.1% |
| 2026-06-06 01:00:00:00 | 191 | 4.3% |
| 2026-06-06 02:00:00:00 | 180 | 4.1% |
| 2026-06-06 03:00:00:00 | 180 | 4.1% |
| 2026-06-06 04:00:00:00 | 47 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Eygelshoven, The Netherlands | 1735 | 89.2% |
| 2 | Ulanqab, China | 56 | 2.9% |
| 3 | Buenos Aires, Argentina | 41 | 2.1% |
| 4 | Dublin, United States | 34 | 1.7% |
| 5 | Los Angeles, United States | 21 | 1.1% |
| 6 | Taipei, Taiwan | 18 | 0.9% |
| 7 | Secaucus, United States | 13 | 0.7% |
| 8 | Santo Domingo Oeste, Dominican Republic | 9 | 0.5% |
| 9 | Warsaw, Poland | 9 | 0.5% |
| 10 | Ashburn, United States | 8 | 0.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `176.65.139.58` | 1735 | 89.2% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 2 | `60.247.168.204` | 56 | 2.9% | China / Inner Mongolia / Ulanqab / Chengdu west dimension digital technology Co., LTD | Hosting/Cloud (data center) |
| 3 | `107.174.155.67` | 21 | 1.1% | United States / California / Los Angeles / sally wang | No apparent signal |
| 4 | `111.243.90.72` | 18 | 0.9% | Taiwan / Taipei City / Taipei / Chunghwa Telecom Co. Ltd. | No apparent signal |
| 5 | `3.17.233.126` | 16 | 0.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 6 | `192.241.179.233` | 13 | 0.7% | United States / New Jersey / Secaucus / Digital Ocean | Hosting/Cloud (digitalocean) |
| 7 | `151.101.217.44` | 12 | 0.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 8 | `2.22.149.136` | 10 | 0.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 9 | `23.64.58.26` | 10 | 0.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. | CDN/Edge (akamai) |
| 10 | `3.131.24.55` | 9 | 0.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `18.217.208.51` | 9 | 0.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `45.194.67.2` | 9 | 0.5% | Dominican Republic / Santo Domingo Province / Santo Domingo Oeste / Aaroppe Internet Services Ltd Sti | No apparent signal |
| 13 | `151.101.217.230` | 9 | 0.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 14 | `54.37.128.241` | 9 | 0.5% | Poland / Mazovia / Warsaw / OVH Sp. z o. o | Hosting/Cloud (ovh) |
| 15 | `100.28.153.226` | 8 | 0.4% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `60.247.168.204` | 56 | 34.8% | Hosting/Cloud (data center) | China / Inner Mongolia / Ulanqab / Chengdu west dimension digital technology Co., LTD |
| 2 | `3.17.233.126` | 16 | 9.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `192.241.179.233` | 13 | 8.1% | Hosting/Cloud (digitalocean) | United States / New Jersey / Secaucus / Digital Ocean |
| 4 | `151.101.217.44` | 12 | 7.5% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `2.22.149.136` | 10 | 6.2% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 6 | `23.64.58.26` | 10 | 6.2% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. |
| 7 | `3.131.24.55` | 9 | 5.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 8 | `18.217.208.51` | 9 | 5.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 9 | `151.101.217.230` | 9 | 5.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 10 | `54.37.128.241` | 9 | 5.6% | Hosting/Cloud (ovh) | Poland / Mazovia / Warsaw / OVH Sp. z o. o |
| 11 | `100.28.153.226` | 8 | 5.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
