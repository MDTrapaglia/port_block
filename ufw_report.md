# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 731
- Unique source IPs: 520
- Unique countries/cities (24h): 110
- Unique destination ports: 558

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 30 | 4.1% |
| 2 | `22` | 10 | 1.4% |
| 3 | `53` | 8 | 1.1% |
| 4 | `5060` | 8 | 1.1% |
| 5 | `48610` | 6 | 0.8% |
| 6 | `37076` | 6 | 0.8% |
| 7 | `8080` | 5 | 0.7% |
| 8 | `2222` | 4 | 0.5% |
| 9 | `1900` | 4 | 0.5% |
| 10 | `37476` | 4 | 0.5% |
| 11 | `17000` | 4 | 0.5% |
| 12 | `27017` | 4 | 0.5% |
| 13 | `3389` | 4 | 0.5% |
| 14 | `161` | 4 | 0.5% |
| 15 | `81` | 3 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 670 | 91.7% |
| 2 | `UDP` | 60 | 8.2% |
| 3 | `47` | 1 | 0.1% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `80.94.92.16` | 83 | 11.4% |
| 2 | `151.101.217.44` | 12 | 1.6% |
| 3 | `50.224.83.237` | 7 | 1.0% |
| 4 | `151.101.219.52` | 7 | 1.0% |
| 5 | `104.16.79.73` | 6 | 0.8% |
| 6 | `141.98.83.48` | 5 | 0.7% |
| 7 | `85.217.140.33` | 5 | 0.7% |
| 8 | `85.217.140.30` | 4 | 0.5% |
| 9 | `162.159.142.241` | 4 | 0.5% |
| 10 | `162.159.140.229` | 4 | 0.5% |
| 11 | `91.196.152.195` | 3 | 0.4% |
| 12 | `85.217.140.29` | 3 | 0.4% |
| 13 | `45.82.76.119` | 3 | 0.4% |
| 14 | `91.231.89.155` | 3 | 0.4% |
| 15 | `104.18.20.225` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 620 | 92.5% |
| 2 | `ACK+FIN+PSH` | 30 | 4.5% |
| 3 | `ACK+FIN` | 11 | 1.6% |
| 4 | `ACK+PSH` | 6 | 0.9% |
| 5 | `SYN+ECE+CWR` | 3 | 0.4% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 731 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `50.224.83.237` -> `23` | 7 | 1.0% |
| 2 | `151.101.217.44` -> `48610` | 6 | 0.8% |
| 3 | `151.101.217.44` -> `37076` | 6 | 0.8% |
| 4 | `162.159.140.229` -> `37476` | 4 | 0.5% |
| 5 | `151.101.219.52` -> `42864` | 3 | 0.4% |
| 6 | `162.159.142.241` -> `47782` | 3 | 0.4% |
| 7 | `104.18.20.225` -> `36142` | 3 | 0.4% |
| 8 | `45.205.1.163` -> `17000` | 3 | 0.4% |
| 9 | `104.16.79.73` -> `56500` | 3 | 0.4% |
| 10 | `104.16.80.73` -> `60882` | 3 | 0.4% |
| 11 | `104.16.79.73` -> `40516` | 3 | 0.4% |
| 12 | `66.132.159.24` -> `53` | 3 | 0.4% |
| 13 | `223.16.154.241` -> `23` | 2 | 0.3% |
| 14 | `91.224.92.28` -> `34568` | 2 | 0.3% |
| 15 | `83.233.22.225` -> `23` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-11 00:00:00:00 | 130 | 17.8% |
| 2026-10-11 01:00:00:00 | 200 | 27.4% |
| 2026-10-11 02:00:00:00 | 178 | 24.4% |
| 2026-10-11 03:00:00:00 | 182 | 24.9% |
| 2026-10-11 04:00:00:00 | 41 | 5.6% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 83 | 54.6% |
| 2 | Buenos Aires, Argentina | 19 | 12.5% |
| 3 | Toronto, Canada | 17 | 11.2% |
| 4 | Gravelines, France | 15 | 9.9% |
| 5 | Humble, United States | 7 | 4.6% |
| 6 | Panama City, Panama | 5 | 3.3% |
| 7 | Roubaix, France | 3 | 2.0% |
| 8 | London, United Kingdom | 3 | 2.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `80.94.92.16` | 83 | 54.6% | The Netherlands / North Holland / Amsterdam / Techoff SRV Limited | No apparent signal |
| 2 | `151.101.217.44` | 12 | 7.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 3 | `50.224.83.237` | 7 | 4.6% | United States / Texas / Humble / Comcast Cable Communications, LLC | No apparent signal |
| 4 | `151.101.219.52` | 7 | 4.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `104.16.79.73` | 6 | 3.9% | Canada / Ontario / Toronto / Cloudflare, Inc. | CDN/Edge (cloudflare) |
| 6 | `141.98.83.48` | 5 | 3.3% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 7 | `85.217.140.33` | 5 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.30` | 4 | 2.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `162.159.142.241` | 4 | 2.6% | Canada / Ontario / Toronto / Cloudflare, Inc. | CDN/Edge (cloudflare) |
| 10 | `162.159.140.229` | 4 | 2.6% | Canada / Ontario / Toronto / Cloudflare, Inc. | CDN/Edge (cloudflare) |
| 11 | `91.196.152.195` | 3 | 2.0% | France / Hauts-de-France / Roubaix / ONYPHE | No apparent signal |
| 12 | `85.217.140.29` | 3 | 2.0% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `45.82.76.119` | 3 | 2.0% | United Kingdom / England / London / Detai Prosperous Technologies Limited | No apparent signal |
| 14 | `91.231.89.155` | 3 | 2.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `104.18.20.225` | 3 | 2.0% | Canada / Ontario / Toronto / Cloudflare, Inc. | CDN/Edge (cloudflare) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `151.101.217.44` | 12 | 29.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 2 | `151.101.219.52` | 7 | 17.1% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `104.16.79.73` | 6 | 14.6% | CDN/Edge (cloudflare) | Canada / Ontario / Toronto / Cloudflare, Inc. |
| 4 | `141.98.83.48` | 5 | 12.2% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 5 | `162.159.142.241` | 4 | 9.8% | CDN/Edge (cloudflare) | Canada / Ontario / Toronto / Cloudflare, Inc. |
| 6 | `162.159.140.229` | 4 | 9.8% | CDN/Edge (cloudflare) | Canada / Ontario / Toronto / Cloudflare, Inc. |
| 7 | `104.18.20.225` | 3 | 7.3% | CDN/Edge (cloudflare) | Canada / Ontario / Toronto / Cloudflare, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
