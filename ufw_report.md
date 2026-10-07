# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4418
- Unique source IPs: 2281
- Unique countries/cities (24h): 305
- Unique destination ports: 2760

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 112 | 2.5% |
| 2 | `22` | 68 | 1.5% |
| 3 | `8080` | 39 | 0.9% |
| 4 | `1433` | 35 | 0.8% |
| 5 | `8081` | 29 | 0.7% |
| 6 | `81` | 27 | 0.6% |
| 7 | `5060` | 26 | 0.6% |
| 8 | `53` | 24 | 0.5% |
| 9 | `8443` | 23 | 0.5% |
| 10 | `3389` | 21 | 0.5% |
| 11 | `8000` | 20 | 0.5% |
| 12 | `2222` | 16 | 0.4% |
| 13 | `123` | 15 | 0.3% |
| 14 | `6379` | 14 | 0.3% |
| 15 | `11211` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4020 | 91.0% |
| 2 | `UDP` | 393 | 8.9% |
| 3 | `47` | 4 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.99.16.45` | 303 | 6.9% |
| 2 | `222.255.117.65` | 56 | 1.3% |
| 3 | `151.101.218.13` | 40 | 0.9% |
| 4 | `85.217.140.18` | 18 | 0.4% |
| 5 | `45.198.224.125` | 17 | 0.4% |
| 6 | `85.217.140.23` | 16 | 0.4% |
| 7 | `204.76.203.219` | 16 | 0.4% |
| 8 | `79.124.40.162` | 16 | 0.4% |
| 9 | `91.231.89.130` | 15 | 0.3% |
| 10 | `94.183.174.99` | 14 | 0.3% |
| 11 | `91.231.89.205` | 14 | 0.3% |
| 12 | `91.231.89.150` | 13 | 0.3% |
| 13 | `18.190.15.50` | 13 | 0.3% |
| 14 | `141.98.83.48` | 13 | 0.3% |
| 15 | `91.231.89.238` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3854 | 95.9% |
| 2 | `ACK+FIN+PSH` | 90 | 2.2% |
| 3 | `ACK+PSH` | 45 | 1.1% |
| 4 | `SYN+ECE+CWR` | 14 | 0.3% |
| 5 | `ACK+FIN` | 9 | 0.2% |
| 6 | `ACK` | 8 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4418 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.205.1.160` -> `6036` | 10 | 0.2% |
| 2 | `45.205.1.163` -> `17000` | 9 | 0.2% |
| 3 | `45.198.224.125` -> `8081` | 7 | 0.2% |
| 4 | `45.198.224.125` -> `9090` | 7 | 0.2% |
| 5 | `91.224.92.28` -> `34567` | 7 | 0.2% |
| 6 | `151.101.218.13` -> `54820` | 7 | 0.2% |
| 7 | `151.101.218.13` -> `32871` | 7 | 0.2% |
| 8 | `45.198.224.124` -> `81` | 6 | 0.1% |
| 9 | `151.101.216.159` -> `42462` | 6 | 0.1% |
| 10 | `201.20.85.122` -> `6379` | 6 | 0.1% |
| 11 | `170.51.241.171` -> `54676` | 6 | 0.1% |
| 12 | `151.101.218.13` -> `31833` | 6 | 0.1% |
| 13 | `216.180.246.22` -> `80` | 6 | 0.1% |
| 14 | `94.183.174.99` -> `8080` | 5 | 0.1% |
| 15 | `204.76.203.237` -> `81` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-06 04:00:00:00 | 134 | 3.0% |
| 2026-10-06 05:00:00:00 | 177 | 4.0% |
| 2026-10-06 06:00:00:00 | 183 | 4.1% |
| 2026-10-06 07:00:00:00 | 187 | 4.2% |
| 2026-10-06 08:00:00:00 | 179 | 4.1% |
| 2026-10-06 09:00:00:00 | 179 | 4.1% |
| 2026-10-06 10:00:00:00 | 182 | 4.1% |
| 2026-10-06 11:00:00:00 | 202 | 4.6% |
| 2026-10-06 12:00:00:00 | 195 | 4.4% |
| 2026-10-06 13:00:00:00 | 190 | 4.3% |
| 2026-10-06 14:00:00:00 | 181 | 4.1% |
| 2026-10-06 15:00:00:00 | 178 | 4.0% |
| 2026-10-06 16:00:00:00 | 180 | 4.1% |
| 2026-10-06 17:00:00:00 | 182 | 4.1% |
| 2026-10-06 18:00:00:00 | 180 | 4.1% |
| 2026-10-06 19:00:00:00 | 179 | 4.1% |
| 2026-10-06 20:00:00:00 | 180 | 4.1% |
| 2026-10-06 21:00:00:00 | 180 | 4.1% |
| 2026-10-06 22:00:00:00 | 201 | 4.5% |
| 2026-10-06 23:00:00:00 | 180 | 4.1% |
| 2026-10-07 00:00:00:00 | 182 | 4.1% |
| 2026-10-07 01:00:00:00 | 190 | 4.3% |
| 2026-10-07 02:00:00:00 | 184 | 4.2% |
| 2026-10-07 03:00:00:00 | 188 | 4.3% |
| 2026-10-07 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Montreal, Canada | 303 | 52.5% |
| 2 | Gravelines, France | 89 | 15.4% |
| 3 | Ho Chi Minh City, Vietnam | 56 | 9.7% |
| 4 | Buenos Aires, Argentina | 40 | 6.9% |
| 5 | Stockholm, Sweden | 17 | 2.9% |
| 6 | Eygelshoven, Netherlands | 16 | 2.8% |
| 7 | Sopot, Bulgaria | 16 | 2.8% |
| 8 | Hauzenberg, Germany | 14 | 2.4% |
| 9 | Dublin, United States | 13 | 2.3% |
| 10 | Panama City, Panama | 13 | 2.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.99.16.45` | 303 | 52.5% | Canada / Quebec / Montreal / OVH Hosting, Inc. | Hosting/Cloud (ovh) |
| 2 | `222.255.117.65` | 56 | 9.7% | Vietnam / Ho Chi Minh City (HCMC) / Ho Chi Minh City / VietNam Data Communication Company | No apparent signal |
| 3 | `151.101.218.13` | 40 | 6.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `85.217.140.18` | 18 | 3.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `45.198.224.125` | 17 | 2.9% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 6 | `85.217.140.23` | 16 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `204.76.203.219` | 16 | 2.8% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 8 | `79.124.40.162` | 16 | 2.8% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 9 | `91.231.89.130` | 15 | 2.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `94.183.174.99` | 14 | 2.4% | Germany / Bavaria / Hauzenberg / Pfcloud UG | No apparent signal |
| 11 | `91.231.89.205` | 14 | 2.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.150` | 13 | 2.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `18.190.15.50` | 13 | 2.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `141.98.83.48` | 13 | 2.3% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 15 | `91.231.89.238` | 13 | 2.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.99.16.45` | 303 | 82.1% | Hosting/Cloud (ovh) | Canada / Quebec / Montreal / OVH Hosting, Inc. |
| 2 | `151.101.218.13` | 40 | 10.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `18.190.15.50` | 13 | 3.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `141.98.83.48` | 13 | 3.5% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
