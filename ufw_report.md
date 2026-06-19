# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4393
- Unique source IPs: 2177
- Unique countries/cities (24h): 309
- Unique destination ports: 2330

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 941 | 21.4% |
| 2 | `unknown` | 58 | 1.3% |
| 3 | `22` | 32 | 0.7% |
| 4 | `5060` | 25 | 0.6% |
| 5 | `3389` | 23 | 0.5% |
| 6 | `1433` | 21 | 0.5% |
| 7 | `8080` | 20 | 0.5% |
| 8 | `8443` | 20 | 0.5% |
| 9 | `5555` | 16 | 0.4% |
| 10 | `27015` | 15 | 0.3% |
| 11 | `3306` | 14 | 0.3% |
| 12 | `88` | 13 | 0.3% |
| 13 | `8888` | 13 | 0.3% |
| 14 | `8000` | 13 | 0.3% |
| 15 | `3000` | 12 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4037 | 91.9% |
| 2 | `UDP` | 298 | 6.8% |
| 3 | `47` | 57 | 1.3% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `80.95.194.124` | 373 | 8.5% |
| 2 | `202.71.141.170` | 340 | 7.7% |
| 3 | `119.5.213.182` | 256 | 5.8% |
| 4 | `78.92.227.234` | 135 | 3.1% |
| 5 | `216.180.246.30` | 79 | 1.8% |
| 6 | `92.204.138.187` | 67 | 1.5% |
| 7 | `206.189.225.77` | 12 | 0.3% |
| 8 | `151.101.218.13` | 12 | 0.3% |
| 9 | `93.123.72.183` | 11 | 0.3% |
| 10 | `3.131.24.55` | 10 | 0.2% |
| 11 | `81.10.69.33` | 10 | 0.2% |
| 12 | `18.189.74.1` | 10 | 0.2% |
| 13 | `18.221.179.104` | 10 | 0.2% |
| 14 | `18.190.15.50` | 10 | 0.2% |
| 15 | `172.93.106.153` | 9 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3936 | 97.5% |
| 2 | `ACK+FIN+PSH` | 68 | 1.7% |
| 3 | `ACK+PSH` | 16 | 0.4% |
| 4 | `ACK` | 6 | 0.1% |
| 5 | `SYN+ECE+CWR` | 6 | 0.1% |
| 6 | `ACK+FIN` | 5 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4391 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `80.95.194.124` -> `23` | 373 | 8.5% |
| 2 | `119.5.213.182` -> `23` | 256 | 5.8% |
| 3 | `78.92.227.234` -> `23` | 135 | 3.1% |
| 4 | `92.204.138.187` -> `23` | 67 | 1.5% |
| 5 | `206.189.225.77` -> `23` | 12 | 0.3% |
| 6 | `81.10.69.33` -> `23` | 10 | 0.2% |
| 7 | `79.63.45.2` -> `23` | 9 | 0.2% |
| 8 | `94.156.152.50` -> `23` | 9 | 0.2% |
| 9 | `2.180.169.231` -> `23` | 8 | 0.2% |
| 10 | `166.62.41.96` -> `23` | 8 | 0.2% |
| 11 | `170.51.247.49` -> `49460` | 7 | 0.2% |
| 12 | `184.168.31.238` -> `23` | 6 | 0.1% |
| 13 | `170.51.247.33` -> `59156` | 6 | 0.1% |
| 14 | `216.180.246.30` -> `8300` | 6 | 0.1% |
| 15 | `130.12.180.174` -> `23` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-18 04:00:00:00 | 134 | 3.1% |
| 2026-06-18 05:00:00:00 | 180 | 4.1% |
| 2026-06-18 06:00:00:00 | 179 | 4.1% |
| 2026-06-18 07:00:00:00 | 181 | 4.1% |
| 2026-06-18 08:00:00:00 | 180 | 4.1% |
| 2026-06-18 09:00:00:00 | 193 | 4.4% |
| 2026-06-18 10:00:00:00 | 193 | 4.4% |
| 2026-06-18 11:00:00:00 | 180 | 4.1% |
| 2026-06-18 12:00:00:00 | 180 | 4.1% |
| 2026-06-18 13:00:00:00 | 180 | 4.1% |
| 2026-06-18 14:00:00:00 | 182 | 4.1% |
| 2026-06-18 15:00:00:00 | 180 | 4.1% |
| 2026-06-18 16:00:00:00 | 192 | 4.4% |
| 2026-06-18 17:00:00:00 | 186 | 4.2% |
| 2026-06-18 18:00:00:00 | 180 | 4.1% |
| 2026-06-18 19:00:00:00 | 180 | 4.1% |
| 2026-06-18 20:00:00:00 | 186 | 4.2% |
| 2026-06-18 21:00:00:00 | 180 | 4.1% |
| 2026-06-18 22:00:00:00 | 180 | 4.1% |
| 2026-06-18 23:00:00:00 | 197 | 4.5% |
| 2026-06-19 00:00:00:00 | 180 | 4.1% |
| 2026-06-19 01:00:00:00 | 181 | 4.1% |
| 2026-06-19 02:00:00:00 | 180 | 4.1% |
| 2026-06-19 03:00:00:00 | 184 | 4.2% |
| 2026-06-19 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Croydon, United Kingdom | 373 | 27.8% |
| 2 | Frankfurt am Main, Germany | 340 | 25.3% |
| 3 | Chengdu, China | 256 | 19.0% |
| 4 | Mátészalka, Hungary | 135 | 10.0% |
| 5 | Massy, France | 79 | 5.9% |
| 6 | Warrenton, United States | 67 | 5.0% |
| 7 | Dublin, United States | 40 | 3.0% |
| 8 | North Bergen, United States | 12 | 0.9% |
| 9 | Buenos Aires, Argentina | 12 | 0.9% |
| 10 | Amsterdam, Netherlands | 11 | 0.8% |
| 11 | Al Mansurah, Egypt | 10 | 0.7% |
| 12 | Piscataway, United States | 9 | 0.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `80.95.194.124` | 373 | 27.8% | United Kingdom / England / Croydon / ICUK Computing Services Limited | No apparent signal |
| 2 | `202.71.141.170` | 340 | 25.3% | Germany / Hesse / Frankfurt am Main / 1&1 Versatel Deutschland GmbH | No apparent signal |
| 3 | `119.5.213.182` | 256 | 19.0% | China / Sichuan / Chengdu / CNC Group CHINA169 Sichuan Province Network | No apparent signal |
| 4 | `78.92.227.234` | 135 | 10.0% | Hungary / Szabolcs-Szatmár-Bereg / Mátészalka / Magyar Telekom | No apparent signal |
| 5 | `216.180.246.30` | 79 | 5.9% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 6 | `92.204.138.187` | 67 | 5.0% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 7 | `206.189.225.77` | 12 | 0.9% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 8 | `151.101.218.13` | 12 | 0.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 9 | `93.123.72.183` | 11 | 0.8% | Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 10 | `3.131.24.55` | 10 | 0.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `81.10.69.33` | 10 | 0.7% | Egypt / Dakahlia / Al Mansurah / TE Data | No apparent signal |
| 12 | `18.189.74.1` | 10 | 0.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `18.221.179.104` | 10 | 0.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `18.190.15.50` | 10 | 0.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `172.93.106.153` | 9 | 0.7% | United States / New Jersey / Piscataway / Klemen Stirn | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.30` | 79 | 55.2% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `206.189.225.77` | 12 | 8.4% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 3 | `151.101.218.13` | 12 | 8.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `3.131.24.55` | 10 | 7.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.189.74.1` | 10 | 7.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `18.221.179.104` | 10 | 7.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `18.190.15.50` | 10 | 7.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
