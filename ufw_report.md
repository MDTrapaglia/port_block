# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4368
- Unique source IPs: 2327
- Unique countries/cities (24h): 320
- Unique destination ports: 2076

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 657 | 15.0% |
| 2 | `27015` | 62 | 1.4% |
| 3 | `22` | 40 | 0.9% |
| 4 | `3389` | 39 | 0.9% |
| 5 | `8080` | 38 | 0.9% |
| 6 | `5060` | 34 | 0.8% |
| 7 | `5900` | 27 | 0.6% |
| 8 | `53` | 26 | 0.6% |
| 9 | `8443` | 24 | 0.5% |
| 10 | `2222` | 20 | 0.5% |
| 11 | `8081` | 20 | 0.5% |
| 12 | `9200` | 20 | 0.5% |
| 13 | `5000` | 17 | 0.4% |
| 14 | `10001` | 15 | 0.3% |
| 15 | `unknown` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3848 | 88.1% |
| 2 | `UDP` | 505 | 11.6% |
| 3 | `47` | 14 | 0.3% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `15.204.234.74` | 588 | 13.5% |
| 2 | `86.54.24.215` | 25 | 0.6% |
| 3 | `17.57.144.152` | 21 | 0.5% |
| 4 | `5.187.35.142` | 19 | 0.4% |
| 5 | `77.91.71.67` | 19 | 0.4% |
| 6 | `138.226.239.21` | 17 | 0.4% |
| 7 | `138.226.239.22` | 16 | 0.4% |
| 8 | `185.136.15.77` | 15 | 0.3% |
| 9 | `3.142.170.60` | 14 | 0.3% |
| 10 | `77.91.71.66` | 14 | 0.3% |
| 11 | `13.219.1.233` | 14 | 0.3% |
| 12 | `204.76.203.15` | 14 | 0.3% |
| 13 | `2.22.149.179` | 14 | 0.3% |
| 14 | `51.159.110.167` | 13 | 0.3% |
| 15 | `34.197.70.90` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3711 | 96.4% |
| 2 | `ACK+PSH` | 74 | 1.9% |
| 3 | `ACK+FIN+PSH` | 51 | 1.3% |
| 4 | `ACK` | 5 | 0.1% |
| 5 | `ACK+FIN` | 5 | 0.1% |
| 6 | `SYN+ECE+CWR` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4366 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `15.204.234.74` -> `23` | 588 | 13.5% |
| 2 | `69.17.52.1` -> `8333` | 9 | 0.2% |
| 3 | `138.226.239.21` -> `3389` | 8 | 0.2% |
| 4 | `2.22.149.139` -> `6357` | 7 | 0.2% |
| 5 | `2.22.149.177` -> `6187` | 6 | 0.1% |
| 6 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 7 | `51.159.110.167` -> `25565` | 5 | 0.1% |
| 8 | `17.57.144.152` -> `55301` | 5 | 0.1% |
| 9 | `17.57.144.152` -> `55316` | 5 | 0.1% |
| 10 | `199.45.155.90` -> `8443` | 5 | 0.1% |
| 11 | `2.22.149.179` -> `64898` | 5 | 0.1% |
| 12 | `180.167.128.203` -> `22` | 4 | 0.1% |
| 13 | `95.100.44.10` -> `40796` | 4 | 0.1% |
| 14 | `51.159.110.167` -> `25564` | 4 | 0.1% |
| 15 | `34.156.112.15` -> `990` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-31 04:00:00:00 | 134 | 3.1% |
| 2026-05-31 05:00:00:00 | 184 | 4.2% |
| 2026-05-31 06:00:00:00 | 180 | 4.1% |
| 2026-05-31 07:00:00:00 | 178 | 4.1% |
| 2026-05-31 08:00:00:00 | 181 | 4.1% |
| 2026-05-31 09:00:00:00 | 181 | 4.1% |
| 2026-05-31 10:00:00:00 | 169 | 3.9% |
| 2026-05-31 11:00:00:00 | 178 | 4.1% |
| 2026-05-31 12:00:00:00 | 184 | 4.2% |
| 2026-05-31 13:00:00:00 | 179 | 4.1% |
| 2026-05-31 14:00:00:00 | 180 | 4.1% |
| 2026-05-31 15:00:00:00 | 180 | 4.1% |
| 2026-05-31 16:00:00:00 | 181 | 4.1% |
| 2026-05-31 17:00:00:00 | 179 | 4.1% |
| 2026-05-31 18:00:00:00 | 181 | 4.1% |
| 2026-05-31 19:00:00:00 | 179 | 4.1% |
| 2026-05-31 20:00:00:00 | 182 | 4.2% |
| 2026-05-31 21:00:00:00 | 180 | 4.1% |
| 2026-05-31 22:00:00:00 | 210 | 4.8% |
| 2026-05-31 23:00:00:00 | 180 | 4.1% |
| 2026-06-01 00:00:00:00 | 197 | 4.5% |
| 2026-06-01 01:00:00:00 | 184 | 4.2% |
| 2026-06-01 02:00:00:00 | 181 | 4.1% |
| 2026-06-01 03:00:00:00 | 172 | 3.9% |
| 2026-06-01 04:00:00:00 | 54 | 1.2% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Reston, United States | 588 | 72.1% |
| 2 | Jerusalem, Israel | 33 | 4.0% |
| 3 | Port Vila, Vanuatu | 33 | 4.0% |
| 4 | Ashburn, United States | 26 | 3.2% |
| 5 | Riga, Latvia | 25 | 3.1% |
| 6 | United States / California / Cupertino / Apple Inc | 21 | 2.6% |
| 7 | Amsterdam, The Netherlands | 19 | 2.3% |
| 8 | Almaty, Kazakhstan | 15 | 1.8% |
| 9 | Dublin, United States | 14 | 1.7% |
| 10 | Eygelshoven, Netherlands | 14 | 1.7% |
| 11 | Buenos Aires, Argentina | 14 | 1.7% |
| 12 | Paris, France | 13 | 1.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `15.204.234.74` | 588 | 72.1% | United States / Virginia / Reston / OVH US LLC | Hosting/Cloud (ovh) |
| 2 | `86.54.24.215` | 25 | 3.1% | Latvia / Rīga / Riga / Noyobzoda Faridduni Saidilhom | No apparent signal |
| 3 | `17.57.144.152` | 21 | 2.6% | United States / California / Cupertino / Apple Inc | No apparent signal |
| 4 | `5.187.35.142` | 19 | 2.3% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 5 | `77.91.71.67` | 19 | 2.3% | Israel / Jerusalem / Jerusalem / Proline IT Ltd | No apparent signal |
| 6 | `138.226.239.21` | 17 | 2.1% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 7 | `138.226.239.22` | 16 | 2.0% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 8 | `185.136.15.77` | 15 | 1.8% | Kazakhstan / Almaty / Almaty / net | No apparent signal |
| 9 | `3.142.170.60` | 14 | 1.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `77.91.71.66` | 14 | 1.7% | Israel / Jerusalem / Jerusalem / Proline IT Ltd | No apparent signal |
| 11 | `13.219.1.233` | 14 | 1.7% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 12 | `204.76.203.15` | 14 | 1.7% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 13 | `2.22.149.179` | 14 | 1.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 14 | `51.159.110.167` | 13 | 1.6% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 15 | `34.197.70.90` | 12 | 1.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `15.204.234.74` | 588 | 89.8% | Hosting/Cloud (ovh) | United States / Virginia / Reston / OVH US LLC |
| 2 | `3.142.170.60` | 14 | 2.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `13.219.1.233` | 14 | 2.1% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 4 | `2.22.149.179` | 14 | 2.1% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 5 | `51.159.110.167` | 13 | 2.0% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 6 | `34.197.70.90` | 12 | 1.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
