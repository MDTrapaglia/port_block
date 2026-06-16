# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4433
- Unique source IPs: 2392
- Unique countries/cities (24h): 425
- Unique destination ports: 2084

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1195 | 27.0% |
| 2 | `unknown` | 75 | 1.7% |
| 3 | `8080` | 35 | 0.8% |
| 4 | `22` | 34 | 0.8% |
| 5 | `27015` | 31 | 0.7% |
| 6 | `3389` | 27 | 0.6% |
| 7 | `5060` | 23 | 0.5% |
| 8 | `8081` | 22 | 0.5% |
| 9 | `8443` | 20 | 0.5% |
| 10 | `161` | 18 | 0.4% |
| 11 | `8000` | 18 | 0.4% |
| 12 | `1433` | 18 | 0.4% |
| 13 | `21` | 16 | 0.4% |
| 14 | `123` | 16 | 0.4% |
| 15 | `5555` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4002 | 90.3% |
| 2 | `UDP` | 356 | 8.0% |
| 3 | `47` | 73 | 1.6% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `152.42.163.59` | 222 | 5.0% |
| 2 | `84.16.231.135` | 217 | 4.9% |
| 3 | `123.165.86.133` | 113 | 2.5% |
| 4 | `186.232.82.113` | 64 | 1.4% |
| 5 | `171.114.229.34` | 60 | 1.4% |
| 6 | `194.180.48.27` | 52 | 1.2% |
| 7 | `37.32.77.132` | 41 | 0.9% |
| 8 | `14.183.169.47` | 39 | 0.9% |
| 9 | `200.3.26.64` | 35 | 0.8% |
| 10 | `113.218.222.16` | 35 | 0.8% |
| 11 | `59.126.36.143` | 34 | 0.8% |
| 12 | `45.153.34.246` | 24 | 0.5% |
| 13 | `204.76.203.78` | 24 | 0.5% |
| 14 | `138.255.10.120` | 22 | 0.5% |
| 15 | `151.101.219.52` | 18 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3854 | 96.3% |
| 2 | `ACK+FIN+PSH` | 98 | 2.4% |
| 3 | `ACK+FIN` | 20 | 0.5% |
| 4 | `ACK+PSH` | 18 | 0.4% |
| 5 | `SYN+ECE+CWR` | 8 | 0.2% |
| 6 | `ACK` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4425 | 99.8% |
| 2 | `wlan0` | 8 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `152.42.163.59` -> `23` | 222 | 5.0% |
| 2 | `84.16.231.135` -> `23` | 217 | 4.9% |
| 3 | `123.165.86.133` -> `23` | 113 | 2.5% |
| 4 | `171.114.229.34` -> `23` | 60 | 1.4% |
| 5 | `37.32.77.132` -> `23` | 41 | 0.9% |
| 6 | `14.183.169.47` -> `23` | 39 | 0.9% |
| 7 | `200.3.26.64` -> `23` | 35 | 0.8% |
| 8 | `113.218.222.16` -> `23` | 35 | 0.8% |
| 9 | `59.126.36.143` -> `23` | 34 | 0.8% |
| 10 | `138.255.10.120` -> `23` | 22 | 0.5% |
| 11 | `192.241.179.233` -> `23` | 8 | 0.2% |
| 12 | `192.168.100.1` -> `68` | 8 | 0.2% |
| 13 | `94.156.152.50` -> `23` | 7 | 0.2% |
| 14 | `151.101.218.73` -> `49207` | 6 | 0.1% |
| 15 | `43.159.95.155` -> `57300` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-15 04:00:00:00 | 146 | 3.3% |
| 2026-06-15 05:00:00:00 | 180 | 4.1% |
| 2026-06-15 06:00:00:00 | 185 | 4.2% |
| 2026-06-15 07:00:00:00 | 180 | 4.1% |
| 2026-06-15 08:00:00:00 | 175 | 3.9% |
| 2026-06-15 09:00:00:00 | 168 | 3.8% |
| 2026-06-15 10:00:00:00 | 183 | 4.1% |
| 2026-06-15 11:00:00:00 | 192 | 4.3% |
| 2026-06-15 12:00:00:00 | 182 | 4.1% |
| 2026-06-15 13:00:00:00 | 180 | 4.1% |
| 2026-06-15 14:00:00:00 | 201 | 4.5% |
| 2026-06-15 15:00:00:00 | 180 | 4.1% |
| 2026-06-15 16:00:00:00 | 180 | 4.1% |
| 2026-06-15 17:00:00:00 | 178 | 4.0% |
| 2026-06-15 18:00:00:00 | 184 | 4.2% |
| 2026-06-15 19:00:00:00 | 180 | 4.1% |
| 2026-06-15 20:00:00:00 | 202 | 4.6% |
| 2026-06-15 21:00:00:00 | 180 | 4.1% |
| 2026-06-15 22:00:00:00 | 182 | 4.1% |
| 2026-06-15 23:00:00:00 | 191 | 4.3% |
| 2026-06-16 00:00:00:00 | 196 | 4.4% |
| 2026-06-16 01:00:00:00 | 192 | 4.3% |
| 2026-06-16 02:00:00:00 | 190 | 4.3% |
| 2026-06-16 03:00:00:00 | 180 | 4.1% |
| 2026-06-16 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Singapore, Singapore | 222 | 22.2% |
| 2 | Frankfurt am Main, Germany | 217 | 21.7% |
| 3 | Harbin, China | 113 | 11.3% |
| 4 | Lins, Brazil | 64 | 6.4% |
| 5 | Shizishan, China | 60 | 6.0% |
| 6 | Berngau, Germany | 52 | 5.2% |
| 7 | Eygelshoven, The Netherlands | 48 | 4.8% |
| 8 | Baku, Azerbaijan | 41 | 4.1% |
| 9 | Ho Chi Minh City, Vietnam | 39 | 3.9% |
| 10 | Belford Roxo, Brazil | 35 | 3.5% |
| 11 | Qingyuan, China | 35 | 3.5% |
| 12 | Miaoli, Taiwan | 34 | 3.4% |
| 13 | São Tomé, Brazil | 22 | 2.2% |
| 14 | Buenos Aires, Argentina | 18 | 1.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `152.42.163.59` | 222 | 22.2% | Singapore / South West / Singapore / Digital Ocean | Hosting/Cloud (digitalocean) |
| 2 | `84.16.231.135` | 217 | 21.7% | Germany / Hesse / Frankfurt am Main / Leaseweb Deutschland GmbH | Hosting/Cloud (leaseweb) |
| 3 | `123.165.86.133` | 113 | 11.3% | China / Heilongjiang / Harbin / Chinanet HL | No apparent signal |
| 4 | `186.232.82.113` | 64 | 6.4% | Brazil / São Paulo / Lins / Eveo S.A | No apparent signal |
| 5 | `171.114.229.34` | 60 | 6.0% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 6 | `194.180.48.27` | 52 | 5.2% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 7 | `37.32.77.132` | 41 | 4.1% | Azerbaijan / Baku City / Baku / SHAKH Telecom LLC | No apparent signal |
| 8 | `14.183.169.47` | 39 | 3.9% | Vietnam / Ho Chi Minh / Ho Chi Minh City / Vietnam Posts and Telecommunications Group | No apparent signal |
| 9 | `200.3.26.64` | 35 | 3.5% | Brazil / Rio de Janeiro / Belford Roxo / Espaco Digital | No apparent signal |
| 10 | `113.218.222.16` | 35 | 3.5% | China / Hunan / Qingyuan / Chinanet HN | No apparent signal |
| 11 | `59.126.36.143` | 34 | 3.4% | Taiwan / Miaoli / Miaoli / Chunghwa Telecom Co. Ltd. | No apparent signal |
| 12 | `45.153.34.246` | 24 | 2.4% | The Netherlands / Limburg / Eygelshoven / VMHeaven.io | No apparent signal |
| 13 | `204.76.203.78` | 24 | 2.4% | The Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 14 | `138.255.10.120` | 22 | 2.2% | Brazil / Rio Grande do Norte / São Tomé / Werbi Provedor E Servicos De Telecomunicacoes Ltda | No apparent signal |
| 15 | `151.101.219.52` | 18 | 1.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `152.42.163.59` | 222 | 48.6% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / Digital Ocean |
| 2 | `84.16.231.135` | 217 | 47.5% | Hosting/Cloud (leaseweb) | Germany / Hesse / Frankfurt am Main / Leaseweb Deutschland GmbH |
| 3 | `151.101.219.52` | 18 | 3.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
