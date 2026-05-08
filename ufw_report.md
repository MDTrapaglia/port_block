# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4326
- Unique source IPs: 2462
- Unique countries/cities (24h): 327
- Unique destination ports: 2552

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 369 | 8.5% |
| 2 | `5060` | 38 | 0.9% |
| 3 | `22` | 32 | 0.7% |
| 4 | `3389` | 22 | 0.5% |
| 5 | `8080` | 21 | 0.5% |
| 6 | `8081` | 19 | 0.4% |
| 7 | `53` | 19 | 0.4% |
| 8 | `2222` | 17 | 0.4% |
| 9 | `21` | 16 | 0.4% |
| 10 | `3306` | 15 | 0.3% |
| 11 | `8443` | 15 | 0.3% |
| 12 | `25` | 15 | 0.3% |
| 13 | `1900` | 14 | 0.3% |
| 14 | `2323` | 14 | 0.3% |
| 15 | `1433` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3783 | 87.4% |
| 2 | `UDP` | 534 | 12.3% |
| 3 | `47` | 9 | 0.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.168.100.118` | 152 | 3.5% |
| 2 | `119.59.100.58` | 131 | 3.0% |
| 3 | `87.246.54.153` | 48 | 1.1% |
| 4 | `178.63.201.137` | 38 | 0.9% |
| 5 | `206.217.141.165` | 20 | 0.5% |
| 6 | `67.215.249.253` | 20 | 0.5% |
| 7 | `85.217.149.48` | 19 | 0.4% |
| 8 | `195.201.129.101` | 18 | 0.4% |
| 9 | `85.217.149.20` | 17 | 0.4% |
| 10 | `85.217.149.35` | 17 | 0.4% |
| 11 | `85.217.149.52` | 16 | 0.4% |
| 12 | `85.217.149.15` | 16 | 0.4% |
| 13 | `85.217.149.17` | 16 | 0.4% |
| 14 | `85.217.149.47` | 15 | 0.3% |
| 15 | `85.217.149.34` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3741 | 98.9% |
| 2 | `ACK+PSH` | 31 | 0.8% |
| 3 | `ACK` | 6 | 0.2% |
| 4 | `SYN+ECE+CWR` | 4 | 0.1% |
| 5 | `ACK+FIN+PSH` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4321 | 99.9% |
| 2 | `wlan0` | 5 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `119.59.100.58` -> `23` | 131 | 3.0% |
| 2 | `178.63.201.137` -> `23` | 38 | 0.9% |
| 3 | `206.217.141.165` -> `23` | 20 | 0.5% |
| 4 | `67.215.249.253` -> `23` | 20 | 0.5% |
| 5 | `195.201.129.101` -> `23` | 18 | 0.4% |
| 6 | `38.51.144.240` -> `64760` | 7 | 0.2% |
| 7 | `124.198.131.185` -> `8021` | 6 | 0.1% |
| 8 | `172.110.223.139` -> `5060` | 6 | 0.1% |
| 9 | `69.17.52.1` -> `8333` | 6 | 0.1% |
| 10 | `72.167.37.165` -> `23` | 5 | 0.1% |
| 11 | `51.159.110.167` -> `25564` | 5 | 0.1% |
| 12 | `192.168.100.1` -> `68` | 4 | 0.1% |
| 13 | `45.87.41.130` -> `23` | 4 | 0.1% |
| 14 | `51.159.110.167` -> `25565` | 4 | 0.1% |
| 15 | `66.132.195.105` -> `10001` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-07 04:00:00:00 | 133 | 3.1% |
| 2026-05-07 05:00:00:00 | 183 | 4.2% |
| 2026-05-07 06:00:00:00 | 180 | 4.2% |
| 2026-05-07 07:00:00:00 | 181 | 4.2% |
| 2026-05-07 08:00:00:00 | 181 | 4.2% |
| 2026-05-07 09:00:00:00 | 179 | 4.1% |
| 2026-05-07 10:00:00:00 | 181 | 4.2% |
| 2026-05-07 11:00:00:00 | 180 | 4.2% |
| 2026-05-07 12:00:00:00 | 179 | 4.1% |
| 2026-05-07 13:00:00:00 | 179 | 4.1% |
| 2026-05-07 14:00:00:00 | 182 | 4.2% |
| 2026-05-07 15:00:00:00 | 179 | 4.1% |
| 2026-05-07 16:00:00:00 | 181 | 4.2% |
| 2026-05-07 17:00:00:00 | 180 | 4.2% |
| 2026-05-07 18:00:00:00 | 180 | 4.2% |
| 2026-05-07 19:00:00:00 | 179 | 4.1% |
| 2026-05-07 20:00:00:00 | 181 | 4.2% |
| 2026-05-07 21:00:00:00 | 180 | 4.2% |
| 2026-05-07 22:00:00:00 | 180 | 4.2% |
| 2026-05-07 23:00:00:00 | 180 | 4.2% |
| 2026-05-08 00:00:00:00 | 178 | 4.1% |
| 2026-05-08 01:00:00:00 | 183 | 4.2% |
| 2026-05-08 02:00:00:00 | 180 | 4.2% |
| 2026-05-08 03:00:00:00 | 182 | 4.2% |
| 2026-05-08 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | private | 152 | 27.2% |
| 2 | Bang Rak, Thailand | 131 | 23.5% |
| 3 | Beauharnois, Canada | 67 | 12.0% |
| 4 | New York, United States | 64 | 11.5% |
| 5 | Rousse, Bulgaria | 48 | 8.6% |
| 6 | Falkenstein, Germany | 38 | 6.8% |
| 7 | Elk Grove Village, United States | 20 | 3.6% |
| 8 | Los Angeles, United States | 20 | 3.6% |
| 9 | Nuremberg, Germany | 18 | 3.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.168.100.118` | 152 | 27.2% | private | Private/CGNAT |
| 2 | `119.59.100.58` | 131 | 23.5% | Thailand / Bangkok / Bang Rak / Metrabyte Co., Ltd | No apparent signal |
| 3 | `87.246.54.153` | 48 | 8.6% | Bulgaria / Ruse / Rousse / Cablenet Ruse | No apparent signal |
| 4 | `178.63.201.137` | 38 | 6.8% | Germany / Saxony / Falkenstein / Hetzner Online GmbH | Hosting/Cloud (hetzner) |
| 5 | `206.217.141.165` | 20 | 3.6% | United States / Illinois / Elk Grove Village / RackNerd LLC | No apparent signal |
| 6 | `67.215.249.253` | 20 | 3.6% | United States / California / Los Angeles / RackNerd LLC | No apparent signal |
| 7 | `85.217.149.48` | 19 | 3.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 8 | `195.201.129.101` | 18 | 3.2% | Germany / Bavaria / Nuremberg / Hetzner Online GmbH | Hosting/Cloud (hetzner) |
| 9 | `85.217.149.20` | 17 | 3.0% | United States / New York / New York / Modat B.V | No apparent signal |
| 10 | `85.217.149.35` | 17 | 3.0% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 11 | `85.217.149.52` | 16 | 2.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 12 | `85.217.149.15` | 16 | 2.9% | United States / New York / New York / Modat B.V | No apparent signal |
| 13 | `85.217.149.17` | 16 | 2.9% | United States / New York / New York / Modat B.V | No apparent signal |
| 14 | `85.217.149.47` | 15 | 2.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 15 | `85.217.149.34` | 15 | 2.7% | United States / New York / New York / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `178.63.201.137` | 38 | 67.9% | Hosting/Cloud (hetzner) | Germany / Saxony / Falkenstein / Hetzner Online GmbH |
| 2 | `195.201.129.101` | 18 | 32.1% | Hosting/Cloud (hetzner) | Germany / Bavaria / Nuremberg / Hetzner Online GmbH |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
