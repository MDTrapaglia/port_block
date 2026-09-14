# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4378
- Unique source IPs: 2732
- Unique countries/cities (24h): 406
- Unique destination ports: 2450

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 266 | 6.1% |
| 2 | `22` | 124 | 2.8% |
| 3 | `1433` | 58 | 1.3% |
| 4 | `8080` | 41 | 0.9% |
| 5 | `5060` | 34 | 0.8% |
| 6 | `53` | 29 | 0.7% |
| 7 | `3389` | 27 | 0.6% |
| 8 | `161` | 25 | 0.6% |
| 9 | `3306` | 25 | 0.6% |
| 10 | `123` | 21 | 0.5% |
| 11 | `8443` | 20 | 0.5% |
| 12 | `3000` | 19 | 0.4% |
| 13 | `21` | 19 | 0.4% |
| 14 | `unknown` | 17 | 0.4% |
| 15 | `5432` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3865 | 88.3% |
| 2 | `UDP` | 496 | 11.3% |
| 3 | `47` | 15 | 0.3% |
| 4 | `4` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `79.124.62.218` | 37 | 0.8% |
| 2 | `176.65.148.6` | 23 | 0.5% |
| 3 | `113.200.214.90` | 22 | 0.5% |
| 4 | `151.101.218.13` | 18 | 0.4% |
| 5 | `85.217.140.23` | 16 | 0.4% |
| 6 | `85.217.140.5` | 16 | 0.4% |
| 7 | `85.217.149.37` | 15 | 0.3% |
| 8 | `85.217.140.6` | 14 | 0.3% |
| 9 | `18.217.208.51` | 14 | 0.3% |
| 10 | `85.217.140.1` | 14 | 0.3% |
| 11 | `216.70.97.74` | 14 | 0.3% |
| 12 | `85.217.140.3` | 14 | 0.3% |
| 13 | `85.217.140.30` | 13 | 0.3% |
| 14 | `18.221.179.104` | 13 | 0.3% |
| 15 | `85.217.140.22` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3765 | 97.4% |
| 2 | `ACK+FIN+PSH` | 57 | 1.5% |
| 3 | `ACK+PSH` | 24 | 0.6% |
| 4 | `SYN+ECE+CWR` | 12 | 0.3% |
| 5 | `ACK` | 5 | 0.1% |
| 6 | `ACK+FIN` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4378 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `113.200.214.90` -> `1433` | 22 | 0.5% |
| 2 | `216.70.97.74` -> `23` | 14 | 0.3% |
| 3 | `216.180.246.187` -> `53` | 8 | 0.2% |
| 4 | `223.96.92.77` -> `1433` | 7 | 0.2% |
| 5 | `151.101.216.158` -> `49938` | 7 | 0.2% |
| 6 | `66.132.172.186` -> `21` | 6 | 0.1% |
| 7 | `199.45.154.54` -> `8080` | 6 | 0.1% |
| 8 | `151.101.218.73` -> `58576` | 6 | 0.1% |
| 9 | `151.101.218.13` -> `58549` | 6 | 0.1% |
| 10 | `170.51.247.32` -> `45131` | 6 | 0.1% |
| 11 | `151.101.218.13` -> `45115` | 6 | 0.1% |
| 12 | `151.101.218.13` -> `58722` | 6 | 0.1% |
| 13 | `186.123.128.53` -> `1433` | 5 | 0.1% |
| 14 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 15 | `17.57.144.153` -> `58078` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-13 04:00:00:00 | 131 | 3.0% |
| 2026-09-13 05:00:00:00 | 185 | 4.2% |
| 2026-09-13 06:00:00:00 | 180 | 4.1% |
| 2026-09-13 07:00:00:00 | 179 | 4.1% |
| 2026-09-13 08:00:00:00 | 178 | 4.1% |
| 2026-09-13 09:00:00:00 | 182 | 4.2% |
| 2026-09-13 10:00:00:00 | 180 | 4.1% |
| 2026-09-13 11:00:00:00 | 180 | 4.1% |
| 2026-09-13 12:00:00:00 | 194 | 4.4% |
| 2026-09-13 13:00:00:00 | 178 | 4.1% |
| 2026-09-13 14:00:00:00 | 179 | 4.1% |
| 2026-09-13 15:00:00:00 | 182 | 4.2% |
| 2026-09-13 16:00:00:00 | 181 | 4.1% |
| 2026-09-13 17:00:00:00 | 181 | 4.1% |
| 2026-09-13 18:00:00:00 | 186 | 4.2% |
| 2026-09-13 19:00:00:00 | 187 | 4.3% |
| 2026-09-13 20:00:00:00 | 178 | 4.1% |
| 2026-09-13 21:00:00:00 | 180 | 4.1% |
| 2026-09-13 22:00:00:00 | 196 | 4.5% |
| 2026-09-13 23:00:00:00 | 197 | 4.5% |
| 2026-09-14 00:00:00:00 | 181 | 4.1% |
| 2026-09-14 01:00:00:00 | 179 | 4.1% |
| 2026-09-14 02:00:00:00 | 181 | 4.1% |
| 2026-09-14 03:00:00:00 | 178 | 4.1% |
| 2026-09-14 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 85 | 33.3% |
| 2 | Victoria, Seychelles | 37 | 14.5% |
| 3 | Dublin, United States | 27 | 10.6% |
| 4 | Eygelshoven, The Netherlands | 23 | 9.0% |
| 5 | Xi'an, China | 22 | 8.6% |
| 6 | Buenos Aires, Argentina | 18 | 7.1% |
| 7 | Beauharnois, Canada | 15 | 5.9% |
| 8 | Paris, France | 14 | 5.5% |
| 9 | Ashburn, United States | 14 | 5.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `79.124.62.218` | 37 | 14.5% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 2 | `176.65.148.6` | 23 | 9.0% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 3 | `113.200.214.90` | 22 | 8.6% | China / Shaanxi / Xi'an / CNC Group CHINA169 Shannxi Province Network | No apparent signal |
| 4 | `151.101.218.13` | 18 | 7.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `85.217.140.23` | 16 | 6.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `85.217.140.5` | 16 | 6.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.149.37` | 15 | 5.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 8 | `85.217.140.6` | 14 | 5.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `18.217.208.51` | 14 | 5.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `85.217.140.1` | 14 | 5.5% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 11 | `216.70.97.74` | 14 | 5.5% | United States / Virginia / Ashburn / GoDaddy.com, LLC | No apparent signal |
| 12 | `85.217.140.3` | 14 | 5.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `85.217.140.30` | 13 | 5.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `18.221.179.104` | 13 | 5.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `85.217.140.22` | 12 | 4.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 18 | 40.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `18.217.208.51` | 14 | 31.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.221.179.104` | 13 | 28.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
