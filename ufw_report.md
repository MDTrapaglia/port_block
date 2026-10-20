# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4405
- Unique source IPs: 2631
- Unique countries/cities (24h): 551
- Unique destination ports: 1425

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 2243 | 50.9% |
| 2 | `22` | 41 | 0.9% |
| 3 | `5060` | 28 | 0.6% |
| 4 | `53` | 22 | 0.5% |
| 5 | `8080` | 18 | 0.4% |
| 6 | `3389` | 17 | 0.4% |
| 7 | `8443` | 14 | 0.3% |
| 8 | `161` | 13 | 0.3% |
| 9 | `81` | 11 | 0.2% |
| 10 | `8000` | 10 | 0.2% |
| 11 | `8081` | 10 | 0.2% |
| 12 | `1433` | 9 | 0.2% |
| 13 | `3306` | 9 | 0.2% |
| 14 | `25` | 9 | 0.2% |
| 15 | `6379` | 8 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4195 | 95.2% |
| 2 | `UDP` | 205 | 4.7% |
| 3 | `47` | 5 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `24.152.7.98` | 81 | 1.8% |
| 2 | `123.173.90.220` | 68 | 1.5% |
| 3 | `222.127.243.18` | 65 | 1.5% |
| 4 | `116.207.115.184` | 58 | 1.3% |
| 5 | `5.237.91.18` | 57 | 1.3% |
| 6 | `175.9.134.159` | 56 | 1.3% |
| 7 | `2.180.132.225` | 53 | 1.2% |
| 8 | `222.217.26.133` | 51 | 1.2% |
| 9 | `119.99.251.151` | 49 | 1.1% |
| 10 | `59.180.176.51` | 42 | 1.0% |
| 11 | `42.100.27.130` | 36 | 0.8% |
| 12 | `151.101.218.13` | 33 | 0.7% |
| 13 | `171.114.225.97` | 27 | 0.6% |
| 14 | `175.43.119.91` | 26 | 0.6% |
| 15 | `118.249.40.234` | 22 | 0.5% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 4096 | 97.6% |
| 2 | `ACK+FIN+PSH` | 78 | 1.9% |
| 3 | `ACK+PSH` | 11 | 0.3% |
| 4 | `ACK+FIN` | 6 | 0.1% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4405 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `24.152.7.98` -> `23` | 81 | 1.8% |
| 2 | `123.173.90.220` -> `23` | 68 | 1.5% |
| 3 | `222.127.243.18` -> `23` | 65 | 1.5% |
| 4 | `116.207.115.184` -> `23` | 58 | 1.3% |
| 5 | `5.237.91.18` -> `23` | 57 | 1.3% |
| 6 | `175.9.134.159` -> `23` | 56 | 1.3% |
| 7 | `2.180.132.225` -> `23` | 53 | 1.2% |
| 8 | `222.217.26.133` -> `23` | 51 | 1.2% |
| 9 | `119.99.251.151` -> `23` | 49 | 1.1% |
| 10 | `59.180.176.51` -> `23` | 42 | 1.0% |
| 11 | `42.100.27.130` -> `23` | 36 | 0.8% |
| 12 | `171.114.225.97` -> `23` | 27 | 0.6% |
| 13 | `175.43.119.91` -> `23` | 26 | 0.6% |
| 14 | `118.249.40.234` -> `23` | 22 | 0.5% |
| 15 | `45.238.26.39` -> `23` | 20 | 0.5% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-19 04:00:00:00 | 136 | 3.1% |
| 2026-10-19 05:00:00:00 | 179 | 4.1% |
| 2026-10-19 06:00:00:00 | 181 | 4.1% |
| 2026-10-19 07:00:00:00 | 190 | 4.3% |
| 2026-10-19 08:00:00:00 | 195 | 4.4% |
| 2026-10-19 09:00:00:00 | 183 | 4.2% |
| 2026-10-19 10:00:00:00 | 205 | 4.7% |
| 2026-10-19 11:00:00:00 | 178 | 4.0% |
| 2026-10-19 12:00:00:00 | 182 | 4.1% |
| 2026-10-19 13:00:00:00 | 180 | 4.1% |
| 2026-10-19 14:00:00:00 | 179 | 4.1% |
| 2026-10-19 15:00:00:00 | 181 | 4.1% |
| 2026-10-19 16:00:00:00 | 180 | 4.1% |
| 2026-10-19 17:00:00:00 | 180 | 4.1% |
| 2026-10-19 18:00:00:00 | 186 | 4.2% |
| 2026-10-19 19:00:00:00 | 180 | 4.1% |
| 2026-10-19 20:00:00:00 | 182 | 4.1% |
| 2026-10-19 21:00:00:00 | 181 | 4.1% |
| 2026-10-19 22:00:00:00 | 189 | 4.3% |
| 2026-10-19 23:00:00:00 | 180 | 4.1% |
| 2026-10-20 00:00:00:00 | 180 | 4.1% |
| 2026-10-20 01:00:00:00 | 179 | 4.1% |
| 2026-10-20 02:00:00:00 | 194 | 4.4% |
| 2026-10-20 03:00:00:00 | 179 | 4.1% |
| 2026-10-20 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Shizishan, China | 134 | 18.5% |
| 2 | Manaus, Brazil | 81 | 11.2% |
| 3 | Jilin, China | 68 | 9.4% |
| 4 | Iloilo City, Philippines | 65 | 9.0% |
| 5 | Karaj, Iran | 57 | 7.9% |
| 6 | Changsha, China | 56 | 7.7% |
| 7 | Tehran, Iran | 53 | 7.3% |
| 8 | Liuzhou, China | 51 | 7.0% |
| 9 | New Delhi, India | 42 | 5.8% |
| 10 | Harbin, China | 36 | 5.0% |
| 11 | Buenos Aires, Argentina | 33 | 4.6% |
| 12 | Quanzhou, China | 26 | 3.6% |
| 13 | Qingyuan, China | 22 | 3.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `24.152.7.98` | 81 | 11.2% | Brazil / Amazonas / Manaus / NEW CLICK TELECOMUNICACOES LTDA | Hosting/Cloud (amazon) |
| 2 | `123.173.90.220` | 68 | 9.4% | China / Jilin / Jilin / Chinanet JL | No apparent signal |
| 3 | `222.127.243.18` | 65 | 9.0% | Philippines / Western Visayas / Iloilo City / GLBB | No apparent signal |
| 4 | `116.207.115.184` | 58 | 8.0% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 5 | `5.237.91.18` | 57 | 7.9% | Iran / Alborz Province / Karaj / Telecommunication Company of Alborz | No apparent signal |
| 6 | `175.9.134.159` | 56 | 7.7% | China / Hunan / Changsha / Chinanet HN | No apparent signal |
| 7 | `2.180.132.225` | 53 | 7.3% | Iran / Tehran / Tehran / Telecommunication Company | No apparent signal |
| 8 | `222.217.26.133` | 51 | 7.0% | China / Guangxi / Liuzhou / Chinanet GX | No apparent signal |
| 9 | `119.99.251.151` | 49 | 6.8% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 10 | `59.180.176.51` | 42 | 5.8% | India / National Capital Territory of Delhi / New Delhi / MTNL Mumbai | No apparent signal |
| 11 | `42.100.27.130` | 36 | 5.0% | China / Heilongjiang / Harbin / Chinanet HL | No apparent signal |
| 12 | `151.101.218.13` | 33 | 4.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 13 | `171.114.225.97` | 27 | 3.7% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 14 | `175.43.119.91` | 26 | 3.6% | China / Fujian / Quanzhou / China Unicom Fujian Province Network | No apparent signal |
| 15 | `118.249.40.234` | 22 | 3.0% | China / Hunan / Qingyuan / Chinanet HN | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `24.152.7.98` | 81 | 71.1% | Hosting/Cloud (amazon) | Brazil / Amazonas / Manaus / NEW CLICK TELECOMUNICACOES LTDA |
| 2 | `151.101.218.13` | 33 | 28.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
