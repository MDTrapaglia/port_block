# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4408
- Unique source IPs: 2522
- Unique countries/cities (24h): 535
- Unique destination ports: 2052

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1290 | 29.3% |
| 2 | `22` | 64 | 1.5% |
| 3 | `8080` | 37 | 0.8% |
| 4 | `5060` | 28 | 0.6% |
| 5 | `3389` | 24 | 0.5% |
| 6 | `53` | 20 | 0.5% |
| 7 | `8081` | 19 | 0.4% |
| 8 | `8443` | 17 | 0.4% |
| 9 | `1433` | 17 | 0.4% |
| 10 | `3306` | 15 | 0.3% |
| 11 | `5432` | 13 | 0.3% |
| 12 | `123` | 12 | 0.3% |
| 13 | `2222` | 12 | 0.3% |
| 14 | `25` | 12 | 0.3% |
| 15 | `40000` | 11 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4180 | 94.8% |
| 2 | `UDP` | 226 | 5.1% |
| 3 | `47` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.21` | 99 | 2.2% |
| 2 | `193.178.158.123` | 65 | 1.5% |
| 3 | `123.245.84.137` | 48 | 1.1% |
| 4 | `180.191.14.194` | 47 | 1.1% |
| 5 | `93.152.221.108` | 41 | 0.9% |
| 6 | `112.117.183.133` | 37 | 0.8% |
| 7 | `85.217.140.17` | 35 | 0.8% |
| 8 | `223.151.75.179` | 35 | 0.8% |
| 9 | `121.61.3.176` | 34 | 0.8% |
| 10 | `85.217.140.14` | 20 | 0.5% |
| 11 | `31.200.234.27` | 20 | 0.5% |
| 12 | `42.100.23.120` | 19 | 0.4% |
| 13 | `151.101.218.73` | 19 | 0.4% |
| 14 | `2.22.149.160` | 14 | 0.3% |
| 15 | `216.228.219.233` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 4051 | 96.9% |
| 2 | `ACK+FIN+PSH` | 82 | 2.0% |
| 3 | `ACK+PSH` | 36 | 0.9% |
| 4 | `ACK+FIN` | 6 | 0.1% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4408 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `123.245.84.137` -> `23` | 48 | 1.1% |
| 2 | `180.191.14.194` -> `23` | 47 | 1.1% |
| 3 | `112.117.183.133` -> `23` | 37 | 0.8% |
| 4 | `223.151.75.179` -> `23` | 35 | 0.8% |
| 5 | `121.61.3.176` -> `23` | 34 | 0.8% |
| 6 | `31.200.234.27` -> `23` | 20 | 0.5% |
| 7 | `42.100.23.120` -> `23` | 19 | 0.4% |
| 8 | `216.228.219.233` -> `23` | 13 | 0.3% |
| 9 | `121.57.181.157` -> `23` | 13 | 0.3% |
| 10 | `42.242.158.28` -> `23` | 12 | 0.3% |
| 11 | `109.63.118.182` -> `23` | 11 | 0.2% |
| 12 | `197.158.24.109` -> `23` | 8 | 0.2% |
| 13 | `151.101.216.157` -> `40000` | 7 | 0.2% |
| 14 | `216.180.246.21` -> `50010` | 7 | 0.2% |
| 15 | `101.98.137.2` -> `23` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-21 04:00:00:00 | 135 | 3.1% |
| 2026-10-21 05:00:00:00 | 191 | 4.3% |
| 2026-10-21 06:00:00:00 | 179 | 4.1% |
| 2026-10-21 07:00:00:00 | 181 | 4.1% |
| 2026-10-21 08:00:00:00 | 183 | 4.2% |
| 2026-10-21 09:00:00:00 | 186 | 4.2% |
| 2026-10-21 10:00:00:00 | 180 | 4.1% |
| 2026-10-21 11:00:00:00 | 180 | 4.1% |
| 2026-10-21 12:00:00:00 | 180 | 4.1% |
| 2026-10-21 13:00:00:00 | 180 | 4.1% |
| 2026-10-21 14:00:00:00 | 193 | 4.4% |
| 2026-10-21 15:00:00:00 | 182 | 4.1% |
| 2026-10-21 16:00:00:00 | 179 | 4.1% |
| 2026-10-21 17:00:00:00 | 180 | 4.1% |
| 2026-10-21 18:00:00:00 | 180 | 4.1% |
| 2026-10-21 19:00:00:00 | 191 | 4.3% |
| 2026-10-21 20:00:00:00 | 193 | 4.4% |
| 2026-10-21 21:00:00:00 | 179 | 4.1% |
| 2026-10-21 22:00:00:00 | 180 | 4.1% |
| 2026-10-21 23:00:00:00 | 181 | 4.1% |
| 2026-10-22 00:00:00:00 | 178 | 4.0% |
| 2026-10-22 01:00:00:00 | 180 | 4.1% |
| 2026-10-22 02:00:00:00 | 203 | 4.6% |
| 2026-10-22 03:00:00:00 | 189 | 4.3% |
| 2026-10-22 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 99 | 18.1% |
| 2 | St Petersburg, Russia | 65 | 11.9% |
| 3 | Gravelines, France | 55 | 10.1% |
| 4 | Shenyang, China | 48 | 8.8% |
| 5 | Cabanatuan City, Philippines | 47 | 8.6% |
| 6 | Frankfurt am Main, Germany | 41 | 7.5% |
| 7 | Kunming, China | 37 | 6.8% |
| 8 | Qingyuan, China | 35 | 6.4% |
| 9 | Shizishan, China | 34 | 6.2% |
| 10 | Nakhodka, Russia | 20 | 3.7% |
| 11 | Harbin, China | 19 | 3.5% |
| 12 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 19 | 3.5% |
| 13 | Buenos Aires, Argentina | 14 | 2.6% |
| 14 | Bécancour, Canada | 13 | 2.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.21` | 99 | 18.1% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `193.178.158.123` | 65 | 11.9% | Russia / St.-Petersburg / St Petersburg / UFO TECHNOLOGIES LIMITED | No apparent signal |
| 3 | `123.245.84.137` | 48 | 8.8% | China / Liaoning / Shenyang / JunQu2 | No apparent signal |
| 4 | `180.191.14.194` | 47 | 8.6% | Philippines / Central Luzon / Cabanatuan City / Globe Telecom | No apparent signal |
| 5 | `93.152.221.108` | 41 | 7.5% | Germany / Hesse / Frankfurt am Main / TechTies Inc | No apparent signal |
| 6 | `112.117.183.133` | 37 | 6.8% | China / Yunnan / Kunming / Chinanet YN | No apparent signal |
| 7 | `85.217.140.17` | 35 | 6.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `223.151.75.179` | 35 | 6.4% | China / Hunan / Qingyuan / Chinanet HN | No apparent signal |
| 9 | `121.61.3.176` | 34 | 6.2% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 10 | `85.217.140.14` | 20 | 3.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `31.200.234.27` | 20 | 3.7% | Russia / Primorye / Nakhodka / ISP Podryad Nets | No apparent signal |
| 12 | `42.100.23.120` | 19 | 3.5% | China / Heilongjiang / Harbin / Chinanet HL | No apparent signal |
| 13 | `151.101.218.73` | 19 | 3.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 14 | `2.22.149.160` | 14 | 2.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 15 | `216.228.219.233` | 13 | 2.4% | Canada / Quebec / Bécancour / Cable Axion Digitel Inc | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.21` | 99 | 75.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `151.101.218.73` | 19 | 14.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `2.22.149.160` | 14 | 10.6% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
