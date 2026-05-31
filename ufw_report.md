# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 691
- Unique source IPs: 588
- Unique countries/cities (24h): 121
- Unique destination ports: 538

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `27015` | 10 | 1.4% |
| 2 | `23` | 9 | 1.3% |
| 3 | `22` | 8 | 1.2% |
| 4 | `2222` | 6 | 0.9% |
| 5 | `8082` | 6 | 0.9% |
| 6 | `63452` | 6 | 0.9% |
| 7 | `1433` | 5 | 0.7% |
| 8 | `8443` | 5 | 0.7% |
| 9 | `3389` | 5 | 0.7% |
| 10 | `5060` | 4 | 0.6% |
| 11 | `21` | 4 | 0.6% |
| 12 | `8090` | 4 | 0.6% |
| 13 | `8080` | 4 | 0.6% |
| 14 | `53` | 4 | 0.6% |
| 15 | `3306` | 4 | 0.6% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 611 | 88.4% |
| 2 | `UDP` | 80 | 11.6% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `170.51.247.42` | 12 | 1.7% |
| 2 | `2.22.149.138` | 5 | 0.7% |
| 3 | `194.164.107.6` | 4 | 0.6% |
| 4 | `199.45.155.82` | 4 | 0.6% |
| 5 | `71.6.134.235` | 3 | 0.4% |
| 6 | `193.163.125.106` | 3 | 0.4% |
| 7 | `5.187.35.142` | 3 | 0.4% |
| 8 | `18.190.15.50` | 3 | 0.4% |
| 9 | `77.91.71.66` | 3 | 0.4% |
| 10 | `17.57.144.155` | 3 | 0.4% |
| 11 | `205.210.31.237` | 3 | 0.4% |
| 12 | `34.197.70.90` | 3 | 0.4% |
| 13 | `18.221.179.104` | 3 | 0.4% |
| 14 | `147.185.132.255` | 3 | 0.4% |
| 15 | `207.90.244.17` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 587 | 96.1% |
| 2 | `ACK+FIN+PSH` | 13 | 2.1% |
| 3 | `ACK+PSH` | 9 | 1.5% |
| 4 | `ACK+FIN` | 2 | 0.3% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 691 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `170.51.247.42` -> `63452` | 6 | 0.9% |
| 2 | `199.45.155.82` -> `8000` | 4 | 0.6% |
| 3 | `2.22.149.138` -> `2715` | 3 | 0.4% |
| 4 | `17.57.144.155` -> `55256` | 3 | 0.4% |
| 5 | `170.51.247.42` -> `3727` | 3 | 0.4% |
| 6 | `71.6.134.235` -> `10161` | 2 | 0.3% |
| 7 | `2.22.149.138` -> `62492` | 2 | 0.3% |
| 8 | `15.204.234.74` -> `23` | 2 | 0.3% |
| 9 | `103.28.16.162` -> `22` | 2 | 0.3% |
| 10 | `115.86.73.98` -> `27015` | 2 | 0.3% |
| 11 | `71.6.134.230` -> `2123` | 2 | 0.3% |
| 12 | `170.51.247.42` -> `3729` | 2 | 0.3% |
| 13 | `66.132.195.51` -> `21` | 2 | 0.3% |
| 14 | `199.45.155.110` -> `8001` | 2 | 0.3% |
| 15 | `66.132.172.136` -> `554` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-31 00:00:00:00 | 93 | 13.5% |
| 2026-05-31 01:00:00:00 | 180 | 26.0% |
| 2026-05-31 02:00:00:00 | 193 | 27.9% |
| 2026-05-31 03:00:00:00 | 179 | 25.9% |
| 2026-05-31 04:00:00:00 | 46 | 6.7% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Buenos Aires, Argentina | 17 | 29.3% |
| 2 | Dublin, United States | 6 | 10.3% |
| 3 | Santa Clara, United States | 6 | 10.3% |
| 4 | Singapore, Singapore | 4 | 6.9% |
| 5 | Hong Kong, Hong Kong | 4 | 6.9% |
| 6 | Las Vegas, United States | 3 | 5.2% |
| 7 | Leeds, United Kingdom | 3 | 5.2% |
| 8 | Amsterdam, The Netherlands | 3 | 5.2% |
| 9 | Jerusalem, Israel | 3 | 5.2% |
| 10 | Cupertino, United States | 3 | 5.2% |
| 11 | Ashburn, United States | 3 | 5.2% |
| 12 | Pflugerville, United States | 3 | 5.2% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `170.51.247.42` | 12 | 20.7% | Argentina / Buenos Aires F.D. / Buenos Aires / AMX Argentina S.A | No apparent signal |
| 2 | `2.22.149.138` | 5 | 8.6% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 3 | `194.164.107.6` | 4 | 6.9% | Singapore / North West / Singapore / Valence Technology Co | No apparent signal |
| 4 | `199.45.155.82` | 4 | 6.9% | Hong Kong / Kowloon / Hong Kong / Censys, Inc. | No apparent signal |
| 5 | `71.6.134.235` | 3 | 5.2% | United States / Nevada / Las Vegas / CariNet, Inc. | No apparent signal |
| 6 | `193.163.125.106` | 3 | 5.2% | United Kingdom / England / Leeds / Constantine Cybersecurity LTD | No apparent signal |
| 7 | `5.187.35.142` | 3 | 5.2% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd | No apparent signal |
| 8 | `18.190.15.50` | 3 | 5.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `77.91.71.66` | 3 | 5.2% | Israel / Jerusalem / Jerusalem / Proline IT Ltd | No apparent signal |
| 10 | `17.57.144.155` | 3 | 5.2% | United States / California / Cupertino / Apple Inc | No apparent signal |
| 11 | `205.210.31.237` | 3 | 5.2% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |
| 12 | `34.197.70.90` | 3 | 5.2% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `18.221.179.104` | 3 | 5.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `147.185.132.255` | 3 | 5.2% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |
| 15 | `207.90.244.17` | 3 | 5.2% | United States / Texas / Pflugerville / SHODAN, LLC | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `2.22.149.138` | 5 | 25.0% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 2 | `18.190.15.50` | 3 | 15.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `205.210.31.237` | 3 | 15.0% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |
| 4 | `34.197.70.90` | 3 | 15.0% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `18.221.179.104` | 3 | 15.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `147.185.132.255` | 3 | 15.0% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
