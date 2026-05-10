# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 610
- Unique source IPs: 518
- Unique countries/cities (24h): 116
- Unique destination ports: 461

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 18 | 3.0% |
| 2 | `8080` | 10 | 1.6% |
| 3 | `5060` | 8 | 1.3% |
| 4 | `5555` | 7 | 1.1% |
| 5 | `81` | 7 | 1.1% |
| 6 | `83` | 6 | 1.0% |
| 7 | `22` | 6 | 1.0% |
| 8 | `82` | 5 | 0.8% |
| 9 | `8333` | 5 | 0.8% |
| 10 | `88` | 5 | 0.8% |
| 11 | `3000` | 5 | 0.8% |
| 12 | `3389` | 5 | 0.8% |
| 13 | `8083` | 4 | 0.7% |
| 14 | `8443` | 4 | 0.7% |
| 15 | `1194` | 4 | 0.7% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 541 | 88.7% |
| 2 | `UDP` | 69 | 11.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `204.76.203.212` | 28 | 4.6% |
| 2 | `176.65.139.8` | 4 | 0.7% |
| 3 | `69.17.52.1` | 4 | 0.7% |
| 4 | `98.90.43.197` | 4 | 0.7% |
| 5 | `17.57.144.152` | 4 | 0.7% |
| 6 | `200.114.86.153` | 3 | 0.5% |
| 7 | `124.198.131.185` | 3 | 0.5% |
| 8 | `100.49.117.77` | 3 | 0.5% |
| 9 | `3.131.24.55` | 3 | 0.5% |
| 10 | `86.54.31.38` | 3 | 0.5% |
| 11 | `167.71.26.229` | 3 | 0.5% |
| 12 | `198.235.24.178` | 3 | 0.5% |
| 13 | `147.185.133.142` | 3 | 0.5% |
| 14 | `89.248.163.48` | 3 | 0.5% |
| 15 | `85.217.149.41` | 2 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 533 | 98.5% |
| 2 | `ACK+PSH` | 6 | 1.1% |
| 3 | `SYN+ECE+CWR` | 2 | 0.4% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 610 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `204.76.203.212` -> `83` | 6 | 1.0% |
| 2 | `204.76.203.212` -> `81` | 6 | 1.0% |
| 3 | `204.76.203.212` -> `82` | 5 | 0.8% |
| 4 | `176.65.139.8` -> `5555` | 4 | 0.7% |
| 5 | `69.17.52.1` -> `8333` | 4 | 0.7% |
| 6 | `204.76.203.212` -> `88` | 4 | 0.7% |
| 7 | `204.76.203.212` -> `8080` | 4 | 0.7% |
| 8 | `17.57.144.152` -> `55854` | 4 | 0.7% |
| 9 | `124.198.131.185` -> `3000` | 3 | 0.5% |
| 10 | `204.76.203.212` -> `85` | 3 | 0.5% |
| 11 | `200.114.86.153` -> `3306` | 2 | 0.3% |
| 12 | `180.93.75.229` -> `555` | 2 | 0.3% |
| 13 | `45.198.224.9` -> `12345` | 2 | 0.3% |
| 14 | `103.76.241.85` -> `22` | 2 | 0.3% |
| 15 | `35.195.247.231` -> `53` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-10 00:00:00:00 | 24 | 3.9% |
| 2026-05-10 01:00:00:00 | 181 | 29.7% |
| 2026-05-10 02:00:00:00 | 180 | 29.5% |
| 2026-05-10 03:00:00:00 | 180 | 29.5% |
| 2026-05-10 04:00:00:00 | 45 | 7.4% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Eygelshoven, The Netherlands | 32 | 43.8% |
| 2 | Ashburn, United States | 7 | 9.6% |
| 3 | Amsterdam, The Netherlands | 6 | 8.2% |
| 4 | Santa Clara, United States | 6 | 8.2% |
| 5 | New York, United States | 5 | 6.8% |
| 6 | Lewes, United States | 4 | 5.5% |
| 7 | United States / California / Cupertino / Apple Inc | 4 | 5.5% |
| 8 | La Plata, Argentina | 3 | 4.1% |
| 9 | Dublin, United States | 3 | 4.1% |
| 10 | North Bergen, United States | 3 | 4.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `204.76.203.212` | 28 | 38.4% | The Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 2 | `176.65.139.8` | 4 | 5.5% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 3 | `69.17.52.1` | 4 | 5.5% | United States / Delaware / Lewes / Spruce Creek Networks LLC | No apparent signal |
| 4 | `98.90.43.197` | 4 | 5.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 5 | `17.57.144.152` | 4 | 5.5% | United States / California / Cupertino / Apple Inc | No apparent signal |
| 6 | `200.114.86.153` | 3 | 4.1% | Argentina / Buenos Aires / La Plata / Citarella S.A. | No apparent signal |
| 7 | `124.198.131.185` | 3 | 4.1% | United States / New York / New York / 1337 Services GmbH | No apparent signal |
| 8 | `100.49.117.77` | 3 | 4.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 9 | `3.131.24.55` | 3 | 4.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `86.54.31.38` | 3 | 4.1% | The Netherlands / North Holland / Amsterdam / ADSL: Circle IT Solutions Limited | No apparent signal |
| 11 | `167.71.26.229` | 3 | 4.1% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 12 | `198.235.24.178` | 3 | 4.1% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |
| 13 | `147.185.133.142` | 3 | 4.1% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |
| 14 | `89.248.163.48` | 3 | 4.1% | The Netherlands / North Holland / Amsterdam / Quasi Networks LTD. | No apparent signal |
| 15 | `85.217.149.41` | 2 | 2.7% | United States / New York / New York / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `98.90.43.197` | 4 | 21.1% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 2 | `100.49.117.77` | 3 | 15.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 3 | `3.131.24.55` | 3 | 15.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `167.71.26.229` | 3 | 15.8% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 5 | `198.235.24.178` | 3 | 15.8% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |
| 6 | `147.185.133.142` | 3 | 15.8% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
