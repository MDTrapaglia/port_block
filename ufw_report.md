# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 784
- Unique source IPs: 571
- Unique countries/cities (24h): 126
- Unique destination ports: 535

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `7680` | 49 | 6.2% |
| 2 | `23` | 30 | 3.8% |
| 3 | `22` | 13 | 1.7% |
| 4 | `16055` | 9 | 1.1% |
| 5 | `16524` | 8 | 1.0% |
| 6 | `3306` | 7 | 0.9% |
| 7 | `3389` | 7 | 0.9% |
| 8 | `8080` | 6 | 0.8% |
| 9 | `15677` | 6 | 0.8% |
| 10 | `53` | 6 | 0.8% |
| 11 | `44349` | 6 | 0.8% |
| 12 | `15672` | 6 | 0.8% |
| 13 | `5060` | 5 | 0.6% |
| 14 | `16118` | 5 | 0.6% |
| 15 | `1900` | 4 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 730 | 93.1% |
| 2 | `UDP` | 54 | 6.9% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.187` | 38 | 4.8% |
| 2 | `77.239.124.2` | 28 | 3.6% |
| 3 | `68.73.112.130` | 12 | 1.5% |
| 4 | `151.101.218.13` | 12 | 1.5% |
| 5 | `76.158.232.86` | 8 | 1.0% |
| 6 | `185.242.226.9` | 6 | 0.8% |
| 7 | `50.45.252.114` | 5 | 0.6% |
| 8 | `173.90.47.130` | 4 | 0.5% |
| 9 | `73.162.96.52` | 4 | 0.5% |
| 10 | `73.17.195.132` | 4 | 0.5% |
| 11 | `172.59.160.129` | 4 | 0.5% |
| 12 | `157.245.254.81` | 4 | 0.5% |
| 13 | `46.33.232.109` | 4 | 0.5% |
| 14 | `2.23.164.165` | 4 | 0.5% |
| 15 | `91.196.152.206` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 704 | 96.4% |
| 2 | `ACK+FIN+PSH` | 20 | 2.7% |
| 3 | `SYN+ECE+CWR` | 2 | 0.3% |
| 4 | `ACK+PSH` | 2 | 0.3% |
| 5 | `ACK+FIN` | 2 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 784 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `68.73.112.130` -> `7680` | 12 | 1.5% |
| 2 | `216.180.246.187` -> `16055` | 9 | 1.1% |
| 3 | `76.158.232.86` -> `7680` | 8 | 1.0% |
| 4 | `216.180.246.187` -> `16524` | 8 | 1.0% |
| 5 | `216.180.246.187` -> `15677` | 6 | 0.8% |
| 6 | `151.101.218.13` -> `44349` | 6 | 0.8% |
| 7 | `216.180.246.187` -> `15672` | 6 | 0.8% |
| 8 | `50.45.252.114` -> `7680` | 5 | 0.6% |
| 9 | `216.180.246.187` -> `16118` | 5 | 0.6% |
| 10 | `173.90.47.130` -> `7680` | 4 | 0.5% |
| 11 | `73.162.96.52` -> `7680` | 4 | 0.5% |
| 12 | `73.17.195.132` -> `7680` | 4 | 0.5% |
| 13 | `216.180.246.187` -> `18181` | 4 | 0.5% |
| 14 | `172.59.160.129` -> `7680` | 4 | 0.5% |
| 15 | `151.101.218.13` -> `44045` | 4 | 0.5% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-25 00:00:00:00 | 175 | 22.3% |
| 2026-10-25 01:00:00:00 | 193 | 24.6% |
| 2026-10-25 02:00:00:00 | 184 | 23.5% |
| 2026-10-25 03:00:00:00 | 186 | 23.7% |
| 2026-10-25 04:00:00:00 | 46 | 5.9% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 38 | 27.1% |
| 2 | Paris, France | 28 | 20.0% |
| 3 | Buenos Aires, Argentina | 16 | 11.4% |
| 4 | Raleigh, United States | 12 | 8.6% |
| 5 | Roseville, United States | 8 | 5.7% |
| 6 | San Jose, United States | 8 | 5.7% |
| 7 | Amsterdam, The Netherlands | 6 | 4.3% |
| 8 | Tigard, United States | 5 | 3.6% |
| 9 | Brecksville, United States | 4 | 2.9% |
| 10 | Boston, United States | 4 | 2.9% |
| 11 | North Bergen, United States | 4 | 2.9% |
| 12 | Mykolayiv, Ukraine | 4 | 2.9% |
| 13 | Roubaix, France | 3 | 2.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.187` | 38 | 27.1% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `77.239.124.2` | 28 | 20.0% | France / Île-de-France / Paris / RocketCloud | No apparent signal |
| 3 | `68.73.112.130` | 12 | 8.6% | United States / North Carolina / Raleigh / PPPoX Pool - Rback2 EHMIL | No apparent signal |
| 4 | `151.101.218.13` | 12 | 8.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `76.158.232.86` | 8 | 5.7% | United States / California / Roseville / Comcast Cable Communications, LLC | No apparent signal |
| 6 | `185.242.226.9` | 6 | 4.3% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 7 | `50.45.252.114` | 5 | 3.6% | United States / Oregon / Tigard / Ziply Fiber | No apparent signal |
| 8 | `173.90.47.130` | 4 | 2.9% | United States / Ohio / Brecksville / Spectrum | No apparent signal |
| 9 | `73.162.96.52` | 4 | 2.9% | United States / California / San Jose / Comcast IP Services, L.L.C. | No apparent signal |
| 10 | `73.17.195.132` | 4 | 2.9% | United States / Massachusetts / Boston / Comcast Cable Communications, LLC | No apparent signal |
| 11 | `172.59.160.129` | 4 | 2.9% | United States / California / San Jose / T-Mobile USA, Inc. | Mobile/CGNAT (mobile) |
| 12 | `157.245.254.81` | 4 | 2.9% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `46.33.232.109` | 4 | 2.9% | Ukraine / Mykolaiv / Mykolayiv / WildPark Co | No apparent signal |
| 14 | `2.23.164.165` | 4 | 2.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 15 | `91.196.152.206` | 3 | 2.1% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.187` | 38 | 65.5% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `151.101.218.13` | 12 | 20.7% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `157.245.254.81` | 4 | 6.9% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 4 | `2.23.164.165` | 4 | 6.9% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
