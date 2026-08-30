# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 669
- Unique source IPs: 575
- Unique countries/cities (24h): 141
- Unique destination ports: 494

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 45 | 6.7% |
| 2 | `22` | 19 | 2.8% |
| 3 | `5555` | 8 | 1.2% |
| 4 | `10661` | 8 | 1.2% |
| 5 | `5060` | 6 | 0.9% |
| 6 | `unknown` | 6 | 0.9% |
| 7 | `49291` | 6 | 0.9% |
| 8 | `8080` | 5 | 0.7% |
| 9 | `27017` | 5 | 0.7% |
| 10 | `123` | 4 | 0.6% |
| 11 | `1080` | 4 | 0.6% |
| 12 | `3306` | 4 | 0.6% |
| 13 | `1434` | 4 | 0.6% |
| 14 | `993` | 4 | 0.6% |
| 15 | `88` | 4 | 0.6% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 582 | 87.0% |
| 2 | `UDP` | 81 | 12.1% |
| 3 | `47` | 6 | 0.9% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `81.110.171.250` | 9 | 1.3% |
| 2 | `54.203.147.253` | 8 | 1.2% |
| 3 | `38.51.144.232` | 6 | 0.9% |
| 4 | `192.248.150.180` | 4 | 0.6% |
| 5 | `85.217.140.33` | 4 | 0.6% |
| 6 | `193.163.125.205` | 3 | 0.4% |
| 7 | `185.73.23.133` | 3 | 0.4% |
| 8 | `3.131.24.55` | 3 | 0.4% |
| 9 | `204.76.203.4` | 3 | 0.4% |
| 10 | `177.128.174.242` | 3 | 0.4% |
| 11 | `85.217.140.35` | 3 | 0.4% |
| 12 | `85.217.140.30` | 3 | 0.4% |
| 13 | `66.69.123.191` | 3 | 0.4% |
| 14 | `168.196.246.184` | 3 | 0.4% |
| 15 | `85.217.140.29` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 563 | 96.7% |
| 2 | `ACK+PSH` | 17 | 2.9% |
| 3 | `SYN+ECE+CWR` | 2 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 669 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `81.110.171.250` -> `23` | 9 | 1.3% |
| 2 | `54.203.147.253` -> `10661` | 8 | 1.2% |
| 3 | `38.51.144.232` -> `49291` | 6 | 0.9% |
| 4 | `66.132.195.85` -> `1194` | 2 | 0.3% |
| 5 | `102.38.103.239` -> `22` | 2 | 0.3% |
| 6 | `204.76.203.4` -> `25565` | 2 | 0.3% |
| 7 | `207.175.206.140` -> `27017` | 2 | 0.3% |
| 8 | `177.128.174.242` -> `23` | 2 | 0.3% |
| 9 | `66.69.123.191` -> `22` | 2 | 0.3% |
| 10 | `168.196.246.184` -> `23` | 2 | 0.3% |
| 11 | `181.78.94.156` -> `22` | 2 | 0.3% |
| 12 | `34.38.31.171` -> `22` | 2 | 0.3% |
| 13 | `178.20.210.151` -> `22` | 2 | 0.3% |
| 14 | `178.20.210.152` -> `1723` | 2 | 0.3% |
| 15 | `34.79.151.68` -> `110` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-08-30 00:00:00:00 | 80 | 12.0% |
| 2026-08-30 01:00:00:00 | 182 | 27.2% |
| 2026-08-30 02:00:00:00 | 180 | 26.9% |
| 2026-08-30 03:00:00:00 | 175 | 26.2% |
| 2026-08-30 04:00:00:00 | 51 | 7.6% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Gravelines, France | 13 | 21.3% |
| 2 | Manchester, United Kingdom | 9 | 14.8% |
| 3 | Portland, United States | 8 | 13.1% |
| 4 | Meredith, United States | 6 | 9.8% |
| 5 | Canary Wharf, United Kingdom | 4 | 6.6% |
| 6 | Leeds, United Kingdom | 3 | 4.9% |
| 7 | Frankfurt am Main, Germany | 3 | 4.9% |
| 8 | Dublin, United States | 3 | 4.9% |
| 9 | Eygelshoven, The Netherlands | 3 | 4.9% |
| 10 | Belo Horizonte, Brazil | 3 | 4.9% |
| 11 | Rowlett, United States | 3 | 4.9% |
| 12 | Moreno, Argentina | 3 | 4.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `81.110.171.250` | 9 | 14.8% | United Kingdom / England / Manchester / Vmcbbuk | No apparent signal |
| 2 | `54.203.147.253` | 8 | 13.1% | United States / Oregon / Portland / AWS EC2 (us-west-2) | Hosting/Cloud (aws) |
| 3 | `38.51.144.232` | 6 | 9.8% | United States / New Hampshire / Meredith / Conexon Connect | No apparent signal |
| 4 | `192.248.150.180` | 4 | 6.6% | United Kingdom / England / Canary Wharf / Vultr Holdings LLC London | Hosting/Cloud (vultr) |
| 5 | `85.217.140.33` | 4 | 6.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `193.163.125.205` | 3 | 4.9% | United Kingdom / England / Leeds / Constantine Cybersecurity LTD | No apparent signal |
| 7 | `185.73.23.133` | 3 | 4.9% | Germany / Hesse / Frankfurt am Main / RUB LIR Inet2 | No apparent signal |
| 8 | `3.131.24.55` | 3 | 4.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `204.76.203.4` | 3 | 4.9% | The Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 10 | `177.128.174.242` | 3 | 4.9% | Brazil / Minas Gerais / Belo Horizonte / Lsnetwoks Solutions | No apparent signal |
| 11 | `85.217.140.35` | 3 | 4.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.30` | 3 | 4.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `66.69.123.191` | 3 | 4.9% | United States / Texas / Rowlett / Spectrum | No apparent signal |
| 14 | `168.196.246.184` | 3 | 4.9% | Argentina / Buenos Aires / Moreno / Linkear SRL | No apparent signal |
| 15 | `85.217.140.29` | 3 | 4.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `54.203.147.253` | 8 | 53.3% | Hosting/Cloud (aws) | United States / Oregon / Portland / AWS EC2 (us-west-2) |
| 2 | `192.248.150.180` | 4 | 26.7% | Hosting/Cloud (vultr) | United Kingdom / England / Canary Wharf / Vultr Holdings LLC London |
| 3 | `3.131.24.55` | 3 | 20.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
