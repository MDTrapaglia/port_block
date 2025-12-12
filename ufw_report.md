# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4486
- Unique source IPs: 1872
- Unique destination ports: 2561

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `8333` | 464 | 10.3% |
| 2 | `23` | 131 | 2.9% |
| 3 | `443` | 74 | 1.6% |
| 4 | `8080` | 53 | 1.2% |
| 5 | `22` | 39 | 0.9% |
| 6 | `3389` | 38 | 0.8% |
| 7 | `8728` | 30 | 0.7% |
| 8 | `5000` | 27 | 0.6% |
| 9 | `53` | 20 | 0.4% |
| 10 | `1433` | 19 | 0.4% |
| 11 | `8443` | 19 | 0.4% |
| 12 | `389` | 16 | 0.4% |
| 13 | `5060` | 15 | 0.3% |
| 14 | `3000` | 15 | 0.3% |
| 15 | `1900` | 14 | 0.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `194.180.49.70` | 134 | 3.0% |
| 2 | `147.229.8.240` | 107 | 2.4% |
| 3 | `79.124.62.230` | 90 | 2.0% |
| 4 | `79.124.62.126` | 82 | 1.8% |
| 5 | `109.236.61.34` | 57 | 1.3% |
| 6 | `103.99.170.131` | 51 | 1.1% |
| 7 | `185.91.127.107` | 44 | 1.0% |
| 8 | `100.24.10.103` | 42 | 0.9% |
| 9 | `103.99.170.132` | 41 | 0.9% |
| 10 | `208.68.7.148` | 41 | 0.9% |
| 11 | `151.101.218.73` | 30 | 0.7% |
| 12 | `103.102.230.4` | 23 | 0.5% |
| 13 | `45.11.57.212` | 22 | 0.5% |
| 14 | `85.217.140.1` | 22 | 0.5% |
| 15 | `51.161.174.170` | 20 | 0.4% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `147.229.8.240` -> `8333` | 107 | 2.4% |
| 2 | `103.99.170.131` -> `8333` | 51 | 1.1% |
| 3 | `100.24.10.103` -> `8333` | 42 | 0.9% |
| 4 | `103.99.170.132` -> `8333` | 41 | 0.9% |
| 5 | `208.68.7.148` -> `8333` | 41 | 0.9% |
| 6 | `103.102.230.4` -> `8728` | 23 | 0.5% |
| 7 | `109.236.61.34` -> `5000` | 23 | 0.5% |
| 8 | `45.11.57.212` -> `8333` | 22 | 0.5% |
| 9 | `129.132.30.218` -> `8333` | 18 | 0.4% |
| 10 | `109.236.61.34` -> `8080` | 16 | 0.4% |
| 11 | `204.76.203.83` -> `22` | 15 | 0.3% |
| 12 | `109.236.61.34` -> `8092` | 12 | 0.3% |
| 13 | `79.124.62.126` -> `3389` | 11 | 0.2% |
| 14 | `185.244.104.2` -> `443` | 11 | 0.2% |
| 15 | `192.168.100.1` -> `68` | 9 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2025-12-11 10:00:00:00 | 44 | 1.0% |
| 2025-12-11 11:00:00:00 | 197 | 4.4% |
| 2025-12-11 12:00:00:00 | 181 | 4.0% |
| 2025-12-11 13:00:00:00 | 180 | 4.0% |
| 2025-12-11 14:00:00:00 | 189 | 4.2% |
| 2025-12-11 15:00:00:00 | 179 | 4.0% |
| 2025-12-11 16:00:00:00 | 182 | 4.1% |
| 2025-12-11 17:00:00:00 | 181 | 4.0% |
| 2025-12-11 18:00:00:00 | 181 | 4.0% |
| 2025-12-11 19:00:00:00 | 209 | 4.7% |
| 2025-12-11 20:00:00:00 | 199 | 4.4% |
| 2025-12-11 21:00:00:00 | 180 | 4.0% |
| 2025-12-11 22:00:00:00 | 186 | 4.1% |
| 2025-12-11 23:00:00:00 | 188 | 4.2% |
| 2025-12-12 00:00:00:00 | 232 | 5.2% |
| 2025-12-12 01:00:00:00 | 179 | 4.0% |
| 2025-12-12 02:00:00:00 | 180 | 4.0% |
| 2025-12-12 03:00:00:00 | 180 | 4.0% |
| 2025-12-12 04:00:00:00 | 180 | 4.0% |
| 2025-12-12 05:00:00:00 | 188 | 4.2% |
| 2025-12-12 06:00:00:00 | 181 | 4.0% |
| 2025-12-12 07:00:00:00 | 181 | 4.0% |
| 2025-12-12 08:00:00:00 | 183 | 4.1% |
| 2025-12-12 09:00:00:00 | 180 | 4.0% |
| 2025-12-12 10:00:00:00 | 146 | 3.3% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Germany / Bavaria / Berngau / HostSlick | 134 | 16.6% |
| 2 | Czechia / South Moravian / Tišnov / VUTBR | 107 | 13.3% |
| 3 | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | 90 | 11.2% |
| 4 | Victoria, Seychelles | 82 | 10.2% |
| 5 | Amsterdam, The Netherlands | 57 | 7.1% |
| 6 | San Jose, United States | 51 | 6.3% |
| 7 | Eygelshoven, The Netherlands | 44 | 5.5% |
| 8 | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | 42 | 5.2% |
| 9 | United States / California / San Jose / WIZ K K | 41 | 5.1% |
| 10 | New York, United States | 41 | 5.1% |
| 11 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 30 | 3.7% |
| 12 | Yakutsk, Russia | 23 | 2.9% |
| 13 | Kyiv, Ukraine | 22 | 2.7% |
| 14 | Paris, France | 22 | 2.7% |
| 15 | North Sydney, Australia | 20 | 2.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `194.180.49.70` | 134 | 16.6% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 2 | `147.229.8.240` | 107 | 13.3% | Czechia / South Moravian / Tišnov / VUTBR | No apparent signal |
| 3 | `79.124.62.230` | 90 | 11.2% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 4 | `79.124.62.126` | 82 | 10.2% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 5 | `109.236.61.34` | 57 | 7.1% | The Netherlands / North Holland / Amsterdam / ColocationX Ltd | Hosting/Cloud (colo) |
| 6 | `103.99.170.131` | 51 | 6.3% | United States / California / San Jose / WIZ K K | No apparent signal |
| 7 | `185.91.127.107` | 44 | 5.5% | The Netherlands / Limburg / Eygelshoven / Tube VPS | No apparent signal |
| 8 | `100.24.10.103` | 42 | 5.2% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 9 | `103.99.170.132` | 41 | 5.1% | United States / California / San Jose / WIZ K K | No apparent signal |
| 10 | `208.68.7.148` | 41 | 5.1% | United States / New York / New York / Privacy Services | No apparent signal |
| 11 | `151.101.218.73` | 30 | 3.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 12 | `103.102.230.4` | 23 | 2.9% | Russia / Sakha / Yakutsk / mkr. Rostoshi | Mobile/CGNAT (lte) |
| 13 | `45.11.57.212` | 22 | 2.7% | Ukraine / Kyiv City / Kyiv / Virtual Systems LLC | No apparent signal |
| 14 | `85.217.140.1` | 22 | 2.7% | France / Île-de-France / Paris / Modat B.V | No apparent signal |
| 15 | `51.161.174.170` | 20 | 2.5% | Australia / New South Wales / North Sydney / OVH Australia PTY LTD | Hosting/Cloud (ovh) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `109.236.61.34` | 57 | 38.3% | Hosting/Cloud (colo) | The Netherlands / North Holland / Amsterdam / ColocationX Ltd |
| 2 | `100.24.10.103` | 42 | 28.2% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 3 | `151.101.218.73` | 30 | 20.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `51.161.174.170` | 20 | 13.4% | Hosting/Cloud (ovh) | Australia / New South Wales / North Sydney / OVH Australia PTY LTD |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source IPs](ufw_plots/ufw_top_ips.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
