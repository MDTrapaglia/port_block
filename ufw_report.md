# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4403
- Unique source IPs: 2351
- Unique countries/cities (24h): 324
- Unique destination ports: 2331

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 171 | 3.9% |
| 2 | `22` | 124 | 2.8% |
| 3 | `8080` | 45 | 1.0% |
| 4 | `1433` | 36 | 0.8% |
| 5 | `81` | 32 | 0.7% |
| 6 | `53` | 30 | 0.7% |
| 7 | `3389` | 29 | 0.7% |
| 8 | `5060` | 28 | 0.6% |
| 9 | `8443` | 26 | 0.6% |
| 10 | `161` | 24 | 0.5% |
| 11 | `1900` | 21 | 0.5% |
| 12 | `2222` | 20 | 0.5% |
| 13 | `123` | 19 | 0.4% |
| 14 | `21` | 19 | 0.4% |
| 15 | `9200` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3958 | 89.9% |
| 2 | `UDP` | 433 | 9.8% |
| 3 | `47` | 9 | 0.2% |
| 4 | `4` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.128` | 46 | 1.0% |
| 2 | `132.148.73.100` | 24 | 0.5% |
| 3 | `222.186.42.98` | 20 | 0.5% |
| 4 | `85.217.140.6` | 16 | 0.4% |
| 5 | `151.101.218.13` | 16 | 0.4% |
| 6 | `85.217.140.2` | 15 | 0.3% |
| 7 | `85.217.140.33` | 15 | 0.3% |
| 8 | `91.231.89.117` | 15 | 0.3% |
| 9 | `16.5.0.234` | 15 | 0.3% |
| 10 | `91.231.89.205` | 14 | 0.3% |
| 11 | `91.231.89.150` | 14 | 0.3% |
| 12 | `91.231.89.130` | 14 | 0.3% |
| 13 | `91.231.89.238` | 14 | 0.3% |
| 14 | `91.196.152.123` | 14 | 0.3% |
| 15 | `79.124.40.162` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3827 | 96.7% |
| 2 | `ACK+FIN+PSH` | 81 | 2.0% |
| 3 | `ACK+PSH` | 32 | 0.8% |
| 4 | `SYN+ECE+CWR` | 13 | 0.3% |
| 5 | `ACK+FIN` | 5 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4403 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `132.148.73.100` -> `23` | 24 | 0.5% |
| 2 | `216.180.246.128` -> `1980` | 14 | 0.3% |
| 3 | `45.198.224.124` -> `81` | 9 | 0.2% |
| 4 | `216.180.246.128` -> `1987` | 9 | 0.2% |
| 5 | `5.55.205.64` -> `23` | 9 | 0.2% |
| 6 | `216.180.246.128` -> `1912` | 8 | 0.2% |
| 7 | `216.180.246.128` -> `1935` | 8 | 0.2% |
| 8 | `216.180.246.173` -> `8080` | 8 | 0.2% |
| 9 | `91.224.92.28` -> `34567` | 7 | 0.2% |
| 10 | `186.123.1.125` -> `1433` | 7 | 0.2% |
| 11 | `45.198.224.125` -> `8080` | 7 | 0.2% |
| 12 | `216.180.246.128` -> `1981` | 7 | 0.2% |
| 13 | `23.64.58.32` -> `29123` | 7 | 0.2% |
| 14 | `45.205.1.163` -> `17000` | 6 | 0.1% |
| 15 | `151.101.218.73` -> `51700` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-05 04:00:00:00 | 137 | 3.1% |
| 2026-10-05 05:00:00:00 | 180 | 4.1% |
| 2026-10-05 06:00:00:00 | 180 | 4.1% |
| 2026-10-05 07:00:00:00 | 179 | 4.1% |
| 2026-10-05 08:00:00:00 | 181 | 4.1% |
| 2026-10-05 09:00:00:00 | 172 | 3.9% |
| 2026-10-05 10:00:00:00 | 181 | 4.1% |
| 2026-10-05 11:00:00:00 | 182 | 4.1% |
| 2026-10-05 12:00:00:00 | 180 | 4.1% |
| 2026-10-05 13:00:00:00 | 180 | 4.1% |
| 2026-10-05 14:00:00:00 | 179 | 4.1% |
| 2026-10-05 15:00:00:00 | 181 | 4.1% |
| 2026-10-05 16:00:00:00 | 219 | 5.0% |
| 2026-10-05 17:00:00:00 | 181 | 4.1% |
| 2026-10-05 18:00:00:00 | 180 | 4.1% |
| 2026-10-05 19:00:00:00 | 196 | 4.5% |
| 2026-10-05 20:00:00:00 | 182 | 4.1% |
| 2026-10-05 21:00:00:00 | 178 | 4.0% |
| 2026-10-05 22:00:00:00 | 182 | 4.1% |
| 2026-10-05 23:00:00:00 | 180 | 4.1% |
| 2026-10-06 00:00:00:00 | 182 | 4.1% |
| 2026-10-06 01:00:00:00 | 194 | 4.4% |
| 2026-10-06 02:00:00:00 | 190 | 4.3% |
| 2026-10-06 03:00:00:00 | 179 | 4.1% |
| 2026-10-06 04:00:00:00 | 48 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 117 | 44.0% |
| 2 | Massy, France | 46 | 17.3% |
| 3 | Tempe, United States | 24 | 9.0% |
| 4 | Nanjing, China | 20 | 7.5% |
| 5 | Buenos Aires, Argentina | 16 | 6.0% |
| 6 | São Paulo, Brazil | 15 | 5.6% |
| 7 | Roubaix, France | 14 | 5.3% |
| 8 | Sopot, Bulgaria | 14 | 5.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.128` | 46 | 17.3% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `132.148.73.100` | 24 | 9.0% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 3 | `222.186.42.98` | 20 | 7.5% | China / Jiangsu / Nanjing / Chinanet JS | No apparent signal |
| 4 | `85.217.140.6` | 16 | 6.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `151.101.218.13` | 16 | 6.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `85.217.140.2` | 15 | 5.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.33` | 15 | 5.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `91.231.89.117` | 15 | 5.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `16.5.0.234` | 15 | 5.6% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 10 | `91.231.89.205` | 14 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 11 | `91.231.89.150` | 14 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.130` | 14 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.231.89.238` | 14 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.196.152.123` | 14 | 5.3% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 15 | `79.124.40.162` | 14 | 5.3% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.128` | 46 | 74.2% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `151.101.218.13` | 16 | 25.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
