# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4374
- Unique source IPs: 2484
- Unique countries/cities (24h): 270
- Unique destination ports: 2475

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 113 | 2.6% |
| 2 | `22` | 61 | 1.4% |
| 3 | `3389` | 35 | 0.8% |
| 4 | `53` | 34 | 0.8% |
| 5 | `8080` | 34 | 0.8% |
| 6 | `1433` | 33 | 0.8% |
| 7 | `3306` | 28 | 0.6% |
| 8 | `8443` | 25 | 0.6% |
| 9 | `5060` | 25 | 0.6% |
| 10 | `8888` | 23 | 0.5% |
| 11 | `123` | 19 | 0.4% |
| 12 | `8081` | 16 | 0.4% |
| 13 | `8000` | 16 | 0.4% |
| 14 | `6379` | 15 | 0.3% |
| 15 | `161` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4015 | 91.8% |
| 2 | `UDP` | 351 | 8.0% |
| 3 | `47` | 6 | 0.1% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.222` | 194 | 4.4% |
| 2 | `79.124.49.62` | 23 | 0.5% |
| 3 | `45.198.224.125` | 17 | 0.4% |
| 4 | `2.22.149.176` | 16 | 0.4% |
| 5 | `52.21.227.35` | 14 | 0.3% |
| 6 | `91.196.152.235` | 14 | 0.3% |
| 7 | `91.196.152.190` | 14 | 0.3% |
| 8 | `91.196.152.222` | 14 | 0.3% |
| 9 | `91.231.89.72` | 14 | 0.3% |
| 10 | `91.231.89.238` | 13 | 0.3% |
| 11 | `91.231.89.104` | 13 | 0.3% |
| 12 | `91.231.89.205` | 13 | 0.3% |
| 13 | `167.99.151.166` | 12 | 0.3% |
| 14 | `91.231.89.224` | 12 | 0.3% |
| 15 | `195.184.76.198` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3937 | 98.1% |
| 2 | `ACK+FIN+PSH` | 47 | 1.2% |
| 3 | `ACK+PSH` | 20 | 0.5% |
| 4 | `SYN+ECE+CWR` | 5 | 0.1% |
| 5 | `ACK+FIN` | 5 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4374 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.222` -> `8899` | 10 | 0.2% |
| 2 | `216.180.246.222` -> `9003` | 10 | 0.2% |
| 3 | `216.180.246.222` -> `8933` | 9 | 0.2% |
| 4 | `216.180.246.222` -> `8993` | 9 | 0.2% |
| 5 | `216.180.246.222` -> `9006` | 9 | 0.2% |
| 6 | `216.180.246.222` -> `9013` | 9 | 0.2% |
| 7 | `216.180.246.222` -> `8898` | 8 | 0.2% |
| 8 | `216.180.246.222` -> `8900` | 8 | 0.2% |
| 9 | `216.180.246.222` -> `9002` | 8 | 0.2% |
| 10 | `216.180.246.222` -> `9004` | 8 | 0.2% |
| 11 | `216.180.246.222` -> `9007` | 8 | 0.2% |
| 12 | `216.180.246.222` -> `9011` | 8 | 0.2% |
| 13 | `216.180.246.222` -> `9022` | 8 | 0.2% |
| 14 | `154.80.128.160` -> `6036` | 7 | 0.2% |
| 15 | `45.198.224.125` -> `8081` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-05 04:00:00:00 | 135 | 3.1% |
| 2026-11-05 05:00:00:00 | 180 | 4.1% |
| 2026-11-05 06:00:00:00 | 180 | 4.1% |
| 2026-11-05 07:00:00:00 | 181 | 4.1% |
| 2026-11-05 08:00:00:00 | 179 | 4.1% |
| 2026-11-05 09:00:00:00 | 179 | 4.1% |
| 2026-11-05 10:00:00:00 | 182 | 4.2% |
| 2026-11-05 11:00:00:00 | 185 | 4.2% |
| 2026-11-05 12:00:00:00 | 181 | 4.1% |
| 2026-11-05 13:00:00:00 | 199 | 4.6% |
| 2026-11-05 14:00:00:00 | 184 | 4.2% |
| 2026-11-05 15:00:00:00 | 183 | 4.2% |
| 2026-11-05 16:00:00:00 | 184 | 4.2% |
| 2026-11-05 17:00:00:00 | 181 | 4.1% |
| 2026-11-05 18:00:00:00 | 178 | 4.1% |
| 2026-11-05 19:00:00:00 | 180 | 4.1% |
| 2026-11-05 20:00:00:00 | 181 | 4.1% |
| 2026-11-05 21:00:00:00 | 180 | 4.1% |
| 2026-11-05 22:00:00:00 | 188 | 4.3% |
| 2026-11-05 23:00:00:00 | 181 | 4.1% |
| 2026-11-06 00:00:00:00 | 181 | 4.1% |
| 2026-11-06 01:00:00:00 | 180 | 4.1% |
| 2026-11-06 02:00:00:00 | 177 | 4.0% |
| 2026-11-06 03:00:00:00 | 181 | 4.1% |
| 2026-11-06 04:00:00:00 | 53 | 1.2% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 194 | 49.1% |
| 2 | Gravelines, France | 65 | 16.5% |
| 3 | Roubaix, France | 42 | 10.6% |
| 4 | Sopot, Bulgaria | 23 | 5.8% |
| 5 | Stockholm, Sweden | 17 | 4.3% |
| 6 | Buenos Aires, Argentina | 16 | 4.1% |
| 7 | Ashburn, United States | 14 | 3.5% |
| 8 | North Bergen, United States | 12 | 3.0% |
| 9 | Warrenton, United States | 12 | 3.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.222` | 194 | 49.1% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `79.124.49.62` | 23 | 5.8% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 3 | `45.198.224.125` | 17 | 4.3% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 4 | `2.22.149.176` | 16 | 4.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 5 | `52.21.227.35` | 14 | 3.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 6 | `91.196.152.235` | 14 | 3.5% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 7 | `91.196.152.190` | 14 | 3.5% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 8 | `91.196.152.222` | 14 | 3.5% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 9 | `91.231.89.72` | 14 | 3.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `91.231.89.238` | 13 | 3.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 11 | `91.231.89.104` | 13 | 3.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `91.231.89.205` | 13 | 3.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `167.99.151.166` | 12 | 3.0% | United States / New Jersey / North Bergen / Digital Ocean | Hosting/Cloud (digitalocean) |
| 14 | `91.231.89.224` | 12 | 3.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `195.184.76.198` | 12 | 3.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.222` | 194 | 82.2% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `2.22.149.176` | 16 | 6.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `52.21.227.35` | 14 | 5.9% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 4 | `167.99.151.166` | 12 | 5.1% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / Digital Ocean |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
