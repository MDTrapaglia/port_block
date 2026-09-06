# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 711
- Unique source IPs: 576
- Unique countries/cities (24h): 148
- Unique destination ports: 550

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 38 | 5.3% |
| 2 | `22` | 10 | 1.4% |
| 3 | `8080` | 8 | 1.1% |
| 4 | `1433` | 6 | 0.8% |
| 5 | `2000` | 5 | 0.7% |
| 6 | `6379` | 5 | 0.7% |
| 7 | `44196` | 5 | 0.7% |
| 8 | `5985` | 4 | 0.6% |
| 9 | `8000` | 4 | 0.6% |
| 10 | `27017` | 4 | 0.6% |
| 11 | `5060` | 4 | 0.6% |
| 12 | `9200` | 4 | 0.6% |
| 13 | `8081` | 4 | 0.6% |
| 14 | `53` | 4 | 0.6% |
| 15 | `88` | 3 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 635 | 89.3% |
| 2 | `UDP` | 73 | 10.3% |
| 3 | `47` | 3 | 0.4% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `16.5.0.237` | 13 | 1.8% |
| 2 | `16.5.0.242` | 13 | 1.8% |
| 3 | `16.5.0.239` | 12 | 1.7% |
| 4 | `16.5.0.238` | 9 | 1.3% |
| 5 | `151.101.216.159` | 6 | 0.8% |
| 6 | `16.5.0.240` | 5 | 0.7% |
| 7 | `85.217.140.35` | 4 | 0.6% |
| 8 | `170.64.151.177` | 4 | 0.6% |
| 9 | `85.217.140.22` | 4 | 0.6% |
| 10 | `85.217.140.34` | 4 | 0.6% |
| 11 | `16.5.0.236` | 4 | 0.6% |
| 12 | `85.217.140.6` | 3 | 0.4% |
| 13 | `45.194.67.120` | 3 | 0.4% |
| 14 | `34.197.70.90` | 3 | 0.4% |
| 15 | `77.239.124.127` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 627 | 98.7% |
| 2 | `ACK+FIN+PSH` | 6 | 0.9% |
| 3 | `ACK+PSH` | 2 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 711 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `151.101.216.159` -> `44196` | 5 | 0.7% |
| 2 | `77.239.124.127` -> `23` | 2 | 0.3% |
| 3 | `66.132.186.190` -> `2000` | 2 | 0.3% |
| 4 | `207.175.16.107` -> `23` | 2 | 0.3% |
| 5 | `66.132.195.49` -> `135` | 2 | 0.3% |
| 6 | `34.62.215.55` -> `6379` | 2 | 0.3% |
| 7 | `94.255.128.177` -> `8080` | 2 | 0.3% |
| 8 | `104.54.87.50` -> `23` | 2 | 0.3% |
| 9 | `141.98.83.48` -> `3283` | 2 | 0.3% |
| 10 | `47.251.174.175` -> `88` | 1 | 0.1% |
| 11 | `16.5.0.237` -> `8182` | 1 | 0.1% |
| 12 | `16.5.0.237` -> `20002` | 1 | 0.1% |
| 13 | `216.25.89.157` -> `9333` | 1 | 0.1% |
| 14 | `16.5.0.239` -> `8020` | 1 | 0.1% |
| 15 | `85.217.140.6` -> `35950` | 1 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-06 00:00:00:00 | 119 | 16.7% |
| 2026-09-06 01:00:00:00 | 181 | 25.5% |
| 2026-09-06 02:00:00:00 | 186 | 26.2% |
| 2026-09-06 03:00:00:00 | 180 | 25.3% |
| 2026-09-06 04:00:00:00 | 45 | 6.3% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | São Paulo, Brazil | 59 | 65.6% |
| 2 | Gravelines, France | 15 | 16.7% |
| 3 | Buenos Aires, Argentina | 6 | 6.7% |
| 4 | Sydney, Australia | 4 | 4.4% |
| 5 | Ashburn, United States | 3 | 3.3% |
| 6 | Amsterdam, The Netherlands | 3 | 3.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `16.5.0.237` | 13 | 14.4% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 2 | `16.5.0.242` | 13 | 14.4% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 3 | `16.5.0.239` | 12 | 13.3% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 4 | `16.5.0.238` | 9 | 10.0% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 5 | `151.101.216.159` | 6 | 6.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `16.5.0.240` | 5 | 5.6% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 7 | `85.217.140.35` | 4 | 4.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `170.64.151.177` | 4 | 4.4% | Australia / New South Wales / Sydney / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 9 | `85.217.140.22` | 4 | 4.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.34` | 4 | 4.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `16.5.0.236` | 4 | 4.4% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 12 | `85.217.140.6` | 3 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `45.194.67.120` | 3 | 3.3% | Brazil / São Paulo / São Paulo / Cloud Innovation Ltd | No apparent signal |
| 14 | `34.197.70.90` | 3 | 3.3% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `77.239.124.127` | 3 | 3.3% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.216.159` | 6 | 46.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `170.64.151.177` | 4 | 30.8% | Hosting/Cloud (digitalocean) | Australia / New South Wales / Sydney / DigitalOcean, LLC |
| 3 | `34.197.70.90` | 3 | 23.1% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
