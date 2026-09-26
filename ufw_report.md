# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4351
- Unique source IPs: 2463
- Unique countries/cities (24h): 314
- Unique destination ports: 2566

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 160 | 3.7% |
| 2 | `22` | 73 | 1.7% |
| 3 | `5060` | 39 | 0.9% |
| 4 | `3389` | 37 | 0.9% |
| 5 | `8443` | 33 | 0.8% |
| 6 | `8080` | 27 | 0.6% |
| 7 | `17000` | 27 | 0.6% |
| 8 | `1433` | 26 | 0.6% |
| 9 | `53` | 25 | 0.6% |
| 10 | `8088` | 23 | 0.5% |
| 11 | `6036` | 21 | 0.5% |
| 12 | `27036` | 18 | 0.4% |
| 13 | `3000` | 17 | 0.4% |
| 14 | `17001` | 16 | 0.4% |
| 15 | `3306` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3960 | 91.0% |
| 2 | `UDP` | 381 | 8.8% |
| 3 | `47` | 8 | 0.2% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.209` | 115 | 2.6% |
| 2 | `97.74.236.238` | 19 | 0.4% |
| 3 | `85.217.140.27` | 18 | 0.4% |
| 4 | `85.217.140.35` | 17 | 0.4% |
| 5 | `85.217.140.5` | 17 | 0.4% |
| 6 | `186.123.164.151` | 16 | 0.4% |
| 7 | `185.224.128.16` | 15 | 0.3% |
| 8 | `85.217.140.18` | 15 | 0.3% |
| 9 | `85.217.140.29` | 15 | 0.3% |
| 10 | `85.217.140.34` | 14 | 0.3% |
| 11 | `91.231.89.72` | 14 | 0.3% |
| 12 | `91.231.89.224` | 14 | 0.3% |
| 13 | `91.230.168.233` | 14 | 0.3% |
| 14 | `151.101.218.13` | 14 | 0.3% |
| 15 | `91.231.89.130` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3893 | 98.3% |
| 2 | `ACK+PSH` | 27 | 0.7% |
| 3 | `ACK+FIN+PSH` | 21 | 0.5% |
| 4 | `SYN+ECE+CWR` | 12 | 0.3% |
| 5 | `ACK+FIN` | 4 | 0.1% |
| 6 | `RST` | 2 | 0.1% |
| 7 | `ACK+RST` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4351 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `97.74.236.238` -> `23` | 19 | 0.4% |
| 2 | `186.123.164.151` -> `27036` | 16 | 0.4% |
| 3 | `216.180.246.209` -> `8088` | 10 | 0.2% |
| 4 | `216.180.246.209` -> `8087` | 9 | 0.2% |
| 5 | `216.180.246.209` -> `8120` | 8 | 0.2% |
| 6 | `216.180.246.209` -> `8140` | 8 | 0.2% |
| 7 | `216.180.246.209` -> `8153` | 8 | 0.2% |
| 8 | `216.180.246.209` -> `8079` | 7 | 0.2% |
| 9 | `216.180.246.209` -> `8083` | 7 | 0.2% |
| 10 | `151.101.218.13` -> `56926` | 7 | 0.2% |
| 11 | `216.180.246.209` -> `8128` | 7 | 0.2% |
| 12 | `178.20.210.152` -> `1723` | 6 | 0.1% |
| 13 | `66.132.195.118` -> `8443` | 6 | 0.1% |
| 14 | `216.180.246.209` -> `8091` | 6 | 0.1% |
| 15 | `216.180.246.209` -> `8092` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-25 04:00:00:00 | 138 | 3.2% |
| 2026-09-25 05:00:00:00 | 179 | 4.1% |
| 2026-09-25 06:00:00:00 | 180 | 4.1% |
| 2026-09-25 07:00:00:00 | 180 | 4.1% |
| 2026-09-25 08:00:00:00 | 180 | 4.1% |
| 2026-09-25 09:00:00:00 | 178 | 4.1% |
| 2026-09-25 10:00:00:00 | 182 | 4.2% |
| 2026-09-25 11:00:00:00 | 180 | 4.1% |
| 2026-09-25 12:00:00:00 | 181 | 4.2% |
| 2026-09-25 13:00:00:00 | 178 | 4.1% |
| 2026-09-25 14:00:00:00 | 180 | 4.1% |
| 2026-09-25 15:00:00:00 | 179 | 4.1% |
| 2026-09-25 16:00:00:00 | 182 | 4.2% |
| 2026-09-25 17:00:00:00 | 180 | 4.1% |
| 2026-09-25 18:00:00:00 | 193 | 4.4% |
| 2026-09-25 19:00:00:00 | 179 | 4.1% |
| 2026-09-25 20:00:00:00 | 180 | 4.1% |
| 2026-09-25 21:00:00:00 | 181 | 4.2% |
| 2026-09-25 22:00:00:00 | 180 | 4.1% |
| 2026-09-25 23:00:00:00 | 182 | 4.2% |
| 2026-09-26 00:00:00:00 | 193 | 4.4% |
| 2026-09-26 01:00:00:00 | 179 | 4.1% |
| 2026-09-26 02:00:00:00 | 181 | 4.2% |
| 2026-09-26 03:00:00:00 | 180 | 4.1% |
| 2026-09-26 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 137 | 41.5% |
| 2 | Massy, France | 115 | 34.8% |
| 3 | Tempe, United States | 19 | 5.8% |
| 4 | Córdoba, Argentina | 16 | 4.8% |
| 5 | Amsterdam, The Netherlands | 15 | 4.5% |
| 6 | Hillsboro, United States | 14 | 4.2% |
| 7 | Buenos Aires, Argentina | 14 | 4.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.209` | 115 | 34.8% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `97.74.236.238` | 19 | 5.8% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 3 | `85.217.140.27` | 18 | 5.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 4 | `85.217.140.35` | 17 | 5.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `85.217.140.5` | 17 | 5.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `186.123.164.151` | 16 | 4.8% | Argentina / Cordoba / Córdoba / AMX Argentina S.A | No apparent signal |
| 7 | `185.224.128.16` | 15 | 4.5% | The Netherlands / North Holland / Amsterdam / Alsycon B.V | No apparent signal |
| 8 | `85.217.140.18` | 15 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.29` | 15 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.34` | 14 | 4.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `91.231.89.72` | 14 | 4.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.224` | 14 | 4.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.230.168.233` | 14 | 4.2% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 14 | `151.101.218.13` | 14 | 4.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 15 | `91.231.89.130` | 13 | 3.9% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.209` | 115 | 89.1% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 14 | 10.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
