# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4321
- Unique source IPs: 2596
- Unique countries/cities (24h): 380
- Unique destination ports: 2682

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 201 | 4.7% |
| 2 | `22` | 83 | 1.9% |
| 3 | `5060` | 42 | 1.0% |
| 4 | `8080` | 35 | 0.8% |
| 5 | `3389` | 27 | 0.6% |
| 6 | `53` | 26 | 0.6% |
| 7 | `3306` | 23 | 0.5% |
| 8 | `123` | 20 | 0.5% |
| 9 | `5900` | 19 | 0.4% |
| 10 | `1433` | 18 | 0.4% |
| 11 | `5432` | 18 | 0.4% |
| 12 | `unknown` | 18 | 0.4% |
| 13 | `21` | 17 | 0.4% |
| 14 | `8443` | 17 | 0.4% |
| 15 | `8081` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3871 | 89.6% |
| 2 | `UDP` | 432 | 10.0% |
| 3 | `47` | 16 | 0.4% |
| 4 | `41` | 1 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `2.26.29.47` | 72 | 1.7% |
| 2 | `103.167.89.213` | 58 | 1.3% |
| 3 | `103.153.183.18` | 19 | 0.4% |
| 4 | `172.110.223.179` | 15 | 0.3% |
| 5 | `85.217.140.19` | 14 | 0.3% |
| 6 | `85.217.140.30` | 14 | 0.3% |
| 7 | `85.217.140.7` | 13 | 0.3% |
| 8 | `141.98.83.48` | 13 | 0.3% |
| 9 | `149.33.19.95` | 13 | 0.3% |
| 10 | `85.217.140.6` | 12 | 0.3% |
| 11 | `18.217.208.51` | 12 | 0.3% |
| 12 | `85.217.140.22` | 11 | 0.3% |
| 13 | `18.190.15.50` | 11 | 0.3% |
| 14 | `85.217.140.34` | 11 | 0.3% |
| 15 | `85.217.149.37` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3857 | 99.6% |
| 2 | `SYN+ECE+CWR` | 10 | 0.3% |
| 3 | `ACK+PSH` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4321 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `172.110.223.179` -> `5060` | 15 | 0.3% |
| 2 | `202.112.237.201` -> `53` | 8 | 0.2% |
| 3 | `216.180.246.99` -> `8080` | 8 | 0.2% |
| 4 | `94.154.43.64` -> `123` | 5 | 0.1% |
| 5 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 6 | `69.17.52.1` -> `8333` | 5 | 0.1% |
| 7 | `77.239.124.127` -> `23` | 5 | 0.1% |
| 8 | `216.180.246.89` -> `53` | 5 | 0.1% |
| 9 | `198.244.200.163` -> `5060` | 4 | 0.1% |
| 10 | `77.239.124.127` -> `2323` | 4 | 0.1% |
| 11 | `80.87.206.19` -> `9443` | 4 | 0.1% |
| 12 | `66.132.172.186` -> `25` | 4 | 0.1% |
| 13 | `66.132.186.198` -> `3306` | 4 | 0.1% |
| 14 | `35.187.178.55` -> `22` | 4 | 0.1% |
| 15 | `124.105.184.49` -> `22` | 3 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-01 04:00:00:00 | 136 | 3.1% |
| 2026-09-01 05:00:00:00 | 179 | 4.1% |
| 2026-09-01 06:00:00:00 | 180 | 4.2% |
| 2026-09-01 07:00:00:00 | 180 | 4.2% |
| 2026-09-01 08:00:00:00 | 179 | 4.1% |
| 2026-09-01 09:00:00:00 | 180 | 4.2% |
| 2026-09-01 10:00:00:00 | 178 | 4.1% |
| 2026-09-01 11:00:00:00 | 182 | 4.2% |
| 2026-09-01 12:00:00:00 | 180 | 4.2% |
| 2026-09-01 13:00:00:00 | 181 | 4.2% |
| 2026-09-01 14:00:00:00 | 178 | 4.1% |
| 2026-09-01 15:00:00:00 | 180 | 4.2% |
| 2026-09-01 16:00:00:00 | 181 | 4.2% |
| 2026-09-01 17:00:00:00 | 180 | 4.2% |
| 2026-09-01 18:00:00:00 | 178 | 4.1% |
| 2026-09-01 19:00:00:00 | 183 | 4.2% |
| 2026-09-01 20:00:00:00 | 180 | 4.2% |
| 2026-09-01 21:00:00:00 | 179 | 4.1% |
| 2026-09-01 22:00:00:00 | 180 | 4.2% |
| 2026-09-01 23:00:00:00 | 181 | 4.2% |
| 2026-09-02 00:00:00:00 | 180 | 4.2% |
| 2026-09-02 01:00:00:00 | 180 | 4.2% |
| 2026-09-02 02:00:00:00 | 179 | 4.1% |
| 2026-09-02 03:00:00:00 | 180 | 4.2% |
| 2026-09-02 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 75 | 25.1% |
| 2 | Frankfurt am Main, Germany | 72 | 24.1% |
| 3 | Liên Chiểu, Vietnam | 58 | 19.4% |
| 4 | Dublin, United States | 23 | 7.7% |
| 5 | Dallas, United States | 19 | 6.4% |
| 6 | Atlanta, United States | 15 | 5.0% |
| 7 | Panama City, Panama | 13 | 4.3% |
| 8 | Buenos Aires, Argentina | 13 | 4.3% |
| 9 | Beauharnois, Canada | 11 | 3.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `2.26.29.47` | 72 | 24.1% | Germany / Hesse / Frankfurt am Main / Nekobyte International Limited | No apparent signal |
| 2 | `103.167.89.213` | 58 | 19.4% | Vietnam / Da Nang City / Liên Chiểu / Jobkey Joint Stock Company | No apparent signal |
| 3 | `103.153.183.18` | 19 | 6.4% | United States / Texas / Dallas / Harsh Jain | No apparent signal |
| 4 | `172.110.223.179` | 15 | 5.0% | United States / Georgia / Atlanta / Dedires LLC | No apparent signal |
| 5 | `85.217.140.19` | 14 | 4.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `85.217.140.30` | 14 | 4.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.7` | 13 | 4.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `141.98.83.48` | 13 | 4.3% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 9 | `149.33.19.95` | 13 | 4.3% | Argentina / Buenos Aires F.D. / Buenos Aires / 3NT SOLUTIONS LLP | No apparent signal |
| 10 | `85.217.140.6` | 12 | 4.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `18.217.208.51` | 12 | 4.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `85.217.140.22` | 11 | 3.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `18.190.15.50` | 11 | 3.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `85.217.140.34` | 11 | 3.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `85.217.149.37` | 11 | 3.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `141.98.83.48` | 13 | 36.1% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 2 | `18.217.208.51` | 12 | 33.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.190.15.50` | 11 | 30.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
