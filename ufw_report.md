# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4408
- Unique source IPs: 2643
- Unique countries/cities (24h): 392
- Unique destination ports: 2266

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 725 | 16.4% |
| 2 | `unknown` | 73 | 1.7% |
| 3 | `8080` | 33 | 0.7% |
| 4 | `2323` | 32 | 0.7% |
| 5 | `22` | 31 | 0.7% |
| 6 | `5060` | 30 | 0.7% |
| 7 | `5555` | 26 | 0.6% |
| 8 | `3389` | 25 | 0.6% |
| 9 | `27015` | 23 | 0.5% |
| 10 | `1433` | 22 | 0.5% |
| 11 | `3306` | 22 | 0.5% |
| 12 | `8443` | 17 | 0.4% |
| 13 | `53` | 17 | 0.4% |
| 14 | `9000` | 16 | 0.4% |
| 15 | `8000` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3913 | 88.8% |
| 2 | `UDP` | 422 | 9.6% |
| 3 | `47` | 72 | 1.6% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.142` | 134 | 3.0% |
| 2 | `104.247.75.190` | 98 | 2.2% |
| 3 | `37.32.45.101` | 47 | 1.1% |
| 4 | `36.234.49.133` | 38 | 0.9% |
| 5 | `151.101.218.13` | 23 | 0.5% |
| 6 | `149.154.167.220` | 22 | 0.5% |
| 7 | `149.154.166.110` | 20 | 0.5% |
| 8 | `105.184.93.176` | 16 | 0.4% |
| 9 | `24.199.88.4` | 14 | 0.3% |
| 10 | `85.217.149.20` | 14 | 0.3% |
| 11 | `192.168.100.118` | 14 | 0.3% |
| 12 | `192.168.100.174` | 13 | 0.3% |
| 13 | `222.95.180.4` | 12 | 0.3% |
| 14 | `2.22.149.178` | 11 | 0.2% |
| 15 | `38.34.175.13` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3785 | 96.7% |
| 2 | `ACK+FIN+PSH` | 67 | 1.7% |
| 3 | `ACK+PSH` | 36 | 0.9% |
| 4 | `ACK+FIN` | 19 | 0.5% |
| 5 | `SYN+ECE+CWR` | 5 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4403 | 99.9% |
| 2 | `wlan0` | 5 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `104.247.75.190` -> `23` | 98 | 2.2% |
| 2 | `36.234.49.133` -> `23` | 38 | 0.9% |
| 3 | `105.184.93.176` -> `23` | 16 | 0.4% |
| 4 | `24.199.88.4` -> `23` | 14 | 0.3% |
| 5 | `222.95.180.4` -> `23` | 12 | 0.3% |
| 6 | `38.34.175.13` -> `23` | 11 | 0.2% |
| 7 | `38.34.175.19` -> `23` | 10 | 0.2% |
| 8 | `43.245.39.47` -> `23` | 10 | 0.2% |
| 9 | `114.226.82.136` -> `23` | 10 | 0.2% |
| 10 | `189.126.4.194` -> `23` | 9 | 0.2% |
| 11 | `38.34.175.20` -> `23` | 9 | 0.2% |
| 12 | `216.180.246.142` -> `4433` | 9 | 0.2% |
| 13 | `216.180.246.142` -> `5001` | 9 | 0.2% |
| 14 | `69.17.52.1` -> `8333` | 8 | 0.2% |
| 15 | `38.34.175.88` -> `23` | 8 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-16 04:00:00:00 | 143 | 3.2% |
| 2026-06-16 05:00:00:00 | 182 | 4.1% |
| 2026-06-16 06:00:00:00 | 231 | 5.2% |
| 2026-06-16 07:00:00:00 | 180 | 4.1% |
| 2026-06-16 08:00:00:00 | 180 | 4.1% |
| 2026-06-16 09:00:00:00 | 180 | 4.1% |
| 2026-06-16 10:00:00:00 | 179 | 4.1% |
| 2026-06-16 11:00:00:00 | 180 | 4.1% |
| 2026-06-16 12:00:00:00 | 181 | 4.1% |
| 2026-06-16 13:00:00:00 | 180 | 4.1% |
| 2026-06-16 14:00:00:00 | 182 | 4.1% |
| 2026-06-16 15:00:00:00 | 180 | 4.1% |
| 2026-06-16 16:00:00:00 | 180 | 4.1% |
| 2026-06-16 17:00:00:00 | 187 | 4.2% |
| 2026-06-16 18:00:00:00 | 197 | 4.5% |
| 2026-06-16 19:00:00:00 | 180 | 4.1% |
| 2026-06-16 20:00:00:00 | 179 | 4.1% |
| 2026-06-16 21:00:00:00 | 181 | 4.1% |
| 2026-06-16 22:00:00:00 | 180 | 4.1% |
| 2026-06-16 23:00:00:00 | 180 | 4.1% |
| 2026-06-17 00:00:00:00 | 180 | 4.1% |
| 2026-06-17 01:00:00:00 | 180 | 4.1% |
| 2026-06-17 02:00:00:00 | 179 | 4.1% |
| 2026-06-17 03:00:00:00 | 181 | 4.1% |
| 2026-06-17 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 134 | 27.5% |
| 2 | Los Angeles, United States | 98 | 20.1% |
| 3 | Abadan, Iran | 47 | 9.7% |
| 4 | Amsterdam, Netherlands | 42 | 8.6% |
| 5 | Taichung, Taiwan | 38 | 7.8% |
| 6 | Buenos Aires, Argentina | 34 | 7.0% |
| 7 | private | 27 | 5.5% |
| 8 | Kimberley, South Africa | 16 | 3.3% |
| 9 | North Bergen, United States | 14 | 2.9% |
| 10 | New York, United States | 14 | 2.9% |
| 11 | Nanjing, China | 12 | 2.5% |
| 12 | Redondo Beach, United States | 11 | 2.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.142` | 134 | 27.5% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `104.247.75.190` | 98 | 20.1% | United States / California / Los Angeles / InMotion Hosting, Inc | No apparent signal |
| 3 | `37.32.45.101` | 47 | 9.7% | Iran / Khuzestan / Abadan / Peyman Ertebatat poya | No apparent signal |
| 4 | `36.234.49.133` | 38 | 7.8% | Taiwan / Taichung City / Taichung / Chunghwa Telecom Co. Ltd. | No apparent signal |
| 5 | `151.101.218.13` | 23 | 4.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `149.154.167.220` | 22 | 4.5% | Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 7 | `149.154.166.110` | 20 | 4.1% | Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 8 | `105.184.93.176` | 16 | 3.3% | South Africa / Northern Cape / Kimberley / Telkom Internet Broadband 105 | No apparent signal |
| 9 | `24.199.88.4` | 14 | 2.9% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 10 | `85.217.149.20` | 14 | 2.9% | United States / New York / New York / Modat B.V | No apparent signal |
| 11 | `192.168.100.118` | 14 | 2.9% | private | Private/CGNAT |
| 12 | `192.168.100.174` | 13 | 2.7% | private | Private/CGNAT |
| 13 | `222.95.180.4` | 12 | 2.5% | China / Jiangsu / Nanjing / Chinanet JS | No apparent signal |
| 14 | `2.22.149.178` | 11 | 2.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 15 | `38.34.175.13` | 11 | 2.3% | United States / California / Redondo Beach / Enzu Inc | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.142` | 134 | 73.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 23 | 12.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `24.199.88.4` | 14 | 7.7% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 4 | `2.22.149.178` | 11 | 6.0% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
