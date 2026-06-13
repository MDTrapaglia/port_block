# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4421
- Unique source IPs: 2573
- Unique countries/cities (24h): 373
- Unique destination ports: 2562

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 387 | 8.8% |
| 2 | `unknown` | 72 | 1.6% |
| 3 | `27015` | 44 | 1.0% |
| 4 | `8080` | 38 | 0.9% |
| 5 | `22` | 36 | 0.8% |
| 6 | `1433` | 29 | 0.7% |
| 7 | `3389` | 25 | 0.6% |
| 8 | `8443` | 22 | 0.5% |
| 9 | `8081` | 21 | 0.5% |
| 10 | `81` | 20 | 0.5% |
| 11 | `5060` | 17 | 0.4% |
| 12 | `53` | 17 | 0.4% |
| 13 | `88` | 16 | 0.4% |
| 14 | `1900` | 16 | 0.4% |
| 15 | `1723` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3921 | 88.7% |
| 2 | `UDP` | 428 | 9.7% |
| 3 | `47` | 70 | 1.6% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `210.16.100.120` | 302 | 6.8% |
| 2 | `62.210.142.176` | 158 | 3.6% |
| 3 | `59.74.227.233` | 25 | 0.6% |
| 4 | `85.217.149.41` | 24 | 0.5% |
| 5 | `85.217.149.20` | 18 | 0.4% |
| 6 | `93.123.72.183` | 16 | 0.4% |
| 7 | `85.217.149.47` | 15 | 0.3% |
| 8 | `85.217.149.34` | 14 | 0.3% |
| 9 | `151.101.219.52` | 14 | 0.3% |
| 10 | `3.142.170.60` | 13 | 0.3% |
| 11 | `85.217.149.42` | 13 | 0.3% |
| 12 | `18.190.15.50` | 12 | 0.3% |
| 13 | `170.51.247.16` | 12 | 0.3% |
| 14 | `170.51.247.42` | 11 | 0.2% |
| 15 | `185.224.128.16` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3773 | 96.2% |
| 2 | `ACK+FIN+PSH` | 75 | 1.9% |
| 3 | `ACK+PSH` | 44 | 1.1% |
| 4 | `ACK+FIN` | 10 | 0.3% |
| 5 | `ACK+RST` | 10 | 0.3% |
| 6 | `SYN+ECE+CWR` | 5 | 0.1% |
| 7 | `ACK` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4415 | 99.9% |
| 2 | `wlan0` | 6 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `210.16.100.120` -> `23` | 302 | 6.8% |
| 2 | `24.199.88.4` -> `23` | 11 | 0.2% |
| 3 | `62.210.142.176` -> `1912` | 9 | 0.2% |
| 4 | `62.210.142.176` -> `1987` | 9 | 0.2% |
| 5 | `62.210.142.176` -> `1999` | 8 | 0.2% |
| 6 | `62.210.142.176` -> `2022` | 8 | 0.2% |
| 7 | `62.210.142.176` -> `2079` | 8 | 0.2% |
| 8 | `170.51.247.42` -> `49743` | 7 | 0.2% |
| 9 | `62.210.142.176` -> `2018` | 7 | 0.2% |
| 10 | `62.210.142.176` -> `2080` | 7 | 0.2% |
| 11 | `178.20.210.152` -> `1723` | 6 | 0.1% |
| 12 | `62.210.142.176` -> `1988` | 6 | 0.1% |
| 13 | `62.210.142.176` -> `2001` | 6 | 0.1% |
| 14 | `62.210.142.176` -> `2002` | 6 | 0.1% |
| 15 | `69.17.52.1` -> `8333` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-12 04:00:00:00 | 145 | 3.3% |
| 2026-06-12 05:00:00:00 | 180 | 4.1% |
| 2026-06-12 06:00:00:00 | 179 | 4.0% |
| 2026-06-12 07:00:00:00 | 180 | 4.1% |
| 2026-06-12 08:00:00:00 | 181 | 4.1% |
| 2026-06-12 09:00:00:00 | 180 | 4.1% |
| 2026-06-12 10:00:00:00 | 182 | 4.1% |
| 2026-06-12 11:00:00:00 | 189 | 4.3% |
| 2026-06-12 12:00:00:00 | 180 | 4.1% |
| 2026-06-12 13:00:00:00 | 178 | 4.0% |
| 2026-06-12 14:00:00:00 | 182 | 4.1% |
| 2026-06-12 15:00:00:00 | 180 | 4.1% |
| 2026-06-12 16:00:00:00 | 197 | 4.5% |
| 2026-06-12 17:00:00:00 | 178 | 4.0% |
| 2026-06-12 18:00:00:00 | 186 | 4.2% |
| 2026-06-12 19:00:00:00 | 196 | 4.4% |
| 2026-06-12 20:00:00:00 | 188 | 4.3% |
| 2026-06-12 21:00:00:00 | 179 | 4.0% |
| 2026-06-12 22:00:00:00 | 181 | 4.1% |
| 2026-06-12 23:00:00:00 | 180 | 4.1% |
| 2026-06-13 00:00:00:00 | 179 | 4.0% |
| 2026-06-13 01:00:00:00 | 186 | 4.2% |
| 2026-06-13 02:00:00:00 | 198 | 4.5% |
| 2026-06-13 03:00:00:00 | 191 | 4.3% |
| 2026-06-13 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dallas, United States | 302 | 45.9% |
| 2 | Paris, France | 158 | 24.0% |
| 3 | New York, United States | 56 | 8.5% |
| 4 | Buenos Aires, Argentina | 37 | 5.6% |
| 5 | Beauharnois, Canada | 28 | 4.3% |
| 6 | Xi'an, China | 25 | 3.8% |
| 7 | Dublin, United States | 25 | 3.8% |
| 8 | Amsterdam, Netherlands | 16 | 2.4% |
| 9 | Amsterdam, The Netherlands | 11 | 1.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `210.16.100.120` | 302 | 45.9% | United States / Texas / Dallas / Scalebuzz Solutions Pvt Ltd | Hosting/Cloud (psychz) |
| 2 | `62.210.142.176` | 158 | 24.0% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 3 | `59.74.227.233` | 25 | 3.8% | China / Shaanxi / Xi'an / XAR Cernet | No apparent signal |
| 4 | `85.217.149.41` | 24 | 3.6% | United States / New York / New York / Modat B.V | No apparent signal |
| 5 | `85.217.149.20` | 18 | 2.7% | United States / New York / New York / Modat B.V | No apparent signal |
| 6 | `93.123.72.183` | 16 | 2.4% | Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 7 | `85.217.149.47` | 15 | 2.3% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 8 | `85.217.149.34` | 14 | 2.1% | United States / New York / New York / Modat B.V | No apparent signal |
| 9 | `151.101.219.52` | 14 | 2.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 10 | `3.142.170.60` | 13 | 2.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `85.217.149.42` | 13 | 2.0% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 12 | `18.190.15.50` | 12 | 1.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `170.51.247.16` | 12 | 1.8% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 14 | `170.51.247.42` | 11 | 1.7% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 15 | `185.224.128.16` | 11 | 1.7% | The Netherlands / North Holland / Amsterdam / Alsycon B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `210.16.100.120` | 302 | 60.5% | Hosting/Cloud (psychz) | United States / Texas / Dallas / Scalebuzz Solutions Pvt Ltd |
| 2 | `62.210.142.176` | 158 | 31.7% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 3 | `151.101.219.52` | 14 | 2.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `3.142.170.60` | 13 | 2.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.190.15.50` | 12 | 2.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
