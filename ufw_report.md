# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 186
- Unique source IPs: 84
- Unique countries/cities (24h): 34
- Unique destination ports: 105

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `50000` | 6 | 3.2% |
| 2 | `45269` | 4 | 2.2% |
| 3 | `45623` | 4 | 2.2% |
| 4 | `48396` | 4 | 2.2% |
| 5 | `36640` | 4 | 2.2% |
| 6 | `33647` | 4 | 2.2% |
| 7 | `56305` | 4 | 2.2% |
| 8 | `46555` | 4 | 2.2% |
| 9 | `57091` | 4 | 2.2% |
| 10 | `60568` | 4 | 2.2% |
| 11 | `50354` | 4 | 2.2% |
| 12 | `47801` | 4 | 2.2% |
| 13 | `51126` | 4 | 2.2% |
| 14 | `53831` | 4 | 2.2% |
| 15 | `35544` | 4 | 2.2% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `UDP` | 103 | 55.4% |
| 2 | `TCP` | 82 | 44.1% |
| 3 | `47` | 1 | 0.5% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.168.100.118` | 102 | 54.8% |
| 2 | `124.198.131.185` | 2 | 1.1% |
| 3 | `3.131.24.55` | 1 | 0.5% |
| 4 | `66.132.195.24` | 1 | 0.5% |
| 5 | `147.185.133.139` | 1 | 0.5% |
| 6 | `64.62.197.229` | 1 | 0.5% |
| 7 | `205.210.31.244` | 1 | 0.5% |
| 8 | `193.163.125.41` | 1 | 0.5% |
| 9 | `162.216.149.233` | 1 | 0.5% |
| 10 | `193.163.125.39` | 1 | 0.5% |
| 11 | `52.20.198.190` | 1 | 0.5% |
| 12 | `100.49.117.77` | 1 | 0.5% |
| 13 | `104.243.35.104` | 1 | 0.5% |
| 14 | `207.90.244.18` | 1 | 0.5% |
| 15 | `205.210.31.238` | 1 | 0.5% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 82 | 100.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `wlan0` | 102 | 54.8% |
| 2 | `eth0` | 84 | 45.2% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.168.100.118` -> `50000` | 6 | 3.2% |
| 2 | `192.168.100.118` -> `45269` | 4 | 2.2% |
| 3 | `192.168.100.118` -> `45623` | 4 | 2.2% |
| 4 | `192.168.100.118` -> `48396` | 4 | 2.2% |
| 5 | `192.168.100.118` -> `36640` | 4 | 2.2% |
| 6 | `192.168.100.118` -> `33647` | 4 | 2.2% |
| 7 | `192.168.100.118` -> `56305` | 4 | 2.2% |
| 8 | `192.168.100.118` -> `46555` | 4 | 2.2% |
| 9 | `192.168.100.118` -> `57091` | 4 | 2.2% |
| 10 | `192.168.100.118` -> `60568` | 4 | 2.2% |
| 11 | `192.168.100.118` -> `50354` | 4 | 2.2% |
| 12 | `192.168.100.118` -> `47801` | 4 | 2.2% |
| 13 | `192.168.100.118` -> `51126` | 4 | 2.2% |
| 14 | `192.168.100.118` -> `53831` | 4 | 2.2% |
| 15 | `192.168.100.118` -> `35544` | 4 | 2.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-03 00:00:00:00 | 104 | 55.9% |
| 2026-05-03 01:00:00:00 | 82 | 44.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | private | 102 | 87.2% |
| 2 | Santa Clara, United States | 3 | 2.6% |
| 3 | New York, United States | 2 | 1.7% |
| 4 | Leeds, United Kingdom | 2 | 1.7% |
| 5 | Ashburn, United States | 2 | 1.7% |
| 6 | Dublin, United States | 1 | 0.9% |
| 7 | Ann Arbor, United States | 1 | 0.9% |
| 8 | Pleasanton, United States | 1 | 0.9% |
| 9 | North Charleston, United States | 1 | 0.9% |
| 10 | Piscataway, United States | 1 | 0.9% |
| 11 | Pflugerville, United States | 1 | 0.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.168.100.118` | 102 | 87.2% | private | Private/CGNAT |
| 2 | `124.198.131.185` | 2 | 1.7% | United States / New York / New York / 1337 Services GmbH | No apparent signal |
| 3 | `3.131.24.55` | 1 | 0.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 4 | `66.132.195.24` | 1 | 0.9% | United States / Michigan / Ann Arbor / Censys, Inc. | No apparent signal |
| 5 | `147.185.133.139` | 1 | 0.9% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |
| 6 | `64.62.197.229` | 1 | 0.9% | United States / California / Pleasanton / The Shadowserver Foundation, Inc | No apparent signal |
| 7 | `205.210.31.244` | 1 | 0.9% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |
| 8 | `193.163.125.41` | 1 | 0.9% | United Kingdom / England / Leeds / Constantine Cybersecurity LTD | No apparent signal |
| 9 | `162.216.149.233` | 1 | 0.9% | United States / South Carolina / North Charleston / Google Cloud (us-east1) | Hosting/Cloud (google cloud) |
| 10 | `193.163.125.39` | 1 | 0.9% | United Kingdom / England / Leeds / Constantine Cybersecurity LTD | No apparent signal |
| 11 | `52.20.198.190` | 1 | 0.9% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 12 | `100.49.117.77` | 1 | 0.9% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 13 | `104.243.35.104` | 1 | 0.9% | United States / New Jersey / Piscataway / Matt Smith | No apparent signal |
| 14 | `207.90.244.18` | 1 | 0.9% | United States / Texas / Pflugerville / SHODAN, LLC | No apparent signal |
| 15 | `205.210.31.238` | 1 | 0.9% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `3.131.24.55` | 1 | 14.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 2 | `147.185.133.139` | 1 | 14.3% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |
| 3 | `205.210.31.244` | 1 | 14.3% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |
| 4 | `162.216.149.233` | 1 | 14.3% | Hosting/Cloud (google cloud) | United States / South Carolina / North Charleston / Google Cloud (us-east1) |
| 5 | `52.20.198.190` | 1 | 14.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 6 | `100.49.117.77` | 1 | 14.3% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 7 | `205.210.31.238` | 1 | 14.3% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
