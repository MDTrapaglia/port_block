# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4420
- Unique source IPs: 2350
- Unique countries/cities (24h): 375
- Unique destination ports: 2094

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1062 | 24.0% |
| 2 | `22` | 44 | 1.0% |
| 3 | `5060` | 34 | 0.8% |
| 4 | `8080` | 28 | 0.6% |
| 5 | `3389` | 20 | 0.5% |
| 6 | `5900` | 17 | 0.4% |
| 7 | `5432` | 17 | 0.4% |
| 8 | `unknown` | 16 | 0.4% |
| 9 | `53` | 16 | 0.4% |
| 10 | `8000` | 14 | 0.3% |
| 11 | `8081` | 14 | 0.3% |
| 12 | `8088` | 14 | 0.3% |
| 13 | `3306` | 14 | 0.3% |
| 14 | `8443` | 12 | 0.3% |
| 15 | `25` | 12 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4062 | 91.9% |
| 2 | `UDP` | 342 | 7.7% |
| 3 | `47` | 16 | 0.4% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `96.127.180.162` | 278 | 6.3% |
| 2 | `41.168.10.139` | 154 | 3.5% |
| 3 | `206.183.111.36` | 146 | 3.3% |
| 4 | `23.81.44.23` | 130 | 2.9% |
| 5 | `104.36.149.26` | 57 | 1.3% |
| 6 | `23.29.127.18` | 53 | 1.2% |
| 7 | `92.204.138.159` | 37 | 0.8% |
| 8 | `197.242.158.191` | 36 | 0.8% |
| 9 | `219.153.113.102` | 22 | 0.5% |
| 10 | `103.6.245.158` | 22 | 0.5% |
| 11 | `149.154.167.220` | 19 | 0.4% |
| 12 | `157.230.226.40` | 15 | 0.3% |
| 13 | `43.228.157.9` | 15 | 0.3% |
| 14 | `2.22.149.153` | 15 | 0.3% |
| 15 | `142.93.57.83` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3881 | 95.5% |
| 2 | `ACK+FIN+PSH` | 93 | 2.3% |
| 3 | `ACK+PSH` | 70 | 1.7% |
| 4 | `ACK+FIN` | 7 | 0.2% |
| 5 | `ACK` | 5 | 0.1% |
| 6 | `SYN+ECE+CWR` | 5 | 0.1% |
| 7 | `ACK+FIN+PSH+CWR` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4418 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `96.127.180.162` -> `23` | 278 | 6.3% |
| 2 | `41.168.10.139` -> `23` | 154 | 3.5% |
| 3 | `206.183.111.36` -> `23` | 146 | 3.3% |
| 4 | `23.81.44.23` -> `23` | 130 | 2.9% |
| 5 | `104.36.149.26` -> `23` | 57 | 1.3% |
| 6 | `92.204.138.159` -> `23` | 37 | 0.8% |
| 7 | `197.242.158.191` -> `23` | 36 | 0.8% |
| 8 | `103.6.245.158` -> `23` | 22 | 0.5% |
| 9 | `142.93.57.83` -> `23` | 14 | 0.3% |
| 10 | `99.239.70.204` -> `23` | 12 | 0.3% |
| 11 | `149.154.167.220` -> `51620` | 8 | 0.2% |
| 12 | `18.188.172.227` -> `38852` | 7 | 0.2% |
| 13 | `124.198.131.185` -> `8021` | 6 | 0.1% |
| 14 | `66.132.172.211` -> `44888` | 6 | 0.1% |
| 15 | `140.233.190.89` -> `9000` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-12 04:00:00:00 | 132 | 3.0% |
| 2026-05-12 05:00:00:00 | 182 | 4.1% |
| 2026-05-12 06:00:00:00 | 179 | 4.1% |
| 2026-05-12 07:00:00:00 | 180 | 4.1% |
| 2026-05-12 08:00:00:00 | 181 | 4.1% |
| 2026-05-12 09:00:00:00 | 187 | 4.2% |
| 2026-05-12 10:00:00:00 | 195 | 4.4% |
| 2026-05-12 11:00:00:00 | 196 | 4.4% |
| 2026-05-12 12:00:00:00 | 188 | 4.3% |
| 2026-05-12 13:00:00:00 | 180 | 4.1% |
| 2026-05-12 14:00:00:00 | 180 | 4.1% |
| 2026-05-12 15:00:00:00 | 196 | 4.4% |
| 2026-05-12 16:00:00:00 | 194 | 4.4% |
| 2026-05-12 17:00:00:00 | 184 | 4.2% |
| 2026-05-12 18:00:00:00 | 179 | 4.1% |
| 2026-05-12 19:00:00:00 | 180 | 4.1% |
| 2026-05-12 20:00:00:00 | 181 | 4.1% |
| 2026-05-12 21:00:00:00 | 179 | 4.1% |
| 2026-05-12 22:00:00:00 | 180 | 4.1% |
| 2026-05-12 23:00:00:00 | 207 | 4.7% |
| 2026-05-13 00:00:00:00 | 179 | 4.1% |
| 2026-05-13 01:00:00:00 | 178 | 4.0% |
| 2026-05-13 02:00:00:00 | 183 | 4.1% |
| 2026-05-13 03:00:00:00 | 177 | 4.0% |
| 2026-05-13 04:00:00:00 | 42 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Norcross, United States | 278 | 27.4% |
| 2 | Walkerville, South Africa | 154 | 15.2% |
| 3 | Mumbai, India | 146 | 14.4% |
| 4 | Minato-ku, Japan | 130 | 12.8% |
| 5 | Calgary, Canada | 57 | 5.6% |
| 6 | New York, United States | 53 | 5.2% |
| 7 | Warrenton, United States | 37 | 3.7% |
| 8 | Johannesburg, South Africa | 36 | 3.6% |
| 9 | North Bergen, United States | 29 | 2.9% |
| 10 | Chongqing, China | 22 | 2.2% |
| 11 | Kuala Lumpur, Malaysia | 22 | 2.2% |
| 12 | Amsterdam, Netherlands | 19 | 1.9% |
| 13 | Singapore, Singapore | 15 | 1.5% |
| 14 | Buenos Aires, Argentina | 15 | 1.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `96.127.180.162` | 278 | 27.4% | United States / Georgia / Norcross / Internap Holding LLC | No apparent signal |
| 2 | `41.168.10.139` | 154 | 15.2% | South Africa / Gauteng / Walkerville / NeoHost | No apparent signal |
| 3 | `206.183.111.36` | 146 | 14.4% | India / Maharashtra / Mumbai / Web Werks India Pvt. Ltd. | No apparent signal |
| 4 | `23.81.44.23` | 130 | 12.8% | Japan / Tokyo / Minato-ku / Leaseweb Japan K.K. | Hosting/Cloud (leaseweb) |
| 5 | `104.36.149.26` | 57 | 5.6% | Canada / Alberta / Calgary / Idigital Internet Inc | No apparent signal |
| 6 | `23.29.127.18` | 53 | 5.2% | United States / New York / New York / HIVELOCITY, Inc. | Hosting/Cloud (hivelocity) |
| 7 | `92.204.138.159` | 37 | 3.7% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 8 | `197.242.158.191` | 36 | 3.6% | South Africa / Gauteng / Johannesburg / Afrihost | No apparent signal |
| 9 | `219.153.113.102` | 22 | 2.2% | China / Chongqing / Chongqing / Chinanet CQ | No apparent signal |
| 10 | `103.6.245.158` | 22 | 2.2% | Malaysia / Kuala Lumpur / Kuala Lumpur / ICORE928 | No apparent signal |
| 11 | `149.154.167.220` | 19 | 1.9% | Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 12 | `157.230.226.40` | 15 | 1.5% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `43.228.157.9` | 15 | 1.5% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 14 | `2.22.149.153` | 15 | 1.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 15 | `142.93.57.83` | 14 | 1.4% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `23.81.44.23` | 130 | 57.3% | Hosting/Cloud (leaseweb) | Japan / Tokyo / Minato-ku / Leaseweb Japan K.K. |
| 2 | `23.29.127.18` | 53 | 23.3% | Hosting/Cloud (hivelocity) | United States / New York / New York / HIVELOCITY, Inc. |
| 3 | `157.230.226.40` | 15 | 6.6% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 4 | `2.22.149.153` | 15 | 6.6% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 5 | `142.93.57.83` | 14 | 6.2% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
