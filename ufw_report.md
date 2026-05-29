# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 2023
- Unique source IPs: 1459
- Unique countries/cities (24h): 196
- Unique destination ports: 1323

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 108 | 5.3% |
| 2 | `8080` | 24 | 1.2% |
| 3 | `22` | 23 | 1.1% |
| 4 | `27015` | 15 | 0.7% |
| 5 | `8443` | 14 | 0.7% |
| 6 | `3306` | 13 | 0.6% |
| 7 | `5900` | 12 | 0.6% |
| 8 | `5060` | 11 | 0.5% |
| 9 | `3389` | 11 | 0.5% |
| 10 | `27017` | 9 | 0.4% |
| 11 | `9200` | 9 | 0.4% |
| 12 | `53` | 8 | 0.4% |
| 13 | `5683` | 8 | 0.4% |
| 14 | `161` | 7 | 0.3% |
| 15 | `8088` | 7 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 1800 | 89.0% |
| 2 | `UDP` | 219 | 10.8% |
| 3 | `47` | 3 | 0.1% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `146.190.164.28` | 62 | 3.1% |
| 2 | `23.64.58.56` | 17 | 0.8% |
| 3 | `176.65.148.229` | 15 | 0.7% |
| 4 | `141.98.83.48` | 11 | 0.5% |
| 5 | `151.101.216.159` | 9 | 0.4% |
| 6 | `124.198.131.22` | 8 | 0.4% |
| 7 | `88.208.17.2` | 8 | 0.4% |
| 8 | `204.76.203.15` | 7 | 0.3% |
| 9 | `18.221.179.104` | 7 | 0.3% |
| 10 | `34.228.104.231` | 7 | 0.3% |
| 11 | `3.83.245.221` | 7 | 0.3% |
| 12 | `18.190.15.50` | 7 | 0.3% |
| 13 | `18.189.74.1` | 6 | 0.3% |
| 14 | `3.142.170.60` | 6 | 0.3% |
| 15 | `209.222.101.194` | 6 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 1730 | 96.1% |
| 2 | `ACK+FIN+PSH` | 41 | 2.3% |
| 3 | `ACK+PSH` | 20 | 1.1% |
| 4 | `ACK+FIN` | 7 | 0.4% |
| 5 | `SYN+ECE+CWR` | 1 | 0.1% |
| 6 | `ACK` | 1 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 2019 | 99.8% |
| 2 | `wlan0` | 4 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `146.190.164.28` -> `23` | 62 | 3.1% |
| 2 | `178.128.172.49` -> `23` | 6 | 0.3% |
| 3 | `199.45.155.88` -> `8443` | 6 | 0.3% |
| 4 | `69.17.52.1` -> `8333` | 5 | 0.2% |
| 5 | `151.101.216.159` -> `50290` | 5 | 0.2% |
| 6 | `151.101.216.158` -> `47892` | 5 | 0.2% |
| 7 | `192.168.100.1` -> `68` | 4 | 0.2% |
| 8 | `184.31.2.71` -> `54642` | 4 | 0.2% |
| 9 | `151.101.219.52` -> `43296` | 4 | 0.2% |
| 10 | `88.208.17.2` -> `33954` | 4 | 0.2% |
| 11 | `88.208.17.2` -> `50070` | 4 | 0.2% |
| 12 | `124.198.131.22` -> `8021` | 3 | 0.1% |
| 13 | `209.222.101.194` -> `8188` | 3 | 0.1% |
| 14 | `95.220.220.40` -> `8080` | 3 | 0.1% |
| 15 | `124.198.131.22` -> `8088` | 3 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-28 04:00:00:00 | 139 | 6.9% |
| 2026-05-28 05:00:00:00 | 179 | 8.8% |
| 2026-05-28 06:00:00:00 | 180 | 8.9% |
| 2026-05-28 07:00:00:00 | 80 | 4.0% |
| 2026-05-28 08:00:00:00 | 143 | 7.1% |
| 2026-05-28 21:00:00:00 | 126 | 6.2% |
| 2026-05-28 22:00:00:00 | 181 | 8.9% |
| 2026-05-28 23:00:00:00 | 198 | 9.8% |
| 2026-05-29 00:00:00:00 | 183 | 9.0% |
| 2026-05-29 01:00:00:00 | 197 | 9.7% |
| 2026-05-29 02:00:00:00 | 182 | 9.0% |
| 2026-05-29 03:00:00:00 | 191 | 9.4% |
| 2026-05-29 04:00:00:00 | 44 | 2.2% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Santa Clara, United States | 62 | 33.9% |
| 2 | Buenos Aires, Argentina | 26 | 14.2% |
| 3 | Dublin, United States | 26 | 14.2% |
| 4 | Eygelshoven, The Netherlands | 15 | 8.2% |
| 5 | Ashburn, United States | 14 | 7.7% |
| 6 | Panama City, Panama | 11 | 6.0% |
| 7 | New York, United States | 8 | 4.4% |
| 8 | Amsterdam, The Netherlands | 8 | 4.4% |
| 9 | Eygelshoven, Netherlands | 7 | 3.8% |
| 10 | Piscataway, United States | 6 | 3.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `146.190.164.28` | 62 | 33.9% | United States / California / Santa Clara / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `23.64.58.56` | 17 | 9.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. | CDN/Edge (akamai) |
| 3 | `176.65.148.229` | 15 | 8.2% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 4 | `141.98.83.48` | 11 | 6.0% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 5 | `151.101.216.159` | 9 | 4.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `124.198.131.22` | 8 | 4.4% | United States / New York / New York / 1337 Services GmbH | No apparent signal |
| 7 | `88.208.17.2` | 8 | 4.4% | The Netherlands / North Holland / Amsterdam / Advancedhosters Limited | No apparent signal |
| 8 | `204.76.203.15` | 7 | 3.8% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 9 | `18.221.179.104` | 7 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `34.228.104.231` | 7 | 3.8% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 11 | `3.83.245.221` | 7 | 3.8% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 12 | `18.190.15.50` | 7 | 3.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `18.189.74.1` | 6 | 3.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `3.142.170.60` | 6 | 3.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `209.222.101.194` | 6 | 3.3% | United States / New Jersey / Piscataway / ReliableSite.Net LLC | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `146.190.164.28` | 62 | 44.6% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / DigitalOcean, LLC |
| 2 | `23.64.58.56` | 17 | 12.2% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. |
| 3 | `141.98.83.48` | 11 | 7.9% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 4 | `151.101.216.159` | 9 | 6.5% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `18.221.179.104` | 7 | 5.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `34.228.104.231` | 7 | 5.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 7 | `3.83.245.221` | 7 | 5.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 8 | `18.190.15.50` | 7 | 5.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 9 | `18.189.74.1` | 6 | 4.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 10 | `3.142.170.60` | 6 | 4.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
