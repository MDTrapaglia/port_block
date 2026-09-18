# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4412
- Unique source IPs: 2610
- Unique countries/cities (24h): 316
- Unique destination ports: 2656

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 190 | 4.3% |
| 2 | `22` | 87 | 2.0% |
| 3 | `8080` | 41 | 0.9% |
| 4 | `1433` | 30 | 0.7% |
| 5 | `17000` | 28 | 0.6% |
| 6 | `6036` | 28 | 0.6% |
| 7 | `3389` | 27 | 0.6% |
| 8 | `5060` | 26 | 0.6% |
| 9 | `8443` | 25 | 0.6% |
| 10 | `53` | 24 | 0.5% |
| 11 | `2222` | 23 | 0.5% |
| 12 | `17001` | 21 | 0.5% |
| 13 | `21` | 20 | 0.5% |
| 14 | `unknown` | 17 | 0.4% |
| 15 | `3306` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4011 | 90.9% |
| 2 | `UDP` | 384 | 8.7% |
| 3 | `47` | 15 | 0.3% |
| 4 | `41` | 1 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `151.101.218.13` | 26 | 0.6% |
| 2 | `208.109.39.19` | 24 | 0.5% |
| 3 | `45.194.92.221` | 22 | 0.5% |
| 4 | `178.20.210.198` | 22 | 0.5% |
| 5 | `85.217.140.34` | 19 | 0.4% |
| 6 | `85.217.140.18` | 17 | 0.4% |
| 7 | `85.217.140.1` | 17 | 0.4% |
| 8 | `85.217.140.35` | 16 | 0.4% |
| 9 | `85.217.140.22` | 16 | 0.4% |
| 10 | `85.217.149.37` | 15 | 0.3% |
| 11 | `85.217.140.29` | 14 | 0.3% |
| 12 | `195.178.110.204` | 14 | 0.3% |
| 13 | `3.147.122.184` | 13 | 0.3% |
| 14 | `85.217.140.30` | 13 | 0.3% |
| 15 | `217.60.76.226` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3891 | 97.0% |
| 2 | `ACK+FIN+PSH` | 77 | 1.9% |
| 3 | `ACK+PSH` | 20 | 0.5% |
| 4 | `ACK+FIN` | 14 | 0.3% |
| 5 | `SYN+ECE+CWR` | 9 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4412 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `208.109.39.19` -> `23` | 24 | 0.5% |
| 2 | `45.194.92.221` -> `17000` | 9 | 0.2% |
| 3 | `216.180.246.233` -> `8080` | 8 | 0.2% |
| 4 | `216.180.246.122` -> `8080` | 8 | 0.2% |
| 5 | `45.194.92.221` -> `17001` | 7 | 0.2% |
| 6 | `194.28.89.218` -> `5038` | 7 | 0.2% |
| 7 | `23.40.188.32` -> `62809` | 7 | 0.2% |
| 8 | `151.101.218.13` -> `59580` | 7 | 0.2% |
| 9 | `77.239.124.127` -> `2323` | 6 | 0.1% |
| 10 | `45.194.92.221` -> `6036` | 6 | 0.1% |
| 11 | `201.20.85.122` -> `6379` | 6 | 0.1% |
| 12 | `151.101.218.73` -> `62833` | 6 | 0.1% |
| 13 | `186.123.128.53` -> `1433` | 5 | 0.1% |
| 14 | `170.51.241.170` -> `58650` | 5 | 0.1% |
| 15 | `199.45.155.45` -> `554` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-17 04:00:00:00 | 135 | 3.1% |
| 2026-09-17 05:00:00:00 | 181 | 4.1% |
| 2026-09-17 06:00:00:00 | 177 | 4.0% |
| 2026-09-17 07:00:00:00 | 183 | 4.1% |
| 2026-09-17 08:00:00:00 | 179 | 4.1% |
| 2026-09-17 09:00:00:00 | 181 | 4.1% |
| 2026-09-17 10:00:00:00 | 178 | 4.0% |
| 2026-09-17 11:00:00:00 | 182 | 4.1% |
| 2026-09-17 12:00:00:00 | 180 | 4.1% |
| 2026-09-17 13:00:00:00 | 180 | 4.1% |
| 2026-09-17 14:00:00:00 | 179 | 4.1% |
| 2026-09-17 15:00:00:00 | 180 | 4.1% |
| 2026-09-17 16:00:00:00 | 184 | 4.2% |
| 2026-09-17 17:00:00:00 | 193 | 4.4% |
| 2026-09-17 18:00:00:00 | 199 | 4.5% |
| 2026-09-17 19:00:00:00 | 210 | 4.8% |
| 2026-09-17 20:00:00:00 | 181 | 4.1% |
| 2026-09-17 21:00:00:00 | 180 | 4.1% |
| 2026-09-17 22:00:00:00 | 181 | 4.1% |
| 2026-09-17 23:00:00:00 | 177 | 4.0% |
| 2026-09-18 00:00:00:00 | 182 | 4.1% |
| 2026-09-18 01:00:00:00 | 183 | 4.1% |
| 2026-09-18 02:00:00:00 | 180 | 4.1% |
| 2026-09-18 03:00:00:00 | 188 | 4.3% |
| 2026-09-18 04:00:00:00 | 59 | 1.3% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 95 | 36.4% |
| 2 | Buenos Aires, Argentina | 26 | 10.0% |
| 3 | Tempe, United States | 24 | 9.2% |
| 4 | Toronto, Canada | 22 | 8.4% |
| 5 | Būlaevo, Kazakhstan | 22 | 8.4% |
| 6 | Paris, France | 17 | 6.5% |
| 7 | Beauharnois, Canada | 15 | 5.7% |
| 8 | Andorra la Vella, Andorra | 14 | 5.4% |
| 9 | Dublin, United States | 13 | 5.0% |
| 10 | Eygelshoven, The Netherlands | 13 | 5.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 26 | 10.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 2 | `208.109.39.19` | 24 | 9.2% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 3 | `45.194.92.221` | 22 | 8.4% | Canada / Ontario / Toronto / East Coast Host | No apparent signal |
| 4 | `178.20.210.198` | 22 | 8.4% | Kazakhstan / North Kazakhstan / Būlaevo / Shereverov network | No apparent signal |
| 5 | `85.217.140.34` | 19 | 7.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `85.217.140.18` | 17 | 6.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.1` | 17 | 6.5% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 8 | `85.217.140.35` | 16 | 6.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.22` | 16 | 6.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.149.37` | 15 | 5.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 11 | `85.217.140.29` | 14 | 5.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `195.178.110.204` | 14 | 5.4% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 13 | `3.147.122.184` | 13 | 5.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `85.217.140.30` | 13 | 5.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `217.60.76.226` | 13 | 5.0% | The Netherlands / Limburg / Eygelshoven / Iryna Ivanenko | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 26 | 66.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `3.147.122.184` | 13 | 33.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
