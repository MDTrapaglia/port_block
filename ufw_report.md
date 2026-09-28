# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4356
- Unique source IPs: 2673
- Unique countries/cities (24h): 326
- Unique destination ports: 2467

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 168 | 3.9% |
| 2 | `22` | 99 | 2.3% |
| 3 | `3389` | 38 | 0.9% |
| 4 | `5060` | 32 | 0.7% |
| 5 | `53` | 31 | 0.7% |
| 6 | `17000` | 30 | 0.7% |
| 7 | `1433` | 30 | 0.7% |
| 8 | `8443` | 26 | 0.6% |
| 9 | `8080` | 25 | 0.6% |
| 10 | `6036` | 24 | 0.6% |
| 11 | `3306` | 21 | 0.5% |
| 12 | `2222` | 19 | 0.4% |
| 13 | `9200` | 18 | 0.4% |
| 14 | `8081` | 17 | 0.4% |
| 15 | `25` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3935 | 90.3% |
| 2 | `UDP` | 410 | 9.4% |
| 3 | `47` | 8 | 0.2% |
| 4 | `4` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `107.175.233.24` | 25 | 0.6% |
| 2 | `85.217.140.30` | 19 | 0.4% |
| 3 | `85.217.149.37` | 18 | 0.4% |
| 4 | `85.217.140.5` | 17 | 0.4% |
| 5 | `85.217.140.18` | 16 | 0.4% |
| 6 | `85.217.140.1` | 16 | 0.4% |
| 7 | `18.217.208.51` | 15 | 0.3% |
| 8 | `18.190.15.50` | 15 | 0.3% |
| 9 | `85.217.140.7` | 15 | 0.3% |
| 10 | `85.217.140.34` | 15 | 0.3% |
| 11 | `142.251.129.46` | 15 | 0.3% |
| 12 | `2.22.149.177` | 15 | 0.3% |
| 13 | `85.217.140.27` | 14 | 0.3% |
| 14 | `85.217.140.6` | 14 | 0.3% |
| 15 | `85.217.140.33` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3846 | 97.7% |
| 2 | `ACK+PSH` | 36 | 0.9% |
| 3 | `ACK+FIN+PSH` | 35 | 0.9% |
| 4 | `SYN+ECE+CWR` | 16 | 0.4% |
| 5 | `ACK+FIN` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4356 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `205.237.106.81` -> `6036` | 12 | 0.3% |
| 2 | `47.236.54.176` -> `23` | 8 | 0.2% |
| 3 | `205.237.105.190` -> `17000` | 7 | 0.2% |
| 4 | `80.67.33.209` -> `23` | 6 | 0.1% |
| 5 | `178.20.210.152` -> `1723` | 6 | 0.1% |
| 6 | `205.237.104.18` -> `17001` | 6 | 0.1% |
| 7 | `186.123.1.125` -> `1433` | 5 | 0.1% |
| 8 | `89.42.231.200` -> `17000` | 5 | 0.1% |
| 9 | `201.20.85.122` -> `6379` | 5 | 0.1% |
| 10 | `109.94.173.183` -> `3389` | 5 | 0.1% |
| 11 | `66.132.172.130` -> `25` | 5 | 0.1% |
| 12 | `190.104.36.219` -> `22` | 5 | 0.1% |
| 13 | `2.22.149.177` -> `36297` | 5 | 0.1% |
| 14 | `51.222.40.109` -> `554` | 4 | 0.1% |
| 15 | `45.205.1.163` -> `17000` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-27 04:00:00:00 | 135 | 3.1% |
| 2026-09-27 05:00:00:00 | 179 | 4.1% |
| 2026-09-27 06:00:00:00 | 180 | 4.1% |
| 2026-09-27 07:00:00:00 | 176 | 4.0% |
| 2026-09-27 08:00:00:00 | 185 | 4.2% |
| 2026-09-27 09:00:00:00 | 178 | 4.1% |
| 2026-09-27 10:00:00:00 | 179 | 4.1% |
| 2026-09-27 11:00:00:00 | 182 | 4.2% |
| 2026-09-27 12:00:00:00 | 190 | 4.4% |
| 2026-09-27 13:00:00:00 | 180 | 4.1% |
| 2026-09-27 14:00:00:00 | 175 | 4.0% |
| 2026-09-27 15:00:00:00 | 185 | 4.2% |
| 2026-09-27 16:00:00:00 | 179 | 4.1% |
| 2026-09-27 17:00:00:00 | 178 | 4.1% |
| 2026-09-27 18:00:00:00 | 183 | 4.2% |
| 2026-09-27 19:00:00:00 | 179 | 4.1% |
| 2026-09-27 20:00:00:00 | 181 | 4.2% |
| 2026-09-27 21:00:00:00 | 197 | 4.5% |
| 2026-09-27 22:00:00:00 | 179 | 4.1% |
| 2026-09-27 23:00:00:00 | 182 | 4.2% |
| 2026-09-28 00:00:00:00 | 186 | 4.3% |
| 2026-09-28 01:00:00:00 | 182 | 4.2% |
| 2026-09-28 02:00:00:00 | 181 | 4.2% |
| 2026-09-28 03:00:00:00 | 179 | 4.1% |
| 2026-09-28 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 124 | 51.0% |
| 2 | Dublin, United States | 30 | 12.3% |
| 3 | Los Angeles, United States | 25 | 10.3% |
| 4 | Beauharnois, Canada | 18 | 7.4% |
| 5 | Paris, France | 16 | 6.6% |
| 6 | Mountain View, United States | 15 | 6.2% |
| 7 | Buenos Aires, Argentina | 15 | 6.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `107.175.233.24` | 25 | 10.3% | United States / California / Los Angeles / ColoCrossing | Hosting/Cloud (colo) |
| 2 | `85.217.140.30` | 19 | 7.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 3 | `85.217.149.37` | 18 | 7.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 4 | `85.217.140.5` | 17 | 7.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `85.217.140.18` | 16 | 6.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `85.217.140.1` | 16 | 6.6% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 7 | `18.217.208.51` | 15 | 6.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `18.190.15.50` | 15 | 6.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `85.217.140.7` | 15 | 6.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.34` | 15 | 6.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `142.251.129.46` | 15 | 6.2% | United States / California / Mountain View / Google LLC | Hosting/Cloud (google llc) |
| 12 | `2.22.149.177` | 15 | 6.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 13 | `85.217.140.27` | 14 | 5.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `85.217.140.6` | 14 | 5.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `85.217.140.33` | 14 | 5.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `107.175.233.24` | 25 | 29.4% | Hosting/Cloud (colo) | United States / California / Los Angeles / ColoCrossing |
| 2 | `18.217.208.51` | 15 | 17.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.190.15.50` | 15 | 17.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `142.251.129.46` | 15 | 17.6% | Hosting/Cloud (google llc) | United States / California / Mountain View / Google LLC |
| 5 | `2.22.149.177` | 15 | 17.6% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
