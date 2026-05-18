# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4343
- Unique source IPs: 1420
- Unique countries/cities (24h): 279
- Unique destination ports: 3526

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 84 | 1.9% |
| 2 | `27015` | 66 | 1.5% |
| 3 | `8080` | 31 | 0.7% |
| 4 | `22` | 17 | 0.4% |
| 5 | `5060` | 17 | 0.4% |
| 6 | `3389` | 13 | 0.3% |
| 7 | `53` | 11 | 0.3% |
| 8 | `17185` | 10 | 0.2% |
| 9 | `2222` | 9 | 0.2% |
| 10 | `1433` | 9 | 0.2% |
| 11 | `9200` | 9 | 0.2% |
| 12 | `2095` | 9 | 0.2% |
| 13 | `3004` | 9 | 0.2% |
| 14 | `8443` | 8 | 0.2% |
| 15 | `123` | 8 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4043 | 93.1% |
| 2 | `UDP` | 295 | 6.8% |
| 3 | `47` | 4 | 0.1% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `77.90.185.43` | 2364 | 54.4% |
| 2 | `216.180.246.27` | 40 | 0.9% |
| 3 | `5.61.209.33` | 11 | 0.3% |
| 4 | `198.199.75.230` | 10 | 0.2% |
| 5 | `43.228.157.10` | 10 | 0.2% |
| 6 | `208.109.32.229` | 10 | 0.2% |
| 7 | `18.119.209.50` | 9 | 0.2% |
| 8 | `51.250.24.20` | 9 | 0.2% |
| 9 | `43.228.157.8` | 9 | 0.2% |
| 10 | `3.132.36.44` | 9 | 0.2% |
| 11 | `100.28.153.226` | 8 | 0.2% |
| 12 | `18.217.208.51` | 8 | 0.2% |
| 13 | `151.101.217.44` | 8 | 0.2% |
| 14 | `185.242.226.73` | 7 | 0.2% |
| 15 | `43.228.157.9` | 7 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 4003 | 99.0% |
| 2 | `ACK+FIN+PSH` | 22 | 0.5% |
| 3 | `ACK+PSH` | 12 | 0.3% |
| 4 | `SYN+ECE+CWR` | 3 | 0.1% |
| 5 | `ACK+FIN` | 2 | 0.0% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4341 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `5.61.209.33` -> `8080` | 11 | 0.3% |
| 2 | `198.199.75.230` -> `23` | 10 | 0.2% |
| 3 | `208.109.32.229` -> `23` | 10 | 0.2% |
| 4 | `216.180.246.27` -> `3004` | 9 | 0.2% |
| 5 | `216.180.246.27` -> `17185` | 9 | 0.2% |
| 6 | `216.180.246.27` -> `2095` | 8 | 0.2% |
| 7 | `103.56.162.106` -> `23` | 7 | 0.2% |
| 8 | `177.53.6.115` -> `8080` | 6 | 0.1% |
| 9 | `216.180.246.27` -> `2103` | 6 | 0.1% |
| 10 | `3.132.36.44` -> `57594` | 5 | 0.1% |
| 11 | `151.101.217.44` -> `57760` | 5 | 0.1% |
| 12 | `45.153.34.63` -> `23` | 4 | 0.1% |
| 13 | `162.159.140.229` -> `35996` | 4 | 0.1% |
| 14 | `3.132.36.44` -> `57598` | 4 | 0.1% |
| 15 | `104.18.193.136` -> `19356` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-17 04:00:00:00 | 135 | 3.1% |
| 2026-05-17 05:00:00:00 | 180 | 4.1% |
| 2026-05-17 06:00:00:00 | 179 | 4.1% |
| 2026-05-17 07:00:00:00 | 177 | 4.1% |
| 2026-05-17 08:00:00:00 | 183 | 4.2% |
| 2026-05-17 09:00:00:00 | 179 | 4.1% |
| 2026-05-17 10:00:00:00 | 177 | 4.1% |
| 2026-05-17 11:00:00:00 | 183 | 4.2% |
| 2026-05-17 12:00:00:00 | 180 | 4.1% |
| 2026-05-17 13:00:00:00 | 180 | 4.1% |
| 2026-05-17 14:00:00:00 | 180 | 4.1% |
| 2026-05-17 15:00:00:00 | 180 | 4.1% |
| 2026-05-17 16:00:00:00 | 180 | 4.1% |
| 2026-05-17 17:00:00:00 | 180 | 4.1% |
| 2026-05-17 18:00:00:00 | 180 | 4.1% |
| 2026-05-17 19:00:00:00 | 180 | 4.1% |
| 2026-05-17 20:00:00:00 | 180 | 4.1% |
| 2026-05-17 21:00:00:00 | 180 | 4.1% |
| 2026-05-17 22:00:00:00 | 193 | 4.4% |
| 2026-05-17 23:00:00:00 | 180 | 4.1% |
| 2026-05-18 00:00:00:00 | 185 | 4.3% |
| 2026-05-18 01:00:00:00 | 179 | 4.1% |
| 2026-05-18 02:00:00:00 | 188 | 4.3% |
| 2026-05-18 03:00:00:00 | 180 | 4.1% |
| 2026-05-18 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Augsburg, Germany | 2364 | 93.8% |
| 2 | Massy, France | 40 | 1.6% |
| 3 | Singapore, Singapore | 26 | 1.0% |
| 4 | Dublin, United States | 26 | 1.0% |
| 5 | Amsterdam, The Netherlands | 18 | 0.7% |
| 6 | North Bergen, United States | 10 | 0.4% |
| 7 | Tempe, United States | 10 | 0.4% |
| 8 | Moscow, Russia | 9 | 0.4% |
| 9 | Ashburn, United States | 8 | 0.3% |
| 10 | Buenos Aires, Argentina | 8 | 0.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `77.90.185.43` | 2364 | 93.8% | Germany / Bavaria / Augsburg / Inside Network LTD | No apparent signal |
| 2 | `216.180.246.27` | 40 | 1.6% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 3 | `5.61.209.33` | 11 | 0.4% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd. Network | No apparent signal |
| 4 | `198.199.75.230` | 10 | 0.4% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `43.228.157.10` | 10 | 0.4% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 6 | `208.109.32.229` | 10 | 0.4% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 7 | `18.119.209.50` | 9 | 0.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `51.250.24.20` | 9 | 0.4% | Russia / Moscow / Moscow / Yandex.Cloud LLC | No apparent signal |
| 9 | `43.228.157.8` | 9 | 0.4% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 10 | `3.132.36.44` | 9 | 0.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `100.28.153.226` | 8 | 0.3% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 12 | `18.217.208.51` | 8 | 0.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `151.101.217.44` | 8 | 0.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 14 | `185.242.226.73` | 7 | 0.3% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 15 | `43.228.157.9` | 7 | 0.3% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.27` | 40 | 43.5% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `198.199.75.230` | 10 | 10.9% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 3 | `18.119.209.50` | 9 | 9.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `3.132.36.44` | 9 | 9.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `100.28.153.226` | 8 | 8.7% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 6 | `18.217.208.51` | 8 | 8.7% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `151.101.217.44` | 8 | 8.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
