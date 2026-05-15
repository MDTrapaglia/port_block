# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4405
- Unique source IPs: 2742
- Unique countries/cities (24h): 372
- Unique destination ports: 2548

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 182 | 4.1% |
| 2 | `22` | 45 | 1.0% |
| 3 | `5060` | 37 | 0.8% |
| 4 | `8080` | 24 | 0.5% |
| 5 | `53` | 24 | 0.5% |
| 6 | `1433` | 24 | 0.5% |
| 7 | `9200` | 21 | 0.5% |
| 8 | `5555` | 20 | 0.5% |
| 9 | `3389` | 20 | 0.5% |
| 10 | `3306` | 19 | 0.4% |
| 11 | `8443` | 18 | 0.4% |
| 12 | `8888` | 17 | 0.4% |
| 13 | `8000` | 17 | 0.4% |
| 14 | `5900` | 16 | 0.4% |
| 15 | `25565` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4000 | 90.8% |
| 2 | `UDP` | 390 | 8.9% |
| 3 | `47` | 14 | 0.3% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `176.65.139.78` | 60 | 1.4% |
| 2 | `176.65.149.213` | 58 | 1.3% |
| 3 | `87.121.84.148` | 37 | 0.8% |
| 4 | `124.198.131.185` | 18 | 0.4% |
| 5 | `176.65.148.92` | 16 | 0.4% |
| 6 | `43.228.157.9` | 15 | 0.3% |
| 7 | `172.93.106.153` | 14 | 0.3% |
| 8 | `85.217.149.43` | 13 | 0.3% |
| 9 | `170.51.247.43` | 13 | 0.3% |
| 10 | `2.22.149.171` | 13 | 0.3% |
| 11 | `38.102.86.198` | 13 | 0.3% |
| 12 | `23.64.58.7` | 13 | 0.3% |
| 13 | `3.142.170.60` | 12 | 0.3% |
| 14 | `5.61.209.102` | 11 | 0.2% |
| 15 | `5.187.35.142` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3833 | 95.8% |
| 2 | `ACK+FIN+PSH` | 79 | 2.0% |
| 3 | `ACK+PSH` | 64 | 1.6% |
| 4 | `ACK` | 15 | 0.4% |
| 5 | `ACK+FIN` | 5 | 0.1% |
| 6 | `SYN+ECE+CWR` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4400 | 99.9% |
| 2 | `wlan0` | 5 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `38.102.86.198` -> `23` | 13 | 0.3% |
| 2 | `69.17.52.1` -> `8333` | 10 | 0.2% |
| 3 | `124.198.131.185` -> `8021` | 7 | 0.2% |
| 4 | `176.65.139.188` -> `5555` | 7 | 0.2% |
| 5 | `54.203.147.253` -> `33745` | 7 | 0.2% |
| 6 | `124.198.131.185` -> `3001` | 6 | 0.1% |
| 7 | `23.64.58.5` -> `63196` | 6 | 0.1% |
| 8 | `151.101.218.73` -> `13033` | 6 | 0.1% |
| 9 | `15.204.157.192` -> `5060` | 5 | 0.1% |
| 10 | `1.71.143.145` -> `23` | 5 | 0.1% |
| 11 | `170.51.247.43` -> `10195` | 5 | 0.1% |
| 12 | `2.22.149.171` -> `11045` | 5 | 0.1% |
| 13 | `31.13.94.2` -> `61108` | 5 | 0.1% |
| 14 | `23.64.58.33` -> `12285` | 5 | 0.1% |
| 15 | `95.100.88.83` -> `12281` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-14 04:00:00:00 | 135 | 3.1% |
| 2026-05-14 05:00:00:00 | 179 | 4.1% |
| 2026-05-14 06:00:00:00 | 180 | 4.1% |
| 2026-05-14 07:00:00:00 | 181 | 4.1% |
| 2026-05-14 08:00:00:00 | 179 | 4.1% |
| 2026-05-14 09:00:00:00 | 185 | 4.2% |
| 2026-05-14 10:00:00:00 | 178 | 4.0% |
| 2026-05-14 11:00:00:00 | 182 | 4.1% |
| 2026-05-14 12:00:00:00 | 182 | 4.1% |
| 2026-05-14 13:00:00:00 | 180 | 4.1% |
| 2026-05-14 14:00:00:00 | 198 | 4.5% |
| 2026-05-14 15:00:00:00 | 181 | 4.1% |
| 2026-05-14 16:00:00:00 | 180 | 4.1% |
| 2026-05-14 17:00:00:00 | 180 | 4.1% |
| 2026-05-14 18:00:00:00 | 179 | 4.1% |
| 2026-05-14 19:00:00:00 | 180 | 4.1% |
| 2026-05-14 20:00:00:00 | 181 | 4.1% |
| 2026-05-14 21:00:00:00 | 180 | 4.1% |
| 2026-05-14 22:00:00:00 | 180 | 4.1% |
| 2026-05-14 23:00:00:00 | 179 | 4.1% |
| 2026-05-15 00:00:00:00 | 205 | 4.7% |
| 2026-05-15 01:00:00:00 | 180 | 4.1% |
| 2026-05-15 02:00:00:00 | 213 | 4.8% |
| 2026-05-15 03:00:00:00 | 181 | 4.1% |
| 2026-05-15 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Eygelshoven, The Netherlands | 76 | 24.0% |
| 2 | Eygelshoven, Netherlands | 58 | 18.3% |
| 3 | Buenos Aires, Argentina | 39 | 12.3% |
| 4 | Las Vegas, United States | 37 | 11.7% |
| 5 | New York, United States | 31 | 9.8% |
| 6 | Amsterdam, The Netherlands | 22 | 6.9% |
| 7 | Singapore, Singapore | 15 | 4.7% |
| 8 | Piscataway, United States | 14 | 4.4% |
| 9 | Montreal, Canada | 13 | 4.1% |
| 10 | Dublin, United States | 12 | 3.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `176.65.139.78` | 60 | 18.9% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 2 | `176.65.149.213` | 58 | 18.3% | Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 3 | `87.121.84.148` | 37 | 11.7% | United States / Nevada / Las Vegas / VPSVAULT.HOST LTD | No apparent signal |
| 4 | `124.198.131.185` | 18 | 5.7% | United States / New York / New York / 1337 Services GmbH | No apparent signal |
| 5 | `176.65.148.92` | 16 | 5.0% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 6 | `43.228.157.9` | 15 | 4.7% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 7 | `172.93.106.153` | 14 | 4.4% | United States / New Jersey / Piscataway / Klemen Stirn | No apparent signal |
| 8 | `85.217.149.43` | 13 | 4.1% | United States / New York / New York / Modat B.V | No apparent signal |
| 9 | `170.51.247.43` | 13 | 4.1% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 10 | `2.22.149.171` | 13 | 4.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 11 | `38.102.86.198` | 13 | 4.1% | Canada / Quebec / Montreal / Rica Web Services | No apparent signal |
| 12 | `23.64.58.7` | 13 | 4.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. | CDN/Edge (akamai) |
| 13 | `3.142.170.60` | 12 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `5.61.209.102` | 11 | 3.5% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd. Network | No apparent signal |
| 15 | `5.187.35.142` | 11 | 3.5% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `2.22.149.171` | 13 | 34.2% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 2 | `23.64.58.7` | 13 | 34.2% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. |
| 3 | `3.142.170.60` | 12 | 31.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
