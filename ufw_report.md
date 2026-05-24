# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 740
- Unique source IPs: 594
- Unique countries/cities (24h): 164
- Unique destination ports: 535

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 85 | 11.5% |
| 2 | `27015` | 11 | 1.5% |
| 3 | `3389` | 9 | 1.2% |
| 4 | `53` | 7 | 0.9% |
| 5 | `43973` | 5 | 0.7% |
| 6 | `22022` | 5 | 0.7% |
| 7 | `22` | 5 | 0.7% |
| 8 | `8800` | 5 | 0.7% |
| 9 | `3224` | 5 | 0.7% |
| 10 | `8000` | 4 | 0.5% |
| 11 | `2087` | 4 | 0.5% |
| 12 | `8333` | 4 | 0.5% |
| 13 | `2000` | 4 | 0.5% |
| 14 | `5678` | 3 | 0.4% |
| 15 | `8888` | 3 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 672 | 90.8% |
| 2 | `UDP` | 68 | 9.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.114` | 19 | 2.6% |
| 2 | `165.22.105.175` | 12 | 1.6% |
| 3 | `132.148.131.176` | 11 | 1.5% |
| 4 | `85.217.149.35` | 8 | 1.1% |
| 5 | `85.217.149.20` | 8 | 1.1% |
| 6 | `151.101.218.73` | 7 | 0.9% |
| 7 | `85.217.149.48` | 7 | 0.9% |
| 8 | `85.217.149.42` | 6 | 0.8% |
| 9 | `85.217.149.43` | 5 | 0.7% |
| 10 | `85.217.149.47` | 5 | 0.7% |
| 11 | `178.20.210.182` | 4 | 0.5% |
| 12 | `85.217.149.17` | 4 | 0.5% |
| 13 | `138.226.239.22` | 3 | 0.4% |
| 14 | `18.217.208.51` | 3 | 0.4% |
| 15 | `147.185.133.201` | 3 | 0.4% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 657 | 97.8% |
| 2 | `ACK+PSH` | 8 | 1.2% |
| 3 | `ACK+FIN+PSH` | 7 | 1.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 740 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `165.22.105.175` -> `23` | 12 | 1.6% |
| 2 | `132.148.131.176` -> `23` | 11 | 1.5% |
| 3 | `151.101.218.73` -> `43973` | 5 | 0.7% |
| 4 | `216.180.246.114` -> `8800` | 5 | 0.7% |
| 5 | `216.180.246.114` -> `3224` | 5 | 0.7% |
| 6 | `216.180.246.114` -> `22022` | 4 | 0.5% |
| 7 | `69.17.52.1` -> `8333` | 3 | 0.4% |
| 8 | `176.65.148.172` -> `3389` | 3 | 0.4% |
| 9 | `142.250.0.188` -> `38480` | 3 | 0.4% |
| 10 | `151.101.218.73` -> `43807` | 2 | 0.3% |
| 11 | `187.21.16.111` -> `23` | 2 | 0.3% |
| 12 | `74.249.177.38` -> `2087` | 2 | 0.3% |
| 13 | `141.98.83.48` -> `53` | 2 | 0.3% |
| 14 | `216.180.246.114` -> `97` | 2 | 0.3% |
| 15 | `216.180.246.114` -> `8899` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-24 00:00:00:00 | 155 | 20.9% |
| 2026-05-24 01:00:00:00 | 179 | 24.2% |
| 2026-05-24 02:00:00:00 | 181 | 24.5% |
| 2026-05-24 03:00:00:00 | 177 | 23.9% |
| 2026-05-24 04:00:00:00 | 48 | 6.5% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Beauharnois, Canada | 26 | 24.8% |
| 2 | Massy, France | 19 | 18.1% |
| 3 | New York, United States | 17 | 16.2% |
| 4 | Singapore, Singapore | 12 | 11.4% |
| 5 | Tempe, United States | 11 | 10.5% |
| 6 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 7 | 6.7% |
| 7 | Būlaevo, Kazakhstan | 4 | 3.8% |
| 8 | Port Vila, Vanuatu | 3 | 2.9% |
| 9 | Dublin, United States | 3 | 2.9% |
| 10 | Santa Clara, United States | 3 | 2.9% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.114` | 19 | 18.1% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `165.22.105.175` | 12 | 11.4% | Singapore / South West / Singapore / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 3 | `132.148.131.176` | 11 | 10.5% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 4 | `85.217.149.35` | 8 | 7.6% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 5 | `85.217.149.20` | 8 | 7.6% | United States / New York / New York / Modat B.V | No apparent signal |
| 6 | `151.101.218.73` | 7 | 6.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `85.217.149.48` | 7 | 6.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 8 | `85.217.149.42` | 6 | 5.7% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 9 | `85.217.149.43` | 5 | 4.8% | United States / New York / New York / Modat B.V | No apparent signal |
| 10 | `85.217.149.47` | 5 | 4.8% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 11 | `178.20.210.182` | 4 | 3.8% | Kazakhstan / North Kazakhstan / Būlaevo / Shereverov network | No apparent signal |
| 12 | `85.217.149.17` | 4 | 3.8% | United States / New York / New York / Modat B.V | No apparent signal |
| 13 | `138.226.239.22` | 3 | 2.9% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 14 | `18.217.208.51` | 3 | 2.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `147.185.133.201` | 3 | 2.9% | United States / California / Santa Clara / Palo Alto Networks, Inc | Hosting/Cloud (google llc) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.114` | 19 | 43.2% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `165.22.105.175` | 12 | 27.3% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / DigitalOcean, LLC |
| 3 | `151.101.218.73` | 7 | 15.9% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `18.217.208.51` | 3 | 6.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 5 | `147.185.133.201` | 3 | 6.8% | Hosting/Cloud (google llc) | United States / California / Santa Clara / Palo Alto Networks, Inc |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
