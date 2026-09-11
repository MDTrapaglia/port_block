# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4459
- Unique source IPs: 2609
- Unique countries/cities (24h): 397
- Unique destination ports: 2682

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 262 | 5.9% |
| 2 | `22` | 81 | 1.8% |
| 3 | `1433` | 41 | 0.9% |
| 4 | `53` | 32 | 0.7% |
| 5 | `8080` | 25 | 0.6% |
| 6 | `5060` | 24 | 0.5% |
| 7 | `3389` | 23 | 0.5% |
| 8 | `8081` | 18 | 0.4% |
| 9 | `8443` | 17 | 0.4% |
| 10 | `2222` | 17 | 0.4% |
| 11 | `1900` | 16 | 0.4% |
| 12 | `3306` | 16 | 0.4% |
| 13 | `3702` | 16 | 0.4% |
| 14 | `123` | 14 | 0.3% |
| 15 | `81` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3994 | 89.6% |
| 2 | `UDP` | 453 | 10.2% |
| 3 | `47` | 12 | 0.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `31.24.92.180` | 72 | 1.6% |
| 2 | `151.101.218.13` | 64 | 1.4% |
| 3 | `81.110.171.250` | 23 | 0.5% |
| 4 | `51.254.243.118` | 19 | 0.4% |
| 5 | `151.101.218.73` | 18 | 0.4% |
| 6 | `85.217.140.19` | 15 | 0.3% |
| 7 | `85.217.140.1` | 14 | 0.3% |
| 8 | `85.217.140.2` | 14 | 0.3% |
| 9 | `18.221.179.104` | 13 | 0.3% |
| 10 | `77.239.124.127` | 13 | 0.3% |
| 11 | `85.217.140.18` | 13 | 0.3% |
| 12 | `85.217.140.20` | 13 | 0.3% |
| 13 | `45.194.67.120` | 12 | 0.3% |
| 14 | `93.123.109.6` | 12 | 0.3% |
| 15 | `176.65.134.24` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3805 | 95.3% |
| 2 | `ACK+FIN+PSH` | 119 | 3.0% |
| 3 | `ACK+PSH` | 23 | 0.6% |
| 4 | `ACK+FIN` | 20 | 0.5% |
| 5 | `SYN+ECE+CWR` | 14 | 0.4% |
| 6 | `ACK` | 12 | 0.3% |
| 7 | `ACK+ECE` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4458 | 100.0% |
| 2 | `wlan0` | 1 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `81.110.171.250` -> `23` | 23 | 0.5% |
| 2 | `223.96.92.77` -> `1433` | 9 | 0.2% |
| 3 | `193.90.12.122` -> `23` | 7 | 0.2% |
| 4 | `170.51.241.169` -> `56538` | 7 | 0.2% |
| 5 | `77.239.124.127` -> `2323` | 6 | 0.1% |
| 6 | `69.17.52.1` -> `8333` | 6 | 0.1% |
| 7 | `151.101.218.13` -> `51288` | 6 | 0.1% |
| 8 | `95.100.88.48` -> `51338` | 6 | 0.1% |
| 9 | `151.101.218.73` -> `55906` | 6 | 0.1% |
| 10 | `151.101.218.13` -> `56566` | 6 | 0.1% |
| 11 | `152.171.48.149` -> `44117` | 6 | 0.1% |
| 12 | `77.239.124.127` -> `23` | 5 | 0.1% |
| 13 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 14 | `151.101.218.13` -> `51354` | 5 | 0.1% |
| 15 | `23.40.188.25` -> `52788` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-10 04:00:00:00 | 146 | 3.3% |
| 2026-09-10 05:00:00:00 | 180 | 4.0% |
| 2026-09-10 06:00:00:00 | 180 | 4.0% |
| 2026-09-10 07:00:00:00 | 181 | 4.1% |
| 2026-09-10 08:00:00:00 | 177 | 4.0% |
| 2026-09-10 09:00:00:00 | 181 | 4.1% |
| 2026-09-10 10:00:00:00 | 181 | 4.1% |
| 2026-09-10 11:00:00:00 | 181 | 4.1% |
| 2026-09-10 12:00:00:00 | 201 | 4.5% |
| 2026-09-10 13:00:00:00 | 197 | 4.4% |
| 2026-09-10 14:00:00:00 | 180 | 4.0% |
| 2026-09-10 15:00:00:00 | 180 | 4.0% |
| 2026-09-10 16:00:00:00 | 202 | 4.5% |
| 2026-09-10 17:00:00:00 | 180 | 4.0% |
| 2026-09-10 18:00:00:00 | 180 | 4.0% |
| 2026-09-10 19:00:00:00 | 197 | 4.4% |
| 2026-09-10 20:00:00:00 | 180 | 4.0% |
| 2026-09-10 21:00:00:00 | 179 | 4.0% |
| 2026-09-10 22:00:00:00 | 181 | 4.1% |
| 2026-09-10 23:00:00:00 | 228 | 5.1% |
| 2026-09-11 00:00:00:00 | 182 | 4.1% |
| 2026-09-11 01:00:00:00 | 179 | 4.0% |
| 2026-09-11 02:00:00:00 | 181 | 4.1% |
| 2026-09-11 03:00:00:00 | 180 | 4.0% |
| 2026-09-11 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Minsk, Belarus | 72 | 22.0% |
| 2 | Buenos Aires, Argentina | 64 | 19.6% |
| 3 | Gravelines, France | 55 | 16.8% |
| 4 | Manchester, United Kingdom | 23 | 7.0% |
| 5 | Roubaix, France | 19 | 5.8% |
| 6 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 18 | 5.5% |
| 7 | Paris, France | 14 | 4.3% |
| 8 | Dublin, United States | 13 | 4.0% |
| 9 | Amsterdam, The Netherlands | 13 | 4.0% |
| 10 | São Paulo, Brazil | 12 | 3.7% |
| 11 | Andorra la Vella, Andorra | 12 | 3.7% |
| 12 | Hauzenberg, Germany | 12 | 3.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `31.24.92.180` | 72 | 22.0% | Belarus / Minsk City / Minsk / Business network LTD | No apparent signal |
| 2 | `151.101.218.13` | 64 | 19.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `81.110.171.250` | 23 | 7.0% | United Kingdom / England / Manchester / Vmcbbuk | No apparent signal |
| 4 | `51.254.243.118` | 19 | 5.8% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 5 | `151.101.218.73` | 18 | 5.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `85.217.140.19` | 15 | 4.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.1` | 14 | 4.3% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 8 | `85.217.140.2` | 14 | 4.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `18.221.179.104` | 13 | 4.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `77.239.124.127` | 13 | 4.0% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |
| 11 | `85.217.140.18` | 13 | 4.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.20` | 13 | 4.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `45.194.67.120` | 12 | 3.7% | Brazil / São Paulo / São Paulo / Cloud Innovation Ltd | No apparent signal |
| 14 | `93.123.109.6` | 12 | 3.7% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 15 | `176.65.134.24` | 12 | 3.7% | Germany / Bavaria / Hauzenberg / Pfcloud UG | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 64 | 56.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `51.254.243.118` | 19 | 16.7% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |
| 3 | `151.101.218.73` | 18 | 15.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `18.221.179.104` | 13 | 11.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
