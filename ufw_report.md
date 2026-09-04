# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4342
- Unique source IPs: 2541
- Unique countries/cities (24h): 385
- Unique destination ports: 2762

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 329 | 7.6% |
| 2 | `22` | 67 | 1.5% |
| 3 | `5060` | 64 | 1.5% |
| 4 | `53` | 26 | 0.6% |
| 5 | `8080` | 26 | 0.6% |
| 6 | `8443` | 25 | 0.6% |
| 7 | `3389` | 22 | 0.5% |
| 8 | `8000` | 21 | 0.5% |
| 9 | `1433` | 20 | 0.5% |
| 10 | `unknown` | 18 | 0.4% |
| 11 | `3306` | 17 | 0.4% |
| 12 | `8081` | 16 | 0.4% |
| 13 | `2222` | 15 | 0.3% |
| 14 | `9200` | 13 | 0.3% |
| 15 | `27015` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3902 | 89.9% |
| 2 | `UDP` | 422 | 9.7% |
| 3 | `47` | 16 | 0.4% |
| 4 | `4` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `142.93.183.218` | 102 | 2.3% |
| 2 | `45.128.157.202` | 74 | 1.7% |
| 3 | `160.153.175.11` | 28 | 0.6% |
| 4 | `172.110.223.179` | 24 | 0.6% |
| 5 | `103.173.18.146` | 19 | 0.4% |
| 6 | `85.217.140.5` | 14 | 0.3% |
| 7 | `85.217.140.6` | 14 | 0.3% |
| 8 | `85.217.140.22` | 13 | 0.3% |
| 9 | `85.217.140.2` | 12 | 0.3% |
| 10 | `85.217.140.28` | 12 | 0.3% |
| 11 | `85.217.140.29` | 11 | 0.3% |
| 12 | `85.217.149.37` | 11 | 0.3% |
| 13 | `18.217.208.51` | 11 | 0.3% |
| 14 | `85.217.140.19` | 10 | 0.2% |
| 15 | `85.217.140.23` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3861 | 98.9% |
| 2 | `ACK+FIN+PSH` | 18 | 0.5% |
| 3 | `ACK+PSH` | 12 | 0.3% |
| 4 | `SYN+ECE+CWR` | 11 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4342 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `142.93.183.218` -> `23` | 102 | 2.3% |
| 2 | `160.153.175.11` -> `23` | 28 | 0.6% |
| 3 | `172.110.223.179` -> `5060` | 24 | 0.6% |
| 4 | `186.123.1.125` -> `1433` | 7 | 0.2% |
| 5 | `199.45.154.113` -> `8443` | 7 | 0.2% |
| 6 | `109.94.173.183` -> `3389` | 5 | 0.1% |
| 7 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 8 | `198.15.126.237` -> `27015` | 5 | 0.1% |
| 9 | `2.22.149.154` -> `52046` | 5 | 0.1% |
| 10 | `160.119.76.127` -> `5060` | 4 | 0.1% |
| 11 | `188.241.120.4` -> `3389` | 4 | 0.1% |
| 12 | `80.87.206.19` -> `9443` | 4 | 0.1% |
| 13 | `121.40.126.115` -> `2222` | 4 | 0.1% |
| 14 | `2.22.149.154` -> `7031` | 4 | 0.1% |
| 15 | `162.19.19.234` -> `5060` | 3 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-03 04:00:00:00 | 144 | 3.3% |
| 2026-09-03 05:00:00:00 | 180 | 4.1% |
| 2026-09-03 06:00:00:00 | 179 | 4.1% |
| 2026-09-03 07:00:00:00 | 181 | 4.2% |
| 2026-09-03 08:00:00:00 | 179 | 4.1% |
| 2026-09-03 09:00:00:00 | 179 | 4.1% |
| 2026-09-03 10:00:00:00 | 181 | 4.2% |
| 2026-09-03 11:00:00:00 | 180 | 4.1% |
| 2026-09-03 12:00:00:00 | 181 | 4.2% |
| 2026-09-03 13:00:00:00 | 179 | 4.1% |
| 2026-09-03 14:00:00:00 | 179 | 4.1% |
| 2026-09-03 15:00:00:00 | 181 | 4.2% |
| 2026-09-03 16:00:00:00 | 180 | 4.1% |
| 2026-09-03 17:00:00:00 | 180 | 4.1% |
| 2026-09-03 18:00:00:00 | 180 | 4.1% |
| 2026-09-03 19:00:00:00 | 178 | 4.1% |
| 2026-09-03 20:00:00:00 | 182 | 4.2% |
| 2026-09-03 21:00:00:00 | 181 | 4.2% |
| 2026-09-03 22:00:00:00 | 179 | 4.1% |
| 2026-09-03 23:00:00:00 | 191 | 4.4% |
| 2026-09-04 00:00:00:00 | 182 | 4.2% |
| 2026-09-04 01:00:00:00 | 180 | 4.1% |
| 2026-09-04 02:00:00:00 | 179 | 4.1% |
| 2026-09-04 03:00:00:00 | 181 | 4.2% |
| 2026-09-04 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Clifton, United States | 102 | 27.9% |
| 2 | Gravelines, France | 96 | 26.3% |
| 3 | Hengevelde, The Netherlands | 74 | 20.3% |
| 4 | Tempe, United States | 28 | 7.7% |
| 5 | Atlanta, United States | 24 | 6.6% |
| 6 | Mumbai, India | 19 | 5.2% |
| 7 | Beauharnois, Canada | 11 | 3.0% |
| 8 | Dublin, United States | 11 | 3.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `142.93.183.218` | 102 | 27.9% | United States / New Jersey / Clifton / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `45.128.157.202` | 74 | 20.3% | The Netherlands / Overijssel / Hengevelde / MC-Node | Mobile/CGNAT (lte) |
| 3 | `160.153.175.11` | 28 | 7.7% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 4 | `172.110.223.179` | 24 | 6.6% | United States / Georgia / Atlanta / Dedires LLC | No apparent signal |
| 5 | `103.173.18.146` | 19 | 5.2% | India / Maharashtra / Mumbai / Game | No apparent signal |
| 6 | `85.217.140.5` | 14 | 3.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.6` | 14 | 3.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.22` | 13 | 3.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.2` | 12 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.28` | 12 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.29` | 11 | 3.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.149.37` | 11 | 3.0% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 13 | `18.217.208.51` | 11 | 3.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `85.217.140.19` | 10 | 2.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `85.217.140.23` | 10 | 2.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `142.93.183.218` | 102 | 90.3% | Hosting/Cloud (digitalocean) | United States / New Jersey / Clifton / DigitalOcean, LLC |
| 2 | `18.217.208.51` | 11 | 9.7% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
