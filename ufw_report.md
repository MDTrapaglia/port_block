# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4358
- Unique source IPs: 2426
- Unique countries/cities (24h): 312
- Unique destination ports: 2458

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 682 | 15.6% |
| 2 | `unknown` | 50 | 1.1% |
| 3 | `8080` | 44 | 1.0% |
| 4 | `22` | 34 | 0.8% |
| 5 | `5060` | 30 | 0.7% |
| 6 | `27015` | 26 | 0.6% |
| 7 | `1433` | 25 | 0.6% |
| 8 | `123` | 24 | 0.6% |
| 9 | `3389` | 23 | 0.5% |
| 10 | `8443` | 22 | 0.5% |
| 11 | `53` | 20 | 0.5% |
| 12 | `25` | 16 | 0.4% |
| 13 | `8000` | 16 | 0.4% |
| 14 | `6379` | 14 | 0.3% |
| 15 | `5555` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3914 | 89.8% |
| 2 | `UDP` | 394 | 9.0% |
| 3 | `47` | 50 | 1.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `164.92.115.22` | 539 | 12.4% |
| 2 | `92.204.128.6` | 69 | 1.6% |
| 3 | `85.217.149.47` | 27 | 0.6% |
| 4 | `85.217.149.34` | 21 | 0.5% |
| 5 | `85.217.149.49` | 19 | 0.4% |
| 6 | `15.204.11.198` | 18 | 0.4% |
| 7 | `85.217.149.20` | 18 | 0.4% |
| 8 | `85.217.149.17` | 18 | 0.4% |
| 9 | `143.198.174.13` | 17 | 0.4% |
| 10 | `93.123.72.183` | 15 | 0.3% |
| 11 | `85.217.149.15` | 15 | 0.3% |
| 12 | `85.217.149.42` | 14 | 0.3% |
| 13 | `79.63.45.2` | 13 | 0.3% |
| 14 | `85.217.149.48` | 13 | 0.3% |
| 15 | `3.131.24.55` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3860 | 98.6% |
| 2 | `ACK+FIN+PSH` | 28 | 0.7% |
| 3 | `ACK+PSH` | 15 | 0.4% |
| 4 | `SYN+ECE+CWR` | 5 | 0.1% |
| 5 | `ACK` | 5 | 0.1% |
| 6 | `ACK+FIN` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4352 | 99.9% |
| 2 | `wlan0` | 6 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `164.92.115.22` -> `23` | 539 | 12.4% |
| 2 | `92.204.128.6` -> `23` | 69 | 1.6% |
| 3 | `15.204.11.198` -> `23` | 18 | 0.4% |
| 4 | `79.63.45.2` -> `23` | 13 | 0.3% |
| 5 | `222.79.104.148` -> `6379` | 10 | 0.2% |
| 6 | `94.156.152.50` -> `23` | 8 | 0.2% |
| 7 | `69.17.52.1` -> `8333` | 8 | 0.2% |
| 8 | `45.198.224.18` -> `8728` | 7 | 0.2% |
| 9 | `23.40.188.34` -> `51002` | 6 | 0.1% |
| 10 | `93.123.72.183` -> `8080` | 6 | 0.1% |
| 11 | `192.168.100.1` -> `68` | 6 | 0.1% |
| 12 | `151.101.218.13` -> `13593` | 6 | 0.1% |
| 13 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 14 | `3.87.27.156` -> `8443` | 5 | 0.1% |
| 15 | `151.101.218.13` -> `51026` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-19 04:00:00:00 | 136 | 3.1% |
| 2026-06-19 05:00:00:00 | 180 | 4.1% |
| 2026-06-19 06:00:00:00 | 197 | 4.5% |
| 2026-06-19 07:00:00:00 | 180 | 4.1% |
| 2026-06-19 08:00:00:00 | 175 | 4.0% |
| 2026-06-19 09:00:00:00 | 184 | 4.2% |
| 2026-06-19 10:00:00:00 | 181 | 4.2% |
| 2026-06-19 11:00:00:00 | 179 | 4.1% |
| 2026-06-19 12:00:00:00 | 180 | 4.1% |
| 2026-06-19 13:00:00:00 | 180 | 4.1% |
| 2026-06-19 14:00:00:00 | 182 | 4.2% |
| 2026-06-19 15:00:00:00 | 188 | 4.3% |
| 2026-06-19 16:00:00:00 | 180 | 4.1% |
| 2026-06-19 17:00:00:00 | 180 | 4.1% |
| 2026-06-19 18:00:00:00 | 182 | 4.2% |
| 2026-06-19 19:00:00:00 | 180 | 4.1% |
| 2026-06-19 20:00:00:00 | 180 | 4.1% |
| 2026-06-19 21:00:00:00 | 180 | 4.1% |
| 2026-06-19 22:00:00:00 | 180 | 4.1% |
| 2026-06-19 23:00:00:00 | 180 | 4.1% |
| 2026-06-20 00:00:00:00 | 180 | 4.1% |
| 2026-06-20 01:00:00:00 | 180 | 4.1% |
| 2026-06-20 02:00:00:00 | 182 | 4.2% |
| 2026-06-20 03:00:00:00 | 180 | 4.1% |
| 2026-06-20 04:00:00:00 | 52 | 1.2% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Santa Clara, United States | 539 | 65.1% |
| 2 | Beauharnois, Canada | 73 | 8.8% |
| 3 | New York, United States | 72 | 8.7% |
| 4 | Warrenton, United States | 69 | 8.3% |
| 5 | Hillsboro, United States | 18 | 2.2% |
| 6 | North Bergen, United States | 17 | 2.1% |
| 7 | Amsterdam, Netherlands | 15 | 1.8% |
| 8 | Rome, Italy | 13 | 1.6% |
| 9 | Dublin, United States | 12 | 1.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `164.92.115.22` | 539 | 65.1% | United States / California / Santa Clara / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `92.204.128.6` | 69 | 8.3% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 3 | `85.217.149.47` | 27 | 3.3% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 4 | `85.217.149.34` | 21 | 2.5% | United States / New York / New York / Modat B.V | No apparent signal |
| 5 | `85.217.149.49` | 19 | 2.3% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 6 | `15.204.11.198` | 18 | 2.2% | United States / Oregon / Hillsboro / OVH US LLC | Hosting/Cloud (ovh) |
| 7 | `85.217.149.20` | 18 | 2.2% | United States / New York / New York / Modat B.V | No apparent signal |
| 8 | `85.217.149.17` | 18 | 2.2% | United States / New York / New York / Modat B.V | No apparent signal |
| 9 | `143.198.174.13` | 17 | 2.1% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 10 | `93.123.72.183` | 15 | 1.8% | Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 11 | `85.217.149.15` | 15 | 1.8% | United States / New York / New York / Modat B.V | No apparent signal |
| 12 | `85.217.149.42` | 14 | 1.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 13 | `79.63.45.2` | 13 | 1.6% | Italy / Lazio / Rome / INTERBUSINESS | Mobile/CGNAT (telecom italia) |
| 14 | `85.217.149.48` | 13 | 1.6% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 15 | `3.131.24.55` | 12 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `164.92.115.22` | 539 | 92.0% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / DigitalOcean, LLC |
| 2 | `15.204.11.198` | 18 | 3.1% | Hosting/Cloud (ovh) | United States / Oregon / Hillsboro / OVH US LLC |
| 3 | `143.198.174.13` | 17 | 2.9% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 4 | `3.131.24.55` | 12 | 2.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
