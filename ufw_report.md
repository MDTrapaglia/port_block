# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4363
- Unique source IPs: 2679
- Unique countries/cities (24h): 331
- Unique destination ports: 2603

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 178 | 4.1% |
| 2 | `22` | 51 | 1.2% |
| 3 | `27015` | 49 | 1.1% |
| 4 | `1433` | 29 | 0.7% |
| 5 | `5060` | 27 | 0.6% |
| 6 | `3389` | 26 | 0.6% |
| 7 | `8080` | 25 | 0.6% |
| 8 | `8081` | 24 | 0.6% |
| 9 | `8443` | 24 | 0.6% |
| 10 | `2222` | 23 | 0.5% |
| 11 | `3306` | 22 | 0.5% |
| 12 | `8888` | 20 | 0.5% |
| 13 | `53` | 18 | 0.4% |
| 14 | `88` | 17 | 0.4% |
| 15 | `8000` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3906 | 89.5% |
| 2 | `UDP` | 444 | 10.2% |
| 3 | `47` | 11 | 0.3% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `103.153.182.184` | 71 | 1.6% |
| 2 | `204.76.203.51` | 34 | 0.8% |
| 3 | `45.38.190.201` | 33 | 0.8% |
| 4 | `72.167.43.61` | 30 | 0.7% |
| 5 | `5.39.32.198` | 21 | 0.5% |
| 6 | `118.123.1.36` | 16 | 0.4% |
| 7 | `18.119.209.50` | 13 | 0.3% |
| 8 | `151.80.77.244` | 13 | 0.3% |
| 9 | `151.243.11.37` | 11 | 0.3% |
| 10 | `18.189.74.1` | 11 | 0.3% |
| 11 | `3.142.170.60` | 11 | 0.3% |
| 12 | `3.131.24.55` | 11 | 0.3% |
| 13 | `204.76.203.15` | 11 | 0.3% |
| 14 | `51.159.110.167` | 10 | 0.2% |
| 15 | `45.148.10.121` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3827 | 98.0% |
| 2 | `ACK+FIN+PSH` | 38 | 1.0% |
| 3 | `ACK+PSH` | 28 | 0.7% |
| 4 | `SYN+ECE+CWR` | 5 | 0.1% |
| 5 | `ACK` | 4 | 0.1% |
| 6 | `ACK+FIN` | 3 | 0.1% |
| 7 | `RST` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4363 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `103.153.182.184` -> `23` | 71 | 1.6% |
| 2 | `72.167.43.61` -> `23` | 30 | 0.7% |
| 3 | `24.199.88.4` -> `23` | 9 | 0.2% |
| 4 | `69.17.52.1` -> `8333` | 8 | 0.2% |
| 5 | `5.61.209.43` -> `8080` | 8 | 0.2% |
| 6 | `31.13.94.14` -> `61900` | 7 | 0.2% |
| 7 | `192.241.179.233` -> `23` | 6 | 0.1% |
| 8 | `66.132.172.136` -> `8443` | 6 | 0.1% |
| 9 | `151.101.218.13` -> `63552` | 6 | 0.1% |
| 10 | `45.205.1.68` -> `2011` | 5 | 0.1% |
| 11 | `64.34.84.39` -> `8088` | 5 | 0.1% |
| 12 | `173.208.51.67` -> `22` | 5 | 0.1% |
| 13 | `51.159.110.167` -> `25565` | 4 | 0.1% |
| 14 | `51.159.110.167` -> `25566` | 4 | 0.1% |
| 15 | `3.163.139.38` -> `64140` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-11 04:00:00:00 | 134 | 3.1% |
| 2026-06-11 05:00:00:00 | 181 | 4.1% |
| 2026-06-11 06:00:00:00 | 179 | 4.1% |
| 2026-06-11 07:00:00:00 | 180 | 4.1% |
| 2026-06-11 08:00:00:00 | 181 | 4.1% |
| 2026-06-11 09:00:00:00 | 178 | 4.1% |
| 2026-06-11 10:00:00:00 | 181 | 4.1% |
| 2026-06-11 11:00:00:00 | 178 | 4.1% |
| 2026-06-11 12:00:00:00 | 182 | 4.2% |
| 2026-06-11 13:00:00:00 | 179 | 4.1% |
| 2026-06-11 14:00:00:00 | 181 | 4.1% |
| 2026-06-11 15:00:00:00 | 181 | 4.1% |
| 2026-06-11 16:00:00:00 | 201 | 4.6% |
| 2026-06-11 17:00:00:00 | 179 | 4.1% |
| 2026-06-11 18:00:00:00 | 182 | 4.2% |
| 2026-06-11 19:00:00:00 | 179 | 4.1% |
| 2026-06-11 20:00:00:00 | 180 | 4.1% |
| 2026-06-11 21:00:00:00 | 178 | 4.1% |
| 2026-06-11 22:00:00:00 | 183 | 4.2% |
| 2026-06-11 23:00:00:00 | 179 | 4.1% |
| 2026-06-12 00:00:00:00 | 183 | 4.2% |
| 2026-06-12 01:00:00:00 | 198 | 4.5% |
| 2026-06-12 02:00:00:00 | 180 | 4.1% |
| 2026-06-12 03:00:00:00 | 179 | 4.1% |
| 2026-06-12 04:00:00:00 | 47 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Dallas, United States | 71 | 23.2% |
| 2 | Dublin, United States | 46 | 15.0% |
| 3 | Eygelshoven, Netherlands | 45 | 14.7% |
| 4 | Limburg, Germany | 33 | 10.8% |
| 5 | Paris, France | 31 | 10.1% |
| 6 | Tempe, United States | 30 | 9.8% |
| 7 | Chengdu, China | 16 | 5.2% |
| 8 | Roubaix, France | 13 | 4.2% |
| 9 | Frankfurt am Main, Germany | 11 | 3.6% |
| 10 | Amsterdam, The Netherlands | 10 | 3.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `103.153.182.184` | 71 | 23.2% | United States / Texas / Dallas / Harsh Jain | No apparent signal |
| 2 | `204.76.203.51` | 34 | 11.1% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 3 | `45.38.190.201` | 33 | 10.8% | Germany / Hesse / Limburg / Digital LLC | No apparent signal |
| 4 | `72.167.43.61` | 30 | 9.8% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 5 | `5.39.32.198` | 21 | 6.9% | France / Île-de-France / Paris / Dong Hongyan | Hosting/Cloud (ovh) |
| 6 | `118.123.1.36` | 16 | 5.2% | China / Sichuan / Chengdu / SC MY Lanxun Tech Corp | No apparent signal |
| 7 | `18.119.209.50` | 13 | 4.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 8 | `151.80.77.244` | 13 | 4.2% | France / Hauts-de-France / Roubaix / Mizban Web Paytakht | Hosting/Cloud (ovh) |
| 9 | `151.243.11.37` | 11 | 3.6% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 10 | `18.189.74.1` | 11 | 3.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `3.142.170.60` | 11 | 3.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `3.131.24.55` | 11 | 3.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `204.76.203.15` | 11 | 3.6% | Netherlands / Limburg / Eygelshoven / Intelligence Hosting LLC | No apparent signal |
| 14 | `51.159.110.167` | 10 | 3.3% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 15 | `45.148.10.121` | 10 | 3.3% | The Netherlands / North Holland / Amsterdam / Techoff SRV Limited | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `5.39.32.198` | 21 | 23.3% | Hosting/Cloud (ovh) | France / Île-de-France / Paris / Dong Hongyan |
| 2 | `18.119.209.50` | 13 | 14.4% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `151.80.77.244` | 13 | 14.4% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / Mizban Web Paytakht |
| 4 | `18.189.74.1` | 11 | 12.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `3.142.170.60` | 11 | 12.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `3.131.24.55` | 11 | 12.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `51.159.110.167` | 10 | 11.1% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
