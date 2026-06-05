# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4357
- Unique source IPs: 2808
- Unique countries/cities (24h): 343
- Unique destination ports: 2657

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 129 | 3.0% |
| 2 | `27015` | 79 | 1.8% |
| 3 | `8080` | 48 | 1.1% |
| 4 | `22` | 43 | 1.0% |
| 5 | `5060` | 36 | 0.8% |
| 6 | `8443` | 31 | 0.7% |
| 7 | `3389` | 27 | 0.6% |
| 8 | `9200` | 23 | 0.5% |
| 9 | `1433` | 22 | 0.5% |
| 10 | `8000` | 20 | 0.5% |
| 11 | `3306` | 18 | 0.4% |
| 12 | `53` | 17 | 0.4% |
| 13 | `21` | 17 | 0.4% |
| 14 | `5555` | 15 | 0.3% |
| 15 | `2222` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3843 | 88.2% |
| 2 | `UDP` | 504 | 11.6% |
| 3 | `47` | 9 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `176.65.148.229` | 55 | 1.3% |
| 2 | `202.124.193.221` | 45 | 1.0% |
| 3 | `89.125.154.191` | 32 | 0.7% |
| 4 | `192.241.179.233` | 14 | 0.3% |
| 5 | `2.22.149.177` | 13 | 0.3% |
| 6 | `45.205.1.240` | 12 | 0.3% |
| 7 | `51.159.110.167` | 12 | 0.3% |
| 8 | `204.76.203.15` | 12 | 0.3% |
| 9 | `94.156.152.50` | 12 | 0.3% |
| 10 | `151.243.11.37` | 10 | 0.2% |
| 11 | `18.190.15.50` | 10 | 0.2% |
| 12 | `45.205.1.241` | 10 | 0.2% |
| 13 | `101.36.129.185` | 10 | 0.2% |
| 14 | `18.221.179.104` | 9 | 0.2% |
| 15 | `100.50.17.159` | 9 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3765 | 98.0% |
| 2 | `ACK+PSH` | 37 | 1.0% |
| 3 | `ACK+FIN+PSH` | 27 | 0.7% |
| 4 | `ACK+FIN` | 10 | 0.3% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4355 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.241.179.233` -> `23` | 14 | 0.3% |
| 2 | `94.156.152.50` -> `23` | 12 | 0.3% |
| 3 | `91.227.220.35` -> `23` | 9 | 0.2% |
| 4 | `66.132.172.139` -> `8443` | 8 | 0.2% |
| 5 | `69.17.52.1` -> `8333` | 7 | 0.2% |
| 6 | `31.13.94.142` -> `54826` | 7 | 0.2% |
| 7 | `45.198.224.18` -> `8728` | 6 | 0.1% |
| 8 | `124.198.131.39` -> `3000` | 6 | 0.1% |
| 9 | `2.22.149.177` -> `54712` | 5 | 0.1% |
| 10 | `216.180.246.53` -> `53` | 5 | 0.1% |
| 11 | `51.159.110.167` -> `25564` | 4 | 0.1% |
| 12 | `51.159.110.167` -> `25565` | 4 | 0.1% |
| 13 | `51.159.110.167` -> `25566` | 4 | 0.1% |
| 14 | `34.102.215.99` -> `54212` | 4 | 0.1% |
| 15 | `66.132.224.87` -> `587` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-04 04:00:00:00 | 134 | 3.1% |
| 2026-06-04 05:00:00:00 | 179 | 4.1% |
| 2026-06-04 06:00:00:00 | 182 | 4.2% |
| 2026-06-04 07:00:00:00 | 180 | 4.1% |
| 2026-06-04 08:00:00:00 | 180 | 4.1% |
| 2026-06-04 09:00:00:00 | 179 | 4.1% |
| 2026-06-04 10:00:00:00 | 179 | 4.1% |
| 2026-06-04 11:00:00:00 | 207 | 4.8% |
| 2026-06-04 12:00:00:00 | 183 | 4.2% |
| 2026-06-04 13:00:00:00 | 179 | 4.1% |
| 2026-06-04 14:00:00:00 | 179 | 4.1% |
| 2026-06-04 15:00:00:00 | 180 | 4.1% |
| 2026-06-04 16:00:00:00 | 181 | 4.2% |
| 2026-06-04 17:00:00:00 | 179 | 4.1% |
| 2026-06-04 18:00:00:00 | 190 | 4.4% |
| 2026-06-04 19:00:00:00 | 179 | 4.1% |
| 2026-06-04 20:00:00:00 | 180 | 4.1% |
| 2026-06-04 21:00:00:00 | 181 | 4.2% |
| 2026-06-04 22:00:00:00 | 180 | 4.1% |
| 2026-06-04 23:00:00:00 | 180 | 4.1% |
| 2026-06-05 00:00:00:00 | 178 | 4.1% |
| 2026-06-05 01:00:00:00 | 182 | 4.2% |
| 2026-06-05 02:00:00:00 | 180 | 4.1% |
| 2026-06-05 03:00:00:00 | 178 | 4.1% |
| 2026-06-05 04:00:00:00 | 48 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Eygelshoven, The Netherlands | 55 | 20.8% |
| 2 | Mandaluyong, Philippines | 45 | 17.0% |
| 3 | Frankfurt am Main, Germany | 42 | 15.8% |
| 4 | São Paulo, Brazil | 22 | 8.3% |
| 5 | Dublin, United States | 19 | 7.2% |
| 6 | Secaucus, United States | 14 | 5.3% |
| 7 | Buenos Aires, Argentina | 13 | 4.9% |
| 8 | Paris, France | 12 | 4.5% |
| 9 | Eygelshoven, Netherlands | 12 | 4.5% |
| 10 | Centurion, South Africa | 12 | 4.5% |
| 11 | Shenzhen City Centre, China | 10 | 3.8% |
| 12 | Ashburn, United States | 9 | 3.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `176.65.148.229` | 55 | 20.8% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 2 | `202.124.193.221` | 45 | 17.0% | Philippines / Metro Manila / Mandaluyong / WIT Phils Inc | No apparent signal |
| 3 | `89.125.154.191` | 32 | 12.1% | Germany / Hesse / Frankfurt am Main / RCS Technologies FZE LLC | No apparent signal |
| 4 | `192.241.179.233` | 14 | 5.3% | United States / New Jersey / Secaucus / Digital Ocean | Hosting/Cloud (digitalocean) |
| 5 | `2.22.149.177` | 13 | 4.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 6 | `45.205.1.240` | 12 | 4.5% | Brazil / São Paulo / São Paulo / Vpsvault.host LTD | No apparent signal |
| 7 | `51.159.110.167` | 12 | 4.5% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 8 | `204.76.203.15` | 12 | 4.5% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 9 | `94.156.152.50` | 12 | 4.5% | South Africa / Gauteng / Centurion / Internet Magnate (Pty) Ltd | No apparent signal |
| 10 | `151.243.11.37` | 10 | 3.8% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 11 | `18.190.15.50` | 10 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `45.205.1.241` | 10 | 3.8% | Brazil / São Paulo / São Paulo / Vpsvault.host LTD | No apparent signal |
| 13 | `101.36.129.185` | 10 | 3.8% | China / Guangdong / Shenzhen City Centre / Beijing Zhonglianlixin Technology Co., Ltd. | Mobile/CGNAT (mobile) |
| 14 | `18.221.179.104` | 9 | 3.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `100.50.17.159` | 9 | 3.4% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.241.179.233` | 14 | 20.9% | Hosting/Cloud (digitalocean) | United States / New Jersey / Secaucus / Digital Ocean |
| 2 | `2.22.149.177` | 13 | 19.4% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `51.159.110.167` | 12 | 17.9% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 4 | `18.190.15.50` | 10 | 14.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.221.179.104` | 9 | 13.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `100.50.17.159` | 9 | 13.4% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
