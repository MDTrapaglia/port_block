# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4394
- Unique source IPs: 2518
- Unique countries/cities (24h): 308
- Unique destination ports: 2474

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 172 | 3.9% |
| 2 | `22` | 73 | 1.7% |
| 3 | `3389` | 43 | 1.0% |
| 4 | `53` | 39 | 0.9% |
| 5 | `8080` | 38 | 0.9% |
| 6 | `5060` | 38 | 0.9% |
| 7 | `8443` | 21 | 0.5% |
| 8 | `8000` | 21 | 0.5% |
| 9 | `1723` | 21 | 0.5% |
| 10 | `1433` | 21 | 0.5% |
| 11 | `3306` | 17 | 0.4% |
| 12 | `9090` | 17 | 0.4% |
| 13 | `8081` | 17 | 0.4% |
| 14 | `8888` | 16 | 0.4% |
| 15 | `21` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4066 | 92.5% |
| 2 | `UDP` | 324 | 7.4% |
| 3 | `47` | 2 | 0.0% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.220` | 187 | 4.3% |
| 2 | `160.119.76.173` | 17 | 0.4% |
| 3 | `45.198.224.125` | 14 | 0.3% |
| 4 | `91.230.168.124` | 13 | 0.3% |
| 5 | `91.231.89.130` | 13 | 0.3% |
| 6 | `91.231.89.0` | 13 | 0.3% |
| 7 | `91.231.89.150` | 13 | 0.3% |
| 8 | `79.124.59.82` | 13 | 0.3% |
| 9 | `80.82.77.139` | 12 | 0.3% |
| 10 | `195.184.76.180` | 12 | 0.3% |
| 11 | `195.184.76.175` | 12 | 0.3% |
| 12 | `134.122.121.37` | 12 | 0.3% |
| 13 | `91.196.152.123` | 12 | 0.3% |
| 14 | `23.40.188.42` | 12 | 0.3% |
| 15 | `91.196.152.222` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3943 | 97.0% |
| 2 | `ACK+FIN+PSH` | 73 | 1.8% |
| 3 | `ACK+PSH` | 39 | 1.0% |
| 4 | `SYN+ECE+CWR` | 6 | 0.1% |
| 5 | `ACK` | 4 | 0.1% |
| 6 | `ACK+FIN` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4394 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.220` -> `9137` | 11 | 0.3% |
| 2 | `216.180.246.220` -> `9073` | 10 | 0.2% |
| 3 | `216.180.246.220` -> `9083` | 10 | 0.2% |
| 4 | `216.180.246.220` -> `9081` | 9 | 0.2% |
| 5 | `216.180.246.220` -> `9100` | 9 | 0.2% |
| 6 | `216.180.246.220` -> `9080` | 8 | 0.2% |
| 7 | `216.180.246.220` -> `9094` | 8 | 0.2% |
| 8 | `216.180.246.220` -> `9095` | 8 | 0.2% |
| 9 | `216.180.246.220` -> `9114` | 8 | 0.2% |
| 10 | `216.180.246.220` -> `9122` | 8 | 0.2% |
| 11 | `216.180.246.101` -> `8080` | 8 | 0.2% |
| 12 | `216.180.246.220` -> `9132` | 8 | 0.2% |
| 13 | `178.20.210.152` -> `1723` | 7 | 0.2% |
| 14 | `62.210.114.99` -> `3389` | 7 | 0.2% |
| 15 | `216.180.246.220` -> `9092` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-27 04:00:00:00 | 135 | 3.1% |
| 2026-10-27 05:00:00:00 | 177 | 4.0% |
| 2026-10-27 06:00:00:00 | 183 | 4.2% |
| 2026-10-27 07:00:00:00 | 179 | 4.1% |
| 2026-10-27 08:00:00:00 | 179 | 4.1% |
| 2026-10-27 09:00:00:00 | 182 | 4.1% |
| 2026-10-27 10:00:00:00 | 186 | 4.2% |
| 2026-10-27 11:00:00:00 | 181 | 4.1% |
| 2026-10-27 12:00:00:00 | 183 | 4.2% |
| 2026-10-27 13:00:00:00 | 189 | 4.3% |
| 2026-10-27 14:00:00:00 | 180 | 4.1% |
| 2026-10-27 15:00:00:00 | 179 | 4.1% |
| 2026-10-27 16:00:00:00 | 180 | 4.1% |
| 2026-10-27 17:00:00:00 | 183 | 4.2% |
| 2026-10-27 18:00:00:00 | 181 | 4.1% |
| 2026-10-27 19:00:00:00 | 180 | 4.1% |
| 2026-10-27 20:00:00:00 | 191 | 4.3% |
| 2026-10-27 21:00:00:00 | 185 | 4.2% |
| 2026-10-27 22:00:00:00 | 197 | 4.5% |
| 2026-10-27 23:00:00:00 | 180 | 4.1% |
| 2026-10-28 00:00:00:00 | 197 | 4.5% |
| 2026-10-28 01:00:00:00 | 180 | 4.1% |
| 2026-10-28 02:00:00:00 | 180 | 4.1% |
| 2026-10-28 03:00:00:00 | 181 | 4.1% |
| 2026-10-28 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 187 | 51.1% |
| 2 | Gravelines, France | 39 | 10.7% |
| 3 | Warrenton, United States | 24 | 6.6% |
| 4 | Roubaix, France | 23 | 6.3% |
| 5 | Amsterdam, The Netherlands | 17 | 4.6% |
| 6 | Stockholm, Sweden | 14 | 3.8% |
| 7 | Hillsboro, United States | 13 | 3.6% |
| 8 | Sopot, Bulgaria | 13 | 3.6% |
| 9 | Amsterdam, Netherlands | 12 | 3.3% |
| 10 | North Bergen, United States | 12 | 3.3% |
| 11 | Buenos Aires, Argentina | 12 | 3.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.220` | 187 | 51.1% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `160.119.76.173` | 17 | 4.6% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |
| 3 | `45.198.224.125` | 14 | 3.8% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 4 | `91.230.168.124` | 13 | 3.6% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 5 | `91.231.89.130` | 13 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 6 | `91.231.89.0` | 13 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `91.231.89.150` | 13 | 3.6% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 8 | `79.124.59.82` | 13 | 3.6% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 9 | `80.82.77.139` | 12 | 3.3% | Netherlands / North Holland / Amsterdam / IP Volume inc | No apparent signal |
| 10 | `195.184.76.180` | 12 | 3.3% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 11 | `195.184.76.175` | 12 | 3.3% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 12 | `134.122.121.37` | 12 | 3.3% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `91.196.152.123` | 12 | 3.3% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 14 | `23.40.188.42` | 12 | 3.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. | CDN/Edge (akamai) |
| 15 | `91.196.152.222` | 11 | 3.0% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.220` | 187 | 88.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `134.122.121.37` | 12 | 5.7% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 3 | `23.40.188.42` | 12 | 5.7% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
