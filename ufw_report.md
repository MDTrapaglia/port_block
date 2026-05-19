# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4318
- Unique source IPs: 2558
- Unique countries/cities (24h): 399
- Unique destination ports: 2296

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 218 | 5.0% |
| 2 | `27015` | 126 | 2.9% |
| 3 | `8080` | 67 | 1.6% |
| 4 | `22` | 48 | 1.1% |
| 5 | `3389` | 30 | 0.7% |
| 6 | `5060` | 29 | 0.7% |
| 7 | `53` | 26 | 0.6% |
| 8 | `25` | 25 | 0.6% |
| 9 | `5555` | 23 | 0.5% |
| 10 | `161` | 23 | 0.5% |
| 11 | `1433` | 22 | 0.5% |
| 12 | `9200` | 22 | 0.5% |
| 13 | `2222` | 20 | 0.5% |
| 14 | `8443` | 20 | 0.5% |
| 15 | `3306` | 20 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3707 | 85.8% |
| 2 | `UDP` | 598 | 13.8% |
| 3 | `47` | 11 | 0.3% |
| 4 | `41` | 2 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.204` | 151 | 3.5% |
| 2 | `146.19.210.8` | 76 | 1.8% |
| 3 | `5.61.209.33` | 25 | 0.6% |
| 4 | `43.228.157.10` | 24 | 0.6% |
| 5 | `43.228.157.9` | 24 | 0.6% |
| 6 | `20.9.36.57` | 22 | 0.5% |
| 7 | `146.19.173.46` | 22 | 0.5% |
| 8 | `185.242.3.226` | 20 | 0.5% |
| 9 | `43.228.157.8` | 17 | 0.4% |
| 10 | `123.139.214.42` | 14 | 0.3% |
| 11 | `176.65.139.188` | 14 | 0.3% |
| 12 | `18.189.74.1` | 13 | 0.3% |
| 13 | `51.159.110.167` | 12 | 0.3% |
| 14 | `52.20.198.190` | 11 | 0.3% |
| 15 | `100.50.17.159` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3664 | 98.8% |
| 2 | `ACK+PSH` | 30 | 0.8% |
| 3 | `SYN+ECE+CWR` | 9 | 0.2% |
| 4 | `ACK` | 3 | 0.1% |
| 5 | `ACK+FIN+PSH` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4316 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `146.19.210.8` -> `23` | 76 | 1.8% |
| 2 | `5.61.209.33` -> `8080` | 25 | 0.6% |
| 3 | `20.9.36.57` -> `23` | 22 | 0.5% |
| 4 | `146.19.173.46` -> `23` | 22 | 0.5% |
| 5 | `123.139.214.42` -> `23` | 14 | 0.3% |
| 6 | `176.65.139.188` -> `5555` | 14 | 0.3% |
| 7 | `216.180.246.204` -> `63345` | 14 | 0.3% |
| 8 | `216.180.246.204` -> `7596` | 10 | 0.2% |
| 9 | `216.180.246.204` -> `10010` | 10 | 0.2% |
| 10 | `216.180.246.204` -> `1200` | 10 | 0.2% |
| 11 | `69.17.52.1` -> `8333` | 9 | 0.2% |
| 12 | `216.180.246.204` -> `1974` | 9 | 0.2% |
| 13 | `216.180.246.204` -> `6550` | 9 | 0.2% |
| 14 | `216.180.246.204` -> `19999` | 9 | 0.2% |
| 15 | `216.180.246.204` -> `6667` | 9 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-18 04:00:00:00 | 135 | 3.1% |
| 2026-05-18 05:00:00:00 | 179 | 4.1% |
| 2026-05-18 06:00:00:00 | 184 | 4.3% |
| 2026-05-18 07:00:00:00 | 179 | 4.1% |
| 2026-05-18 08:00:00:00 | 180 | 4.2% |
| 2026-05-18 09:00:00:00 | 179 | 4.1% |
| 2026-05-18 10:00:00:00 | 179 | 4.1% |
| 2026-05-18 11:00:00:00 | 177 | 4.1% |
| 2026-05-18 12:00:00:00 | 175 | 4.1% |
| 2026-05-18 13:00:00:00 | 184 | 4.3% |
| 2026-05-18 14:00:00:00 | 176 | 4.1% |
| 2026-05-18 15:00:00:00 | 184 | 4.3% |
| 2026-05-18 16:00:00:00 | 181 | 4.2% |
| 2026-05-18 17:00:00:00 | 181 | 4.2% |
| 2026-05-18 18:00:00:00 | 179 | 4.1% |
| 2026-05-18 19:00:00:00 | 181 | 4.2% |
| 2026-05-18 20:00:00:00 | 180 | 4.2% |
| 2026-05-18 21:00:00:00 | 179 | 4.1% |
| 2026-05-18 22:00:00:00 | 182 | 4.2% |
| 2026-05-18 23:00:00:00 | 179 | 4.1% |
| 2026-05-19 00:00:00:00 | 181 | 4.2% |
| 2026-05-19 01:00:00:00 | 179 | 4.1% |
| 2026-05-19 02:00:00:00 | 181 | 4.2% |
| 2026-05-19 03:00:00:00 | 180 | 4.2% |
| 2026-05-19 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 151 | 33.1% |
| 2 | Hegra, Norway | 76 | 16.7% |
| 3 | Singapore, Singapore | 65 | 14.3% |
| 4 | Amsterdam, The Netherlands | 47 | 10.3% |
| 5 | Des Moines, United States | 22 | 4.8% |
| 6 | Ashburn, United States | 22 | 4.8% |
| 7 | Frankfurt am Main, Germany | 20 | 4.4% |
| 8 | Xi'an, China | 14 | 3.1% |
| 9 | Eygelshoven, The Netherlands | 14 | 3.1% |
| 10 | Dublin, United States | 13 | 2.9% |
| 11 | Paris, France | 12 | 2.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.204` | 151 | 33.1% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `146.19.210.8` | 76 | 16.7% | Norway / Trøndelag / Hegra / Qloud | No apparent signal |
| 3 | `5.61.209.33` | 25 | 5.5% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd. Network | No apparent signal |
| 4 | `43.228.157.10` | 24 | 5.3% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 5 | `43.228.157.9` | 24 | 5.3% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 6 | `20.9.36.57` | 22 | 4.8% | United States / Iowa / Des Moines / Microsoft Azure Cloud (centralus) | Hosting/Cloud (azure) |
| 7 | `146.19.173.46` | 22 | 4.8% | The Netherlands / North Holland / Amsterdam / IP Connect Inc | No apparent signal |
| 8 | `185.242.3.226` | 20 | 4.4% | Germany / Hesse / Frankfurt am Main / Felcloud | No apparent signal |
| 9 | `43.228.157.8` | 17 | 3.7% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 10 | `123.139.214.42` | 14 | 3.1% | China / Shaanxi / Xi'an / CNC Group CHINA169 Shanni Province Network | No apparent signal |
| 11 | `176.65.139.188` | 14 | 3.1% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 12 | `18.189.74.1` | 13 | 2.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `51.159.110.167` | 12 | 2.6% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 14 | `52.20.198.190` | 11 | 2.4% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 15 | `100.50.17.159` | 11 | 2.4% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.204` | 151 | 68.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `20.9.36.57` | 22 | 10.0% | Hosting/Cloud (azure) | United States / Iowa / Des Moines / Microsoft Azure Cloud (centralus) |
| 3 | `18.189.74.1` | 13 | 5.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `51.159.110.167` | 12 | 5.5% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 5 | `52.20.198.190` | 11 | 5.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 6 | `100.50.17.159` | 11 | 5.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
