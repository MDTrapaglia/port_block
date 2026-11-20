# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4444
- Unique source IPs: 2516
- Unique countries/cities (24h): 302
- Unique destination ports: 2371

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 115 | 2.6% |
| 2 | `7680` | 81 | 1.8% |
| 3 | `22` | 66 | 1.5% |
| 4 | `8080` | 44 | 1.0% |
| 5 | `3389` | 40 | 0.9% |
| 6 | `5060` | 33 | 0.7% |
| 7 | `53` | 30 | 0.7% |
| 8 | `1433` | 24 | 0.5% |
| 9 | `8443` | 23 | 0.5% |
| 10 | `3306` | 21 | 0.5% |
| 11 | `8000` | 20 | 0.5% |
| 12 | `27017` | 19 | 0.4% |
| 13 | `8008` | 18 | 0.4% |
| 14 | `8081` | 18 | 0.4% |
| 15 | `33435` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4046 | 91.0% |
| 2 | `UDP` | 389 | 8.8% |
| 3 | `47` | 6 | 0.1% |
| 4 | `132` | 3 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.48` | 168 | 3.8% |
| 2 | `186.123.147.169` | 25 | 0.6% |
| 3 | `70.54.121.165` | 25 | 0.6% |
| 4 | `2.22.149.168` | 22 | 0.5% |
| 5 | `104.204.174.215` | 20 | 0.5% |
| 6 | `2.22.149.169` | 17 | 0.4% |
| 7 | `91.231.89.10` | 16 | 0.4% |
| 8 | `72.203.72.165` | 15 | 0.3% |
| 9 | `138.68.16.163` | 15 | 0.3% |
| 10 | `141.98.83.48` | 14 | 0.3% |
| 11 | `195.184.76.116` | 14 | 0.3% |
| 12 | `149.154.166.110` | 14 | 0.3% |
| 13 | `34.197.70.90` | 13 | 0.3% |
| 14 | `195.184.76.62` | 13 | 0.3% |
| 15 | `195.184.76.185` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3871 | 95.7% |
| 2 | `ACK+FIN+PSH` | 106 | 2.6% |
| 3 | `ACK+PSH` | 46 | 1.1% |
| 4 | `ACK+FIN` | 19 | 0.5% |
| 5 | `SYN+ECE+CWR` | 3 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4444 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `70.54.121.165` -> `7680` | 25 | 0.6% |
| 2 | `104.204.174.215` -> `7680` | 20 | 0.5% |
| 3 | `72.203.72.165` -> `7680` | 15 | 0.3% |
| 4 | `186.123.147.169` -> `23` | 14 | 0.3% |
| 5 | `68.4.170.109` -> `7680` | 11 | 0.2% |
| 6 | `186.123.147.169` -> `8291` | 11 | 0.2% |
| 7 | `216.180.246.48` -> `8005` | 9 | 0.2% |
| 8 | `216.180.246.48` -> `8008` | 9 | 0.2% |
| 9 | `216.180.246.48` -> `8011` | 9 | 0.2% |
| 10 | `216.180.246.48` -> `8028` | 9 | 0.2% |
| 11 | `91.224.92.45` -> `34567` | 8 | 0.2% |
| 12 | `95.100.88.80` -> `49248` | 8 | 0.2% |
| 13 | `93.123.109.6` -> `1723` | 7 | 0.2% |
| 14 | `216.180.246.48` -> `7900` | 7 | 0.2% |
| 15 | `216.180.246.48` -> `8014` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-19 04:00:00:00 | 135 | 3.0% |
| 2026-11-19 05:00:00:00 | 180 | 4.1% |
| 2026-11-19 06:00:00:00 | 179 | 4.0% |
| 2026-11-19 07:00:00:00 | 182 | 4.1% |
| 2026-11-19 08:00:00:00 | 180 | 4.1% |
| 2026-11-19 09:00:00:00 | 185 | 4.2% |
| 2026-11-19 10:00:00:00 | 181 | 4.1% |
| 2026-11-19 11:00:00:00 | 179 | 4.0% |
| 2026-11-19 12:00:00:00 | 178 | 4.0% |
| 2026-11-19 13:00:00:00 | 182 | 4.1% |
| 2026-11-19 14:00:00:00 | 182 | 4.1% |
| 2026-11-19 15:00:00:00 | 186 | 4.2% |
| 2026-11-19 16:00:00:00 | 182 | 4.1% |
| 2026-11-19 17:00:00:00 | 180 | 4.1% |
| 2026-11-19 18:00:00:00 | 183 | 4.1% |
| 2026-11-19 19:00:00:00 | 200 | 4.5% |
| 2026-11-19 20:00:00:00 | 180 | 4.1% |
| 2026-11-19 21:00:00:00 | 179 | 4.0% |
| 2026-11-19 22:00:00:00 | 200 | 4.5% |
| 2026-11-19 23:00:00:00 | 185 | 4.2% |
| 2026-11-20 00:00:00:00 | 238 | 5.4% |
| 2026-11-20 01:00:00:00 | 180 | 4.1% |
| 2026-11-20 02:00:00:00 | 184 | 4.1% |
| 2026-11-20 03:00:00:00 | 180 | 4.1% |
| 2026-11-20 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 168 | 41.6% |
| 2 | Warrenton, United States | 40 | 9.9% |
| 3 | Buenos Aires, Argentina | 39 | 9.7% |
| 4 | Santa Fe, Argentina | 25 | 6.2% |
| 5 | Nepean, Canada | 25 | 6.2% |
| 6 | Moorpark, United States | 20 | 5.0% |
| 7 | Gravelines, France | 16 | 4.0% |
| 8 | San Clemente, United States | 15 | 3.7% |
| 9 | Santa Clara, United States | 15 | 3.7% |
| 10 | Panama City, Panama | 14 | 3.5% |
| 11 | Amsterdam, Netherlands | 14 | 3.5% |
| 12 | Ashburn, United States | 13 | 3.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.48` | 168 | 41.6% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `186.123.147.169` | 25 | 6.2% | Argentina / Santa Fe / Santa Fe / AMX Argentina S.A | No apparent signal |
| 3 | `70.54.121.165` | 25 | 6.2% | Canada / Ontario / Nepean / Sympatico HSE | No apparent signal |
| 4 | `2.22.149.168` | 22 | 5.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 5 | `104.204.174.215` | 20 | 5.0% | United States / California / Moorpark / Aspire Broadband, LLC | No apparent signal |
| 6 | `2.22.149.169` | 17 | 4.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 7 | `91.231.89.10` | 16 | 4.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 8 | `72.203.72.165` | 15 | 3.7% | United States / California / San Clemente / Cox Communications Inc. | No apparent signal |
| 9 | `138.68.16.163` | 15 | 3.7% | United States / California / Santa Clara / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 10 | `141.98.83.48` | 14 | 3.5% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 11 | `195.184.76.116` | 14 | 3.5% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 12 | `149.154.166.110` | 14 | 3.5% | Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 13 | `34.197.70.90` | 13 | 3.2% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 14 | `195.184.76.62` | 13 | 3.2% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 15 | `195.184.76.185` | 13 | 3.2% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.48` | 168 | 67.5% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `2.22.149.168` | 22 | 8.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `2.22.149.169` | 17 | 6.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 4 | `138.68.16.163` | 15 | 6.0% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / DigitalOcean, LLC |
| 5 | `141.98.83.48` | 14 | 5.6% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 6 | `34.197.70.90` | 13 | 5.2% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
