# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4375
- Unique source IPs: 2728
- Unique countries/cities (24h): 479
- Unique destination ports: 1821

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1063 | 24.3% |
| 2 | `22` | 55 | 1.3% |
| 3 | `53` | 34 | 0.8% |
| 4 | `5060` | 32 | 0.7% |
| 5 | `3389` | 29 | 0.7% |
| 6 | `8080` | 28 | 0.6% |
| 7 | `3306` | 26 | 0.6% |
| 8 | `8888` | 18 | 0.4% |
| 9 | `5555` | 18 | 0.4% |
| 10 | `1433` | 17 | 0.4% |
| 11 | `8443` | 17 | 0.4% |
| 12 | `5985` | 17 | 0.4% |
| 13 | `8081` | 17 | 0.4% |
| 14 | `8000` | 15 | 0.3% |
| 15 | `161` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4012 | 91.7% |
| 2 | `UDP` | 354 | 8.1% |
| 3 | `132` | 4 | 0.1% |
| 4 | `47` | 4 | 0.1% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.230` | 161 | 3.7% |
| 2 | `144.31.239.205` | 53 | 1.2% |
| 3 | `92.118.39.76` | 18 | 0.4% |
| 4 | `92.118.39.246` | 14 | 0.3% |
| 5 | `79.124.40.186` | 13 | 0.3% |
| 6 | `18.221.179.104` | 13 | 0.3% |
| 7 | `192.207.105.196` | 13 | 0.3% |
| 8 | `77.239.124.188` | 13 | 0.3% |
| 9 | `79.124.59.82` | 11 | 0.3% |
| 10 | `91.231.89.10` | 11 | 0.3% |
| 11 | `176.65.148.207` | 11 | 0.3% |
| 12 | `18.119.209.50` | 11 | 0.3% |
| 13 | `195.184.76.71` | 10 | 0.2% |
| 14 | `91.230.168.233` | 10 | 0.2% |
| 15 | `2.22.149.169` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3945 | 98.3% |
| 2 | `ACK+FIN+PSH` | 42 | 1.0% |
| 3 | `ACK+FIN` | 13 | 0.3% |
| 4 | `ACK+PSH` | 9 | 0.2% |
| 5 | `SYN+ECE+CWR` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4375 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `181.224.223.146` -> `23` | 9 | 0.2% |
| 2 | `216.180.246.230` -> `5985` | 9 | 0.2% |
| 3 | `216.180.246.230` -> `6023` | 9 | 0.2% |
| 4 | `216.180.246.230` -> `6035` | 8 | 0.2% |
| 5 | `216.180.246.230` -> `5555` | 7 | 0.2% |
| 6 | `216.180.246.230` -> `5678` | 7 | 0.2% |
| 7 | `216.180.246.230` -> `5989` | 7 | 0.2% |
| 8 | `103.30.11.172` -> `22` | 6 | 0.1% |
| 9 | `216.180.246.230` -> `5432` | 6 | 0.1% |
| 10 | `216.180.246.230` -> `5443` | 6 | 0.1% |
| 11 | `216.180.246.230` -> `5901` | 6 | 0.1% |
| 12 | `216.180.246.230` -> `5984` | 6 | 0.1% |
| 13 | `216.180.246.230` -> `6037` | 6 | 0.1% |
| 14 | `216.180.246.230` -> `5544` | 5 | 0.1% |
| 15 | `216.180.246.230` -> `5900` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-25 04:00:00:00 | 135 | 3.1% |
| 2026-11-25 05:00:00:00 | 179 | 4.1% |
| 2026-11-25 06:00:00:00 | 182 | 4.2% |
| 2026-11-25 07:00:00:00 | 181 | 4.1% |
| 2026-11-25 08:00:00:00 | 189 | 4.3% |
| 2026-11-25 09:00:00:00 | 180 | 4.1% |
| 2026-11-25 10:00:00:00 | 180 | 4.1% |
| 2026-11-25 11:00:00:00 | 180 | 4.1% |
| 2026-11-25 12:00:00:00 | 181 | 4.1% |
| 2026-11-25 13:00:00:00 | 179 | 4.1% |
| 2026-11-25 14:00:00:00 | 180 | 4.1% |
| 2026-11-25 15:00:00:00 | 180 | 4.1% |
| 2026-11-25 16:00:00:00 | 186 | 4.3% |
| 2026-11-25 17:00:00:00 | 181 | 4.1% |
| 2026-11-25 18:00:00:00 | 190 | 4.3% |
| 2026-11-25 19:00:00:00 | 193 | 4.4% |
| 2026-11-25 20:00:00:00 | 180 | 4.1% |
| 2026-11-25 21:00:00:00 | 181 | 4.1% |
| 2026-11-25 22:00:00:00 | 181 | 4.1% |
| 2026-11-25 23:00:00:00 | 191 | 4.4% |
| 2026-11-26 00:00:00:00 | 181 | 4.1% |
| 2026-11-26 01:00:00:00 | 179 | 4.1% |
| 2026-11-26 02:00:00:00 | 181 | 4.1% |
| 2026-11-26 03:00:00:00 | 180 | 4.1% |
| 2026-11-26 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 161 | 43.3% |
| 2 | Helsinki, Finland | 53 | 14.2% |
| 3 | Sopot, Bulgaria | 24 | 6.5% |
| 4 | Dublin, United States | 24 | 6.5% |
| 5 | Dallas, United States | 18 | 4.8% |
| 6 | Amsterdam, The Netherlands | 14 | 3.8% |
| 7 | Newburyport, United States | 13 | 3.5% |
| 8 | Paris, France | 13 | 3.5% |
| 9 | Gravelines, France | 11 | 3.0% |
| 10 | Eygelshoven, The Netherlands | 11 | 3.0% |
| 11 | Warrenton, United States | 10 | 2.7% |
| 12 | Hillsboro, United States | 10 | 2.7% |
| 13 | Buenos Aires, Argentina | 10 | 2.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.230` | 161 | 43.3% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `144.31.239.205` | 53 | 14.2% | Finland / Uusimaa / Helsinki / SERV.HOST GROUP LTD | No apparent signal |
| 3 | `92.118.39.76` | 18 | 4.8% | United States / Texas / Dallas / Pptechnology Limited | No apparent signal |
| 4 | `92.118.39.246` | 14 | 3.8% | The Netherlands / North Holland / Amsterdam / Pptechnology Limited | No apparent signal |
| 5 | `79.124.40.186` | 13 | 3.5% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 6 | `18.221.179.104` | 13 | 3.5% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `192.207.105.196` | 13 | 3.5% | United States / Massachusetts / Newburyport / Searchlight Cyber LLC | Hosting/Cloud (ovh) |
| 8 | `77.239.124.188` | 13 | 3.5% | France / Île-de-France / Paris / RocketCloud | No apparent signal |
| 9 | `79.124.59.82` | 11 | 3.0% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 10 | `91.231.89.10` | 11 | 3.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 11 | `176.65.148.207` | 11 | 3.0% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 12 | `18.119.209.50` | 11 | 3.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `195.184.76.71` | 10 | 2.7% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `91.230.168.233` | 10 | 2.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 15 | `2.22.149.169` | 10 | 2.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.230` | 161 | 77.4% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `18.221.179.104` | 13 | 6.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `192.207.105.196` | 13 | 6.2% | Hosting/Cloud (ovh) | United States / Massachusetts / Newburyport / Searchlight Cyber LLC |
| 4 | `18.119.209.50` | 11 | 5.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `2.22.149.169` | 10 | 4.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
