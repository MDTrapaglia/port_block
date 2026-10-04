# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 616
- Unique source IPs: 438
- Unique countries/cities (24h): 100
- Unique destination ports: 484

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 17 | 2.8% |
| 2 | `22` | 7 | 1.1% |
| 3 | `31460` | 7 | 1.1% |
| 4 | `31324` | 6 | 1.0% |
| 5 | `5555` | 6 | 1.0% |
| 6 | `31412` | 6 | 1.0% |
| 7 | `32332` | 6 | 1.0% |
| 8 | `9000` | 5 | 0.8% |
| 9 | `5060` | 4 | 0.6% |
| 10 | `8080` | 4 | 0.6% |
| 11 | `1194` | 4 | 0.6% |
| 12 | `8443` | 4 | 0.6% |
| 13 | `6379` | 4 | 0.6% |
| 14 | `3389` | 4 | 0.6% |
| 15 | `6036` | 4 | 0.6% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 572 | 92.9% |
| 2 | `UDP` | 44 | 7.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `5.253.38.204` | 81 | 13.1% |
| 2 | `216.180.246.234` | 33 | 5.4% |
| 3 | `185.242.226.8` | 6 | 1.0% |
| 4 | `37.77.150.67` | 5 | 0.8% |
| 5 | `85.217.140.2` | 3 | 0.5% |
| 6 | `193.163.125.193` | 3 | 0.5% |
| 7 | `195.184.76.198` | 3 | 0.5% |
| 8 | `195.184.76.180` | 3 | 0.5% |
| 9 | `195.184.76.185` | 3 | 0.5% |
| 10 | `85.217.140.3` | 3 | 0.5% |
| 11 | `85.217.149.37` | 3 | 0.5% |
| 12 | `100.49.117.77` | 3 | 0.5% |
| 13 | `31.128.251.105` | 3 | 0.5% |
| 14 | `85.217.140.18` | 3 | 0.5% |
| 15 | `45.194.92.102` | 2 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 565 | 98.8% |
| 2 | `SYN+ECE+CWR` | 7 | 1.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 616 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.234` -> `31460` | 7 | 1.1% |
| 2 | `216.180.246.234` -> `31324` | 6 | 1.0% |
| 3 | `216.180.246.234` -> `31412` | 6 | 1.0% |
| 4 | `216.180.246.234` -> `32332` | 6 | 1.0% |
| 5 | `216.180.246.234` -> `31423` | 4 | 0.6% |
| 6 | `216.180.246.234` -> `32365` | 3 | 0.5% |
| 7 | `37.77.150.67` -> `14333` | 2 | 0.3% |
| 8 | `31.128.251.105` -> `23` | 2 | 0.3% |
| 9 | `94.154.43.163` -> `1880` | 2 | 0.3% |
| 10 | `153.80.249.226` -> `23` | 2 | 0.3% |
| 11 | `186.123.1.125` -> `1433` | 2 | 0.3% |
| 12 | `185.218.108.97` -> `37777` | 2 | 0.3% |
| 13 | `178.93.201.147` -> `9527` | 2 | 0.3% |
| 14 | `37.77.150.67` -> `14337` | 2 | 0.3% |
| 15 | `45.194.92.102` -> `17000` | 1 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-04 00:00:00:00 | 30 | 4.9% |
| 2026-10-04 01:00:00:00 | 179 | 29.1% |
| 2026-10-04 02:00:00:00 | 181 | 29.4% |
| 2026-10-04 03:00:00:00 | 175 | 28.4% |
| 2026-10-04 04:00:00:00 | 51 | 8.3% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Los Angeles, United States | 81 | 51.6% |
| 2 | Massy, France | 33 | 21.0% |
| 3 | Gravelines, France | 9 | 5.7% |
| 4 | Warrenton, United States | 9 | 5.7% |
| 5 | Amsterdam, The Netherlands | 6 | 3.8% |
| 6 | Zelenograd, Russia | 5 | 3.2% |
| 7 | Leeds, United Kingdom | 3 | 1.9% |
| 8 | Beauharnois, Canada | 3 | 1.9% |
| 9 | Ashburn, United States | 3 | 1.9% |
| 10 | Berezne, Ukraine | 3 | 1.9% |
| 11 | Toronto, Canada | 2 | 1.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `5.253.38.204` | 81 | 51.6% | United States / California / Los Angeles / Securewan | No apparent signal |
| 2 | `216.180.246.234` | 33 | 21.0% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 3 | `185.242.226.8` | 6 | 3.8% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 4 | `37.77.150.67` | 5 | 3.2% | Russia / Moscow / Zelenograd / LLC Baxet | VPN/Proxy suspected (proton) |
| 5 | `85.217.140.2` | 3 | 1.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `193.163.125.193` | 3 | 1.9% | United Kingdom / England / Leeds / Constantine Cybersecurity LTD | No apparent signal |
| 7 | `195.184.76.198` | 3 | 1.9% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 8 | `195.184.76.180` | 3 | 1.9% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 9 | `195.184.76.185` | 3 | 1.9% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 10 | `85.217.140.3` | 3 | 1.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.149.37` | 3 | 1.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 12 | `100.49.117.77` | 3 | 1.9% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `31.128.251.105` | 3 | 1.9% | Ukraine / Rivne Oblast / Berezne / "Merlin-Telekom" LLC | No apparent signal |
| 14 | `85.217.140.18` | 3 | 1.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `45.194.92.102` | 2 | 1.3% | Canada / Ontario / Toronto / East Coast Host | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.234` | 33 | 80.5% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `37.77.150.67` | 5 | 12.2% | VPN/Proxy suspected (proton) | Russia / Moscow / Zelenograd / LLC Baxet |
| 3 | `100.49.117.77` | 3 | 7.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
