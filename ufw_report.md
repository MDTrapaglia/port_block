# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4432
- Unique source IPs: 2577
- Unique countries/cities (24h): 321
- Unique destination ports: 2631

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 118 | 2.7% |
| 2 | `22` | 55 | 1.2% |
| 3 | `8080` | 47 | 1.1% |
| 4 | `unknown` | 40 | 0.9% |
| 5 | `1433` | 27 | 0.6% |
| 6 | `8443` | 27 | 0.6% |
| 7 | `5060` | 26 | 0.6% |
| 8 | `3389` | 23 | 0.5% |
| 9 | `27015` | 21 | 0.5% |
| 10 | `8081` | 21 | 0.5% |
| 11 | `53` | 20 | 0.5% |
| 12 | `8000` | 18 | 0.4% |
| 13 | `1900` | 16 | 0.4% |
| 14 | `3306` | 16 | 0.4% |
| 15 | `4000` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3898 | 88.0% |
| 2 | `UDP` | 494 | 11.1% |
| 3 | `47` | 38 | 0.9% |
| 4 | `41` | 1 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `62.210.142.177` | 182 | 4.1% |
| 2 | `8.219.12.186` | 28 | 0.6% |
| 3 | `208.109.189.59` | 21 | 0.5% |
| 4 | `85.217.149.49` | 18 | 0.4% |
| 5 | `85.217.149.17` | 17 | 0.4% |
| 6 | `151.101.217.44` | 16 | 0.4% |
| 7 | `93.123.72.183` | 15 | 0.3% |
| 8 | `198.12.150.45` | 14 | 0.3% |
| 9 | `35.169.206.177` | 13 | 0.3% |
| 10 | `151.101.218.13` | 12 | 0.3% |
| 11 | `204.76.203.15` | 12 | 0.3% |
| 12 | `85.217.149.48` | 12 | 0.3% |
| 13 | `104.19.220.32` | 12 | 0.3% |
| 14 | `85.217.149.52` | 11 | 0.2% |
| 15 | `142.251.129.174` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3688 | 94.6% |
| 2 | `ACK+FIN+PSH` | 92 | 2.4% |
| 3 | `ACK+PSH` | 88 | 2.3% |
| 4 | `ACK+FIN` | 12 | 0.3% |
| 5 | `ACK` | 8 | 0.2% |
| 6 | `SYN+ECE+CWR` | 6 | 0.2% |
| 7 | `ACK+RST` | 3 | 0.1% |
| 8 | `ACK+FIN+PSH+CWR` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4427 | 99.9% |
| 2 | `wlan0` | 5 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `8.219.12.186` -> `23` | 28 | 0.6% |
| 2 | `208.109.189.59` -> `23` | 21 | 0.5% |
| 3 | `198.12.150.45` -> `23` | 14 | 0.3% |
| 4 | `94.156.152.50` -> `23` | 9 | 0.2% |
| 5 | `62.210.142.177` -> `3333` | 9 | 0.2% |
| 6 | `62.210.142.177` -> `4007` | 9 | 0.2% |
| 7 | `69.17.52.1` -> `8333` | 8 | 0.2% |
| 8 | `62.210.142.177` -> `3304` | 8 | 0.2% |
| 9 | `62.210.142.177` -> `3337` | 8 | 0.2% |
| 10 | `62.210.142.177` -> `3400` | 8 | 0.2% |
| 11 | `62.210.142.177` -> `4000` | 8 | 0.2% |
| 12 | `62.210.142.177` -> `4002` | 8 | 0.2% |
| 13 | `62.210.142.177` -> `4006` | 8 | 0.2% |
| 14 | `62.210.142.177` -> `4222` | 8 | 0.2% |
| 15 | `178.20.210.152` -> `1723` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-25 04:00:00:00 | 134 | 3.0% |
| 2026-06-25 05:00:00:00 | 192 | 4.3% |
| 2026-06-25 06:00:00:00 | 183 | 4.1% |
| 2026-06-25 07:00:00:00 | 179 | 4.0% |
| 2026-06-25 08:00:00:00 | 181 | 4.1% |
| 2026-06-25 09:00:00:00 | 180 | 4.1% |
| 2026-06-25 10:00:00:00 | 182 | 4.1% |
| 2026-06-25 11:00:00:00 | 178 | 4.0% |
| 2026-06-25 12:00:00:00 | 181 | 4.1% |
| 2026-06-25 13:00:00:00 | 181 | 4.1% |
| 2026-06-25 14:00:00:00 | 210 | 4.7% |
| 2026-06-25 15:00:00:00 | 190 | 4.3% |
| 2026-06-25 16:00:00:00 | 179 | 4.0% |
| 2026-06-25 17:00:00:00 | 190 | 4.3% |
| 2026-06-25 18:00:00:00 | 181 | 4.1% |
| 2026-06-25 19:00:00:00 | 181 | 4.1% |
| 2026-06-25 20:00:00:00 | 178 | 4.0% |
| 2026-06-25 21:00:00:00 | 182 | 4.1% |
| 2026-06-25 22:00:00:00 | 180 | 4.1% |
| 2026-06-25 23:00:00:00 | 212 | 4.8% |
| 2026-06-26 00:00:00:00 | 191 | 4.3% |
| 2026-06-26 01:00:00:00 | 180 | 4.1% |
| 2026-06-26 02:00:00:00 | 182 | 4.1% |
| 2026-06-26 03:00:00:00 | 181 | 4.1% |
| 2026-06-26 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Paris, France | 182 | 46.2% |
| 2 | Beauharnois, Canada | 41 | 10.4% |
| 3 | Tempe, United States | 35 | 8.9% |
| 4 | Singapore, Singapore | 28 | 7.1% |
| 5 | Buenos Aires, Argentina | 28 | 7.1% |
| 6 | New York, United States | 17 | 4.3% |
| 7 | Amsterdam, Netherlands | 15 | 3.8% |
| 8 | Ashburn, United States | 13 | 3.3% |
| 9 | Eygelshoven, Netherlands | 12 | 3.0% |
| 10 | Toronto, Canada | 12 | 3.0% |
| 11 | São Paulo, Brazil | 11 | 2.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.177` | 182 | 46.2% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 2 | `8.219.12.186` | 28 | 7.1% | Singapore / North West / Singapore / Alibaba.com Singapore E-Commerce Private Limited | Hosting/Cloud (alibaba) |
| 3 | `208.109.189.59` | 21 | 5.3% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 4 | `85.217.149.49` | 18 | 4.6% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 5 | `85.217.149.17` | 17 | 4.3% | United States / New York / New York / Modat B.V | No apparent signal |
| 6 | `151.101.217.44` | 16 | 4.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `93.123.72.183` | 15 | 3.8% | Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 8 | `198.12.150.45` | 14 | 3.6% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 9 | `35.169.206.177` | 13 | 3.3% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 10 | `151.101.218.13` | 12 | 3.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 11 | `204.76.203.15` | 12 | 3.0% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 12 | `85.217.149.48` | 12 | 3.0% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 13 | `104.19.220.32` | 12 | 3.0% | Canada / Ontario / Toronto / Cloudflare, Inc. | CDN/Edge (cloudflare) |
| 14 | `85.217.149.52` | 11 | 2.8% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 15 | `142.251.129.174` | 11 | 2.8% | Brazil / São Paulo / São Paulo / Google LLC | Hosting/Cloud (google llc) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.177` | 182 | 66.4% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `8.219.12.186` | 28 | 10.2% | Hosting/Cloud (alibaba) | Singapore / North West / Singapore / Alibaba.com Singapore E-Commerce Private Limited |
| 3 | `151.101.217.44` | 16 | 5.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `35.169.206.177` | 13 | 4.7% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `151.101.218.13` | 12 | 4.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 6 | `104.19.220.32` | 12 | 4.4% | CDN/Edge (cloudflare) | Canada / Ontario / Toronto / Cloudflare, Inc. |
| 7 | `142.251.129.174` | 11 | 4.0% | Hosting/Cloud (google llc) | Brazil / São Paulo / São Paulo / Google LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
