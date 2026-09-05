# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4366
- Unique source IPs: 2514
- Unique countries/cities (24h): 367
- Unique destination ports: 2696

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 204 | 4.7% |
| 2 | `22` | 71 | 1.6% |
| 3 | `53` | 31 | 0.7% |
| 4 | `3389` | 27 | 0.6% |
| 5 | `8443` | 27 | 0.6% |
| 6 | `5060` | 23 | 0.5% |
| 7 | `8080` | 22 | 0.5% |
| 8 | `1433` | 19 | 0.4% |
| 9 | `5555` | 16 | 0.4% |
| 10 | `9200` | 15 | 0.3% |
| 11 | `27017` | 15 | 0.3% |
| 12 | `143` | 15 | 0.3% |
| 13 | `161` | 15 | 0.3% |
| 14 | `25` | 14 | 0.3% |
| 15 | `8686` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3947 | 90.4% |
| 2 | `UDP` | 406 | 9.3% |
| 3 | `47` | 13 | 0.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.68` | 191 | 4.4% |
| 2 | `103.173.18.146` | 49 | 1.1% |
| 3 | `94.154.43.175` | 24 | 0.5% |
| 4 | `85.239.245.161` | 18 | 0.4% |
| 5 | `2.22.149.168` | 16 | 0.4% |
| 6 | `148.59.129.127` | 15 | 0.3% |
| 7 | `141.98.83.48` | 14 | 0.3% |
| 8 | `149.33.19.95` | 13 | 0.3% |
| 9 | `151.101.218.13` | 13 | 0.3% |
| 10 | `18.217.208.51` | 12 | 0.3% |
| 11 | `185.224.128.16` | 12 | 0.3% |
| 12 | `85.217.140.27` | 12 | 0.3% |
| 13 | `85.217.140.19` | 12 | 0.3% |
| 14 | `2.22.149.138` | 12 | 0.3% |
| 15 | `85.217.149.37` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3867 | 98.0% |
| 2 | `ACK+FIN+PSH` | 42 | 1.1% |
| 3 | `ACK+PSH` | 24 | 0.6% |
| 4 | `SYN+ECE+CWR` | 10 | 0.3% |
| 5 | `ACK+FIN` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4366 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.68` -> `8686` | 11 | 0.3% |
| 2 | `216.180.246.68` -> `8621` | 9 | 0.2% |
| 3 | `216.180.246.68` -> `8265` | 8 | 0.2% |
| 4 | `216.180.246.68` -> `8283` | 8 | 0.2% |
| 5 | `216.180.246.68` -> `8384` | 8 | 0.2% |
| 6 | `216.180.246.68` -> `8400` | 8 | 0.2% |
| 7 | `216.180.246.68` -> `8545` | 8 | 0.2% |
| 8 | `216.180.246.68` -> `8252` | 7 | 0.2% |
| 9 | `198.15.126.237` -> `27015` | 7 | 0.2% |
| 10 | `216.180.246.68` -> `8291` | 7 | 0.2% |
| 11 | `216.180.246.68` -> `8443` | 7 | 0.2% |
| 12 | `216.180.246.68` -> `8500` | 7 | 0.2% |
| 13 | `216.180.246.68` -> `8501` | 7 | 0.2% |
| 14 | `216.180.246.68` -> `8554` | 7 | 0.2% |
| 15 | `216.180.246.68` -> `8602` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-04 04:00:00:00 | 135 | 3.1% |
| 2026-09-04 05:00:00:00 | 180 | 4.1% |
| 2026-09-04 06:00:00:00 | 179 | 4.1% |
| 2026-09-04 07:00:00:00 | 180 | 4.1% |
| 2026-09-04 08:00:00:00 | 180 | 4.1% |
| 2026-09-04 09:00:00:00 | 180 | 4.1% |
| 2026-09-04 10:00:00:00 | 180 | 4.1% |
| 2026-09-04 11:00:00:00 | 179 | 4.1% |
| 2026-09-04 12:00:00:00 | 182 | 4.2% |
| 2026-09-04 13:00:00:00 | 179 | 4.1% |
| 2026-09-04 14:00:00:00 | 178 | 4.1% |
| 2026-09-04 15:00:00:00 | 182 | 4.2% |
| 2026-09-04 16:00:00:00 | 181 | 4.1% |
| 2026-09-04 17:00:00:00 | 180 | 4.1% |
| 2026-09-04 18:00:00:00 | 178 | 4.1% |
| 2026-09-04 19:00:00:00 | 182 | 4.2% |
| 2026-09-04 20:00:00:00 | 177 | 4.1% |
| 2026-09-04 21:00:00:00 | 182 | 4.2% |
| 2026-09-04 22:00:00:00 | 217 | 5.0% |
| 2026-09-04 23:00:00:00 | 185 | 4.2% |
| 2026-09-05 00:00:00:00 | 179 | 4.1% |
| 2026-09-05 01:00:00:00 | 184 | 4.2% |
| 2026-09-05 02:00:00:00 | 180 | 4.1% |
| 2026-09-05 03:00:00:00 | 180 | 4.1% |
| 2026-09-05 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 191 | 45.0% |
| 2 | Buenos Aires, Argentina | 54 | 12.7% |
| 3 | Mumbai, India | 49 | 11.6% |
| 4 | Amsterdam, The Netherlands | 36 | 8.5% |
| 5 | Gravelines, France | 24 | 5.7% |
| 6 | St Louis, United States | 18 | 4.2% |
| 7 | Piscataway, United States | 15 | 3.5% |
| 8 | Panama City, Panama | 14 | 3.3% |
| 9 | Dublin, United States | 12 | 2.8% |
| 10 | Beauharnois, Canada | 11 | 2.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.68` | 191 | 45.0% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `103.173.18.146` | 49 | 11.6% | India / Maharashtra / Mumbai / Game | No apparent signal |
| 3 | `94.154.43.175` | 24 | 5.7% | The Netherlands / North Holland / Amsterdam / FOP Danik Vyacheslav Evgenievich | No apparent signal |
| 4 | `85.239.245.161` | 18 | 4.2% | United States / Missouri / St Louis / Casablanca INT | Hosting/Cloud (contabo) |
| 5 | `2.22.149.168` | 16 | 3.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 6 | `148.59.129.127` | 15 | 3.5% | United States / New Jersey / Piscataway / Globex Internet Sevices Corporation | No apparent signal |
| 7 | `141.98.83.48` | 14 | 3.3% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 8 | `149.33.19.95` | 13 | 3.1% | Argentina / Buenos Aires F.D. / Buenos Aires / 3NT SOLUTIONS LLP | No apparent signal |
| 9 | `151.101.218.13` | 13 | 3.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 10 | `18.217.208.51` | 12 | 2.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `185.224.128.16` | 12 | 2.8% | The Netherlands / North Holland / Amsterdam / Alsycon B.V | No apparent signal |
| 12 | `85.217.140.27` | 12 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `85.217.140.19` | 12 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `2.22.149.138` | 12 | 2.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 15 | `85.217.149.37` | 11 | 2.6% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.68` | 191 | 69.2% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `85.239.245.161` | 18 | 6.5% | Hosting/Cloud (contabo) | United States / Missouri / St Louis / Casablanca INT |
| 3 | `2.22.149.168` | 16 | 5.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 4 | `141.98.83.48` | 14 | 5.1% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 5 | `151.101.218.13` | 13 | 4.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 6 | `18.217.208.51` | 12 | 4.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `2.22.149.138` | 12 | 4.3% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
