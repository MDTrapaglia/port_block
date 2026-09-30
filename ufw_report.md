# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4429
- Unique source IPs: 2415
- Unique countries/cities (24h): 299
- Unique destination ports: 2502

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 131 | 3.0% |
| 2 | `22` | 71 | 1.6% |
| 3 | `8080` | 40 | 0.9% |
| 4 | `5060` | 39 | 0.9% |
| 5 | `1433` | 34 | 0.8% |
| 6 | `53` | 29 | 0.7% |
| 7 | `3389` | 27 | 0.6% |
| 8 | `17000` | 27 | 0.6% |
| 9 | `8443` | 23 | 0.5% |
| 10 | `2222` | 22 | 0.5% |
| 11 | `123` | 20 | 0.5% |
| 12 | `3306` | 20 | 0.5% |
| 13 | `17001` | 19 | 0.4% |
| 14 | `8888` | 19 | 0.4% |
| 15 | `6036` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4067 | 91.8% |
| 2 | `UDP` | 351 | 7.9% |
| 3 | `47` | 10 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `62.210.142.160` | 159 | 3.6% |
| 2 | `151.101.218.73` | 36 | 0.8% |
| 3 | `94.154.43.215` | 32 | 0.7% |
| 4 | `16.5.0.239` | 25 | 0.6% |
| 5 | `16.5.0.241` | 24 | 0.5% |
| 6 | `85.217.140.34` | 16 | 0.4% |
| 7 | `85.217.140.30` | 15 | 0.3% |
| 8 | `85.217.140.2` | 14 | 0.3% |
| 9 | `91.230.168.142` | 14 | 0.3% |
| 10 | `2.22.149.138` | 14 | 0.3% |
| 11 | `85.217.140.1` | 13 | 0.3% |
| 12 | `91.231.89.130` | 13 | 0.3% |
| 13 | `91.231.89.150` | 13 | 0.3% |
| 14 | `91.230.168.233` | 13 | 0.3% |
| 15 | `195.178.110.204` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3904 | 96.0% |
| 2 | `ACK+FIN+PSH` | 101 | 2.5% |
| 3 | `ACK+PSH` | 37 | 0.9% |
| 4 | `SYN+ECE+CWR` | 15 | 0.4% |
| 5 | `ACK+FIN` | 8 | 0.2% |
| 6 | `ACK` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4429 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `91.224.92.28` -> `34567` | 9 | 0.2% |
| 2 | `2.23.164.42` -> `61216` | 8 | 0.2% |
| 3 | `62.210.142.160` -> `2087` | 8 | 0.2% |
| 4 | `62.210.142.160` -> `2088` | 8 | 0.2% |
| 5 | `216.180.246.83` -> `8080` | 8 | 0.2% |
| 6 | `62.210.142.160` -> `2379` | 8 | 0.2% |
| 7 | `151.101.218.73` -> `2799` | 7 | 0.2% |
| 8 | `186.123.128.53` -> `1433` | 7 | 0.2% |
| 9 | `186.123.1.125` -> `1433` | 7 | 0.2% |
| 10 | `62.210.142.160` -> `2100` | 7 | 0.2% |
| 11 | `62.210.142.160` -> `2101` | 7 | 0.2% |
| 12 | `62.210.142.160` -> `2194` | 7 | 0.2% |
| 13 | `62.210.142.160` -> `2200` | 7 | 0.2% |
| 14 | `62.210.142.160` -> `2223` | 7 | 0.2% |
| 15 | `151.101.218.73` -> `6785` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-29 04:00:00:00 | 158 | 3.6% |
| 2026-09-29 05:00:00:00 | 179 | 4.0% |
| 2026-09-29 06:00:00:00 | 180 | 4.1% |
| 2026-09-29 07:00:00:00 | 181 | 4.1% |
| 2026-09-29 08:00:00:00 | 179 | 4.0% |
| 2026-09-29 09:00:00:00 | 181 | 4.1% |
| 2026-09-29 10:00:00:00 | 201 | 4.5% |
| 2026-09-29 11:00:00:00 | 186 | 4.2% |
| 2026-09-29 12:00:00:00 | 179 | 4.0% |
| 2026-09-29 13:00:00:00 | 187 | 4.2% |
| 2026-09-29 14:00:00:00 | 179 | 4.0% |
| 2026-09-29 15:00:00:00 | 201 | 4.5% |
| 2026-09-29 16:00:00:00 | 180 | 4.1% |
| 2026-09-29 17:00:00:00 | 180 | 4.1% |
| 2026-09-29 18:00:00:00 | 194 | 4.4% |
| 2026-09-29 19:00:00:00 | 180 | 4.1% |
| 2026-09-29 20:00:00:00 | 181 | 4.1% |
| 2026-09-29 21:00:00:00 | 180 | 4.1% |
| 2026-09-29 22:00:00:00 | 185 | 4.2% |
| 2026-09-29 23:00:00:00 | 181 | 4.1% |
| 2026-09-30 00:00:00:00 | 180 | 4.1% |
| 2026-09-30 01:00:00:00 | 180 | 4.1% |
| 2026-09-30 02:00:00:00 | 190 | 4.3% |
| 2026-09-30 03:00:00:00 | 181 | 4.1% |
| 2026-09-30 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Paris, France | 172 | 41.5% |
| 2 | Gravelines, France | 71 | 17.1% |
| 3 | São Paulo, Brazil | 49 | 11.8% |
| 4 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 36 | 8.7% |
| 5 | Amsterdam, The Netherlands | 32 | 7.7% |
| 6 | Hillsboro, United States | 27 | 6.5% |
| 7 | Buenos Aires, Argentina | 14 | 3.4% |
| 8 | Andorra la Vella, Andorra | 13 | 3.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.160` | 159 | 38.4% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 2 | `151.101.218.73` | 36 | 8.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `94.154.43.215` | 32 | 7.7% | The Netherlands / North Holland / Amsterdam / FOP Danik Vyacheslav Evgenievich | No apparent signal |
| 4 | `16.5.0.239` | 25 | 6.0% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 5 | `16.5.0.241` | 24 | 5.8% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 6 | `85.217.140.34` | 16 | 3.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.30` | 15 | 3.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.2` | 14 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `91.230.168.142` | 14 | 3.4% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 10 | `2.22.149.138` | 14 | 3.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 11 | `85.217.140.1` | 13 | 3.1% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 12 | `91.231.89.130` | 13 | 3.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.231.89.150` | 13 | 3.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.230.168.233` | 13 | 3.1% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 15 | `195.178.110.204` | 13 | 3.1% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.160` | 159 | 76.1% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `151.101.218.73` | 36 | 17.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `2.22.149.138` | 14 | 6.7% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
