# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4373
- Unique source IPs: 2204
- Unique countries/cities (24h): 271
- Unique destination ports: 2471

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 153 | 3.5% |
| 2 | `22` | 79 | 1.8% |
| 3 | `5060` | 51 | 1.2% |
| 4 | `21` | 49 | 1.1% |
| 5 | `8080` | 42 | 1.0% |
| 6 | `53` | 34 | 0.8% |
| 7 | `3389` | 27 | 0.6% |
| 8 | `3306` | 25 | 0.6% |
| 9 | `1433` | 23 | 0.5% |
| 10 | `8081` | 20 | 0.5% |
| 11 | `1723` | 19 | 0.4% |
| 12 | `8000` | 18 | 0.4% |
| 13 | `8443` | 17 | 0.4% |
| 14 | `81` | 17 | 0.4% |
| 15 | `9200` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4000 | 91.5% |
| 2 | `UDP` | 364 | 8.3% |
| 3 | `47` | 8 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `193.46.255.141` | 552 | 12.6% |
| 2 | `216.180.246.60` | 37 | 0.8% |
| 3 | `151.101.218.13` | 20 | 0.5% |
| 4 | `45.198.224.125` | 16 | 0.4% |
| 5 | `118.123.1.37` | 14 | 0.3% |
| 6 | `91.231.89.224` | 14 | 0.3% |
| 7 | `91.196.152.222` | 14 | 0.3% |
| 8 | `91.231.89.251` | 13 | 0.3% |
| 9 | `195.184.76.20` | 13 | 0.3% |
| 10 | `91.230.168.142` | 13 | 0.3% |
| 11 | `79.124.49.62` | 13 | 0.3% |
| 12 | `18.190.15.50` | 12 | 0.3% |
| 13 | `91.231.89.72` | 12 | 0.3% |
| 14 | `34.228.104.231` | 12 | 0.3% |
| 15 | `195.184.76.180` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3908 | 97.7% |
| 2 | `ACK+FIN+PSH` | 49 | 1.2% |
| 3 | `ACK+PSH` | 32 | 0.8% |
| 4 | `ACK` | 4 | 0.1% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |
| 6 | `ACK+FIN` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4373 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `72.46.87.211` -> `23` | 11 | 0.3% |
| 2 | `154.16.139.185` -> `37777` | 10 | 0.2% |
| 3 | `45.198.224.125` -> `9090` | 8 | 0.2% |
| 4 | `154.80.128.160` -> `6036` | 8 | 0.2% |
| 5 | `216.180.246.60` -> `22` | 8 | 0.2% |
| 6 | `54.203.147.253` -> `56945` | 8 | 0.2% |
| 7 | `185.243.5.118` -> `5060` | 7 | 0.2% |
| 8 | `172.110.223.188` -> `5060` | 6 | 0.1% |
| 9 | `151.101.218.13` -> `60302` | 6 | 0.1% |
| 10 | `203.151.27.181` -> `23` | 6 | 0.1% |
| 11 | `62.210.114.99` -> `3389` | 6 | 0.1% |
| 12 | `216.180.246.60` -> `85` | 6 | 0.1% |
| 13 | `216.180.246.60` -> `554` | 6 | 0.1% |
| 14 | `151.243.11.230` -> `1900` | 5 | 0.1% |
| 15 | `151.101.218.13` -> `62258` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-04 04:00:00:00 | 135 | 3.1% |
| 2026-11-04 05:00:00:00 | 180 | 4.1% |
| 2026-11-04 06:00:00:00 | 180 | 4.1% |
| 2026-11-04 07:00:00:00 | 181 | 4.1% |
| 2026-11-04 08:00:00:00 | 180 | 4.1% |
| 2026-11-04 09:00:00:00 | 178 | 4.1% |
| 2026-11-04 10:00:00:00 | 182 | 4.2% |
| 2026-11-04 11:00:00:00 | 191 | 4.4% |
| 2026-11-04 12:00:00:00 | 199 | 4.6% |
| 2026-11-04 13:00:00:00 | 181 | 4.1% |
| 2026-11-04 14:00:00:00 | 188 | 4.3% |
| 2026-11-04 15:00:00:00 | 181 | 4.1% |
| 2026-11-04 16:00:00:00 | 180 | 4.1% |
| 2026-11-04 17:00:00:00 | 179 | 4.1% |
| 2026-11-04 18:00:00:00 | 178 | 4.1% |
| 2026-11-04 19:00:00:00 | 182 | 4.2% |
| 2026-11-04 20:00:00:00 | 180 | 4.1% |
| 2026-11-04 21:00:00:00 | 180 | 4.1% |
| 2026-11-04 22:00:00:00 | 191 | 4.4% |
| 2026-11-04 23:00:00:00 | 179 | 4.1% |
| 2026-11-05 00:00:00:00 | 180 | 4.1% |
| 2026-11-05 01:00:00:00 | 182 | 4.2% |
| 2026-11-05 02:00:00:00 | 179 | 4.1% |
| 2026-11-05 03:00:00:00 | 181 | 4.1% |
| 2026-11-05 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Rushden, United Kingdom | 552 | 72.0% |
| 2 | Gravelines, France | 39 | 5.1% |
| 3 | Massy, France | 37 | 4.8% |
| 4 | Warrenton, United States | 25 | 3.3% |
| 5 | Buenos Aires, Argentina | 20 | 2.6% |
| 6 | Stockholm, Sweden | 16 | 2.1% |
| 7 | Chengdu, China | 14 | 1.8% |
| 8 | Roubaix, France | 14 | 1.8% |
| 9 | Hillsboro, United States | 13 | 1.7% |
| 10 | Sopot, Bulgaria | 13 | 1.7% |
| 11 | Dublin, United States | 12 | 1.6% |
| 12 | Ashburn, United States | 12 | 1.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `193.46.255.141` | 552 | 72.0% | United Kingdom / England / Rushden / Unmanaged LTD | No apparent signal |
| 2 | `216.180.246.60` | 37 | 4.8% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 3 | `151.101.218.13` | 20 | 2.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `45.198.224.125` | 16 | 2.1% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 5 | `118.123.1.37` | 14 | 1.8% | China / Sichuan / Chengdu / SC MY Lanxun Tech Corp | No apparent signal |
| 6 | `91.231.89.224` | 14 | 1.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `91.196.152.222` | 14 | 1.8% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 8 | `91.231.89.251` | 13 | 1.7% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `195.184.76.20` | 13 | 1.7% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 10 | `91.230.168.142` | 13 | 1.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 11 | `79.124.49.62` | 13 | 1.7% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 12 | `18.190.15.50` | 12 | 1.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `91.231.89.72` | 12 | 1.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `34.228.104.231` | 12 | 1.6% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `195.184.76.180` | 12 | 1.6% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.60` | 37 | 45.7% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `151.101.218.13` | 20 | 24.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `18.190.15.50` | 12 | 14.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `34.228.104.231` | 12 | 14.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
