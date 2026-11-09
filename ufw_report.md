# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4320
- Unique source IPs: 2661
- Unique countries/cities (24h): 327
- Unique destination ports: 2262

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 158 | 3.7% |
| 2 | `22` | 88 | 2.0% |
| 3 | `8080` | 51 | 1.2% |
| 4 | `5060` | 48 | 1.1% |
| 5 | `3389` | 44 | 1.0% |
| 6 | `53` | 38 | 0.9% |
| 7 | `9034` | 32 | 0.7% |
| 8 | `1433` | 25 | 0.6% |
| 9 | `2222` | 22 | 0.5% |
| 10 | `9200` | 21 | 0.5% |
| 11 | `8443` | 21 | 0.5% |
| 12 | `8081` | 18 | 0.4% |
| 13 | `1723` | 18 | 0.4% |
| 14 | `21` | 18 | 0.4% |
| 15 | `5555` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3950 | 91.4% |
| 2 | `UDP` | 367 | 8.5% |
| 3 | `47` | 2 | 0.0% |
| 4 | `132` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.215` | 148 | 3.4% |
| 2 | `216.180.246.165` | 88 | 2.0% |
| 3 | `45.148.121.138` | 40 | 0.9% |
| 4 | `79.124.58.134` | 28 | 0.6% |
| 5 | `195.178.110.89` | 16 | 0.4% |
| 6 | `195.178.110.92` | 14 | 0.3% |
| 7 | `79.124.49.146` | 13 | 0.3% |
| 8 | `3.147.122.184` | 12 | 0.3% |
| 9 | `3.83.245.221` | 12 | 0.3% |
| 10 | `3.151.116.231` | 12 | 0.3% |
| 11 | `45.198.224.125` | 12 | 0.3% |
| 12 | `34.228.104.231` | 11 | 0.3% |
| 13 | `164.92.200.161` | 11 | 0.3% |
| 14 | `91.196.152.235` | 10 | 0.2% |
| 15 | `86.54.31.44` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3948 | 99.9% |
| 2 | `SYN+ECE+CWR` | 2 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4320 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.148.121.138` -> `23` | 40 | 0.9% |
| 2 | `216.180.246.165` -> `8111` | 11 | 0.3% |
| 3 | `216.180.246.215` -> `9418` | 9 | 0.2% |
| 4 | `216.180.246.215` -> `9443` | 9 | 0.2% |
| 5 | `216.180.246.215` -> `9600` | 9 | 0.2% |
| 6 | `216.180.246.165` -> `8252` | 9 | 0.2% |
| 7 | `216.180.246.215` -> `9200` | 8 | 0.2% |
| 8 | `62.210.114.99` -> `3389` | 8 | 0.2% |
| 9 | `154.80.128.160` -> `6036` | 8 | 0.2% |
| 10 | `216.180.246.215` -> `9887` | 8 | 0.2% |
| 11 | `45.198.224.125` -> `8080` | 7 | 0.2% |
| 12 | `154.80.128.163` -> `17000` | 7 | 0.2% |
| 13 | `216.180.246.215` -> `9876` | 7 | 0.2% |
| 14 | `216.180.246.215` -> `9904` | 7 | 0.2% |
| 15 | `216.180.246.215` -> `9924` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-08 04:00:00:00 | 135 | 3.1% |
| 2026-11-08 05:00:00:00 | 180 | 4.2% |
| 2026-11-08 06:00:00:00 | 179 | 4.1% |
| 2026-11-08 07:00:00:00 | 180 | 4.2% |
| 2026-11-08 08:00:00:00 | 180 | 4.2% |
| 2026-11-08 09:00:00:00 | 180 | 4.2% |
| 2026-11-08 10:00:00:00 | 178 | 4.1% |
| 2026-11-08 11:00:00:00 | 182 | 4.2% |
| 2026-11-08 12:00:00:00 | 180 | 4.2% |
| 2026-11-08 13:00:00:00 | 180 | 4.2% |
| 2026-11-08 14:00:00:00 | 180 | 4.2% |
| 2026-11-08 15:00:00:00 | 179 | 4.1% |
| 2026-11-08 16:00:00:00 | 182 | 4.2% |
| 2026-11-08 17:00:00:00 | 178 | 4.1% |
| 2026-11-08 18:00:00:00 | 180 | 4.2% |
| 2026-11-08 19:00:00:00 | 179 | 4.1% |
| 2026-11-08 20:00:00:00 | 180 | 4.2% |
| 2026-11-08 21:00:00:00 | 183 | 4.2% |
| 2026-11-08 22:00:00:00 | 180 | 4.2% |
| 2026-11-08 23:00:00:00 | 178 | 4.1% |
| 2026-11-09 00:00:00:00 | 181 | 4.2% |
| 2026-11-09 01:00:00:00 | 181 | 4.2% |
| 2026-11-09 02:00:00:00 | 179 | 4.1% |
| 2026-11-09 03:00:00:00 | 179 | 4.1% |
| 2026-11-09 04:00:00:00 | 47 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 236 | 54.0% |
| 2 | Amsterdam, The Netherlands | 50 | 11.4% |
| 3 | Sopot, Bulgaria | 41 | 9.4% |
| 4 | Andorra la Vella, Andorra | 30 | 6.9% |
| 5 | Dublin, United States | 24 | 5.5% |
| 6 | Ashburn, United States | 23 | 5.3% |
| 7 | Stockholm, Sweden | 12 | 2.7% |
| 8 | Frankfurt am Main, Germany | 11 | 2.5% |
| 9 | Roubaix, France | 10 | 2.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.215` | 148 | 33.9% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `216.180.246.165` | 88 | 20.1% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 3 | `45.148.121.138` | 40 | 9.2% | The Netherlands / North Holland / Amsterdam / SpectraIP B.V. | No apparent signal |
| 4 | `79.124.58.134` | 28 | 6.4% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 5 | `195.178.110.89` | 16 | 3.7% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 6 | `195.178.110.92` | 14 | 3.2% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 7 | `79.124.49.146` | 13 | 3.0% | Bulgaria / Plovdiv / Sopot / Tamatiya EOOD | No apparent signal |
| 8 | `3.147.122.184` | 12 | 2.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `3.83.245.221` | 12 | 2.7% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 10 | `3.151.116.231` | 12 | 2.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `45.198.224.125` | 12 | 2.7% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 12 | `34.228.104.231` | 11 | 2.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `164.92.200.161` | 11 | 2.5% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 14 | `91.196.152.235` | 10 | 2.3% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 15 | `86.54.31.44` | 10 | 2.3% | The Netherlands / North Holland / Amsterdam / MISTRAL | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.215` | 148 | 50.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `216.180.246.165` | 88 | 29.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 3 | `3.147.122.184` | 12 | 4.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `3.83.245.221` | 12 | 4.1% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `3.151.116.231` | 12 | 4.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `34.228.104.231` | 11 | 3.7% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 7 | `164.92.200.161` | 11 | 3.7% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
