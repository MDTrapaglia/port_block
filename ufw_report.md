# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 635
- Unique source IPs: 522
- Unique countries/cities (24h): 109
- Unique destination ports: 482

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 28 | 4.4% |
| 2 | `22` | 27 | 4.3% |
| 3 | `3389` | 12 | 1.9% |
| 4 | `8080` | 10 | 1.6% |
| 5 | `53` | 10 | 1.6% |
| 6 | `5060` | 6 | 0.9% |
| 7 | `3128` | 6 | 0.9% |
| 8 | `27017` | 4 | 0.6% |
| 9 | `4444` | 4 | 0.6% |
| 10 | `2222` | 4 | 0.6% |
| 11 | `9999` | 4 | 0.6% |
| 12 | `3306` | 3 | 0.5% |
| 13 | `2095` | 3 | 0.5% |
| 14 | `8081` | 3 | 0.5% |
| 15 | `7443` | 3 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 562 | 88.5% |
| 2 | `UDP` | 71 | 11.2% |
| 3 | `41` | 1 | 0.2% |
| 4 | `4` | 1 | 0.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `164.92.129.109` | 9 | 1.4% |
| 2 | `141.98.83.48` | 5 | 0.8% |
| 3 | `45.198.224.15` | 5 | 0.8% |
| 4 | `77.239.124.252` | 5 | 0.8% |
| 5 | `185.73.23.133` | 5 | 0.8% |
| 6 | `190.104.248.106` | 4 | 0.6% |
| 7 | `91.230.168.252` | 3 | 0.5% |
| 8 | `91.196.152.246` | 3 | 0.5% |
| 9 | `193.163.125.171` | 3 | 0.5% |
| 10 | `195.184.76.62` | 3 | 0.5% |
| 11 | `80.94.92.130` | 3 | 0.5% |
| 12 | `18.217.208.51` | 3 | 0.5% |
| 13 | `34.228.104.231` | 3 | 0.5% |
| 14 | `100.28.153.226` | 3 | 0.5% |
| 15 | `195.184.76.220` | 3 | 0.5% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 558 | 99.3% |
| 2 | `ACK+PSH` | 2 | 0.4% |
| 3 | `SYN+ECE+CWR` | 2 | 0.4% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 635 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `77.239.124.252` -> `23` | 5 | 0.8% |
| 2 | `164.92.129.109` -> `3128` | 4 | 0.6% |
| 3 | `190.104.248.106` -> `22` | 4 | 0.6% |
| 4 | `164.92.129.109` -> `8080` | 3 | 0.5% |
| 5 | `194.165.16.163` -> `3389` | 3 | 0.5% |
| 6 | `66.132.195.109` -> `53` | 3 | 0.5% |
| 7 | `141.98.83.48` -> `11211` | 2 | 0.3% |
| 8 | `190.188.104.118` -> `23` | 2 | 0.3% |
| 9 | `212.70.110.247` -> `22` | 2 | 0.3% |
| 10 | `185.73.23.133` -> `5684` | 2 | 0.3% |
| 11 | `182.138.220.145` -> `22` | 2 | 0.3% |
| 12 | `160.119.76.173` -> `5060` | 2 | 0.3% |
| 13 | `197.2.148.223` -> `22` | 2 | 0.3% |
| 14 | `194.62.138.170` -> `23` | 2 | 0.3% |
| 15 | `62.210.114.99` -> `3389` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-15 00:00:00:00 | 48 | 7.6% |
| 2026-11-15 01:00:00:00 | 179 | 28.2% |
| 2026-11-15 02:00:00:00 | 181 | 28.5% |
| 2026-11-15 03:00:00:00 | 181 | 28.5% |
| 2026-11-15 04:00:00:00 | 46 | 7.2% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Frankfurt am Main, Germany | 14 | 23.3% |
| 2 | Amsterdam, The Netherlands | 8 | 13.3% |
| 3 | Warrenton, United States | 6 | 10.0% |
| 4 | Ashburn, United States | 6 | 10.0% |
| 5 | Panama City, Panama | 5 | 8.3% |
| 6 | Stockholm, Sweden | 5 | 8.3% |
| 7 | Olavarría, Argentina | 4 | 6.7% |
| 8 | Hillsboro, United States | 3 | 5.0% |
| 9 | Roubaix, France | 3 | 5.0% |
| 10 | Leeds, United Kingdom | 3 | 5.0% |
| 11 | Dublin, United States | 3 | 5.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `164.92.129.109` | 9 | 15.0% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `141.98.83.48` | 5 | 8.3% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 3 | `45.198.224.15` | 5 | 8.3% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 4 | `77.239.124.252` | 5 | 8.3% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |
| 5 | `185.73.23.133` | 5 | 8.3% | Germany / Hesse / Frankfurt am Main / RUB LIR Inet2 | No apparent signal |
| 6 | `190.104.248.106` | 4 | 6.7% | Argentina / Buenos Aires / Olavarría / Tecnica del Rio SRL | No apparent signal |
| 7 | `91.230.168.252` | 3 | 5.0% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 8 | `91.196.152.246` | 3 | 5.0% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 9 | `193.163.125.171` | 3 | 5.0% | United Kingdom / England / Leeds / Constantine Cybersecurity LTD | No apparent signal |
| 10 | `195.184.76.62` | 3 | 5.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 11 | `80.94.92.130` | 3 | 5.0% | The Netherlands / North Holland / Amsterdam / Techoff SRV Limited | No apparent signal |
| 12 | `18.217.208.51` | 3 | 5.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `34.228.104.231` | 3 | 5.0% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 14 | `100.28.153.226` | 3 | 5.0% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `195.184.76.220` | 3 | 5.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `164.92.129.109` | 9 | 39.1% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |
| 2 | `141.98.83.48` | 5 | 21.7% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 3 | `18.217.208.51` | 3 | 13.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `34.228.104.231` | 3 | 13.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `100.28.153.226` | 3 | 13.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
