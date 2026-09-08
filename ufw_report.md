# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4365
- Unique source IPs: 2587
- Unique countries/cities (24h): 372
- Unique destination ports: 2697

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 215 | 4.9% |
| 2 | `22` | 76 | 1.7% |
| 3 | `8080` | 35 | 0.8% |
| 4 | `53` | 29 | 0.7% |
| 5 | `5060` | 28 | 0.6% |
| 6 | `3389` | 26 | 0.6% |
| 7 | `2222` | 22 | 0.5% |
| 8 | `8443` | 22 | 0.5% |
| 9 | `161` | 21 | 0.5% |
| 10 | `1433` | 20 | 0.5% |
| 11 | `123` | 18 | 0.4% |
| 12 | `3306` | 18 | 0.4% |
| 13 | `8081` | 15 | 0.3% |
| 14 | `1900` | 14 | 0.3% |
| 15 | `143` | 12 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3982 | 91.2% |
| 2 | `UDP` | 373 | 8.5% |
| 3 | `47` | 9 | 0.2% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `213.21.253.154` | 90 | 2.1% |
| 2 | `23.17.98.160` | 54 | 1.2% |
| 3 | `150.107.36.82` | 43 | 1.0% |
| 4 | `34.91.30.173` | 26 | 0.6% |
| 5 | `104.197.97.140` | 24 | 0.5% |
| 6 | `34.150.56.13` | 22 | 0.5% |
| 7 | `85.217.140.33` | 15 | 0.3% |
| 8 | `85.217.140.22` | 14 | 0.3% |
| 9 | `85.217.140.19` | 14 | 0.3% |
| 10 | `151.243.11.240` | 14 | 0.3% |
| 11 | `85.217.140.7` | 13 | 0.3% |
| 12 | `85.217.140.6` | 12 | 0.3% |
| 13 | `52.15.153.107` | 12 | 0.3% |
| 14 | `2.22.149.152` | 12 | 0.3% |
| 15 | `151.101.217.91` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3912 | 98.2% |
| 2 | `ACK+FIN+PSH` | 43 | 1.1% |
| 3 | `ACK+PSH` | 20 | 0.5% |
| 4 | `ACK+FIN` | 3 | 0.1% |
| 5 | `SYN+ECE+CWR` | 3 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4365 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `194.193.136.132` -> `23` | 9 | 0.2% |
| 2 | `216.180.246.79` -> `53` | 6 | 0.1% |
| 3 | `151.101.217.91` -> `60036` | 6 | 0.1% |
| 4 | `94.154.43.218` -> `37215` | 5 | 0.1% |
| 5 | `2.22.149.152` -> `59424` | 5 | 0.1% |
| 6 | `2.22.149.152` -> `14315` | 4 | 0.1% |
| 7 | `77.239.124.127` -> `60001` | 4 | 0.1% |
| 8 | `157.230.131.241` -> `2345` | 4 | 0.1% |
| 9 | `109.94.173.183` -> `3389` | 4 | 0.1% |
| 10 | `64.225.45.127` -> `2222` | 4 | 0.1% |
| 11 | `77.239.124.127` -> `2323` | 4 | 0.1% |
| 12 | `8.233.134.81` -> `15187` | 4 | 0.1% |
| 13 | `66.132.195.109` -> `8443` | 4 | 0.1% |
| 14 | `2.22.149.179` -> `16085` | 4 | 0.1% |
| 15 | `187.190.15.168` -> `8080` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-07 04:00:00:00 | 133 | 3.0% |
| 2026-09-07 05:00:00:00 | 193 | 4.4% |
| 2026-09-07 06:00:00:00 | 181 | 4.1% |
| 2026-09-07 07:00:00:00 | 179 | 4.1% |
| 2026-09-07 08:00:00:00 | 190 | 4.4% |
| 2026-09-07 09:00:00:00 | 182 | 4.2% |
| 2026-09-07 10:00:00:00 | 178 | 4.1% |
| 2026-09-07 11:00:00:00 | 182 | 4.2% |
| 2026-09-07 12:00:00:00 | 191 | 4.4% |
| 2026-09-07 13:00:00:00 | 179 | 4.1% |
| 2026-09-07 14:00:00:00 | 180 | 4.1% |
| 2026-09-07 15:00:00:00 | 181 | 4.1% |
| 2026-09-07 16:00:00:00 | 180 | 4.1% |
| 2026-09-07 17:00:00:00 | 180 | 4.1% |
| 2026-09-07 18:00:00:00 | 181 | 4.1% |
| 2026-09-07 19:00:00:00 | 180 | 4.1% |
| 2026-09-07 20:00:00:00 | 179 | 4.1% |
| 2026-09-07 21:00:00:00 | 180 | 4.1% |
| 2026-09-07 22:00:00:00 | 181 | 4.1% |
| 2026-09-07 23:00:00:00 | 190 | 4.4% |
| 2026-09-08 00:00:00:00 | 179 | 4.1% |
| 2026-09-08 01:00:00:00 | 181 | 4.1% |
| 2026-09-08 02:00:00:00 | 181 | 4.1% |
| 2026-09-08 03:00:00:00 | 180 | 4.1% |
| 2026-09-08 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Frankfurt am Main, Germany | 104 | 27.6% |
| 2 | Gravelines, France | 68 | 18.0% |
| 3 | Edmonton, Canada | 54 | 14.3% |
| 4 | Los Angeles, United States | 43 | 11.4% |
| 5 | Groningen, Netherlands | 26 | 6.9% |
| 6 | Council Bluffs, United States | 24 | 6.4% |
| 7 | Buenos Aires, Argentina | 24 | 6.4% |
| 8 | Hong Kong, Hong Kong | 22 | 5.8% |
| 9 | Columbus, United States | 12 | 3.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `213.21.253.154` | 90 | 23.9% | Germany / Hesse / Frankfurt am Main / Xorek.Cloud Frankfurt | No apparent signal |
| 2 | `23.17.98.160` | 54 | 14.3% | Canada / Alberta / Edmonton / TELUS-HSIA-EDTNABXT | No apparent signal |
| 3 | `150.107.36.82` | 43 | 11.4% | United States / California / Los Angeles / Ucloud Information Technology (hk) Limited | No apparent signal |
| 4 | `34.91.30.173` | 26 | 6.9% | Netherlands / Groningen / Groningen / Google Cloud (europe-west4) | Hosting/Cloud (google cloud) |
| 5 | `104.197.97.140` | 24 | 6.4% | United States / Iowa / Council Bluffs / Google Cloud (us-central1) | Hosting/Cloud (google cloud) |
| 6 | `34.150.56.13` | 22 | 5.8% | Hong Kong / Central and Western District / Hong Kong / Google Cloud (asia-east2) | Hosting/Cloud (google cloud) |
| 7 | `85.217.140.33` | 15 | 4.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.22` | 14 | 3.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.19` | 14 | 3.7% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `151.243.11.240` | 14 | 3.7% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 11 | `85.217.140.7` | 13 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.6` | 12 | 3.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `52.15.153.107` | 12 | 3.2% | United States / Ohio / Columbus / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `2.22.149.152` | 12 | 3.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 15 | `151.101.217.91` | 12 | 3.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `34.91.30.173` | 26 | 24.1% | Hosting/Cloud (google cloud) | Netherlands / Groningen / Groningen / Google Cloud (europe-west4) |
| 2 | `104.197.97.140` | 24 | 22.2% | Hosting/Cloud (google cloud) | United States / Iowa / Council Bluffs / Google Cloud (us-central1) |
| 3 | `34.150.56.13` | 22 | 20.4% | Hosting/Cloud (google cloud) | Hong Kong / Central and Western District / Hong Kong / Google Cloud (asia-east2) |
| 4 | `52.15.153.107` | 12 | 11.1% | Hosting/Cloud (aws) | United States / Ohio / Columbus / AWS EC2 (us-east-2) |
| 5 | `2.22.149.152` | 12 | 11.1% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 6 | `151.101.217.91` | 12 | 11.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
