# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4354
- Unique source IPs: 2611
- Unique countries/cities (24h): 377
- Unique destination ports: 2600

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 115 | 2.6% |
| 2 | `27015` | 70 | 1.6% |
| 3 | `8080` | 57 | 1.3% |
| 4 | `22` | 43 | 1.0% |
| 5 | `3389` | 38 | 0.9% |
| 6 | `5060` | 34 | 0.8% |
| 7 | `8081` | 31 | 0.7% |
| 8 | `8443` | 27 | 0.6% |
| 9 | `3306` | 21 | 0.5% |
| 10 | `53` | 19 | 0.4% |
| 11 | `2222` | 19 | 0.4% |
| 12 | `1433` | 19 | 0.4% |
| 13 | `161` | 18 | 0.4% |
| 14 | `9200` | 17 | 0.4% |
| 15 | `21` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3752 | 86.2% |
| 2 | `UDP` | 599 | 13.8% |
| 3 | `47` | 3 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `176.65.139.55` | 60 | 1.4% |
| 2 | `101.36.129.185` | 51 | 1.2% |
| 3 | `64.89.160.119` | 47 | 1.1% |
| 4 | `176.65.139.130` | 29 | 0.7% |
| 5 | `112.140.184.197` | 19 | 0.4% |
| 6 | `192.241.179.233` | 16 | 0.4% |
| 7 | `18.119.209.50` | 15 | 0.3% |
| 8 | `5.187.35.142` | 15 | 0.3% |
| 9 | `204.76.203.15` | 15 | 0.3% |
| 10 | `44.215.219.236` | 14 | 0.3% |
| 11 | `2.22.149.137` | 13 | 0.3% |
| 12 | `151.243.11.37` | 12 | 0.3% |
| 13 | `3.131.24.55` | 12 | 0.3% |
| 14 | `18.190.15.50` | 12 | 0.3% |
| 15 | `159.223.169.110` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3654 | 97.4% |
| 2 | `ACK+FIN+PSH` | 42 | 1.1% |
| 3 | `ACK+PSH` | 38 | 1.0% |
| 4 | `ACK` | 9 | 0.2% |
| 5 | `SYN+ECE+CWR` | 5 | 0.1% |
| 6 | `ACK+FIN` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4354 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `112.140.184.197` -> `23` | 19 | 0.4% |
| 2 | `192.241.179.233` -> `23` | 16 | 0.4% |
| 3 | `104.238.81.133` -> `23` | 10 | 0.2% |
| 4 | `69.17.52.1` -> `8333` | 7 | 0.2% |
| 5 | `178.20.210.152` -> `1723` | 7 | 0.2% |
| 6 | `124.198.131.39` -> `3000` | 6 | 0.1% |
| 7 | `45.205.1.68` -> `2011` | 5 | 0.1% |
| 8 | `45.198.224.18` -> `8728` | 5 | 0.1% |
| 9 | `130.12.180.174` -> `23` | 5 | 0.1% |
| 10 | `2.23.164.216` -> `64588` | 5 | 0.1% |
| 11 | `66.132.195.77` -> `25` | 5 | 0.1% |
| 12 | `66.132.195.62` -> `8080` | 5 | 0.1% |
| 13 | `162.159.128.233` -> `50012` | 5 | 0.1% |
| 14 | `2.22.149.137` -> `52790` | 5 | 0.1% |
| 15 | `51.159.110.167` -> `25564` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-08 04:00:00:00 | 133 | 3.1% |
| 2026-06-08 05:00:00:00 | 180 | 4.1% |
| 2026-06-08 06:00:00:00 | 181 | 4.2% |
| 2026-06-08 07:00:00:00 | 178 | 4.1% |
| 2026-06-08 08:00:00:00 | 167 | 3.8% |
| 2026-06-08 09:00:00:00 | 180 | 4.1% |
| 2026-06-08 10:00:00:00 | 181 | 4.2% |
| 2026-06-08 11:00:00:00 | 188 | 4.3% |
| 2026-06-08 12:00:00:00 | 180 | 4.1% |
| 2026-06-08 13:00:00:00 | 180 | 4.1% |
| 2026-06-08 14:00:00:00 | 181 | 4.2% |
| 2026-06-08 15:00:00:00 | 179 | 4.1% |
| 2026-06-08 16:00:00:00 | 180 | 4.1% |
| 2026-06-08 17:00:00:00 | 181 | 4.2% |
| 2026-06-08 18:00:00:00 | 180 | 4.1% |
| 2026-06-08 19:00:00:00 | 178 | 4.1% |
| 2026-06-08 20:00:00:00 | 181 | 4.2% |
| 2026-06-08 21:00:00:00 | 180 | 4.1% |
| 2026-06-08 22:00:00:00 | 181 | 4.2% |
| 2026-06-08 23:00:00:00 | 179 | 4.1% |
| 2026-06-09 00:00:00:00 | 185 | 4.2% |
| 2026-06-09 01:00:00:00 | 194 | 4.5% |
| 2026-06-09 02:00:00:00 | 195 | 4.5% |
| 2026-06-09 03:00:00:00 | 187 | 4.3% |
| 2026-06-09 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Eygelshoven, The Netherlands | 89 | 26.0% |
| 2 | Shenzhen City Centre, China | 51 | 14.9% |
| 3 | Schieren, Luxembourg | 47 | 13.7% |
| 4 | Dublin, United States | 39 | 11.4% |
| 5 | Singapore, Singapore | 19 | 5.6% |
| 6 | Secaucus, United States | 16 | 4.7% |
| 7 | Amsterdam, The Netherlands | 15 | 4.4% |
| 8 | Eygelshoven, Netherlands | 15 | 4.4% |
| 9 | Ashburn, United States | 14 | 4.1% |
| 10 | Buenos Aires, Argentina | 13 | 3.8% |
| 11 | Frankfurt am Main, Germany | 12 | 3.5% |
| 12 | North Bergen, United States | 12 | 3.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `176.65.139.55` | 60 | 17.5% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 2 | `101.36.129.185` | 51 | 14.9% | China / Guangdong / Shenzhen City Centre / Beijing Zhonglianlixin Technology Co., Ltd. | Mobile/CGNAT (mobile) |
| 3 | `64.89.160.119` | 47 | 13.7% | Luxembourg / Diekirch / Schieren / Ghosty Networks LLC | No apparent signal |
| 4 | `176.65.139.130` | 29 | 8.5% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 5 | `112.140.184.197` | 19 | 5.6% | Singapore / Central Singapore / Singapore / Sparkstation | No apparent signal |
| 6 | `192.241.179.233` | 16 | 4.7% | United States / New Jersey / Secaucus / Digital Ocean | Hosting/Cloud (digitalocean) |
| 7 | `18.119.209.50` | 15 | 4.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `5.187.35.142` | 15 | 4.4% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 9 | `204.76.203.15` | 15 | 4.4% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 10 | `44.215.219.236` | 14 | 4.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 11 | `2.22.149.137` | 13 | 3.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 12 | `151.243.11.37` | 12 | 3.5% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 13 | `3.131.24.55` | 12 | 3.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `18.190.15.50` | 12 | 3.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `159.223.169.110` | 12 | 3.5% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.241.179.233` | 16 | 17.0% | Hosting/Cloud (digitalocean) | United States / New Jersey / Secaucus / Digital Ocean |
| 2 | `18.119.209.50` | 15 | 16.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `44.215.219.236` | 14 | 14.9% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 4 | `2.22.149.137` | 13 | 13.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 5 | `3.131.24.55` | 12 | 12.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `18.190.15.50` | 12 | 12.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `159.223.169.110` | 12 | 12.8% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
