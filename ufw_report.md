# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4403
- Unique source IPs: 2560
- Unique countries/cities (24h): 407
- Unique destination ports: 2463

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 228 | 5.2% |
| 2 | `22` | 95 | 2.2% |
| 3 | `53` | 33 | 0.7% |
| 4 | `8080` | 31 | 0.7% |
| 5 | `5060` | 26 | 0.6% |
| 6 | `3389` | 24 | 0.5% |
| 7 | `unknown` | 22 | 0.5% |
| 8 | `21` | 21 | 0.5% |
| 9 | `81` | 20 | 0.5% |
| 10 | `2222` | 20 | 0.5% |
| 11 | `5555` | 19 | 0.4% |
| 12 | `82` | 19 | 0.4% |
| 13 | `80` | 18 | 0.4% |
| 14 | `1433` | 18 | 0.4% |
| 15 | `5038` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4016 | 91.2% |
| 2 | `UDP` | 365 | 8.3% |
| 3 | `47` | 16 | 0.4% |
| 4 | `41` | 4 | 0.1% |
| 5 | `132` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.136` | 180 | 4.1% |
| 2 | `16.5.0.242` | 70 | 1.6% |
| 3 | `16.5.0.237` | 67 | 1.5% |
| 4 | `16.5.0.238` | 66 | 1.5% |
| 5 | `151.101.218.13` | 25 | 0.6% |
| 6 | `16.5.0.236` | 20 | 0.5% |
| 7 | `85.217.140.22` | 16 | 0.4% |
| 8 | `85.217.140.35` | 15 | 0.3% |
| 9 | `85.217.140.29` | 14 | 0.3% |
| 10 | `151.101.218.73` | 14 | 0.3% |
| 11 | `45.194.67.44` | 13 | 0.3% |
| 12 | `85.217.140.5` | 13 | 0.3% |
| 13 | `85.217.140.28` | 13 | 0.3% |
| 14 | `52.15.153.107` | 11 | 0.2% |
| 15 | `18.217.208.51` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3907 | 97.3% |
| 2 | `ACK+FIN+PSH` | 58 | 1.4% |
| 3 | `ACK` | 22 | 0.5% |
| 4 | `ACK+PSH` | 19 | 0.5% |
| 5 | `ACK+FIN` | 7 | 0.2% |
| 6 | `SYN+ECE+CWR` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4403 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.136` -> `82` | 12 | 0.3% |
| 2 | `216.180.246.136` -> `84` | 10 | 0.2% |
| 3 | `216.180.246.136` -> `88` | 10 | 0.2% |
| 4 | `216.180.246.136` -> `17` | 8 | 0.2% |
| 5 | `216.180.246.136` -> `67` | 8 | 0.2% |
| 6 | `216.180.246.136` -> `79` | 8 | 0.2% |
| 7 | `216.180.246.136` -> `81` | 8 | 0.2% |
| 8 | `151.101.218.13` -> `55932` | 8 | 0.2% |
| 9 | `216.180.246.136` -> `85` | 8 | 0.2% |
| 10 | `216.180.246.136` -> `1` | 7 | 0.2% |
| 11 | `216.180.246.136` -> `83` | 7 | 0.2% |
| 12 | `64.225.45.127` -> `2222` | 7 | 0.2% |
| 13 | `52.88.236.22` -> `31650` | 7 | 0.2% |
| 14 | `216.180.246.136` -> `13` | 6 | 0.1% |
| 15 | `216.180.246.136` -> `22` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-06 04:00:00:00 | 134 | 3.0% |
| 2026-09-06 05:00:00:00 | 180 | 4.1% |
| 2026-09-06 06:00:00:00 | 180 | 4.1% |
| 2026-09-06 07:00:00:00 | 181 | 4.1% |
| 2026-09-06 08:00:00:00 | 197 | 4.5% |
| 2026-09-06 09:00:00:00 | 180 | 4.1% |
| 2026-09-06 10:00:00:00 | 177 | 4.0% |
| 2026-09-06 11:00:00:00 | 181 | 4.1% |
| 2026-09-06 12:00:00:00 | 183 | 4.2% |
| 2026-09-06 13:00:00:00 | 190 | 4.3% |
| 2026-09-06 14:00:00:00 | 180 | 4.1% |
| 2026-09-06 15:00:00:00 | 181 | 4.1% |
| 2026-09-06 16:00:00:00 | 180 | 4.1% |
| 2026-09-06 17:00:00:00 | 180 | 4.1% |
| 2026-09-06 18:00:00:00 | 180 | 4.1% |
| 2026-09-06 19:00:00:00 | 179 | 4.1% |
| 2026-09-06 20:00:00:00 | 192 | 4.4% |
| 2026-09-06 21:00:00:00 | 178 | 4.0% |
| 2026-09-06 22:00:00:00 | 181 | 4.1% |
| 2026-09-06 23:00:00:00 | 181 | 4.1% |
| 2026-09-07 00:00:00:00 | 192 | 4.4% |
| 2026-09-07 01:00:00:00 | 210 | 4.8% |
| 2026-09-07 02:00:00:00 | 181 | 4.1% |
| 2026-09-07 03:00:00:00 | 179 | 4.1% |
| 2026-09-07 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | São Paulo, Brazil | 223 | 40.7% |
| 2 | Massy, France | 180 | 32.8% |
| 3 | Gravelines, France | 71 | 13.0% |
| 4 | Buenos Aires, Argentina | 25 | 4.6% |
| 5 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 14 | 2.6% |
| 6 | Grand'Anse, Seychelles | 13 | 2.4% |
| 7 | Columbus, United States | 11 | 2.0% |
| 8 | Dublin, United States | 11 | 2.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.136` | 180 | 32.8% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `16.5.0.242` | 70 | 12.8% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 3 | `16.5.0.237` | 67 | 12.2% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 4 | `16.5.0.238` | 66 | 12.0% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 5 | `151.101.218.13` | 25 | 4.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `16.5.0.236` | 20 | 3.6% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 7 | `85.217.140.22` | 16 | 2.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.35` | 15 | 2.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.29` | 14 | 2.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `151.101.218.73` | 14 | 2.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 11 | `45.194.67.44` | 13 | 2.4% | Seychelles / Grand Anse Mahe / Grand'Anse / Aaroppe Internet Services Ltd Sti | No apparent signal |
| 12 | `85.217.140.5` | 13 | 2.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `85.217.140.28` | 13 | 2.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `52.15.153.107` | 11 | 2.0% | United States / Ohio / Columbus / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `18.217.208.51` | 11 | 2.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.136` | 180 | 74.7% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 25 | 10.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.73` | 14 | 5.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `52.15.153.107` | 11 | 4.6% | Hosting/Cloud (aws) | United States / Ohio / Columbus / AWS EC2 (us-east-2) |
| 5 | `18.217.208.51` | 11 | 4.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
