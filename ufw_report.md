# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4364
- Unique source IPs: 2425
- Unique countries/cities (24h): 261
- Unique destination ports: 2565

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 140 | 3.2% |
| 2 | `41641` | 81 | 1.9% |
| 3 | `22` | 79 | 1.8% |
| 4 | `5060` | 54 | 1.2% |
| 5 | `8080` | 51 | 1.2% |
| 6 | `3389` | 37 | 0.8% |
| 7 | `21` | 33 | 0.8% |
| 8 | `53` | 27 | 0.6% |
| 9 | `3306` | 25 | 0.6% |
| 10 | `1433` | 23 | 0.5% |
| 11 | `8443` | 18 | 0.4% |
| 12 | `27017` | 18 | 0.4% |
| 13 | `33435` | 18 | 0.4% |
| 14 | `123` | 16 | 0.4% |
| 15 | `161` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3913 | 89.7% |
| 2 | `UDP` | 442 | 10.1% |
| 3 | `47` | 8 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `122.15.245.13` | 119 | 2.7% |
| 2 | `190.123.122.115` | 64 | 1.5% |
| 3 | `45.248.159.181` | 29 | 0.7% |
| 4 | `186.143.203.205` | 17 | 0.4% |
| 5 | `91.196.152.195` | 14 | 0.3% |
| 6 | `18.221.179.104` | 14 | 0.3% |
| 7 | `2.22.149.170` | 14 | 0.3% |
| 8 | `72.46.87.211` | 14 | 0.3% |
| 9 | `91.231.89.72` | 13 | 0.3% |
| 10 | `91.230.168.124` | 13 | 0.3% |
| 11 | `3.147.122.184` | 12 | 0.3% |
| 12 | `91.196.152.35` | 12 | 0.3% |
| 13 | `91.231.89.0` | 12 | 0.3% |
| 14 | `91.196.152.190` | 12 | 0.3% |
| 15 | `91.231.89.117` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3833 | 98.0% |
| 2 | `ACK+FIN+PSH` | 42 | 1.1% |
| 3 | `ACK+PSH` | 26 | 0.7% |
| 4 | `ACK+FIN` | 6 | 0.2% |
| 5 | `SYN+ECE+CWR` | 3 | 0.1% |
| 6 | `ACK` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4364 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `190.123.122.115` -> `41641` | 64 | 1.5% |
| 2 | `186.143.203.205` -> `41641` | 17 | 0.4% |
| 3 | `72.46.87.211` -> `23` | 14 | 0.3% |
| 4 | `172.110.223.182` -> `5060` | 12 | 0.3% |
| 5 | `172.110.223.188` -> `5060` | 9 | 0.2% |
| 6 | `154.80.128.163` -> `17000` | 8 | 0.2% |
| 7 | `154.80.128.160` -> `6036` | 8 | 0.2% |
| 8 | `216.180.246.37` -> `8080` | 7 | 0.2% |
| 9 | `170.51.241.160` -> `15527` | 7 | 0.2% |
| 10 | `91.224.92.45` -> `34568` | 6 | 0.1% |
| 11 | `216.180.246.207` -> `4006` | 6 | 0.1% |
| 12 | `95.100.88.89` -> `55536` | 6 | 0.1% |
| 13 | `66.132.195.53` -> `53` | 6 | 0.1% |
| 14 | `45.198.224.125` -> `8080` | 5 | 0.1% |
| 15 | `62.210.114.99` -> `3389` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-03 04:00:00:00 | 134 | 3.1% |
| 2026-11-03 05:00:00:00 | 180 | 4.1% |
| 2026-11-03 06:00:00:00 | 181 | 4.1% |
| 2026-11-03 07:00:00:00 | 185 | 4.2% |
| 2026-11-03 08:00:00:00 | 180 | 4.1% |
| 2026-11-03 09:00:00:00 | 180 | 4.1% |
| 2026-11-03 10:00:00:00 | 181 | 4.1% |
| 2026-11-03 11:00:00:00 | 182 | 4.2% |
| 2026-11-03 12:00:00:00 | 180 | 4.1% |
| 2026-11-03 13:00:00:00 | 180 | 4.1% |
| 2026-11-03 14:00:00:00 | 175 | 4.0% |
| 2026-11-03 15:00:00:00 | 190 | 4.4% |
| 2026-11-03 16:00:00:00 | 183 | 4.2% |
| 2026-11-03 17:00:00:00 | 179 | 4.1% |
| 2026-11-03 18:00:00:00 | 197 | 4.5% |
| 2026-11-03 19:00:00:00 | 179 | 4.1% |
| 2026-11-03 20:00:00:00 | 180 | 4.1% |
| 2026-11-03 21:00:00:00 | 181 | 4.1% |
| 2026-11-03 22:00:00:00 | 179 | 4.1% |
| 2026-11-03 23:00:00:00 | 180 | 4.1% |
| 2026-11-04 00:00:00:00 | 191 | 4.4% |
| 2026-11-04 01:00:00:00 | 180 | 4.1% |
| 2026-11-04 02:00:00:00 | 181 | 4.1% |
| 2026-11-04 03:00:00:00 | 180 | 4.1% |
| 2026-11-04 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Pune, India | 119 | 32.1% |
| 2 | Córdoba, Argentina | 64 | 17.3% |
| 3 | Roubaix, France | 38 | 10.2% |
| 4 | Gravelines, France | 37 | 10.0% |
| 5 | Buenos Aires, Argentina | 31 | 8.4% |
| 6 | Mohali, India | 29 | 7.8% |
| 7 | Dublin, United States | 26 | 7.0% |
| 8 | Singapore, Singapore | 14 | 3.8% |
| 9 | Hillsboro, United States | 13 | 3.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `122.15.245.13` | 119 | 32.1% | India / Maharashtra / Pune / VODAFONE-STATIC | Mobile/CGNAT (vodafone) |
| 2 | `190.123.122.115` | 64 | 17.3% | Argentina / Cordoba / Córdoba / Clariphy Argentina S.A | Hosting/Cloud (datacenter) |
| 3 | `45.248.159.181` | 29 | 7.8% | India / Punjab / Mohali / Fastway Citizen Cable Network Pvt. Ltd. | No apparent signal |
| 4 | `186.143.203.205` | 17 | 4.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Telefónica Móviles Argentina S.A. (Movistar Argentina) | Mobile/CGNAT (telefonica) |
| 5 | `91.196.152.195` | 14 | 3.8% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 6 | `18.221.179.104` | 14 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `2.22.149.170` | 14 | 3.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 8 | `72.46.87.211` | 14 | 3.8% | Singapore / Central Singapore / Singapore / Latitude.sh | No apparent signal |
| 9 | `91.231.89.72` | 13 | 3.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `91.230.168.124` | 13 | 3.5% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 11 | `3.147.122.184` | 12 | 3.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `91.196.152.35` | 12 | 3.2% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 13 | `91.231.89.0` | 12 | 3.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.196.152.190` | 12 | 3.2% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 15 | `91.231.89.117` | 12 | 3.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `190.123.122.115` | 64 | 61.5% | Hosting/Cloud (datacenter) | Argentina / Cordoba / Córdoba / Clariphy Argentina S.A |
| 2 | `18.221.179.104` | 14 | 13.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `2.22.149.170` | 14 | 13.5% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 4 | `3.147.122.184` | 12 | 11.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
