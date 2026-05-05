# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4340
- Unique source IPs: 2172
- Unique countries/cities (24h): 370
- Unique destination ports: 2355

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 678 | 15.6% |
| 2 | `22` | 46 | 1.1% |
| 3 | `8080` | 25 | 0.6% |
| 4 | `5060` | 24 | 0.6% |
| 5 | `3389` | 22 | 0.5% |
| 6 | `53` | 20 | 0.5% |
| 7 | `3306` | 20 | 0.5% |
| 8 | `8081` | 19 | 0.4% |
| 9 | `161` | 19 | 0.4% |
| 10 | `1433` | 17 | 0.4% |
| 11 | `unknown` | 16 | 0.4% |
| 12 | `2323` | 15 | 0.3% |
| 13 | `2087` | 15 | 0.3% |
| 14 | `8333` | 13 | 0.3% |
| 15 | `389` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3973 | 91.5% |
| 2 | `UDP` | 351 | 8.1% |
| 3 | `47` | 16 | 0.4% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `160.119.76.46` | 368 | 8.5% |
| 2 | `198.147.26.226` | 174 | 4.0% |
| 3 | `208.115.219.122` | 129 | 3.0% |
| 4 | `179.43.182.86` | 117 | 2.7% |
| 5 | `128.199.25.179` | 36 | 0.8% |
| 6 | `210.114.174.108` | 34 | 0.8% |
| 7 | `61.216.93.43` | 27 | 0.6% |
| 8 | `70.34.216.25` | 20 | 0.5% |
| 9 | `85.217.149.42` | 17 | 0.4% |
| 10 | `89.248.163.48` | 15 | 0.3% |
| 11 | `151.101.218.73` | 15 | 0.3% |
| 12 | `85.217.149.48` | 13 | 0.3% |
| 13 | `172.93.106.153` | 12 | 0.3% |
| 14 | `207.180.235.16` | 12 | 0.3% |
| 15 | `160.250.95.72` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3921 | 98.7% |
| 2 | `ACK+FIN+PSH` | 29 | 0.7% |
| 3 | `ACK+PSH` | 14 | 0.4% |
| 4 | `SYN+ECE+CWR` | 4 | 0.1% |
| 5 | `ACK+FIN` | 4 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4335 | 99.9% |
| 2 | `wlan0` | 5 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `198.147.26.226` -> `23` | 174 | 4.0% |
| 2 | `208.115.219.122` -> `23` | 129 | 3.0% |
| 3 | `179.43.182.86` -> `23` | 117 | 2.7% |
| 4 | `128.199.25.179` -> `23` | 36 | 0.8% |
| 5 | `70.34.216.25` -> `23` | 20 | 0.5% |
| 6 | `207.180.235.16` -> `23` | 12 | 0.3% |
| 7 | `160.250.95.72` -> `23` | 12 | 0.3% |
| 8 | `69.17.52.1` -> `8333` | 10 | 0.2% |
| 9 | `124.198.131.185` -> `8021` | 7 | 0.2% |
| 10 | `190.92.173.64` -> `23` | 5 | 0.1% |
| 11 | `151.101.218.73` -> `50012` | 5 | 0.1% |
| 12 | `51.159.110.167` -> `25566` | 4 | 0.1% |
| 13 | `51.159.110.167` -> `25565` | 4 | 0.1% |
| 14 | `178.20.210.152` -> `8728` | 4 | 0.1% |
| 15 | `66.132.186.193` -> `2000` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-04 04:00:00:00 | 132 | 3.0% |
| 2026-05-04 05:00:00:00 | 185 | 4.3% |
| 2026-05-04 06:00:00:00 | 180 | 4.1% |
| 2026-05-04 07:00:00:00 | 173 | 4.0% |
| 2026-05-04 08:00:00:00 | 169 | 3.9% |
| 2026-05-04 09:00:00:00 | 185 | 4.3% |
| 2026-05-04 10:00:00:00 | 173 | 4.0% |
| 2026-05-04 11:00:00:00 | 183 | 4.2% |
| 2026-05-04 12:00:00:00 | 183 | 4.2% |
| 2026-05-04 13:00:00:00 | 180 | 4.1% |
| 2026-05-04 14:00:00:00 | 177 | 4.1% |
| 2026-05-04 15:00:00:00 | 182 | 4.2% |
| 2026-05-04 16:00:00:00 | 181 | 4.2% |
| 2026-05-04 17:00:00:00 | 180 | 4.1% |
| 2026-05-04 18:00:00:00 | 180 | 4.1% |
| 2026-05-04 19:00:00:00 | 181 | 4.2% |
| 2026-05-04 20:00:00:00 | 179 | 4.1% |
| 2026-05-04 21:00:00:00 | 179 | 4.1% |
| 2026-05-04 22:00:00:00 | 180 | 4.1% |
| 2026-05-04 23:00:00:00 | 192 | 4.4% |
| 2026-05-05 00:00:00:00 | 190 | 4.4% |
| 2026-05-05 01:00:00:00 | 192 | 4.4% |
| 2026-05-05 02:00:00:00 | 180 | 4.1% |
| 2026-05-05 03:00:00:00 | 178 | 4.1% |
| 2026-05-05 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 383 | 38.3% |
| 2 | Piscataway, United States | 186 | 18.6% |
| 3 | Chicago, United States | 129 | 12.9% |
| 4 | Rümlang, Switzerland | 117 | 11.7% |
| 5 | Bengaluru, India | 36 | 3.6% |
| 6 | Seoul, South Korea | 34 | 3.4% |
| 7 | Beauharnois, Canada | 30 | 3.0% |
| 8 | New Taipei City, Taiwan | 27 | 2.7% |
| 9 | Spånga, Sweden | 20 | 2.0% |
| 10 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 15 | 1.5% |
| 11 | Lauterbourg, France | 12 | 1.2% |
| 12 | Dhaka, Bangladesh | 12 | 1.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `160.119.76.46` | 368 | 36.8% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |
| 2 | `198.147.26.226` | 174 | 17.4% | United States / New Jersey / Piscataway / Host World Net LLC | No apparent signal |
| 3 | `208.115.219.122` | 129 | 12.9% | United States / Illinois / Chicago / Limestone Networks | No apparent signal |
| 4 | `179.43.182.86` | 117 | 11.7% | Switzerland / Zurich / Rümlang / Private Layer Inc | No apparent signal |
| 5 | `128.199.25.179` | 36 | 3.6% | India / Karnataka / Bengaluru / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 6 | `210.114.174.108` | 34 | 3.4% | South Korea / Seoul / Seoul / Shinbinet IDC | No apparent signal |
| 7 | `61.216.93.43` | 27 | 2.7% | Taiwan / New Taipei City / New Taipei City / Chunghwa Telecom Co. Ltd. | No apparent signal |
| 8 | `70.34.216.25` | 20 | 2.0% | Sweden / Stockholm County / Spånga / Vultr | Hosting/Cloud (vultr) |
| 9 | `85.217.149.42` | 17 | 1.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 10 | `89.248.163.48` | 15 | 1.5% | The Netherlands / North Holland / Amsterdam / Quasi Networks LTD. | No apparent signal |
| 11 | `151.101.218.73` | 15 | 1.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 12 | `85.217.149.48` | 13 | 1.3% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 13 | `172.93.106.153` | 12 | 1.2% | United States / New Jersey / Piscataway / Klemen Stirn | No apparent signal |
| 14 | `207.180.235.16` | 12 | 1.2% | France / Grand Est / Lauterbourg / Contabo GmbH | Hosting/Cloud (contabo) |
| 15 | `160.250.95.72` | 12 | 1.2% | Bangladesh / Dhaka Division / Dhaka / Masum Talukder | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `128.199.25.179` | 36 | 43.4% | Hosting/Cloud (digitalocean) | India / Karnataka / Bengaluru / DigitalOcean, LLC |
| 2 | `70.34.216.25` | 20 | 24.1% | Hosting/Cloud (vultr) | Sweden / Stockholm County / Spånga / Vultr |
| 3 | `151.101.218.73` | 15 | 18.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `207.180.235.16` | 12 | 14.5% | Hosting/Cloud (contabo) | France / Grand Est / Lauterbourg / Contabo GmbH |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
