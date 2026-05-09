# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4419
- Unique source IPs: 2447
- Unique countries/cities (24h): 326
- Unique destination ports: 2329

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 708 | 16.0% |
| 2 | `22` | 41 | 0.9% |
| 3 | `5060` | 39 | 0.9% |
| 4 | `8080` | 30 | 0.7% |
| 5 | `3389` | 28 | 0.6% |
| 6 | `5555` | 21 | 0.5% |
| 7 | `5900` | 20 | 0.5% |
| 8 | `1433` | 20 | 0.5% |
| 9 | `8000` | 18 | 0.4% |
| 10 | `3306` | 18 | 0.4% |
| 11 | `53` | 17 | 0.4% |
| 12 | `8443` | 16 | 0.4% |
| 13 | `8081` | 15 | 0.3% |
| 14 | `unknown` | 15 | 0.3% |
| 15 | `25` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4036 | 91.3% |
| 2 | `UDP` | 368 | 8.3% |
| 3 | `47` | 14 | 0.3% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `89.163.135.198` | 172 | 3.9% |
| 2 | `69.4.83.194` | 156 | 3.5% |
| 3 | `101.71.122.130` | 54 | 1.2% |
| 4 | `173.247.242.229` | 42 | 1.0% |
| 5 | `151.101.218.73` | 38 | 0.9% |
| 6 | `193.32.208.81` | 29 | 0.7% |
| 7 | `68.178.163.112` | 28 | 0.6% |
| 8 | `98.70.24.181` | 25 | 0.6% |
| 9 | `5.175.45.46` | 24 | 0.5% |
| 10 | `34.160.212.185` | 23 | 0.5% |
| 11 | `102.130.71.187` | 23 | 0.5% |
| 12 | `85.239.151.36` | 20 | 0.5% |
| 13 | `13.92.135.230` | 18 | 0.4% |
| 14 | `164.92.188.38` | 17 | 0.4% |
| 15 | `66.96.207.92` | 17 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3872 | 95.9% |
| 2 | `ACK+FIN+PSH` | 76 | 1.9% |
| 3 | `ACK+PSH` | 55 | 1.4% |
| 4 | `ACK+FIN` | 19 | 0.5% |
| 5 | `SYN+ECE+CWR` | 10 | 0.2% |
| 6 | `ACK` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4411 | 99.8% |
| 2 | `wlan0` | 8 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `89.163.135.198` -> `23` | 172 | 3.9% |
| 2 | `69.4.83.194` -> `23` | 156 | 3.5% |
| 3 | `173.247.242.229` -> `23` | 42 | 1.0% |
| 4 | `193.32.208.81` -> `23` | 29 | 0.7% |
| 5 | `68.178.163.112` -> `23` | 28 | 0.6% |
| 6 | `98.70.24.181` -> `23` | 25 | 0.6% |
| 7 | `5.175.45.46` -> `23` | 24 | 0.5% |
| 8 | `102.130.71.187` -> `23` | 23 | 0.5% |
| 9 | `13.92.135.230` -> `23` | 18 | 0.4% |
| 10 | `164.92.188.38` -> `23` | 17 | 0.4% |
| 11 | `138.201.195.227` -> `23` | 15 | 0.3% |
| 12 | `176.65.139.8` -> `5555` | 12 | 0.3% |
| 13 | `69.17.52.1` -> `8333` | 10 | 0.2% |
| 14 | `195.154.59.83` -> `23` | 10 | 0.2% |
| 15 | `124.198.131.185` -> `8021` | 9 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-08 04:00:00:00 | 133 | 3.0% |
| 2026-05-08 05:00:00:00 | 180 | 4.1% |
| 2026-05-08 06:00:00:00 | 181 | 4.1% |
| 2026-05-08 07:00:00:00 | 183 | 4.1% |
| 2026-05-08 08:00:00:00 | 178 | 4.0% |
| 2026-05-08 09:00:00:00 | 181 | 4.1% |
| 2026-05-08 10:00:00:00 | 180 | 4.1% |
| 2026-05-08 11:00:00:00 | 184 | 4.2% |
| 2026-05-08 12:00:00:00 | 178 | 4.0% |
| 2026-05-08 13:00:00:00 | 197 | 4.5% |
| 2026-05-08 14:00:00:00 | 179 | 4.1% |
| 2026-05-08 15:00:00:00 | 182 | 4.1% |
| 2026-05-08 16:00:00:00 | 194 | 4.4% |
| 2026-05-08 17:00:00:00 | 178 | 4.0% |
| 2026-05-08 18:00:00:00 | 194 | 4.4% |
| 2026-05-08 19:00:00:00 | 182 | 4.1% |
| 2026-05-08 20:00:00:00 | 178 | 4.0% |
| 2026-05-08 21:00:00:00 | 179 | 4.1% |
| 2026-05-08 22:00:00:00 | 181 | 4.1% |
| 2026-05-08 23:00:00:00 | 188 | 4.3% |
| 2026-05-09 00:00:00:00 | 180 | 4.1% |
| 2026-05-09 01:00:00:00 | 210 | 4.8% |
| 2026-05-09 02:00:00:00 | 193 | 4.4% |
| 2026-05-09 03:00:00:00 | 182 | 4.1% |
| 2026-05-09 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Frankfurt am Main, Germany | 189 | 27.6% |
| 2 | Buffalo, United States | 156 | 22.7% |
| 3 | Hangzhou, China | 54 | 7.9% |
| 4 | Los Angeles, United States | 42 | 6.1% |
| 5 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 38 | 5.5% |
| 6 | City of London, United Kingdom | 29 | 4.2% |
| 7 | Santa Clara, United States | 28 | 4.1% |
| 8 | Pune, India | 25 | 3.6% |
| 9 | Madrid, Spain | 24 | 3.5% |
| 10 | Kansas City, United States | 23 | 3.4% |
| 11 | Luanda, Angola | 23 | 3.4% |
| 12 | New York, United States | 20 | 2.9% |
| 13 | Boydton, United States | 18 | 2.6% |
| 14 | Singapore, Singapore | 17 | 2.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `89.163.135.198` | 172 | 25.1% | Germany / Hesse / Frankfurt am Main / myLoc managed IT AG | No apparent signal |
| 2 | `69.4.83.194` | 156 | 22.7% | United States / New York / Buffalo / B2 Net Solutions Inc | No apparent signal |
| 3 | `101.71.122.130` | 54 | 7.9% | China / Zhejiang / Hangzhou / China Unicom Zhejiang Province Network | No apparent signal |
| 4 | `173.247.242.229` | 42 | 6.1% | United States / California / Los Angeles / Corporate Colocation Inc. | Hosting/Cloud (colo) |
| 5 | `151.101.218.73` | 38 | 5.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `193.32.208.81` | 29 | 4.2% | United Kingdom / England / City of London / Hydra Communications Ltd | No apparent signal |
| 7 | `68.178.163.112` | 28 | 4.1% | United States / California / Santa Clara / GoDaddy.com, LLC | No apparent signal |
| 8 | `98.70.24.181` | 25 | 3.6% | India / Maharashtra / Pune / Microsoft Azure Cloud (centralindia) | Hosting/Cloud (azure) |
| 9 | `5.175.45.46` | 24 | 3.5% | Spain / Madrid / Madrid / AXARNET COMUNICACIONES, S.L | No apparent signal |
| 10 | `34.160.212.185` | 23 | 3.4% | United States / Missouri / Kansas City / Google Cloud | Hosting/Cloud (google cloud) |
| 11 | `102.130.71.187` | 23 | 3.4% | Angola / Luanda Province / Luanda / Resvd | No apparent signal |
| 12 | `85.239.151.36` | 20 | 2.9% | United States / New York / New York / Aeza Network | No apparent signal |
| 13 | `13.92.135.230` | 18 | 2.6% | United States / Virginia / Boydton / Microsoft Azure Cloud (eastus) | Hosting/Cloud (azure) |
| 14 | `164.92.188.38` | 17 | 2.5% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 15 | `66.96.207.92` | 17 | 2.5% | Singapore / Central Singapore / Singapore / MyRepublic Ltd | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `173.247.242.229` | 42 | 25.8% | Hosting/Cloud (colo) | United States / California / Los Angeles / Corporate Colocation Inc. |
| 2 | `151.101.218.73` | 38 | 23.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `98.70.24.181` | 25 | 15.3% | Hosting/Cloud (azure) | India / Maharashtra / Pune / Microsoft Azure Cloud (centralindia) |
| 4 | `34.160.212.185` | 23 | 14.1% | Hosting/Cloud (google cloud) | United States / Missouri / Kansas City / Google Cloud |
| 5 | `13.92.135.230` | 18 | 11.0% | Hosting/Cloud (azure) | United States / Virginia / Boydton / Microsoft Azure Cloud (eastus) |
| 6 | `164.92.188.38` | 17 | 10.4% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
