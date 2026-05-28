# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4336
- Unique source IPs: 2587
- Unique countries/cities (24h): 382
- Unique destination ports: 2437

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 181 | 4.2% |
| 2 | `27015` | 64 | 1.5% |
| 3 | `22` | 42 | 1.0% |
| 4 | `5060` | 37 | 0.9% |
| 5 | `8080` | 32 | 0.7% |
| 6 | `3389` | 31 | 0.7% |
| 7 | `8443` | 28 | 0.6% |
| 8 | `9200` | 22 | 0.5% |
| 9 | `8333` | 22 | 0.5% |
| 10 | `3000` | 21 | 0.5% |
| 11 | `1433` | 21 | 0.5% |
| 12 | `8081` | 20 | 0.5% |
| 13 | `161` | 20 | 0.5% |
| 14 | `53` | 19 | 0.4% |
| 15 | `3306` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3740 | 86.3% |
| 2 | `UDP` | 582 | 13.4% |
| 3 | `47` | 11 | 0.3% |
| 4 | `4` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `206.81.2.201` | 79 | 1.8% |
| 2 | `194.32.122.17` | 19 | 0.4% |
| 3 | `51.159.110.167` | 17 | 0.4% |
| 4 | `161.35.10.162` | 17 | 0.4% |
| 5 | `124.198.131.22` | 16 | 0.4% |
| 6 | `69.17.52.1` | 16 | 0.4% |
| 7 | `3.131.24.55` | 13 | 0.3% |
| 8 | `170.51.247.40` | 13 | 0.3% |
| 9 | `18.190.15.50` | 12 | 0.3% |
| 10 | `18.119.209.50` | 12 | 0.3% |
| 11 | `151.243.11.37` | 12 | 0.3% |
| 12 | `3.142.170.60` | 11 | 0.3% |
| 13 | `204.76.203.15` | 11 | 0.3% |
| 14 | `100.50.17.159` | 11 | 0.3% |
| 15 | `35.169.206.177` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3639 | 97.3% |
| 2 | `ACK+PSH` | 50 | 1.3% |
| 3 | `ACK+FIN+PSH` | 46 | 1.2% |
| 4 | `ACK+FIN` | 4 | 0.1% |
| 5 | `SYN+ECE+CWR` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4327 | 99.8% |
| 2 | `wlan0` | 9 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `206.81.2.201` -> `23` | 79 | 1.8% |
| 2 | `69.17.52.1` -> `8333` | 16 | 0.4% |
| 3 | `124.198.131.22` -> `3000` | 12 | 0.3% |
| 4 | `192.168.100.1` -> `68` | 9 | 0.2% |
| 5 | `216.180.246.6` -> `80` | 7 | 0.2% |
| 6 | `51.159.110.167` -> `25566` | 6 | 0.1% |
| 7 | `47.89.154.16` -> `443` | 6 | 0.1% |
| 8 | `51.159.110.167` -> `25564` | 6 | 0.1% |
| 9 | `66.132.172.41` -> `44888` | 6 | 0.1% |
| 10 | `142.251.0.188` -> `47390` | 6 | 0.1% |
| 11 | `51.159.110.167` -> `25565` | 5 | 0.1% |
| 12 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 13 | `66.132.195.110` -> `9013` | 5 | 0.1% |
| 14 | `199.45.155.86` -> `4514` | 5 | 0.1% |
| 15 | `2.23.164.166` -> `59319` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-27 04:00:00:00 | 135 | 3.1% |
| 2026-05-27 05:00:00:00 | 175 | 4.0% |
| 2026-05-27 06:00:00:00 | 177 | 4.1% |
| 2026-05-27 07:00:00:00 | 174 | 4.0% |
| 2026-05-27 08:00:00:00 | 183 | 4.2% |
| 2026-05-27 09:00:00:00 | 179 | 4.1% |
| 2026-05-27 10:00:00:00 | 181 | 4.2% |
| 2026-05-27 11:00:00:00 | 168 | 3.9% |
| 2026-05-27 12:00:00:00 | 183 | 4.2% |
| 2026-05-27 13:00:00:00 | 193 | 4.5% |
| 2026-05-27 14:00:00:00 | 175 | 4.0% |
| 2026-05-27 15:00:00:00 | 180 | 4.2% |
| 2026-05-27 16:00:00:00 | 178 | 4.1% |
| 2026-05-27 17:00:00:00 | 189 | 4.4% |
| 2026-05-27 18:00:00:00 | 185 | 4.3% |
| 2026-05-27 19:00:00:00 | 181 | 4.2% |
| 2026-05-27 20:00:00:00 | 180 | 4.2% |
| 2026-05-27 21:00:00:00 | 180 | 4.2% |
| 2026-05-27 22:00:00:00 | 191 | 4.4% |
| 2026-05-27 23:00:00:00 | 186 | 4.3% |
| 2026-05-28 00:00:00:00 | 180 | 4.2% |
| 2026-05-28 01:00:00:00 | 180 | 4.2% |
| 2026-05-28 02:00:00:00 | 182 | 4.2% |
| 2026-05-28 03:00:00:00 | 180 | 4.2% |
| 2026-05-28 04:00:00:00 | 41 | 0.9% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | North Bergen, United States | 96 | 35.6% |
| 2 | Dublin, United States | 48 | 17.8% |
| 3 | Ashburn, United States | 22 | 8.1% |
| 4 | Vilnius, Lithuania | 19 | 7.0% |
| 5 | Paris, France | 17 | 6.3% |
| 6 | New York, United States | 16 | 5.9% |
| 7 | Lewes, United States | 16 | 5.9% |
| 8 | Buenos Aires, Argentina | 13 | 4.8% |
| 9 | Frankfurt am Main, Germany | 12 | 4.4% |
| 10 | Eygelshoven, Netherlands | 11 | 4.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `206.81.2.201` | 79 | 29.3% | United States / New Jersey / North Bergen / Digital Ocean | Hosting/Cloud (digitalocean) |
| 2 | `194.32.122.17` | 19 | 7.0% | Lithuania / Vilnius / Vilnius / Cyberghost SRL | No apparent signal |
| 3 | `51.159.110.167` | 17 | 6.3% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 4 | `161.35.10.162` | 17 | 6.3% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `124.198.131.22` | 16 | 5.9% | United States / New York / New York / 1337 Services GmbH | No apparent signal |
| 6 | `69.17.52.1` | 16 | 5.9% | United States / Delaware / Lewes / Spruce Creek Networks LLC | No apparent signal |
| 7 | `3.131.24.55` | 13 | 4.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `170.51.247.40` | 13 | 4.8% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 9 | `18.190.15.50` | 12 | 4.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `18.119.209.50` | 12 | 4.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `151.243.11.37` | 12 | 4.4% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 12 | `3.142.170.60` | 11 | 4.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `204.76.203.15` | 11 | 4.1% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 14 | `100.50.17.159` | 11 | 4.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `35.169.206.177` | 11 | 4.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `206.81.2.201` | 79 | 43.2% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / Digital Ocean |
| 2 | `51.159.110.167` | 17 | 9.3% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 3 | `161.35.10.162` | 17 | 9.3% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 4 | `3.131.24.55` | 13 | 7.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.190.15.50` | 12 | 6.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `18.119.209.50` | 12 | 6.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `3.142.170.60` | 11 | 6.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 8 | `100.50.17.159` | 11 | 6.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 9 | `35.169.206.177` | 11 | 6.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
