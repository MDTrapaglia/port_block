# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4436
- Unique source IPs: 2393
- Unique countries/cities (24h): 300
- Unique destination ports: 2739

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 112 | 2.5% |
| 2 | `22` | 73 | 1.6% |
| 3 | `3389` | 35 | 0.8% |
| 4 | `5060` | 33 | 0.7% |
| 5 | `8080` | 32 | 0.7% |
| 6 | `53` | 23 | 0.5% |
| 7 | `1433` | 22 | 0.5% |
| 8 | `8081` | 21 | 0.5% |
| 9 | `8000` | 21 | 0.5% |
| 10 | `2222` | 20 | 0.5% |
| 11 | `161` | 20 | 0.5% |
| 12 | `8443` | 19 | 0.4% |
| 13 | `5432` | 17 | 0.4% |
| 14 | `389` | 16 | 0.4% |
| 15 | `9200` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4059 | 91.5% |
| 2 | `UDP` | 367 | 8.3% |
| 3 | `47` | 8 | 0.2% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.45` | 98 | 2.2% |
| 2 | `185.172.56.112` | 75 | 1.7% |
| 3 | `151.101.218.13` | 49 | 1.1% |
| 4 | `151.101.218.73` | 19 | 0.4% |
| 5 | `177.136.44.6` | 18 | 0.4% |
| 6 | `85.217.140.33` | 17 | 0.4% |
| 7 | `45.198.224.154` | 17 | 0.4% |
| 8 | `85.217.140.3` | 17 | 0.4% |
| 9 | `85.217.140.2` | 16 | 0.4% |
| 10 | `85.217.149.37` | 16 | 0.4% |
| 11 | `91.231.89.0` | 15 | 0.3% |
| 12 | `91.231.89.215` | 15 | 0.3% |
| 13 | `85.217.140.6` | 15 | 0.3% |
| 14 | `91.196.152.222` | 15 | 0.3% |
| 15 | `91.231.89.10` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3894 | 95.9% |
| 2 | `ACK+FIN+PSH` | 103 | 2.5% |
| 3 | `ACK+PSH` | 34 | 0.8% |
| 4 | `SYN+ECE+CWR` | 14 | 0.3% |
| 5 | `ACK+FIN` | 13 | 0.3% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4436 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `62.210.114.99` -> `3389` | 10 | 0.2% |
| 2 | `216.180.246.45` -> `32566` | 9 | 0.2% |
| 3 | `216.180.246.45` -> `33034` | 9 | 0.2% |
| 4 | `45.205.1.163` -> `17000` | 9 | 0.2% |
| 5 | `216.180.246.45` -> `32768` | 8 | 0.2% |
| 6 | `216.180.246.45` -> `34567` | 7 | 0.2% |
| 7 | `151.101.218.13` -> `60924` | 7 | 0.2% |
| 8 | `216.180.246.45` -> `31210` | 6 | 0.1% |
| 9 | `216.180.246.45` -> `31324` | 6 | 0.1% |
| 10 | `45.205.1.160` -> `6036` | 6 | 0.1% |
| 11 | `216.180.246.45` -> `31423` | 6 | 0.1% |
| 12 | `216.180.246.45` -> `31460` | 6 | 0.1% |
| 13 | `151.101.216.159` -> `49252` | 6 | 0.1% |
| 14 | `45.198.224.125` -> `8081` | 6 | 0.1% |
| 15 | `216.180.246.45` -> `33060` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-16 04:00:00:00 | 136 | 3.1% |
| 2026-10-16 05:00:00:00 | 192 | 4.3% |
| 2026-10-16 06:00:00:00 | 180 | 4.1% |
| 2026-10-16 07:00:00:00 | 184 | 4.1% |
| 2026-10-16 08:00:00:00 | 182 | 4.1% |
| 2026-10-16 09:00:00:00 | 178 | 4.0% |
| 2026-10-16 10:00:00:00 | 182 | 4.1% |
| 2026-10-16 11:00:00:00 | 180 | 4.1% |
| 2026-10-16 12:00:00:00 | 203 | 4.6% |
| 2026-10-16 13:00:00:00 | 177 | 4.0% |
| 2026-10-16 14:00:00:00 | 193 | 4.4% |
| 2026-10-16 15:00:00:00 | 194 | 4.4% |
| 2026-10-16 16:00:00:00 | 193 | 4.4% |
| 2026-10-16 17:00:00:00 | 180 | 4.1% |
| 2026-10-16 18:00:00:00 | 181 | 4.1% |
| 2026-10-16 19:00:00:00 | 179 | 4.0% |
| 2026-10-16 20:00:00:00 | 189 | 4.3% |
| 2026-10-16 21:00:00:00 | 182 | 4.1% |
| 2026-10-16 22:00:00:00 | 187 | 4.2% |
| 2026-10-16 23:00:00:00 | 180 | 4.1% |
| 2026-10-17 00:00:00:00 | 180 | 4.1% |
| 2026-10-17 01:00:00:00 | 177 | 4.0% |
| 2026-10-17 02:00:00:00 | 184 | 4.1% |
| 2026-10-17 03:00:00:00 | 198 | 4.5% |
| 2026-10-17 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 110 | 26.4% |
| 2 | Massy, France | 98 | 23.5% |
| 3 | Amsterdam, The Netherlands | 75 | 18.0% |
| 4 | Buenos Aires, Argentina | 49 | 11.8% |
| 5 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 19 | 4.6% |
| 6 | Salvador, Brazil | 18 | 4.3% |
| 7 | Stockholm, Sweden | 17 | 4.1% |
| 8 | Beauharnois, Canada | 16 | 3.8% |
| 9 | Roubaix, France | 15 | 3.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.45` | 98 | 23.5% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `185.172.56.112` | 75 | 18.0% | The Netherlands / North Holland / Amsterdam / SecureAttack | No apparent signal |
| 3 | `151.101.218.13` | 49 | 11.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `151.101.218.73` | 19 | 4.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `177.136.44.6` | 18 | 4.3% | Brazil / Bahia / Salvador / Suburbio Telecomunicacoes Ltda | No apparent signal |
| 6 | `85.217.140.33` | 17 | 4.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `45.198.224.154` | 17 | 4.1% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 8 | `85.217.140.3` | 17 | 4.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.2` | 16 | 3.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.149.37` | 16 | 3.8% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 11 | `91.231.89.0` | 15 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.215` | 15 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `85.217.140.6` | 15 | 3.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `91.196.152.222` | 15 | 3.6% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 15 | `91.231.89.10` | 15 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.45` | 98 | 59.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 49 | 29.5% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.73` | 19 | 11.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
