# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4439
- Unique source IPs: 2493
- Unique countries/cities (24h): 354
- Unique destination ports: 2406

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 832 | 18.7% |
| 2 | `8080` | 38 | 0.9% |
| 3 | `22` | 37 | 0.8% |
| 4 | `unknown` | 37 | 0.8% |
| 5 | `27015` | 25 | 0.6% |
| 6 | `8000` | 18 | 0.4% |
| 7 | `3389` | 18 | 0.4% |
| 8 | `1433` | 17 | 0.4% |
| 9 | `5060` | 17 | 0.4% |
| 10 | `8443` | 15 | 0.3% |
| 11 | `389` | 15 | 0.3% |
| 12 | `8081` | 14 | 0.3% |
| 13 | `81` | 12 | 0.3% |
| 14 | `8085` | 12 | 0.3% |
| 15 | `8333` | 12 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3996 | 90.0% |
| 2 | `UDP` | 406 | 9.1% |
| 3 | `47` | 37 | 0.8% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `89.31.120.238` | 229 | 5.2% |
| 2 | `196.189.69.192` | 132 | 3.0% |
| 3 | `223.151.252.40` | 110 | 2.5% |
| 4 | `59.180.144.78` | 97 | 2.2% |
| 5 | `159.223.62.234` | 45 | 1.0% |
| 6 | `59.180.143.72` | 26 | 0.6% |
| 7 | `117.251.194.245` | 25 | 0.6% |
| 8 | `5.83.143.41` | 25 | 0.6% |
| 9 | `85.217.149.52` | 21 | 0.5% |
| 10 | `85.217.149.48` | 19 | 0.4% |
| 11 | `85.217.149.49` | 16 | 0.4% |
| 12 | `206.0.186.204` | 16 | 0.4% |
| 13 | `151.101.217.44` | 14 | 0.3% |
| 14 | `35.169.206.177` | 12 | 0.3% |
| 15 | `104.36.113.23` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3803 | 95.2% |
| 2 | `ACK+FIN+PSH` | 89 | 2.2% |
| 3 | `ACK+PSH` | 72 | 1.8% |
| 4 | `ACK+FIN` | 20 | 0.5% |
| 5 | `ACK+RST` | 5 | 0.1% |
| 6 | `SYN+ECE+CWR` | 5 | 0.1% |
| 7 | `ACK` | 1 | 0.0% |
| 8 | `RST` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4435 | 99.9% |
| 2 | `wlan0` | 4 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `196.189.69.192` -> `23` | 132 | 3.0% |
| 2 | `223.151.252.40` -> `23` | 110 | 2.5% |
| 3 | `59.180.144.78` -> `23` | 97 | 2.2% |
| 4 | `59.180.143.72` -> `23` | 26 | 0.6% |
| 5 | `117.251.194.245` -> `23` | 25 | 0.6% |
| 6 | `206.0.186.204` -> `23` | 16 | 0.4% |
| 7 | `206.0.169.233` -> `23` | 10 | 0.2% |
| 8 | `69.17.52.1` -> `8333` | 9 | 0.2% |
| 9 | `151.101.217.91` -> `59092` | 8 | 0.2% |
| 10 | `5.61.209.43` -> `8080` | 8 | 0.2% |
| 11 | `204.237.133.243` -> `43168` | 7 | 0.2% |
| 12 | `151.101.217.44` -> `40088` | 7 | 0.2% |
| 13 | `8.28.7.82` -> `41580` | 6 | 0.1% |
| 14 | `52.88.236.22` -> `45444` | 6 | 0.1% |
| 15 | `104.36.113.23` -> `57726` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-26 04:00:00:00 | 132 | 3.0% |
| 2026-06-26 05:00:00:00 | 181 | 4.1% |
| 2026-06-26 06:00:00:00 | 182 | 4.1% |
| 2026-06-26 07:00:00:00 | 180 | 4.1% |
| 2026-06-26 08:00:00:00 | 202 | 4.6% |
| 2026-06-26 09:00:00:00 | 180 | 4.1% |
| 2026-06-26 10:00:00:00 | 180 | 4.1% |
| 2026-06-26 11:00:00:00 | 179 | 4.0% |
| 2026-06-26 12:00:00:00 | 181 | 4.1% |
| 2026-06-26 13:00:00:00 | 180 | 4.1% |
| 2026-06-26 14:00:00:00 | 183 | 4.1% |
| 2026-06-26 15:00:00:00 | 246 | 5.5% |
| 2026-06-26 16:00:00:00 | 179 | 4.0% |
| 2026-06-26 17:00:00:00 | 180 | 4.1% |
| 2026-06-26 18:00:00:00 | 180 | 4.1% |
| 2026-06-26 19:00:00:00 | 180 | 4.1% |
| 2026-06-26 20:00:00:00 | 180 | 4.1% |
| 2026-06-26 21:00:00:00 | 180 | 4.1% |
| 2026-06-26 22:00:00:00 | 180 | 4.1% |
| 2026-06-26 23:00:00:00 | 180 | 4.1% |
| 2026-06-27 00:00:00:00 | 207 | 4.7% |
| 2026-06-27 01:00:00:00 | 180 | 4.1% |
| 2026-06-27 02:00:00:00 | 182 | 4.1% |
| 2026-06-27 03:00:00:00 | 179 | 4.0% |
| 2026-06-27 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dubai, United Arab Emirates | 229 | 28.7% |
| 2 | Addis Ababa, Ethiopia | 132 | 16.5% |
| 3 | Qingyuan, China | 110 | 13.8% |
| 4 | Delhi, India | 97 | 12.1% |
| 5 | Beauharnois, Canada | 56 | 7.0% |
| 6 | Singapore, Singapore | 45 | 5.6% |
| 7 | New Delhi, India | 26 | 3.3% |
| 8 | Bhubaneswar, India | 25 | 3.1% |
| 9 | Amsterdam, The Netherlands | 25 | 3.1% |
| 10 | Cabimas, Venezuela | 16 | 2.0% |
| 11 | Buenos Aires, Argentina | 14 | 1.8% |
| 12 | Ashburn, United States | 12 | 1.5% |
| 13 | Redwood City, United States | 12 | 1.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `89.31.120.238` | 229 | 28.7% | United Arab Emirates / Dubai / Dubai / EDIS GmbH | VPN/Proxy suspected (m247) |
| 2 | `196.189.69.192` | 132 | 16.5% | Ethiopia / Addis Ababa / Addis Ababa / Ethiotelecom | VPN/Proxy suspected (pia) |
| 3 | `223.151.252.40` | 110 | 13.8% | China / Hunan / Qingyuan / Chinanet HN | No apparent signal |
| 4 | `59.180.144.78` | 97 | 12.1% | India / National Capital Territory of Delhi / Delhi / MTNL Mumbai | No apparent signal |
| 5 | `159.223.62.234` | 45 | 5.6% | Singapore / South West / Singapore / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 6 | `59.180.143.72` | 26 | 3.3% | India / National Capital Territory of Delhi / New Delhi / MTNL Mumbai | No apparent signal |
| 7 | `117.251.194.245` | 25 | 3.1% | India / Odisha / Bhubaneswar / BSNL Internet | No apparent signal |
| 8 | `5.83.143.41` | 25 | 3.1% | The Netherlands / North Holland / Amsterdam / Joel Krause | No apparent signal |
| 9 | `85.217.149.52` | 21 | 2.6% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 10 | `85.217.149.48` | 19 | 2.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 11 | `85.217.149.49` | 16 | 2.0% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 12 | `206.0.186.204` | 16 | 2.0% | Venezuela / Zulia / Cabimas / Colnetwork C.A | No apparent signal |
| 13 | `151.101.217.44` | 14 | 1.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 14 | `35.169.206.177` | 12 | 1.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `104.36.113.23` | 12 | 1.5% | United States / California / Redwood City / PubMatic, Inc. | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `89.31.120.238` | 229 | 53.0% | VPN/Proxy suspected (m247) | United Arab Emirates / Dubai / Dubai / EDIS GmbH |
| 2 | `196.189.69.192` | 132 | 30.6% | VPN/Proxy suspected (pia) | Ethiopia / Addis Ababa / Addis Ababa / Ethiotelecom |
| 3 | `159.223.62.234` | 45 | 10.4% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / DigitalOcean, LLC |
| 4 | `151.101.217.44` | 14 | 3.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `35.169.206.177` | 12 | 2.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
