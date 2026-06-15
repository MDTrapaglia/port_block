# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4443
- Unique source IPs: 2445
- Unique countries/cities (24h): 444
- Unique destination ports: 1561

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1819 | 40.9% |
| 2 | `unknown` | 78 | 1.8% |
| 3 | `8080` | 38 | 0.9% |
| 4 | `22` | 29 | 0.7% |
| 5 | `27015` | 24 | 0.5% |
| 6 | `3389` | 22 | 0.5% |
| 7 | `8443` | 20 | 0.5% |
| 8 | `5060` | 18 | 0.4% |
| 9 | `1433` | 16 | 0.4% |
| 10 | `6379` | 15 | 0.3% |
| 11 | `81` | 12 | 0.3% |
| 12 | `2222` | 12 | 0.3% |
| 13 | `53` | 12 | 0.3% |
| 14 | `9200` | 11 | 0.2% |
| 15 | `8090` | 11 | 0.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4078 | 91.8% |
| 2 | `UDP` | 287 | 6.5% |
| 3 | `47` | 77 | 1.7% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `84.16.231.135` | 106 | 2.4% |
| 2 | `88.227.183.162` | 86 | 1.9% |
| 3 | `177.66.96.220` | 69 | 1.6% |
| 4 | `59.174.119.183` | 60 | 1.4% |
| 5 | `119.5.205.202` | 52 | 1.2% |
| 6 | `46.98.126.205` | 48 | 1.1% |
| 7 | `114.138.99.209` | 47 | 1.1% |
| 8 | `119.163.171.86` | 44 | 1.0% |
| 9 | `27.223.137.15` | 42 | 0.9% |
| 10 | `91.149.56.207` | 41 | 0.9% |
| 11 | `216.180.246.213` | 40 | 0.9% |
| 12 | `46.236.65.80` | 36 | 0.8% |
| 13 | `122.96.50.102` | 34 | 0.8% |
| 14 | `122.97.137.217` | 30 | 0.7% |
| 15 | `58.47.122.80` | 28 | 0.6% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3930 | 96.4% |
| 2 | `ACK+FIN+PSH` | 91 | 2.2% |
| 3 | `ACK+PSH` | 23 | 0.6% |
| 4 | `ACK+FIN` | 15 | 0.4% |
| 5 | `ACK+RST` | 10 | 0.2% |
| 6 | `SYN+ECE+CWR` | 5 | 0.1% |
| 7 | `ACK` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4435 | 99.8% |
| 2 | `wlan0` | 8 | 0.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `84.16.231.135` -> `23` | 106 | 2.4% |
| 2 | `88.227.183.162` -> `23` | 86 | 1.9% |
| 3 | `177.66.96.220` -> `23` | 69 | 1.6% |
| 4 | `59.174.119.183` -> `23` | 60 | 1.4% |
| 5 | `119.5.205.202` -> `23` | 52 | 1.2% |
| 6 | `46.98.126.205` -> `23` | 48 | 1.1% |
| 7 | `114.138.99.209` -> `23` | 47 | 1.1% |
| 8 | `119.163.171.86` -> `23` | 44 | 1.0% |
| 9 | `27.223.137.15` -> `23` | 42 | 0.9% |
| 10 | `91.149.56.207` -> `23` | 41 | 0.9% |
| 11 | `46.236.65.80` -> `23` | 36 | 0.8% |
| 12 | `122.96.50.102` -> `23` | 34 | 0.8% |
| 13 | `122.97.137.217` -> `23` | 30 | 0.7% |
| 14 | `58.47.122.80` -> `23` | 28 | 0.6% |
| 15 | `5.237.102.98` -> `23` | 27 | 0.6% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-14 04:00:00:00 | 134 | 3.0% |
| 2026-06-14 05:00:00:00 | 179 | 4.0% |
| 2026-06-14 06:00:00:00 | 183 | 4.1% |
| 2026-06-14 07:00:00:00 | 180 | 4.1% |
| 2026-06-14 08:00:00:00 | 180 | 4.1% |
| 2026-06-14 09:00:00:00 | 180 | 4.1% |
| 2026-06-14 10:00:00:00 | 182 | 4.1% |
| 2026-06-14 11:00:00:00 | 203 | 4.6% |
| 2026-06-14 12:00:00:00 | 204 | 4.6% |
| 2026-06-14 13:00:00:00 | 179 | 4.0% |
| 2026-06-14 14:00:00:00 | 183 | 4.1% |
| 2026-06-14 15:00:00:00 | 189 | 4.3% |
| 2026-06-14 16:00:00:00 | 180 | 4.1% |
| 2026-06-14 17:00:00:00 | 191 | 4.3% |
| 2026-06-14 18:00:00:00 | 180 | 4.1% |
| 2026-06-14 19:00:00:00 | 211 | 4.7% |
| 2026-06-14 20:00:00:00 | 180 | 4.1% |
| 2026-06-14 21:00:00:00 | 181 | 4.1% |
| 2026-06-14 22:00:00:00 | 180 | 4.1% |
| 2026-06-14 23:00:00:00 | 180 | 4.1% |
| 2026-06-15 00:00:00:00 | 180 | 4.1% |
| 2026-06-15 01:00:00:00 | 180 | 4.1% |
| 2026-06-15 02:00:00:00 | 181 | 4.1% |
| 2026-06-15 03:00:00:00 | 197 | 4.4% |
| 2026-06-15 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Frankfurt am Main, Germany | 106 | 13.9% |
| 2 | Istanbul, Türkiye | 86 | 11.3% |
| 3 | Macaparana, Brazil | 69 | 9.0% |
| 4 | Shizishan, China | 60 | 7.9% |
| 5 | Chengdu, China | 52 | 6.8% |
| 6 | Dnipro, Ukraine | 48 | 6.3% |
| 7 | Guiyang, China | 47 | 6.2% |
| 8 | Jinan, China | 44 | 5.8% |
| 9 | Qingdao, China | 42 | 5.5% |
| 10 | Fjerdingby, Norway | 41 | 5.4% |
| 11 | Massy, France | 40 | 5.2% |
| 12 | Umeå, Sweden | 36 | 4.7% |
| 13 | Shanghai, China | 34 | 4.5% |
| 14 | Tangquan, China | 30 | 3.9% |
| 15 | Qingyuan, China | 28 | 3.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `84.16.231.135` | 106 | 13.9% | Germany / Hesse / Frankfurt am Main / Leaseweb Deutschland GmbH | Hosting/Cloud (leaseweb) |
| 2 | `88.227.183.162` | 86 | 11.3% | Türkiye / Istanbul / Istanbul / TurkTelecom | No apparent signal |
| 3 | `177.66.96.220` | 69 | 9.0% | Brazil / Pernambuco / Macaparana / Saulo J. de Moura Borba ME | No apparent signal |
| 4 | `59.174.119.183` | 60 | 7.9% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 5 | `119.5.205.202` | 52 | 6.8% | China / Sichuan / Chengdu / CNC Group CHINA169 Sichuan Province Network | No apparent signal |
| 6 | `46.98.126.205` | 48 | 6.3% | Ukraine / Dnipropetrovsk Oblast / Dnipro / ISP "Fregat" | No apparent signal |
| 7 | `114.138.99.209` | 47 | 6.2% | China / Guizhou / Guiyang / Chinanet GZ | No apparent signal |
| 8 | `119.163.171.86` | 44 | 5.8% | China / Shandong / Jinan / CNC Group CHINA169 Shandong Province Network | No apparent signal |
| 9 | `27.223.137.15` | 42 | 5.5% | China / Shandong / Qingdao / China Unicom Shandong Province Network | No apparent signal |
| 10 | `91.149.56.207` | 41 | 5.4% | Norway / Akershus / Fjerdingby / Ice Communication Norge | No apparent signal |
| 11 | `216.180.246.213` | 40 | 5.2% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 12 | `46.236.65.80` | 36 | 4.7% | Sweden / Västerbotten County / Umeå / Bredband2 | No apparent signal |
| 13 | `122.96.50.102` | 34 | 4.5% | China / Shanghai / Shanghai / CNC Group CHINA169 Jiangsu Province Network | No apparent signal |
| 14 | `122.97.137.217` | 30 | 3.9% | China / Jiangsu / Tangquan / CNC Group CHINA169 Jiangsu Province Network | No apparent signal |
| 15 | `58.47.122.80` | 28 | 3.7% | China / Hunan / Qingyuan / Chinanet HN | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `84.16.231.135` | 106 | 72.6% | Hosting/Cloud (leaseweb) | Germany / Hesse / Frankfurt am Main / Leaseweb Deutschland GmbH |
| 2 | `216.180.246.213` | 40 | 27.4% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
