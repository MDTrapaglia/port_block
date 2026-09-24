# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4394
- Unique source IPs: 2212
- Unique countries/cities (24h): 346
- Unique destination ports: 2497

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 163 | 3.7% |
| 2 | `22` | 95 | 2.2% |
| 3 | `1433` | 36 | 0.8% |
| 4 | `8080` | 36 | 0.8% |
| 5 | `3389` | 36 | 0.8% |
| 6 | `53` | 33 | 0.8% |
| 7 | `5060` | 31 | 0.7% |
| 8 | `8443` | 27 | 0.6% |
| 9 | `3306` | 25 | 0.6% |
| 10 | `2222` | 22 | 0.5% |
| 11 | `unknown` | 19 | 0.4% |
| 12 | `25` | 19 | 0.4% |
| 13 | `123` | 19 | 0.4% |
| 14 | `21` | 18 | 0.4% |
| 15 | `5900` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3994 | 90.9% |
| 2 | `UDP` | 381 | 8.7% |
| 3 | `47` | 12 | 0.3% |
| 4 | `2` | 6 | 0.1% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `157.66.47.64` | 79 | 1.8% |
| 2 | `151.101.218.13` | 34 | 0.8% |
| 3 | `34.133.44.46` | 24 | 0.5% |
| 4 | `185.242.3.254` | 22 | 0.5% |
| 5 | `85.217.140.20` | 19 | 0.4% |
| 6 | `91.231.89.150` | 16 | 0.4% |
| 7 | `94.154.43.159` | 16 | 0.4% |
| 8 | `85.217.140.18` | 16 | 0.4% |
| 9 | `85.217.140.30` | 16 | 0.4% |
| 10 | `46.151.178.133` | 16 | 0.4% |
| 11 | `85.217.140.27` | 15 | 0.3% |
| 12 | `195.184.76.116` | 15 | 0.3% |
| 13 | `91.231.89.130` | 15 | 0.3% |
| 14 | `91.196.152.35` | 15 | 0.3% |
| 15 | `85.217.140.22` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3858 | 96.6% |
| 2 | `ACK+FIN+PSH` | 72 | 1.8% |
| 3 | `ACK+PSH` | 38 | 1.0% |
| 4 | `SYN+ECE+CWR` | 21 | 0.5% |
| 5 | `ACK+FIN` | 5 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4388 | 99.9% |
| 2 | `wlan0` | 6 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `151.101.218.13` -> `50548` | 8 | 0.2% |
| 2 | `196.244.192.202` -> `22` | 7 | 0.2% |
| 3 | `130.12.180.65` -> `5555` | 7 | 0.2% |
| 4 | `192.168.100.64` -> `unknown` | 6 | 0.1% |
| 5 | `69.48.216.114` -> `54134` | 6 | 0.1% |
| 6 | `180.93.244.95` -> `5911` | 6 | 0.1% |
| 7 | `167.94.146.60` -> `993` | 6 | 0.1% |
| 8 | `151.101.218.13` -> `12271` | 6 | 0.1% |
| 9 | `151.101.218.13` -> `50002` | 6 | 0.1% |
| 10 | `201.20.85.122` -> `6379` | 5 | 0.1% |
| 11 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 12 | `223.96.92.77` -> `1433` | 5 | 0.1% |
| 13 | `193.90.12.122` -> `23` | 5 | 0.1% |
| 14 | `2.22.149.177` -> `49284` | 5 | 0.1% |
| 15 | `151.101.218.13` -> `49276` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-23 04:00:00:00 | 134 | 3.0% |
| 2026-09-23 05:00:00:00 | 180 | 4.1% |
| 2026-09-23 06:00:00:00 | 181 | 4.1% |
| 2026-09-23 07:00:00:00 | 180 | 4.1% |
| 2026-09-23 08:00:00:00 | 178 | 4.1% |
| 2026-09-23 09:00:00:00 | 183 | 4.2% |
| 2026-09-23 10:00:00:00 | 181 | 4.1% |
| 2026-09-23 11:00:00:00 | 177 | 4.0% |
| 2026-09-23 12:00:00:00 | 196 | 4.5% |
| 2026-09-23 13:00:00:00 | 184 | 4.2% |
| 2026-09-23 14:00:00:00 | 180 | 4.1% |
| 2026-09-23 15:00:00:00 | 180 | 4.1% |
| 2026-09-23 16:00:00:00 | 180 | 4.1% |
| 2026-09-23 17:00:00:00 | 177 | 4.0% |
| 2026-09-23 18:00:00:00 | 199 | 4.5% |
| 2026-09-23 19:00:00:00 | 177 | 4.0% |
| 2026-09-23 20:00:00:00 | 183 | 4.2% |
| 2026-09-23 21:00:00:00 | 190 | 4.3% |
| 2026-09-23 22:00:00:00 | 188 | 4.3% |
| 2026-09-23 23:00:00:00 | 189 | 4.3% |
| 2026-09-24 00:00:00:00 | 192 | 4.4% |
| 2026-09-24 01:00:00:00 | 179 | 4.1% |
| 2026-09-24 02:00:00:00 | 180 | 4.1% |
| 2026-09-24 03:00:00:00 | 180 | 4.1% |
| 2026-09-24 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 112 | 33.6% |
| 2 | Hanoi, Vietnam | 79 | 23.7% |
| 3 | Buenos Aires, Argentina | 34 | 10.2% |
| 4 | Council Bluffs, United States | 24 | 7.2% |
| 5 | Frankfurt am Main, Germany | 22 | 6.6% |
| 6 | Amsterdam, The Netherlands | 16 | 4.8% |
| 7 | Hong Kong, Hong Kong | 16 | 4.8% |
| 8 | Warrenton, United States | 15 | 4.5% |
| 9 | Roubaix, France | 15 | 4.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `157.66.47.64` | 79 | 23.7% | Vietnam / Hanoi / Hanoi / Jupiter Media Joint Stock Company | No apparent signal |
| 2 | `151.101.218.13` | 34 | 10.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `34.133.44.46` | 24 | 7.2% | United States / Iowa / Council Bluffs / Google Cloud (us-central1) | Hosting/Cloud (google cloud) |
| 4 | `185.242.3.254` | 22 | 6.6% | Germany / Hesse / Frankfurt am Main / Felcloud | No apparent signal |
| 5 | `85.217.140.20` | 19 | 5.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `91.231.89.150` | 16 | 4.8% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `94.154.43.159` | 16 | 4.8% | The Netherlands / North Holland / Amsterdam / FOP Danik Vyacheslav Evgenievich | No apparent signal |
| 8 | `85.217.140.18` | 16 | 4.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.30` | 16 | 4.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `46.151.178.133` | 16 | 4.8% | Hong Kong / Kowloon / Hong Kong / Sino Worldwide Trading Limited | No apparent signal |
| 11 | `85.217.140.27` | 15 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `195.184.76.116` | 15 | 4.5% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 13 | `91.231.89.130` | 15 | 4.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.196.152.35` | 15 | 4.5% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 15 | `85.217.140.22` | 15 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 34 | 58.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `34.133.44.46` | 24 | 41.4% | Hosting/Cloud (google cloud) | United States / Iowa / Council Bluffs / Google Cloud (us-central1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
