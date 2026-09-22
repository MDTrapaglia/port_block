# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4424
- Unique source IPs: 2246
- Unique countries/cities (24h): 305
- Unique destination ports: 2393

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 147 | 3.3% |
| 2 | `22` | 81 | 1.8% |
| 3 | `5060` | 41 | 0.9% |
| 4 | `1433` | 33 | 0.7% |
| 5 | `8080` | 31 | 0.7% |
| 6 | `17000` | 31 | 0.7% |
| 7 | `3389` | 31 | 0.7% |
| 8 | `unknown` | 30 | 0.7% |
| 9 | `2222` | 29 | 0.7% |
| 10 | `53` | 28 | 0.6% |
| 11 | `8443` | 27 | 0.6% |
| 12 | `161` | 26 | 0.6% |
| 13 | `6036` | 22 | 0.5% |
| 14 | `17001` | 21 | 0.5% |
| 15 | `25` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3984 | 90.1% |
| 2 | `UDP` | 410 | 9.3% |
| 3 | `2` | 16 | 0.4% |
| 4 | `47` | 11 | 0.2% |
| 5 | `132` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.167` | 185 | 4.2% |
| 2 | `37.156.195.1` | 91 | 2.1% |
| 3 | `94.154.43.131` | 28 | 0.6% |
| 4 | `172.110.223.173` | 19 | 0.4% |
| 5 | `118.123.1.32` | 18 | 0.4% |
| 6 | `85.217.140.20` | 17 | 0.4% |
| 7 | `161.35.113.151` | 17 | 0.4% |
| 8 | `85.217.140.22` | 16 | 0.4% |
| 9 | `85.217.140.5` | 16 | 0.4% |
| 10 | `85.217.140.23` | 16 | 0.4% |
| 11 | `192.168.100.64` | 15 | 0.3% |
| 12 | `91.231.89.87` | 14 | 0.3% |
| 13 | `18.217.208.51` | 14 | 0.3% |
| 14 | `85.217.149.37` | 14 | 0.3% |
| 15 | `85.217.140.27` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3819 | 95.9% |
| 2 | `ACK+FIN+PSH` | 70 | 1.8% |
| 3 | `ACK+PSH` | 45 | 1.1% |
| 4 | `ACK+FIN` | 33 | 0.8% |
| 5 | `SYN+ECE+CWR` | 17 | 0.4% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4408 | 99.6% |
| 2 | `wlan0` | 16 | 0.4% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.168.100.64` -> `unknown` | 15 | 0.3% |
| 2 | `216.180.246.167` -> `2223` | 12 | 0.3% |
| 3 | `216.180.246.167` -> `2106` | 11 | 0.2% |
| 4 | `216.180.246.167` -> `2108` | 10 | 0.2% |
| 5 | `216.180.246.167` -> `2332` | 10 | 0.2% |
| 6 | `216.180.246.167` -> `2345` | 10 | 0.2% |
| 7 | `216.180.246.167` -> `2510` | 10 | 0.2% |
| 8 | `216.180.246.167` -> `2112` | 9 | 0.2% |
| 9 | `216.180.246.167` -> `2323` | 9 | 0.2% |
| 10 | `216.180.246.167` -> `2100` | 8 | 0.2% |
| 11 | `216.180.246.167` -> `2200` | 8 | 0.2% |
| 12 | `216.180.246.167` -> `2103` | 7 | 0.2% |
| 13 | `216.180.246.167` -> `2350` | 7 | 0.2% |
| 14 | `216.180.246.167` -> `2351` | 7 | 0.2% |
| 15 | `216.180.246.167` -> `2380` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-21 04:00:00:00 | 142 | 3.2% |
| 2026-09-21 05:00:00:00 | 180 | 4.1% |
| 2026-09-21 06:00:00:00 | 180 | 4.1% |
| 2026-09-21 07:00:00:00 | 180 | 4.1% |
| 2026-09-21 08:00:00:00 | 180 | 4.1% |
| 2026-09-21 09:00:00:00 | 179 | 4.0% |
| 2026-09-21 10:00:00:00 | 181 | 4.1% |
| 2026-09-21 11:00:00:00 | 179 | 4.0% |
| 2026-09-21 12:00:00:00 | 180 | 4.1% |
| 2026-09-21 13:00:00:00 | 185 | 4.2% |
| 2026-09-21 14:00:00:00 | 182 | 4.1% |
| 2026-09-21 15:00:00:00 | 178 | 4.0% |
| 2026-09-21 16:00:00:00 | 182 | 4.1% |
| 2026-09-21 17:00:00:00 | 180 | 4.1% |
| 2026-09-21 18:00:00:00 | 176 | 4.0% |
| 2026-09-21 19:00:00:00 | 184 | 4.2% |
| 2026-09-21 20:00:00:00 | 180 | 4.1% |
| 2026-09-21 21:00:00:00 | 178 | 4.0% |
| 2026-09-21 22:00:00:00 | 239 | 5.4% |
| 2026-09-21 23:00:00:00 | 205 | 4.6% |
| 2026-09-22 00:00:00:00 | 190 | 4.3% |
| 2026-09-22 01:00:00:00 | 179 | 4.0% |
| 2026-09-22 02:00:00:00 | 181 | 4.1% |
| 2026-09-22 03:00:00:00 | 179 | 4.0% |
| 2026-09-22 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 185 | 37.4% |
| 2 | Gravelines, France | 93 | 18.8% |
| 3 | Stockholm, Sweden | 91 | 18.4% |
| 4 | Amsterdam, The Netherlands | 28 | 5.7% |
| 5 | Hong Kong, Hong Kong | 19 | 3.8% |
| 6 | Chengdu, China | 18 | 3.6% |
| 7 | North Bergen, United States | 17 | 3.4% |
| 8 | private | 15 | 3.0% |
| 9 | Dublin, United States | 14 | 2.8% |
| 10 | Beauharnois, Canada | 14 | 2.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.167` | 185 | 37.4% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `37.156.195.1` | 91 | 18.4% | Sweden / Stockholm County / Stockholm / Vetenskapsradet / SUNET | No apparent signal |
| 3 | `94.154.43.131` | 28 | 5.7% | The Netherlands / North Holland / Amsterdam / FOP Danik Vyacheslav Evgenievich | No apparent signal |
| 4 | `172.110.223.173` | 19 | 3.8% | Hong Kong / Kowloon / Hong Kong / Dedires LLC | No apparent signal |
| 5 | `118.123.1.32` | 18 | 3.6% | China / Sichuan / Chengdu / SC MY Lanxun Tech Corp | No apparent signal |
| 6 | `85.217.140.20` | 17 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `161.35.113.151` | 17 | 3.4% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 8 | `85.217.140.22` | 16 | 3.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.5` | 16 | 3.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.23` | 16 | 3.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `192.168.100.64` | 15 | 3.0% | private | Private/CGNAT |
| 12 | `91.231.89.87` | 14 | 2.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `18.217.208.51` | 14 | 2.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `85.217.149.37` | 14 | 2.8% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 15 | `85.217.140.27` | 14 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.167` | 185 | 85.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `161.35.113.151` | 17 | 7.9% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 3 | `18.217.208.51` | 14 | 6.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
