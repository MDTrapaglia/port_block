# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4484
- Unique source IPs: 1770
- Unique destination ports: 2684

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `8333` | 403 | 9.0% |
| 2 | `23` | 97 | 2.2% |
| 3 | `443` | 96 | 2.1% |
| 4 | `8080` | 48 | 1.1% |
| 5 | `22` | 44 | 1.0% |
| 6 | `3389` | 31 | 0.7% |
| 7 | `8728` | 27 | 0.6% |
| 8 | `5060` | 19 | 0.4% |
| 9 | `8443` | 19 | 0.4% |
| 10 | `1433` | 17 | 0.4% |
| 11 | `53` | 17 | 0.4% |
| 12 | `5000` | 16 | 0.4% |
| 13 | `8092` | 15 | 0.3% |
| 14 | `2222` | 15 | 0.3% |
| 15 | `2323` | 14 | 0.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `194.180.49.70` | 137 | 3.1% |
| 2 | `45.147.46.32` | 116 | 2.6% |
| 3 | `147.229.8.240` | 110 | 2.5% |
| 4 | `46.31.77.187` | 103 | 2.3% |
| 5 | `185.241.206.91` | 81 | 1.8% |
| 6 | `79.124.62.230` | 77 | 1.7% |
| 7 | `79.124.62.126` | 68 | 1.5% |
| 8 | `109.236.61.34` | 55 | 1.2% |
| 9 | `151.101.218.73` | 53 | 1.2% |
| 10 | `185.91.127.107` | 45 | 1.0% |
| 11 | `103.99.170.132` | 43 | 1.0% |
| 12 | `208.68.7.148` | 42 | 0.9% |
| 13 | `103.99.170.131` | 40 | 0.9% |
| 14 | `115.231.78.11` | 30 | 0.7% |
| 15 | `129.132.30.218` | 23 | 0.5% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `147.229.8.240` -> `8333` | 110 | 2.5% |
| 2 | `103.99.170.132` -> `8333` | 43 | 1.0% |
| 3 | `208.68.7.148` -> `8333` | 42 | 0.9% |
| 4 | `103.99.170.131` -> `8333` | 40 | 0.9% |
| 5 | `129.132.30.218` -> `8333` | 23 | 0.5% |
| 6 | `109.236.61.34` -> `8080` | 20 | 0.4% |
| 7 | `204.76.203.83` -> `22` | 19 | 0.4% |
| 8 | `103.102.230.4` -> `8728` | 18 | 0.4% |
| 9 | `45.11.57.212` -> `8333` | 18 | 0.4% |
| 10 | `109.236.61.34` -> `8092` | 13 | 0.3% |
| 11 | `109.236.61.34` -> `5000` | 13 | 0.3% |
| 12 | `72.65.246.82` -> `8333` | 11 | 0.2% |
| 13 | `185.244.104.2` -> `443` | 10 | 0.2% |
| 14 | `100.24.10.103` -> `8333` | 10 | 0.2% |
| 15 | `109.236.61.34` -> `443` | 9 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2025-12-10 17:00:00:00 | 90 | 2.0% |
| 2025-12-10 18:00:00:00 | 191 | 4.3% |
| 2025-12-10 19:00:00:00 | 180 | 4.0% |
| 2025-12-10 20:00:00:00 | 180 | 4.0% |
| 2025-12-10 21:00:00:00 | 180 | 4.0% |
| 2025-12-10 22:00:00:00 | 180 | 4.0% |
| 2025-12-10 23:00:00:00 | 189 | 4.2% |
| 2025-12-11 00:00:00:00 | 247 | 5.5% |
| 2025-12-11 01:00:00:00 | 180 | 4.0% |
| 2025-12-11 02:00:00:00 | 180 | 4.0% |
| 2025-12-11 03:00:00:00 | 192 | 4.3% |
| 2025-12-11 04:00:00:00 | 180 | 4.0% |
| 2025-12-11 05:00:00:00 | 180 | 4.0% |
| 2025-12-11 06:00:00:00 | 180 | 4.0% |
| 2025-12-11 07:00:00:00 | 180 | 4.0% |
| 2025-12-11 08:00:00:00 | 180 | 4.0% |
| 2025-12-11 09:00:00:00 | 199 | 4.4% |
| 2025-12-11 10:00:00:00 | 196 | 4.4% |
| 2025-12-11 11:00:00:00 | 197 | 4.4% |
| 2025-12-11 12:00:00:00 | 181 | 4.0% |
| 2025-12-11 13:00:00:00 | 180 | 4.0% |
| 2025-12-11 14:00:00:00 | 189 | 4.2% |
| 2025-12-11 15:00:00:00 | 179 | 4.0% |
| 2025-12-11 16:00:00:00 | 182 | 4.1% |
| 2025-12-11 17:00:00:00 | 92 | 2.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `194.180.49.70` | 137 | 13.4% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 2 | `45.147.46.32` | 116 | 11.3% | Turkey / Istanbul / Beyoğlu / Hosting Dunyam Bilisim Teknolojileri Ticaret Limited Sirketi | No apparent signal |
| 3 | `147.229.8.240` | 110 | 10.8% | Czechia / South Moravian / Tišnov / VUTBR | No apparent signal |
| 4 | `46.31.77.187` | 103 | 10.1% | Türkiye / Istanbul / Beylikduzu / Hosting Dunyam Bilisim Teknolojileri Tic. Ltd. STI | No apparent signal |
| 5 | `185.241.206.91` | 81 | 7.9% | The Netherlands / North Holland / Amsterdam / ESTOXY OU | No apparent signal |
| 6 | `79.124.62.230` | 77 | 7.5% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 7 | `79.124.62.126` | 68 | 6.6% | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD | No apparent signal |
| 8 | `109.236.61.34` | 55 | 5.4% | The Netherlands / North Holland / Amsterdam / ColocationX Ltd | Hosting/Cloud (colo) |
| 9 | `151.101.218.73` | 53 | 5.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 10 | `185.91.127.107` | 45 | 4.4% | The Netherlands / Limburg / Eygelshoven / Tube VPS | No apparent signal |
| 11 | `103.99.170.132` | 43 | 4.2% | United States / California / San Jose / WIZ K K | No apparent signal |
| 12 | `208.68.7.148` | 42 | 4.1% | United States / New York / New York / Privacy Services | No apparent signal |
| 13 | `103.99.170.131` | 40 | 3.9% | United States / California / San Jose / WIZ K K | No apparent signal |
| 14 | `115.231.78.11` | 30 | 2.9% | China / Zhejiang / Hangzhou / Hangzhou Duchuang Keji Co., Ltd | No apparent signal |
| 15 | `129.132.30.218` | 23 | 2.2% | Switzerland / Zurich / Zurich / Swiss Federal Institute of Technology Zurich | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `109.236.61.34` | 55 | 50.9% | Hosting/Cloud (colo) | The Netherlands / North Holland / Amsterdam / ColocationX Ltd |
| 2 | `151.101.218.73` | 53 | 49.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source IPs](ufw_plots/ufw_top_ips.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
