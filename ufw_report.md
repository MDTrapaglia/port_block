# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 654
- Unique source IPs: 453
- Unique countries/cities (24h): 99
- Unique destination ports: 473

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 99 | 15.1% |
| 2 | `8080` | 7 | 1.1% |
| 3 | `110` | 5 | 0.8% |
| 4 | `1194` | 5 | 0.8% |
| 5 | `8888` | 5 | 0.8% |
| 6 | `22` | 4 | 0.6% |
| 7 | `3389` | 4 | 0.6% |
| 8 | `8000` | 4 | 0.6% |
| 9 | `5060` | 4 | 0.6% |
| 10 | `1900` | 4 | 0.6% |
| 11 | `27015` | 4 | 0.6% |
| 12 | `6379` | 3 | 0.5% |
| 13 | `8081` | 3 | 0.5% |
| 14 | `unknown` | 3 | 0.5% |
| 15 | `54408` | 3 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 587 | 89.8% |
| 2 | `UDP` | 64 | 9.8% |
| 3 | `47` | 3 | 0.5% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `15.204.11.198` | 90 | 13.8% |
| 2 | `85.217.149.42` | 12 | 1.8% |
| 3 | `170.51.247.42` | 10 | 1.5% |
| 4 | `85.217.149.17` | 9 | 1.4% |
| 5 | `85.217.149.15` | 9 | 1.4% |
| 6 | `85.217.149.48` | 8 | 1.2% |
| 7 | `85.217.149.20` | 6 | 0.9% |
| 8 | `85.217.149.49` | 5 | 0.8% |
| 9 | `79.63.45.2` | 4 | 0.6% |
| 10 | `85.217.149.52` | 4 | 0.6% |
| 11 | `128.14.227.52` | 3 | 0.5% |
| 12 | `141.98.83.48` | 3 | 0.5% |
| 13 | `45.249.244.136` | 3 | 0.5% |
| 14 | `45.194.67.146` | 3 | 0.5% |
| 15 | `104.243.35.45` | 3 | 0.5% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 564 | 96.1% |
| 2 | `ACK+FIN+PSH` | 11 | 1.9% |
| 3 | `ACK+PSH` | 7 | 1.2% |
| 4 | `ACK+FIN` | 5 | 0.9% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 654 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `15.204.11.198` -> `23` | 90 | 13.8% |
| 2 | `79.63.45.2` -> `23` | 4 | 0.6% |
| 3 | `170.51.247.42` -> `54408` | 3 | 0.5% |
| 4 | `2.23.164.121` -> `18325` | 3 | 0.5% |
| 5 | `35.195.47.30` -> `110` | 2 | 0.3% |
| 6 | `141.98.83.48` -> `11211` | 2 | 0.3% |
| 7 | `170.51.247.42` -> `18205` | 2 | 0.3% |
| 8 | `170.51.241.136` -> `54466` | 2 | 0.3% |
| 9 | `170.51.247.42` -> `18211` | 2 | 0.3% |
| 10 | `2.23.164.154` -> `18137` | 2 | 0.3% |
| 11 | `45.198.224.18` -> `8728` | 2 | 0.3% |
| 12 | `69.17.52.1` -> `8333` | 2 | 0.3% |
| 13 | `199.195.248.205` -> `1194` | 2 | 0.3% |
| 14 | `34.79.153.219` -> `110` | 2 | 0.3% |
| 15 | `162.216.149.91` -> `48586` | 1 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-21 00:00:00:00 | 52 | 8.0% |
| 2026-06-21 01:00:00:00 | 196 | 30.0% |
| 2026-06-21 02:00:00:00 | 180 | 27.5% |
| 2026-06-21 03:00:00:00 | 179 | 27.4% |
| 2026-06-21 04:00:00:00 | 47 | 7.2% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Hillsboro, United States | 90 | 52.3% |
| 2 | Beauharnois, Canada | 29 | 16.9% |
| 3 | New York, United States | 24 | 14.0% |
| 4 | Buenos Aires, Argentina | 10 | 5.8% |
| 5 | Rome, Italy | 4 | 2.3% |
| 6 | Taipei, Taiwan | 3 | 1.7% |
| 7 | Panama City, Panama | 3 | 1.7% |
| 8 | Hong Kong, Hong Kong | 3 | 1.7% |
| 9 | São Paulo, Brazil | 3 | 1.7% |
| 10 | Piscataway, United States | 3 | 1.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `15.204.11.198` | 90 | 52.3% | United States / Oregon / Hillsboro / OVH US LLC | Hosting/Cloud (ovh) |
| 2 | `85.217.149.42` | 12 | 7.0% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 3 | `170.51.247.42` | 10 | 5.8% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 4 | `85.217.149.17` | 9 | 5.2% | United States / New York / New York / Modat B.V | No apparent signal |
| 5 | `85.217.149.15` | 9 | 5.2% | United States / New York / New York / Modat B.V | No apparent signal |
| 6 | `85.217.149.48` | 8 | 4.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 7 | `85.217.149.20` | 6 | 3.5% | United States / New York / New York / Modat B.V | No apparent signal |
| 8 | `85.217.149.49` | 5 | 2.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 9 | `79.63.45.2` | 4 | 2.3% | Italy / Lazio / Rome / INTERBUSINESS | Mobile/CGNAT (telecom italia) |
| 10 | `85.217.149.52` | 4 | 2.3% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 11 | `128.14.227.52` | 3 | 1.7% | Taiwan / Taipei City / Taipei / UCLOUD | No apparent signal |
| 12 | `141.98.83.48` | 3 | 1.7% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 13 | `45.249.244.136` | 3 | 1.7% | Hong Kong / Kowloon / Hong Kong / Ucloud Information Technology (hk) Limited | No apparent signal |
| 14 | `45.194.67.146` | 3 | 1.7% | Brazil / São Paulo / São Paulo / Cloud Innovation Ltd | No apparent signal |
| 15 | `104.243.35.45` | 3 | 1.7% | United States / New Jersey / Piscataway / OBDE Group | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `15.204.11.198` | 90 | 96.8% | Hosting/Cloud (ovh) | United States / Oregon / Hillsboro / OVH US LLC |
| 2 | `141.98.83.48` | 3 | 3.2% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
