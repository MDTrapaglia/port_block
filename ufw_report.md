# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4348
- Unique source IPs: 2035
- Unique countries/cities (24h): 318
- Unique destination ports: 2242

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 738 | 17.0% |
| 2 | `3389` | 45 | 1.0% |
| 3 | `27015` | 43 | 1.0% |
| 4 | `22` | 40 | 0.9% |
| 5 | `8080` | 24 | 0.6% |
| 6 | `5060` | 20 | 0.5% |
| 7 | `1433` | 19 | 0.4% |
| 8 | `27017` | 18 | 0.4% |
| 9 | `8443` | 16 | 0.4% |
| 10 | `161` | 15 | 0.3% |
| 11 | `10001` | 14 | 0.3% |
| 12 | `53` | 13 | 0.3% |
| 13 | `21` | 13 | 0.3% |
| 14 | `1900` | 13 | 0.3% |
| 15 | `2375` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4013 | 92.3% |
| 2 | `UDP` | 328 | 7.5% |
| 3 | `47` | 6 | 0.1% |
| 4 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `160.119.76.63` | 405 | 9.3% |
| 2 | `103.166.200.226` | 393 | 9.0% |
| 3 | `51.159.3.123` | 165 | 3.8% |
| 4 | `216.180.246.203` | 125 | 2.9% |
| 5 | `216.180.246.19` | 56 | 1.3% |
| 6 | `207.154.242.136` | 42 | 1.0% |
| 7 | `217.148.142.94` | 21 | 0.5% |
| 8 | `180.235.129.180` | 21 | 0.5% |
| 9 | `194.180.49.245` | 18 | 0.4% |
| 10 | `151.101.218.73` | 15 | 0.3% |
| 11 | `138.226.239.21` | 13 | 0.3% |
| 12 | `206.81.7.125` | 12 | 0.3% |
| 13 | `17.57.144.155` | 12 | 0.3% |
| 14 | `45.198.224.10` | 11 | 0.3% |
| 15 | `124.198.131.22` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3933 | 98.0% |
| 2 | `ACK+PSH` | 48 | 1.2% |
| 3 | `ACK+FIN+PSH` | 26 | 0.6% |
| 4 | `ACK` | 3 | 0.1% |
| 5 | `SYN+ECE+CWR` | 2 | 0.0% |
| 6 | `ACK+FIN` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4344 | 99.9% |
| 2 | `wlan0` | 4 | 0.1% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `103.166.200.226` -> `23` | 393 | 9.0% |
| 2 | `51.159.3.123` -> `23` | 165 | 3.8% |
| 3 | `207.154.242.136` -> `23` | 42 | 1.0% |
| 4 | `217.148.142.94` -> `23` | 21 | 0.5% |
| 5 | `180.235.129.180` -> `23` | 21 | 0.5% |
| 6 | `216.180.246.203` -> `3389` | 13 | 0.3% |
| 7 | `216.180.246.203` -> `16992` | 13 | 0.3% |
| 8 | `216.180.246.203` -> `5140` | 10 | 0.2% |
| 9 | `216.180.246.203` -> `806` | 10 | 0.2% |
| 10 | `66.132.172.197` -> `10001` | 10 | 0.2% |
| 11 | `69.17.52.1` -> `8333` | 9 | 0.2% |
| 12 | `216.180.246.203` -> `6003` | 8 | 0.2% |
| 13 | `216.180.246.203` -> `657` | 8 | 0.2% |
| 14 | `216.180.246.203` -> `6666` | 8 | 0.2% |
| 15 | `216.180.246.203` -> `2049` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-25 04:00:00:00 | 134 | 3.1% |
| 2026-05-25 05:00:00:00 | 178 | 4.1% |
| 2026-05-25 06:00:00:00 | 184 | 4.2% |
| 2026-05-25 07:00:00:00 | 180 | 4.1% |
| 2026-05-25 08:00:00:00 | 181 | 4.2% |
| 2026-05-25 09:00:00:00 | 179 | 4.1% |
| 2026-05-25 10:00:00:00 | 182 | 4.2% |
| 2026-05-25 11:00:00:00 | 184 | 4.2% |
| 2026-05-25 12:00:00:00 | 181 | 4.2% |
| 2026-05-25 13:00:00:00 | 179 | 4.1% |
| 2026-05-25 14:00:00:00 | 184 | 4.2% |
| 2026-05-25 15:00:00:00 | 180 | 4.1% |
| 2026-05-25 16:00:00:00 | 184 | 4.2% |
| 2026-05-25 17:00:00:00 | 181 | 4.2% |
| 2026-05-25 18:00:00:00 | 180 | 4.1% |
| 2026-05-25 19:00:00:00 | 180 | 4.1% |
| 2026-05-25 20:00:00:00 | 180 | 4.1% |
| 2026-05-25 21:00:00:00 | 178 | 4.1% |
| 2026-05-25 22:00:00:00 | 182 | 4.2% |
| 2026-05-25 23:00:00:00 | 180 | 4.1% |
| 2026-05-26 00:00:00:00 | 192 | 4.4% |
| 2026-05-26 01:00:00:00 | 180 | 4.1% |
| 2026-05-26 02:00:00:00 | 181 | 4.2% |
| 2026-05-26 03:00:00:00 | 179 | 4.1% |
| 2026-05-26 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 405 | 30.7% |
| 2 | Jakarta, Indonesia | 393 | 29.8% |
| 3 | Massy, France | 181 | 13.7% |
| 4 | Paris, France | 165 | 12.5% |
| 5 | Frankfurt am Main, Germany | 42 | 3.2% |
| 6 | New York, United States | 31 | 2.4% |
| 7 | Ultimo, Australia | 21 | 1.6% |
| 8 | Berngau, Germany | 18 | 1.4% |
| 9 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 15 | 1.1% |
| 10 | Port Vila, Vanuatu | 13 | 1.0% |
| 11 | North Bergen, United States | 12 | 0.9% |
| 12 | Cupertino, United States | 12 | 0.9% |
| 13 | Stockholm, Sweden | 11 | 0.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `160.119.76.63` | 405 | 30.7% | The Netherlands / North Holland / Amsterdam / HostUS Solutions LLC | No apparent signal |
| 2 | `103.166.200.226` | 393 | 29.8% | Indonesia / Jakarta / Jakarta / Hipernet Indodata | No apparent signal |
| 3 | `51.159.3.123` | 165 | 12.5% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 4 | `216.180.246.203` | 125 | 9.5% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 5 | `216.180.246.19` | 56 | 4.2% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 6 | `207.154.242.136` | 42 | 3.2% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 7 | `217.148.142.94` | 21 | 1.6% | United States / New York / New York / M247 LTD | VPN/Proxy suspected (m247) |
| 8 | `180.235.129.180` | 21 | 1.6% | Australia / New South Wales / Ultimo / Netregistry | Mobile/CGNAT (5g) |
| 9 | `194.180.49.245` | 18 | 1.4% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 10 | `151.101.218.73` | 15 | 1.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 11 | `138.226.239.21` | 13 | 1.0% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 12 | `206.81.7.125` | 12 | 0.9% | United States / New Jersey / North Bergen / Digital Ocean | Hosting/Cloud (digitalocean) |
| 13 | `17.57.144.155` | 12 | 0.9% | United States / California / Cupertino / Apple Inc | No apparent signal |
| 14 | `45.198.224.10` | 11 | 0.8% | Sweden / Stockholm County / Stockholm / Cloud Innovation Ltd | No apparent signal |
| 15 | `124.198.131.22` | 10 | 0.8% | United States / New York / New York / 1337 Services GmbH | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `51.159.3.123` | 165 | 37.8% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `216.180.246.203` | 125 | 28.7% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 3 | `216.180.246.19` | 56 | 12.8% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 4 | `207.154.242.136` | 42 | 9.6% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |
| 5 | `217.148.142.94` | 21 | 4.8% | VPN/Proxy suspected (m247) | United States / New York / New York / M247 LTD |
| 6 | `151.101.218.73` | 15 | 3.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 7 | `206.81.7.125` | 12 | 2.8% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / Digital Ocean |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
