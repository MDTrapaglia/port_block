# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4411
- Unique source IPs: 2432
- Unique countries/cities (24h): 436
- Unique destination ports: 2415

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 492 | 11.2% |
| 2 | `22` | 45 | 1.0% |
| 3 | `3389` | 33 | 0.7% |
| 4 | `5060` | 30 | 0.7% |
| 5 | `2323` | 27 | 0.6% |
| 6 | `53` | 22 | 0.5% |
| 7 | `1433` | 21 | 0.5% |
| 8 | `8333` | 19 | 0.4% |
| 9 | `3306` | 19 | 0.4% |
| 10 | `9200` | 19 | 0.4% |
| 11 | `8080` | 18 | 0.4% |
| 12 | `1900` | 17 | 0.4% |
| 13 | `389` | 17 | 0.4% |
| 14 | `21` | 16 | 0.4% |
| 15 | `2375` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3954 | 89.6% |
| 2 | `UDP` | 444 | 10.1% |
| 3 | `47` | 12 | 0.3% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `160.119.76.62` | 385 | 8.7% |
| 2 | `103.8.29.103` | 152 | 3.4% |
| 3 | `151.101.218.73` | 42 | 1.0% |
| 4 | `47.160.209.223` | 37 | 0.8% |
| 5 | `103.15.81.78` | 26 | 0.6% |
| 6 | `143.92.53.133` | 24 | 0.5% |
| 7 | `205.186.144.66` | 23 | 0.5% |
| 8 | `89.248.163.48` | 21 | 0.5% |
| 9 | `45.139.122.80` | 19 | 0.4% |
| 10 | `192.168.100.118` | 16 | 0.4% |
| 11 | `69.17.52.1` | 15 | 0.3% |
| 12 | `172.93.106.153` | 12 | 0.3% |
| 13 | `104.36.149.26` | 12 | 0.3% |
| 14 | `3.131.24.55` | 11 | 0.2% |
| 15 | `45.142.193.146` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3815 | 96.5% |
| 2 | `ACK+FIN+PSH` | 85 | 2.1% |
| 3 | `ACK+PSH` | 34 | 0.9% |
| 4 | `ACK+FIN` | 10 | 0.3% |
| 5 | `SYN+ECE+CWR` | 6 | 0.2% |
| 6 | `ACK` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4403 | 99.8% |
| 2 | `wlan0` | 8 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `103.8.29.103` -> `23` | 152 | 3.4% |
| 2 | `47.160.209.223` -> `23` | 30 | 0.7% |
| 3 | `143.92.53.133` -> `23` | 24 | 0.5% |
| 4 | `205.186.144.66` -> `23` | 23 | 0.5% |
| 5 | `69.17.52.1` -> `8333` | 15 | 0.3% |
| 6 | `104.36.149.26` -> `23` | 12 | 0.3% |
| 7 | `45.139.122.80` -> `17000` | 8 | 0.2% |
| 8 | `47.160.209.223` -> `2323` | 7 | 0.2% |
| 9 | `151.101.218.73` -> `5107` | 7 | 0.2% |
| 10 | `3.162.185.78` -> `54280` | 7 | 0.2% |
| 11 | `151.101.218.73` -> `6637` | 7 | 0.2% |
| 12 | `140.233.190.89` -> `9000` | 5 | 0.1% |
| 13 | `124.198.131.185` -> `8021` | 5 | 0.1% |
| 14 | `178.20.210.152` -> `8728` | 5 | 0.1% |
| 15 | `199.45.155.106` -> `9012` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-11 04:00:00:00 | 131 | 3.0% |
| 2026-05-11 05:00:00:00 | 176 | 4.0% |
| 2026-05-11 06:00:00:00 | 180 | 4.1% |
| 2026-05-11 07:00:00:00 | 181 | 4.1% |
| 2026-05-11 08:00:00:00 | 179 | 4.1% |
| 2026-05-11 09:00:00:00 | 180 | 4.1% |
| 2026-05-11 10:00:00:00 | 179 | 4.1% |
| 2026-05-11 11:00:00:00 | 179 | 4.1% |
| 2026-05-11 12:00:00:00 | 178 | 4.0% |
| 2026-05-11 13:00:00:00 | 184 | 4.2% |
| 2026-05-11 14:00:00:00 | 180 | 4.1% |
| 2026-05-11 15:00:00:00 | 177 | 4.0% |
| 2026-05-11 16:00:00:00 | 198 | 4.5% |
| 2026-05-11 17:00:00:00 | 179 | 4.1% |
| 2026-05-11 18:00:00:00 | 189 | 4.3% |
| 2026-05-11 19:00:00:00 | 184 | 4.2% |
| 2026-05-11 20:00:00:00 | 179 | 4.1% |
| 2026-05-11 21:00:00:00 | 181 | 4.1% |
| 2026-05-11 22:00:00:00 | 179 | 4.1% |
| 2026-05-11 23:00:00:00 | 204 | 4.6% |
| 2026-05-12 00:00:00:00 | 180 | 4.1% |
| 2026-05-12 01:00:00:00 | 196 | 4.4% |
| 2026-05-12 02:00:00:00 | 184 | 4.2% |
| 2026-05-12 03:00:00:00 | 209 | 4.7% |
| 2026-05-12 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 425 | 52.7% |
| 2 | Chatswood, Australia | 152 | 18.9% |
| 3 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 42 | 5.2% |
| 4 | College Station, United States | 37 | 4.6% |
| 5 | New Delhi, India | 26 | 3.2% |
| 6 | Sheung Wan, Hong Kong | 24 | 3.0% |
| 7 | Ashburn, United States | 23 | 2.9% |
| 8 | private | 16 | 2.0% |
| 9 | Lewes, United States | 15 | 1.9% |
| 10 | Piscataway, United States | 12 | 1.5% |
| 11 | Calgary, Canada | 12 | 1.5% |
| 12 | Dublin, United States | 11 | 1.4% |
| 13 | London, United Kingdom | 11 | 1.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `160.119.76.62` | 385 | 47.8% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |
| 2 | `103.8.29.103` | 152 | 18.9% | Australia / New South Wales / Chatswood / MDS - AU | No apparent signal |
| 3 | `151.101.218.73` | 42 | 5.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `47.160.209.223` | 37 | 4.6% | United States / Texas / College Station / Frontier Communications Corporation | No apparent signal |
| 5 | `103.15.81.78` | 26 | 3.2% | India / National Capital Territory of Delhi / New Delhi / Spacenet  PVT LTD | No apparent signal |
| 6 | `143.92.53.133` | 24 | 3.0% | Hong Kong / Central and Western District / Sheung Wan / Rackip Consultancy Pte. LTD | No apparent signal |
| 7 | `205.186.144.66` | 23 | 2.9% | United States / Virginia / Ashburn / GoDaddy.com, LLC | No apparent signal |
| 8 | `89.248.163.48` | 21 | 2.6% | The Netherlands / North Holland / Amsterdam / Quasi Networks LTD. | No apparent signal |
| 9 | `45.139.122.80` | 19 | 2.4% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 10 | `192.168.100.118` | 16 | 2.0% | private | Private/CGNAT |
| 11 | `69.17.52.1` | 15 | 1.9% | United States / Delaware / Lewes / Spruce Creek Networks LLC | No apparent signal |
| 12 | `172.93.106.153` | 12 | 1.5% | United States / New Jersey / Piscataway / Klemen Stirn | No apparent signal |
| 13 | `104.36.149.26` | 12 | 1.5% | Canada / Alberta / Calgary / Idigital Internet Inc | No apparent signal |
| 14 | `3.131.24.55` | 11 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `45.142.193.146` | 11 | 1.4% | United Kingdom / England / London / Limited Network LTD | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.73` | 42 | 79.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `3.131.24.55` | 11 | 20.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
