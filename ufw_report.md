# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4307
- Unique source IPs: 2503
- Unique countries/cities (24h): 452
- Unique destination ports: 2254

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 336 | 7.8% |
| 2 | `27015` | 73 | 1.7% |
| 3 | `22` | 50 | 1.2% |
| 4 | `3389` | 42 | 1.0% |
| 5 | `5060` | 38 | 0.9% |
| 6 | `8080` | 33 | 0.8% |
| 7 | `1433` | 27 | 0.6% |
| 8 | `8443` | 22 | 0.5% |
| 9 | `8081` | 21 | 0.5% |
| 10 | `21` | 20 | 0.5% |
| 11 | `8082` | 19 | 0.4% |
| 12 | `8333` | 19 | 0.4% |
| 13 | `8888` | 19 | 0.4% |
| 14 | `53` | 18 | 0.4% |
| 15 | `3306` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3787 | 87.9% |
| 2 | `UDP` | 510 | 11.8% |
| 3 | `47` | 9 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.114` | 101 | 2.3% |
| 2 | `165.22.105.175` | 42 | 1.0% |
| 3 | `92.204.138.198` | 35 | 0.8% |
| 4 | `85.217.149.18` | 30 | 0.7% |
| 5 | `85.217.149.35` | 24 | 0.6% |
| 6 | `85.217.149.43` | 21 | 0.5% |
| 7 | `69.17.52.1` | 18 | 0.4% |
| 8 | `77.91.71.66` | 18 | 0.4% |
| 9 | `85.217.149.49` | 17 | 0.4% |
| 10 | `103.166.200.226` | 17 | 0.4% |
| 11 | `77.91.71.67` | 16 | 0.4% |
| 12 | `85.217.149.15` | 16 | 0.4% |
| 13 | `194.180.49.245` | 16 | 0.4% |
| 14 | `45.198.224.10` | 15 | 0.3% |
| 15 | `138.226.239.21` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3724 | 98.3% |
| 2 | `ACK+PSH` | 28 | 0.7% |
| 3 | `ACK` | 13 | 0.3% |
| 4 | `ACK+FIN+PSH` | 12 | 0.3% |
| 5 | `SYN+ECE+CWR` | 10 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4305 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `165.22.105.175` -> `23` | 42 | 1.0% |
| 2 | `92.204.138.198` -> `23` | 35 | 0.8% |
| 3 | `69.17.52.1` -> `8333` | 18 | 0.4% |
| 4 | `103.166.200.226` -> `23` | 17 | 0.4% |
| 5 | `176.67.174.7` -> `23` | 13 | 0.3% |
| 6 | `216.180.246.114` -> `6002` | 12 | 0.3% |
| 7 | `216.180.246.114` -> `2050` | 9 | 0.2% |
| 8 | `216.180.246.114` -> `50277` | 9 | 0.2% |
| 9 | `216.180.246.114` -> `50300` | 8 | 0.2% |
| 10 | `216.180.246.114` -> `17007` | 8 | 0.2% |
| 11 | `216.180.246.114` -> `1129` | 8 | 0.2% |
| 12 | `216.180.246.203` -> `9417` | 8 | 0.2% |
| 13 | `138.226.239.21` -> `3389` | 7 | 0.2% |
| 14 | `216.180.246.114` -> `11111` | 7 | 0.2% |
| 15 | `178.20.210.152` -> `1723` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-24 04:00:00:00 | 132 | 3.1% |
| 2026-05-24 05:00:00:00 | 182 | 4.2% |
| 2026-05-24 06:00:00:00 | 181 | 4.2% |
| 2026-05-24 07:00:00:00 | 180 | 4.2% |
| 2026-05-24 08:00:00:00 | 185 | 4.3% |
| 2026-05-24 09:00:00:00 | 181 | 4.2% |
| 2026-05-24 10:00:00:00 | 181 | 4.2% |
| 2026-05-24 11:00:00:00 | 165 | 3.8% |
| 2026-05-24 12:00:00:00 | 180 | 4.2% |
| 2026-05-24 13:00:00:00 | 174 | 4.0% |
| 2026-05-24 14:00:00:00 | 180 | 4.2% |
| 2026-05-24 15:00:00:00 | 181 | 4.2% |
| 2026-05-24 16:00:00:00 | 180 | 4.2% |
| 2026-05-24 17:00:00:00 | 179 | 4.2% |
| 2026-05-24 18:00:00:00 | 181 | 4.2% |
| 2026-05-24 19:00:00:00 | 177 | 4.1% |
| 2026-05-24 20:00:00:00 | 180 | 4.2% |
| 2026-05-24 21:00:00:00 | 180 | 4.2% |
| 2026-05-24 22:00:00:00 | 180 | 4.2% |
| 2026-05-24 23:00:00:00 | 179 | 4.2% |
| 2026-05-25 00:00:00:00 | 181 | 4.2% |
| 2026-05-25 01:00:00:00 | 180 | 4.2% |
| 2026-05-25 02:00:00:00 | 182 | 4.2% |
| 2026-05-25 03:00:00:00 | 180 | 4.2% |
| 2026-05-25 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 101 | 25.2% |
| 2 | New York, United States | 67 | 16.7% |
| 3 | Singapore, Singapore | 42 | 10.5% |
| 4 | Beauharnois, Canada | 41 | 10.2% |
| 5 | Warrenton, United States | 35 | 8.7% |
| 6 | Jerusalem, Israel | 34 | 8.5% |
| 7 | Lewes, United States | 18 | 4.5% |
| 8 | Jakarta, Indonesia | 17 | 4.2% |
| 9 | Berngau, Germany | 16 | 4.0% |
| 10 | Stockholm, Sweden | 15 | 3.7% |
| 11 | Port Vila, Vanuatu | 15 | 3.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.114` | 101 | 25.2% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `165.22.105.175` | 42 | 10.5% | Singapore / South West / Singapore / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 3 | `92.204.138.198` | 35 | 8.7% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 4 | `85.217.149.18` | 30 | 7.5% | United States / New York / New York / Modat B.V | No apparent signal |
| 5 | `85.217.149.35` | 24 | 6.0% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 6 | `85.217.149.43` | 21 | 5.2% | United States / New York / New York / Modat B.V | No apparent signal |
| 7 | `69.17.52.1` | 18 | 4.5% | United States / Delaware / Lewes / Spruce Creek Networks LLC | No apparent signal |
| 8 | `77.91.71.66` | 18 | 4.5% | Israel / Jerusalem / Jerusalem / Proline IT Ltd | No apparent signal |
| 9 | `85.217.149.49` | 17 | 4.2% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 10 | `103.166.200.226` | 17 | 4.2% | Indonesia / Jakarta / Jakarta / Hipernet Indodata | No apparent signal |
| 11 | `77.91.71.67` | 16 | 4.0% | Israel / Jerusalem / Jerusalem / Proline IT Ltd | No apparent signal |
| 12 | `85.217.149.15` | 16 | 4.0% | United States / New York / New York / Modat B.V | No apparent signal |
| 13 | `194.180.49.245` | 16 | 4.0% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 14 | `45.198.224.10` | 15 | 3.7% | Sweden / Stockholm County / Stockholm / Cloud Innovation Ltd | No apparent signal |
| 15 | `138.226.239.21` | 15 | 3.7% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.114` | 101 | 70.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `165.22.105.175` | 42 | 29.4% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
