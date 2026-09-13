# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 699
- Unique source IPs: 529
- Unique countries/cities (24h): 121
- Unique destination ports: 533

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 21 | 3.0% |
| 2 | `22` | 10 | 1.4% |
| 3 | `25650` | 10 | 1.4% |
| 4 | `25463` | 9 | 1.3% |
| 5 | `3389` | 8 | 1.1% |
| 6 | `2000` | 7 | 1.0% |
| 7 | `123` | 7 | 1.0% |
| 8 | `42555` | 7 | 1.0% |
| 9 | `5060` | 6 | 0.9% |
| 10 | `8443` | 6 | 0.9% |
| 11 | `3306` | 5 | 0.7% |
| 12 | `1433` | 5 | 0.7% |
| 13 | `389` | 5 | 0.7% |
| 14 | `65322` | 5 | 0.7% |
| 15 | `3232` | 5 | 0.7% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 625 | 89.4% |
| 2 | `UDP` | 72 | 10.3% |
| 3 | `47` | 2 | 0.3% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.54` | 30 | 4.3% |
| 2 | `5.252.101.22` | 28 | 4.0% |
| 3 | `176.65.148.6` | 9 | 1.3% |
| 4 | `151.101.218.73` | 7 | 1.0% |
| 5 | `185.242.226.8` | 6 | 0.9% |
| 6 | `151.101.218.13` | 5 | 0.7% |
| 7 | `85.217.149.37` | 4 | 0.6% |
| 8 | `85.217.140.28` | 4 | 0.6% |
| 9 | `85.217.140.18` | 4 | 0.6% |
| 10 | `85.217.140.33` | 4 | 0.6% |
| 11 | `85.217.140.34` | 4 | 0.6% |
| 12 | `85.217.140.7` | 3 | 0.4% |
| 13 | `3.131.24.55` | 3 | 0.4% |
| 14 | `85.217.140.6` | 3 | 0.4% |
| 15 | `18.119.209.50` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 600 | 96.0% |
| 2 | `ACK+FIN+PSH` | 14 | 2.2% |
| 3 | `ACK+PSH` | 7 | 1.1% |
| 4 | `SYN+ECE+CWR` | 3 | 0.5% |
| 5 | `ACK+FIN` | 1 | 0.2% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 699 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.54` -> `25650` | 10 | 1.4% |
| 2 | `216.180.246.54` -> `25463` | 9 | 1.3% |
| 3 | `151.101.218.73` -> `42555` | 7 | 1.0% |
| 4 | `151.101.218.13` -> `65322` | 5 | 0.7% |
| 5 | `216.180.246.54` -> `25500` | 4 | 0.6% |
| 6 | `216.180.246.54` -> `25471` | 3 | 0.4% |
| 7 | `216.180.246.54` -> `25565` | 3 | 0.4% |
| 8 | `180.93.245.203` -> `11` | 3 | 0.4% |
| 9 | `54.163.40.36` -> `3232` | 3 | 0.4% |
| 10 | `107.23.137.152` -> `3389` | 3 | 0.4% |
| 11 | `193.90.12.122` -> `23` | 2 | 0.3% |
| 12 | `185.169.4.236` -> `25` | 2 | 0.3% |
| 13 | `35.189.218.93` -> `3306` | 2 | 0.3% |
| 14 | `159.100.13.116` -> `3389` | 2 | 0.3% |
| 15 | `66.132.172.209` -> `2000` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-13 00:00:00:00 | 97 | 13.9% |
| 2026-09-13 01:00:00:00 | 183 | 26.2% |
| 2026-09-13 02:00:00:00 | 192 | 27.5% |
| 2026-09-13 03:00:00:00 | 183 | 26.2% |
| 2026-09-13 04:00:00:00 | 44 | 6.3% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 30 | 25.6% |
| 2 | Frankfurt am Main, Germany | 28 | 23.9% |
| 3 | Gravelines, France | 22 | 18.8% |
| 4 | Eygelshoven, The Netherlands | 9 | 7.7% |
| 5 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 7 | 6.0% |
| 6 | Amsterdam, The Netherlands | 6 | 5.1% |
| 7 | Dublin, United States | 6 | 5.1% |
| 8 | Buenos Aires, Argentina | 5 | 4.3% |
| 9 | Beauharnois, Canada | 4 | 3.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.54` | 30 | 25.6% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `5.252.101.22` | 28 | 23.9% | Germany / Hesse / Frankfurt am Main / Mo's Operations GmbH | No apparent signal |
| 3 | `176.65.148.6` | 9 | 7.7% | The Netherlands / Limburg / Eygelshoven / Pfcloud UG | No apparent signal |
| 4 | `151.101.218.73` | 7 | 6.0% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 5 | `185.242.226.8` | 6 | 5.1% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 6 | `151.101.218.13` | 5 | 4.3% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `85.217.149.37` | 4 | 3.4% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 8 | `85.217.140.28` | 4 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.140.18` | 4 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `85.217.140.33` | 4 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.34` | 4 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.7` | 3 | 2.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `3.131.24.55` | 3 | 2.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `85.217.140.6` | 3 | 2.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `18.119.209.50` | 3 | 2.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.54` | 30 | 62.5% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `151.101.218.73` | 7 | 14.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `151.101.218.13` | 5 | 10.4% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `3.131.24.55` | 3 | 6.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `18.119.209.50` | 3 | 6.2% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
