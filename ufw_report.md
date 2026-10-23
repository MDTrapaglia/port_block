# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4458
- Unique source IPs: 2363
- Unique countries/cities (24h): 284
- Unique destination ports: 2604

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 139 | 3.1% |
| 2 | `22` | 85 | 1.9% |
| 3 | `3389` | 37 | 0.8% |
| 4 | `8443` | 35 | 0.8% |
| 5 | `5060` | 35 | 0.8% |
| 6 | `8080` | 33 | 0.7% |
| 7 | `53` | 25 | 0.6% |
| 8 | `1900` | 21 | 0.5% |
| 9 | `8081` | 20 | 0.4% |
| 10 | `1433` | 19 | 0.4% |
| 11 | `81` | 18 | 0.4% |
| 12 | `8291` | 17 | 0.4% |
| 13 | `25` | 15 | 0.3% |
| 14 | `3306` | 14 | 0.3% |
| 15 | `8181` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4101 | 92.0% |
| 2 | `UDP` | 353 | 7.9% |
| 3 | `47` | 4 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.130` | 192 | 4.3% |
| 2 | `77.239.124.251` | 73 | 1.6% |
| 3 | `216.180.246.219` | 59 | 1.3% |
| 4 | `151.101.218.13` | 48 | 1.1% |
| 5 | `216.180.246.186` | 39 | 0.9% |
| 6 | `94.183.174.95` | 28 | 0.6% |
| 7 | `3.147.122.184` | 15 | 0.3% |
| 8 | `91.231.89.117` | 15 | 0.3% |
| 9 | `91.230.168.129` | 14 | 0.3% |
| 10 | `45.198.224.125` | 14 | 0.3% |
| 11 | `91.230.168.233` | 14 | 0.3% |
| 12 | `91.231.89.224` | 13 | 0.3% |
| 13 | `91.231.89.87` | 13 | 0.3% |
| 14 | `195.184.76.71` | 13 | 0.3% |
| 15 | `18.190.15.50` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3908 | 95.3% |
| 2 | `ACK+FIN+PSH` | 125 | 3.0% |
| 3 | `ACK+PSH` | 46 | 1.1% |
| 4 | `ACK+FIN` | 16 | 0.4% |
| 5 | `SYN+ECE+CWR` | 6 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4458 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `193.47.62.187` -> `1900` | 11 | 0.2% |
| 2 | `62.210.114.99` -> `3389` | 10 | 0.2% |
| 3 | `216.180.246.130` -> `8291` | 10 | 0.2% |
| 4 | `216.180.246.219` -> `8789` | 10 | 0.2% |
| 5 | `216.180.246.130` -> `8181` | 9 | 0.2% |
| 6 | `216.180.246.130` -> `8245` | 9 | 0.2% |
| 7 | `216.180.246.130` -> `8400` | 9 | 0.2% |
| 8 | `216.180.246.186` -> `23` | 9 | 0.2% |
| 9 | `216.180.246.130` -> `8140` | 8 | 0.2% |
| 10 | `216.180.246.130` -> `8153` | 8 | 0.2% |
| 11 | `165.22.41.116` -> `23` | 8 | 0.2% |
| 12 | `216.180.246.130` -> `8300` | 8 | 0.2% |
| 13 | `216.180.246.130` -> `8501` | 8 | 0.2% |
| 14 | `216.180.246.130` -> `8545` | 8 | 0.2% |
| 15 | `151.101.218.13` -> `62532` | 8 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-22 04:00:00:00 | 135 | 3.0% |
| 2026-10-22 05:00:00:00 | 179 | 4.0% |
| 2026-10-22 06:00:00:00 | 180 | 4.0% |
| 2026-10-22 07:00:00:00 | 180 | 4.0% |
| 2026-10-22 08:00:00:00 | 180 | 4.0% |
| 2026-10-22 09:00:00:00 | 180 | 4.0% |
| 2026-10-22 10:00:00:00 | 181 | 4.1% |
| 2026-10-22 11:00:00:00 | 182 | 4.1% |
| 2026-10-22 12:00:00:00 | 204 | 4.6% |
| 2026-10-22 13:00:00:00 | 180 | 4.0% |
| 2026-10-22 14:00:00:00 | 200 | 4.5% |
| 2026-10-22 15:00:00:00 | 204 | 4.6% |
| 2026-10-22 16:00:00:00 | 207 | 4.6% |
| 2026-10-22 17:00:00:00 | 179 | 4.0% |
| 2026-10-22 18:00:00:00 | 178 | 4.0% |
| 2026-10-22 19:00:00:00 | 192 | 4.3% |
| 2026-10-22 20:00:00:00 | 179 | 4.0% |
| 2026-10-22 21:00:00:00 | 180 | 4.0% |
| 2026-10-22 22:00:00:00 | 181 | 4.1% |
| 2026-10-22 23:00:00:00 | 184 | 4.1% |
| 2026-10-23 00:00:00:00 | 181 | 4.1% |
| 2026-10-23 01:00:00:00 | 207 | 4.6% |
| 2026-10-23 02:00:00:00 | 178 | 4.0% |
| 2026-10-23 03:00:00:00 | 182 | 4.1% |
| 2026-10-23 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 290 | 51.5% |
| 2 | Paris, France | 73 | 13.0% |
| 3 | Buenos Aires, Argentina | 48 | 8.5% |
| 4 | Gravelines, France | 41 | 7.3% |
| 5 | Hauzenberg, Germany | 28 | 5.0% |
| 6 | Dublin, United States | 28 | 5.0% |
| 7 | Hillsboro, United States | 28 | 5.0% |
| 8 | Stockholm, Sweden | 14 | 2.5% |
| 9 | Warrenton, United States | 13 | 2.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.130` | 192 | 34.1% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `77.239.124.251` | 73 | 13.0% | France / Île-de-France / Paris / RocketCloud | No apparent signal |
| 3 | `216.180.246.219` | 59 | 10.5% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 4 | `151.101.218.13` | 48 | 8.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `216.180.246.186` | 39 | 6.9% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 6 | `94.183.174.95` | 28 | 5.0% | Germany / Bavaria / Hauzenberg / Pfcloud UG | No apparent signal |
| 7 | `3.147.122.184` | 15 | 2.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `91.231.89.117` | 15 | 2.7% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `91.230.168.129` | 14 | 2.5% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 10 | `45.198.224.125` | 14 | 2.5% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 11 | `91.230.168.233` | 14 | 2.5% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 12 | `91.231.89.224` | 13 | 2.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 13 | `91.231.89.87` | 13 | 2.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `195.184.76.71` | 13 | 2.3% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 15 | `18.190.15.50` | 13 | 2.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.130` | 192 | 52.5% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `216.180.246.219` | 59 | 16.1% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 3 | `151.101.218.13` | 48 | 13.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `216.180.246.186` | 39 | 10.7% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 5 | `3.147.122.184` | 15 | 4.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `18.190.15.50` | 13 | 3.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
