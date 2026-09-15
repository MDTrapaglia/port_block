# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4429
- Unique source IPs: 2468
- Unique countries/cities (24h): 380
- Unique destination ports: 2513

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 312 | 7.0% |
| 2 | `22` | 95 | 2.1% |
| 3 | `1433` | 30 | 0.7% |
| 4 | `53` | 30 | 0.7% |
| 5 | `5060` | 29 | 0.7% |
| 6 | `3306` | 25 | 0.6% |
| 7 | `3389` | 22 | 0.5% |
| 8 | `8443` | 21 | 0.5% |
| 9 | `8080` | 20 | 0.5% |
| 10 | `161` | 20 | 0.5% |
| 11 | `3000` | 20 | 0.5% |
| 12 | `21` | 17 | 0.4% |
| 13 | `8081` | 17 | 0.4% |
| 14 | `9200` | 16 | 0.4% |
| 15 | `27017` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4003 | 90.4% |
| 2 | `UDP` | 421 | 9.5% |
| 3 | `47` | 5 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `165.22.57.101` | 144 | 3.3% |
| 2 | `216.180.246.82` | 110 | 2.5% |
| 3 | `80.249.99.148` | 68 | 1.5% |
| 4 | `151.101.218.13` | 24 | 0.5% |
| 5 | `151.101.218.73` | 17 | 0.4% |
| 6 | `85.217.140.6` | 15 | 0.3% |
| 7 | `85.217.140.23` | 14 | 0.3% |
| 8 | `85.217.140.28` | 14 | 0.3% |
| 9 | `85.217.140.19` | 14 | 0.3% |
| 10 | `18.217.208.51` | 14 | 0.3% |
| 11 | `85.217.140.18` | 14 | 0.3% |
| 12 | `147.182.178.48` | 13 | 0.3% |
| 13 | `151.101.219.52` | 13 | 0.3% |
| 14 | `2.22.149.176` | 13 | 0.3% |
| 15 | `85.217.140.3` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3778 | 94.4% |
| 2 | `ACK+FIN+PSH` | 97 | 2.4% |
| 3 | `ACK` | 70 | 1.7% |
| 4 | `ACK+PSH` | 38 | 0.9% |
| 5 | `ACK+FIN` | 11 | 0.3% |
| 6 | `SYN+ECE+CWR` | 9 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4429 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `165.22.57.101` -> `23` | 144 | 3.3% |
| 2 | `216.180.246.82` -> `3081` | 9 | 0.2% |
| 3 | `216.180.246.82` -> `2811` | 8 | 0.2% |
| 4 | `2.22.149.176` -> `62146` | 8 | 0.2% |
| 5 | `151.101.219.52` -> `46136` | 7 | 0.2% |
| 6 | `151.101.218.73` -> `47373` | 7 | 0.2% |
| 7 | `151.101.218.73` -> `61622` | 7 | 0.2% |
| 8 | `216.180.246.82` -> `3000` | 7 | 0.2% |
| 9 | `216.180.246.82` -> `2601` | 6 | 0.1% |
| 10 | `216.180.246.82` -> `3005` | 6 | 0.1% |
| 11 | `216.180.246.82` -> `3041` | 6 | 0.1% |
| 12 | `189.159.211.204` -> `22` | 6 | 0.1% |
| 13 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 14 | `141.98.83.48` -> `161` | 5 | 0.1% |
| 15 | `223.96.92.77` -> `1433` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-14 04:00:00:00 | 135 | 3.0% |
| 2026-09-14 05:00:00:00 | 179 | 4.0% |
| 2026-09-14 06:00:00:00 | 182 | 4.1% |
| 2026-09-14 07:00:00:00 | 190 | 4.3% |
| 2026-09-14 08:00:00:00 | 218 | 4.9% |
| 2026-09-14 09:00:00:00 | 175 | 4.0% |
| 2026-09-14 10:00:00:00 | 184 | 4.2% |
| 2026-09-14 11:00:00:00 | 181 | 4.1% |
| 2026-09-14 12:00:00:00 | 181 | 4.1% |
| 2026-09-14 13:00:00:00 | 180 | 4.1% |
| 2026-09-14 14:00:00:00 | 179 | 4.0% |
| 2026-09-14 15:00:00:00 | 193 | 4.4% |
| 2026-09-14 16:00:00:00 | 178 | 4.0% |
| 2026-09-14 17:00:00:00 | 183 | 4.1% |
| 2026-09-14 18:00:00:00 | 179 | 4.0% |
| 2026-09-14 19:00:00:00 | 180 | 4.1% |
| 2026-09-14 20:00:00:00 | 181 | 4.1% |
| 2026-09-14 21:00:00:00 | 202 | 4.6% |
| 2026-09-14 22:00:00:00 | 180 | 4.1% |
| 2026-09-14 23:00:00:00 | 181 | 4.1% |
| 2026-09-15 00:00:00:00 | 185 | 4.2% |
| 2026-09-15 01:00:00:00 | 197 | 4.4% |
| 2026-09-15 02:00:00:00 | 181 | 4.1% |
| 2026-09-15 03:00:00:00 | 180 | 4.1% |
| 2026-09-15 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Singapore, Singapore | 144 | 28.9% |
| 2 | Massy, France | 110 | 22.0% |
| 3 | Gravelines, France | 83 | 16.6% |
| 4 | City of London, United Kingdom | 68 | 13.6% |
| 5 | Buenos Aires, Argentina | 50 | 10.0% |
| 6 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 17 | 3.4% |
| 7 | Dublin, United States | 14 | 2.8% |
| 8 | North Bergen, United States | 13 | 2.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `165.22.57.101` | 144 | 28.9% | Singapore / South West / Singapore / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `216.180.246.82` | 110 | 22.0% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 3 | `80.249.99.148` | 68 | 13.6% | United Kingdom / England / City of London / NetConnex Ltd. | No apparent signal |
| 4 | `151.101.218.13` | 24 | 4.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `151.101.218.73` | 17 | 3.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `85.217.140.6` | 15 | 3.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 7 | `85.217.140.23` | 14 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.28` | 14 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.19` | 14 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `18.217.208.51` | 14 | 2.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `85.217.140.18` | 14 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `147.182.178.48` | 13 | 2.6% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `151.101.219.52` | 13 | 2.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 14 | `2.22.149.176` | 13 | 2.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 15 | `85.217.140.3` | 12 | 2.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `165.22.57.101` | 144 | 41.4% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / DigitalOcean, LLC |
| 2 | `216.180.246.82` | 110 | 31.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 3 | `151.101.218.13` | 24 | 6.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `151.101.218.73` | 17 | 4.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `18.217.208.51` | 14 | 4.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `147.182.178.48` | 13 | 3.7% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 7 | `151.101.219.52` | 13 | 3.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 8 | `2.22.149.176` | 13 | 3.7% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
