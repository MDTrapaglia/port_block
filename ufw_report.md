# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4331
- Unique source IPs: 2495
- Unique countries/cities (24h): 277
- Unique destination ports: 2570

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 108 | 2.5% |
| 2 | `22` | 96 | 2.2% |
| 3 | `3389` | 43 | 1.0% |
| 4 | `8080` | 40 | 0.9% |
| 5 | `5060` | 33 | 0.8% |
| 6 | `53` | 29 | 0.7% |
| 7 | `1433` | 25 | 0.6% |
| 8 | `8443` | 23 | 0.5% |
| 9 | `8081` | 20 | 0.5% |
| 10 | `21` | 17 | 0.4% |
| 11 | `1723` | 17 | 0.4% |
| 12 | `389` | 16 | 0.4% |
| 13 | `3306` | 16 | 0.4% |
| 14 | `3128` | 15 | 0.3% |
| 15 | `5432` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3958 | 91.4% |
| 2 | `UDP` | 369 | 8.5% |
| 3 | `47` | 3 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `79.124.49.146` | 24 | 0.6% |
| 2 | `45.198.224.31` | 21 | 0.5% |
| 3 | `151.101.216.159` | 20 | 0.5% |
| 4 | `3.151.116.231` | 16 | 0.4% |
| 5 | `195.184.76.71` | 16 | 0.4% |
| 6 | `91.231.89.104` | 14 | 0.3% |
| 7 | `91.231.89.215` | 14 | 0.3% |
| 8 | `91.196.152.35` | 14 | 0.3% |
| 9 | `91.230.168.142` | 13 | 0.3% |
| 10 | `18.119.209.50` | 13 | 0.3% |
| 11 | `91.231.89.150` | 13 | 0.3% |
| 12 | `91.231.89.0` | 12 | 0.3% |
| 13 | `91.231.89.87` | 12 | 0.3% |
| 14 | `91.231.89.205` | 12 | 0.3% |
| 15 | `18.190.15.50` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3903 | 98.6% |
| 2 | `ACK+PSH` | 36 | 0.9% |
| 3 | `ACK+FIN+PSH` | 15 | 0.4% |
| 4 | `SYN+ECE+CWR` | 3 | 0.1% |
| 5 | `ACK+FIN` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4331 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `118.212.132.226` -> `22` | 8 | 0.2% |
| 2 | `62.210.114.99` -> `3389` | 8 | 0.2% |
| 3 | `93.157.249.218` -> `23` | 7 | 0.2% |
| 4 | `93.123.109.6` -> `1723` | 7 | 0.2% |
| 5 | `151.101.216.159` -> `39192` | 7 | 0.2% |
| 6 | `177.112.215.133` -> `3128` | 6 | 0.1% |
| 7 | `172.110.223.182` -> `5060` | 6 | 0.1% |
| 8 | `66.132.172.201` -> `22` | 6 | 0.1% |
| 9 | `45.198.224.125` -> `8080` | 5 | 0.1% |
| 10 | `151.101.216.159` -> `39190` | 5 | 0.1% |
| 11 | `178.20.210.151` -> `22` | 5 | 0.1% |
| 12 | `151.101.216.159` -> `46168` | 5 | 0.1% |
| 13 | `45.198.224.125` -> `9090` | 4 | 0.1% |
| 14 | `104.36.194.66` -> `50352` | 4 | 0.1% |
| 15 | `186.122.88.103` -> `7070` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-12 04:00:00:00 | 133 | 3.1% |
| 2026-11-12 05:00:00:00 | 180 | 4.2% |
| 2026-11-12 06:00:00:00 | 180 | 4.2% |
| 2026-11-12 07:00:00:00 | 180 | 4.2% |
| 2026-11-12 08:00:00:00 | 189 | 4.4% |
| 2026-11-12 09:00:00:00 | 180 | 4.2% |
| 2026-11-12 10:00:00:00 | 178 | 4.1% |
| 2026-11-12 11:00:00:00 | 182 | 4.2% |
| 2026-11-12 12:00:00:00 | 179 | 4.1% |
| 2026-11-12 13:00:00:00 | 181 | 4.2% |
| 2026-11-12 14:00:00:00 | 179 | 4.1% |
| 2026-11-12 15:00:00:00 | 181 | 4.2% |
| 2026-11-12 16:00:00:00 | 180 | 4.2% |
| 2026-11-12 17:00:00:00 | 180 | 4.2% |
| 2026-11-12 18:00:00:00 | 179 | 4.1% |
| 2026-11-12 19:00:00:00 | 188 | 4.3% |
| 2026-11-12 20:00:00:00 | 180 | 4.2% |
| 2026-11-12 21:00:00:00 | 175 | 4.0% |
| 2026-11-12 22:00:00:00 | 180 | 4.2% |
| 2026-11-12 23:00:00:00 | 180 | 4.2% |
| 2026-11-13 00:00:00:00 | 180 | 4.2% |
| 2026-11-13 01:00:00:00 | 180 | 4.2% |
| 2026-11-13 02:00:00:00 | 177 | 4.1% |
| 2026-11-13 03:00:00:00 | 183 | 4.2% |
| 2026-11-13 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 77 | 34.1% |
| 2 | Dublin, United States | 41 | 18.1% |
| 3 | Sopot, Bulgaria | 24 | 10.6% |
| 4 | Stockholm, Sweden | 21 | 9.3% |
| 5 | Buenos Aires, Argentina | 20 | 8.8% |
| 6 | Warrenton, United States | 16 | 7.1% |
| 7 | Roubaix, France | 14 | 6.2% |
| 8 | Hillsboro, United States | 13 | 5.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `79.124.49.146` | 24 | 10.6% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 2 | `45.198.224.31` | 21 | 9.3% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 3 | `151.101.216.159` | 20 | 8.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `3.151.116.231` | 16 | 7.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 5 | `195.184.76.71` | 16 | 7.1% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 6 | `91.231.89.104` | 14 | 6.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `91.231.89.215` | 14 | 6.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 8 | `91.196.152.35` | 14 | 6.2% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 9 | `91.230.168.142` | 13 | 5.8% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 10 | `18.119.209.50` | 13 | 5.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `91.231.89.150` | 13 | 5.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.0` | 12 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.231.89.87` | 12 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.231.89.205` | 12 | 5.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `18.190.15.50` | 12 | 5.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.216.159` | 20 | 32.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `3.151.116.231` | 16 | 26.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.119.209.50` | 13 | 21.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `18.190.15.50` | 12 | 19.7% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
