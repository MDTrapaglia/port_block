# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4404
- Unique source IPs: 2284
- Unique countries/cities (24h): 290
- Unique destination ports: 2484

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 98 | 2.2% |
| 2 | `22` | 70 | 1.6% |
| 3 | `8080` | 47 | 1.1% |
| 4 | `3389` | 46 | 1.0% |
| 5 | `5060` | 31 | 0.7% |
| 6 | `8443` | 28 | 0.6% |
| 7 | `1433` | 26 | 0.6% |
| 8 | `53` | 26 | 0.6% |
| 9 | `3306` | 25 | 0.6% |
| 10 | `2222` | 23 | 0.5% |
| 11 | `9200` | 22 | 0.5% |
| 12 | `161` | 20 | 0.5% |
| 13 | `8081` | 19 | 0.4% |
| 14 | `9034` | 18 | 0.4% |
| 15 | `3000` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4012 | 91.1% |
| 2 | `UDP` | 384 | 8.7% |
| 3 | `47` | 7 | 0.2% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.93` | 109 | 2.5% |
| 2 | `109.205.211.110` | 36 | 0.8% |
| 3 | `194.180.48.39` | 34 | 0.8% |
| 4 | `129.153.224.127` | 26 | 0.6% |
| 5 | `195.178.110.89` | 25 | 0.6% |
| 6 | `193.122.228.133` | 20 | 0.5% |
| 7 | `45.198.224.125` | 16 | 0.4% |
| 8 | `18.217.208.51` | 15 | 0.3% |
| 9 | `91.231.89.0` | 15 | 0.3% |
| 10 | `91.230.168.211` | 14 | 0.3% |
| 11 | `91.231.89.150` | 14 | 0.3% |
| 12 | `45.141.233.67` | 14 | 0.3% |
| 13 | `132.226.61.140` | 14 | 0.3% |
| 14 | `129.158.246.220` | 14 | 0.3% |
| 15 | `91.196.152.190` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3876 | 96.6% |
| 2 | `ACK+FIN+PSH` | 73 | 1.8% |
| 3 | `ACK+PSH` | 42 | 1.0% |
| 4 | `ACK+FIN` | 11 | 0.3% |
| 5 | `SYN+ECE+CWR` | 8 | 0.2% |
| 6 | `ACK` | 1 | 0.0% |
| 7 | `ACK+RST` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4404 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.93` -> `1935` | 10 | 0.2% |
| 2 | `62.210.114.99` -> `3389` | 9 | 0.2% |
| 3 | `52.88.236.22` -> `10793` | 9 | 0.2% |
| 4 | `118.212.132.226` -> `22` | 8 | 0.2% |
| 5 | `216.180.246.93` -> `1911` | 8 | 0.2% |
| 6 | `216.180.246.93` -> `2022` | 8 | 0.2% |
| 7 | `44.217.232.30` -> `48847` | 7 | 0.2% |
| 8 | `216.180.246.93` -> `1887` | 7 | 0.2% |
| 9 | `216.180.246.93` -> `1980` | 7 | 0.2% |
| 10 | `216.180.246.93` -> `1987` | 7 | 0.2% |
| 11 | `216.180.246.93` -> `1988` | 7 | 0.2% |
| 12 | `216.180.246.93` -> `2003` | 7 | 0.2% |
| 13 | `159.65.130.17` -> `3000` | 6 | 0.1% |
| 14 | `170.64.224.25` -> `23` | 6 | 0.1% |
| 15 | `151.101.216.157` -> `35458` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-11 04:00:00:00 | 134 | 3.0% |
| 2026-11-11 05:00:00:00 | 177 | 4.0% |
| 2026-11-11 06:00:00:00 | 182 | 4.1% |
| 2026-11-11 07:00:00:00 | 183 | 4.2% |
| 2026-11-11 08:00:00:00 | 192 | 4.4% |
| 2026-11-11 09:00:00:00 | 182 | 4.1% |
| 2026-11-11 10:00:00:00 | 185 | 4.2% |
| 2026-11-11 11:00:00:00 | 180 | 4.1% |
| 2026-11-11 12:00:00:00 | 179 | 4.1% |
| 2026-11-11 13:00:00:00 | 198 | 4.5% |
| 2026-11-11 14:00:00:00 | 176 | 4.0% |
| 2026-11-11 15:00:00:00 | 180 | 4.1% |
| 2026-11-11 16:00:00:00 | 181 | 4.1% |
| 2026-11-11 17:00:00:00 | 178 | 4.0% |
| 2026-11-11 18:00:00:00 | 181 | 4.1% |
| 2026-11-11 19:00:00:00 | 179 | 4.1% |
| 2026-11-11 20:00:00:00 | 180 | 4.1% |
| 2026-11-11 21:00:00:00 | 181 | 4.1% |
| 2026-11-11 22:00:00:00 | 199 | 4.5% |
| 2026-11-11 23:00:00:00 | 180 | 4.1% |
| 2026-11-12 00:00:00:00 | 196 | 4.5% |
| 2026-11-12 01:00:00:00 | 193 | 4.4% |
| 2026-11-12 02:00:00:00 | 180 | 4.1% |
| 2026-11-12 03:00:00:00 | 179 | 4.1% |
| 2026-11-12 04:00:00:00 | 48 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 109 | 28.8% |
| 2 | Ashburn, United States | 74 | 19.5% |
| 3 | Amsterdam, The Netherlands | 36 | 9.5% |
| 4 | Berngau, Germany | 34 | 9.0% |
| 5 | Gravelines, France | 29 | 7.7% |
| 6 | Andorra la Vella, Andorra | 25 | 6.6% |
| 7 | Stockholm, Sweden | 16 | 4.2% |
| 8 | Dublin, United States | 15 | 4.0% |
| 9 | Hillsboro, United States | 14 | 3.7% |
| 10 | London, United Kingdom | 14 | 3.7% |
| 11 | Roubaix, France | 13 | 3.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.93` | 109 | 28.8% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `109.205.211.110` | 36 | 9.5% | The Netherlands / North Holland / Amsterdam / Colocatel Inc | Hosting/Cloud (colo) |
| 3 | `194.180.48.39` | 34 | 9.0% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 4 | `129.153.224.127` | 26 | 6.9% | United States / Virginia / Ashburn / Oracle Cloud Infrastructure (us-ashburn-1) | No apparent signal |
| 5 | `195.178.110.89` | 25 | 6.6% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 6 | `193.122.228.133` | 20 | 5.3% | United States / Virginia / Ashburn / Oracle Cloud Infrastructure (us-ashburn-1) | No apparent signal |
| 7 | `45.198.224.125` | 16 | 4.2% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 8 | `18.217.208.51` | 15 | 4.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `91.231.89.0` | 15 | 4.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `91.230.168.211` | 14 | 3.7% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 11 | `91.231.89.150` | 14 | 3.7% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 12 | `45.141.233.67` | 14 | 3.7% | United Kingdom / England / London / Razinet | No apparent signal |
| 13 | `132.226.61.140` | 14 | 3.7% | United States / Virginia / Ashburn / Oracle Cloud Infrastructure (us-ashburn-1) | No apparent signal |
| 14 | `129.158.246.220` | 14 | 3.7% | United States / Virginia / Ashburn / Oracle Cloud Infrastructure (us-ashburn-1) | No apparent signal |
| 15 | `91.196.152.190` | 13 | 3.4% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.93` | 109 | 68.1% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `109.205.211.110` | 36 | 22.5% | Hosting/Cloud (colo) | The Netherlands / North Holland / Amsterdam / Colocatel Inc |
| 3 | `18.217.208.51` | 15 | 9.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
