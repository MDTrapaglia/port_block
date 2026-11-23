# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4345
- Unique source IPs: 2694
- Unique countries/cities (24h): 332
- Unique destination ports: 2327

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 119 | 2.7% |
| 2 | `22` | 97 | 2.2% |
| 3 | `53` | 51 | 1.2% |
| 4 | `3389` | 43 | 1.0% |
| 5 | `5060` | 37 | 0.9% |
| 6 | `1433` | 36 | 0.8% |
| 7 | `8080` | 35 | 0.8% |
| 8 | `8443` | 29 | 0.7% |
| 9 | `161` | 26 | 0.6% |
| 10 | `8081` | 26 | 0.6% |
| 11 | `2222` | 23 | 0.5% |
| 12 | `123` | 22 | 0.5% |
| 13 | `1723` | 20 | 0.5% |
| 14 | `3306` | 19 | 0.4% |
| 15 | `3000` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3867 | 89.0% |
| 2 | `UDP` | 467 | 10.7% |
| 3 | `47` | 8 | 0.2% |
| 4 | `132` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `178.236.185.67` | 50 | 1.2% |
| 2 | `45.156.87.168` | 44 | 1.0% |
| 3 | `219.153.113.103` | 29 | 0.7% |
| 4 | `151.101.218.13` | 19 | 0.4% |
| 5 | `87.120.104.79` | 16 | 0.4% |
| 6 | `3.147.122.184` | 15 | 0.3% |
| 7 | `18.190.15.50` | 14 | 0.3% |
| 8 | `3.15.230.87` | 14 | 0.3% |
| 9 | `34.197.70.90` | 13 | 0.3% |
| 10 | `86.54.31.36` | 13 | 0.3% |
| 11 | `3.131.24.55` | 12 | 0.3% |
| 12 | `94.156.152.46` | 11 | 0.3% |
| 13 | `80.82.77.139` | 11 | 0.3% |
| 14 | `18.217.208.51` | 11 | 0.3% |
| 15 | `18.221.179.104` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3818 | 98.7% |
| 2 | `ACK+FIN+PSH` | 28 | 0.7% |
| 3 | `ACK+PSH` | 10 | 0.3% |
| 4 | `SYN+ECE+CWR` | 9 | 0.2% |
| 5 | `ACK+FIN` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4345 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `118.212.132.226` -> `22` | 8 | 0.2% |
| 2 | `178.20.210.152` -> `1723` | 7 | 0.2% |
| 3 | `81.171.6.91` -> `22` | 7 | 0.2% |
| 4 | `91.224.92.45` -> `34567` | 6 | 0.1% |
| 5 | `216.180.246.90` -> `53` | 6 | 0.1% |
| 6 | `95.100.88.82` -> `38985` | 6 | 0.1% |
| 7 | `151.101.218.13` -> `63145` | 6 | 0.1% |
| 8 | `66.132.186.181` -> `50582` | 6 | 0.1% |
| 9 | `66.132.186.166` -> `8443` | 6 | 0.1% |
| 10 | `94.156.152.46` -> `2233` | 5 | 0.1% |
| 11 | `57.144.102.3` -> `36802` | 5 | 0.1% |
| 12 | `66.132.159.134` -> `8443` | 5 | 0.1% |
| 13 | `178.236.185.67` -> `3001` | 5 | 0.1% |
| 14 | `95.100.88.82` -> `62826` | 5 | 0.1% |
| 15 | `93.123.109.6` -> `1723` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-22 04:00:00:00 | 133 | 3.1% |
| 2026-11-22 05:00:00:00 | 181 | 4.2% |
| 2026-11-22 06:00:00:00 | 179 | 4.1% |
| 2026-11-22 07:00:00:00 | 178 | 4.1% |
| 2026-11-22 08:00:00:00 | 182 | 4.2% |
| 2026-11-22 09:00:00:00 | 181 | 4.2% |
| 2026-11-22 10:00:00:00 | 179 | 4.1% |
| 2026-11-22 11:00:00:00 | 177 | 4.1% |
| 2026-11-22 12:00:00:00 | 182 | 4.2% |
| 2026-11-22 13:00:00:00 | 209 | 4.8% |
| 2026-11-22 14:00:00:00 | 183 | 4.2% |
| 2026-11-22 15:00:00:00 | 179 | 4.1% |
| 2026-11-22 16:00:00:00 | 180 | 4.1% |
| 2026-11-22 17:00:00:00 | 180 | 4.1% |
| 2026-11-22 18:00:00:00 | 177 | 4.1% |
| 2026-11-22 19:00:00:00 | 181 | 4.2% |
| 2026-11-22 20:00:00:00 | 181 | 4.2% |
| 2026-11-22 21:00:00:00 | 179 | 4.1% |
| 2026-11-22 22:00:00:00 | 180 | 4.1% |
| 2026-11-22 23:00:00:00 | 180 | 4.1% |
| 2026-11-23 00:00:00:00 | 180 | 4.1% |
| 2026-11-23 01:00:00:00 | 181 | 4.2% |
| 2026-11-23 02:00:00:00 | 178 | 4.1% |
| 2026-11-23 03:00:00:00 | 181 | 4.2% |
| 2026-11-23 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dublin, United States | 63 | 22.3% |
| 2 | Amsterdam, The Netherlands | 57 | 20.1% |
| 3 | Mumbai, India | 50 | 17.7% |
| 4 | Chongqing, China | 29 | 10.2% |
| 5 | Buenos Aires, Argentina | 19 | 6.7% |
| 6 | Sandefjord, Norway | 16 | 5.7% |
| 7 | Columbus, United States | 14 | 4.9% |
| 8 | Ashburn, United States | 13 | 4.6% |
| 9 | Centurion, South Africa | 11 | 3.9% |
| 10 | Amsterdam, Netherlands | 11 | 3.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `178.236.185.67` | 50 | 17.7% | India / Maharashtra / Mumbai / HIVELOCITY, Inc | Hosting/Cloud (hivelocity) |
| 2 | `45.156.87.168` | 44 | 15.5% | The Netherlands / North Holland / Amsterdam / TechTies Inc | No apparent signal |
| 3 | `219.153.113.103` | 29 | 10.2% | China / Chongqing / Chongqing / Chinanet CQ | No apparent signal |
| 4 | `151.101.218.13` | 19 | 6.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `87.120.104.79` | 16 | 5.7% | Norway / Vestfold / Sandefjord / Sino Worldwide Trading Limited | No apparent signal |
| 6 | `3.147.122.184` | 15 | 5.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `18.190.15.50` | 14 | 4.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `3.15.230.87` | 14 | 4.9% | United States / Ohio / Columbus / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `34.197.70.90` | 13 | 4.6% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 10 | `86.54.31.36` | 13 | 4.6% | The Netherlands / North Holland / Amsterdam / ADSL: Circle IT Solutions Limited | No apparent signal |
| 11 | `3.131.24.55` | 12 | 4.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `94.156.152.46` | 11 | 3.9% | South Africa / Gauteng / Centurion / Internet Magnate (Pty) Ltd | No apparent signal |
| 13 | `80.82.77.139` | 11 | 3.9% | Netherlands / North Holland / Amsterdam / IP Volume inc | No apparent signal |
| 14 | `18.217.208.51` | 11 | 3.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `18.221.179.104` | 11 | 3.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `178.236.185.67` | 50 | 31.4% | Hosting/Cloud (hivelocity) | India / Maharashtra / Mumbai / HIVELOCITY, Inc |
| 2 | `151.101.218.13` | 19 | 11.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `3.147.122.184` | 15 | 9.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `18.190.15.50` | 14 | 8.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `3.15.230.87` | 14 | 8.8% | Hosting/Cloud (aws) | United States / Ohio / Columbus / AWS EC2 (us-east-2) |
| 6 | `34.197.70.90` | 13 | 8.2% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 7 | `3.131.24.55` | 12 | 7.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 8 | `18.217.208.51` | 11 | 6.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 9 | `18.221.179.104` | 11 | 6.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
