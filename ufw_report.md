# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4394
- Unique source IPs: 2768
- Unique countries/cities (24h): 333
- Unique destination ports: 2735

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 111 | 2.5% |
| 2 | `8080` | 60 | 1.4% |
| 3 | `27015` | 59 | 1.3% |
| 4 | `3389` | 39 | 0.9% |
| 5 | `22` | 36 | 0.8% |
| 6 | `5060` | 32 | 0.7% |
| 7 | `8443` | 21 | 0.5% |
| 8 | `1433` | 20 | 0.5% |
| 9 | `53` | 20 | 0.5% |
| 10 | `25` | 19 | 0.4% |
| 11 | `8000` | 19 | 0.4% |
| 12 | `3306` | 19 | 0.4% |
| 13 | `1900` | 18 | 0.4% |
| 14 | `123` | 17 | 0.4% |
| 15 | `389` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3891 | 88.6% |
| 2 | `UDP` | 495 | 11.3% |
| 3 | `47` | 5 | 0.1% |
| 4 | `4` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `176.65.139.117` | 21 | 0.5% |
| 2 | `138.226.239.21` | 18 | 0.4% |
| 3 | `77.91.71.66` | 17 | 0.4% |
| 4 | `208.109.244.195` | 17 | 0.4% |
| 5 | `5.187.35.142` | 16 | 0.4% |
| 6 | `208.109.212.211` | 16 | 0.4% |
| 7 | `77.91.71.67` | 15 | 0.3% |
| 8 | `13.59.96.40` | 15 | 0.3% |
| 9 | `138.226.239.22` | 14 | 0.3% |
| 10 | `100.50.17.159` | 12 | 0.3% |
| 11 | `18.221.179.104` | 12 | 0.3% |
| 12 | `185.136.15.77` | 12 | 0.3% |
| 13 | `151.101.218.73` | 12 | 0.3% |
| 14 | `100.49.117.77` | 11 | 0.3% |
| 15 | `3.131.24.55` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3762 | 96.7% |
| 2 | `ACK+FIN+PSH` | 66 | 1.7% |
| 3 | `ACK+PSH` | 46 | 1.2% |
| 4 | `SYN+ECE+CWR` | 6 | 0.2% |
| 5 | `ACK` | 6 | 0.2% |
| 6 | `ACK+FIN` | 5 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4392 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `176.65.139.117` -> `8080` | 21 | 0.5% |
| 2 | `208.109.244.195` -> `23` | 17 | 0.4% |
| 3 | `208.109.212.211` -> `23` | 16 | 0.4% |
| 4 | `138.226.239.21` -> `3389` | 10 | 0.2% |
| 5 | `69.17.52.1` -> `8333` | 8 | 0.2% |
| 6 | `2.23.164.116` -> `5979` | 8 | 0.2% |
| 7 | `151.101.218.73` -> `4631` | 7 | 0.2% |
| 8 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 9 | `66.132.195.117` -> `7070` | 5 | 0.1% |
| 10 | `13.59.96.40` -> `57178` | 5 | 0.1% |
| 11 | `13.59.96.40` -> `57172` | 5 | 0.1% |
| 12 | `205.200.179.20` -> `23` | 5 | 0.1% |
| 13 | `199.45.155.74` -> `25` | 4 | 0.1% |
| 14 | `87.251.64.157` -> `9022` | 4 | 0.1% |
| 15 | `45.198.224.18` -> `8728` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-29 04:00:00:00 | 135 | 3.1% |
| 2026-05-29 05:00:00:00 | 181 | 4.1% |
| 2026-05-29 06:00:00:00 | 180 | 4.1% |
| 2026-05-29 07:00:00:00 | 182 | 4.1% |
| 2026-05-29 08:00:00:00 | 178 | 4.1% |
| 2026-05-29 09:00:00:00 | 177 | 4.0% |
| 2026-05-29 10:00:00:00 | 188 | 4.3% |
| 2026-05-29 11:00:00:00 | 182 | 4.1% |
| 2026-05-29 12:00:00:00 | 180 | 4.1% |
| 2026-05-29 13:00:00:00 | 185 | 4.2% |
| 2026-05-29 14:00:00:00 | 194 | 4.4% |
| 2026-05-29 15:00:00:00 | 181 | 4.1% |
| 2026-05-29 16:00:00:00 | 179 | 4.1% |
| 2026-05-29 17:00:00:00 | 181 | 4.1% |
| 2026-05-29 18:00:00:00 | 191 | 4.3% |
| 2026-05-29 19:00:00:00 | 180 | 4.1% |
| 2026-05-29 20:00:00:00 | 181 | 4.1% |
| 2026-05-29 21:00:00:00 | 181 | 4.1% |
| 2026-05-29 22:00:00:00 | 191 | 4.3% |
| 2026-05-29 23:00:00:00 | 185 | 4.2% |
| 2026-05-30 00:00:00:00 | 180 | 4.1% |
| 2026-05-30 01:00:00:00 | 194 | 4.4% |
| 2026-05-30 02:00:00:00 | 183 | 4.2% |
| 2026-05-30 03:00:00:00 | 177 | 4.0% |
| 2026-05-30 04:00:00:00 | 48 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dublin, United States | 38 | 17.4% |
| 2 | Tempe, United States | 33 | 15.1% |
| 3 | Port Vila, Vanuatu | 32 | 14.6% |
| 4 | Jerusalem, Israel | 32 | 14.6% |
| 5 | Ashburn, United States | 23 | 10.5% |
| 6 | Eygelshoven, The Netherlands | 21 | 9.6% |
| 7 | Amsterdam, The Netherlands | 16 | 7.3% |
| 8 | Almaty, Kazakhstan | 12 | 5.5% |
| 9 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 12 | 5.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `176.65.139.117` | 21 | 9.6% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 2 | `138.226.239.21` | 18 | 8.2% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 3 | `77.91.71.66` | 17 | 7.8% | Israel / Jerusalem / Jerusalem / Proline IT Ltd | No apparent signal |
| 4 | `208.109.244.195` | 17 | 7.8% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 5 | `5.187.35.142` | 16 | 7.3% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 6 | `208.109.212.211` | 16 | 7.3% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 7 | `77.91.71.67` | 15 | 6.8% | Israel / Jerusalem / Jerusalem / Proline IT Ltd | No apparent signal |
| 8 | `13.59.96.40` | 15 | 6.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `138.226.239.22` | 14 | 6.4% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 10 | `100.50.17.159` | 12 | 5.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 11 | `18.221.179.104` | 12 | 5.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `185.136.15.77` | 12 | 5.5% | Kazakhstan / Almaty / Almaty / net | No apparent signal |
| 13 | `151.101.218.73` | 12 | 5.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 14 | `100.49.117.77` | 11 | 5.0% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `3.131.24.55` | 11 | 5.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `13.59.96.40` | 15 | 20.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 2 | `100.50.17.159` | 12 | 16.4% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 3 | `18.221.179.104` | 12 | 16.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `151.101.218.73` | 12 | 16.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `100.49.117.77` | 11 | 15.1% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 6 | `3.131.24.55` | 11 | 15.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
