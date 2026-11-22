# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 677
- Unique source IPs: 516
- Unique countries/cities (24h): 109
- Unique destination ports: 468

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 24 | 3.5% |
| 2 | `22` | 17 | 2.5% |
| 3 | `6503` | 8 | 1.2% |
| 4 | `6512` | 8 | 1.2% |
| 5 | `6666` | 7 | 1.0% |
| 6 | `3306` | 7 | 1.0% |
| 7 | `50758` | 6 | 0.9% |
| 8 | `53` | 6 | 0.9% |
| 9 | `6550` | 6 | 0.9% |
| 10 | `6667` | 6 | 0.9% |
| 11 | `61230` | 6 | 0.9% |
| 12 | `27017` | 5 | 0.7% |
| 13 | `8443` | 5 | 0.7% |
| 14 | `8080` | 5 | 0.7% |
| 15 | `5060` | 5 | 0.7% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 615 | 90.8% |
| 2 | `UDP` | 62 | 9.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.37` | 50 | 7.4% |
| 2 | `2.22.149.169` | 10 | 1.5% |
| 3 | `45.156.87.168` | 10 | 1.5% |
| 4 | `178.236.185.67` | 8 | 1.2% |
| 5 | `151.101.216.158` | 6 | 0.9% |
| 6 | `58.239.107.192` | 6 | 0.9% |
| 7 | `170.51.247.41` | 6 | 0.9% |
| 8 | `185.73.23.133` | 4 | 0.6% |
| 9 | `73.41.139.22` | 4 | 0.6% |
| 10 | `23.213.206.37` | 4 | 0.6% |
| 11 | `95.100.88.74` | 4 | 0.6% |
| 12 | `31.184.195.246` | 3 | 0.4% |
| 13 | `91.231.89.173` | 3 | 0.4% |
| 14 | `194.180.48.122` | 3 | 0.4% |
| 15 | `91.196.152.206` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 579 | 94.1% |
| 2 | `ACK+FIN+PSH` | 23 | 3.7% |
| 3 | `ACK+PSH` | 7 | 1.1% |
| 4 | `ACK+FIN` | 6 | 1.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 677 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.37` -> `6503` | 8 | 1.2% |
| 2 | `216.180.246.37` -> `6512` | 8 | 1.2% |
| 3 | `216.180.246.37` -> `6666` | 7 | 1.0% |
| 4 | `151.101.216.158` -> `50758` | 6 | 0.9% |
| 5 | `58.239.107.192` -> `23` | 6 | 0.9% |
| 6 | `216.180.246.37` -> `6550` | 6 | 0.9% |
| 7 | `216.180.246.37` -> `6667` | 6 | 0.9% |
| 8 | `170.51.247.41` -> `61230` | 6 | 0.9% |
| 9 | `216.180.246.37` -> `6610` | 4 | 0.6% |
| 10 | `216.180.246.37` -> `6677` | 4 | 0.6% |
| 11 | `216.180.246.37` -> `6697` | 4 | 0.6% |
| 12 | `23.213.206.37` -> `61276` | 4 | 0.6% |
| 13 | `95.100.88.74` -> `61400` | 4 | 0.6% |
| 14 | `216.180.246.37` -> `6500` | 2 | 0.3% |
| 15 | `54.37.61.97` -> `5100` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-22 00:00:00:00 | 67 | 9.9% |
| 2026-11-22 01:00:00:00 | 177 | 26.1% |
| 2026-11-22 02:00:00:00 | 182 | 26.9% |
| 2026-11-22 03:00:00:00 | 205 | 30.3% |
| 2026-11-22 04:00:00:00 | 46 | 6.8% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 50 | 40.3% |
| 2 | Buenos Aires, Argentina | 26 | 21.0% |
| 3 | Amsterdam, The Netherlands | 10 | 8.1% |
| 4 | Mumbai, India | 8 | 6.5% |
| 5 | Seoul, South Korea | 6 | 4.8% |
| 6 | Frankfurt am Main, Germany | 4 | 3.2% |
| 7 | Sacramento, United States | 4 | 3.2% |
| 8 | Miami, United States | 4 | 3.2% |
| 9 | St Petersburg, Russia | 3 | 2.4% |
| 10 | Gravelines, France | 3 | 2.4% |
| 11 | Berngau, Germany | 3 | 2.4% |
| 12 | Roubaix, France | 3 | 2.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.37` | 50 | 40.3% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `2.22.149.169` | 10 | 8.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 3 | `45.156.87.168` | 10 | 8.1% | The Netherlands / North Holland / Amsterdam / TechTies Inc | No apparent signal |
| 4 | `178.236.185.67` | 8 | 6.5% | India / Maharashtra / Mumbai / HIVELOCITY, Inc | Hosting/Cloud (hivelocity) |
| 5 | `151.101.216.158` | 6 | 4.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `58.239.107.192` | 6 | 4.8% | South Korea / Seoul / Seoul / broadNnet | No apparent signal |
| 7 | `170.51.247.41` | 6 | 4.8% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 8 | `185.73.23.133` | 4 | 3.2% | Germany / Hesse / Frankfurt am Main / RUB LIR Inet2 | No apparent signal |
| 9 | `73.41.139.22` | 4 | 3.2% | United States / California / Sacramento / Comcast IP Services, L.L.C. | No apparent signal |
| 10 | `23.213.206.37` | 4 | 3.2% | United States / Florida / Miami / Akamai Technologies, Inc. | CDN/Edge (akamai) |
| 11 | `95.100.88.74` | 4 | 3.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 12 | `31.184.195.246` | 3 | 2.4% | Russia / St.-Petersburg / St Petersburg / PIN DC | No apparent signal |
| 13 | `91.231.89.173` | 3 | 2.4% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `194.180.48.122` | 3 | 2.4% | Germany / Bavaria / Berngau / HostSlick | No apparent signal |
| 15 | `91.196.152.206` | 3 | 2.4% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.37` | 50 | 61.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `2.22.149.169` | 10 | 12.2% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 3 | `178.236.185.67` | 8 | 9.8% | Hosting/Cloud (hivelocity) | India / Maharashtra / Mumbai / HIVELOCITY, Inc |
| 4 | `151.101.216.158` | 6 | 7.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 5 | `23.213.206.37` | 4 | 4.9% | CDN/Edge (akamai) | United States / Florida / Miami / Akamai Technologies, Inc. |
| 6 | `95.100.88.74` | 4 | 4.9% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
