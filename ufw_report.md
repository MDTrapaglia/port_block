# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4455
- Unique source IPs: 2408
- Unique countries/cities (24h): 388
- Unique destination ports: 2282

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 949 | 21.3% |
| 2 | `22` | 41 | 0.9% |
| 3 | `5060` | 34 | 0.8% |
| 4 | `8080` | 32 | 0.7% |
| 5 | `53` | 25 | 0.6% |
| 6 | `unknown` | 19 | 0.4% |
| 7 | `2087` | 17 | 0.4% |
| 8 | `1900` | 15 | 0.3% |
| 9 | `8081` | 15 | 0.3% |
| 10 | `8443` | 14 | 0.3% |
| 11 | `3389` | 13 | 0.3% |
| 12 | `8728` | 13 | 0.3% |
| 13 | `8082` | 12 | 0.3% |
| 14 | `25` | 12 | 0.3% |
| 15 | `3000` | 11 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4051 | 90.9% |
| 2 | `UDP` | 385 | 8.6% |
| 3 | `47` | 18 | 0.4% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `35.222.192.22` | 159 | 3.6% |
| 2 | `172.93.102.19` | 132 | 3.0% |
| 3 | `198.50.125.139` | 93 | 2.1% |
| 4 | `209.145.51.211` | 66 | 1.5% |
| 5 | `80.251.153.178` | 60 | 1.3% |
| 6 | `151.101.218.73` | 36 | 0.8% |
| 7 | `35.212.204.23` | 28 | 0.6% |
| 8 | `154.12.252.160` | 24 | 0.5% |
| 9 | `189.90.139.126` | 24 | 0.5% |
| 10 | `43.228.157.49` | 23 | 0.5% |
| 11 | `50.6.8.71` | 22 | 0.5% |
| 12 | `85.217.149.15` | 15 | 0.3% |
| 13 | `85.217.149.34` | 15 | 0.3% |
| 14 | `103.191.218.186` | 15 | 0.3% |
| 15 | `85.217.149.17` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3856 | 95.2% |
| 2 | `ACK+FIN+PSH` | 107 | 2.6% |
| 3 | `ACK+PSH` | 54 | 1.3% |
| 4 | `ACK+FIN` | 24 | 0.6% |
| 5 | `ACK` | 7 | 0.2% |
| 6 | `SYN+ECE+CWR` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4450 | 99.9% |
| 2 | `wlan0` | 5 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `35.222.192.22` -> `23` | 159 | 3.6% |
| 2 | `172.93.102.19` -> `23` | 132 | 3.0% |
| 3 | `198.50.125.139` -> `23` | 93 | 2.1% |
| 4 | `209.145.51.211` -> `23` | 66 | 1.5% |
| 5 | `80.251.153.178` -> `23` | 60 | 1.3% |
| 6 | `154.12.252.160` -> `23` | 24 | 0.5% |
| 7 | `189.90.139.126` -> `23` | 24 | 0.5% |
| 8 | `43.228.157.49` -> `23` | 23 | 0.5% |
| 9 | `50.6.8.71` -> `23` | 22 | 0.5% |
| 10 | `103.191.218.186` -> `23` | 15 | 0.3% |
| 11 | `154.12.237.150` -> `23` | 12 | 0.3% |
| 12 | `45.32.155.55` -> `23` | 11 | 0.2% |
| 13 | `147.182.240.221` -> `23` | 11 | 0.2% |
| 14 | `144.202.39.74` -> `23` | 11 | 0.2% |
| 15 | `193.226.169.5` -> `23` | 9 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-01 04:00:00:00 | 135 | 3.0% |
| 2026-05-01 05:00:00:00 | 179 | 4.0% |
| 2026-05-01 06:00:00:00 | 179 | 4.0% |
| 2026-05-01 07:00:00:00 | 182 | 4.1% |
| 2026-05-01 08:00:00:00 | 179 | 4.0% |
| 2026-05-01 09:00:00:00 | 178 | 4.0% |
| 2026-05-01 10:00:00:00 | 199 | 4.5% |
| 2026-05-01 11:00:00:00 | 187 | 4.2% |
| 2026-05-01 12:00:00:00 | 179 | 4.0% |
| 2026-05-01 13:00:00:00 | 181 | 4.1% |
| 2026-05-01 14:00:00:00 | 178 | 4.0% |
| 2026-05-01 15:00:00:00 | 220 | 4.9% |
| 2026-05-01 16:00:00:00 | 192 | 4.3% |
| 2026-05-01 17:00:00:00 | 178 | 4.0% |
| 2026-05-01 18:00:00:00 | 182 | 4.1% |
| 2026-05-01 19:00:00:00 | 180 | 4.0% |
| 2026-05-01 20:00:00:00 | 180 | 4.0% |
| 2026-05-01 21:00:00:00 | 179 | 4.0% |
| 2026-05-01 22:00:00:00 | 181 | 4.1% |
| 2026-05-01 23:00:00:00 | 192 | 4.3% |
| 2026-05-02 00:00:00:00 | 190 | 4.3% |
| 2026-05-02 01:00:00:00 | 184 | 4.1% |
| 2026-05-02 02:00:00:00 | 197 | 4.4% |
| 2026-05-02 03:00:00:00 | 199 | 4.5% |
| 2026-05-02 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Council Bluffs, United States | 159 | 21.9% |
| 2 | Piscataway, United States | 132 | 18.2% |
| 3 | Montreal, Canada | 93 | 12.8% |
| 4 | St Louis, United States | 90 | 12.4% |
| 5 | Amsterdam, Netherlands | 60 | 8.3% |
| 6 | New York, United States | 44 | 6.1% |
| 7 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 36 | 5.0% |
| 8 | The Dalles, United States | 28 | 3.9% |
| 9 | Franca, Brazil | 24 | 3.3% |
| 10 | Singapore, Singapore | 23 | 3.2% |
| 11 | Ashburn, United States | 22 | 3.0% |
| 12 | Kuningan, Indonesia | 15 | 2.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `35.222.192.22` | 159 | 21.9% | United States / Iowa / Council Bluffs / Google Cloud (us-central1) | Hosting/Cloud (google cloud) |
| 2 | `172.93.102.19` | 132 | 18.2% | United States / New Jersey / Piscataway / Dan Thompson | No apparent signal |
| 3 | `198.50.125.139` | 93 | 12.8% | Canada / Quebec / Montreal / iWeb Technologies Inc | Hosting/Cloud (leaseweb) |
| 4 | `209.145.51.211` | 66 | 9.1% | United States / Missouri / St Louis / Contabo Inc | Hosting/Cloud (contabo) |
| 5 | `80.251.153.178` | 60 | 8.3% | Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 6 | `151.101.218.73` | 36 | 5.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `35.212.204.23` | 28 | 3.9% | United States / Oregon / The Dalles / Google Cloud (us-west1) | Hosting/Cloud (google cloud) |
| 8 | `154.12.252.160` | 24 | 3.3% | United States / Missouri / St Louis / Contabo Inc | Hosting/Cloud (contabo) |
| 9 | `189.90.139.126` | 24 | 3.3% | Brazil / São Paulo / Franca / Com4 Data Center Ltda | Hosting/Cloud (data center) |
| 10 | `43.228.157.49` | 23 | 3.2% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 11 | `50.6.8.71` | 22 | 3.0% | United States / Virginia / Ashburn / Newfold Digital, Inc | No apparent signal |
| 12 | `85.217.149.15` | 15 | 2.1% | United States / New York / New York / Modat B.V | No apparent signal |
| 13 | `85.217.149.34` | 15 | 2.1% | United States / New York / New York / Modat B.V | No apparent signal |
| 14 | `103.191.218.186` | 15 | 2.1% | Indonesia / West Java / Kuningan / PT Replay Inti Media | No apparent signal |
| 15 | `85.217.149.17` | 14 | 1.9% | United States / New York / New York / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `35.222.192.22` | 159 | 37.0% | Hosting/Cloud (google cloud) | United States / Iowa / Council Bluffs / Google Cloud (us-central1) |
| 2 | `198.50.125.139` | 93 | 21.6% | Hosting/Cloud (leaseweb) | Canada / Quebec / Montreal / iWeb Technologies Inc |
| 3 | `209.145.51.211` | 66 | 15.3% | Hosting/Cloud (contabo) | United States / Missouri / St Louis / Contabo Inc |
| 4 | `151.101.218.73` | 36 | 8.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `35.212.204.23` | 28 | 6.5% | Hosting/Cloud (google cloud) | United States / Oregon / The Dalles / Google Cloud (us-west1) |
| 6 | `154.12.252.160` | 24 | 5.6% | Hosting/Cloud (contabo) | United States / Missouri / St Louis / Contabo Inc |
| 7 | `189.90.139.126` | 24 | 5.6% | Hosting/Cloud (data center) | Brazil / São Paulo / Franca / Com4 Data Center Ltda |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
