# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4317
- Unique source IPs: 2490
- Unique countries/cities (24h): 316
- Unique destination ports: 2257

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 183 | 4.2% |
| 2 | `22` | 104 | 2.4% |
| 3 | `853` | 72 | 1.7% |
| 4 | `8080` | 50 | 1.2% |
| 5 | `3389` | 47 | 1.1% |
| 6 | `5060` | 43 | 1.0% |
| 7 | `53` | 37 | 0.9% |
| 8 | `8443` | 29 | 0.7% |
| 9 | `1433` | 28 | 0.6% |
| 10 | `17000` | 28 | 0.6% |
| 11 | `6036` | 25 | 0.6% |
| 12 | `21` | 21 | 0.5% |
| 13 | `17001` | 20 | 0.5% |
| 14 | `25` | 19 | 0.4% |
| 15 | `6379` | 18 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3884 | 90.0% |
| 2 | `UDP` | 415 | 9.6% |
| 3 | `47` | 10 | 0.2% |
| 4 | `132` | 6 | 0.1% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.143` | 174 | 4.0% |
| 2 | `217.60.77.23` | 72 | 1.7% |
| 3 | `217.60.76.226` | 24 | 0.6% |
| 4 | `130.12.180.42` | 20 | 0.5% |
| 5 | `45.135.193.159` | 19 | 0.4% |
| 6 | `208.109.212.211` | 19 | 0.4% |
| 7 | `85.217.140.22` | 16 | 0.4% |
| 8 | `85.217.140.24` | 15 | 0.3% |
| 9 | `85.217.149.37` | 15 | 0.3% |
| 10 | `85.217.140.6` | 15 | 0.3% |
| 11 | `85.217.140.30` | 14 | 0.3% |
| 12 | `85.217.140.29` | 14 | 0.3% |
| 13 | `85.217.140.23` | 14 | 0.3% |
| 14 | `18.119.209.50` | 13 | 0.3% |
| 15 | `85.217.140.34` | 13 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3866 | 99.5% |
| 2 | `SYN+ECE+CWR` | 17 | 0.4% |
| 3 | `ACK+PSH` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4317 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `217.60.77.23` -> `853` | 71 | 1.6% |
| 2 | `208.109.212.211` -> `23` | 19 | 0.4% |
| 3 | `216.180.246.143` -> `4950` | 12 | 0.3% |
| 4 | `130.12.180.42` -> `1881` | 11 | 0.3% |
| 5 | `216.180.246.143` -> `4719` | 10 | 0.2% |
| 6 | `216.180.246.143` -> `4770` | 10 | 0.2% |
| 7 | `216.180.246.143` -> `5003` | 10 | 0.2% |
| 8 | `216.180.246.143` -> `5004` | 10 | 0.2% |
| 9 | `186.123.1.125` -> `1433` | 9 | 0.2% |
| 10 | `216.180.246.143` -> `4710` | 9 | 0.2% |
| 11 | `216.180.246.143` -> `5001` | 9 | 0.2% |
| 12 | `216.180.246.143` -> `4567` | 8 | 0.2% |
| 13 | `216.180.246.143` -> `4764` | 8 | 0.2% |
| 14 | `216.180.246.143` -> `4900` | 8 | 0.2% |
| 15 | `130.12.180.42` -> `1880` | 8 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-20 04:00:00:00 | 131 | 3.0% |
| 2026-09-20 05:00:00:00 | 180 | 4.2% |
| 2026-09-20 06:00:00:00 | 182 | 4.2% |
| 2026-09-20 07:00:00:00 | 181 | 4.2% |
| 2026-09-20 08:00:00:00 | 179 | 4.1% |
| 2026-09-20 09:00:00:00 | 177 | 4.1% |
| 2026-09-20 10:00:00:00 | 183 | 4.2% |
| 2026-09-20 11:00:00:00 | 179 | 4.1% |
| 2026-09-20 12:00:00:00 | 181 | 4.2% |
| 2026-09-20 13:00:00:00 | 179 | 4.1% |
| 2026-09-20 14:00:00:00 | 181 | 4.2% |
| 2026-09-20 15:00:00:00 | 181 | 4.2% |
| 2026-09-20 16:00:00:00 | 179 | 4.1% |
| 2026-09-20 17:00:00:00 | 181 | 4.2% |
| 2026-09-20 18:00:00:00 | 179 | 4.1% |
| 2026-09-20 19:00:00:00 | 181 | 4.2% |
| 2026-09-20 20:00:00:00 | 180 | 4.2% |
| 2026-09-20 21:00:00:00 | 180 | 4.2% |
| 2026-09-20 22:00:00:00 | 179 | 4.1% |
| 2026-09-20 23:00:00:00 | 181 | 4.2% |
| 2026-09-21 00:00:00:00 | 180 | 4.2% |
| 2026-09-21 01:00:00:00 | 180 | 4.2% |
| 2026-09-21 02:00:00:00 | 178 | 4.1% |
| 2026-09-21 03:00:00:00 | 181 | 4.2% |
| 2026-09-21 04:00:00:00 | 44 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 174 | 38.1% |
| 2 | Gravelines, France | 101 | 22.1% |
| 3 | London, United States | 72 | 15.8% |
| 4 | Eygelshoven, The Netherlands | 24 | 5.3% |
| 5 | Amsterdam, The Netherlands | 20 | 4.4% |
| 6 | Langen, Germany | 19 | 4.2% |
| 7 | Tempe, United States | 19 | 4.2% |
| 8 | Beauharnois, Canada | 15 | 3.3% |
| 9 | Dublin, United States | 13 | 2.8% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.143` | 174 | 38.1% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `217.60.77.23` | 72 | 15.8% | United States / Kentucky / London / Miteflux Technologies Ltd | No apparent signal |
| 3 | `217.60.76.226` | 24 | 5.3% | The Netherlands / Limburg / Eygelshoven / Iryna Ivanenko | No apparent signal |
| 4 | `130.12.180.42` | 20 | 4.4% | The Netherlands / North Holland / Amsterdam / Virtualine Technologies | No apparent signal |
| 5 | `45.135.193.159` | 19 | 4.2% | Germany / Hesse / Langen / Pfcloud UG | No apparent signal |
| 6 | `208.109.212.211` | 19 | 4.2% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 7 | `85.217.140.22` | 16 | 3.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `85.217.140.24` | 15 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 9 | `85.217.149.37` | 15 | 3.3% | Canada / Quebec / Beauharnois / Modat B.V | No apparent signal |
| 10 | `85.217.140.6` | 15 | 3.3% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 11 | `85.217.140.30` | 14 | 3.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.29` | 14 | 3.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `85.217.140.23` | 14 | 3.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 14 | `18.119.209.50` | 13 | 2.8% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `85.217.140.34` | 13 | 2.8% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.143` | 174 | 93.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `18.119.209.50` | 13 | 7.0% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
