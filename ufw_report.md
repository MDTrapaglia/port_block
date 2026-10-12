# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4457
- Unique source IPs: 2475
- Unique countries/cities (24h): 296
- Unique destination ports: 2511

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 300 | 6.7% |
| 2 | `22` | 101 | 2.3% |
| 3 | `8080` | 43 | 1.0% |
| 4 | `5060` | 40 | 0.9% |
| 5 | `3389` | 31 | 0.7% |
| 6 | `53` | 22 | 0.5% |
| 7 | `8081` | 20 | 0.4% |
| 8 | `123` | 18 | 0.4% |
| 9 | `3306` | 17 | 0.4% |
| 10 | `81` | 17 | 0.4% |
| 11 | `5432` | 17 | 0.4% |
| 12 | `1723` | 16 | 0.4% |
| 13 | `8000` | 16 | 0.4% |
| 14 | `6379` | 16 | 0.4% |
| 15 | `5038` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4122 | 92.5% |
| 2 | `UDP` | 326 | 7.3% |
| 3 | `47` | 9 | 0.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `72.47.208.106` | 124 | 2.8% |
| 2 | `216.180.246.248` | 118 | 2.6% |
| 3 | `150.241.96.68` | 83 | 1.9% |
| 4 | `50.224.83.237` | 55 | 1.2% |
| 5 | `79.124.59.106` | 19 | 0.4% |
| 6 | `151.101.218.13` | 19 | 0.4% |
| 7 | `45.198.224.125` | 16 | 0.4% |
| 8 | `85.217.140.27` | 16 | 0.4% |
| 9 | `85.217.140.5` | 14 | 0.3% |
| 10 | `85.217.140.29` | 14 | 0.3% |
| 11 | `151.101.218.73` | 14 | 0.3% |
| 12 | `85.217.140.28` | 13 | 0.3% |
| 13 | `85.217.140.18` | 13 | 0.3% |
| 14 | `113.57.144.218` | 13 | 0.3% |
| 15 | `3.151.116.231` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3960 | 96.1% |
| 2 | `ACK+FIN+PSH` | 118 | 2.9% |
| 3 | `ACK+PSH` | 19 | 0.5% |
| 4 | `ACK+FIN` | 12 | 0.3% |
| 5 | `SYN+ECE+CWR` | 10 | 0.2% |
| 6 | `ACK+RST` | 2 | 0.0% |
| 7 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4457 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `72.47.208.106` -> `23` | 124 | 2.8% |
| 2 | `50.224.83.237` -> `23` | 55 | 1.2% |
| 3 | `216.180.246.248` -> `5123` | 12 | 0.3% |
| 4 | `45.198.224.124` -> `81` | 9 | 0.2% |
| 5 | `216.180.246.248` -> `5122` | 8 | 0.2% |
| 6 | `23.64.58.25` -> `59152` | 8 | 0.2% |
| 7 | `216.180.246.248` -> `5431` | 8 | 0.2% |
| 8 | `45.198.224.125` -> `9090` | 7 | 0.2% |
| 9 | `45.205.1.160` -> `6036` | 7 | 0.2% |
| 10 | `151.101.218.13` -> `57711` | 7 | 0.2% |
| 11 | `216.180.246.248` -> `5062` | 7 | 0.2% |
| 12 | `216.180.246.248` -> `5080` | 7 | 0.2% |
| 13 | `216.180.246.65` -> `8080` | 7 | 0.2% |
| 14 | `216.180.246.248` -> `5090` | 7 | 0.2% |
| 15 | `216.180.246.248` -> `5249` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-11 04:00:00:00 | 140 | 3.1% |
| 2026-10-11 05:00:00:00 | 179 | 4.0% |
| 2026-10-11 06:00:00:00 | 180 | 4.0% |
| 2026-10-11 07:00:00:00 | 179 | 4.0% |
| 2026-10-11 08:00:00:00 | 180 | 4.0% |
| 2026-10-11 09:00:00:00 | 178 | 4.0% |
| 2026-10-11 10:00:00:00 | 202 | 4.5% |
| 2026-10-11 11:00:00:00 | 187 | 4.2% |
| 2026-10-11 12:00:00:00 | 182 | 4.1% |
| 2026-10-11 13:00:00:00 | 180 | 4.0% |
| 2026-10-11 14:00:00:00 | 180 | 4.0% |
| 2026-10-11 15:00:00:00 | 180 | 4.0% |
| 2026-10-11 16:00:00:00 | 180 | 4.0% |
| 2026-10-11 17:00:00:00 | 180 | 4.0% |
| 2026-10-11 18:00:00:00 | 180 | 4.0% |
| 2026-10-11 19:00:00:00 | 179 | 4.0% |
| 2026-10-11 20:00:00:00 | 186 | 4.2% |
| 2026-10-11 21:00:00:00 | 216 | 4.8% |
| 2026-10-11 22:00:00:00 | 187 | 4.2% |
| 2026-10-11 23:00:00:00 | 202 | 4.5% |
| 2026-10-12 00:00:00:00 | 184 | 4.1% |
| 2026-10-12 01:00:00:00 | 203 | 4.6% |
| 2026-10-12 02:00:00:00 | 179 | 4.0% |
| 2026-10-12 03:00:00:00 | 188 | 4.2% |
| 2026-10-12 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Tempe, United States | 124 | 22.8% |
| 2 | Massy, France | 118 | 21.7% |
| 3 | Helsinki, Finland | 83 | 15.3% |
| 4 | Gravelines, France | 70 | 12.9% |
| 5 | Humble, United States | 55 | 10.1% |
| 6 | Sopot, Bulgaria | 19 | 3.5% |
| 7 | Buenos Aires, Argentina | 19 | 3.5% |
| 8 | Stockholm, Sweden | 16 | 2.9% |
| 9 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 14 | 2.6% |
| 10 | Wuhan, China | 13 | 2.4% |
| 11 | Dublin, United States | 12 | 2.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `72.47.208.106` | 124 | 22.8% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 2 | `216.180.246.248` | 118 | 21.7% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 3 | `150.241.96.68` | 83 | 15.3% | Finland / Uusimaa / Helsinki / xorek.cloud International LTD | No apparent signal |
| 4 | `50.224.83.237` | 55 | 10.1% | United States / Texas / Humble / Comcast Cable Communications, LLC | No apparent signal |
| 5 | `79.124.59.106` | 19 | 3.5% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 6 | `151.101.218.13` | 19 | 3.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `45.198.224.125` | 16 | 2.9% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 8 | `85.217.140.27` | 16 | 2.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.5` | 14 | 2.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.29` | 14 | 2.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `151.101.218.73` | 14 | 2.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 12 | `85.217.140.28` | 13 | 2.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `85.217.140.18` | 13 | 2.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `113.57.144.218` | 13 | 2.4% | China / Hubei / Wuhan / CNC Group CHINA169 Hubei Province Network | No apparent signal |
| 15 | `3.151.116.231` | 12 | 2.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.248` | 118 | 72.4% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 19 | 11.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.73` | 14 | 8.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `3.151.116.231` | 12 | 7.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
