# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4358
- Unique source IPs: 2571
- Unique countries/cities (24h): 401
- Unique destination ports: 2619

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 214 | 4.9% |
| 2 | `22` | 70 | 1.6% |
| 3 | `8080` | 35 | 0.8% |
| 4 | `1433` | 32 | 0.7% |
| 5 | `5060` | 29 | 0.7% |
| 6 | `53` | 24 | 0.6% |
| 7 | `3389` | 20 | 0.5% |
| 8 | `8443` | 19 | 0.4% |
| 9 | `1900` | 19 | 0.4% |
| 10 | `unknown` | 18 | 0.4% |
| 11 | `1434` | 17 | 0.4% |
| 12 | `161` | 17 | 0.4% |
| 13 | `27017` | 17 | 0.4% |
| 14 | `21` | 16 | 0.4% |
| 15 | `389` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3900 | 89.5% |
| 2 | `UDP` | 440 | 10.1% |
| 3 | `47` | 17 | 0.4% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.96` | 161 | 3.7% |
| 2 | `209.99.187.232` | 28 | 0.6% |
| 3 | `66.96.215.92` | 25 | 0.6% |
| 4 | `2.22.149.160` | 20 | 0.5% |
| 5 | `85.217.140.5` | 18 | 0.4% |
| 6 | `85.217.140.27` | 14 | 0.3% |
| 7 | `178.255.42.186` | 13 | 0.3% |
| 8 | `85.217.140.34` | 13 | 0.3% |
| 9 | `85.217.140.33` | 13 | 0.3% |
| 10 | `85.217.140.28` | 12 | 0.3% |
| 11 | `185.224.128.16` | 12 | 0.3% |
| 12 | `85.217.140.7` | 12 | 0.3% |
| 13 | `151.243.11.240` | 12 | 0.3% |
| 14 | `3.151.116.231` | 11 | 0.3% |
| 15 | `85.217.149.37` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3802 | 97.5% |
| 2 | `ACK+FIN+PSH` | 38 | 1.0% |
| 3 | `ACK+PSH` | 27 | 0.7% |
| 4 | `ACK` | 19 | 0.5% |
| 5 | `SYN+ECE+CWR` | 11 | 0.3% |
| 6 | `ACK+FIN` | 2 | 0.1% |
| 7 | `ACK+RST` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4358 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.96` -> `25` | 9 | 0.2% |
| 2 | `216.180.246.96` -> `84` | 9 | 0.2% |
| 3 | `216.180.246.96` -> `53` | 8 | 0.2% |
| 4 | `178.20.210.152` -> `1723` | 7 | 0.2% |
| 5 | `216.180.246.96` -> `17` | 7 | 0.2% |
| 6 | `216.180.246.96` -> `22` | 7 | 0.2% |
| 7 | `216.180.246.96` -> `24` | 7 | 0.2% |
| 8 | `216.180.246.96` -> `86` | 7 | 0.2% |
| 9 | `216.180.246.96` -> `90` | 7 | 0.2% |
| 10 | `223.96.92.77` -> `1433` | 6 | 0.1% |
| 11 | `194.28.89.218` -> `5038` | 6 | 0.1% |
| 12 | `216.180.246.96` -> `67` | 6 | 0.1% |
| 13 | `216.180.246.96` -> `70` | 6 | 0.1% |
| 14 | `216.180.246.96` -> `72` | 6 | 0.1% |
| 15 | `216.180.246.96` -> `74` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-11 04:00:00:00 | 135 | 3.1% |
| 2026-09-11 05:00:00:00 | 180 | 4.1% |
| 2026-09-11 06:00:00:00 | 178 | 4.1% |
| 2026-09-11 07:00:00:00 | 180 | 4.1% |
| 2026-09-11 08:00:00:00 | 179 | 4.1% |
| 2026-09-11 09:00:00:00 | 181 | 4.2% |
| 2026-09-11 10:00:00:00 | 177 | 4.1% |
| 2026-09-11 11:00:00:00 | 182 | 4.2% |
| 2026-09-11 12:00:00:00 | 180 | 4.1% |
| 2026-09-11 13:00:00:00 | 181 | 4.2% |
| 2026-09-11 14:00:00:00 | 178 | 4.1% |
| 2026-09-11 15:00:00:00 | 182 | 4.2% |
| 2026-09-11 16:00:00:00 | 177 | 4.1% |
| 2026-09-11 17:00:00:00 | 181 | 4.2% |
| 2026-09-11 18:00:00:00 | 181 | 4.2% |
| 2026-09-11 19:00:00:00 | 181 | 4.2% |
| 2026-09-11 20:00:00:00 | 180 | 4.1% |
| 2026-09-11 21:00:00:00 | 180 | 4.1% |
| 2026-09-11 22:00:00:00 | 179 | 4.1% |
| 2026-09-11 23:00:00:00 | 198 | 4.5% |
| 2026-09-12 00:00:00:00 | 181 | 4.2% |
| 2026-09-12 01:00:00:00 | 202 | 4.6% |
| 2026-09-12 02:00:00:00 | 179 | 4.1% |
| 2026-09-12 03:00:00:00 | 182 | 4.2% |
| 2026-09-12 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 161 | 42.9% |
| 2 | Gravelines, France | 82 | 21.9% |
| 3 | Zurich, Switzerland | 28 | 7.5% |
| 4 | Singapore, Singapore | 25 | 6.7% |
| 5 | Buenos Aires, Argentina | 20 | 5.3% |
| 6 | Gdansk, Poland | 13 | 3.5% |
| 7 | Amsterdam, The Netherlands | 12 | 3.2% |
| 8 | Frankfurt am Main, Germany | 12 | 3.2% |
| 9 | Dublin, United States | 11 | 2.9% |
| 10 | Beauharnois, Canada | 11 | 2.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.96` | 161 | 42.9% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `209.99.187.232` | 28 | 7.5% | Switzerland / Zurich / Zurich / HostRoyale Technologies | No apparent signal |
| 3 | `66.96.215.92` | 25 | 6.7% | Singapore / Central Singapore / Singapore / MyRepublic Ltd | No apparent signal |
| 4 | `2.22.149.160` | 20 | 5.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 5 | `85.217.140.5` | 18 | 4.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `85.217.140.27` | 14 | 3.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `178.255.42.186` | 13 | 3.5% | Poland / Pomerania / Gdansk / Synkom sp. z o.o. | No apparent signal |
| 8 | `85.217.140.34` | 13 | 3.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.33` | 13 | 3.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.28` | 12 | 3.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `185.224.128.16` | 12 | 3.2% | The Netherlands / North Holland / Amsterdam / Alsycon B.V | No apparent signal |
| 12 | `85.217.140.7` | 12 | 3.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `151.243.11.240` | 12 | 3.2% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 14 | `3.151.116.231` | 11 | 2.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `85.217.149.37` | 11 | 2.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.96` | 161 | 83.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `2.22.149.160` | 20 | 10.4% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `3.151.116.231` | 11 | 5.7% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
