# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4339
- Unique source IPs: 2412
- Unique countries/cities (24h): 300
- Unique destination ports: 2232

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 868 | 20.0% |
| 2 | `22` | 46 | 1.1% |
| 3 | `8080` | 32 | 0.7% |
| 4 | `5060` | 28 | 0.6% |
| 5 | `53` | 28 | 0.6% |
| 6 | `5555` | 27 | 0.6% |
| 7 | `3389` | 26 | 0.6% |
| 8 | `1433` | 18 | 0.4% |
| 9 | `3306` | 15 | 0.3% |
| 10 | `8000` | 15 | 0.3% |
| 11 | `8443` | 14 | 0.3% |
| 12 | `8333` | 14 | 0.3% |
| 13 | `5900` | 13 | 0.3% |
| 14 | `161` | 13 | 0.3% |
| 15 | `8088` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3966 | 91.4% |
| 2 | `UDP` | 363 | 8.4% |
| 3 | `47` | 9 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `38.102.86.198` | 616 | 14.2% |
| 2 | `137.184.169.96` | 61 | 1.4% |
| 3 | `111.68.25.6` | 48 | 1.1% |
| 4 | `164.92.172.229` | 43 | 1.0% |
| 5 | `176.65.139.188` | 18 | 0.4% |
| 6 | `51.159.110.167` | 14 | 0.3% |
| 7 | `185.242.3.226` | 12 | 0.3% |
| 8 | `18.221.179.104` | 11 | 0.3% |
| 9 | `204.76.203.15` | 11 | 0.3% |
| 10 | `69.17.52.1` | 11 | 0.3% |
| 11 | `45.198.224.10` | 11 | 0.3% |
| 12 | `35.169.206.177` | 10 | 0.2% |
| 13 | `5.187.35.26` | 10 | 0.2% |
| 14 | `134.209.112.87` | 9 | 0.2% |
| 15 | `43.228.157.10` | 9 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3916 | 98.7% |
| 2 | `ACK+PSH` | 21 | 0.5% |
| 3 | `ACK+FIN+PSH` | 14 | 0.4% |
| 4 | `ACK` | 7 | 0.2% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |
| 6 | `ACK+FIN` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4337 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `38.102.86.198` -> `23` | 616 | 14.2% |
| 2 | `137.184.169.96` -> `23` | 61 | 1.4% |
| 3 | `111.68.25.6` -> `23` | 48 | 1.1% |
| 4 | `164.92.172.229` -> `23` | 43 | 1.0% |
| 5 | `176.65.139.188` -> `5555` | 18 | 0.4% |
| 6 | `69.17.52.1` -> `8333` | 11 | 0.3% |
| 7 | `45.40.143.148` -> `23` | 9 | 0.2% |
| 8 | `198.12.157.248` -> `23` | 9 | 0.2% |
| 9 | `2.23.164.154` -> `14301` | 7 | 0.2% |
| 10 | `154.0.30.137` -> `3389` | 6 | 0.1% |
| 11 | `151.101.218.73` -> `63862` | 6 | 0.1% |
| 12 | `51.159.110.167` -> `25564` | 5 | 0.1% |
| 13 | `51.159.110.167` -> `25565` | 5 | 0.1% |
| 14 | `24.199.88.4` -> `23` | 4 | 0.1% |
| 15 | `51.159.110.167` -> `25566` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-15 04:00:00:00 | 135 | 3.1% |
| 2026-05-15 05:00:00:00 | 179 | 4.1% |
| 2026-05-15 06:00:00:00 | 181 | 4.2% |
| 2026-05-15 07:00:00:00 | 180 | 4.1% |
| 2026-05-15 08:00:00:00 | 180 | 4.1% |
| 2026-05-15 09:00:00:00 | 180 | 4.1% |
| 2026-05-15 10:00:00:00 | 182 | 4.2% |
| 2026-05-15 11:00:00:00 | 180 | 4.1% |
| 2026-05-15 12:00:00:00 | 179 | 4.1% |
| 2026-05-15 13:00:00:00 | 181 | 4.2% |
| 2026-05-15 14:00:00:00 | 180 | 4.1% |
| 2026-05-15 15:00:00:00 | 179 | 4.1% |
| 2026-05-15 16:00:00:00 | 181 | 4.2% |
| 2026-05-15 17:00:00:00 | 180 | 4.1% |
| 2026-05-15 18:00:00:00 | 179 | 4.1% |
| 2026-05-15 19:00:00:00 | 181 | 4.2% |
| 2026-05-15 20:00:00:00 | 197 | 4.5% |
| 2026-05-15 21:00:00:00 | 180 | 4.1% |
| 2026-05-15 22:00:00:00 | 181 | 4.2% |
| 2026-05-15 23:00:00:00 | 179 | 4.1% |
| 2026-05-16 00:00:00:00 | 181 | 4.2% |
| 2026-05-16 01:00:00:00 | 178 | 4.1% |
| 2026-05-16 02:00:00:00 | 182 | 4.2% |
| 2026-05-16 03:00:00:00 | 178 | 4.1% |
| 2026-05-16 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Montreal, Canada | 616 | 68.9% |
| 2 | Toronto, Canada | 61 | 6.8% |
| 3 | Frankfurt am Main, Germany | 55 | 6.2% |
| 4 | Bantul, Indonesia | 48 | 5.4% |
| 5 | Eygelshoven, The Netherlands | 18 | 2.0% |
| 6 | Paris, France | 14 | 1.6% |
| 7 | Dublin, United States | 11 | 1.2% |
| 8 | Eygelshoven, Netherlands | 11 | 1.2% |
| 9 | Lewes, United States | 11 | 1.2% |
| 10 | Stockholm, Sweden | 11 | 1.2% |
| 11 | Ashburn, United States | 10 | 1.1% |
| 12 | Amsterdam, The Netherlands | 10 | 1.1% |
| 13 | North Bergen, United States | 9 | 1.0% |
| 14 | Singapore, Singapore | 9 | 1.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `38.102.86.198` | 616 | 68.9% | Canada / Quebec / Montreal / Rica Web Services | No apparent signal |
| 2 | `137.184.169.96` | 61 | 6.8% | Canada / Ontario / Toronto / Digital Ocean | Hosting/Cloud (digitalocean) |
| 3 | `111.68.25.6` | 48 | 5.4% | Indonesia / Yogyakarta / Bantul / GMEDIA | No apparent signal |
| 4 | `164.92.172.229` | 43 | 4.8% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `176.65.139.188` | 18 | 2.0% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 6 | `51.159.110.167` | 14 | 1.6% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 7 | `185.242.3.226` | 12 | 1.3% | Germany / Hesse / Frankfurt am Main / Felcloud | No apparent signal |
| 8 | `18.221.179.104` | 11 | 1.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `204.76.203.15` | 11 | 1.2% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 10 | `69.17.52.1` | 11 | 1.2% | United States / Delaware / Lewes / Spruce Creek Networks LLC | No apparent signal |
| 11 | `45.198.224.10` | 11 | 1.2% | Sweden / Stockholm County / Stockholm / Cloud Innovation Ltd | No apparent signal |
| 12 | `35.169.206.177` | 10 | 1.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `5.187.35.26` | 10 | 1.1% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 14 | `134.209.112.87` | 9 | 1.0% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 15 | `43.228.157.10` | 9 | 1.0% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `137.184.169.96` | 61 | 41.2% | Hosting/Cloud (digitalocean) | Canada / Ontario / Toronto / Digital Ocean |
| 2 | `164.92.172.229` | 43 | 29.1% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |
| 3 | `51.159.110.167` | 14 | 9.5% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 4 | `18.221.179.104` | 11 | 7.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `35.169.206.177` | 10 | 6.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 6 | `134.209.112.87` | 9 | 6.1% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
