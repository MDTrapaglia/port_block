# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4339
- Unique source IPs: 2684
- Unique countries/cities (24h): 474
- Unique destination ports: 1915

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1145 | 26.4% |
| 2 | `unknown` | 67 | 1.5% |
| 3 | `27015` | 39 | 0.9% |
| 4 | `22` | 34 | 0.8% |
| 5 | `8080` | 34 | 0.8% |
| 6 | `37215` | 28 | 0.6% |
| 7 | `5555` | 28 | 0.6% |
| 8 | `5060` | 26 | 0.6% |
| 9 | `8443` | 22 | 0.5% |
| 10 | `1433` | 21 | 0.5% |
| 11 | `8888` | 19 | 0.4% |
| 12 | `389` | 18 | 0.4% |
| 13 | `81` | 18 | 0.4% |
| 14 | `8081` | 17 | 0.4% |
| 15 | `3306` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3862 | 89.0% |
| 2 | `UDP` | 410 | 9.4% |
| 3 | `47` | 67 | 1.5% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `175.153.76.168` | 88 | 2.0% |
| 2 | `175.1.190.88` | 85 | 2.0% |
| 3 | `27.24.104.44` | 64 | 1.5% |
| 4 | `43.254.205.48` | 57 | 1.3% |
| 5 | `112.103.130.41` | 54 | 1.2% |
| 6 | `176.65.148.135` | 33 | 0.8% |
| 7 | `84.0.60.153` | 30 | 0.7% |
| 8 | `78.92.227.234` | 28 | 0.6% |
| 9 | `185.74.221.30` | 25 | 0.6% |
| 10 | `93.123.72.183` | 19 | 0.4% |
| 11 | `192.169.226.90` | 16 | 0.4% |
| 12 | `206.189.225.77` | 15 | 0.3% |
| 13 | `147.182.129.34` | 14 | 0.3% |
| 14 | `195.178.110.204` | 13 | 0.3% |
| 15 | `94.156.152.50` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3827 | 99.1% |
| 2 | `ACK+PSH` | 15 | 0.4% |
| 3 | `ACK+FIN+PSH` | 13 | 0.3% |
| 4 | `SYN+ECE+CWR` | 6 | 0.2% |
| 5 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4333 | 99.9% |
| 2 | `wlan0` | 6 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `175.153.76.168` -> `23` | 88 | 2.0% |
| 2 | `175.1.190.88` -> `23` | 85 | 2.0% |
| 3 | `27.24.104.44` -> `23` | 64 | 1.5% |
| 4 | `43.254.205.48` -> `23` | 57 | 1.3% |
| 5 | `112.103.130.41` -> `23` | 54 | 1.2% |
| 6 | `84.0.60.153` -> `23` | 30 | 0.7% |
| 7 | `78.92.227.234` -> `23` | 28 | 0.6% |
| 8 | `192.169.226.90` -> `23` | 16 | 0.4% |
| 9 | `206.189.225.77` -> `23` | 15 | 0.3% |
| 10 | `94.156.152.50` -> `23` | 12 | 0.3% |
| 11 | `81.10.69.33` -> `23` | 11 | 0.3% |
| 12 | `114.226.82.136` -> `23` | 9 | 0.2% |
| 13 | `176.65.139.220` -> `389` | 9 | 0.2% |
| 14 | `222.246.42.129` -> `23` | 8 | 0.2% |
| 15 | `69.17.52.1` -> `8333` | 8 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-17 04:00:00:00 | 135 | 3.1% |
| 2026-06-17 05:00:00:00 | 180 | 4.1% |
| 2026-06-17 06:00:00:00 | 181 | 4.2% |
| 2026-06-17 07:00:00:00 | 181 | 4.2% |
| 2026-06-17 08:00:00:00 | 180 | 4.1% |
| 2026-06-17 09:00:00:00 | 180 | 4.1% |
| 2026-06-17 10:00:00:00 | 180 | 4.1% |
| 2026-06-17 11:00:00:00 | 179 | 4.1% |
| 2026-06-17 12:00:00:00 | 181 | 4.2% |
| 2026-06-17 13:00:00:00 | 178 | 4.1% |
| 2026-06-17 14:00:00:00 | 182 | 4.2% |
| 2026-06-17 15:00:00:00 | 180 | 4.1% |
| 2026-06-17 16:00:00:00 | 180 | 4.1% |
| 2026-06-17 17:00:00:00 | 193 | 4.4% |
| 2026-06-17 18:00:00:00 | 180 | 4.1% |
| 2026-06-17 19:00:00:00 | 180 | 4.1% |
| 2026-06-17 20:00:00:00 | 179 | 4.1% |
| 2026-06-17 21:00:00:00 | 181 | 4.2% |
| 2026-06-17 22:00:00:00 | 182 | 4.2% |
| 2026-06-17 23:00:00:00 | 180 | 4.1% |
| 2026-06-18 00:00:00:00 | 180 | 4.1% |
| 2026-06-18 01:00:00:00 | 179 | 4.1% |
| 2026-06-18 02:00:00:00 | 182 | 4.2% |
| 2026-06-18 03:00:00:00 | 180 | 4.1% |
| 2026-06-18 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Chengdu, China | 88 | 15.9% |
| 2 | Qingyuan, China | 85 | 15.4% |
| 3 | Shizishan, China | 64 | 11.6% |
| 4 | Bilimora, India | 57 | 10.3% |
| 5 | Harbin, China | 54 | 9.8% |
| 6 | Eygelshoven, Netherlands | 33 | 6.0% |
| 7 | Csenger, Hungary | 30 | 5.4% |
| 8 | North Bergen, United States | 29 | 5.2% |
| 9 | Mátészalka, Hungary | 28 | 5.1% |
| 10 | Tehran, Iran | 25 | 4.5% |
| 11 | Amsterdam, Netherlands | 19 | 3.4% |
| 12 | Tempe, United States | 16 | 2.9% |
| 13 | Andorra la Vella, Andorra | 13 | 2.4% |
| 14 | Centurion, South Africa | 12 | 2.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `175.153.76.168` | 88 | 15.9% | China / Sichuan / Chengdu / China Unicom Sichuan Province Network | No apparent signal |
| 2 | `175.1.190.88` | 85 | 15.4% | China / Hunan / Qingyuan / Chinanet HN | No apparent signal |
| 3 | `27.24.104.44` | 64 | 11.6% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 4 | `43.254.205.48` | 57 | 10.3% | India / Gujarat / Bilimora / Digital Network | No apparent signal |
| 5 | `112.103.130.41` | 54 | 9.8% | China / Heilongjiang / Harbin / Chinanet HL | No apparent signal |
| 6 | `176.65.148.135` | 33 | 6.0% | Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 7 | `84.0.60.153` | 30 | 5.4% | Hungary / Szabolcs-Szatmár-Bereg / Csenger / Magyar Telekom | No apparent signal |
| 8 | `78.92.227.234` | 28 | 5.1% | Hungary / Szabolcs-Szatmár-Bereg / Mátészalka / Magyar Telekom | No apparent signal |
| 9 | `185.74.221.30` | 25 | 4.5% | Iran / Tehran / Tehran / Sindad Network Technology PJSC | No apparent signal |
| 10 | `93.123.72.183` | 19 | 3.4% | Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 11 | `192.169.226.90` | 16 | 2.9% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 12 | `206.189.225.77` | 15 | 2.7% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `147.182.129.34` | 14 | 2.5% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 14 | `195.178.110.204` | 13 | 2.4% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 15 | `94.156.152.50` | 12 | 2.2% | South Africa / Gauteng / Centurion / Internet Magnate (Pty) Ltd | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `206.189.225.77` | 15 | 51.7% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 2 | `147.182.129.34` | 14 | 48.3% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
