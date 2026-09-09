# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4356
- Unique source IPs: 2487
- Unique countries/cities (24h): 355
- Unique destination ports: 2676

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 198 | 4.5% |
| 2 | `22` | 60 | 1.4% |
| 3 | `1433` | 37 | 0.8% |
| 4 | `53` | 37 | 0.8% |
| 5 | `8080` | 26 | 0.6% |
| 6 | `5060` | 21 | 0.5% |
| 7 | `3389` | 20 | 0.5% |
| 8 | `2222` | 16 | 0.4% |
| 9 | `3306` | 16 | 0.4% |
| 10 | `8443` | 15 | 0.3% |
| 11 | `5432` | 15 | 0.3% |
| 12 | `161` | 14 | 0.3% |
| 13 | `9200` | 14 | 0.3% |
| 14 | `8088` | 14 | 0.3% |
| 15 | `1900` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3949 | 90.7% |
| 2 | `UDP` | 396 | 9.1% |
| 3 | `47` | 11 | 0.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23.94.28.170` | 141 | 3.2% |
| 2 | `34.47.178.181` | 57 | 1.3% |
| 3 | `103.78.166.108` | 56 | 1.3% |
| 4 | `184.67.58.230` | 55 | 1.3% |
| 5 | `34.64.142.188` | 26 | 0.6% |
| 6 | `151.101.218.13` | 24 | 0.6% |
| 7 | `34.175.134.60` | 23 | 0.5% |
| 8 | `34.158.17.209` | 23 | 0.5% |
| 9 | `204.76.203.7` | 22 | 0.5% |
| 10 | `208.109.212.211` | 17 | 0.4% |
| 11 | `50.116.26.4` | 16 | 0.4% |
| 12 | `85.217.140.34` | 14 | 0.3% |
| 13 | `45.135.193.159` | 14 | 0.3% |
| 14 | `85.217.140.30` | 13 | 0.3% |
| 15 | `34.228.104.231` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3893 | 98.6% |
| 2 | `ACK+FIN+PSH` | 31 | 0.8% |
| 3 | `ACK+PSH` | 15 | 0.4% |
| 4 | `SYN+ECE+CWR` | 6 | 0.2% |
| 5 | `ACK+FIN` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4356 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `208.109.212.211` -> `23` | 17 | 0.4% |
| 2 | `151.101.218.13` -> `62418` | 7 | 0.2% |
| 3 | `151.101.218.13` -> `17895` | 6 | 0.1% |
| 4 | `2.23.164.82` -> `61520` | 5 | 0.1% |
| 5 | `77.239.124.127` -> `2323` | 5 | 0.1% |
| 6 | `69.17.52.1` -> `8333` | 5 | 0.1% |
| 7 | `151.101.218.13` -> `62607` | 5 | 0.1% |
| 8 | `186.123.1.125` -> `1433` | 5 | 0.1% |
| 9 | `178.20.210.152` -> `1723` | 4 | 0.1% |
| 10 | `162.217.103.70` -> `5060` | 4 | 0.1% |
| 11 | `95.100.88.49` -> `17915` | 4 | 0.1% |
| 12 | `66.132.195.90` -> `2000` | 4 | 0.1% |
| 13 | `66.132.172.143` -> `53` | 4 | 0.1% |
| 14 | `94.154.43.195` -> `37215` | 3 | 0.1% |
| 15 | `151.243.11.240` -> `389` | 3 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-08 04:00:00:00 | 135 | 3.1% |
| 2026-09-08 05:00:00:00 | 183 | 4.2% |
| 2026-09-08 06:00:00:00 | 184 | 4.2% |
| 2026-09-08 07:00:00:00 | 178 | 4.1% |
| 2026-09-08 08:00:00:00 | 182 | 4.2% |
| 2026-09-08 09:00:00:00 | 180 | 4.1% |
| 2026-09-08 10:00:00:00 | 179 | 4.1% |
| 2026-09-08 11:00:00:00 | 180 | 4.1% |
| 2026-09-08 12:00:00:00 | 180 | 4.1% |
| 2026-09-08 13:00:00:00 | 180 | 4.1% |
| 2026-09-08 14:00:00:00 | 193 | 4.4% |
| 2026-09-08 15:00:00:00 | 180 | 4.1% |
| 2026-09-08 16:00:00:00 | 195 | 4.5% |
| 2026-09-08 17:00:00:00 | 181 | 4.2% |
| 2026-09-08 18:00:00:00 | 180 | 4.1% |
| 2026-09-08 19:00:00:00 | 179 | 4.1% |
| 2026-09-08 20:00:00:00 | 182 | 4.2% |
| 2026-09-08 21:00:00:00 | 180 | 4.1% |
| 2026-09-08 22:00:00:00 | 179 | 4.1% |
| 2026-09-08 23:00:00:00 | 180 | 4.1% |
| 2026-09-09 00:00:00:00 | 181 | 4.2% |
| 2026-09-09 01:00:00:00 | 179 | 4.1% |
| 2026-09-09 02:00:00:00 | 177 | 4.1% |
| 2026-09-09 03:00:00:00 | 184 | 4.2% |
| 2026-09-09 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Buffalo, United States | 141 | 27.4% |
| 2 | Mumbai, India | 57 | 11.1% |
| 3 | Puducherry, India | 56 | 10.9% |
| 4 | Edmonton, Canada | 55 | 10.7% |
| 5 | Gravelines, France | 27 | 5.3% |
| 6 | Seoul, South Korea | 26 | 5.1% |
| 7 | Buenos Aires, Argentina | 24 | 4.7% |
| 8 | Madrid, Spain | 23 | 4.5% |
| 9 | Zurich, Switzerland | 23 | 4.5% |
| 10 | Eygelshoven, The Netherlands | 22 | 4.3% |
| 11 | Tempe, United States | 17 | 3.3% |
| 12 | Richardson, United States | 16 | 3.1% |
| 13 | Langen, Germany | 14 | 2.7% |
| 14 | Ashburn, United States | 13 | 2.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `23.94.28.170` | 141 | 27.4% | United States / New York / Buffalo / Mikhel Francis yap | No apparent signal |
| 2 | `34.47.178.181` | 57 | 11.1% | India / Maharashtra / Mumbai / Google Cloud (asia-south1) | Hosting/Cloud (google cloud) |
| 3 | `103.78.166.108` | 56 | 10.9% | India / Union Territory of Puducherry / Puducherry / C32 Broadband Pvt. Ltd. | No apparent signal |
| 4 | `184.67.58.230` | 55 | 10.7% | Canada / Alberta / Edmonton / Shaw Communications | No apparent signal |
| 5 | `34.64.142.188` | 26 | 5.1% | South Korea / Seoul / Seoul / Google Cloud (asia-northeast3) | Hosting/Cloud (google cloud) |
| 6 | `151.101.218.13` | 24 | 4.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `34.175.134.60` | 23 | 4.5% | Spain / Madrid / Madrid / Google Cloud (europe-southwest1) | Hosting/Cloud (google cloud) |
| 8 | `34.158.17.209` | 23 | 4.5% | Switzerland / Zurich / Zurich / Google Cloud (europe-west6) | Hosting/Cloud (google cloud) |
| 9 | `204.76.203.7` | 22 | 4.3% | The Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 10 | `208.109.212.211` | 17 | 3.3% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 11 | `50.116.26.4` | 16 | 3.1% | United States / Texas / Richardson / Linode | Hosting/Cloud (linode) |
| 12 | `85.217.140.34` | 14 | 2.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `45.135.193.159` | 14 | 2.7% | Germany / Hesse / Langen / Pfcloud UG | No apparent signal |
| 14 | `85.217.140.30` | 13 | 2.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `34.228.104.231` | 13 | 2.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `34.47.178.181` | 57 | 31.3% | Hosting/Cloud (google cloud) | India / Maharashtra / Mumbai / Google Cloud (asia-south1) |
| 2 | `34.64.142.188` | 26 | 14.3% | Hosting/Cloud (google cloud) | South Korea / Seoul / Seoul / Google Cloud (asia-northeast3) |
| 3 | `151.101.218.13` | 24 | 13.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `34.175.134.60` | 23 | 12.6% | Hosting/Cloud (google cloud) | Spain / Madrid / Madrid / Google Cloud (europe-southwest1) |
| 5 | `34.158.17.209` | 23 | 12.6% | Hosting/Cloud (google cloud) | Switzerland / Zurich / Zurich / Google Cloud (europe-west6) |
| 6 | `50.116.26.4` | 16 | 8.8% | Hosting/Cloud (linode) | United States / Texas / Richardson / Linode |
| 7 | `34.228.104.231` | 13 | 7.1% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
