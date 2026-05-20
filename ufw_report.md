# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4415
- Unique source IPs: 2783
- Unique countries/cities (24h): 368
- Unique destination ports: 2560

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `27015` | 114 | 2.6% |
| 2 | `23` | 97 | 2.2% |
| 3 | `22` | 55 | 1.2% |
| 4 | `8080` | 40 | 0.9% |
| 5 | `3389` | 38 | 0.9% |
| 6 | `5060` | 34 | 0.8% |
| 7 | `8081` | 26 | 0.6% |
| 8 | `53` | 22 | 0.5% |
| 9 | `8000` | 21 | 0.5% |
| 10 | `8443` | 21 | 0.5% |
| 11 | `9200` | 19 | 0.4% |
| 12 | `161` | 18 | 0.4% |
| 13 | `9000` | 18 | 0.4% |
| 14 | `2375` | 17 | 0.4% |
| 15 | `25565` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3859 | 87.4% |
| 2 | `UDP` | 544 | 12.3% |
| 3 | `47` | 9 | 0.2% |
| 4 | `4` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `176.65.148.92` | 34 | 0.8% |
| 2 | `151.101.218.73` | 32 | 0.7% |
| 3 | `2.22.149.160` | 22 | 0.5% |
| 4 | `43.228.157.8` | 18 | 0.4% |
| 5 | `113.211.214.98` | 14 | 0.3% |
| 6 | `151.101.218.13` | 14 | 0.3% |
| 7 | `100.28.153.226` | 13 | 0.3% |
| 8 | `51.159.110.167` | 13 | 0.3% |
| 9 | `18.217.208.51` | 12 | 0.3% |
| 10 | `52.20.198.190` | 11 | 0.2% |
| 11 | `18.221.179.104` | 11 | 0.2% |
| 12 | `151.243.11.37` | 11 | 0.2% |
| 13 | `154.0.30.137` | 11 | 0.2% |
| 14 | `18.190.15.50` | 11 | 0.2% |
| 15 | `204.76.203.15` | 11 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3691 | 95.6% |
| 2 | `ACK+FIN+PSH` | 84 | 2.2% |
| 3 | `ACK+PSH` | 59 | 1.5% |
| 4 | `ACK` | 10 | 0.3% |
| 5 | `ACK+FIN` | 9 | 0.2% |
| 6 | `SYN+ECE+CWR` | 6 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4413 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `154.0.30.137` -> `3389` | 11 | 0.2% |
| 2 | `69.17.52.1` -> `8333` | 9 | 0.2% |
| 3 | `151.101.218.13` -> `27296` | 8 | 0.2% |
| 4 | `140.233.190.89` -> `9000` | 7 | 0.2% |
| 5 | `151.101.218.73` -> `25115` | 6 | 0.1% |
| 6 | `2.22.149.160` -> `27133` | 6 | 0.1% |
| 7 | `151.101.218.13` -> `52526` | 6 | 0.1% |
| 8 | `166.62.124.255` -> `23` | 6 | 0.1% |
| 9 | `178.20.210.152` -> `1723` | 5 | 0.1% |
| 10 | `51.159.110.167` -> `25566` | 5 | 0.1% |
| 11 | `51.159.110.167` -> `25565` | 5 | 0.1% |
| 12 | `95.100.44.10` -> `37764` | 5 | 0.1% |
| 13 | `66.132.195.108` -> `4500` | 5 | 0.1% |
| 14 | `151.101.218.73` -> `51330` | 5 | 0.1% |
| 15 | `151.101.218.73` -> `25107` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-19 04:00:00:00 | 132 | 3.0% |
| 2026-05-19 05:00:00:00 | 180 | 4.1% |
| 2026-05-19 06:00:00:00 | 182 | 4.1% |
| 2026-05-19 07:00:00:00 | 173 | 3.9% |
| 2026-05-19 08:00:00:00 | 191 | 4.3% |
| 2026-05-19 09:00:00:00 | 180 | 4.1% |
| 2026-05-19 10:00:00:00 | 179 | 4.1% |
| 2026-05-19 11:00:00:00 | 189 | 4.3% |
| 2026-05-19 12:00:00:00 | 187 | 4.2% |
| 2026-05-19 13:00:00:00 | 184 | 4.2% |
| 2026-05-19 14:00:00:00 | 179 | 4.1% |
| 2026-05-19 15:00:00:00 | 181 | 4.1% |
| 2026-05-19 16:00:00:00 | 181 | 4.1% |
| 2026-05-19 17:00:00:00 | 178 | 4.0% |
| 2026-05-19 18:00:00:00 | 181 | 4.1% |
| 2026-05-19 19:00:00:00 | 187 | 4.2% |
| 2026-05-19 20:00:00:00 | 178 | 4.0% |
| 2026-05-19 21:00:00:00 | 181 | 4.1% |
| 2026-05-19 22:00:00:00 | 222 | 5.0% |
| 2026-05-19 23:00:00:00 | 188 | 4.3% |
| 2026-05-20 00:00:00:00 | 177 | 4.0% |
| 2026-05-20 01:00:00:00 | 199 | 4.5% |
| 2026-05-20 02:00:00:00 | 180 | 4.1% |
| 2026-05-20 03:00:00:00 | 178 | 4.0% |
| 2026-05-20 04:00:00:00 | 48 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Buenos Aires, Argentina | 36 | 15.1% |
| 2 | Eygelshoven, The Netherlands | 34 | 14.3% |
| 3 | Dublin, United States | 34 | 14.3% |
| 4 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 32 | 13.4% |
| 5 | Ashburn, United States | 24 | 10.1% |
| 6 | Singapore, Singapore | 18 | 7.6% |
| 7 | Puchong, Malaysia | 14 | 5.9% |
| 8 | Paris, France | 13 | 5.5% |
| 9 | Frankfurt am Main, Germany | 11 | 4.6% |
| 10 | Abidjan, Ivory Coast | 11 | 4.6% |
| 11 | Eygelshoven, Netherlands | 11 | 4.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `176.65.148.92` | 34 | 14.3% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 2 | `151.101.218.73` | 32 | 13.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `2.22.149.160` | 22 | 9.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 4 | `43.228.157.8` | 18 | 7.6% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 5 | `113.211.214.98` | 14 | 5.9% | Malaysia / Selangor / Puchong / Maxis Broadband Sdn.Bhd | No apparent signal |
| 6 | `151.101.218.13` | 14 | 5.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `100.28.153.226` | 13 | 5.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 8 | `51.159.110.167` | 13 | 5.5% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 9 | `18.217.208.51` | 12 | 5.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `52.20.198.190` | 11 | 4.6% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 11 | `18.221.179.104` | 11 | 4.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `151.243.11.37` | 11 | 4.6% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 13 | `154.0.30.137` | 11 | 4.6% | Ivory Coast / Abidjan Autonomous District / Abidjan / Moov LS Business | No apparent signal |
| 14 | `18.190.15.50` | 11 | 4.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `204.76.203.15` | 11 | 4.6% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.218.73` | 32 | 23.0% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `2.22.149.160` | 22 | 15.8% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `151.101.218.13` | 14 | 10.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `100.28.153.226` | 13 | 9.4% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `51.159.110.167` | 13 | 9.4% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 6 | `18.217.208.51` | 12 | 8.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `52.20.198.190` | 11 | 7.9% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 8 | `18.221.179.104` | 11 | 7.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 9 | `18.190.15.50` | 11 | 7.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
