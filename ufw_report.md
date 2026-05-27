# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4425
- Unique source IPs: 2432
- Unique countries/cities (24h): 341
- Unique destination ports: 2887

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 116 | 2.6% |
| 2 | `22` | 58 | 1.3% |
| 3 | `27015` | 52 | 1.2% |
| 4 | `3389` | 33 | 0.7% |
| 5 | `5060` | 31 | 0.7% |
| 6 | `8443` | 30 | 0.7% |
| 7 | `53` | 27 | 0.6% |
| 8 | `8080` | 27 | 0.6% |
| 9 | `3306` | 18 | 0.4% |
| 10 | `21` | 17 | 0.4% |
| 11 | `1433` | 17 | 0.4% |
| 12 | `3000` | 17 | 0.4% |
| 13 | `8001` | 16 | 0.4% |
| 14 | `123` | 14 | 0.3% |
| 15 | `8081` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3999 | 90.4% |
| 2 | `UDP` | 421 | 9.5% |
| 3 | `47` | 5 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `194.180.48.25` | 536 | 12.1% |
| 2 | `216.180.246.155` | 32 | 0.7% |
| 3 | `170.51.247.48` | 21 | 0.5% |
| 4 | `104.234.7.50` | 16 | 0.4% |
| 5 | `85.217.149.15` | 16 | 0.4% |
| 6 | `18.221.179.104` | 14 | 0.3% |
| 7 | `18.119.209.50` | 12 | 0.3% |
| 8 | `85.217.149.34` | 12 | 0.3% |
| 9 | `151.101.218.73` | 12 | 0.3% |
| 10 | `23.64.58.60` | 11 | 0.2% |
| 11 | `3.131.24.55` | 10 | 0.2% |
| 12 | `51.159.110.167` | 10 | 0.2% |
| 13 | `18.189.74.1` | 10 | 0.2% |
| 14 | `85.217.149.47` | 10 | 0.2% |
| 15 | `85.217.149.49` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3852 | 96.3% |
| 2 | `ACK+FIN+PSH` | 76 | 1.9% |
| 3 | `ACK+PSH` | 46 | 1.2% |
| 4 | `ACK+FIN` | 20 | 0.5% |
| 5 | `SYN+ECE+CWR` | 5 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4416 | 99.8% |
| 2 | `wlan0` | 9 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `104.238.110.208` -> `23` | 10 | 0.2% |
| 2 | `124.198.131.22` -> `3000` | 9 | 0.2% |
| 3 | `69.17.52.1` -> `8333` | 9 | 0.2% |
| 4 | `192.168.100.1` -> `68` | 9 | 0.2% |
| 5 | `167.94.146.50` -> `8443` | 7 | 0.2% |
| 6 | `216.180.246.155` -> `8001` | 7 | 0.2% |
| 7 | `178.20.210.152` -> `1723` | 6 | 0.1% |
| 8 | `2.23.164.167` -> `63478` | 6 | 0.1% |
| 9 | `216.180.246.155` -> `8443` | 6 | 0.1% |
| 10 | `154.0.30.137` -> `3389` | 5 | 0.1% |
| 11 | `130.12.180.174` -> `23` | 5 | 0.1% |
| 12 | `2.23.164.143` -> `55345` | 5 | 0.1% |
| 13 | `216.180.246.155` -> `34600` | 5 | 0.1% |
| 14 | `139.19.117.130` -> `22` | 4 | 0.1% |
| 15 | `66.132.195.38` -> `2212` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-26 04:00:00:00 | 136 | 3.1% |
| 2026-05-26 05:00:00:00 | 179 | 4.0% |
| 2026-05-26 06:00:00:00 | 181 | 4.1% |
| 2026-05-26 07:00:00:00 | 178 | 4.0% |
| 2026-05-26 08:00:00:00 | 180 | 4.1% |
| 2026-05-26 09:00:00:00 | 181 | 4.1% |
| 2026-05-26 10:00:00:00 | 183 | 4.1% |
| 2026-05-26 11:00:00:00 | 188 | 4.2% |
| 2026-05-26 12:00:00:00 | 182 | 4.1% |
| 2026-05-26 13:00:00:00 | 179 | 4.0% |
| 2026-05-26 14:00:00:00 | 182 | 4.1% |
| 2026-05-26 15:00:00:00 | 193 | 4.4% |
| 2026-05-26 16:00:00:00 | 221 | 5.0% |
| 2026-05-26 17:00:00:00 | 178 | 4.0% |
| 2026-05-26 18:00:00:00 | 195 | 4.4% |
| 2026-05-26 19:00:00:00 | 181 | 4.1% |
| 2026-05-26 20:00:00:00 | 180 | 4.1% |
| 2026-05-26 21:00:00:00 | 179 | 4.0% |
| 2026-05-26 22:00:00:00 | 181 | 4.1% |
| 2026-05-26 23:00:00:00 | 181 | 4.1% |
| 2026-05-27 00:00:00:00 | 180 | 4.1% |
| 2026-05-27 01:00:00:00 | 180 | 4.1% |
| 2026-05-27 02:00:00:00 | 182 | 4.1% |
| 2026-05-27 03:00:00:00 | 200 | 4.5% |
| 2026-05-27 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Berngau, Germany | 536 | 73.2% |
| 2 | Dublin, United States | 46 | 6.3% |
| 3 | Massy, France | 32 | 4.4% |
| 4 | Buenos Aires, Argentina | 32 | 4.4% |
| 5 | New York, United States | 28 | 3.8% |
| 6 | Beauharnois, Canada | 20 | 2.7% |
| 7 | Santiago, Chile | 16 | 2.2% |
| 8 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 12 | 1.6% |
| 9 | Paris, France | 10 | 1.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `194.180.48.25` | 536 | 73.2% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 2 | `216.180.246.155` | 32 | 4.4% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 3 | `170.51.247.48` | 21 | 2.9% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 4 | `104.234.7.50` | 16 | 2.2% | Chile / Santiago Metropolitan / Santiago / Grupo Inan SPA | No apparent signal |
| 5 | `85.217.149.15` | 16 | 2.2% | United States / New York / New York / Modat B.V | No apparent signal |
| 6 | `18.221.179.104` | 14 | 1.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `18.119.209.50` | 12 | 1.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `85.217.149.34` | 12 | 1.6% | United States / New York / New York / Modat B.V | No apparent signal |
| 9 | `151.101.218.73` | 12 | 1.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 10 | `23.64.58.60` | 11 | 1.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. | CDN/Edge (akamai) |
| 11 | `3.131.24.55` | 10 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `51.159.110.167` | 10 | 1.4% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 13 | `18.189.74.1` | 10 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `85.217.149.47` | 10 | 1.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 15 | `85.217.149.49` | 10 | 1.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.155` | 32 | 28.8% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `18.221.179.104` | 14 | 12.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `18.119.209.50` | 12 | 10.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `151.101.218.73` | 12 | 10.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `23.64.58.60` | 11 | 9.9% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. |
| 6 | `3.131.24.55` | 10 | 9.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `51.159.110.167` | 10 | 9.0% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 8 | `18.189.74.1` | 10 | 9.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
