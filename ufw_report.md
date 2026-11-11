# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4352
- Unique source IPs: 2499
- Unique countries/cities (24h): 289
- Unique destination ports: 2529

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 91 | 2.1% |
| 2 | `22` | 77 | 1.8% |
| 3 | `3389` | 52 | 1.2% |
| 4 | `5060` | 52 | 1.2% |
| 5 | `8080` | 45 | 1.0% |
| 6 | `53` | 27 | 0.6% |
| 7 | `3306` | 22 | 0.5% |
| 8 | `1433` | 22 | 0.5% |
| 9 | `9034` | 22 | 0.5% |
| 10 | `161` | 21 | 0.5% |
| 11 | `8443` | 21 | 0.5% |
| 12 | `1723` | 19 | 0.4% |
| 13 | `389` | 19 | 0.4% |
| 14 | `5555` | 18 | 0.4% |
| 15 | `8000` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3939 | 90.5% |
| 2 | `UDP` | 403 | 9.3% |
| 3 | `47` | 9 | 0.2% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `160.119.76.165` | 27 | 0.6% |
| 2 | `195.178.110.89` | 17 | 0.4% |
| 3 | `79.124.49.146` | 17 | 0.4% |
| 4 | `45.198.224.125` | 16 | 0.4% |
| 5 | `18.119.209.50` | 15 | 0.3% |
| 6 | `195.184.76.20` | 15 | 0.3% |
| 7 | `91.196.152.35` | 14 | 0.3% |
| 8 | `195.184.76.71` | 14 | 0.3% |
| 9 | `172.110.223.182` | 14 | 0.3% |
| 10 | `91.231.89.10` | 13 | 0.3% |
| 11 | `91.231.89.238` | 13 | 0.3% |
| 12 | `3.131.24.55` | 13 | 0.3% |
| 13 | `18.190.15.50` | 13 | 0.3% |
| 14 | `91.231.89.72` | 13 | 0.3% |
| 15 | `91.230.168.142` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3879 | 98.5% |
| 2 | `ACK+FIN+PSH` | 23 | 0.6% |
| 3 | `ACK+PSH` | 17 | 0.4% |
| 4 | `ACK+FIN` | 9 | 0.2% |
| 5 | `ACK` | 7 | 0.2% |
| 6 | `SYN+ECE+CWR` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4352 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `172.110.223.182` -> `5060` | 14 | 0.3% |
| 2 | `62.210.114.99` -> `3389` | 10 | 0.2% |
| 3 | `154.80.128.160` -> `6036` | 9 | 0.2% |
| 4 | `45.198.224.125` -> `8080` | 8 | 0.2% |
| 5 | `93.123.109.6` -> `1723` | 7 | 0.2% |
| 6 | `154.80.128.163` -> `17000` | 7 | 0.2% |
| 7 | `91.224.92.45` -> `34567` | 5 | 0.1% |
| 8 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 9 | `45.198.224.125` -> `9090` | 5 | 0.1% |
| 10 | `85.234.131.81` -> `23` | 5 | 0.1% |
| 11 | `118.212.132.226` -> `22` | 4 | 0.1% |
| 12 | `154.80.128.121` -> `5555` | 4 | 0.1% |
| 13 | `186.123.128.53` -> `1433` | 4 | 0.1% |
| 14 | `186.123.1.125` -> `1433` | 4 | 0.1% |
| 15 | `154.80.128.124` -> `5555` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-10 04:00:00:00 | 135 | 3.1% |
| 2026-11-10 05:00:00:00 | 178 | 4.1% |
| 2026-11-10 06:00:00:00 | 181 | 4.2% |
| 2026-11-10 07:00:00:00 | 177 | 4.1% |
| 2026-11-10 08:00:00:00 | 183 | 4.2% |
| 2026-11-10 09:00:00:00 | 178 | 4.1% |
| 2026-11-10 10:00:00:00 | 183 | 4.2% |
| 2026-11-10 11:00:00:00 | 178 | 4.1% |
| 2026-11-10 12:00:00:00 | 179 | 4.1% |
| 2026-11-10 13:00:00:00 | 182 | 4.2% |
| 2026-11-10 14:00:00:00 | 180 | 4.1% |
| 2026-11-10 15:00:00:00 | 181 | 4.2% |
| 2026-11-10 16:00:00:00 | 179 | 4.1% |
| 2026-11-10 17:00:00:00 | 190 | 4.4% |
| 2026-11-10 18:00:00:00 | 181 | 4.2% |
| 2026-11-10 19:00:00:00 | 179 | 4.1% |
| 2026-11-10 20:00:00:00 | 180 | 4.1% |
| 2026-11-10 21:00:00:00 | 190 | 4.4% |
| 2026-11-10 22:00:00:00 | 182 | 4.2% |
| 2026-11-10 23:00:00:00 | 178 | 4.1% |
| 2026-11-11 00:00:00:00 | 180 | 4.1% |
| 2026-11-11 01:00:00:00 | 181 | 4.2% |
| 2026-11-11 02:00:00:00 | 191 | 4.4% |
| 2026-11-11 03:00:00:00 | 181 | 4.2% |
| 2026-11-11 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dublin, United States | 41 | 18.1% |
| 2 | Gravelines, France | 39 | 17.3% |
| 3 | Warrenton, United States | 29 | 12.8% |
| 4 | Amsterdam, The Netherlands | 27 | 11.9% |
| 5 | Andorra la Vella, Andorra | 17 | 7.5% |
| 6 | Sopot, Bulgaria | 17 | 7.5% |
| 7 | Stockholm, Sweden | 16 | 7.1% |
| 8 | Roubaix, France | 14 | 6.2% |
| 9 | Newark, United States | 14 | 6.2% |
| 10 | Hillsboro, United States | 12 | 5.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `160.119.76.165` | 27 | 11.9% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |
| 2 | `195.178.110.89` | 17 | 7.5% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 3 | `79.124.49.146` | 17 | 7.5% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 4 | `45.198.224.125` | 16 | 7.1% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 5 | `18.119.209.50` | 15 | 6.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 6 | `195.184.76.20` | 15 | 6.6% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 7 | `91.196.152.35` | 14 | 6.2% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 8 | `195.184.76.71` | 14 | 6.2% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 9 | `172.110.223.182` | 14 | 6.2% | United States / New Jersey / Newark / Dedires LLC | No apparent signal |
| 10 | `91.231.89.10` | 13 | 5.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 11 | `91.231.89.238` | 13 | 5.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `3.131.24.55` | 13 | 5.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `18.190.15.50` | 13 | 5.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `91.231.89.72` | 13 | 5.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `91.230.168.142` | 12 | 5.3% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `18.119.209.50` | 15 | 36.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 2 | `3.131.24.55` | 13 | 31.7% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.190.15.50` | 13 | 31.7% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
