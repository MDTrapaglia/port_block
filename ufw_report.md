# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4408
- Unique source IPs: 2403
- Unique countries/cities (24h): 394
- Unique destination ports: 2283

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 536 | 12.2% |
| 2 | `22` | 43 | 1.0% |
| 3 | `5060` | 40 | 0.9% |
| 4 | `8080` | 28 | 0.6% |
| 5 | `53` | 26 | 0.6% |
| 6 | `3389` | 23 | 0.5% |
| 7 | `1433` | 23 | 0.5% |
| 8 | `389` | 20 | 0.5% |
| 9 | `123` | 18 | 0.4% |
| 10 | `8443` | 18 | 0.4% |
| 11 | `10001` | 17 | 0.4% |
| 12 | `5432` | 17 | 0.4% |
| 13 | `2375` | 17 | 0.4% |
| 14 | `8333` | 16 | 0.4% |
| 15 | `161` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3930 | 89.2% |
| 2 | `UDP` | 464 | 10.5% |
| 3 | `47` | 13 | 0.3% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `31.220.3.165` | 213 | 4.8% |
| 2 | `143.198.198.33` | 82 | 1.9% |
| 3 | `45.9.149.154` | 37 | 0.8% |
| 4 | `196.242.141.12` | 28 | 0.6% |
| 5 | `185.48.32.227` | 23 | 0.5% |
| 6 | `45.9.149.219` | 23 | 0.5% |
| 7 | `159.65.20.241` | 21 | 0.5% |
| 8 | `85.217.149.20` | 15 | 0.3% |
| 9 | `45.153.34.160` | 15 | 0.3% |
| 10 | `3.128.64.243` | 15 | 0.3% |
| 11 | `204.76.203.15` | 14 | 0.3% |
| 12 | `85.217.149.49` | 13 | 0.3% |
| 13 | `3.131.24.55` | 12 | 0.3% |
| 14 | `51.159.110.167` | 12 | 0.3% |
| 15 | `69.17.52.1` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3766 | 95.8% |
| 2 | `ACK+FIN+PSH` | 74 | 1.9% |
| 3 | `ACK+PSH` | 64 | 1.6% |
| 4 | `ACK` | 17 | 0.4% |
| 5 | `SYN+ECE+CWR` | 8 | 0.2% |
| 6 | `ACK+FIN` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4395 | 99.7% |
| 2 | `wlan0` | 13 | 0.3% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `31.220.3.165` -> `23` | 213 | 4.8% |
| 2 | `143.198.198.33` -> `23` | 82 | 1.9% |
| 3 | `185.48.32.227` -> `23` | 23 | 0.5% |
| 4 | `159.65.20.241` -> `23` | 21 | 0.5% |
| 5 | `69.17.52.1` -> `8333` | 12 | 0.3% |
| 6 | `216.180.246.186` -> `53` | 10 | 0.2% |
| 7 | `54.203.116.214` -> `3265` | 10 | 0.2% |
| 8 | `176.65.139.177` -> `9034` | 9 | 0.2% |
| 9 | `192.168.100.117` -> `8613` | 8 | 0.2% |
| 10 | `45.148.121.166` -> `23` | 8 | 0.2% |
| 11 | `23.64.58.134` -> `9227` | 6 | 0.1% |
| 12 | `66.132.186.165` -> `8032` | 5 | 0.1% |
| 13 | `178.20.210.152` -> `8728` | 5 | 0.1% |
| 14 | `44.221.182.210` -> `59726` | 5 | 0.1% |
| 15 | `192.168.100.1` -> `68` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-13 04:00:00:00 | 137 | 3.1% |
| 2026-05-13 05:00:00:00 | 178 | 4.0% |
| 2026-05-13 06:00:00:00 | 183 | 4.2% |
| 2026-05-13 07:00:00:00 | 179 | 4.1% |
| 2026-05-13 08:00:00:00 | 185 | 4.2% |
| 2026-05-13 09:00:00:00 | 175 | 4.0% |
| 2026-05-13 10:00:00:00 | 182 | 4.1% |
| 2026-05-13 11:00:00:00 | 176 | 4.0% |
| 2026-05-13 12:00:00:00 | 198 | 4.5% |
| 2026-05-13 13:00:00:00 | 175 | 4.0% |
| 2026-05-13 14:00:00:00 | 197 | 4.5% |
| 2026-05-13 15:00:00:00 | 180 | 4.1% |
| 2026-05-13 16:00:00:00 | 185 | 4.2% |
| 2026-05-13 17:00:00:00 | 180 | 4.1% |
| 2026-05-13 18:00:00:00 | 190 | 4.3% |
| 2026-05-13 19:00:00:00 | 180 | 4.1% |
| 2026-05-13 20:00:00:00 | 181 | 4.1% |
| 2026-05-13 21:00:00:00 | 181 | 4.1% |
| 2026-05-13 22:00:00:00 | 186 | 4.2% |
| 2026-05-13 23:00:00:00 | 201 | 4.6% |
| 2026-05-14 00:00:00:00 | 193 | 4.4% |
| 2026-05-14 01:00:00:00 | 180 | 4.1% |
| 2026-05-14 02:00:00:00 | 180 | 4.1% |
| 2026-05-14 03:00:00:00 | 180 | 4.1% |
| 2026-05-14 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 213 | 39.8% |
| 2 | Singapore, Singapore | 82 | 15.3% |
| 3 | Amsterdam, Netherlands | 60 | 11.2% |
| 4 | Eygelshoven, Netherlands | 29 | 5.4% |
| 5 | Vienna, Austria | 28 | 5.2% |
| 6 | Dublin, United States | 27 | 5.0% |
| 7 | Rome, Italy | 23 | 4.3% |
| 8 | Slough, United Kingdom | 21 | 3.9% |
| 9 | New York, United States | 15 | 2.8% |
| 10 | Beauharnois, Canada | 13 | 2.4% |
| 11 | Paris, France | 12 | 2.2% |
| 12 | Lewes, United States | 12 | 2.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `31.220.3.165` | 213 | 39.8% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 2 | `143.198.198.33` | 82 | 15.3% | Singapore / South West / Singapore / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 3 | `45.9.149.154` | 37 | 6.9% | Netherlands / North Holland / Amsterdam / Nice IT Services Group Inc. | No apparent signal |
| 4 | `196.242.141.12` | 28 | 5.2% | Austria / Vienna / Vienna / Fiber Grid | No apparent signal |
| 5 | `185.48.32.227` | 23 | 4.3% | Italy / Lazio / Rome / Irideos S.P.A. | No apparent signal |
| 6 | `45.9.149.219` | 23 | 4.3% | Netherlands / North Holland / Amsterdam / Nice IT Services Group Inc. | No apparent signal |
| 7 | `159.65.20.241` | 21 | 3.9% | United Kingdom / England / Slough / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 8 | `85.217.149.20` | 15 | 2.8% | United States / New York / New York / Modat B.V | No apparent signal |
| 9 | `45.153.34.160` | 15 | 2.8% | Netherlands / Limburg / Eygelshoven / VMHeaven.io | No apparent signal |
| 10 | `3.128.64.243` | 15 | 2.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `204.76.203.15` | 14 | 2.6% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 12 | `85.217.149.49` | 13 | 2.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 13 | `3.131.24.55` | 12 | 2.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `51.159.110.167` | 12 | 2.2% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 15 | `69.17.52.1` | 12 | 2.2% | United States / Delaware / Lewes / Spruce Creek Networks LLC | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `143.198.198.33` | 82 | 57.7% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / DigitalOcean, LLC |
| 2 | `159.65.20.241` | 21 | 14.8% | Hosting/Cloud (digitalocean) | United Kingdom / England / Slough / DigitalOcean, LLC |
| 3 | `3.128.64.243` | 15 | 10.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `3.131.24.55` | 12 | 8.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `51.159.110.167` | 12 | 8.5% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
