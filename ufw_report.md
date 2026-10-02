# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4341
- Unique source IPs: 2250
- Unique countries/cities (24h): 284
- Unique destination ports: 2526

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 349 | 8.0% |
| 2 | `22` | 77 | 1.8% |
| 3 | `8080` | 37 | 0.9% |
| 4 | `5060` | 31 | 0.7% |
| 5 | `3389` | 29 | 0.7% |
| 6 | `53` | 27 | 0.6% |
| 7 | `17000` | 24 | 0.6% |
| 8 | `1433` | 24 | 0.6% |
| 9 | `8443` | 24 | 0.6% |
| 10 | `161` | 22 | 0.5% |
| 11 | `8081` | 22 | 0.5% |
| 12 | `123` | 21 | 0.5% |
| 13 | `6036` | 19 | 0.4% |
| 14 | `3000` | 16 | 0.4% |
| 15 | `2222` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3958 | 91.2% |
| 2 | `UDP` | 370 | 8.5% |
| 3 | `47` | 10 | 0.2% |
| 4 | `41` | 2 | 0.0% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `185.28.119.70` | 185 | 4.3% |
| 2 | `134.209.229.23` | 160 | 3.7% |
| 3 | `160.191.244.5` | 68 | 1.6% |
| 4 | `176.65.149.45` | 47 | 1.1% |
| 5 | `216.180.246.214` | 47 | 1.1% |
| 6 | `177.65.188.143` | 30 | 0.7% |
| 7 | `216.180.246.31` | 27 | 0.6% |
| 8 | `45.198.224.125` | 19 | 0.4% |
| 9 | `5.61.209.106` | 19 | 0.4% |
| 10 | `171.224.105.74` | 18 | 0.4% |
| 11 | `195.178.110.204` | 15 | 0.3% |
| 12 | `91.230.168.142` | 14 | 0.3% |
| 13 | `195.184.76.116` | 14 | 0.3% |
| 14 | `91.230.168.190` | 13 | 0.3% |
| 15 | `91.230.168.233` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3895 | 98.4% |
| 2 | `ACK+PSH` | 19 | 0.5% |
| 3 | `ACK+FIN+PSH` | 17 | 0.4% |
| 4 | `ACK` | 14 | 0.4% |
| 5 | `SYN+ECE+CWR` | 11 | 0.3% |
| 6 | `ACK+FIN` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4341 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `134.209.229.23` -> `23` | 160 | 3.7% |
| 2 | `176.65.149.45` -> `23` | 47 | 1.1% |
| 3 | `177.65.188.143` -> `23` | 30 | 0.7% |
| 4 | `91.224.92.28` -> `34567` | 11 | 0.3% |
| 5 | `41.230.76.14` -> `23` | 10 | 0.2% |
| 6 | `45.198.224.125` -> `8081` | 8 | 0.2% |
| 7 | `45.198.224.125` -> `8080` | 8 | 0.2% |
| 8 | `186.123.1.125` -> `1433` | 7 | 0.2% |
| 9 | `216.180.246.214` -> `2856` | 7 | 0.2% |
| 10 | `178.20.210.152` -> `1723` | 6 | 0.1% |
| 11 | `5.61.209.106` -> `17000` | 6 | 0.1% |
| 12 | `216.180.246.214` -> `2869` | 6 | 0.1% |
| 13 | `2.23.164.183` -> `61363` | 6 | 0.1% |
| 14 | `216.180.246.214` -> `3007` | 6 | 0.1% |
| 15 | `201.20.85.122` -> `6379` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-01 04:00:00:00 | 136 | 3.1% |
| 2026-10-01 05:00:00:00 | 180 | 4.1% |
| 2026-10-01 06:00:00:00 | 179 | 4.1% |
| 2026-10-01 07:00:00:00 | 180 | 4.1% |
| 2026-10-01 08:00:00:00 | 182 | 4.2% |
| 2026-10-01 09:00:00:00 | 180 | 4.1% |
| 2026-10-01 10:00:00:00 | 180 | 4.1% |
| 2026-10-01 11:00:00:00 | 179 | 4.1% |
| 2026-10-01 12:00:00:00 | 180 | 4.1% |
| 2026-10-01 13:00:00:00 | 180 | 4.1% |
| 2026-10-01 14:00:00:00 | 181 | 4.2% |
| 2026-10-01 15:00:00:00 | 179 | 4.1% |
| 2026-10-01 16:00:00:00 | 179 | 4.1% |
| 2026-10-01 17:00:00:00 | 178 | 4.1% |
| 2026-10-01 18:00:00:00 | 183 | 4.2% |
| 2026-10-01 19:00:00:00 | 178 | 4.1% |
| 2026-10-01 20:00:00:00 | 184 | 4.2% |
| 2026-10-01 21:00:00:00 | 181 | 4.2% |
| 2026-10-01 22:00:00:00 | 181 | 4.2% |
| 2026-10-01 23:00:00:00 | 180 | 4.1% |
| 2026-10-02 00:00:00:00 | 185 | 4.3% |
| 2026-10-02 01:00:00:00 | 180 | 4.1% |
| 2026-10-02 02:00:00:00 | 190 | 4.4% |
| 2026-10-02 03:00:00:00 | 180 | 4.1% |
| 2026-10-02 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Los Angeles, United States | 185 | 26.9% |
| 2 | Frankfurt am Main, Germany | 160 | 23.2% |
| 3 | Massy, France | 74 | 10.7% |
| 4 | Đố Sơn, Vietnam | 68 | 9.9% |
| 5 | Eygelshoven, The Netherlands | 47 | 6.8% |
| 6 | Hillsboro, United States | 40 | 5.8% |
| 7 | Belém, Brazil | 30 | 4.4% |
| 8 | Stockholm, Sweden | 19 | 2.8% |
| 9 | Amsterdam, The Netherlands | 19 | 2.8% |
| 10 | Hanoi, Vietnam | 18 | 2.6% |
| 11 | Andorra la Vella, Andorra | 15 | 2.2% |
| 12 | Warrenton, United States | 14 | 2.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `185.28.119.70` | 185 | 26.9% | United States / California / Los Angeles / BlueVPS OU | No apparent signal |
| 2 | `134.209.229.23` | 160 | 23.2% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 3 | `160.191.244.5` | 68 | 9.9% | Vietnam / Hai Phong / Đố Sơn / DTDMVNCLOUD | No apparent signal |
| 4 | `176.65.149.45` | 47 | 6.8% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 5 | `216.180.246.214` | 47 | 6.8% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 6 | `177.65.188.143` | 30 | 4.4% | Brazil / Pará / Belém / Claro NXT Telecomunicacoes Ltda | Mobile/CGNAT (claro) |
| 7 | `216.180.246.31` | 27 | 3.9% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 8 | `45.198.224.125` | 19 | 2.8% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 9 | `5.61.209.106` | 19 | 2.8% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd. Network | No apparent signal |
| 10 | `171.224.105.74` | 18 | 2.6% | Vietnam / Hanoi / Hanoi / VIETEL | No apparent signal |
| 11 | `195.178.110.204` | 15 | 2.2% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 12 | `91.230.168.142` | 14 | 2.0% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 13 | `195.184.76.116` | 14 | 2.0% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `91.230.168.190` | 13 | 1.9% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 15 | `91.230.168.233` | 13 | 1.9% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `134.209.229.23` | 160 | 68.4% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |
| 2 | `216.180.246.214` | 47 | 20.1% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 3 | `216.180.246.31` | 27 | 11.5% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
