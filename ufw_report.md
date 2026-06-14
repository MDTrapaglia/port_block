# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 630
- Unique source IPs: 568
- Unique countries/cities (24h): 140
- Unique destination ports: 480

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `unknown` | 27 | 4.3% |
| 2 | `23` | 18 | 2.9% |
| 3 | `8080` | 7 | 1.1% |
| 4 | `22` | 6 | 1.0% |
| 5 | `53` | 6 | 1.0% |
| 6 | `8000` | 5 | 0.8% |
| 7 | `1433` | 5 | 0.8% |
| 8 | `5060` | 5 | 0.8% |
| 9 | `264` | 4 | 0.6% |
| 10 | `11211` | 4 | 0.6% |
| 11 | `427` | 4 | 0.6% |
| 12 | `27015` | 4 | 0.6% |
| 13 | `990` | 4 | 0.6% |
| 14 | `2222` | 4 | 0.6% |
| 15 | `9200` | 4 | 0.6% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 538 | 85.4% |
| 2 | `UDP` | 65 | 10.3% |
| 3 | `47` | 27 | 4.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `141.98.83.48` | 5 | 0.8% |
| 2 | `45.148.10.121` | 4 | 0.6% |
| 3 | `13.219.1.233` | 3 | 0.5% |
| 4 | `94.156.152.50` | 3 | 0.5% |
| 5 | `18.189.74.1` | 3 | 0.5% |
| 6 | `18.190.15.50` | 3 | 0.5% |
| 7 | `134.122.113.215` | 3 | 0.5% |
| 8 | `34.77.202.190` | 3 | 0.5% |
| 9 | `204.76.203.15` | 3 | 0.5% |
| 10 | `45.205.1.76` | 2 | 0.3% |
| 11 | `69.5.169.87` | 2 | 0.3% |
| 12 | `167.94.145.18` | 2 | 0.3% |
| 13 | `100.49.117.77` | 2 | 0.3% |
| 14 | `34.228.104.231` | 2 | 0.3% |
| 15 | `45.205.1.242` | 2 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 536 | 99.6% |
| 2 | `SYN+ECE+CWR` | 1 | 0.2% |
| 3 | `ACK+PSH` | 1 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 630 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `94.156.152.50` -> `23` | 3 | 0.5% |
| 2 | `34.77.202.190` -> `990` | 3 | 0.5% |
| 3 | `34.52.158.58` -> `23` | 2 | 0.3% |
| 4 | `110.10.176.24` -> `5038` | 2 | 0.3% |
| 5 | `141.98.83.48` -> `427` | 2 | 0.3% |
| 6 | `5.61.209.43` -> `8080` | 2 | 0.3% |
| 7 | `118.139.165.2` -> `23` | 2 | 0.3% |
| 8 | `34.62.50.145` -> `53` | 2 | 0.3% |
| 9 | `35.203.210.204` -> `46894` | 1 | 0.2% |
| 10 | `147.185.132.84` -> `995` | 1 | 0.2% |
| 11 | `205.210.31.98` -> `20256` | 1 | 0.2% |
| 12 | `58.51.252.236` -> `unknown` | 1 | 0.2% |
| 13 | `50.116.26.161` -> `54898` | 1 | 0.2% |
| 14 | `47.183.201.51` -> `unknown` | 1 | 0.2% |
| 15 | `45.205.1.76` -> `8181` | 1 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-14 00:00:00:00 | 44 | 7.0% |
| 2026-06-14 01:00:00:00 | 180 | 28.6% |
| 2026-06-14 02:00:00:00 | 180 | 28.6% |
| 2026-06-14 03:00:00:00 | 179 | 28.4% |
| 2026-06-14 04:00:00:00 | 47 | 7.5% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Ashburn, United States | 7 | 16.7% |
| 2 | Dublin, United States | 6 | 14.3% |
| 3 | Panama City, Panama | 5 | 11.9% |
| 4 | Amsterdam, The Netherlands | 4 | 9.5% |
| 5 | São Paulo, Brazil | 4 | 9.5% |
| 6 | Centurion, South Africa | 3 | 7.1% |
| 7 | North Bergen, United States | 3 | 7.1% |
| 8 | Brussels, Belgium | 3 | 7.1% |
| 9 | Eygelshoven, Netherlands | 3 | 7.1% |
| 10 | City of London, United Kingdom | 2 | 4.8% |
| 11 | Ann Arbor, United States | 2 | 4.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `141.98.83.48` | 5 | 11.9% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 2 | `45.148.10.121` | 4 | 9.5% | The Netherlands / North Holland / Amsterdam / Techoff SRV Limited | No apparent signal |
| 3 | `13.219.1.233` | 3 | 7.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 4 | `94.156.152.50` | 3 | 7.1% | South Africa / Gauteng / Centurion / Internet Magnate (Pty) Ltd | No apparent signal |
| 5 | `18.189.74.1` | 3 | 7.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 6 | `18.190.15.50` | 3 | 7.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `134.122.113.215` | 3 | 7.1% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 8 | `34.77.202.190` | 3 | 7.1% | Belgium / Brussels Capital / Brussels / Google Cloud (europe-west1) | Hosting/Cloud (google cloud) |
| 9 | `204.76.203.15` | 3 | 7.1% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 10 | `45.205.1.76` | 2 | 4.8% | Brazil / São Paulo / São Paulo / Vpsvault.host LTD | No apparent signal |
| 11 | `69.5.169.87` | 2 | 4.8% | United Kingdom / England / City of London / Hydra Communications Ltd | No apparent signal |
| 12 | `167.94.145.18` | 2 | 4.8% | United States / Michigan / Ann Arbor / Censys, Inc. | No apparent signal |
| 13 | `100.49.117.77` | 2 | 4.8% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 14 | `34.228.104.231` | 2 | 4.8% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `45.205.1.242` | 2 | 4.8% | Brazil / São Paulo / São Paulo / Vpsvault.host LTD | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `141.98.83.48` | 5 | 20.8% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 2 | `13.219.1.233` | 3 | 12.5% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 3 | `18.189.74.1` | 3 | 12.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `18.190.15.50` | 3 | 12.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `134.122.113.215` | 3 | 12.5% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 6 | `34.77.202.190` | 3 | 12.5% | Hosting/Cloud (google cloud) | Belgium / Brussels Capital / Brussels / Google Cloud (europe-west1) |
| 7 | `100.49.117.77` | 2 | 8.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 8 | `34.228.104.231` | 2 | 8.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
