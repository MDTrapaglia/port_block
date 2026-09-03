# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4318
- Unique source IPs: 2289
- Unique countries/cities (24h): 349
- Unique destination ports: 2766

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 182 | 4.2% |
| 2 | `22` | 75 | 1.7% |
| 3 | `5060` | 47 | 1.1% |
| 4 | `8080` | 31 | 0.7% |
| 5 | `53` | 23 | 0.5% |
| 6 | `3389` | 20 | 0.5% |
| 7 | `8081` | 16 | 0.4% |
| 8 | `8009` | 15 | 0.3% |
| 9 | `123` | 14 | 0.3% |
| 10 | `2222` | 14 | 0.3% |
| 11 | `1433` | 13 | 0.3% |
| 12 | `3306` | 12 | 0.3% |
| 13 | `27017` | 12 | 0.3% |
| 14 | `8010` | 12 | 0.3% |
| 15 | `3000` | 11 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3931 | 91.0% |
| 2 | `UDP` | 377 | 8.7% |
| 3 | `47` | 9 | 0.2% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `82.151.84.22` | 240 | 5.6% |
| 2 | `216.180.246.50` | 163 | 3.8% |
| 3 | `103.153.182.61` | 72 | 1.7% |
| 4 | `16.5.0.244` | 72 | 1.7% |
| 5 | `16.5.0.245` | 65 | 1.5% |
| 6 | `188.255.156.155` | 56 | 1.3% |
| 7 | `103.165.11.233` | 36 | 0.8% |
| 8 | `216.180.246.212` | 26 | 0.6% |
| 9 | `172.110.223.179` | 16 | 0.4% |
| 10 | `85.217.140.29` | 12 | 0.3% |
| 11 | `18.217.208.51` | 11 | 0.3% |
| 12 | `3.147.122.184` | 11 | 0.3% |
| 13 | `77.239.124.127` | 11 | 0.3% |
| 14 | `94.154.43.111` | 11 | 0.3% |
| 15 | `85.217.149.37` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3924 | 99.8% |
| 2 | `SYN+ECE+CWR` | 6 | 0.2% |
| 3 | `ACK+PSH` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4318 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `172.110.223.179` -> `5060` | 16 | 0.4% |
| 2 | `216.180.246.50` -> `8009` | 10 | 0.2% |
| 3 | `216.180.246.50` -> `8012` | 9 | 0.2% |
| 4 | `216.180.246.50` -> `8048` | 9 | 0.2% |
| 5 | `216.180.246.50` -> `8010` | 8 | 0.2% |
| 6 | `216.180.246.50` -> `8031` | 8 | 0.2% |
| 7 | `216.180.246.50` -> `8040` | 8 | 0.2% |
| 8 | `216.180.246.50` -> `8028` | 7 | 0.2% |
| 9 | `216.180.246.50` -> `8036` | 7 | 0.2% |
| 10 | `216.180.246.50` -> `8060` | 7 | 0.2% |
| 11 | `216.180.246.50` -> `8069` | 7 | 0.2% |
| 12 | `216.180.246.50` -> `8008` | 6 | 0.1% |
| 13 | `216.180.246.50` -> `8011` | 6 | 0.1% |
| 14 | `216.180.246.50` -> `8014` | 6 | 0.1% |
| 15 | `216.180.246.50` -> `8075` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-02 04:00:00:00 | 134 | 3.1% |
| 2026-09-02 05:00:00:00 | 179 | 4.1% |
| 2026-09-02 06:00:00:00 | 182 | 4.2% |
| 2026-09-02 07:00:00:00 | 178 | 4.1% |
| 2026-09-02 08:00:00:00 | 182 | 4.2% |
| 2026-09-02 09:00:00:00 | 179 | 4.1% |
| 2026-09-02 10:00:00:00 | 180 | 4.2% |
| 2026-09-02 11:00:00:00 | 181 | 4.2% |
| 2026-09-02 12:00:00:00 | 180 | 4.2% |
| 2026-09-02 13:00:00:00 | 180 | 4.2% |
| 2026-09-02 14:00:00:00 | 178 | 4.1% |
| 2026-09-02 15:00:00:00 | 182 | 4.2% |
| 2026-09-02 16:00:00:00 | 180 | 4.2% |
| 2026-09-02 17:00:00:00 | 179 | 4.1% |
| 2026-09-02 18:00:00:00 | 180 | 4.2% |
| 2026-09-02 19:00:00:00 | 180 | 4.2% |
| 2026-09-02 20:00:00:00 | 180 | 4.2% |
| 2026-09-02 21:00:00:00 | 180 | 4.2% |
| 2026-09-02 22:00:00:00 | 181 | 4.2% |
| 2026-09-02 23:00:00:00 | 179 | 4.1% |
| 2026-09-03 00:00:00:00 | 180 | 4.2% |
| 2026-09-03 01:00:00:00 | 180 | 4.2% |
| 2026-09-03 02:00:00:00 | 180 | 4.2% |
| 2026-09-03 03:00:00:00 | 180 | 4.2% |
| 2026-09-03 04:00:00:00 | 43 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Nouakchott, Mauritania | 240 | 29.6% |
| 2 | Massy, France | 189 | 23.3% |
| 3 | São Paulo, Brazil | 137 | 16.9% |
| 4 | Dallas, United States | 72 | 8.9% |
| 5 | Belgrade, Serbia | 56 | 6.9% |
| 6 | Mumbai, India | 36 | 4.4% |
| 7 | Dublin, United States | 22 | 2.7% |
| 8 | Amsterdam, The Netherlands | 22 | 2.7% |
| 9 | Atlanta, United States | 16 | 2.0% |
| 10 | Gravelines, France | 12 | 1.5% |
| 11 | Beauharnois, Canada | 10 | 1.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `82.151.84.22` | 240 | 29.6% | Mauritania / Nouakchott South / Nouakchott / Interconnexions Networks | No apparent signal |
| 2 | `216.180.246.50` | 163 | 20.1% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 3 | `103.153.182.61` | 72 | 8.9% | United States / Texas / Dallas / Harsh Jain | No apparent signal |
| 4 | `16.5.0.244` | 72 | 8.9% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 5 | `16.5.0.245` | 65 | 8.0% | Brazil / São Paulo / São Paulo / EMBNEX. LLC | No apparent signal |
| 6 | `188.255.156.155` | 56 | 6.9% | Serbia / Belgrade / Belgrade / Orion Telekom Tim d.o.o.Beograd | No apparent signal |
| 7 | `103.165.11.233` | 36 | 4.4% | India / Maharashtra / Mumbai / Orange Waves Networks Private Limited | No apparent signal |
| 8 | `216.180.246.212` | 26 | 3.2% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 9 | `172.110.223.179` | 16 | 2.0% | United States / Georgia / Atlanta / Dedires LLC | No apparent signal |
| 10 | `85.217.140.29` | 12 | 1.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `18.217.208.51` | 11 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `3.147.122.184` | 11 | 1.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `77.239.124.127` | 11 | 1.4% | The Netherlands / North Holland / Amsterdam / RocketCloud | No apparent signal |
| 14 | `94.154.43.111` | 11 | 1.4% | The Netherlands / North Holland / Amsterdam / FOP Danik Vyacheslav Evgenievich | No apparent signal |
| 15 | `85.217.149.37` | 10 | 1.2% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.50` | 163 | 77.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `216.180.246.212` | 26 | 12.3% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 3 | `18.217.208.51` | 11 | 5.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `3.147.122.184` | 11 | 5.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
