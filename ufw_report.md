# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4514
- Unique source IPs: 2553
- Unique countries/cities (24h): 312
- Unique destination ports: 2588

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 165 | 3.7% |
| 2 | `7680` | 142 | 3.1% |
| 3 | `22` | 64 | 1.4% |
| 4 | `8080` | 54 | 1.2% |
| 5 | `3389` | 43 | 1.0% |
| 6 | `1433` | 34 | 0.8% |
| 7 | `5060` | 31 | 0.7% |
| 8 | `53` | 28 | 0.6% |
| 9 | `21` | 23 | 0.5% |
| 10 | `3306` | 23 | 0.5% |
| 11 | `8081` | 22 | 0.5% |
| 12 | `8443` | 21 | 0.5% |
| 13 | `123` | 16 | 0.4% |
| 14 | `81` | 15 | 0.3% |
| 15 | `3128` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4167 | 92.3% |
| 2 | `UDP` | 342 | 7.6% |
| 3 | `47` | 4 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `108.78.173.95` | 87 | 1.9% |
| 2 | `151.101.218.13` | 73 | 1.6% |
| 3 | `46.232.234.191` | 26 | 0.6% |
| 4 | `73.69.184.37` | 23 | 0.5% |
| 5 | `151.101.218.73` | 15 | 0.3% |
| 6 | `87.120.104.79` | 14 | 0.3% |
| 7 | `45.198.224.125` | 14 | 0.3% |
| 8 | `91.231.89.69` | 13 | 0.3% |
| 9 | `91.230.168.211` | 13 | 0.3% |
| 10 | `195.184.76.185` | 12 | 0.3% |
| 11 | `91.231.89.224` | 12 | 0.3% |
| 12 | `195.184.76.198` | 12 | 0.3% |
| 13 | `91.231.89.238` | 12 | 0.3% |
| 14 | `91.231.89.87` | 12 | 0.3% |
| 15 | `91.231.89.150` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3933 | 94.4% |
| 2 | `ACK+FIN+PSH` | 166 | 4.0% |
| 3 | `ACK+PSH` | 36 | 0.9% |
| 4 | `ACK+FIN` | 25 | 0.6% |
| 5 | `SYN+ECE+CWR` | 6 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4513 | 100.0% |
| 2 | `wlan0` | 1 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `108.78.173.95` -> `7680` | 87 | 1.9% |
| 2 | `73.69.184.37` -> `7680` | 23 | 0.5% |
| 3 | `186.123.1.125` -> `1433` | 8 | 0.2% |
| 4 | `76.71.87.100` -> `7680` | 8 | 0.2% |
| 5 | `62.210.114.99` -> `3389` | 7 | 0.2% |
| 6 | `2.23.164.85` -> `56086` | 7 | 0.2% |
| 7 | `151.101.218.13` -> `56453` | 7 | 0.2% |
| 8 | `151.101.218.13` -> `49592` | 6 | 0.1% |
| 9 | `151.101.218.73` -> `54385` | 6 | 0.1% |
| 10 | `169.150.214.132` -> `56164` | 6 | 0.1% |
| 11 | `151.101.218.13` -> `56081` | 6 | 0.1% |
| 12 | `151.101.218.13` -> `1459` | 6 | 0.1% |
| 13 | `151.101.218.13` -> `54142` | 5 | 0.1% |
| 14 | `16.5.0.193` -> `27960` | 5 | 0.1% |
| 15 | `151.101.218.13` -> `54565` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-26 04:00:00:00 | 149 | 3.3% |
| 2026-10-26 05:00:00:00 | 204 | 4.5% |
| 2026-10-26 06:00:00:00 | 178 | 3.9% |
| 2026-10-26 07:00:00:00 | 181 | 4.0% |
| 2026-10-26 08:00:00:00 | 180 | 4.0% |
| 2026-10-26 09:00:00:00 | 197 | 4.4% |
| 2026-10-26 10:00:00:00 | 185 | 4.1% |
| 2026-10-26 11:00:00:00 | 187 | 4.1% |
| 2026-10-26 12:00:00:00 | 181 | 4.0% |
| 2026-10-26 13:00:00:00 | 220 | 4.9% |
| 2026-10-26 14:00:00:00 | 191 | 4.2% |
| 2026-10-26 15:00:00:00 | 187 | 4.1% |
| 2026-10-26 16:00:00:00 | 181 | 4.0% |
| 2026-10-26 17:00:00:00 | 179 | 4.0% |
| 2026-10-26 18:00:00:00 | 193 | 4.3% |
| 2026-10-26 19:00:00:00 | 189 | 4.2% |
| 2026-10-26 20:00:00:00 | 182 | 4.0% |
| 2026-10-26 21:00:00:00 | 194 | 4.3% |
| 2026-10-26 22:00:00:00 | 180 | 4.0% |
| 2026-10-26 23:00:00:00 | 203 | 4.5% |
| 2026-10-27 00:00:00:00 | 178 | 3.9% |
| 2026-10-27 01:00:00:00 | 189 | 4.2% |
| 2026-10-27 02:00:00:00 | 180 | 4.0% |
| 2026-10-27 03:00:00:00 | 181 | 4.0% |
| 2026-10-27 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Leander, United States | 87 | 24.9% |
| 2 | Buenos Aires, Argentina | 73 | 20.9% |
| 3 | Gravelines, France | 61 | 17.4% |
| 4 | Frankfurt am Main, Germany | 26 | 7.4% |
| 5 | Warrenton, United States | 24 | 6.9% |
| 6 | Essex Junction, United States | 23 | 6.6% |
| 7 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 15 | 4.3% |
| 8 | Sandefjord, Norway | 14 | 4.0% |
| 9 | Stockholm, Sweden | 14 | 4.0% |
| 10 | Hillsboro, United States | 13 | 3.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `108.78.173.95` | 87 | 24.9% | United States / Texas / Leander / AT&T Enterprises, LLC | No apparent signal |
| 2 | `151.101.218.13` | 73 | 20.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `46.232.234.191` | 26 | 7.4% | Germany / Hesse / Frankfurt am Main / Joy Services | No apparent signal |
| 4 | `73.69.184.37` | 23 | 6.6% | United States / Vermont / Essex Junction / Comcast IP Services, L.L.C. | No apparent signal |
| 5 | `151.101.218.73` | 15 | 4.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `87.120.104.79` | 14 | 4.0% | Norway / Vestfold / Sandefjord / Sino Worldwide Trading Limited | No apparent signal |
| 7 | `45.198.224.125` | 14 | 4.0% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 8 | `91.231.89.69` | 13 | 3.7% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `91.230.168.211` | 13 | 3.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 10 | `195.184.76.185` | 12 | 3.4% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 11 | `91.231.89.224` | 12 | 3.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `195.184.76.198` | 12 | 3.4% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 13 | `91.231.89.238` | 12 | 3.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.231.89.87` | 12 | 3.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `91.231.89.150` | 12 | 3.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.13` | 73 | 83.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `151.101.218.73` | 15 | 17.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
