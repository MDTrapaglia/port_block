# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4409
- Unique source IPs: 2265
- Unique countries/cities (24h): 339
- Unique destination ports: 2721

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 268 | 6.1% |
| 2 | `unknown` | 54 | 1.2% |
| 3 | `22` | 44 | 1.0% |
| 4 | `8080` | 37 | 0.8% |
| 5 | `5060` | 31 | 0.7% |
| 6 | `3389` | 30 | 0.7% |
| 7 | `53` | 25 | 0.6% |
| 8 | `123` | 23 | 0.5% |
| 9 | `2222` | 19 | 0.4% |
| 10 | `8081` | 17 | 0.4% |
| 11 | `8083` | 16 | 0.4% |
| 12 | `3306` | 15 | 0.3% |
| 13 | `5900` | 15 | 0.3% |
| 14 | `161` | 15 | 0.3% |
| 15 | `1433` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3838 | 87.0% |
| 2 | `UDP` | 517 | 11.7% |
| 3 | `47` | 52 | 1.2% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `112.140.187.102` | 180 | 4.1% |
| 2 | `62.210.142.165` | 121 | 2.7% |
| 3 | `192.168.100.14` | 98 | 2.2% |
| 4 | `5.254.5.89` | 70 | 1.6% |
| 5 | `85.217.140.4` | 30 | 0.7% |
| 6 | `51.83.10.130` | 23 | 0.5% |
| 7 | `51.83.10.134` | 22 | 0.5% |
| 8 | `51.83.10.158` | 21 | 0.5% |
| 9 | `51.83.10.135` | 21 | 0.5% |
| 10 | `51.83.10.147` | 20 | 0.5% |
| 11 | `108.181.62.31` | 20 | 0.5% |
| 12 | `51.83.10.173` | 18 | 0.4% |
| 13 | `85.217.140.5` | 16 | 0.4% |
| 14 | `31.14.32.8` | 16 | 0.4% |
| 15 | `85.217.140.25` | 15 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3721 | 97.0% |
| 2 | `ACK+FIN+PSH` | 70 | 1.8% |
| 3 | `ACK+PSH` | 25 | 0.7% |
| 4 | `ACK+FIN` | 13 | 0.3% |
| 5 | `ACK` | 5 | 0.1% |
| 6 | `SYN+ECE+CWR` | 4 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4390 | 99.6% |
| 2 | `wlan0` | 19 | 0.4% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `112.140.187.102` -> `23` | 180 | 4.1% |
| 2 | `200.219.11.123` -> `5060` | 8 | 0.2% |
| 3 | `62.210.142.165` -> `8083` | 8 | 0.2% |
| 4 | `69.17.52.1` -> `8333` | 7 | 0.2% |
| 5 | `199.45.155.98` -> `21` | 7 | 0.2% |
| 6 | `62.210.142.165` -> `8080` | 7 | 0.2% |
| 7 | `62.210.142.165` -> `8084` | 7 | 0.2% |
| 8 | `62.210.142.165` -> `8089` | 7 | 0.2% |
| 9 | `66.132.172.177` -> `1195` | 6 | 0.1% |
| 10 | `192.168.100.1` -> `68` | 6 | 0.1% |
| 11 | `62.210.142.165` -> `8079` | 6 | 0.1% |
| 12 | `62.210.142.165` -> `8110` | 6 | 0.1% |
| 13 | `2.23.164.148` -> `61028` | 6 | 0.1% |
| 14 | `2.23.164.202` -> `58835` | 6 | 0.1% |
| 15 | `62.210.142.165` -> `8081` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-07-15 04:00:00:00 | 135 | 3.1% |
| 2026-07-15 05:00:00:00 | 178 | 4.0% |
| 2026-07-15 06:00:00:00 | 182 | 4.1% |
| 2026-07-15 07:00:00:00 | 179 | 4.1% |
| 2026-07-15 08:00:00:00 | 180 | 4.1% |
| 2026-07-15 09:00:00:00 | 195 | 4.4% |
| 2026-07-15 10:00:00:00 | 177 | 4.0% |
| 2026-07-15 11:00:00:00 | 184 | 4.2% |
| 2026-07-15 12:00:00:00 | 187 | 4.2% |
| 2026-07-15 13:00:00:00 | 177 | 4.0% |
| 2026-07-15 14:00:00:00 | 183 | 4.2% |
| 2026-07-15 15:00:00:00 | 180 | 4.1% |
| 2026-07-15 16:00:00:00 | 192 | 4.4% |
| 2026-07-15 17:00:00:00 | 180 | 4.1% |
| 2026-07-15 18:00:00:00 | 178 | 4.0% |
| 2026-07-15 19:00:00:00 | 199 | 4.5% |
| 2026-07-15 20:00:00:00 | 211 | 4.8% |
| 2026-07-15 21:00:00:00 | 179 | 4.1% |
| 2026-07-15 22:00:00:00 | 181 | 4.1% |
| 2026-07-15 23:00:00:00 | 180 | 4.1% |
| 2026-07-16 00:00:00:00 | 186 | 4.2% |
| 2026-07-16 01:00:00:00 | 180 | 4.1% |
| 2026-07-16 02:00:00:00 | 181 | 4.1% |
| 2026-07-16 03:00:00:00 | 179 | 4.1% |
| 2026-07-16 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Singapore, Singapore | 180 | 26.0% |
| 2 | Roubaix, France | 125 | 18.1% |
| 3 | Paris, France | 121 | 17.5% |
| 4 | private | 98 | 14.2% |
| 5 | Los Angeles, United States | 70 | 10.1% |
| 6 | Gravelines, France | 61 | 8.8% |
| 7 | Chicago, United States | 20 | 2.9% |
| 8 | Amsterdam, The Netherlands | 16 | 2.3% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `112.140.187.102` | 180 | 26.0% | Singapore / Central Singapore / Singapore / Sparkstation | No apparent signal |
| 2 | `62.210.142.165` | 121 | 17.5% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 3 | `192.168.100.14` | 98 | 14.2% | private | Private/CGNAT |
| 4 | `5.254.5.89` | 70 | 10.1% | United States / California / Los Angeles / Edge Network Technologies Ltd | No apparent signal |
| 5 | `85.217.140.4` | 30 | 4.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `51.83.10.130` | 23 | 3.3% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 7 | `51.83.10.134` | 22 | 3.2% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 8 | `51.83.10.158` | 21 | 3.0% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 9 | `51.83.10.135` | 21 | 3.0% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 10 | `51.83.10.147` | 20 | 2.9% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 11 | `108.181.62.31` | 20 | 2.9% | United States / Illinois / Chicago / TELUS Communications Inc. | Hosting/Cloud (psychz) |
| 12 | `51.83.10.173` | 18 | 2.6% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 13 | `85.217.140.5` | 16 | 2.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `31.14.32.8` | 16 | 2.3% | The Netherlands / North Holland / Amsterdam / Modat | No apparent signal |
| 15 | `85.217.140.25` | 15 | 2.2% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.165` | 121 | 45.5% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `51.83.10.130` | 23 | 8.6% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |
| 3 | `51.83.10.134` | 22 | 8.3% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |
| 4 | `51.83.10.158` | 21 | 7.9% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |
| 5 | `51.83.10.135` | 21 | 7.9% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |
| 6 | `51.83.10.147` | 20 | 7.5% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |
| 7 | `108.181.62.31` | 20 | 7.5% | Hosting/Cloud (psychz) | United States / Illinois / Chicago / TELUS Communications Inc. |
| 8 | `51.83.10.173` | 18 | 6.8% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
