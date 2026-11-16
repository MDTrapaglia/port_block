# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4396
- Unique source IPs: 2606
- Unique countries/cities (24h): 270
- Unique destination ports: 2252

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 216 | 4.9% |
| 2 | `22` | 79 | 1.8% |
| 3 | `8080` | 52 | 1.2% |
| 4 | `3389` | 37 | 0.8% |
| 5 | `5060` | 32 | 0.7% |
| 6 | `161` | 28 | 0.6% |
| 7 | `53` | 27 | 0.6% |
| 8 | `8081` | 27 | 0.6% |
| 9 | `123` | 26 | 0.6% |
| 10 | `1433` | 26 | 0.6% |
| 11 | `8443` | 23 | 0.5% |
| 12 | `8000` | 22 | 0.5% |
| 13 | `3306` | 21 | 0.5% |
| 14 | `8888` | 19 | 0.4% |
| 15 | `1723` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4017 | 91.4% |
| 2 | `UDP` | 372 | 8.5% |
| 3 | `47` | 4 | 0.1% |
| 4 | `132` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.24` | 199 | 4.5% |
| 2 | `188.132.199.206` | 89 | 2.0% |
| 3 | `77.239.124.252` | 24 | 0.5% |
| 4 | `185.224.128.16` | 15 | 0.3% |
| 5 | `45.198.224.125` | 15 | 0.3% |
| 6 | `45.141.233.67` | 15 | 0.3% |
| 7 | `151.101.218.13` | 15 | 0.3% |
| 8 | `18.217.208.51` | 12 | 0.3% |
| 9 | `34.197.70.90` | 12 | 0.3% |
| 10 | `192.207.105.196` | 11 | 0.3% |
| 11 | `100.28.153.226` | 11 | 0.3% |
| 12 | `2.22.149.155` | 11 | 0.3% |
| 13 | `86.54.31.36` | 10 | 0.2% |
| 14 | `34.228.104.231` | 10 | 0.2% |
| 15 | `91.231.89.69` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3913 | 97.4% |
| 2 | `ACK+FIN+PSH` | 70 | 1.7% |
| 3 | `ACK+PSH` | 26 | 0.6% |
| 4 | `ACK+FIN` | 6 | 0.1% |
| 5 | `ACK` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4396 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `188.132.199.206` -> `23` | 89 | 2.0% |
| 2 | `77.239.124.252` -> `23` | 22 | 0.5% |
| 3 | `216.180.246.24` -> `49200` | 11 | 0.3% |
| 4 | `216.180.246.24` -> `50013` | 10 | 0.2% |
| 5 | `216.180.246.24` -> `49152` | 9 | 0.2% |
| 6 | `216.180.246.24` -> `50010` | 9 | 0.2% |
| 7 | `216.180.246.24` -> `50075` | 9 | 0.2% |
| 8 | `34.160.136.227` -> `51632` | 8 | 0.2% |
| 9 | `216.180.246.24` -> `47001` | 8 | 0.2% |
| 10 | `216.180.246.24` -> `49080` | 8 | 0.2% |
| 11 | `216.180.246.24` -> `49151` | 8 | 0.2% |
| 12 | `216.180.246.24` -> `50001` | 8 | 0.2% |
| 13 | `216.180.246.24` -> `50014` | 8 | 0.2% |
| 14 | `216.180.246.24` -> `50105` | 8 | 0.2% |
| 15 | `45.198.224.125` -> `8081` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-15 04:00:00:00 | 134 | 3.0% |
| 2026-11-15 05:00:00:00 | 180 | 4.1% |
| 2026-11-15 06:00:00:00 | 180 | 4.1% |
| 2026-11-15 07:00:00:00 | 176 | 4.0% |
| 2026-11-15 08:00:00:00 | 185 | 4.2% |
| 2026-11-15 09:00:00:00 | 176 | 4.0% |
| 2026-11-15 10:00:00:00 | 181 | 4.1% |
| 2026-11-15 11:00:00:00 | 182 | 4.1% |
| 2026-11-15 12:00:00:00 | 181 | 4.1% |
| 2026-11-15 13:00:00:00 | 180 | 4.1% |
| 2026-11-15 14:00:00:00 | 196 | 4.5% |
| 2026-11-15 15:00:00:00 | 181 | 4.1% |
| 2026-11-15 16:00:00:00 | 199 | 4.5% |
| 2026-11-15 17:00:00:00 | 197 | 4.5% |
| 2026-11-15 18:00:00:00 | 178 | 4.0% |
| 2026-11-15 19:00:00:00 | 181 | 4.1% |
| 2026-11-15 20:00:00:00 | 180 | 4.1% |
| 2026-11-15 21:00:00:00 | 181 | 4.1% |
| 2026-11-15 22:00:00:00 | 179 | 4.1% |
| 2026-11-15 23:00:00:00 | 181 | 4.1% |
| 2026-11-16 00:00:00:00 | 180 | 4.1% |
| 2026-11-16 01:00:00:00 | 179 | 4.1% |
| 2026-11-16 02:00:00:00 | 203 | 4.6% |
| 2026-11-16 03:00:00:00 | 181 | 4.1% |
| 2026-11-16 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 199 | 43.4% |
| 2 | Osmangazi, Turkey | 89 | 19.4% |
| 3 | Amsterdam, The Netherlands | 49 | 10.7% |
| 4 | Ashburn, United States | 33 | 7.2% |
| 5 | Buenos Aires, Argentina | 26 | 5.7% |
| 6 | Stockholm, Sweden | 15 | 3.3% |
| 7 | London, United Kingdom | 15 | 3.3% |
| 8 | Dublin, United States | 12 | 2.6% |
| 9 | Newburyport, United States | 11 | 2.4% |
| 10 | Gravelines, France | 10 | 2.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.24` | 199 | 43.4% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `188.132.199.206` | 89 | 19.4% | Turkey / Bursa Province / Osmangazi / PENTECH BILISIM TEKNOLOJILERI SANAYI VE TICARET LIMITED SIRKETi | No apparent signal |
| 3 | `77.239.124.252` | 24 | 5.2% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |
| 4 | `185.224.128.16` | 15 | 3.3% | The Netherlands / North Holland / Amsterdam / Alsycon B.V | No apparent signal |
| 5 | `45.198.224.125` | 15 | 3.3% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 6 | `45.141.233.67` | 15 | 3.3% | United Kingdom / England / London / Razinet | No apparent signal |
| 7 | `151.101.218.13` | 15 | 3.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 8 | `18.217.208.51` | 12 | 2.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `34.197.70.90` | 12 | 2.6% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 10 | `192.207.105.196` | 11 | 2.4% | United States / Massachusetts / Newburyport / Searchlight Cyber LLC | Hosting/Cloud (ovh) |
| 11 | `100.28.153.226` | 11 | 2.4% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 12 | `2.22.149.155` | 11 | 2.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 13 | `86.54.31.36` | 10 | 2.2% | The Netherlands / North Holland / Amsterdam / ADSL: Circle IT Solutions Limited | No apparent signal |
| 14 | `34.228.104.231` | 10 | 2.2% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `91.231.89.69` | 10 | 2.2% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.24` | 199 | 70.8% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 15 | 5.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `18.217.208.51` | 12 | 4.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `34.197.70.90` | 12 | 4.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `192.207.105.196` | 11 | 3.9% | Hosting/Cloud (ovh) | United States / Massachusetts / Newburyport / Searchlight Cyber LLC |
| 6 | `100.28.153.226` | 11 | 3.9% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 7 | `2.22.149.155` | 11 | 3.9% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 8 | `34.228.104.231` | 10 | 3.6% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
