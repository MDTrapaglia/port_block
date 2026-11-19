# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4417
- Unique source IPs: 2278
- Unique countries/cities (24h): 269
- Unique destination ports: 2206

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `7680` | 368 | 8.3% |
| 2 | `23` | 86 | 1.9% |
| 3 | `22` | 71 | 1.6% |
| 4 | `8080` | 43 | 1.0% |
| 5 | `5060` | 39 | 0.9% |
| 6 | `1433` | 33 | 0.7% |
| 7 | `3389` | 30 | 0.7% |
| 8 | `8443` | 24 | 0.5% |
| 9 | `53` | 24 | 0.5% |
| 10 | `8888` | 22 | 0.5% |
| 11 | `9000` | 17 | 0.4% |
| 12 | `1723` | 17 | 0.4% |
| 13 | `161` | 16 | 0.4% |
| 14 | `21` | 16 | 0.4% |
| 15 | `9200` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4070 | 92.1% |
| 2 | `UDP` | 343 | 7.8% |
| 3 | `47` | 3 | 0.1% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `190.123.122.114` | 268 | 6.1% |
| 2 | `216.180.246.16` | 162 | 3.7% |
| 3 | `217.195.153.112` | 78 | 1.8% |
| 4 | `151.101.218.13` | 30 | 0.7% |
| 5 | `108.178.114.170` | 29 | 0.7% |
| 6 | `149.154.166.110` | 21 | 0.5% |
| 7 | `151.101.218.73` | 20 | 0.5% |
| 8 | `85.234.131.81` | 17 | 0.4% |
| 9 | `68.4.170.109` | 16 | 0.4% |
| 10 | `70.54.121.165` | 16 | 0.4% |
| 11 | `195.184.76.185` | 15 | 0.3% |
| 12 | `91.231.89.150` | 14 | 0.3% |
| 13 | `91.230.168.190` | 14 | 0.3% |
| 14 | `185.231.32.34` | 14 | 0.3% |
| 15 | `72.203.72.165` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3935 | 96.7% |
| 2 | `ACK+FIN+PSH` | 88 | 2.2% |
| 3 | `ACK+PSH` | 35 | 0.9% |
| 4 | `ACK+FIN` | 5 | 0.1% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |
| 6 | `ACK` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4415 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `190.123.122.114` -> `7680` | 268 | 6.1% |
| 2 | `108.178.114.170` -> `7680` | 29 | 0.7% |
| 3 | `85.234.131.81` -> `23` | 17 | 0.4% |
| 4 | `68.4.170.109` -> `7680` | 16 | 0.4% |
| 5 | `70.54.121.165` -> `7680` | 16 | 0.4% |
| 6 | `72.203.72.165` -> `7680` | 14 | 0.3% |
| 7 | `104.204.174.215` -> `7680` | 12 | 0.3% |
| 8 | `216.180.246.16` -> `9005` | 10 | 0.2% |
| 9 | `216.180.246.16` -> `9019` | 9 | 0.2% |
| 10 | `91.224.92.45` -> `34567` | 8 | 0.2% |
| 11 | `216.180.246.16` -> `9008` | 8 | 0.2% |
| 12 | `216.180.246.16` -> `8993` | 7 | 0.2% |
| 13 | `216.180.246.16` -> `9006` | 7 | 0.2% |
| 14 | `216.180.246.16` -> `8888` | 6 | 0.1% |
| 15 | `216.180.246.16` -> `8900` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-18 04:00:00:00 | 134 | 3.0% |
| 2026-11-18 05:00:00:00 | 182 | 4.1% |
| 2026-11-18 06:00:00:00 | 180 | 4.1% |
| 2026-11-18 07:00:00:00 | 179 | 4.1% |
| 2026-11-18 08:00:00:00 | 181 | 4.1% |
| 2026-11-18 09:00:00:00 | 179 | 4.1% |
| 2026-11-18 10:00:00:00 | 177 | 4.0% |
| 2026-11-18 11:00:00:00 | 184 | 4.2% |
| 2026-11-18 12:00:00:00 | 180 | 4.1% |
| 2026-11-18 13:00:00:00 | 192 | 4.3% |
| 2026-11-18 14:00:00:00 | 188 | 4.3% |
| 2026-11-18 15:00:00:00 | 182 | 4.1% |
| 2026-11-18 16:00:00:00 | 180 | 4.1% |
| 2026-11-18 17:00:00:00 | 179 | 4.1% |
| 2026-11-18 18:00:00:00 | 182 | 4.1% |
| 2026-11-18 19:00:00:00 | 179 | 4.1% |
| 2026-11-18 20:00:00:00 | 181 | 4.1% |
| 2026-11-18 21:00:00:00 | 203 | 4.6% |
| 2026-11-18 22:00:00:00 | 197 | 4.5% |
| 2026-11-18 23:00:00:00 | 187 | 4.2% |
| 2026-11-19 00:00:00:00 | 182 | 4.1% |
| 2026-11-19 01:00:00:00 | 200 | 4.5% |
| 2026-11-19 02:00:00:00 | 183 | 4.1% |
| 2026-11-19 03:00:00:00 | 180 | 4.1% |
| 2026-11-19 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Córdoba, Argentina | 268 | 36.8% |
| 2 | Massy, France | 162 | 22.3% |
| 3 | Amsterdam, The Netherlands | 78 | 10.7% |
| 4 | Buenos Aires, Argentina | 30 | 4.1% |
| 5 | Austin, United States | 29 | 4.0% |
| 6 | Amsterdam, Netherlands | 21 | 2.9% |
| 7 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 20 | 2.7% |
| 8 | Reading, United Kingdom | 17 | 2.3% |
| 9 | Mission Viejo, United States | 16 | 2.2% |
| 10 | Nepean, Canada | 16 | 2.2% |
| 11 | Warrenton, United States | 15 | 2.1% |
| 12 | Gravelines, France | 14 | 1.9% |
| 13 | Hillsboro, United States | 14 | 1.9% |
| 14 | Victoria, Seychelles | 14 | 1.9% |
| 15 | San Clemente, United States | 14 | 1.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `190.123.122.114` | 268 | 36.8% | Argentina / Cordoba / Córdoba / Clariphy Argentina S.A | Hosting/Cloud (datacenter) |
| 2 | `216.180.246.16` | 162 | 22.3% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 3 | `217.195.153.112` | 78 | 10.7% | The Netherlands / North Holland / Amsterdam / Shock Hosting LLC | No apparent signal |
| 4 | `151.101.218.13` | 30 | 4.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `108.178.114.170` | 29 | 4.0% | United States / Texas / Austin / Marvell Semiconductor | No apparent signal |
| 6 | `149.154.166.110` | 21 | 2.9% | Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 7 | `151.101.218.73` | 20 | 2.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 8 | `85.234.131.81` | 17 | 2.3% | United Kingdom / England / Reading / POUNDHOST | No apparent signal |
| 9 | `68.4.170.109` | 16 | 2.2% | United States / California / Mission Viejo / Cox Communications Inc | No apparent signal |
| 10 | `70.54.121.165` | 16 | 2.2% | Canada / Ontario / Nepean / Sympatico HSE | No apparent signal |
| 11 | `195.184.76.185` | 15 | 2.1% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 12 | `91.231.89.150` | 14 | 1.9% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.230.168.190` | 14 | 1.9% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 14 | `185.231.32.34` | 14 | 1.9% | Seychelles / La Rivière Anglaise / Victoria / Datashield | No apparent signal |
| 15 | `72.203.72.165` | 14 | 1.9% | United States / California / San Clemente / Cox Communications Inc. | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `190.123.122.114` | 268 | 55.8% | Hosting/Cloud (datacenter) | Argentina / Cordoba / Córdoba / Clariphy Argentina S.A |
| 2 | `216.180.246.16` | 162 | 33.8% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 3 | `151.101.218.13` | 30 | 6.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `151.101.218.73` | 20 | 4.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
