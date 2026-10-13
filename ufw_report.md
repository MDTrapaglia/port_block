# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4407
- Unique source IPs: 2330
- Unique countries/cities (24h): 298
- Unique destination ports: 2684

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 132 | 3.0% |
| 2 | `22` | 60 | 1.4% |
| 3 | `53` | 37 | 0.8% |
| 4 | `5060` | 36 | 0.8% |
| 5 | `8080` | 31 | 0.7% |
| 6 | `8443` | 26 | 0.6% |
| 7 | `161` | 24 | 0.5% |
| 8 | `3389` | 23 | 0.5% |
| 9 | `1433` | 22 | 0.5% |
| 10 | `8081` | 22 | 0.5% |
| 11 | `8000` | 19 | 0.4% |
| 12 | `3306` | 17 | 0.4% |
| 13 | `123` | 17 | 0.4% |
| 14 | `27017` | 17 | 0.4% |
| 15 | `2222` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4055 | 92.0% |
| 2 | `UDP` | 346 | 7.9% |
| 3 | `47` | 5 | 0.1% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `51.159.125.199` | 72 | 1.6% |
| 2 | `179.43.167.3` | 48 | 1.1% |
| 3 | `103.215.74.112` | 40 | 0.9% |
| 4 | `190.211.252.4` | 22 | 0.5% |
| 5 | `85.217.140.22` | 18 | 0.4% |
| 6 | `91.196.152.35` | 17 | 0.4% |
| 7 | `137.184.143.227` | 17 | 0.4% |
| 8 | `85.217.149.37` | 17 | 0.4% |
| 9 | `23.64.58.12` | 17 | 0.4% |
| 10 | `151.101.218.13` | 17 | 0.4% |
| 11 | `85.217.140.2` | 16 | 0.4% |
| 12 | `45.198.224.125` | 15 | 0.3% |
| 13 | `195.184.76.71` | 15 | 0.3% |
| 14 | `195.184.76.180` | 14 | 0.3% |
| 15 | `91.231.89.224` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3927 | 96.8% |
| 2 | `ACK+FIN+PSH` | 79 | 1.9% |
| 3 | `ACK+PSH` | 30 | 0.7% |
| 4 | `SYN+ECE+CWR` | 10 | 0.2% |
| 5 | `ACK+FIN` | 7 | 0.2% |
| 6 | `ACK` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4407 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `51.159.125.199` -> `1080` | 9 | 0.2% |
| 2 | `51.159.125.199` -> `1083` | 7 | 0.2% |
| 3 | `45.198.224.125` -> `9090` | 6 | 0.1% |
| 4 | `45.205.1.163` -> `17000` | 6 | 0.1% |
| 5 | `45.198.224.124` -> `81` | 6 | 0.1% |
| 6 | `45.198.224.125` -> `8080` | 6 | 0.1% |
| 7 | `51.159.125.199` -> `1094` | 6 | 0.1% |
| 8 | `51.159.125.199` -> `1122` | 6 | 0.1% |
| 9 | `51.159.125.199` -> `1129` | 6 | 0.1% |
| 10 | `79.0.5.138` -> `23` | 6 | 0.1% |
| 11 | `51.159.125.199` -> `943` | 6 | 0.1% |
| 12 | `51.159.125.199` -> `980` | 6 | 0.1% |
| 13 | `93.123.109.6` -> `1723` | 5 | 0.1% |
| 14 | `80.66.83.83` -> `5405` | 5 | 0.1% |
| 15 | `135.148.29.54` -> `5060` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-12 04:00:00:00 | 135 | 3.1% |
| 2026-10-12 05:00:00:00 | 180 | 4.1% |
| 2026-10-12 06:00:00:00 | 180 | 4.1% |
| 2026-10-12 07:00:00:00 | 181 | 4.1% |
| 2026-10-12 08:00:00:00 | 179 | 4.1% |
| 2026-10-12 09:00:00:00 | 180 | 4.1% |
| 2026-10-12 10:00:00:00 | 176 | 4.0% |
| 2026-10-12 11:00:00:00 | 182 | 4.1% |
| 2026-10-12 12:00:00:00 | 179 | 4.1% |
| 2026-10-12 13:00:00:00 | 194 | 4.4% |
| 2026-10-12 14:00:00:00 | 197 | 4.5% |
| 2026-10-12 15:00:00:00 | 195 | 4.4% |
| 2026-10-12 16:00:00:00 | 200 | 4.5% |
| 2026-10-12 17:00:00:00 | 185 | 4.2% |
| 2026-10-12 18:00:00:00 | 180 | 4.1% |
| 2026-10-12 19:00:00:00 | 180 | 4.1% |
| 2026-10-12 20:00:00:00 | 180 | 4.1% |
| 2026-10-12 21:00:00:00 | 180 | 4.1% |
| 2026-10-12 22:00:00:00 | 181 | 4.1% |
| 2026-10-12 23:00:00:00 | 181 | 4.1% |
| 2026-10-13 00:00:00:00 | 178 | 4.0% |
| 2026-10-13 01:00:00:00 | 188 | 4.3% |
| 2026-10-13 02:00:00:00 | 190 | 4.3% |
| 2026-10-13 03:00:00:00 | 180 | 4.1% |
| 2026-10-13 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Paris, France | 72 | 20.1% |
| 2 | Rümlang, Switzerland | 48 | 13.4% |
| 3 | Gravelines, France | 48 | 13.4% |
| 4 | Dallas, United States | 40 | 11.1% |
| 5 | Buenos Aires, Argentina | 34 | 9.5% |
| 6 | Warrenton, United States | 29 | 8.1% |
| 7 | Zurich, Switzerland | 22 | 6.1% |
| 8 | Roubaix, France | 17 | 4.7% |
| 9 | North Bergen, United States | 17 | 4.7% |
| 10 | Beauharnois, Canada | 17 | 4.7% |
| 11 | Stockholm, Sweden | 15 | 4.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `51.159.125.199` | 72 | 20.1% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 2 | `179.43.167.3` | 48 | 13.4% | Switzerland / Zurich / Rümlang / Private Layer Inc | No apparent signal |
| 3 | `103.215.74.112` | 40 | 11.1% | United States / Texas / Dallas / Rekha M. Jain | No apparent signal |
| 4 | `190.211.252.4` | 22 | 6.1% | Switzerland / Zurich / Zurich / Private Layer Inc | No apparent signal |
| 5 | `85.217.140.22` | 18 | 5.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `91.196.152.35` | 17 | 4.7% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 7 | `137.184.143.227` | 17 | 4.7% | United States / New Jersey / North Bergen / Digital Ocean | Hosting/Cloud (digitalocean) |
| 8 | `85.217.149.37` | 17 | 4.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 9 | `23.64.58.12` | 17 | 4.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. | CDN/Edge (akamai) |
| 10 | `151.101.218.13` | 17 | 4.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 11 | `85.217.140.2` | 16 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `45.198.224.125` | 15 | 4.2% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 13 | `195.184.76.71` | 15 | 4.2% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `195.184.76.180` | 14 | 3.9% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 15 | `91.231.89.224` | 14 | 3.9% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `51.159.125.199` | 72 | 58.5% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `137.184.143.227` | 17 | 13.8% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / Digital Ocean |
| 3 | `23.64.58.12` | 17 | 13.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. |
| 4 | `151.101.218.13` | 17 | 13.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
