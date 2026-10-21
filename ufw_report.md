# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4384
- Unique source IPs: 2635
- Unique countries/cities (24h): 545
- Unique destination ports: 1667

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1905 | 43.5% |
| 2 | `22` | 40 | 0.9% |
| 3 | `8080` | 30 | 0.7% |
| 4 | `3389` | 23 | 0.5% |
| 5 | `8443` | 18 | 0.4% |
| 6 | `5060` | 16 | 0.4% |
| 7 | `8000` | 15 | 0.3% |
| 8 | `1433` | 13 | 0.3% |
| 9 | `1900` | 13 | 0.3% |
| 10 | `21` | 12 | 0.3% |
| 11 | `53` | 12 | 0.3% |
| 12 | `3306` | 12 | 0.3% |
| 13 | `1723` | 12 | 0.3% |
| 14 | `123` | 11 | 0.3% |
| 15 | `161` | 9 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4202 | 95.8% |
| 2 | `UDP` | 180 | 4.1% |
| 3 | `47` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `179.62.253.144` | 108 | 2.5% |
| 2 | `5.237.86.232` | 68 | 1.6% |
| 3 | `123.169.107.169` | 68 | 1.6% |
| 4 | `38.46.30.51` | 66 | 1.5% |
| 5 | `162.248.101.157` | 51 | 1.2% |
| 6 | `88.204.153.114` | 50 | 1.1% |
| 7 | `151.101.218.13` | 30 | 0.7% |
| 8 | `5.237.96.117` | 28 | 0.6% |
| 9 | `5.27.166.171` | 27 | 0.6% |
| 10 | `59.93.109.198` | 23 | 0.5% |
| 11 | `59.180.172.218` | 23 | 0.5% |
| 12 | `27.24.91.128` | 21 | 0.5% |
| 13 | `85.217.149.37` | 13 | 0.3% |
| 14 | `91.231.89.150` | 11 | 0.3% |
| 15 | `91.231.89.205` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 4116 | 98.0% |
| 2 | `ACK+FIN+PSH` | 58 | 1.4% |
| 3 | `ACK+PSH` | 16 | 0.4% |
| 4 | `SYN+ECE+CWR` | 6 | 0.1% |
| 5 | `ACK+FIN` | 6 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4384 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `179.62.253.144` -> `23` | 108 | 2.5% |
| 2 | `5.237.86.232` -> `23` | 68 | 1.6% |
| 3 | `123.169.107.169` -> `23` | 68 | 1.6% |
| 4 | `38.46.30.51` -> `23` | 66 | 1.5% |
| 5 | `88.204.153.114` -> `23` | 50 | 1.1% |
| 6 | `5.237.96.117` -> `23` | 28 | 0.6% |
| 7 | `5.27.166.171` -> `23` | 27 | 0.6% |
| 8 | `59.93.109.198` -> `23` | 23 | 0.5% |
| 9 | `59.180.172.218` -> `23` | 23 | 0.5% |
| 10 | `27.24.91.128` -> `23` | 21 | 0.5% |
| 11 | `1.182.30.99` -> `23` | 11 | 0.3% |
| 12 | `196.191.104.40` -> `23` | 7 | 0.2% |
| 13 | `151.101.218.13` -> `55090` | 7 | 0.2% |
| 14 | `188.28.190.186` -> `23` | 6 | 0.1% |
| 15 | `45.205.1.160` -> `6036` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-20 04:00:00:00 | 135 | 3.1% |
| 2026-10-20 05:00:00:00 | 180 | 4.1% |
| 2026-10-20 06:00:00:00 | 180 | 4.1% |
| 2026-10-20 07:00:00:00 | 179 | 4.1% |
| 2026-10-20 08:00:00:00 | 181 | 4.1% |
| 2026-10-20 09:00:00:00 | 180 | 4.1% |
| 2026-10-20 10:00:00:00 | 179 | 4.1% |
| 2026-10-20 11:00:00:00 | 181 | 4.1% |
| 2026-10-20 12:00:00:00 | 183 | 4.2% |
| 2026-10-20 13:00:00:00 | 188 | 4.3% |
| 2026-10-20 14:00:00:00 | 180 | 4.1% |
| 2026-10-20 15:00:00:00 | 191 | 4.4% |
| 2026-10-20 16:00:00:00 | 181 | 4.1% |
| 2026-10-20 17:00:00:00 | 187 | 4.3% |
| 2026-10-20 18:00:00:00 | 189 | 4.3% |
| 2026-10-20 19:00:00:00 | 189 | 4.3% |
| 2026-10-20 20:00:00:00 | 181 | 4.1% |
| 2026-10-20 21:00:00:00 | 180 | 4.1% |
| 2026-10-20 22:00:00:00 | 179 | 4.1% |
| 2026-10-20 23:00:00:00 | 182 | 4.2% |
| 2026-10-21 00:00:00:00 | 186 | 4.2% |
| 2026-10-21 01:00:00:00 | 188 | 4.3% |
| 2026-10-21 02:00:00:00 | 180 | 4.1% |
| 2026-10-21 03:00:00:00 | 179 | 4.1% |
| 2026-10-21 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Veinticinco de Mayo, Argentina | 108 | 18.1% |
| 2 | Karaj, Iran | 96 | 16.1% |
| 3 | Jinan, China | 68 | 11.4% |
| 4 | Baní, Dominican Republic | 66 | 11.0% |
| 5 | New York, United States | 51 | 8.5% |
| 6 | Almaty, Kazakhstan | 50 | 8.4% |
| 7 | Buenos Aires, Argentina | 30 | 5.0% |
| 8 | Istanbul, Türkiye | 27 | 4.5% |
| 9 | Bengaluru, India | 23 | 3.8% |
| 10 | Shāhdara, India | 23 | 3.8% |
| 11 | Gravelines, France | 22 | 3.7% |
| 12 | Shizishan, China | 21 | 3.5% |
| 13 | Beauharnois, Canada | 13 | 2.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `179.62.253.144` | 108 | 18.1% | Argentina / Buenos Aires / Veinticinco de Mayo / Red Intercable Digital S.A | No apparent signal |
| 2 | `5.237.86.232` | 68 | 11.4% | Iran / Alborz Province / Karaj / Telecommunication Company of Alborz | No apparent signal |
| 3 | `123.169.107.169` | 68 | 11.4% | China / Shandong / Jinan / Chinanet SD | No apparent signal |
| 4 | `38.46.30.51` | 66 | 11.0% | Dominican Republic / Peravia / Baní / Telecable Banilejo S.R.L | No apparent signal |
| 5 | `162.248.101.157` | 51 | 8.5% | United States / New York / New York / GALAXYGATE, LLC | No apparent signal |
| 6 | `88.204.153.114` | 50 | 8.4% | Kazakhstan / Almaty / Almaty / Rgurk | No apparent signal |
| 7 | `151.101.218.13` | 30 | 5.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 8 | `5.237.96.117` | 28 | 4.7% | Iran / Alborz Province / Karaj / Telecommunication Company of Alborz | No apparent signal |
| 9 | `5.27.166.171` | 27 | 4.5% | Türkiye / Istanbul / Istanbul / Turkcell Internet | No apparent signal |
| 10 | `59.93.109.198` | 23 | 3.8% | India / Karnataka / Bengaluru / BSNL Internet | No apparent signal |
| 11 | `59.180.172.218` | 23 | 3.8% | India / National Capital Territory of Delhi / Shāhdara / MTNL Mumbai | No apparent signal |
| 12 | `27.24.91.128` | 21 | 3.5% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 13 | `85.217.149.37` | 13 | 2.2% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 14 | `91.231.89.150` | 11 | 1.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `91.231.89.205` | 11 | 1.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 30 | 100.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
