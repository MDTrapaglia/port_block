# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4364
- Unique source IPs: 2647
- Unique countries/cities (24h): 493
- Unique destination ports: 1638

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1911 | 43.8% |
| 2 | `22` | 46 | 1.1% |
| 3 | `8080` | 25 | 0.6% |
| 4 | `3389` | 24 | 0.5% |
| 5 | `5060` | 18 | 0.4% |
| 6 | `53` | 17 | 0.4% |
| 7 | `8443` | 14 | 0.3% |
| 8 | `1433` | 12 | 0.3% |
| 9 | `3306` | 11 | 0.3% |
| 10 | `110` | 11 | 0.3% |
| 11 | `21` | 11 | 0.3% |
| 12 | `81` | 11 | 0.3% |
| 13 | `9000` | 11 | 0.3% |
| 14 | `2000` | 10 | 0.2% |
| 15 | `161` | 10 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4168 | 95.5% |
| 2 | `UDP` | 193 | 4.4% |
| 3 | `47` | 3 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `116.208.67.23` | 91 | 2.1% |
| 2 | `121.57.71.54` | 74 | 1.7% |
| 3 | `196.189.130.28` | 73 | 1.7% |
| 4 | `123.165.80.41` | 72 | 1.6% |
| 5 | `119.99.249.169` | 72 | 1.6% |
| 6 | `222.127.63.230` | 70 | 1.6% |
| 7 | `77.91.71.26` | 56 | 1.3% |
| 8 | `5.101.140.66` | 55 | 1.3% |
| 9 | `42.100.26.85` | 53 | 1.2% |
| 10 | `16.5.0.240` | 30 | 0.7% |
| 11 | `138.117.120.230` | 19 | 0.4% |
| 12 | `175.0.21.74` | 16 | 0.4% |
| 13 | `112.103.63.242` | 15 | 0.3% |
| 14 | `185.149.235.44` | 14 | 0.3% |
| 15 | `23.129.232.164` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 4103 | 98.4% |
| 2 | `ACK+FIN+PSH` | 42 | 1.0% |
| 3 | `ACK+PSH` | 10 | 0.2% |
| 4 | `ACK` | 7 | 0.2% |
| 5 | `ACK+FIN` | 3 | 0.1% |
| 6 | `SYN+ECE+CWR` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4364 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `116.208.67.23` -> `23` | 91 | 2.1% |
| 2 | `121.57.71.54` -> `23` | 74 | 1.7% |
| 3 | `196.189.130.28` -> `23` | 73 | 1.7% |
| 4 | `123.165.80.41` -> `23` | 72 | 1.6% |
| 5 | `119.99.249.169` -> `23` | 72 | 1.6% |
| 6 | `222.127.63.230` -> `23` | 70 | 1.6% |
| 7 | `42.100.26.85` -> `23` | 53 | 1.2% |
| 8 | `138.117.120.230` -> `23` | 19 | 0.4% |
| 9 | `175.0.21.74` -> `23` | 16 | 0.4% |
| 10 | `112.103.63.242` -> `23` | 15 | 0.3% |
| 11 | `176.91.225.174` -> `23` | 11 | 0.3% |
| 12 | `105.186.221.67` -> `23` | 10 | 0.2% |
| 13 | `118.42.236.23` -> `23` | 9 | 0.2% |
| 14 | `201.110.177.47` -> `23` | 9 | 0.2% |
| 15 | `151.101.218.13` -> `50096` | 8 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-18 04:00:00:00 | 139 | 3.2% |
| 2026-10-18 05:00:00:00 | 180 | 4.1% |
| 2026-10-18 06:00:00:00 | 178 | 4.1% |
| 2026-10-18 07:00:00:00 | 182 | 4.2% |
| 2026-10-18 08:00:00:00 | 179 | 4.1% |
| 2026-10-18 09:00:00:00 | 181 | 4.1% |
| 2026-10-18 10:00:00:00 | 180 | 4.1% |
| 2026-10-18 11:00:00:00 | 180 | 4.1% |
| 2026-10-18 12:00:00:00 | 180 | 4.1% |
| 2026-10-18 13:00:00:00 | 179 | 4.1% |
| 2026-10-18 14:00:00:00 | 180 | 4.1% |
| 2026-10-18 15:00:00:00 | 181 | 4.1% |
| 2026-10-18 16:00:00:00 | 180 | 4.1% |
| 2026-10-18 17:00:00:00 | 179 | 4.1% |
| 2026-10-18 18:00:00:00 | 181 | 4.1% |
| 2026-10-18 19:00:00:00 | 180 | 4.1% |
| 2026-10-18 20:00:00:00 | 178 | 4.1% |
| 2026-10-18 21:00:00:00 | 181 | 4.1% |
| 2026-10-18 22:00:00:00 | 197 | 4.5% |
| 2026-10-18 23:00:00:00 | 199 | 4.6% |
| 2026-10-19 00:00:00:00 | 179 | 4.1% |
| 2026-10-19 01:00:00:00 | 183 | 4.2% |
| 2026-10-19 02:00:00:00 | 183 | 4.2% |
| 2026-10-19 03:00:00:00 | 180 | 4.1% |
| 2026-10-19 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Shizishan, China | 163 | 22.5% |
| 2 | Harbin, China | 140 | 19.4% |
| 3 | Hechi, China | 74 | 10.2% |
| 4 | Addis Ababa, Ethiopia | 73 | 10.1% |
| 5 | Lahug, Philippines | 70 | 9.7% |
| 6 | Tel Aviv, Israel | 56 | 7.7% |
| 7 | London, United Kingdom | 55 | 7.6% |
| 8 | São Paulo, Brazil | 30 | 4.1% |
| 9 | Kansas City, United States | 27 | 3.7% |
| 10 | Assis, Brazil | 19 | 2.6% |
| 11 | Changsha, China | 16 | 2.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `116.208.67.23` | 91 | 12.6% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 2 | `121.57.71.54` | 74 | 10.2% | China / Guangxi / Hechi / Neimeng Network of ChinaTelecom | No apparent signal |
| 3 | `196.189.130.28` | 73 | 10.1% | Ethiopia / Addis Ababa / Addis Ababa / Ethiotelecom | VPN/Proxy suspected (pia) |
| 4 | `123.165.80.41` | 72 | 10.0% | China / Heilongjiang / Harbin / Chinanet HL | No apparent signal |
| 5 | `119.99.249.169` | 72 | 10.0% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 6 | `222.127.63.230` | 70 | 9.7% | Philippines / Central Visayas / Lahug / Globe Telecom | No apparent signal |
| 7 | `77.91.71.26` | 56 | 7.7% | Israel / Tel Aviv / Tel Aviv / NEW | No apparent signal |
| 8 | `5.101.140.66` | 55 | 7.6% | United Kingdom / England / London / Hostmedialtd | Hosting/Cloud (servers) |
| 9 | `42.100.26.85` | 53 | 7.3% | China / Heilongjiang / Harbin / Chinanet HL | No apparent signal |
| 10 | `16.5.0.240` | 30 | 4.1% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 11 | `138.117.120.230` | 19 | 2.6% | Brazil / São Paulo / Assis / OnLine Assis Telecomunicações Ltda-EPP | No apparent signal |
| 12 | `175.0.21.74` | 16 | 2.2% | China / Hunan / Changsha / Chinanet HN | No apparent signal |
| 13 | `112.103.63.242` | 15 | 2.1% | China / Heilongjiang / Harbin / Chinanet HL | No apparent signal |
| 14 | `185.149.235.44` | 14 | 1.9% | United States / Missouri / Kansas City / Heymman Servers Corporation | Hosting/Cloud (servers) |
| 15 | `23.129.232.164` | 13 | 1.8% | United States / Missouri / Kansas City / Heymman Servers Corporation | Hosting/Cloud (servers) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `196.189.130.28` | 73 | 47.1% | VPN/Proxy suspected (pia) | Ethiopia / Addis Ababa / Addis Ababa / Ethiotelecom |
| 2 | `5.101.140.66` | 55 | 35.5% | Hosting/Cloud (servers) | United Kingdom / England / London / Hostmedialtd |
| 3 | `185.149.235.44` | 14 | 9.0% | Hosting/Cloud (servers) | United States / Missouri / Kansas City / Heymman Servers Corporation |
| 4 | `23.129.232.164` | 13 | 8.4% | Hosting/Cloud (servers) | United States / Missouri / Kansas City / Heymman Servers Corporation |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
