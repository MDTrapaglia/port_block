# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4353
- Unique source IPs: 2182
- Unique countries/cities (24h): 339
- Unique destination ports: 2328

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 445 | 10.2% |
| 2 | `5555` | 42 | 1.0% |
| 3 | `5060` | 40 | 0.9% |
| 4 | `22` | 40 | 0.9% |
| 5 | `8080` | 30 | 0.7% |
| 6 | `8081` | 21 | 0.5% |
| 7 | `3389` | 20 | 0.5% |
| 8 | `21` | 20 | 0.5% |
| 9 | `53` | 19 | 0.4% |
| 10 | `8888` | 18 | 0.4% |
| 11 | `2222` | 17 | 0.4% |
| 12 | `3306` | 17 | 0.4% |
| 13 | `9000` | 17 | 0.4% |
| 14 | `161` | 16 | 0.4% |
| 15 | `2323` | 14 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3965 | 91.1% |
| 2 | `UDP` | 377 | 8.7% |
| 3 | `47` | 11 | 0.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `160.119.76.54` | 428 | 9.8% |
| 2 | `93.123.109.41` | 231 | 5.3% |
| 3 | `192.65.240.78` | 138 | 3.2% |
| 4 | `46.37.183.253` | 91 | 2.1% |
| 5 | `54.189.34.14` | 51 | 1.2% |
| 6 | `83.147.240.98` | 45 | 1.0% |
| 7 | `217.154.239.196` | 26 | 0.6% |
| 8 | `192.3.27.234` | 26 | 0.6% |
| 9 | `176.65.139.8` | 25 | 0.6% |
| 10 | `151.236.33.96` | 22 | 0.5% |
| 11 | `208.109.212.6` | 20 | 0.5% |
| 12 | `192.168.100.118` | 19 | 0.4% |
| 13 | `91.184.244.40` | 18 | 0.4% |
| 14 | `92.204.138.198` | 16 | 0.4% |
| 15 | `89.248.163.48` | 16 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3887 | 98.0% |
| 2 | `ACK+PSH` | 31 | 0.8% |
| 3 | `ACK+FIN+PSH` | 24 | 0.6% |
| 4 | `ACK` | 8 | 0.2% |
| 5 | `ACK+FIN` | 8 | 0.2% |
| 6 | `SYN+ECE+CWR` | 7 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4345 | 99.8% |
| 2 | `wlan0` | 8 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.65.240.78` -> `23` | 138 | 3.2% |
| 2 | `46.37.183.253` -> `23` | 91 | 2.1% |
| 3 | `176.65.139.8` -> `5555` | 25 | 0.6% |
| 4 | `151.236.33.96` -> `23` | 22 | 0.5% |
| 5 | `208.109.212.6` -> `23` | 20 | 0.5% |
| 6 | `92.204.138.198` -> `23` | 16 | 0.4% |
| 7 | `198.211.109.224` -> `23` | 11 | 0.3% |
| 8 | `69.17.52.1` -> `8333` | 9 | 0.2% |
| 9 | `104.219.41.228` -> `23` | 9 | 0.2% |
| 10 | `104.238.82.127` -> `23` | 7 | 0.2% |
| 11 | `178.20.210.152` -> `8728` | 6 | 0.1% |
| 12 | `151.101.219.52` -> `40694` | 6 | 0.1% |
| 13 | `66.132.195.105` -> `161` | 6 | 0.1% |
| 14 | `51.159.110.167` -> `25565` | 5 | 0.1% |
| 15 | `109.175.107.201` -> `5555` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-10 04:00:00:00 | 134 | 3.1% |
| 2026-05-10 05:00:00:00 | 181 | 4.2% |
| 2026-05-10 06:00:00:00 | 180 | 4.1% |
| 2026-05-10 07:00:00:00 | 180 | 4.1% |
| 2026-05-10 08:00:00:00 | 180 | 4.1% |
| 2026-05-10 09:00:00:00 | 180 | 4.1% |
| 2026-05-10 10:00:00:00 | 180 | 4.1% |
| 2026-05-10 11:00:00:00 | 179 | 4.1% |
| 2026-05-10 12:00:00:00 | 180 | 4.1% |
| 2026-05-10 13:00:00:00 | 178 | 4.1% |
| 2026-05-10 14:00:00:00 | 187 | 4.3% |
| 2026-05-10 15:00:00:00 | 182 | 4.2% |
| 2026-05-10 16:00:00:00 | 181 | 4.2% |
| 2026-05-10 17:00:00:00 | 179 | 4.1% |
| 2026-05-10 18:00:00:00 | 178 | 4.1% |
| 2026-05-10 19:00:00:00 | 185 | 4.2% |
| 2026-05-10 20:00:00:00 | 180 | 4.1% |
| 2026-05-10 21:00:00:00 | 179 | 4.1% |
| 2026-05-10 22:00:00:00 | 179 | 4.1% |
| 2026-05-10 23:00:00:00 | 187 | 4.3% |
| 2026-05-11 00:00:00:00 | 202 | 4.6% |
| 2026-05-11 01:00:00:00 | 177 | 4.1% |
| 2026-05-11 02:00:00:00 | 183 | 4.2% |
| 2026-05-11 03:00:00:00 | 179 | 4.1% |
| 2026-05-11 04:00:00:00 | 43 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 444 | 37.9% |
| 2 | Andorra la Vella, Andorra | 231 | 19.7% |
| 3 | Dallas, United States | 138 | 11.8% |
| 4 | Manchester, United Kingdom | 91 | 7.8% |
| 5 | Portland, United States | 51 | 4.4% |
| 6 | Stanton, United States | 45 | 3.8% |
| 7 | Berlin, Germany | 26 | 2.2% |
| 8 | Buffalo, United States | 26 | 2.2% |
| 9 | Eygelshoven, The Netherlands | 25 | 2.1% |
| 10 | Reading, United Kingdom | 22 | 1.9% |
| 11 | Tempe, United States | 20 | 1.7% |
| 12 | private | 19 | 1.6% |
| 13 | Moscow, Russia | 18 | 1.5% |
| 14 | Warrenton, United States | 16 | 1.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `160.119.76.54` | 428 | 36.5% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |
| 2 | `93.123.109.41` | 231 | 19.7% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 3 | `192.65.240.78` | 138 | 11.8% | United States / Texas / Dallas / As3800 LLC | No apparent signal |
| 4 | `46.37.183.253` | 91 | 7.8% | United Kingdom / England / Manchester / Ukfast Exb33 | No apparent signal |
| 5 | `54.189.34.14` | 51 | 4.4% | United States / Oregon / Portland / AWS EC2 (us-west-2) | Hosting/Cloud (aws) |
| 6 | `83.147.240.98` | 45 | 3.8% | United States / California / Stanton | No apparent signal |
| 7 | `217.154.239.196` | 26 | 2.2% | Germany / State of Berlin / Berlin / IONOS SE | No apparent signal |
| 8 | `192.3.27.234` | 26 | 2.2% | United States / New York / Buffalo / RackNerd LLC | No apparent signal |
| 9 | `176.65.139.8` | 25 | 2.1% | The Netherlands / Limburg / Eygelshoven / Storm Industries | No apparent signal |
| 10 | `151.236.33.96` | 22 | 1.9% | United Kingdom / England / Reading / Simply Transit Ltd | No apparent signal |
| 11 | `208.109.212.6` | 20 | 1.7% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 12 | `192.168.100.118` | 19 | 1.6% | private | Private/CGNAT |
| 13 | `91.184.244.40` | 18 | 1.5% | Russia / Moscow / Moscow / Hosting technology LTD | No apparent signal |
| 14 | `92.204.138.198` | 16 | 1.4% | United States / Virginia / Warrenton / Host Europe GmbH | No apparent signal |
| 15 | `89.248.163.48` | 16 | 1.4% | The Netherlands / North Holland / Amsterdam / Quasi Networks LTD. | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `54.189.34.14` | 51 | 100.0% | Hosting/Cloud (aws) | United States / Oregon / Portland / AWS EC2 (us-west-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
