# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4335
- Unique source IPs: 2547
- Unique countries/cities (24h): 398
- Unique destination ports: 2332

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 123 | 2.8% |
| 2 | `27015` | 87 | 2.0% |
| 3 | `22` | 61 | 1.4% |
| 4 | `8080` | 55 | 1.3% |
| 5 | `3389` | 39 | 0.9% |
| 6 | `53` | 36 | 0.8% |
| 7 | `8081` | 30 | 0.7% |
| 8 | `5900` | 29 | 0.7% |
| 9 | `8443` | 29 | 0.7% |
| 10 | `5060` | 29 | 0.7% |
| 11 | `1433` | 26 | 0.6% |
| 12 | `81` | 25 | 0.6% |
| 13 | `88` | 24 | 0.6% |
| 14 | `3306` | 24 | 0.6% |
| 15 | `2222` | 22 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3616 | 83.4% |
| 2 | `UDP` | 708 | 16.3% |
| 3 | `47` | 10 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.249` | 38 | 0.9% |
| 2 | `31.59.160.12` | 34 | 0.8% |
| 3 | `49.163.99.53` | 32 | 0.7% |
| 4 | `82.147.85.62` | 23 | 0.5% |
| 5 | `72.167.38.71` | 20 | 0.5% |
| 6 | `176.65.139.130` | 19 | 0.4% |
| 7 | `17.57.144.155` | 18 | 0.4% |
| 8 | `103.82.195.145` | 16 | 0.4% |
| 9 | `192.241.179.233` | 14 | 0.3% |
| 10 | `3.131.24.55` | 14 | 0.3% |
| 11 | `18.119.209.50` | 14 | 0.3% |
| 12 | `18.189.74.1` | 14 | 0.3% |
| 13 | `18.217.208.51` | 14 | 0.3% |
| 14 | `51.159.110.167` | 14 | 0.3% |
| 15 | `204.76.203.15` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3489 | 96.5% |
| 2 | `ACK+PSH` | 56 | 1.5% |
| 3 | `ACK+FIN+PSH` | 30 | 0.8% |
| 4 | `ACK` | 27 | 0.7% |
| 5 | `ACK+FIN` | 8 | 0.2% |
| 6 | `SYN+ECE+CWR` | 6 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4333 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `72.167.38.71` -> `23` | 20 | 0.5% |
| 2 | `192.241.179.233` -> `23` | 14 | 0.3% |
| 3 | `69.17.52.1` -> `8333` | 11 | 0.3% |
| 4 | `45.198.224.18` -> `8728` | 9 | 0.2% |
| 5 | `178.128.147.121` -> `23` | 7 | 0.2% |
| 6 | `178.20.210.152` -> `1723` | 7 | 0.2% |
| 7 | `216.180.246.249` -> `22` | 7 | 0.2% |
| 8 | `216.180.246.249` -> `81` | 7 | 0.2% |
| 9 | `31.59.160.12` -> `82` | 6 | 0.1% |
| 10 | `31.59.160.12` -> `88` | 6 | 0.1% |
| 11 | `31.59.160.12` -> `8081` | 6 | 0.1% |
| 12 | `31.59.160.12` -> `83` | 6 | 0.1% |
| 13 | `176.65.139.151` -> `23` | 6 | 0.1% |
| 14 | `124.198.131.39` -> `3000` | 6 | 0.1% |
| 15 | `216.180.246.25` -> `53` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-07 04:00:00:00 | 133 | 3.1% |
| 2026-06-07 05:00:00:00 | 180 | 4.2% |
| 2026-06-07 06:00:00:00 | 180 | 4.2% |
| 2026-06-07 07:00:00:00 | 180 | 4.2% |
| 2026-06-07 08:00:00:00 | 181 | 4.2% |
| 2026-06-07 09:00:00:00 | 182 | 4.2% |
| 2026-06-07 10:00:00:00 | 181 | 4.2% |
| 2026-06-07 11:00:00:00 | 179 | 4.1% |
| 2026-06-07 12:00:00:00 | 175 | 4.0% |
| 2026-06-07 13:00:00:00 | 183 | 4.2% |
| 2026-06-07 14:00:00:00 | 172 | 4.0% |
| 2026-06-07 15:00:00:00 | 177 | 4.1% |
| 2026-06-07 16:00:00:00 | 193 | 4.5% |
| 2026-06-07 17:00:00:00 | 179 | 4.1% |
| 2026-06-07 18:00:00:00 | 179 | 4.1% |
| 2026-06-07 19:00:00:00 | 181 | 4.2% |
| 2026-06-07 20:00:00:00 | 179 | 4.1% |
| 2026-06-07 21:00:00:00 | 181 | 4.2% |
| 2026-06-07 22:00:00:00 | 192 | 4.4% |
| 2026-06-07 23:00:00:00 | 179 | 4.1% |
| 2026-06-08 00:00:00:00 | 181 | 4.2% |
| 2026-06-08 01:00:00:00 | 178 | 4.1% |
| 2026-06-08 02:00:00:00 | 184 | 4.2% |
| 2026-06-08 03:00:00:00 | 177 | 4.1% |
| 2026-06-08 04:00:00:00 | 49 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dublin, United States | 56 | 18.9% |
| 2 | Massy, France | 38 | 12.8% |
| 3 | Abu Dhabi, United Arab Emirates | 34 | 11.4% |
| 4 | Gangseo-gu, South Korea | 32 | 10.8% |
| 5 | Novosibirsk, Russia | 23 | 7.7% |
| 6 | Tempe, United States | 20 | 6.7% |
| 7 | Eygelshoven, The Netherlands | 19 | 6.4% |
| 8 | Cupertino, United States | 18 | 6.1% |
| 9 | Thanh Khê, Vietnam | 16 | 5.4% |
| 10 | Secaucus, United States | 14 | 4.7% |
| 11 | Paris, France | 14 | 4.7% |
| 12 | Eygelshoven, Netherlands | 13 | 4.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.249` | 38 | 12.8% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `31.59.160.12` | 34 | 11.4% | United Arab Emirates / Abu Dhabi / Abu Dhabi / GoldIPv4 | No apparent signal |
| 3 | `49.163.99.53` | 32 | 10.8% | South Korea / Seoul / Gangseo-gu / LG POWERCOMM | No apparent signal |
| 4 | `82.147.85.62` | 23 | 7.7% | Russia / Novosibirsk Oblast / Novosibirsk / Nerushenko Vyacheslav Nikolaevich | No apparent signal |
| 5 | `72.167.38.71` | 20 | 6.7% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 6 | `176.65.139.130` | 19 | 6.4% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 7 | `17.57.144.155` | 18 | 6.1% | United States / California / Cupertino / Apple Inc | No apparent signal |
| 8 | `103.82.195.145` | 16 | 5.4% | Vietnam / Da Nang City / Thanh Khê / Cloudfly Corporation | No apparent signal |
| 9 | `192.241.179.233` | 14 | 4.7% | United States / New Jersey / Secaucus / Digital Ocean | Hosting/Cloud (digitalocean) |
| 10 | `3.131.24.55` | 14 | 4.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `18.119.209.50` | 14 | 4.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `18.189.74.1` | 14 | 4.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `18.217.208.51` | 14 | 4.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `51.159.110.167` | 14 | 4.7% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 15 | `204.76.203.15` | 13 | 4.4% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.249` | 38 | 31.1% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `192.241.179.233` | 14 | 11.5% | Hosting/Cloud (digitalocean) | United States / New Jersey / Secaucus / Digital Ocean |
| 3 | `3.131.24.55` | 14 | 11.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `18.119.209.50` | 14 | 11.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.189.74.1` | 14 | 11.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `18.217.208.51` | 14 | 11.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `51.159.110.167` | 14 | 11.5% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
