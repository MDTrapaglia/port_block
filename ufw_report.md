# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4395
- Unique source IPs: 2535
- Unique countries/cities (24h): 417
- Unique destination ports: 2342

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 774 | 17.6% |
| 2 | `22` | 42 | 1.0% |
| 3 | `5060` | 35 | 0.8% |
| 4 | `unknown` | 26 | 0.6% |
| 5 | `8080` | 21 | 0.5% |
| 6 | `3389` | 17 | 0.4% |
| 7 | `1433` | 16 | 0.4% |
| 8 | `8443` | 15 | 0.3% |
| 9 | `53` | 15 | 0.3% |
| 10 | `2222` | 15 | 0.3% |
| 11 | `27017` | 14 | 0.3% |
| 12 | `9200` | 14 | 0.3% |
| 13 | `8081` | 14 | 0.3% |
| 14 | `3306` | 14 | 0.3% |
| 15 | `161` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3972 | 90.4% |
| 2 | `UDP` | 397 | 9.0% |
| 3 | `47` | 24 | 0.5% |
| 4 | `4` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `103.149.105.124` | 36 | 0.8% |
| 2 | `208.82.117.120` | 35 | 0.8% |
| 3 | `151.101.218.73` | 34 | 0.8% |
| 4 | `160.119.76.21` | 32 | 0.7% |
| 5 | `103.149.105.147` | 31 | 0.7% |
| 6 | `159.203.13.117` | 30 | 0.7% |
| 7 | `209.205.219.218` | 27 | 0.6% |
| 8 | `46.175.128.193` | 27 | 0.6% |
| 9 | `207.244.245.89` | 27 | 0.6% |
| 10 | `103.98.104.59` | 26 | 0.6% |
| 11 | `124.198.131.185` | 18 | 0.4% |
| 12 | `165.227.169.148` | 18 | 0.4% |
| 13 | `38.60.162.99` | 16 | 0.4% |
| 14 | `45.142.193.53` | 15 | 0.3% |
| 15 | `89.248.163.48` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3871 | 97.5% |
| 2 | `ACK+FIN+PSH` | 63 | 1.6% |
| 3 | `ACK+PSH` | 23 | 0.6% |
| 4 | `ACK+FIN` | 10 | 0.3% |
| 5 | `ACK` | 4 | 0.1% |
| 6 | `SYN+ECE+CWR` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4395 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `208.82.117.120` -> `23` | 35 | 0.8% |
| 2 | `159.203.13.117` -> `23` | 30 | 0.7% |
| 3 | `209.205.219.218` -> `23` | 27 | 0.6% |
| 4 | `46.175.128.193` -> `23` | 27 | 0.6% |
| 5 | `207.244.245.89` -> `23` | 27 | 0.6% |
| 6 | `103.98.104.59` -> `23` | 26 | 0.6% |
| 7 | `165.227.169.148` -> `23` | 18 | 0.4% |
| 8 | `38.60.162.99` -> `23` | 16 | 0.4% |
| 9 | `162.240.155.31` -> `23` | 14 | 0.3% |
| 10 | `104.248.79.116` -> `23` | 12 | 0.3% |
| 11 | `142.4.11.253` -> `23` | 12 | 0.3% |
| 12 | `103.175.216.43` -> `23` | 11 | 0.3% |
| 13 | `162.241.87.115` -> `23` | 11 | 0.3% |
| 14 | `35.241.171.18` -> `23` | 11 | 0.3% |
| 15 | `69.17.52.1` -> `8333` | 10 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-04-30 04:00:00:00 | 136 | 3.1% |
| 2026-04-30 05:00:00:00 | 177 | 4.0% |
| 2026-04-30 06:00:00:00 | 183 | 4.2% |
| 2026-04-30 07:00:00:00 | 180 | 4.1% |
| 2026-04-30 08:00:00:00 | 181 | 4.1% |
| 2026-04-30 09:00:00:00 | 178 | 4.1% |
| 2026-04-30 10:00:00:00 | 182 | 4.1% |
| 2026-04-30 11:00:00:00 | 179 | 4.1% |
| 2026-04-30 12:00:00:00 | 178 | 4.1% |
| 2026-04-30 13:00:00:00 | 197 | 4.5% |
| 2026-04-30 14:00:00:00 | 178 | 4.1% |
| 2026-04-30 15:00:00:00 | 191 | 4.3% |
| 2026-04-30 16:00:00:00 | 178 | 4.1% |
| 2026-04-30 17:00:00:00 | 198 | 4.5% |
| 2026-04-30 18:00:00:00 | 176 | 4.0% |
| 2026-04-30 19:00:00:00 | 183 | 4.2% |
| 2026-04-30 20:00:00:00 | 180 | 4.1% |
| 2026-04-30 21:00:00:00 | 180 | 4.1% |
| 2026-04-30 22:00:00:00 | 193 | 4.4% |
| 2026-04-30 23:00:00:00 | 197 | 4.5% |
| 2026-05-01 00:00:00:00 | 179 | 4.1% |
| 2026-05-01 01:00:00:00 | 184 | 4.2% |
| 2026-05-01 02:00:00:00 | 182 | 4.1% |
| 2026-05-01 03:00:00:00 | 180 | 4.1% |
| 2026-05-01 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dhaka, Bangladesh | 67 | 17.4% |
| 2 | Amsterdam, The Netherlands | 46 | 11.9% |
| 3 | San Clemente, United States | 35 | 9.1% |
| 4 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 34 | 8.8% |
| 5 | Toronto, Canada | 30 | 7.8% |
| 6 | Piscataway, United States | 27 | 7.0% |
| 7 | Almería, Spain | 27 | 7.0% |
| 8 | St Louis, United States | 27 | 7.0% |
| 9 | Kuningan Barat, Indonesia | 26 | 6.7% |
| 10 | New York, United States | 18 | 4.7% |
| 11 | Frankfurt am Main, Germany | 18 | 4.7% |
| 12 | Los Altos, United States | 16 | 4.1% |
| 13 | London, United Kingdom | 15 | 3.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `103.149.105.124` | 36 | 9.3% | Bangladesh / Dhaka Division / Dhaka / Netcom Internet | No apparent signal |
| 2 | `208.82.117.120` | 35 | 9.1% | United States / California / San Clemente / NDCHost | Hosting/Cloud (data center) |
| 3 | `151.101.218.73` | 34 | 8.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `160.119.76.21` | 32 | 8.3% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |
| 5 | `103.149.105.147` | 31 | 8.0% | Bangladesh / Dhaka Division / Dhaka / Netcom Internet | No apparent signal |
| 6 | `159.203.13.117` | 30 | 7.8% | Canada / Ontario / Toronto / Digital Ocean | Hosting/Cloud (digitalocean) |
| 7 | `209.205.219.218` | 27 | 7.0% | United States / New Jersey / Piscataway / B2 Net Solutions Inc. | No apparent signal |
| 8 | `46.175.128.193` | 27 | 7.0% | Spain / Andalusia / Almería / Soluciones web on line s.l | No apparent signal |
| 9 | `207.244.245.89` | 27 | 7.0% | United States / Missouri / St Louis / Contabo Inc | Hosting/Cloud (contabo) |
| 10 | `103.98.104.59` | 26 | 6.7% | Indonesia / Jakarta / Kuningan Barat / PT. TRIMEDIA SETIYA DATA | No apparent signal |
| 11 | `124.198.131.185` | 18 | 4.7% | United States / New York / New York / 1337 Services GmbH | No apparent signal |
| 12 | `165.227.169.148` | 18 | 4.7% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `38.60.162.99` | 16 | 4.1% | United States / California / Los Altos / KaopuCloud-US | No apparent signal |
| 14 | `45.142.193.53` | 15 | 3.9% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 15 | `89.248.163.48` | 14 | 3.6% | The Netherlands / North Holland / Amsterdam / Quasi Networks LTD. | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `208.82.117.120` | 35 | 24.3% | Hosting/Cloud (data center) | United States / California / San Clemente / NDCHost |
| 2 | `151.101.218.73` | 34 | 23.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `159.203.13.117` | 30 | 20.8% | Hosting/Cloud (digitalocean) | Canada / Ontario / Toronto / Digital Ocean |
| 4 | `207.244.245.89` | 27 | 18.8% | Hosting/Cloud (contabo) | United States / Missouri / St Louis / Contabo Inc |
| 5 | `165.227.169.148` | 18 | 12.5% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
