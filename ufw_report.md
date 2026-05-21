# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4349
- Unique source IPs: 2301
- Unique countries/cities (24h): 376
- Unique destination ports: 2647

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 184 | 4.2% |
| 2 | `27015` | 98 | 2.3% |
| 3 | `22` | 40 | 0.9% |
| 4 | `5060` | 32 | 0.7% |
| 5 | `3389` | 32 | 0.7% |
| 6 | `53` | 27 | 0.6% |
| 7 | `8080` | 26 | 0.6% |
| 8 | `8000` | 23 | 0.5% |
| 9 | `8443` | 23 | 0.5% |
| 10 | `3306` | 20 | 0.5% |
| 11 | `1433` | 19 | 0.4% |
| 12 | `161` | 19 | 0.4% |
| 13 | `8333` | 16 | 0.4% |
| 14 | `25565` | 16 | 0.4% |
| 15 | `1900` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3840 | 88.3% |
| 2 | `UDP` | 501 | 11.5% |
| 3 | `47` | 6 | 0.1% |
| 4 | `41` | 1 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `77.90.185.235` | 562 | 12.9% |
| 2 | `216.180.246.163` | 85 | 2.0% |
| 3 | `43.228.157.8` | 20 | 0.5% |
| 4 | `139.59.214.194` | 19 | 0.4% |
| 5 | `170.84.212.53` | 18 | 0.4% |
| 6 | `151.101.218.73` | 17 | 0.4% |
| 7 | `166.62.124.255` | 14 | 0.3% |
| 8 | `178.62.97.244` | 14 | 0.3% |
| 9 | `69.17.52.1` | 13 | 0.3% |
| 10 | `204.76.203.15` | 13 | 0.3% |
| 11 | `134.195.101.206` | 13 | 0.3% |
| 12 | `118.139.164.140` | 13 | 0.3% |
| 13 | `52.20.198.190` | 12 | 0.3% |
| 14 | `3.131.24.55` | 12 | 0.3% |
| 15 | `18.217.208.51` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3740 | 97.4% |
| 2 | `ACK+FIN+PSH` | 46 | 1.2% |
| 3 | `ACK+PSH` | 31 | 0.8% |
| 4 | `ACK` | 9 | 0.2% |
| 5 | `SYN+ECE+CWR` | 8 | 0.2% |
| 6 | `ACK+FIN` | 5 | 0.1% |
| 7 | `ACK+FIN+PSH+CWR` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4343 | 99.9% |
| 2 | `wlan0` | 6 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `139.59.214.194` -> `23` | 19 | 0.4% |
| 2 | `170.84.212.53` -> `23` | 18 | 0.4% |
| 3 | `166.62.124.255` -> `23` | 14 | 0.3% |
| 4 | `178.62.97.244` -> `23` | 14 | 0.3% |
| 5 | `69.17.52.1` -> `8333` | 13 | 0.3% |
| 6 | `134.195.101.206` -> `23` | 13 | 0.3% |
| 7 | `118.139.164.140` -> `23` | 13 | 0.3% |
| 8 | `69.48.216.17` -> `43148` | 9 | 0.2% |
| 9 | `216.180.246.163` -> `56378` | 9 | 0.2% |
| 10 | `216.180.246.163` -> `17002` | 9 | 0.2% |
| 11 | `199.45.154.148` -> `8000` | 8 | 0.2% |
| 12 | `216.180.246.163` -> `8188` | 8 | 0.2% |
| 13 | `151.101.218.73` -> `33255` | 8 | 0.2% |
| 14 | `154.0.30.137` -> `3389` | 7 | 0.2% |
| 15 | `66.132.195.34` -> `161` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-20 04:00:00:00 | 123 | 2.8% |
| 2026-05-20 05:00:00:00 | 186 | 4.3% |
| 2026-05-20 06:00:00:00 | 181 | 4.2% |
| 2026-05-20 07:00:00:00 | 177 | 4.1% |
| 2026-05-20 08:00:00:00 | 173 | 4.0% |
| 2026-05-20 09:00:00:00 | 170 | 3.9% |
| 2026-05-20 10:00:00:00 | 182 | 4.2% |
| 2026-05-20 11:00:00:00 | 176 | 4.0% |
| 2026-05-20 12:00:00:00 | 183 | 4.2% |
| 2026-05-20 13:00:00:00 | 183 | 4.2% |
| 2026-05-20 14:00:00:00 | 183 | 4.2% |
| 2026-05-20 15:00:00:00 | 181 | 4.2% |
| 2026-05-20 16:00:00:00 | 181 | 4.2% |
| 2026-05-20 17:00:00:00 | 188 | 4.3% |
| 2026-05-20 18:00:00:00 | 184 | 4.2% |
| 2026-05-20 19:00:00:00 | 180 | 4.1% |
| 2026-05-20 20:00:00:00 | 180 | 4.1% |
| 2026-05-20 21:00:00:00 | 181 | 4.2% |
| 2026-05-20 22:00:00:00 | 182 | 4.2% |
| 2026-05-20 23:00:00:00 | 210 | 4.8% |
| 2026-05-21 00:00:00:00 | 180 | 4.1% |
| 2026-05-21 01:00:00:00 | 180 | 4.1% |
| 2026-05-21 02:00:00:00 | 181 | 4.2% |
| 2026-05-21 03:00:00:00 | 179 | 4.1% |
| 2026-05-21 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Augsburg, Germany | 562 | 67.1% |
| 2 | Massy, France | 85 | 10.2% |
| 3 | Singapore, Singapore | 33 | 3.9% |
| 4 | Dublin, United States | 24 | 2.9% |
| 5 | Frankfurt am Main, Germany | 19 | 2.3% |
| 6 | Rafaela, Argentina | 18 | 2.2% |
| 7 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 17 | 2.0% |
| 8 | Tempe, United States | 14 | 1.7% |
| 9 | Slough, United Kingdom | 14 | 1.7% |
| 10 | Lewes, United States | 13 | 1.6% |
| 11 | Eygelshoven, Netherlands | 13 | 1.6% |
| 12 | San Francisco, United States | 13 | 1.6% |
| 13 | Ashburn, United States | 12 | 1.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `77.90.185.235` | 562 | 67.1% | Germany / Bavaria / Augsburg / Inside Network LTD | No apparent signal |
| 2 | `216.180.246.163` | 85 | 10.2% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 3 | `43.228.157.8` | 20 | 2.4% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 4 | `139.59.214.194` | 19 | 2.3% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `170.84.212.53` | 18 | 2.2% | Argentina / Santa Fe / Rafaela / Wiltel Comunicaciones SA | Mobile/CGNAT (lte) |
| 6 | `151.101.218.73` | 17 | 2.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `166.62.124.255` | 14 | 1.7% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 8 | `178.62.97.244` | 14 | 1.7% | United Kingdom / England / Slough / Digital Ocean | Hosting/Cloud (digitalocean) |
| 9 | `69.17.52.1` | 13 | 1.6% | United States / Delaware / Lewes / Spruce Creek Networks LLC | No apparent signal |
| 10 | `204.76.203.15` | 13 | 1.6% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 11 | `134.195.101.206` | 13 | 1.6% | United States / California / San Francisco / Black Mesa Corporation | No apparent signal |
| 12 | `118.139.164.140` | 13 | 1.6% | Singapore / South West / Singapore / Godaddy.com | No apparent signal |
| 13 | `52.20.198.190` | 12 | 1.4% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 14 | `3.131.24.55` | 12 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `18.217.208.51` | 12 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.163` | 85 | 49.7% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `139.59.214.194` | 19 | 11.1% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |
| 3 | `151.101.218.73` | 17 | 9.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `178.62.97.244` | 14 | 8.2% | Hosting/Cloud (digitalocean) | United Kingdom / England / Slough / Digital Ocean |
| 5 | `52.20.198.190` | 12 | 7.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 6 | `3.131.24.55` | 12 | 7.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `18.217.208.51` | 12 | 7.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
