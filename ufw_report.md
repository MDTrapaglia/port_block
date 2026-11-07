# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4338
- Unique source IPs: 2474
- Unique countries/cities (24h): 261
- Unique destination ports: 2513

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 114 | 2.6% |
| 2 | `22` | 70 | 1.6% |
| 3 | `5060` | 37 | 0.9% |
| 4 | `3389` | 36 | 0.8% |
| 5 | `1433` | 36 | 0.8% |
| 6 | `8080` | 35 | 0.8% |
| 7 | `53` | 30 | 0.7% |
| 8 | `3306` | 21 | 0.5% |
| 9 | `8443` | 21 | 0.5% |
| 10 | `8000` | 19 | 0.4% |
| 11 | `1723` | 19 | 0.4% |
| 12 | `1194` | 18 | 0.4% |
| 13 | `25` | 16 | 0.4% |
| 14 | `2000` | 15 | 0.3% |
| 15 | `161` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3970 | 91.5% |
| 2 | `UDP` | 361 | 8.3% |
| 3 | `47` | 6 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.18` | 181 | 4.2% |
| 2 | `79.124.62.10` | 15 | 0.3% |
| 3 | `91.230.168.252` | 14 | 0.3% |
| 4 | `18.221.179.104` | 14 | 0.3% |
| 5 | `148.227.74.124` | 14 | 0.3% |
| 6 | `91.231.89.0` | 13 | 0.3% |
| 7 | `91.196.152.123` | 13 | 0.3% |
| 8 | `91.231.89.10` | 13 | 0.3% |
| 9 | `91.230.168.129` | 13 | 0.3% |
| 10 | `91.230.168.142` | 13 | 0.3% |
| 11 | `91.230.168.190` | 13 | 0.3% |
| 12 | `94.183.174.99` | 13 | 0.3% |
| 13 | `91.231.89.215` | 12 | 0.3% |
| 14 | `195.184.76.116` | 12 | 0.3% |
| 15 | `18.217.208.51` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3945 | 99.4% |
| 2 | `ACK+FIN+PSH` | 15 | 0.4% |
| 3 | `ACK+PSH` | 5 | 0.1% |
| 4 | `SYN+ECE+CWR` | 3 | 0.1% |
| 5 | `ACK+FIN` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4338 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.18` -> `1337` | 10 | 0.2% |
| 2 | `216.180.246.18` -> `1200` | 9 | 0.2% |
| 3 | `216.180.246.18` -> `1409` | 9 | 0.2% |
| 4 | `45.148.121.138` -> `23` | 8 | 0.2% |
| 5 | `216.180.246.18` -> `1198` | 8 | 0.2% |
| 6 | `216.180.246.18` -> `1800` | 8 | 0.2% |
| 7 | `216.180.246.18` -> `1194` | 7 | 0.2% |
| 8 | `216.180.246.18` -> `1441` | 7 | 0.2% |
| 9 | `216.180.246.18` -> `1521` | 7 | 0.2% |
| 10 | `216.180.246.18` -> `1532` | 7 | 0.2% |
| 11 | `216.180.246.18` -> `1554` | 7 | 0.2% |
| 12 | `186.123.1.125` -> `1433` | 6 | 0.1% |
| 13 | `62.210.114.99` -> `3389` | 6 | 0.1% |
| 14 | `154.80.128.160` -> `6036` | 6 | 0.1% |
| 15 | `154.80.128.163` -> `17000` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-06 04:00:00:00 | 135 | 3.1% |
| 2026-11-06 05:00:00:00 | 187 | 4.3% |
| 2026-11-06 06:00:00:00 | 180 | 4.2% |
| 2026-11-06 07:00:00:00 | 179 | 4.1% |
| 2026-11-06 08:00:00:00 | 181 | 4.2% |
| 2026-11-06 09:00:00:00 | 178 | 4.1% |
| 2026-11-06 10:00:00:00 | 181 | 4.2% |
| 2026-11-06 11:00:00:00 | 191 | 4.4% |
| 2026-11-06 12:00:00:00 | 177 | 4.1% |
| 2026-11-06 13:00:00:00 | 182 | 4.2% |
| 2026-11-06 14:00:00:00 | 180 | 4.2% |
| 2026-11-06 15:00:00:00 | 180 | 4.2% |
| 2026-11-06 16:00:00:00 | 180 | 4.2% |
| 2026-11-06 17:00:00:00 | 180 | 4.2% |
| 2026-11-06 18:00:00:00 | 180 | 4.2% |
| 2026-11-06 19:00:00:00 | 180 | 4.2% |
| 2026-11-06 20:00:00:00 | 176 | 4.1% |
| 2026-11-06 21:00:00:00 | 184 | 4.2% |
| 2026-11-06 22:00:00:00 | 181 | 4.2% |
| 2026-11-06 23:00:00:00 | 180 | 4.2% |
| 2026-11-07 00:00:00:00 | 178 | 4.1% |
| 2026-11-07 01:00:00:00 | 181 | 4.2% |
| 2026-11-07 02:00:00:00 | 181 | 4.2% |
| 2026-11-07 03:00:00:00 | 180 | 4.2% |
| 2026-11-07 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 181 | 49.6% |
| 2 | Hillsboro, United States | 53 | 14.5% |
| 3 | Gravelines, France | 38 | 10.4% |
| 4 | Dublin, United States | 26 | 7.1% |
| 5 | Victoria, Seychelles | 15 | 4.1% |
| 6 | Buenos Aires, Argentina | 14 | 3.8% |
| 7 | Roubaix, France | 13 | 3.6% |
| 8 | Hauzenberg, Germany | 13 | 3.6% |
| 9 | Warrenton, United States | 12 | 3.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.18` | 181 | 49.6% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `79.124.62.10` | 15 | 4.1% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 3 | `91.230.168.252` | 14 | 3.8% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 4 | `18.221.179.104` | 14 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 5 | `148.227.74.124` | 14 | 3.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Starlink Argentina SRL | No apparent signal |
| 6 | `91.231.89.0` | 13 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `91.196.152.123` | 13 | 3.6% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 8 | `91.231.89.10` | 13 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `91.230.168.129` | 13 | 3.6% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 10 | `91.230.168.142` | 13 | 3.6% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 11 | `91.230.168.190` | 13 | 3.6% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 12 | `94.183.174.99` | 13 | 3.6% | Germany / Bavaria / Hauzenberg / Pfcloud UG | No apparent signal |
| 13 | `91.231.89.215` | 12 | 3.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `195.184.76.116` | 12 | 3.3% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 15 | `18.217.208.51` | 12 | 3.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.18` | 181 | 87.4% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `18.221.179.104` | 14 | 6.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.217.208.51` | 12 | 5.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
