# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4371
- Unique source IPs: 2503
- Unique countries/cities (24h): 284
- Unique destination ports: 2528

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 79 | 1.8% |
| 2 | `22` | 70 | 1.6% |
| 3 | `5060` | 43 | 1.0% |
| 4 | `8080` | 42 | 1.0% |
| 5 | `3389` | 36 | 0.8% |
| 6 | `8443` | 35 | 0.8% |
| 7 | `53` | 31 | 0.7% |
| 8 | `7680` | 27 | 0.6% |
| 9 | `8081` | 22 | 0.5% |
| 10 | `2222` | 21 | 0.5% |
| 11 | `3306` | 20 | 0.5% |
| 12 | `1723` | 20 | 0.5% |
| 13 | `8088` | 20 | 0.5% |
| 14 | `9200` | 18 | 0.4% |
| 15 | `8888` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3943 | 90.2% |
| 2 | `UDP` | 414 | 9.5% |
| 3 | `47` | 8 | 0.2% |
| 4 | `132` | 4 | 0.1% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `164.52.24.179` | 46 | 1.1% |
| 2 | `24.7.116.142` | 20 | 0.5% |
| 3 | `45.198.224.125` | 17 | 0.4% |
| 4 | `79.124.40.186` | 16 | 0.4% |
| 5 | `91.231.89.215` | 14 | 0.3% |
| 6 | `100.50.17.159` | 13 | 0.3% |
| 7 | `18.119.209.50` | 13 | 0.3% |
| 8 | `91.231.89.72` | 13 | 0.3% |
| 9 | `91.231.89.10` | 12 | 0.3% |
| 10 | `91.231.89.238` | 12 | 0.3% |
| 11 | `91.231.89.104` | 12 | 0.3% |
| 12 | `91.231.89.130` | 12 | 0.3% |
| 13 | `91.231.89.251` | 12 | 0.3% |
| 14 | `195.184.76.71` | 11 | 0.3% |
| 15 | `100.49.117.77` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3879 | 98.4% |
| 2 | `ACK+FIN+PSH` | 48 | 1.2% |
| 3 | `ACK+PSH` | 12 | 0.3% |
| 4 | `ACK+FIN` | 3 | 0.1% |
| 5 | `SYN+ECE+CWR` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4371 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `24.7.116.142` -> `7680` | 20 | 0.5% |
| 2 | `151.101.218.13` -> `59083` | 7 | 0.2% |
| 3 | `45.198.224.125` -> `8081` | 6 | 0.1% |
| 4 | `186.123.1.125` -> `1433` | 6 | 0.1% |
| 5 | `93.123.109.6` -> `1723` | 6 | 0.1% |
| 6 | `170.51.241.170` -> `59531` | 6 | 0.1% |
| 7 | `45.198.224.125` -> `2087` | 5 | 0.1% |
| 8 | `135.148.85.221` -> `5060` | 5 | 0.1% |
| 9 | `164.52.24.179` -> `8443` | 5 | 0.1% |
| 10 | `164.52.24.179` -> `90` | 5 | 0.1% |
| 11 | `151.101.218.73` -> `59105` | 5 | 0.1% |
| 12 | `154.80.128.231` -> `53` | 4 | 0.1% |
| 13 | `178.20.210.152` -> `1723` | 4 | 0.1% |
| 14 | `64.227.159.78` -> `23` | 4 | 0.1% |
| 15 | `196.244.192.202` -> `22` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-27 04:00:00:00 | 135 | 3.1% |
| 2026-11-27 05:00:00:00 | 179 | 4.1% |
| 2026-11-27 06:00:00:00 | 180 | 4.1% |
| 2026-11-27 07:00:00:00 | 181 | 4.1% |
| 2026-11-27 08:00:00:00 | 180 | 4.1% |
| 2026-11-27 09:00:00:00 | 179 | 4.1% |
| 2026-11-27 10:00:00:00 | 180 | 4.1% |
| 2026-11-27 11:00:00:00 | 180 | 4.1% |
| 2026-11-27 12:00:00:00 | 180 | 4.1% |
| 2026-11-27 13:00:00:00 | 180 | 4.1% |
| 2026-11-27 14:00:00:00 | 180 | 4.1% |
| 2026-11-27 15:00:00:00 | 180 | 4.1% |
| 2026-11-27 16:00:00:00 | 181 | 4.1% |
| 2026-11-27 17:00:00:00 | 180 | 4.1% |
| 2026-11-27 18:00:00:00 | 180 | 4.1% |
| 2026-11-27 19:00:00:00 | 180 | 4.1% |
| 2026-11-27 20:00:00:00 | 180 | 4.1% |
| 2026-11-27 21:00:00:00 | 179 | 4.1% |
| 2026-11-27 22:00:00:00 | 180 | 4.1% |
| 2026-11-27 23:00:00:00 | 190 | 4.3% |
| 2026-11-28 00:00:00:00 | 197 | 4.5% |
| 2026-11-28 01:00:00:00 | 203 | 4.6% |
| 2026-11-28 02:00:00:00 | 180 | 4.1% |
| 2026-11-28 03:00:00:00 | 181 | 4.1% |
| 2026-11-28 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 87 | 37.2% |
| 2 | Osaka, Japan | 46 | 19.7% |
| 3 | Ashburn, United States | 24 | 10.3% |
| 4 | Mountain View, United States | 20 | 8.5% |
| 5 | Stockholm, Sweden | 17 | 7.3% |
| 6 | Sopot, Bulgaria | 16 | 6.8% |
| 7 | Dublin, United States | 13 | 5.6% |
| 8 | Warrenton, United States | 11 | 4.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `164.52.24.179` | 46 | 19.7% | Japan / Osaka / Osaka / Capitalonline Data Service (HK) Co | No apparent signal |
| 2 | `24.7.116.142` | 20 | 8.5% | United States / California / Mountain View / Comcast Cable Communications | No apparent signal |
| 3 | `45.198.224.125` | 17 | 7.3% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 4 | `79.124.40.186` | 16 | 6.8% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 5 | `91.231.89.215` | 14 | 6.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 6 | `100.50.17.159` | 13 | 5.6% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 7 | `18.119.209.50` | 13 | 5.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `91.231.89.72` | 13 | 5.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `91.231.89.10` | 12 | 5.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `91.231.89.238` | 12 | 5.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 11 | `91.231.89.104` | 12 | 5.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.130` | 12 | 5.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.231.89.251` | 12 | 5.1% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `195.184.76.71` | 11 | 4.7% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 15 | `100.49.117.77` | 11 | 4.7% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `100.50.17.159` | 13 | 35.1% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 2 | `18.119.209.50` | 13 | 35.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `100.49.117.77` | 11 | 29.7% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
