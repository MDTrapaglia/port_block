# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4350
- Unique source IPs: 1639
- Unique countries/cities (24h): 283
- Unique destination ports: 3127

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 191 | 4.4% |
| 2 | `27015` | 69 | 1.6% |
| 3 | `8080` | 38 | 0.9% |
| 4 | `22` | 24 | 0.6% |
| 5 | `1433` | 23 | 0.5% |
| 6 | `3389` | 22 | 0.5% |
| 7 | `8443` | 18 | 0.4% |
| 8 | `5060` | 17 | 0.4% |
| 9 | `5900` | 17 | 0.4% |
| 10 | `81` | 15 | 0.3% |
| 11 | `21` | 14 | 0.3% |
| 12 | `53` | 13 | 0.3% |
| 13 | `8181` | 12 | 0.3% |
| 14 | `8081` | 12 | 0.3% |
| 15 | `3306` | 12 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4022 | 92.5% |
| 2 | `UDP` | 324 | 7.4% |
| 3 | `47` | 4 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `91.227.114.132` | 1266 | 29.1% |
| 2 | `160.119.76.44` | 378 | 8.7% |
| 3 | `199.223.115.56` | 124 | 2.9% |
| 4 | `216.180.246.41` | 79 | 1.8% |
| 5 | `31.56.209.223` | 32 | 0.7% |
| 6 | `45.142.193.70` | 25 | 0.6% |
| 7 | `45.142.193.122` | 23 | 0.5% |
| 8 | `45.142.193.121` | 23 | 0.5% |
| 9 | `45.142.193.105` | 22 | 0.5% |
| 10 | `45.142.193.131` | 21 | 0.5% |
| 11 | `45.142.193.18` | 19 | 0.4% |
| 12 | `45.142.193.125` | 19 | 0.4% |
| 13 | `45.142.193.118` | 18 | 0.4% |
| 14 | `97.74.236.238` | 16 | 0.4% |
| 15 | `45.142.193.223` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3969 | 98.7% |
| 2 | `ACK+FIN+PSH` | 27 | 0.7% |
| 3 | `ACK+PSH` | 15 | 0.4% |
| 4 | `ACK` | 5 | 0.1% |
| 5 | `SYN+ECE+CWR` | 5 | 0.1% |
| 6 | `ACK+FIN` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4348 | 100.0% |
| 2 | `wlan0` | 2 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `199.223.115.56` -> `23` | 124 | 2.9% |
| 2 | `31.56.209.223` -> `8080` | 16 | 0.4% |
| 3 | `97.74.236.238` -> `23` | 16 | 0.4% |
| 4 | `31.56.209.223` -> `23` | 16 | 0.4% |
| 5 | `216.180.246.41` -> `800` | 8 | 0.2% |
| 6 | `216.180.246.41` -> `5900` | 7 | 0.2% |
| 7 | `216.180.246.41` -> `2084` | 6 | 0.1% |
| 8 | `216.180.246.41` -> `32332` | 6 | 0.1% |
| 9 | `216.180.246.41` -> `44444` | 5 | 0.1% |
| 10 | `216.180.246.41` -> `2443` | 5 | 0.1% |
| 11 | `216.180.246.41` -> `1887` | 5 | 0.1% |
| 12 | `216.180.246.41` -> `19133` | 5 | 0.1% |
| 13 | `199.45.155.96` -> `8443` | 5 | 0.1% |
| 14 | `154.0.30.137` -> `3389` | 4 | 0.1% |
| 15 | `3.128.64.243` -> `53232` | 4 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-01 04:00:00:00 | 133 | 3.1% |
| 2026-06-01 05:00:00:00 | 180 | 4.1% |
| 2026-06-01 06:00:00:00 | 181 | 4.2% |
| 2026-06-01 07:00:00:00 | 195 | 4.5% |
| 2026-06-01 08:00:00:00 | 192 | 4.4% |
| 2026-06-01 09:00:00:00 | 183 | 4.2% |
| 2026-06-01 10:00:00:00 | 179 | 4.1% |
| 2026-06-01 11:00:00:00 | 181 | 4.2% |
| 2026-06-01 12:00:00:00 | 179 | 4.1% |
| 2026-06-01 13:00:00:00 | 180 | 4.1% |
| 2026-06-01 14:00:00:00 | 180 | 4.1% |
| 2026-06-01 15:00:00:00 | 180 | 4.1% |
| 2026-06-01 16:00:00:00 | 180 | 4.1% |
| 2026-06-01 17:00:00:00 | 178 | 4.1% |
| 2026-06-01 18:00:00:00 | 181 | 4.2% |
| 2026-06-01 19:00:00:00 | 182 | 4.2% |
| 2026-06-01 20:00:00:00 | 180 | 4.1% |
| 2026-06-01 21:00:00:00 | 180 | 4.1% |
| 2026-06-01 22:00:00:00 | 180 | 4.1% |
| 2026-06-01 23:00:00:00 | 180 | 4.1% |
| 2026-06-02 00:00:00:00 | 180 | 4.1% |
| 2026-06-02 01:00:00:00 | 180 | 4.1% |
| 2026-06-02 02:00:00:00 | 180 | 4.1% |
| 2026-06-02 03:00:00:00 | 180 | 4.1% |
| 2026-06-02 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Berlin, Germany | 1266 | 60.9% |
| 2 | Cascade, Seychelles | 378 | 18.2% |
| 3 | London, United Kingdom | 185 | 8.9% |
| 4 | Ashburn, United States | 124 | 6.0% |
| 5 | Massy, France | 79 | 3.8% |
| 6 | Eygelshoven, The Netherlands | 32 | 1.5% |
| 7 | Tempe, United States | 16 | 0.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `91.227.114.132` | 1266 | 60.9% | Germany / State of Berlin / Berlin / Xantho UAB | No apparent signal |
| 2 | `160.119.76.44` | 378 | 18.2% | Seychelles / Cascade / Cascade / HostUS Solutions LLC | No apparent signal |
| 3 | `199.223.115.56` | 124 | 6.0% | United States / Virginia / Ashburn / InMotion Hosting, Inc | No apparent signal |
| 4 | `216.180.246.41` | 79 | 3.8% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 5 | `31.56.209.223` | 32 | 1.5% | The Netherlands / Limburg / Eygelshoven / Pfcloud | No apparent signal |
| 6 | `45.142.193.70` | 25 | 1.2% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 7 | `45.142.193.122` | 23 | 1.1% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 8 | `45.142.193.121` | 23 | 1.1% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 9 | `45.142.193.105` | 22 | 1.1% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 10 | `45.142.193.131` | 21 | 1.0% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 11 | `45.142.193.18` | 19 | 0.9% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 12 | `45.142.193.125` | 19 | 0.9% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 13 | `45.142.193.118` | 18 | 0.9% | United Kingdom / England / London / Limited Network LTD | No apparent signal |
| 14 | `97.74.236.238` | 16 | 0.8% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 15 | `45.142.193.223` | 15 | 0.7% | United Kingdom / England / London / Limited Network LTD | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.41` | 79 | 100.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
