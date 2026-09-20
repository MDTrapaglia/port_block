# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 610
- Unique source IPs: 469
- Unique countries/cities (24h): 100
- Unique destination ports: 433

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 25 | 4.1% |
| 2 | `22` | 15 | 2.5% |
| 3 | `4369` | 10 | 1.6% |
| 4 | `53` | 8 | 1.3% |
| 5 | `8080` | 7 | 1.1% |
| 6 | `4343` | 7 | 1.1% |
| 7 | `1433` | 5 | 0.8% |
| 8 | `6036` | 5 | 0.8% |
| 9 | `554` | 5 | 0.8% |
| 10 | `27017` | 5 | 0.8% |
| 11 | `1521` | 4 | 0.7% |
| 12 | `81` | 4 | 0.7% |
| 13 | `123` | 4 | 0.7% |
| 14 | `3389` | 4 | 0.7% |
| 15 | `6379` | 4 | 0.7% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 551 | 90.3% |
| 2 | `UDP` | 58 | 9.5% |
| 3 | `47` | 1 | 0.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.53` | 23 | 3.8% |
| 2 | `216.180.246.143` | 21 | 3.4% |
| 3 | `45.128.157.201` | 20 | 3.3% |
| 4 | `16.5.0.234` | 9 | 1.5% |
| 5 | `45.135.193.159` | 6 | 1.0% |
| 6 | `68.183.175.158` | 4 | 0.7% |
| 7 | `217.60.76.226` | 3 | 0.5% |
| 8 | `85.217.140.22` | 3 | 0.5% |
| 9 | `185.242.226.11` | 3 | 0.5% |
| 10 | `85.217.140.6` | 3 | 0.5% |
| 11 | `85.217.140.35` | 3 | 0.5% |
| 12 | `141.98.83.48` | 3 | 0.5% |
| 13 | `100.28.191.174` | 3 | 0.5% |
| 14 | `193.163.125.199` | 3 | 0.5% |
| 15 | `160.119.76.127` | 3 | 0.5% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 551 | 100.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 610 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.143` -> `4369` | 10 | 1.6% |
| 2 | `216.180.246.143` -> `4343` | 7 | 1.1% |
| 3 | `216.180.246.53` -> `22` | 5 | 0.8% |
| 4 | `216.180.246.143` -> `4248` | 4 | 0.7% |
| 5 | `216.180.246.53` -> `23` | 3 | 0.5% |
| 6 | `216.180.246.53` -> `81` | 3 | 0.5% |
| 7 | `216.180.246.53` -> `8880` | 3 | 0.5% |
| 8 | `216.180.246.53` -> `25461` | 3 | 0.5% |
| 9 | `187.34.86.99` -> `23` | 2 | 0.3% |
| 10 | `217.60.76.226` -> `5290` | 2 | 0.3% |
| 11 | `31.132.90.3` -> `23` | 2 | 0.3% |
| 12 | `51.222.40.109` -> `554` | 2 | 0.3% |
| 13 | `185.93.89.42` -> `1450` | 2 | 0.3% |
| 14 | `34.77.64.106` -> `25` | 2 | 0.3% |
| 15 | `207.175.24.236` -> `6379` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-20 00:00:00:00 | 24 | 3.9% |
| 2026-09-20 01:00:00:00 | 179 | 29.3% |
| 2026-09-20 02:00:00:00 | 180 | 29.5% |
| 2026-09-20 03:00:00:00 | 181 | 29.7% |
| 2026-09-20 04:00:00:00 | 46 | 7.5% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 44 | 40.0% |
| 2 | Hengevelde, The Netherlands | 20 | 18.2% |
| 3 | São Paulo, Brazil | 9 | 8.2% |
| 4 | Gravelines, France | 9 | 8.2% |
| 5 | Langen, Germany | 6 | 5.5% |
| 6 | Amsterdam, The Netherlands | 6 | 5.5% |
| 7 | Santa Clara, United States | 4 | 3.6% |
| 8 | Eygelshoven, The Netherlands | 3 | 2.7% |
| 9 | Panama City, Panama | 3 | 2.7% |
| 10 | Ashburn, United States | 3 | 2.7% |
| 11 | Leeds, United Kingdom | 3 | 2.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.53` | 23 | 20.9% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `216.180.246.143` | 21 | 19.1% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 3 | `45.128.157.201` | 20 | 18.2% | The Netherlands / Overijssel / Hengevelde / MC-Node | Mobile/CGNAT (lte) |
| 4 | `16.5.0.234` | 9 | 8.2% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 5 | `45.135.193.159` | 6 | 5.5% | Germany / Hesse / Langen / Pfcloud UG | No apparent signal |
| 6 | `68.183.175.158` | 4 | 3.6% | United States / California / Santa Clara / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 7 | `217.60.76.226` | 3 | 2.7% | The Netherlands / Limburg / Eygelshoven / Iryna Ivanenko | No apparent signal |
| 8 | `85.217.140.22` | 3 | 2.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `185.242.226.11` | 3 | 2.7% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 10 | `85.217.140.6` | 3 | 2.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.35` | 3 | 2.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `141.98.83.48` | 3 | 2.7% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 13 | `100.28.191.174` | 3 | 2.7% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 14 | `193.163.125.199` | 3 | 2.7% | United Kingdom / England / Leeds / Constantine Cybersecurity LTD | No apparent signal |
| 15 | `160.119.76.127` | 3 | 2.7% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.53` | 23 | 42.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `216.180.246.143` | 21 | 38.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 3 | `68.183.175.158` | 4 | 7.4% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / DigitalOcean, LLC |
| 4 | `141.98.83.48` | 3 | 5.6% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 5 | `100.28.191.174` | 3 | 5.6% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
