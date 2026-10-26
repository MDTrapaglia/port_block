# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4433
- Unique source IPs: 2580
- Unique countries/cities (24h): 324
- Unique destination ports: 2245

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `7680` | 309 | 7.0% |
| 2 | `23` | 218 | 4.9% |
| 3 | `22` | 85 | 1.9% |
| 4 | `8080` | 44 | 1.0% |
| 5 | `53` | 42 | 0.9% |
| 6 | `5060` | 41 | 0.9% |
| 7 | `3389` | 38 | 0.9% |
| 8 | `1433` | 34 | 0.8% |
| 9 | `8000` | 24 | 0.5% |
| 10 | `8443` | 22 | 0.5% |
| 11 | `1900` | 20 | 0.5% |
| 12 | `21` | 16 | 0.4% |
| 13 | `27017` | 15 | 0.3% |
| 14 | `3306` | 15 | 0.3% |
| 15 | `5432` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4071 | 91.8% |
| 2 | `UDP` | 354 | 8.0% |
| 3 | `47` | 6 | 0.1% |
| 4 | `4` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `68.73.112.130` | 63 | 1.4% |
| 2 | `50.45.252.114` | 54 | 1.2% |
| 3 | `172.59.160.129` | 45 | 1.0% |
| 4 | `216.180.246.95` | 42 | 0.9% |
| 5 | `216.180.246.2` | 35 | 0.8% |
| 6 | `73.17.195.132` | 34 | 0.8% |
| 7 | `108.26.185.186` | 26 | 0.6% |
| 8 | `187.180.70.140` | 26 | 0.6% |
| 9 | `77.91.71.27` | 24 | 0.5% |
| 10 | `67.180.141.91` | 24 | 0.5% |
| 11 | `151.101.218.13` | 21 | 0.5% |
| 12 | `24.6.144.201` | 21 | 0.5% |
| 13 | `76.158.232.86` | 20 | 0.5% |
| 14 | `45.198.224.125` | 18 | 0.4% |
| 15 | `79.124.58.22` | 17 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3907 | 96.0% |
| 2 | `ACK+FIN+PSH` | 105 | 2.6% |
| 3 | `ACK+PSH` | 39 | 1.0% |
| 4 | `ACK+FIN` | 11 | 0.3% |
| 5 | `SYN+ECE+CWR` | 7 | 0.2% |
| 6 | `ACK` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4433 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `68.73.112.130` -> `7680` | 63 | 1.4% |
| 2 | `50.45.252.114` -> `7680` | 54 | 1.2% |
| 3 | `172.59.160.129` -> `7680` | 45 | 1.0% |
| 4 | `73.17.195.132` -> `7680` | 34 | 0.8% |
| 5 | `108.26.185.186` -> `7680` | 26 | 0.6% |
| 6 | `187.180.70.140` -> `23` | 26 | 0.6% |
| 7 | `67.180.141.91` -> `7680` | 24 | 0.5% |
| 8 | `24.6.144.201` -> `7680` | 21 | 0.5% |
| 9 | `76.158.232.86` -> `7680` | 20 | 0.5% |
| 10 | `80.94.92.130` -> `8080` | 10 | 0.2% |
| 11 | `186.123.1.125` -> `1433` | 10 | 0.2% |
| 12 | `216.180.246.95` -> `8989` | 9 | 0.2% |
| 13 | `93.117.42.227` -> `23` | 8 | 0.2% |
| 14 | `193.47.62.187` -> `1900` | 8 | 0.2% |
| 15 | `45.198.224.125` -> `8081` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-25 04:00:00:00 | 154 | 3.5% |
| 2026-10-25 05:00:00:00 | 181 | 4.1% |
| 2026-10-25 06:00:00:00 | 180 | 4.1% |
| 2026-10-25 07:00:00:00 | 180 | 4.1% |
| 2026-10-25 08:00:00:00 | 180 | 4.1% |
| 2026-10-25 09:00:00:00 | 180 | 4.1% |
| 2026-10-25 10:00:00:00 | 180 | 4.1% |
| 2026-10-25 11:00:00:00 | 192 | 4.3% |
| 2026-10-25 12:00:00:00 | 188 | 4.2% |
| 2026-10-25 13:00:00:00 | 181 | 4.1% |
| 2026-10-25 14:00:00:00 | 181 | 4.1% |
| 2026-10-25 15:00:00:00 | 180 | 4.1% |
| 2026-10-25 16:00:00:00 | 179 | 4.0% |
| 2026-10-25 17:00:00:00 | 180 | 4.1% |
| 2026-10-25 18:00:00:00 | 198 | 4.5% |
| 2026-10-25 19:00:00:00 | 192 | 4.3% |
| 2026-10-25 20:00:00:00 | 180 | 4.1% |
| 2026-10-25 21:00:00:00 | 192 | 4.3% |
| 2026-10-25 22:00:00:00 | 191 | 4.3% |
| 2026-10-25 23:00:00:00 | 178 | 4.0% |
| 2026-10-26 00:00:00:00 | 189 | 4.3% |
| 2026-10-26 01:00:00:00 | 182 | 4.1% |
| 2026-10-26 02:00:00:00 | 191 | 4.3% |
| 2026-10-26 03:00:00:00 | 181 | 4.1% |
| 2026-10-26 04:00:00:00 | 43 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 77 | 16.4% |
| 2 | San Jose, United States | 69 | 14.7% |
| 3 | Raleigh, United States | 63 | 13.4% |
| 4 | Tigard, United States | 54 | 11.5% |
| 5 | Boston, United States | 34 | 7.2% |
| 6 | Newton, United States | 26 | 5.5% |
| 7 | Belém, Brazil | 26 | 5.5% |
| 8 | Tel Aviv, Israel | 24 | 5.1% |
| 9 | Buenos Aires, Argentina | 21 | 4.5% |
| 10 | Santa Clara, United States | 21 | 4.5% |
| 11 | Roseville, United States | 20 | 4.3% |
| 12 | Stockholm, Sweden | 18 | 3.8% |
| 13 | Sofia, Bulgaria | 17 | 3.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `68.73.112.130` | 63 | 13.4% | United States / North Carolina / Raleigh / PPPoX Pool - Rback2 EHMIL | No apparent signal |
| 2 | `50.45.252.114` | 54 | 11.5% | United States / Oregon / Tigard / Ziply Fiber | No apparent signal |
| 3 | `172.59.160.129` | 45 | 9.6% | United States / California / San Jose / T-Mobile USA, Inc. | Mobile/CGNAT (mobile) |
| 4 | `216.180.246.95` | 42 | 8.9% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 5 | `216.180.246.2` | 35 | 7.4% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 6 | `73.17.195.132` | 34 | 7.2% | United States / Massachusetts / Boston / Comcast Cable Communications, LLC | No apparent signal |
| 7 | `108.26.185.186` | 26 | 5.5% | United States / Massachusetts / Newton / MCI Communications Services, Inc. d/b/a Verizon Business | No apparent signal |
| 8 | `187.180.70.140` | 26 | 5.5% | Brazil / Pará / Belém / NET Serviços de Comunicação S.A. | Mobile/CGNAT (claro) |
| 9 | `77.91.71.27` | 24 | 5.1% | Israel / Tel Aviv / Tel Aviv / NEW | No apparent signal |
| 10 | `67.180.141.91` | 24 | 5.1% | United States / California / San Jose / Comcast Cable Communications, Inc | No apparent signal |
| 11 | `151.101.218.13` | 21 | 4.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 12 | `24.6.144.201` | 21 | 4.5% | United States / California / Santa Clara / Comcast Cable Communications | No apparent signal |
| 13 | `76.158.232.86` | 20 | 4.3% | United States / California / Roseville / Comcast Cable Communications, LLC | No apparent signal |
| 14 | `45.198.224.125` | 18 | 3.8% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 15 | `79.124.58.22` | 17 | 3.6% | Bulgaria / Sofia-Capital / Sofia / Laado Raani Private Housing Space | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.95` | 42 | 42.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `216.180.246.2` | 35 | 35.7% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 3 | `151.101.218.13` | 21 | 21.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
