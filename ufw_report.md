# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4444
- Unique source IPs: 2424
- Unique countries/cities (24h): 353
- Unique destination ports: 2405

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 801 | 18.0% |
| 2 | `22` | 42 | 0.9% |
| 3 | `5060` | 32 | 0.7% |
| 4 | `3389` | 24 | 0.5% |
| 5 | `1433` | 22 | 0.5% |
| 6 | `8080` | 22 | 0.5% |
| 7 | `2323` | 19 | 0.4% |
| 8 | `53` | 19 | 0.4% |
| 9 | `unknown` | 17 | 0.4% |
| 10 | `8333` | 17 | 0.4% |
| 11 | `8088` | 16 | 0.4% |
| 12 | `8443` | 14 | 0.3% |
| 13 | `9200` | 14 | 0.3% |
| 14 | `3306` | 14 | 0.3% |
| 15 | `25` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4060 | 91.4% |
| 2 | `UDP` | 367 | 8.3% |
| 3 | `47` | 15 | 0.3% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `108.61.215.49` | 264 | 5.9% |
| 2 | `45.77.219.186` | 101 | 2.3% |
| 3 | `208.88.75.246` | 72 | 1.6% |
| 4 | `163.61.188.112` | 52 | 1.2% |
| 5 | `144.31.70.89` | 42 | 0.9% |
| 6 | `198.27.76.181` | 39 | 0.9% |
| 7 | `104.152.49.214` | 36 | 0.8% |
| 8 | `65.108.205.251` | 22 | 0.5% |
| 9 | `85.217.149.51` | 20 | 0.5% |
| 10 | `185.129.249.130` | 16 | 0.4% |
| 11 | `192.168.100.118` | 15 | 0.3% |
| 12 | `61.220.189.187` | 15 | 0.3% |
| 13 | `85.217.149.47` | 14 | 0.3% |
| 14 | `85.217.149.34` | 14 | 0.3% |
| 15 | `2.23.164.172` | 14 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3884 | 95.7% |
| 2 | `ACK+FIN+PSH` | 92 | 2.3% |
| 3 | `ACK+PSH` | 52 | 1.3% |
| 4 | `ACK+FIN` | 25 | 0.6% |
| 5 | `ACK` | 5 | 0.1% |
| 6 | `ACK+RST` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4438 | 99.9% |
| 2 | `wlan0` | 6 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `108.61.215.49` -> `23` | 264 | 5.9% |
| 2 | `45.77.219.186` -> `23` | 101 | 2.3% |
| 3 | `208.88.75.246` -> `23` | 72 | 1.6% |
| 4 | `163.61.188.112` -> `23` | 52 | 1.2% |
| 5 | `198.27.76.181` -> `23` | 39 | 0.9% |
| 6 | `104.152.49.214` -> `23` | 36 | 0.8% |
| 7 | `65.108.205.251` -> `23` | 22 | 0.5% |
| 8 | `185.129.249.130` -> `23` | 16 | 0.4% |
| 9 | `61.220.189.187` -> `23` | 15 | 0.3% |
| 10 | `69.17.52.1` -> `8333` | 12 | 0.3% |
| 11 | `194.60.201.105` -> `23` | 11 | 0.2% |
| 12 | `45.139.122.80` -> `60001` | 8 | 0.2% |
| 13 | `37.60.254.188` -> `23` | 7 | 0.2% |
| 14 | `23.64.58.145` -> `52964` | 7 | 0.2% |
| 15 | `51.159.110.167` -> `25564` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-05 04:00:00:00 | 136 | 3.1% |
| 2026-05-05 05:00:00:00 | 177 | 4.0% |
| 2026-05-05 06:00:00:00 | 183 | 4.1% |
| 2026-05-05 07:00:00:00 | 182 | 4.1% |
| 2026-05-05 08:00:00:00 | 189 | 4.3% |
| 2026-05-05 09:00:00:00 | 180 | 4.1% |
| 2026-05-05 10:00:00:00 | 181 | 4.1% |
| 2026-05-05 11:00:00:00 | 180 | 4.1% |
| 2026-05-05 12:00:00:00 | 177 | 4.0% |
| 2026-05-05 13:00:00:00 | 186 | 4.2% |
| 2026-05-05 14:00:00:00 | 186 | 4.2% |
| 2026-05-05 15:00:00:00 | 182 | 4.1% |
| 2026-05-05 16:00:00:00 | 180 | 4.1% |
| 2026-05-05 17:00:00:00 | 180 | 4.1% |
| 2026-05-05 18:00:00:00 | 180 | 4.1% |
| 2026-05-05 19:00:00:00 | 180 | 4.1% |
| 2026-05-05 20:00:00:00 | 180 | 4.1% |
| 2026-05-05 21:00:00:00 | 207 | 4.7% |
| 2026-05-05 22:00:00:00 | 181 | 4.1% |
| 2026-05-05 23:00:00:00 | 181 | 4.1% |
| 2026-05-06 00:00:00:00 | 200 | 4.5% |
| 2026-05-06 01:00:00:00 | 227 | 5.1% |
| 2026-05-06 02:00:00:00 | 186 | 4.2% |
| 2026-05-06 03:00:00:00 | 179 | 4.0% |
| 2026-05-06 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Atlanta, United States | 264 | 35.9% |
| 2 | Piscataway, United States | 101 | 13.7% |
| 3 | Buffalo, United States | 72 | 9.8% |
| 4 | Staten Island, United States | 52 | 7.1% |
| 5 | Amsterdam, Netherlands | 42 | 5.7% |
| 6 | Montreal, Canada | 39 | 5.3% |
| 7 | Nuremberg, Germany | 36 | 4.9% |
| 8 | Beauharnois, Canada | 34 | 4.6% |
| 9 | Helsinki, Finland | 22 | 3.0% |
| 10 | Paterna, Spain | 16 | 2.2% |
| 11 | private | 15 | 2.0% |
| 12 | New Taipei City, Taiwan | 15 | 2.0% |
| 13 | New York, United States | 14 | 1.9% |
| 14 | Buenos Aires, Argentina | 14 | 1.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `108.61.215.49` | 264 | 35.9% | United States / Georgia / Atlanta / Vultr Holdings, LLC | Hosting/Cloud (vultr) |
| 2 | `45.77.219.186` | 101 | 13.7% | United States / New Jersey / Piscataway / Vultr Holdings, LLC | Hosting/Cloud (vultr) |
| 3 | `208.88.75.246` | 72 | 9.8% | United States / New York / Buffalo / HostPapa | No apparent signal |
| 4 | `163.61.188.112` | 52 | 7.1% | United States / New York / Staten Island / MIT | No apparent signal |
| 5 | `144.31.70.89` | 42 | 5.7% | Netherlands / North Holland / Amsterdam / u1host Amsterdam | No apparent signal |
| 6 | `198.27.76.181` | 39 | 5.3% | Canada / Quebec / Montreal / OVH Hosting, Inc. | Hosting/Cloud (ovh) |
| 7 | `104.152.49.214` | 36 | 4.9% | Germany / Bavaria / Nuremberg / DA International Group Ltd | No apparent signal |
| 8 | `65.108.205.251` | 22 | 3.0% | Finland / Uusimaa / Helsinki / Hetzner Online GmbH | Hosting/Cloud (hetzner) |
| 9 | `85.217.149.51` | 20 | 2.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 10 | `185.129.249.130` | 16 | 2.2% | Spain / Valencia / Paterna / AXARNET COMUNICACIONES, S.L | No apparent signal |
| 11 | `192.168.100.118` | 15 | 2.0% | private | Private/CGNAT |
| 12 | `61.220.189.187` | 15 | 2.0% | Taiwan / New Taipei City / New Taipei City / Chunghwa Telecom Co. Ltd. | No apparent signal |
| 13 | `85.217.149.47` | 14 | 1.9% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 14 | `85.217.149.34` | 14 | 1.9% | United States / New York / New York / Modat B.V | No apparent signal |
| 15 | `2.23.164.172` | 14 | 1.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `108.61.215.49` | 264 | 60.0% | Hosting/Cloud (vultr) | United States / Georgia / Atlanta / Vultr Holdings, LLC |
| 2 | `45.77.219.186` | 101 | 23.0% | Hosting/Cloud (vultr) | United States / New Jersey / Piscataway / Vultr Holdings, LLC |
| 3 | `198.27.76.181` | 39 | 8.9% | Hosting/Cloud (ovh) | Canada / Quebec / Montreal / OVH Hosting, Inc. |
| 4 | `65.108.205.251` | 22 | 5.0% | Hosting/Cloud (hetzner) | Finland / Uusimaa / Helsinki / Hetzner Online GmbH |
| 5 | `2.23.164.172` | 14 | 3.2% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
