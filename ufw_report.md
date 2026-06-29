# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4352
- Unique source IPs: 2605
- Unique countries/cities (24h): 400
- Unique destination ports: 1933

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1018 | 23.4% |
| 2 | `22` | 428 | 9.8% |
| 3 | `unknown` | 41 | 0.9% |
| 4 | `8080` | 35 | 0.8% |
| 5 | `53` | 24 | 0.6% |
| 6 | `88` | 22 | 0.5% |
| 7 | `8443` | 21 | 0.5% |
| 8 | `5060` | 19 | 0.4% |
| 9 | `27015` | 18 | 0.4% |
| 10 | `21` | 17 | 0.4% |
| 11 | `3389` | 17 | 0.4% |
| 12 | `25565` | 16 | 0.4% |
| 13 | `81` | 14 | 0.3% |
| 14 | `1433` | 14 | 0.3% |
| 15 | `554` | 12 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3951 | 90.8% |
| 2 | `UDP` | 360 | 8.3% |
| 3 | `47` | 40 | 0.9% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `117.245.143.81` | 114 | 2.6% |
| 2 | `59.180.154.177` | 101 | 2.3% |
| 3 | `78.128.114.66` | 40 | 0.9% |
| 4 | `59.180.147.102` | 33 | 0.8% |
| 5 | `78.128.114.46` | 32 | 0.7% |
| 6 | `92.204.138.44` | 30 | 0.7% |
| 7 | `85.217.149.42` | 25 | 0.6% |
| 8 | `85.217.149.17` | 25 | 0.6% |
| 9 | `62.210.142.164` | 24 | 0.6% |
| 10 | `192.169.179.77` | 21 | 0.5% |
| 11 | `93.123.72.183` | 19 | 0.4% |
| 12 | `85.217.149.20` | 19 | 0.4% |
| 13 | `82.66.201.8` | 18 | 0.4% |
| 14 | `85.217.149.15` | 18 | 0.4% |
| 15 | `79.124.40.106` | 18 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3900 | 98.7% |
| 2 | `ACK+FIN+PSH` | 23 | 0.6% |
| 3 | `ACK+PSH` | 21 | 0.5% |
| 4 | `ACK+FIN` | 4 | 0.1% |
| 5 | `SYN+ECE+CWR` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4347 | 99.9% |
| 2 | `wlan0` | 5 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `117.245.143.81` -> `23` | 114 | 2.6% |
| 2 | `59.180.154.177` -> `23` | 101 | 2.3% |
| 3 | `59.180.147.102` -> `23` | 33 | 0.8% |
| 4 | `92.204.138.44` -> `23` | 30 | 0.7% |
| 5 | `192.169.179.77` -> `23` | 21 | 0.5% |
| 6 | `82.66.201.8` -> `23` | 18 | 0.4% |
| 7 | `132.148.29.10` -> `23` | 14 | 0.3% |
| 8 | `94.156.152.50` -> `23` | 11 | 0.3% |
| 9 | `198.89.99.140` -> `25565` | 10 | 0.2% |
| 10 | `222.79.104.148` -> `6379` | 8 | 0.2% |
| 11 | `93.123.72.183` -> `88` | 7 | 0.2% |
| 12 | `216.180.246.56` -> `53` | 7 | 0.2% |
| 13 | `117.254.113.181` -> `23` | 6 | 0.1% |
| 14 | `216.180.246.111` -> `8080` | 6 | 0.1% |
| 15 | `184.31.2.68` -> `37076` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-28 04:00:00:00 | 135 | 3.1% |
| 2026-06-28 05:00:00:00 | 180 | 4.1% |
| 2026-06-28 06:00:00:00 | 179 | 4.1% |
| 2026-06-28 07:00:00:00 | 182 | 4.2% |
| 2026-06-28 08:00:00:00 | 179 | 4.1% |
| 2026-06-28 09:00:00:00 | 180 | 4.1% |
| 2026-06-28 10:00:00:00 | 181 | 4.2% |
| 2026-06-28 11:00:00:00 | 180 | 4.1% |
| 2026-06-28 12:00:00:00 | 179 | 4.1% |
| 2026-06-28 13:00:00:00 | 184 | 4.2% |
| 2026-06-28 14:00:00:00 | 182 | 4.2% |
| 2026-06-28 15:00:00:00 | 180 | 4.1% |
| 2026-06-28 16:00:00:00 | 180 | 4.1% |
| 2026-06-28 17:00:00:00 | 177 | 4.1% |
| 2026-06-28 18:00:00:00 | 185 | 4.3% |
| 2026-06-28 19:00:00:00 | 179 | 4.1% |
| 2026-06-28 20:00:00:00 | 182 | 4.2% |
| 2026-06-28 21:00:00:00 | 179 | 4.1% |
| 2026-06-28 22:00:00:00 | 180 | 4.1% |
| 2026-06-28 23:00:00:00 | 204 | 4.7% |
| 2026-06-29 00:00:00:00 | 179 | 4.1% |
| 2026-06-29 01:00:00:00 | 181 | 4.2% |
| 2026-06-29 02:00:00:00 | 180 | 4.1% |
| 2026-06-29 03:00:00:00 | 180 | 4.1% |
| 2026-06-29 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Jodhpur, India | 114 | 21.2% |
| 2 | New Delhi, India | 101 | 18.8% |
| 3 | Karlovo, Bulgaria | 72 | 13.4% |
| 4 | New York, United States | 62 | 11.5% |
| 5 | Delhi, India | 33 | 6.1% |
| 6 | Warrenton, United States | 30 | 5.6% |
| 7 | Beauharnois, Canada | 25 | 4.7% |
| 8 | Paris, France | 24 | 4.5% |
| 9 | Tempe, United States | 21 | 3.9% |
| 10 | Amsterdam, Netherlands | 19 | 3.5% |
| 11 | Nice, France | 18 | 3.4% |
| 12 | Sopot, Bulgaria | 18 | 3.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `117.245.143.81` | 114 | 21.2% | India / Rajasthan / Jodhpur / BSNL Internet | No apparent signal |
| 2 | `59.180.154.177` | 101 | 18.8% | India / National Capital Territory of Delhi / New Delhi / MTNL Mumbai | No apparent signal |
| 3 | `78.128.114.66` | 40 | 7.4% | Bulgaria / Plovdiv / Karlovo / Tamatiya EOOD | No apparent signal |
| 4 | `59.180.147.102` | 33 | 6.1% | India / National Capital Territory of Delhi / Delhi / MTNL Mumbai | No apparent signal |
| 5 | `78.128.114.46` | 32 | 6.0% | Bulgaria / Plovdiv / Karlovo / Tamatiya EOOD | No apparent signal |
| 6 | `92.204.138.44` | 30 | 5.6% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 7 | `85.217.149.42` | 25 | 4.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 8 | `85.217.149.17` | 25 | 4.7% | United States / New York / New York / Modat B.V | No apparent signal |
| 9 | `62.210.142.164` | 24 | 4.5% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 10 | `192.169.179.77` | 21 | 3.9% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 11 | `93.123.72.183` | 19 | 3.5% | Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 12 | `85.217.149.20` | 19 | 3.5% | United States / New York / New York / Modat B.V | No apparent signal |
| 13 | `82.66.201.8` | 18 | 3.4% | France / Provence-Alpes-Côte d'Azur / Nice / ProXad network / Free SA | No apparent signal |
| 14 | `85.217.149.15` | 18 | 3.4% | United States / New York / New York / Modat B.V | No apparent signal |
| 15 | `79.124.40.106` | 18 | 3.4% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.164` | 24 | 100.0% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
