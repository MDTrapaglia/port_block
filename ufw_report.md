# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4473
- Unique source IPs: 2204
- Unique countries/cities (24h): 278
- Unique destination ports: 2139

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 877 | 19.6% |
| 2 | `22` | 74 | 1.7% |
| 3 | `1433` | 27 | 0.6% |
| 4 | `3389` | 27 | 0.6% |
| 5 | `8080` | 27 | 0.6% |
| 6 | `5060` | 25 | 0.6% |
| 7 | `53` | 24 | 0.5% |
| 8 | `8888` | 21 | 0.5% |
| 9 | `161` | 21 | 0.5% |
| 10 | `8443` | 21 | 0.5% |
| 11 | `9200` | 17 | 0.4% |
| 12 | `21` | 15 | 0.3% |
| 13 | `1723` | 15 | 0.3% |
| 14 | `3306` | 14 | 0.3% |
| 15 | `8000` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4187 | 93.6% |
| 2 | `UDP` | 283 | 6.3% |
| 3 | `132` | 2 | 0.0% |
| 4 | `47` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `170.64.224.25` | 775 | 17.3% |
| 2 | `149.154.166.110` | 25 | 0.6% |
| 3 | `151.101.218.13` | 24 | 0.5% |
| 4 | `151.101.218.73` | 24 | 0.5% |
| 5 | `157.151.204.243` | 20 | 0.4% |
| 6 | `129.153.38.83` | 16 | 0.4% |
| 7 | `194.180.48.122` | 15 | 0.3% |
| 8 | `3.147.122.184` | 14 | 0.3% |
| 9 | `157.151.190.65` | 14 | 0.3% |
| 10 | `79.124.62.10` | 14 | 0.3% |
| 11 | `18.119.209.50` | 13 | 0.3% |
| 12 | `195.184.76.220` | 13 | 0.3% |
| 13 | `91.196.152.123` | 12 | 0.3% |
| 14 | `91.231.89.205` | 12 | 0.3% |
| 15 | `93.174.95.106` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3987 | 95.2% |
| 2 | `ACK+FIN+PSH` | 126 | 3.0% |
| 3 | `ACK+PSH` | 35 | 0.8% |
| 4 | `ACK+FIN` | 29 | 0.7% |
| 5 | `SYN+ECE+CWR` | 10 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4473 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `170.64.224.25` -> `23` | 775 | 17.3% |
| 2 | `151.101.218.13` -> `51500` | 9 | 0.2% |
| 3 | `151.101.218.13` -> `52534` | 8 | 0.2% |
| 4 | `61.218.153.56` -> `23` | 7 | 0.2% |
| 5 | `149.154.166.110` -> `48348` | 6 | 0.1% |
| 6 | `221.146.115.141` -> `23` | 5 | 0.1% |
| 7 | `93.123.109.6` -> `1723` | 5 | 0.1% |
| 8 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 9 | `118.212.132.226` -> `22` | 5 | 0.1% |
| 10 | `91.224.92.45` -> `34567` | 5 | 0.1% |
| 11 | `34.104.30.2` -> `64230` | 5 | 0.1% |
| 12 | `2.22.149.168` -> `21585` | 5 | 0.1% |
| 13 | `8.233.134.81` -> `24491` | 5 | 0.1% |
| 14 | `95.100.88.59` -> `53570` | 5 | 0.1% |
| 15 | `170.51.247.34` -> `24513` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-17 04:00:00:00 | 138 | 3.1% |
| 2026-11-17 05:00:00:00 | 179 | 4.0% |
| 2026-11-17 06:00:00:00 | 180 | 4.0% |
| 2026-11-17 07:00:00:00 | 189 | 4.2% |
| 2026-11-17 08:00:00:00 | 181 | 4.0% |
| 2026-11-17 09:00:00:00 | 187 | 4.2% |
| 2026-11-17 10:00:00:00 | 179 | 4.0% |
| 2026-11-17 11:00:00:00 | 181 | 4.0% |
| 2026-11-17 12:00:00:00 | 181 | 4.0% |
| 2026-11-17 13:00:00:00 | 190 | 4.2% |
| 2026-11-17 14:00:00:00 | 184 | 4.1% |
| 2026-11-17 15:00:00:00 | 205 | 4.6% |
| 2026-11-17 16:00:00:00 | 181 | 4.0% |
| 2026-11-17 17:00:00:00 | 181 | 4.0% |
| 2026-11-17 18:00:00:00 | 179 | 4.0% |
| 2026-11-17 19:00:00:00 | 182 | 4.1% |
| 2026-11-17 20:00:00:00 | 189 | 4.2% |
| 2026-11-17 21:00:00:00 | 180 | 4.0% |
| 2026-11-17 22:00:00:00 | 180 | 4.0% |
| 2026-11-17 23:00:00:00 | 198 | 4.4% |
| 2026-11-18 00:00:00:00 | 180 | 4.0% |
| 2026-11-18 01:00:00:00 | 223 | 5.0% |
| 2026-11-18 02:00:00:00 | 180 | 4.0% |
| 2026-11-18 03:00:00:00 | 202 | 4.5% |
| 2026-11-18 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Sydney, Australia | 775 | 77.3% |
| 2 | Ashburn, United States | 50 | 5.0% |
| 3 | Amsterdam, Netherlands | 37 | 3.7% |
| 4 | Dublin, United States | 27 | 2.7% |
| 5 | Buenos Aires, Argentina | 24 | 2.4% |
| 6 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 24 | 2.4% |
| 7 | Berngau, Germany | 15 | 1.5% |
| 8 | Victoria, Seychelles | 14 | 1.4% |
| 9 | Warrenton, United States | 13 | 1.3% |
| 10 | Roubaix, France | 12 | 1.2% |
| 11 | Gravelines, France | 12 | 1.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `170.64.224.25` | 775 | 77.3% | Australia / New South Wales / Sydney / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `149.154.166.110` | 25 | 2.5% | Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 3 | `151.101.218.13` | 24 | 2.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `151.101.218.73` | 24 | 2.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `157.151.204.243` | 20 | 2.0% | United States / Virginia / Ashburn / Oracle Cloud Infrastructure (us-ashburn-1) | No apparent signal |
| 6 | `129.153.38.83` | 16 | 1.6% | United States / Virginia / Ashburn / Oracle Cloud Infrastructure (us-ashburn-1) | No apparent signal |
| 7 | `194.180.48.122` | 15 | 1.5% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 8 | `3.147.122.184` | 14 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `157.151.190.65` | 14 | 1.4% | United States / Virginia / Ashburn / Oracle Cloud Infrastructure (us-ashburn-1) | No apparent signal |
| 10 | `79.124.62.10` | 14 | 1.4% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 11 | `18.119.209.50` | 13 | 1.3% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `195.184.76.220` | 13 | 1.3% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 13 | `91.196.152.123` | 12 | 1.2% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 14 | `91.231.89.205` | 12 | 1.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `93.174.95.106` | 12 | 1.2% | Netherlands / North Holland / Amsterdam / IP Volume inc | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `170.64.224.25` | 775 | 91.2% | Hosting/Cloud (digitalocean) | Australia / New South Wales / Sydney / DigitalOcean, LLC |
| 2 | `151.101.218.13` | 24 | 2.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.73` | 24 | 2.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `3.147.122.184` | 14 | 1.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.119.209.50` | 13 | 1.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
