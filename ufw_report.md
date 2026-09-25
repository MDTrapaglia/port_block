# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4414
- Unique source IPs: 2372
- Unique countries/cities (24h): 340
- Unique destination ports: 2575

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 142 | 3.2% |
| 2 | `22` | 97 | 2.2% |
| 3 | `3389` | 36 | 0.8% |
| 4 | `8080` | 33 | 0.7% |
| 5 | `5060` | 31 | 0.7% |
| 6 | `8443` | 23 | 0.5% |
| 7 | `53` | 23 | 0.5% |
| 8 | `1433` | 23 | 0.5% |
| 9 | `2222` | 21 | 0.5% |
| 10 | `17000` | 20 | 0.5% |
| 11 | `9200` | 17 | 0.4% |
| 12 | `3306` | 16 | 0.4% |
| 13 | `27036` | 16 | 0.4% |
| 14 | `8888` | 15 | 0.3% |
| 15 | `8081` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4050 | 91.8% |
| 2 | `UDP` | 353 | 8.0% |
| 3 | `47` | 10 | 0.2% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.42` | 156 | 3.5% |
| 2 | `77.239.124.253` | 77 | 1.7% |
| 3 | `151.101.218.13` | 40 | 0.9% |
| 4 | `85.217.140.1` | 19 | 0.4% |
| 5 | `85.217.140.2` | 18 | 0.4% |
| 6 | `91.231.89.72` | 16 | 0.4% |
| 7 | `85.217.140.34` | 16 | 0.4% |
| 8 | `151.101.218.73` | 16 | 0.4% |
| 9 | `186.123.164.151` | 16 | 0.4% |
| 10 | `85.217.140.5` | 15 | 0.3% |
| 11 | `185.224.128.16` | 15 | 0.3% |
| 12 | `85.217.140.6` | 15 | 0.3% |
| 13 | `195.184.76.71` | 14 | 0.3% |
| 14 | `18.221.179.104` | 13 | 0.3% |
| 15 | `195.184.76.175` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3907 | 96.5% |
| 2 | `ACK+FIN+PSH` | 81 | 2.0% |
| 3 | `ACK+PSH` | 28 | 0.7% |
| 4 | `SYN+ECE+CWR` | 16 | 0.4% |
| 5 | `ACK+FIN` | 16 | 0.4% |
| 6 | `ACK` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4414 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `186.123.164.151` -> `27036` | 16 | 0.4% |
| 2 | `216.180.246.42` -> `14333` | 10 | 0.2% |
| 3 | `66.132.195.81` -> `587` | 8 | 0.2% |
| 4 | `151.101.218.13` -> `52782` | 8 | 0.2% |
| 5 | `216.180.246.42` -> `13563` | 8 | 0.2% |
| 6 | `216.180.246.42` -> `16900` | 8 | 0.2% |
| 7 | `130.12.180.65` -> `5555` | 7 | 0.2% |
| 8 | `216.180.246.42` -> `15242` | 7 | 0.2% |
| 9 | `216.180.246.42` -> `15443` | 7 | 0.2% |
| 10 | `216.180.246.42` -> `16888` | 7 | 0.2% |
| 11 | `151.101.218.13` -> `19331` | 7 | 0.2% |
| 12 | `151.101.218.13` -> `52078` | 6 | 0.1% |
| 13 | `45.142.193.161` -> `3389` | 6 | 0.1% |
| 14 | `216.180.246.42` -> `13753` | 6 | 0.1% |
| 15 | `216.180.246.42` -> `14281` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-24 04:00:00:00 | 135 | 3.1% |
| 2026-09-24 05:00:00:00 | 177 | 4.0% |
| 2026-09-24 06:00:00:00 | 181 | 4.1% |
| 2026-09-24 07:00:00:00 | 179 | 4.1% |
| 2026-09-24 08:00:00:00 | 182 | 4.1% |
| 2026-09-24 09:00:00:00 | 180 | 4.1% |
| 2026-09-24 10:00:00:00 | 180 | 4.1% |
| 2026-09-24 11:00:00:00 | 192 | 4.3% |
| 2026-09-24 12:00:00:00 | 199 | 4.5% |
| 2026-09-24 13:00:00:00 | 179 | 4.1% |
| 2026-09-24 14:00:00:00 | 199 | 4.5% |
| 2026-09-24 15:00:00:00 | 180 | 4.1% |
| 2026-09-24 16:00:00:00 | 187 | 4.2% |
| 2026-09-24 17:00:00:00 | 180 | 4.1% |
| 2026-09-24 18:00:00:00 | 180 | 4.1% |
| 2026-09-24 19:00:00:00 | 180 | 4.1% |
| 2026-09-24 20:00:00:00 | 183 | 4.1% |
| 2026-09-24 21:00:00:00 | 189 | 4.3% |
| 2026-09-24 22:00:00:00 | 185 | 4.2% |
| 2026-09-24 23:00:00:00 | 181 | 4.1% |
| 2026-09-25 00:00:00:00 | 190 | 4.3% |
| 2026-09-25 01:00:00:00 | 179 | 4.1% |
| 2026-09-25 02:00:00:00 | 194 | 4.4% |
| 2026-09-25 03:00:00:00 | 181 | 4.1% |
| 2026-09-25 04:00:00:00 | 42 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 156 | 34.0% |
| 2 | Paris, France | 96 | 20.9% |
| 3 | Gravelines, France | 80 | 17.4% |
| 4 | Buenos Aires, Argentina | 40 | 8.7% |
| 5 | Warrenton, United States | 27 | 5.9% |
| 6 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 16 | 3.5% |
| 7 | Córdoba, Argentina | 16 | 3.5% |
| 8 | Amsterdam, The Netherlands | 15 | 3.3% |
| 9 | Dublin, United States | 13 | 2.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.42` | 156 | 34.0% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `77.239.124.253` | 77 | 16.8% | France / Île-de-France / Paris / RocketCloud | No apparent signal |
| 3 | `151.101.218.13` | 40 | 8.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `85.217.140.1` | 19 | 4.1% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 5 | `85.217.140.2` | 18 | 3.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `91.231.89.72` | 16 | 3.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `85.217.140.34` | 16 | 3.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `151.101.218.73` | 16 | 3.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 9 | `186.123.164.151` | 16 | 3.5% | Argentina / Cordoba / Córdoba / AMX Argentina S.A | No apparent signal |
| 10 | `85.217.140.5` | 15 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `185.224.128.16` | 15 | 3.3% | The Netherlands / North Holland / Amsterdam / Alsycon B.V | No apparent signal |
| 12 | `85.217.140.6` | 15 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `195.184.76.71` | 14 | 3.1% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `18.221.179.104` | 13 | 2.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `195.184.76.175` | 13 | 2.8% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.42` | 156 | 69.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 40 | 17.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.73` | 16 | 7.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `18.221.179.104` | 13 | 5.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
