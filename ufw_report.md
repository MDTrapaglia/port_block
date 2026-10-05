# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4314
- Unique source IPs: 2571
- Unique countries/cities (24h): 301
- Unique destination ports: 2429

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 134 | 3.1% |
| 2 | `22` | 90 | 2.1% |
| 3 | `8080` | 37 | 0.9% |
| 4 | `5060` | 37 | 0.9% |
| 5 | `8443` | 34 | 0.8% |
| 6 | `3389` | 29 | 0.7% |
| 7 | `53` | 29 | 0.7% |
| 8 | `2222` | 25 | 0.6% |
| 9 | `8081` | 25 | 0.6% |
| 10 | `1433` | 24 | 0.6% |
| 11 | `161` | 23 | 0.5% |
| 12 | `3306` | 22 | 0.5% |
| 13 | `21` | 22 | 0.5% |
| 14 | `8000` | 20 | 0.5% |
| 15 | `123` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3861 | 89.5% |
| 2 | `UDP` | 447 | 10.4% |
| 3 | `47` | 5 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `80.94.95.109` | 140 | 3.2% |
| 2 | `195.178.110.204` | 19 | 0.4% |
| 3 | `45.198.224.125` | 17 | 0.4% |
| 4 | `37.77.150.67` | 16 | 0.4% |
| 5 | `195.184.76.62` | 15 | 0.3% |
| 6 | `79.124.40.162` | 14 | 0.3% |
| 7 | `18.217.208.51` | 14 | 0.3% |
| 8 | `85.217.140.3` | 14 | 0.3% |
| 9 | `85.217.140.1` | 13 | 0.3% |
| 10 | `18.221.179.104` | 13 | 0.3% |
| 11 | `3.151.116.231` | 13 | 0.3% |
| 12 | `18.190.15.50` | 13 | 0.3% |
| 13 | `151.243.11.230` | 13 | 0.3% |
| 14 | `85.217.149.37` | 13 | 0.3% |
| 15 | `85.217.140.24` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3831 | 99.2% |
| 2 | `ACK+PSH` | 15 | 0.4% |
| 3 | `SYN+ECE+CWR` | 13 | 0.3% |
| 4 | `ACK` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4314 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.198.224.124` -> `81` | 7 | 0.2% |
| 2 | `201.20.85.122` -> `6379` | 7 | 0.2% |
| 3 | `91.224.92.28` -> `34567` | 7 | 0.2% |
| 4 | `186.123.1.125` -> `1433` | 6 | 0.1% |
| 5 | `45.198.224.125` -> `8080` | 6 | 0.1% |
| 6 | `45.198.224.125` -> `8081` | 6 | 0.1% |
| 7 | `167.94.146.63` -> `7070` | 6 | 0.1% |
| 8 | `45.205.1.163` -> `17000` | 6 | 0.1% |
| 9 | `66.132.195.120` -> `21` | 6 | 0.1% |
| 10 | `45.198.224.125` -> `9090` | 5 | 0.1% |
| 11 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 12 | `66.132.195.101` -> `8443` | 5 | 0.1% |
| 13 | `216.180.246.11` -> `10398` | 5 | 0.1% |
| 14 | `130.12.180.65` -> `5555` | 4 | 0.1% |
| 15 | `57.144.22.196` -> `24899` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-04 04:00:00:00 | 128 | 3.0% |
| 2026-10-04 05:00:00:00 | 186 | 4.3% |
| 2026-10-04 06:00:00:00 | 178 | 4.1% |
| 2026-10-04 07:00:00:00 | 182 | 4.2% |
| 2026-10-04 08:00:00:00 | 180 | 4.2% |
| 2026-10-04 09:00:00:00 | 180 | 4.2% |
| 2026-10-04 10:00:00:00 | 179 | 4.1% |
| 2026-10-04 11:00:00:00 | 179 | 4.1% |
| 2026-10-04 12:00:00:00 | 181 | 4.2% |
| 2026-10-04 13:00:00:00 | 180 | 4.2% |
| 2026-10-04 14:00:00:00 | 178 | 4.1% |
| 2026-10-04 15:00:00:00 | 181 | 4.2% |
| 2026-10-04 16:00:00:00 | 181 | 4.2% |
| 2026-10-04 17:00:00:00 | 180 | 4.2% |
| 2026-10-04 18:00:00:00 | 179 | 4.1% |
| 2026-10-04 19:00:00:00 | 178 | 4.1% |
| 2026-10-04 20:00:00:00 | 182 | 4.2% |
| 2026-10-04 21:00:00:00 | 180 | 4.2% |
| 2026-10-04 22:00:00:00 | 180 | 4.2% |
| 2026-10-04 23:00:00:00 | 180 | 4.2% |
| 2026-10-05 00:00:00:00 | 180 | 4.2% |
| 2026-10-05 01:00:00:00 | 179 | 4.1% |
| 2026-10-05 02:00:00:00 | 177 | 4.1% |
| 2026-10-05 03:00:00:00 | 184 | 4.3% |
| 2026-10-05 04:00:00:00 | 42 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Budapest, Hungary | 140 | 41.3% |
| 2 | Dublin, United States | 53 | 15.6% |
| 3 | Gravelines, France | 26 | 7.7% |
| 4 | Andorra la Vella, Andorra | 19 | 5.6% |
| 5 | Stockholm, Sweden | 17 | 5.0% |
| 6 | Zelenograd, Russia | 16 | 4.7% |
| 7 | Warrenton, United States | 15 | 4.4% |
| 8 | Sopot, Bulgaria | 14 | 4.1% |
| 9 | Paris, France | 13 | 3.8% |
| 10 | Frankfurt am Main, Germany | 13 | 3.8% |
| 11 | Beauharnois, Canada | 13 | 3.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `80.94.95.109` | 140 | 41.3% | Hungary / Budapest / Budapest / Unmanaged LTD | No apparent signal |
| 2 | `195.178.110.204` | 19 | 5.6% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 3 | `45.198.224.125` | 17 | 5.0% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 4 | `37.77.150.67` | 16 | 4.7% | Russia / Moscow / Zelenograd / LLC Baxet | VPN/Proxy suspected (proton) |
| 5 | `195.184.76.62` | 15 | 4.4% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 6 | `79.124.40.162` | 14 | 4.1% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 7 | `18.217.208.51` | 14 | 4.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `85.217.140.3` | 14 | 4.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.1` | 13 | 3.8% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 10 | `18.221.179.104` | 13 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `3.151.116.231` | 13 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `18.190.15.50` | 13 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `151.243.11.230` | 13 | 3.8% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 14 | `85.217.149.37` | 13 | 3.8% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 15 | `85.217.140.24` | 12 | 3.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `37.77.150.67` | 16 | 23.2% | VPN/Proxy suspected (proton) | Russia / Moscow / Zelenograd / LLC Baxet |
| 2 | `18.217.208.51` | 14 | 20.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.221.179.104` | 13 | 18.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `3.151.116.231` | 13 | 18.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.190.15.50` | 13 | 18.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
