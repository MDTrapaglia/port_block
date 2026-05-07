# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4342
- Unique source IPs: 2441
- Unique countries/cities (24h): 396
- Unique destination ports: 2379

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 480 | 11.1% |
| 2 | `22` | 51 | 1.2% |
| 3 | `5060` | 40 | 0.9% |
| 4 | `8080` | 34 | 0.8% |
| 5 | `unknown` | 23 | 0.5% |
| 6 | `3389` | 22 | 0.5% |
| 7 | `1433` | 22 | 0.5% |
| 8 | `2222` | 21 | 0.5% |
| 9 | `3306` | 20 | 0.5% |
| 10 | `3000` | 19 | 0.4% |
| 11 | `21` | 15 | 0.3% |
| 12 | `9000` | 15 | 0.3% |
| 13 | `10001` | 15 | 0.3% |
| 14 | `8443` | 15 | 0.3% |
| 15 | `1900` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3896 | 89.7% |
| 2 | `UDP` | 423 | 9.7% |
| 3 | `47` | 21 | 0.5% |
| 4 | `4` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `165.232.143.119` | 240 | 5.5% |
| 2 | `31.131.21.223` | 57 | 1.3% |
| 3 | `130.12.180.30` | 29 | 0.7% |
| 4 | `192.168.100.118` | 21 | 0.5% |
| 5 | `85.217.149.18` | 18 | 0.4% |
| 6 | `85.217.149.17` | 17 | 0.4% |
| 7 | `85.217.149.41` | 16 | 0.4% |
| 8 | `100.28.252.28` | 16 | 0.4% |
| 9 | `43.241.37.190` | 16 | 0.4% |
| 10 | `85.217.149.34` | 15 | 0.3% |
| 11 | `172.93.106.153` | 15 | 0.3% |
| 12 | `85.217.149.20` | 14 | 0.3% |
| 13 | `85.217.149.15` | 14 | 0.3% |
| 14 | `85.217.149.42` | 13 | 0.3% |
| 15 | `124.198.131.185` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3802 | 97.6% |
| 2 | `ACK+PSH` | 38 | 1.0% |
| 3 | `ACK+FIN+PSH` | 36 | 0.9% |
| 4 | `ACK+FIN` | 10 | 0.3% |
| 5 | `ACK` | 6 | 0.2% |
| 6 | `SYN+ECE+CWR` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4342 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `165.232.143.119` -> `23` | 240 | 5.5% |
| 2 | `43.241.37.190` -> `23` | 16 | 0.4% |
| 3 | `72.167.54.122` -> `23` | 11 | 0.3% |
| 4 | `34.102.215.99` -> `53976` | 8 | 0.2% |
| 5 | `124.198.131.185` -> `8021` | 8 | 0.2% |
| 6 | `100.28.252.28` -> `5173` | 7 | 0.2% |
| 7 | `69.17.52.1` -> `8333` | 7 | 0.2% |
| 8 | `50.194.130.34` -> `23` | 6 | 0.1% |
| 9 | `46.151.178.13` -> `17000` | 5 | 0.1% |
| 10 | `124.198.131.185` -> `3000` | 5 | 0.1% |
| 11 | `100.28.252.28` -> `5175` | 5 | 0.1% |
| 12 | `51.159.110.167` -> `25564` | 5 | 0.1% |
| 13 | `3.132.37.209` -> `60516` | 5 | 0.1% |
| 14 | `180.167.128.203` -> `22` | 4 | 0.1% |
| 15 | `5.135.173.212` -> `5060` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-06 04:00:00:00 | 137 | 3.2% |
| 2026-05-06 05:00:00:00 | 180 | 4.1% |
| 2026-05-06 06:00:00:00 | 178 | 4.1% |
| 2026-05-06 07:00:00:00 | 160 | 3.7% |
| 2026-05-06 08:00:00:00 | 182 | 4.2% |
| 2026-05-06 09:00:00:00 | 182 | 4.2% |
| 2026-05-06 10:00:00:00 | 182 | 4.2% |
| 2026-05-06 11:00:00:00 | 181 | 4.2% |
| 2026-05-06 12:00:00:00 | 181 | 4.2% |
| 2026-05-06 13:00:00:00 | 177 | 4.1% |
| 2026-05-06 14:00:00:00 | 179 | 4.1% |
| 2026-05-06 15:00:00:00 | 180 | 4.1% |
| 2026-05-06 16:00:00:00 | 179 | 4.1% |
| 2026-05-06 17:00:00:00 | 177 | 4.1% |
| 2026-05-06 18:00:00:00 | 183 | 4.2% |
| 2026-05-06 19:00:00:00 | 181 | 4.2% |
| 2026-05-06 20:00:00:00 | 180 | 4.1% |
| 2026-05-06 21:00:00:00 | 180 | 4.1% |
| 2026-05-06 22:00:00:00 | 192 | 4.4% |
| 2026-05-06 23:00:00:00 | 192 | 4.4% |
| 2026-05-07 00:00:00:00 | 190 | 4.4% |
| 2026-05-07 01:00:00:00 | 184 | 4.2% |
| 2026-05-07 02:00:00:00 | 181 | 4.2% |
| 2026-05-07 03:00:00:00 | 179 | 4.1% |
| 2026-05-07 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Santa Clara, United States | 240 | 46.7% |
| 2 | New York, United States | 107 | 20.8% |
| 3 | Rotterdam, Netherlands | 57 | 11.1% |
| 4 | Amsterdam, Netherlands | 29 | 5.6% |
| 5 | private | 21 | 4.1% |
| 6 | Ashburn, United States | 16 | 3.1% |
| 7 | Navi Mumbai, India | 16 | 3.1% |
| 8 | Piscataway, United States | 15 | 2.9% |
| 9 | Beauharnois, Canada | 13 | 2.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `165.232.143.119` | 240 | 46.7% | United States / California / Santa Clara / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `31.131.21.223` | 57 | 11.1% | Netherlands / South Holland / Rotterdam / PE Skurykhin Mukola Volodumurovuch | No apparent signal |
| 3 | `130.12.180.30` | 29 | 5.6% | Netherlands / North Holland / Amsterdam / Virtualine Technologies | No apparent signal |
| 4 | `192.168.100.118` | 21 | 4.1% | private | Private/CGNAT |
| 5 | `85.217.149.18` | 18 | 3.5% | United States / New York / New York / Modat B.V | No apparent signal |
| 6 | `85.217.149.17` | 17 | 3.3% | United States / New York / New York / Modat B.V | No apparent signal |
| 7 | `85.217.149.41` | 16 | 3.1% | United States / New York / New York / Modat B.V | No apparent signal |
| 8 | `100.28.252.28` | 16 | 3.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 9 | `43.241.37.190` | 16 | 3.1% | India / Maharashtra / Navi Mumbai / WEBWERKS | No apparent signal |
| 10 | `85.217.149.34` | 15 | 2.9% | United States / New York / New York / Modat B.V | No apparent signal |
| 11 | `172.93.106.153` | 15 | 2.9% | United States / New Jersey / Piscataway / Klemen Stirn | No apparent signal |
| 12 | `85.217.149.20` | 14 | 2.7% | United States / New York / New York / Modat B.V | No apparent signal |
| 13 | `85.217.149.15` | 14 | 2.7% | United States / New York / New York / Modat B.V | No apparent signal |
| 14 | `85.217.149.42` | 13 | 2.5% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 15 | `124.198.131.185` | 13 | 2.5% | United States / New York / New York / 1337 Services GmbH | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `165.232.143.119` | 240 | 93.8% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / DigitalOcean, LLC |
| 2 | `100.28.252.28` | 16 | 6.2% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
