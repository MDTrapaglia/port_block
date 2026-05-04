# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 2819
- Unique source IPs: 1423
- Unique countries/cities (24h): 280
- Unique destination ports: 1284

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 922 | 32.7% |
| 2 | `22` | 26 | 0.9% |
| 3 | `8080` | 16 | 0.6% |
| 4 | `5060` | 15 | 0.5% |
| 5 | `53` | 14 | 0.5% |
| 6 | `1433` | 14 | 0.5% |
| 7 | `9200` | 13 | 0.5% |
| 8 | `123` | 11 | 0.4% |
| 9 | `1900` | 11 | 0.4% |
| 10 | `3389` | 10 | 0.4% |
| 11 | `unknown` | 10 | 0.4% |
| 12 | `2375` | 10 | 0.4% |
| 13 | `8082` | 10 | 0.4% |
| 14 | `8443` | 10 | 0.4% |
| 15 | `2087` | 10 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 2550 | 90.5% |
| 2 | `UDP` | 259 | 9.2% |
| 3 | `47` | 10 | 0.4% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.77.199.58` | 314 | 11.1% |
| 2 | `35.208.244.118` | 116 | 4.1% |
| 3 | `66.117.4.184` | 106 | 3.8% |
| 4 | `180.210.206.32` | 89 | 3.2% |
| 5 | `52.117.232.104` | 76 | 2.7% |
| 6 | `185.231.223.181` | 47 | 1.7% |
| 7 | `151.101.217.44` | 25 | 0.9% |
| 8 | `192.168.100.118` | 24 | 0.9% |
| 9 | `108.61.192.199` | 20 | 0.7% |
| 10 | `194.102.73.93` | 20 | 0.7% |
| 11 | `5.9.94.245` | 16 | 0.6% |
| 12 | `164.90.152.45` | 14 | 0.5% |
| 13 | `138.255.103.43` | 14 | 0.5% |
| 14 | `85.217.149.15` | 12 | 0.4% |
| 15 | `193.93.249.19` | 12 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 2473 | 97.0% |
| 2 | `ACK+FIN+PSH` | 46 | 1.8% |
| 3 | `ACK+PSH` | 15 | 0.6% |
| 4 | `ACK+FIN` | 12 | 0.5% |
| 5 | `SYN+ECE+CWR` | 3 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 2806 | 99.5% |
| 2 | `wlan0` | 13 | 0.5% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `45.77.199.58` -> `23` | 314 | 11.1% |
| 2 | `35.208.244.118` -> `23` | 116 | 4.1% |
| 3 | `66.117.4.184` -> `23` | 106 | 3.8% |
| 4 | `180.210.206.32` -> `23` | 89 | 3.2% |
| 5 | `52.117.232.104` -> `23` | 76 | 2.7% |
| 6 | `108.61.192.199` -> `23` | 20 | 0.7% |
| 7 | `194.102.73.93` -> `23` | 20 | 0.7% |
| 8 | `5.9.94.245` -> `23` | 16 | 0.6% |
| 9 | `164.90.152.45` -> `23` | 14 | 0.5% |
| 10 | `138.255.103.43` -> `23` | 14 | 0.5% |
| 11 | `193.93.249.19` -> `23` | 12 | 0.4% |
| 12 | `193.164.133.96` -> `23` | 9 | 0.3% |
| 13 | `192.168.100.1` -> `68` | 8 | 0.3% |
| 14 | `23.196.15.96` -> `65460` | 8 | 0.3% |
| 15 | `148.251.196.140` -> `23` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-03 12:00:00:00 | 10 | 0.4% |
| 2026-05-03 13:00:00:00 | 180 | 6.4% |
| 2026-05-03 14:00:00:00 | 187 | 6.6% |
| 2026-05-03 15:00:00:00 | 182 | 6.5% |
| 2026-05-03 16:00:00:00 | 181 | 6.4% |
| 2026-05-03 17:00:00:00 | 181 | 6.4% |
| 2026-05-03 18:00:00:00 | 179 | 6.3% |
| 2026-05-03 19:00:00:00 | 182 | 6.5% |
| 2026-05-03 20:00:00:00 | 181 | 6.4% |
| 2026-05-03 21:00:00:00 | 180 | 6.4% |
| 2026-05-03 22:00:00:00 | 179 | 6.3% |
| 2026-05-03 23:00:00:00 | 183 | 6.5% |
| 2026-05-04 00:00:00:00 | 184 | 6.5% |
| 2026-05-04 01:00:00:00 | 206 | 7.3% |
| 2026-05-04 02:00:00:00 | 181 | 6.4% |
| 2026-05-04 03:00:00:00 | 200 | 7.1% |
| 2026-05-04 04:00:00:00 | 43 | 1.5% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Miami, United States | 314 | 34.7% |
| 2 | Council Bluffs, United States | 116 | 12.8% |
| 3 | Los Angeles, United States | 106 | 11.7% |
| 4 | Singapore, Singapore | 89 | 9.8% |
| 5 | Armonk, United States | 76 | 8.4% |
| 6 | Doesburg, The Netherlands | 47 | 5.2% |
| 7 | Buenos Aires, Argentina | 25 | 2.8% |
| 8 | private | 24 | 2.7% |
| 9 | Atlanta, United States | 20 | 2.2% |
| 10 | Cluj-Napoca, Romania | 20 | 2.2% |
| 11 | Falkenstein, Germany | 16 | 1.8% |
| 12 | Santa Clara, United States | 14 | 1.5% |
| 13 | La Florida, Chile | 14 | 1.5% |
| 14 | New York, United States | 12 | 1.3% |
| 15 | Sundbyberg, Sweden | 12 | 1.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `45.77.199.58` | 314 | 34.7% | United States / Florida / Miami / Vultr Holdings, LLC | Hosting/Cloud (vultr) |
| 2 | `35.208.244.118` | 116 | 12.8% | United States / Iowa / Council Bluffs / Google Cloud (us-central1) | Hosting/Cloud (google cloud) |
| 3 | `66.117.4.184` | 106 | 11.7% | United States / California / Los Angeles / Corporate Colocation Inc. | Hosting/Cloud (colo) |
| 4 | `180.210.206.32` | 89 | 9.8% | Singapore / Central Singapore / Singapore / Sparkstation | No apparent signal |
| 5 | `52.117.232.104` | 76 | 8.4% | United States / New York / Armonk / IBM Cloud | No apparent signal |
| 6 | `185.231.223.181` | 47 | 5.2% | The Netherlands / Gelderland / Doesburg / ABELOHOST | No apparent signal |
| 7 | `151.101.217.44` | 25 | 2.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 8 | `192.168.100.118` | 24 | 2.7% | private | Private/CGNAT |
| 9 | `108.61.192.199` | 20 | 2.2% | United States / Georgia / Atlanta / Vultr Holdings, LLC | Hosting/Cloud (vultr) |
| 10 | `194.102.73.93` | 20 | 2.2% | Romania / Cluj County / Cluj-Napoca / Usamvcluj | No apparent signal |
| 11 | `5.9.94.245` | 16 | 1.8% | Germany / Saxony / Falkenstein / Hetzner | Hosting/Cloud (hetzner) |
| 12 | `164.90.152.45` | 14 | 1.5% | United States / California / Santa Clara / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `138.255.103.43` | 14 | 1.5% | Chile / Santiago Metropolitan / La Florida / CARRASCO Y REYES SERVICIOS INFORMÁTICOS LIMITADA | No apparent signal |
| 14 | `85.217.149.15` | 12 | 1.3% | United States / New York / New York / Modat B.V | No apparent signal |
| 15 | `193.93.249.19` | 12 | 1.3% | Sweden / Stockholm County / Sundbyberg / BINERO | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `45.77.199.58` | 314 | 51.4% | Hosting/Cloud (vultr) | United States / Florida / Miami / Vultr Holdings, LLC |
| 2 | `35.208.244.118` | 116 | 19.0% | Hosting/Cloud (google cloud) | United States / Iowa / Council Bluffs / Google Cloud (us-central1) |
| 3 | `66.117.4.184` | 106 | 17.3% | Hosting/Cloud (colo) | United States / California / Los Angeles / Corporate Colocation Inc. |
| 4 | `151.101.217.44` | 25 | 4.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `108.61.192.199` | 20 | 3.3% | Hosting/Cloud (vultr) | United States / Georgia / Atlanta / Vultr Holdings, LLC |
| 6 | `5.9.94.245` | 16 | 2.6% | Hosting/Cloud (hetzner) | Germany / Saxony / Falkenstein / Hetzner |
| 7 | `164.90.152.45` | 14 | 2.3% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
