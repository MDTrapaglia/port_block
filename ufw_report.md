# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 765
- Unique source IPs: 625
- Unique countries/cities (24h): 110
- Unique destination ports: 569

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 20 | 2.6% |
| 2 | `53` | 17 | 2.2% |
| 3 | `22` | 9 | 1.2% |
| 4 | `3306` | 8 | 1.0% |
| 5 | `1433` | 7 | 0.9% |
| 6 | `8080` | 7 | 0.9% |
| 7 | `3389` | 7 | 0.9% |
| 8 | `5060` | 5 | 0.7% |
| 9 | `8443` | 5 | 0.7% |
| 10 | `21` | 5 | 0.7% |
| 11 | `9000` | 5 | 0.7% |
| 12 | `2222` | 5 | 0.7% |
| 13 | `25` | 4 | 0.5% |
| 14 | `8081` | 4 | 0.5% |
| 15 | `2000` | 4 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 693 | 90.6% |
| 2 | `UDP` | 72 | 9.4% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `202.112.237.201` | 7 | 0.9% |
| 2 | `185.242.226.85` | 6 | 0.8% |
| 3 | `45.148.121.138` | 5 | 0.7% |
| 4 | `195.178.110.92` | 5 | 0.7% |
| 5 | `185.242.226.72` | 5 | 0.7% |
| 6 | `34.230.221.101` | 4 | 0.5% |
| 7 | `86.54.31.36` | 4 | 0.5% |
| 8 | `47.100.201.178` | 4 | 0.5% |
| 9 | `172.110.223.81` | 4 | 0.5% |
| 10 | `34.197.70.90` | 3 | 0.4% |
| 11 | `186.123.1.125` | 3 | 0.4% |
| 12 | `66.132.159.83` | 3 | 0.4% |
| 13 | `66.132.195.117` | 3 | 0.4% |
| 14 | `71.6.155.70` | 3 | 0.4% |
| 15 | `91.231.89.69` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 692 | 99.9% |
| 2 | `SYN+ECE+CWR` | 1 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 765 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `202.112.237.201` -> `53` | 7 | 0.9% |
| 2 | `45.148.121.138` -> `23` | 5 | 0.7% |
| 3 | `47.100.201.178` -> `23` | 4 | 0.5% |
| 4 | `186.123.1.125` -> `1433` | 3 | 0.4% |
| 5 | `66.132.159.83` -> `53` | 3 | 0.4% |
| 6 | `66.132.195.117` -> `2000` | 3 | 0.4% |
| 7 | `35.210.9.177` -> `63256` | 3 | 0.4% |
| 8 | `62.210.114.99` -> `3389` | 3 | 0.4% |
| 9 | `93.123.109.6` -> `1723` | 2 | 0.3% |
| 10 | `202.46.28.143` -> `2222` | 2 | 0.3% |
| 11 | `181.66.253.156` -> `23` | 2 | 0.3% |
| 12 | `35.210.205.173` -> `143` | 2 | 0.3% |
| 13 | `35.210.181.94` -> `110` | 2 | 0.3% |
| 14 | `66.132.186.193` -> `8028` | 2 | 0.3% |
| 15 | `66.132.172.216` -> `8031` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-08 00:00:00:00 | 179 | 23.4% |
| 2026-11-08 01:00:00:00 | 181 | 23.7% |
| 2026-11-08 02:00:00:00 | 179 | 23.4% |
| 2026-11-08 03:00:00:00 | 181 | 23.7% |
| 2026-11-08 04:00:00:00 | 45 | 5.9% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 20 | 32.3% |
| 2 | Haidian, China | 7 | 11.3% |
| 3 | Ashburn, United States | 7 | 11.3% |
| 4 | Ann Arbor, United States | 6 | 9.7% |
| 5 | Andorra la Vella, Andorra | 5 | 8.1% |
| 6 | Shanghai, China | 4 | 6.5% |
| 7 | Hong Kong, Hong Kong | 4 | 6.5% |
| 8 | Asunción, Paraguay | 3 | 4.8% |
| 9 | San Diego, United States | 3 | 4.8% |
| 10 | Gravelines, France | 3 | 4.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `202.112.237.201` | 7 | 11.3% | China / Beijing / Haidian / China Education and Research Network | No apparent signal |
| 2 | `185.242.226.85` | 6 | 9.7% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 3 | `45.148.121.138` | 5 | 8.1% | The Netherlands / North Holland / Amsterdam / SpectraIP B.V. | No apparent signal |
| 4 | `195.178.110.92` | 5 | 8.1% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 5 | `185.242.226.72` | 5 | 8.1% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 6 | `34.230.221.101` | 4 | 6.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 7 | `86.54.31.36` | 4 | 6.5% | The Netherlands / North Holland / Amsterdam / ADSL: Circle IT Solutions Limited | No apparent signal |
| 8 | `47.100.201.178` | 4 | 6.5% | China / Shanghai / Shanghai / Aliyun Computing Co., LTD | Hosting/Cloud (alibaba) |
| 9 | `172.110.223.81` | 4 | 6.5% | Hong Kong / Kowloon / Hong Kong / Dedires LLC | No apparent signal |
| 10 | `34.197.70.90` | 3 | 4.8% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 11 | `186.123.1.125` | 3 | 4.8% | Paraguay / Asuncion / Asunción / Techtel LMDS Comunicaciones Interactivas S.A. | No apparent signal |
| 12 | `66.132.159.83` | 3 | 4.8% | United States / Michigan / Ann Arbor / Censys, Inc. | No apparent signal |
| 13 | `66.132.195.117` | 3 | 4.8% | United States / Michigan / Ann Arbor / Censys, Inc. | No apparent signal |
| 14 | `71.6.155.70` | 3 | 4.8% | United States / California / San Diego / CariNet, Inc. | No apparent signal |
| 15 | `91.231.89.69` | 3 | 4.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `34.230.221.101` | 4 | 36.4% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 2 | `47.100.201.178` | 4 | 36.4% | Hosting/Cloud (alibaba) | China / Shanghai / Shanghai / Aliyun Computing Co., LTD |
| 3 | `34.197.70.90` | 3 | 27.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
