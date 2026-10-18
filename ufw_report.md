# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 680
- Unique source IPs: 480
- Unique countries/cities (24h): 162
- Unique destination ports: 329

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 296 | 43.5% |
| 2 | `22` | 6 | 0.9% |
| 3 | `6666` | 5 | 0.7% |
| 4 | `6699` | 5 | 0.7% |
| 5 | `3306` | 4 | 0.6% |
| 6 | `6789` | 4 | 0.6% |
| 7 | `6667` | 4 | 0.6% |
| 8 | `3389` | 4 | 0.6% |
| 9 | `6697` | 4 | 0.6% |
| 10 | `9443` | 3 | 0.4% |
| 11 | `6036` | 3 | 0.4% |
| 12 | `6677` | 3 | 0.4% |
| 13 | `unknown` | 3 | 0.4% |
| 14 | `123` | 3 | 0.4% |
| 15 | `6700` | 3 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 645 | 94.9% |
| 2 | `UDP` | 32 | 4.7% |
| 3 | `47` | 3 | 0.4% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.98` | 29 | 4.3% |
| 2 | `194.39.243.42` | 26 | 3.8% |
| 3 | `42.243.83.235` | 24 | 3.5% |
| 4 | `27.31.108.165` | 23 | 3.4% |
| 5 | `114.35.195.197` | 11 | 1.6% |
| 6 | `196.190.228.223` | 9 | 1.3% |
| 7 | `27.21.28.53` | 9 | 1.3% |
| 8 | `131.100.223.214` | 8 | 1.2% |
| 9 | `77.91.71.26` | 8 | 1.2% |
| 10 | `175.0.21.74` | 8 | 1.2% |
| 11 | `2.180.134.247` | 5 | 0.7% |
| 12 | `185.242.226.9` | 4 | 0.6% |
| 13 | `187.120.22.126` | 4 | 0.6% |
| 14 | `201.110.177.47` | 4 | 0.6% |
| 15 | `185.73.23.133` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 644 | 99.8% |
| 2 | `SYN+ECE+CWR` | 1 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 680 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `194.39.243.42` -> `23` | 26 | 3.8% |
| 2 | `42.243.83.235` -> `23` | 24 | 3.5% |
| 3 | `27.31.108.165` -> `23` | 23 | 3.4% |
| 4 | `114.35.195.197` -> `23` | 11 | 1.6% |
| 5 | `196.190.228.223` -> `23` | 9 | 1.3% |
| 6 | `27.21.28.53` -> `23` | 9 | 1.3% |
| 7 | `131.100.223.214` -> `23` | 8 | 1.2% |
| 8 | `175.0.21.74` -> `23` | 8 | 1.2% |
| 9 | `2.180.134.247` -> `23` | 5 | 0.7% |
| 10 | `216.180.246.98` -> `6666` | 5 | 0.7% |
| 11 | `216.180.246.98` -> `6699` | 5 | 0.7% |
| 12 | `187.120.22.126` -> `23` | 4 | 0.6% |
| 13 | `201.110.177.47` -> `23` | 4 | 0.6% |
| 14 | `216.180.246.98` -> `6667` | 4 | 0.6% |
| 15 | `216.180.246.98` -> `6697` | 4 | 0.6% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-18 00:00:00:00 | 94 | 13.8% |
| 2026-10-18 01:00:00:00 | 181 | 26.6% |
| 2026-10-18 02:00:00:00 | 179 | 26.3% |
| 2026-10-18 03:00:00:00 | 180 | 26.5% |
| 2026-10-18 04:00:00:00 | 46 | 6.8% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Shizishan, China | 32 | 18.3% |
| 2 | Massy, France | 29 | 16.6% |
| 3 | Nakhchivan, Azerbaijan | 26 | 14.9% |
| 4 | Kunming, China | 24 | 13.7% |
| 5 | Kaohsiung, Taiwan | 11 | 6.3% |
| 6 | Tulu Bolo, Ethiopia | 9 | 5.1% |
| 7 | Lábrea, Brazil | 8 | 4.6% |
| 8 | Tel Aviv, Israel | 8 | 4.6% |
| 9 | Changsha, China | 8 | 4.6% |
| 10 | Tehran, Iran | 5 | 2.9% |
| 11 | Amsterdam, The Netherlands | 4 | 2.3% |
| 12 | Nova Iguaçu, Brazil | 4 | 2.3% |
| 13 | Naucalpan, Mexico | 4 | 2.3% |
| 14 | Frankfurt am Main, Germany | 3 | 1.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.98` | 29 | 16.6% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `194.39.243.42` | 26 | 14.9% | Azerbaijan / Nakhchivan Autonomous Republic / Nakhchivan / Araz Tech LLC | No apparent signal |
| 3 | `42.243.83.235` | 24 | 13.7% | China / Yunnan / Kunming / Chinanet YN | No apparent signal |
| 4 | `27.31.108.165` | 23 | 13.1% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 5 | `114.35.195.197` | 11 | 6.3% | Taiwan / Kaohsiung / Kaohsiung / Chunghwa Telecom Co. Ltd. | No apparent signal |
| 6 | `196.190.228.223` | 9 | 5.1% | Ethiopia / Oromiya / Tulu Bolo / Ethiotelecom | VPN/Proxy suspected (pia) |
| 7 | `27.21.28.53` | 9 | 5.1% | China / Hubei / Shizishan / Chinanet HB | No apparent signal |
| 8 | `131.100.223.214` | 8 | 4.6% | Brazil / Amazonas / Lábrea / N. J. DOS SANTOS SANTANA - ME | Hosting/Cloud (amazon) |
| 9 | `77.91.71.26` | 8 | 4.6% | Israel / Tel Aviv / Tel Aviv / NEW | No apparent signal |
| 10 | `175.0.21.74` | 8 | 4.6% | China / Hunan / Changsha / Chinanet HN | No apparent signal |
| 11 | `2.180.134.247` | 5 | 2.9% | Iran / Tehran / Tehran / Telecommunication Company | No apparent signal |
| 12 | `185.242.226.9` | 4 | 2.3% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 13 | `187.120.22.126` | 4 | 2.3% | Brazil / Rio de Janeiro / Nova Iguaçu / Golden Link | No apparent signal |
| 14 | `201.110.177.47` | 4 | 2.3% | Mexico / México / Naucalpan / Uninet S.A. de C.V | No apparent signal |
| 15 | `185.73.23.133` | 3 | 1.7% | Germany / Hesse / Frankfurt am Main / RUB LIR Inet2 | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.98` | 29 | 63.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `196.190.228.223` | 9 | 19.6% | VPN/Proxy suspected (pia) | Ethiopia / Oromiya / Tulu Bolo / Ethiotelecom |
| 3 | `131.100.223.214` | 8 | 17.4% | Hosting/Cloud (amazon) | Brazil / Amazonas / Lábrea / N. J. DOS SANTOS SANTANA - ME |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
