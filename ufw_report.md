# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4394
- Unique source IPs: 2214
- Unique countries/cities (24h): 265
- Unique destination ports: 2801

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `7680` | 157 | 3.6% |
| 2 | `23` | 111 | 2.5% |
| 3 | `22` | 70 | 1.6% |
| 4 | `3389` | 44 | 1.0% |
| 5 | `8080` | 39 | 0.9% |
| 6 | `5060` | 34 | 0.8% |
| 7 | `8443` | 27 | 0.6% |
| 8 | `1433` | 22 | 0.5% |
| 9 | `53` | 22 | 0.5% |
| 10 | `8000` | 16 | 0.4% |
| 11 | `9200` | 16 | 0.4% |
| 12 | `3306` | 16 | 0.4% |
| 13 | `8081` | 16 | 0.4% |
| 14 | `1723` | 14 | 0.3% |
| 15 | `5432` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4088 | 93.0% |
| 2 | `UDP` | 293 | 6.7% |
| 3 | `47` | 10 | 0.2% |
| 4 | `41` | 3 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `77.239.124.201` | 556 | 12.7% |
| 2 | `24.147.173.252` | 41 | 0.9% |
| 3 | `76.103.223.155` | 30 | 0.7% |
| 4 | `151.101.218.13` | 17 | 0.4% |
| 5 | `68.73.112.130` | 16 | 0.4% |
| 6 | `77.91.71.27` | 15 | 0.3% |
| 7 | `91.231.89.104` | 14 | 0.3% |
| 8 | `91.230.168.190` | 13 | 0.3% |
| 9 | `151.101.218.73` | 13 | 0.3% |
| 10 | `35.146.33.153` | 13 | 0.3% |
| 11 | `91.231.89.130` | 12 | 0.3% |
| 12 | `91.231.89.0` | 12 | 0.3% |
| 13 | `91.231.89.117` | 12 | 0.3% |
| 14 | `91.231.89.251` | 12 | 0.3% |
| 15 | `91.231.89.205` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3973 | 97.2% |
| 2 | `ACK+FIN+PSH` | 65 | 1.6% |
| 3 | `ACK+PSH` | 34 | 0.8% |
| 4 | `ACK+FIN` | 9 | 0.2% |
| 5 | `SYN+ECE+CWR` | 7 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4394 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `24.147.173.252` -> `7680` | 41 | 0.9% |
| 2 | `76.103.223.155` -> `7680` | 30 | 0.7% |
| 3 | `68.73.112.130` -> `7680` | 16 | 0.4% |
| 4 | `35.146.33.153` -> `7680` | 13 | 0.3% |
| 5 | `172.59.160.129` -> `7680` | 11 | 0.3% |
| 6 | `2.185.240.80` -> `23` | 10 | 0.2% |
| 7 | `50.45.252.114` -> `7680` | 9 | 0.2% |
| 8 | `76.158.232.86` -> `7680` | 9 | 0.2% |
| 9 | `62.210.114.99` -> `3389` | 8 | 0.2% |
| 10 | `73.17.195.132` -> `7680` | 8 | 0.2% |
| 11 | `151.101.218.73` -> `12625` | 6 | 0.1% |
| 12 | `182.123.245.238` -> `23` | 6 | 0.1% |
| 13 | `99.65.177.165` -> `7680` | 6 | 0.1% |
| 14 | `45.198.224.125` -> `8080` | 5 | 0.1% |
| 15 | `178.20.210.152` -> `1723` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-23 04:00:00:00 | 135 | 3.1% |
| 2026-10-23 05:00:00:00 | 180 | 4.1% |
| 2026-10-23 06:00:00:00 | 180 | 4.1% |
| 2026-10-23 07:00:00:00 | 181 | 4.1% |
| 2026-10-23 08:00:00:00 | 187 | 4.3% |
| 2026-10-23 09:00:00:00 | 180 | 4.1% |
| 2026-10-23 10:00:00:00 | 180 | 4.1% |
| 2026-10-23 11:00:00:00 | 180 | 4.1% |
| 2026-10-23 12:00:00:00 | 175 | 4.0% |
| 2026-10-23 13:00:00:00 | 201 | 4.6% |
| 2026-10-23 14:00:00:00 | 199 | 4.5% |
| 2026-10-23 15:00:00:00 | 193 | 4.4% |
| 2026-10-23 16:00:00:00 | 178 | 4.1% |
| 2026-10-23 17:00:00:00 | 182 | 4.1% |
| 2026-10-23 18:00:00:00 | 179 | 4.1% |
| 2026-10-23 19:00:00:00 | 181 | 4.1% |
| 2026-10-23 20:00:00:00 | 197 | 4.5% |
| 2026-10-23 21:00:00:00 | 181 | 4.1% |
| 2026-10-23 22:00:00:00 | 180 | 4.1% |
| 2026-10-23 23:00:00:00 | 179 | 4.1% |
| 2026-10-24 00:00:00:00 | 181 | 4.1% |
| 2026-10-24 01:00:00:00 | 180 | 4.1% |
| 2026-10-24 02:00:00:00 | 180 | 4.1% |
| 2026-10-24 03:00:00:00 | 180 | 4.1% |
| 2026-10-24 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 556 | 70.6% |
| 2 | Gravelines, France | 73 | 9.3% |
| 3 | Wallingford, United States | 41 | 5.2% |
| 4 | San Ramon, United States | 30 | 3.8% |
| 5 | Buenos Aires, Argentina | 17 | 2.2% |
| 6 | Raleigh, United States | 16 | 2.0% |
| 7 | Tel Aviv, Israel | 15 | 1.9% |
| 8 | Hillsboro, United States | 13 | 1.7% |
| 9 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 13 | 1.7% |
| 10 | Austin, United States | 13 | 1.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `77.239.124.201` | 556 | 70.6% | The Netherlands / North Holland / Amsterdam / Alfahost LLC | Hosting/Cloud (data center) |
| 2 | `24.147.173.252` | 41 | 5.2% | United States / Connecticut / Wallingford / Comcast Cable Communications Holdings, Inc | No apparent signal |
| 3 | `76.103.223.155` | 30 | 3.8% | United States / California / San Ramon / Comcast Cable Communications, Inc. | No apparent signal |
| 4 | `151.101.218.13` | 17 | 2.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `68.73.112.130` | 16 | 2.0% | United States / North Carolina / Raleigh / PPPoX Pool - Rback2 EHMIL | No apparent signal |
| 6 | `77.91.71.27` | 15 | 1.9% | Israel / Tel Aviv / Tel Aviv / NEW | No apparent signal |
| 7 | `91.231.89.104` | 14 | 1.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 8 | `91.230.168.190` | 13 | 1.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 9 | `151.101.218.73` | 13 | 1.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 10 | `35.146.33.153` | 13 | 1.7% | United States / Texas / Austin / Spectrum | No apparent signal |
| 11 | `91.231.89.130` | 12 | 1.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.0` | 12 | 1.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.231.89.117` | 12 | 1.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.231.89.251` | 12 | 1.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `91.231.89.205` | 11 | 1.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `77.239.124.201` | 556 | 94.9% | Hosting/Cloud (data center) | The Netherlands / North Holland / Amsterdam / Alfahost LLC |
| 2 | `151.101.218.13` | 17 | 2.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.73` | 13 | 2.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
