# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 771
- Unique source IPs: 597
- Unique countries/cities (24h): 125
- Unique destination ports: 546

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 22 | 2.9% |
| 2 | `22` | 19 | 2.5% |
| 3 | `5060` | 11 | 1.4% |
| 4 | `8080` | 10 | 1.3% |
| 5 | `53` | 8 | 1.0% |
| 6 | `3389` | 8 | 1.0% |
| 7 | `1433` | 8 | 1.0% |
| 8 | `85` | 6 | 0.8% |
| 9 | `17000` | 5 | 0.6% |
| 10 | `81` | 5 | 0.6% |
| 11 | `8880` | 5 | 0.6% |
| 12 | `389` | 5 | 0.6% |
| 13 | `27017` | 5 | 0.6% |
| 14 | `8083` | 4 | 0.5% |
| 15 | `2087` | 4 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 695 | 90.1% |
| 2 | `UDP` | 75 | 9.7% |
| 3 | `47` | 1 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.121` | 33 | 4.3% |
| 2 | `64.89.160.221` | 10 | 1.3% |
| 3 | `2.22.149.139` | 8 | 1.0% |
| 4 | `167.99.207.12` | 6 | 0.8% |
| 5 | `185.73.23.133` | 5 | 0.6% |
| 6 | `3.131.24.55` | 4 | 0.5% |
| 7 | `138.226.239.22` | 4 | 0.5% |
| 8 | `35.210.72.197` | 4 | 0.5% |
| 9 | `141.98.83.48` | 4 | 0.5% |
| 10 | `138.226.239.21` | 4 | 0.5% |
| 11 | `45.198.224.125` | 3 | 0.4% |
| 12 | `34.197.70.90` | 3 | 0.4% |
| 13 | `35.169.206.177` | 3 | 0.4% |
| 14 | `71.6.155.70` | 3 | 0.4% |
| 15 | `195.184.76.198` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 684 | 98.4% |
| 2 | `ACK+FIN+PSH` | 7 | 1.0% |
| 3 | `ACK+PSH` | 2 | 0.3% |
| 4 | `ACK` | 2 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 771 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.121` -> `85` | 6 | 0.8% |
| 2 | `216.180.246.121` -> `22` | 5 | 0.6% |
| 3 | `216.180.246.121` -> `23` | 4 | 0.5% |
| 4 | `216.180.246.121` -> `81` | 4 | 0.5% |
| 5 | `216.180.246.121` -> `8880` | 4 | 0.5% |
| 6 | `216.180.246.121` -> `17000` | 4 | 0.5% |
| 7 | `2.22.149.139` -> `8131` | 4 | 0.5% |
| 8 | `2.22.149.139` -> `64022` | 4 | 0.5% |
| 9 | `216.180.246.121` -> `554` | 3 | 0.4% |
| 10 | `216.180.246.121` -> `25461` | 3 | 0.4% |
| 11 | `66.132.159.98` -> `1092` | 3 | 0.4% |
| 12 | `45.198.224.125` -> `8081` | 2 | 0.3% |
| 13 | `35.210.133.236` -> `53` | 2 | 0.3% |
| 14 | `185.73.23.133` -> `5683` | 2 | 0.3% |
| 15 | `93.123.109.6` -> `1723` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-01 00:00:00:00 | 178 | 23.1% |
| 2026-11-01 01:00:00:00 | 187 | 24.3% |
| 2026-11-01 02:00:00:00 | 179 | 23.2% |
| 2026-11-01 03:00:00:00 | 180 | 23.3% |
| 2026-11-01 04:00:00:00 | 47 | 6.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 33 | 34.0% |
| 2 | Schieren, Luxembourg | 10 | 10.3% |
| 3 | Buenos Aires, Argentina | 8 | 8.2% |
| 4 | Port Vila, Vanuatu | 8 | 8.2% |
| 5 | Slough, United Kingdom | 6 | 6.2% |
| 6 | Ashburn, United States | 6 | 6.2% |
| 7 | Frankfurt am Main, Germany | 5 | 5.2% |
| 8 | Dublin, United States | 4 | 4.1% |
| 9 | Brussels, Belgium | 4 | 4.1% |
| 10 | Panama City, Panama | 4 | 4.1% |
| 11 | Stockholm, Sweden | 3 | 3.1% |
| 12 | San Diego, United States | 3 | 3.1% |
| 13 | Warrenton, United States | 3 | 3.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.121` | 33 | 34.0% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `64.89.160.221` | 10 | 10.3% | Luxembourg / Diekirch / Schieren / Netiface LLC | No apparent signal |
| 3 | `2.22.149.139` | 8 | 8.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 4 | `167.99.207.12` | 6 | 6.2% | United Kingdom / England / Slough / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `185.73.23.133` | 5 | 5.2% | Germany / Hesse / Frankfurt am Main / RUB LIR Inet2 | No apparent signal |
| 6 | `3.131.24.55` | 4 | 4.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `138.226.239.22` | 4 | 4.1% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 8 | `35.210.72.197` | 4 | 4.1% | Belgium / Brussels Capital / Brussels / Google Cloud (europe-west1) | Hosting/Cloud (google cloud) |
| 9 | `141.98.83.48` | 4 | 4.1% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 10 | `138.226.239.21` | 4 | 4.1% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 11 | `45.198.224.125` | 3 | 3.1% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 12 | `34.197.70.90` | 3 | 3.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `35.169.206.177` | 3 | 3.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 14 | `71.6.155.70` | 3 | 3.1% | United States / California / San Diego / CariNet, Inc. | No apparent signal |
| 15 | `195.184.76.198` | 3 | 3.1% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.121` | 33 | 50.8% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `2.22.149.139` | 8 | 12.3% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `167.99.207.12` | 6 | 9.2% | Hosting/Cloud (digitalocean) | United Kingdom / England / Slough / DigitalOcean, LLC |
| 4 | `3.131.24.55` | 4 | 6.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `35.210.72.197` | 4 | 6.2% | Hosting/Cloud (google cloud) | Belgium / Brussels Capital / Brussels / Google Cloud (europe-west1) |
| 6 | `141.98.83.48` | 4 | 6.2% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 7 | `34.197.70.90` | 3 | 4.6% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 8 | `35.169.206.177` | 3 | 4.6% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
