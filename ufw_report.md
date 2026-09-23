# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4401
- Unique source IPs: 2426
- Unique countries/cities (24h): 322
- Unique destination ports: 2520

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 167 | 3.8% |
| 2 | `22` | 116 | 2.6% |
| 3 | `unknown` | 54 | 1.2% |
| 4 | `53` | 46 | 1.0% |
| 5 | `3389` | 39 | 0.9% |
| 6 | `8080` | 34 | 0.8% |
| 7 | `1433` | 31 | 0.7% |
| 8 | `8443` | 29 | 0.7% |
| 9 | `17000` | 27 | 0.6% |
| 10 | `5060` | 25 | 0.6% |
| 11 | `17001` | 22 | 0.5% |
| 12 | `2222` | 21 | 0.5% |
| 13 | `3000` | 21 | 0.5% |
| 14 | `6036` | 18 | 0.4% |
| 15 | `21` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4003 | 91.0% |
| 2 | `UDP` | 344 | 7.8% |
| 3 | `2` | 42 | 1.0% |
| 4 | `47` | 9 | 0.2% |
| 5 | `132` | 3 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.168.100.64` | 41 | 0.9% |
| 2 | `51.159.125.208` | 27 | 0.6% |
| 3 | `185.242.3.254` | 19 | 0.4% |
| 4 | `2.22.149.136` | 19 | 0.4% |
| 5 | `85.217.140.1` | 18 | 0.4% |
| 6 | `85.217.140.35` | 18 | 0.4% |
| 7 | `195.184.76.116` | 15 | 0.3% |
| 8 | `151.101.218.13` | 15 | 0.3% |
| 9 | `85.217.140.20` | 14 | 0.3% |
| 10 | `85.217.140.7` | 14 | 0.3% |
| 11 | `85.217.140.29` | 14 | 0.3% |
| 12 | `85.217.140.34` | 14 | 0.3% |
| 13 | `172.110.223.173` | 14 | 0.3% |
| 14 | `85.217.140.33` | 13 | 0.3% |
| 15 | `91.230.168.124` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3872 | 96.7% |
| 2 | `ACK+FIN+PSH` | 76 | 1.9% |
| 3 | `ACK+PSH` | 32 | 0.8% |
| 4 | `SYN+ECE+CWR` | 17 | 0.4% |
| 5 | `ACK+FIN` | 4 | 0.1% |
| 6 | `RST` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4359 | 99.0% |
| 2 | `wlan0` | 42 | 1.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.168.100.64` -> `unknown` | 41 | 0.9% |
| 2 | `2.23.164.77` -> `57126` | 7 | 0.2% |
| 3 | `216.180.246.75` -> `53` | 7 | 0.2% |
| 4 | `81.161.239.10` -> `3389` | 6 | 0.1% |
| 5 | `186.123.1.125` -> `1433` | 6 | 0.1% |
| 6 | `2.23.164.166` -> `56372` | 6 | 0.1% |
| 7 | `193.90.12.122` -> `23` | 6 | 0.1% |
| 8 | `130.12.180.65` -> `5555` | 5 | 0.1% |
| 9 | `89.42.231.200` -> `17000` | 5 | 0.1% |
| 10 | `2.22.149.136` -> `53932` | 5 | 0.1% |
| 11 | `95.100.88.67` -> `6299` | 5 | 0.1% |
| 12 | `170.51.241.171` -> `57158` | 5 | 0.1% |
| 13 | `57.144.206.145` -> `57410` | 5 | 0.1% |
| 14 | `66.132.172.182` -> `53` | 5 | 0.1% |
| 15 | `151.101.218.13` -> `57867` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-22 04:00:00:00 | 136 | 3.1% |
| 2026-09-22 05:00:00:00 | 178 | 4.0% |
| 2026-09-22 06:00:00:00 | 182 | 4.1% |
| 2026-09-22 07:00:00:00 | 180 | 4.1% |
| 2026-09-22 08:00:00:00 | 178 | 4.0% |
| 2026-09-22 09:00:00:00 | 180 | 4.1% |
| 2026-09-22 10:00:00:00 | 193 | 4.4% |
| 2026-09-22 11:00:00:00 | 191 | 4.3% |
| 2026-09-22 12:00:00:00 | 181 | 4.1% |
| 2026-09-22 13:00:00:00 | 201 | 4.6% |
| 2026-09-22 14:00:00:00 | 179 | 4.1% |
| 2026-09-22 15:00:00:00 | 183 | 4.2% |
| 2026-09-22 16:00:00:00 | 181 | 4.1% |
| 2026-09-22 17:00:00:00 | 179 | 4.1% |
| 2026-09-22 18:00:00:00 | 179 | 4.1% |
| 2026-09-22 19:00:00:00 | 180 | 4.1% |
| 2026-09-22 20:00:00:00 | 182 | 4.1% |
| 2026-09-22 21:00:00:00 | 179 | 4.1% |
| 2026-09-22 22:00:00:00 | 195 | 4.4% |
| 2026-09-22 23:00:00:00 | 180 | 4.1% |
| 2026-09-23 00:00:00:00 | 180 | 4.1% |
| 2026-09-23 01:00:00:00 | 198 | 4.5% |
| 2026-09-23 02:00:00:00 | 180 | 4.1% |
| 2026-09-23 03:00:00:00 | 181 | 4.1% |
| 2026-09-23 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 87 | 32.5% |
| 2 | Paris, France | 45 | 16.8% |
| 3 | private | 41 | 15.3% |
| 4 | Buenos Aires, Argentina | 34 | 12.7% |
| 5 | Frankfurt am Main, Germany | 19 | 7.1% |
| 6 | Warrenton, United States | 15 | 5.6% |
| 7 | Hong Kong, Hong Kong | 14 | 5.2% |
| 8 | Hillsboro, United States | 13 | 4.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.168.100.64` | 41 | 15.3% | private | Private/CGNAT |
| 2 | `51.159.125.208` | 27 | 10.1% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 3 | `185.242.3.254` | 19 | 7.1% | Germany / Hesse / Frankfurt am Main / Felcloud | No apparent signal |
| 4 | `2.22.149.136` | 19 | 7.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 5 | `85.217.140.1` | 18 | 6.7% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 6 | `85.217.140.35` | 18 | 6.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `195.184.76.116` | 15 | 5.6% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 8 | `151.101.218.13` | 15 | 5.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 9 | `85.217.140.20` | 14 | 5.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.7` | 14 | 5.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.29` | 14 | 5.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.34` | 14 | 5.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `172.110.223.173` | 14 | 5.2% | Hong Kong / Kowloon / Hong Kong / Dedires LLC | No apparent signal |
| 14 | `85.217.140.33` | 13 | 4.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `91.230.168.124` | 13 | 4.9% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `51.159.125.208` | 27 | 44.3% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `2.22.149.136` | 19 | 31.1% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `151.101.218.13` | 15 | 24.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
