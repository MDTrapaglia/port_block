# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4321
- Unique source IPs: 2382
- Unique countries/cities (24h): 385
- Unique destination ports: 2707

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 184 | 4.3% |
| 2 | `22` | 82 | 1.9% |
| 3 | `8080` | 39 | 0.9% |
| 4 | `5060` | 35 | 0.8% |
| 5 | `53` | 34 | 0.8% |
| 6 | `3389` | 27 | 0.6% |
| 7 | `1433` | 27 | 0.6% |
| 8 | `123` | 21 | 0.5% |
| 9 | `8443` | 20 | 0.5% |
| 10 | `8081` | 19 | 0.4% |
| 11 | `161` | 17 | 0.4% |
| 12 | `5555` | 17 | 0.4% |
| 13 | `2222` | 16 | 0.4% |
| 14 | `25` | 16 | 0.4% |
| 15 | `8888` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3922 | 90.8% |
| 2 | `UDP` | 392 | 9.1% |
| 3 | `47` | 4 | 0.1% |
| 4 | `132` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `93.123.109.124` | 469 | 10.9% |
| 2 | `2.26.60.164` | 71 | 1.6% |
| 3 | `192.176.173.186` | 49 | 1.1% |
| 4 | `85.217.140.22` | 15 | 0.3% |
| 5 | `85.217.140.18` | 14 | 0.3% |
| 6 | `18.190.15.50` | 12 | 0.3% |
| 7 | `85.217.140.28` | 12 | 0.3% |
| 8 | `18.119.209.50` | 12 | 0.3% |
| 9 | `3.131.24.55` | 12 | 0.3% |
| 10 | `151.243.11.240` | 11 | 0.3% |
| 11 | `85.217.140.20` | 11 | 0.3% |
| 12 | `85.217.140.6` | 11 | 0.3% |
| 13 | `24.86.234.67` | 10 | 0.2% |
| 14 | `85.217.140.27` | 10 | 0.2% |
| 15 | `167.172.129.109` | 10 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3905 | 99.6% |
| 2 | `SYN+ECE+CWR` | 16 | 0.4% |
| 3 | `ACK+PSH` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4321 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `24.86.234.67` -> `8080` | 10 | 0.2% |
| 2 | `94.154.43.64` -> `123` | 6 | 0.1% |
| 3 | `172.110.223.179` -> `5060` | 6 | 0.1% |
| 4 | `77.239.124.127` -> `2323` | 5 | 0.1% |
| 5 | `201.153.79.49` -> `22` | 5 | 0.1% |
| 6 | `207.175.28.61` -> `6379` | 5 | 0.1% |
| 7 | `194.164.29.150` -> `60001` | 5 | 0.1% |
| 8 | `66.132.172.203` -> `8028` | 4 | 0.1% |
| 9 | `69.17.52.1` -> `8333` | 4 | 0.1% |
| 10 | `180.93.250.126` -> `10348` | 3 | 0.1% |
| 11 | `77.239.124.127` -> `60001` | 3 | 0.1% |
| 12 | `77.90.185.226` -> `4000` | 3 | 0.1% |
| 13 | `85.11.167.132` -> `8081` | 3 | 0.1% |
| 14 | `51.81.123.140` -> `5060` | 3 | 0.1% |
| 15 | `89.42.231.200` -> `6036` | 3 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-08-31 04:00:00:00 | 132 | 3.1% |
| 2026-08-31 05:00:00:00 | 183 | 4.2% |
| 2026-08-31 06:00:00:00 | 178 | 4.1% |
| 2026-08-31 07:00:00:00 | 181 | 4.2% |
| 2026-08-31 08:00:00:00 | 179 | 4.1% |
| 2026-08-31 09:00:00:00 | 181 | 4.2% |
| 2026-08-31 10:00:00:00 | 181 | 4.2% |
| 2026-08-31 11:00:00:00 | 180 | 4.2% |
| 2026-08-31 12:00:00:00 | 180 | 4.2% |
| 2026-08-31 13:00:00:00 | 180 | 4.2% |
| 2026-08-31 14:00:00:00 | 180 | 4.2% |
| 2026-08-31 15:00:00:00 | 181 | 4.2% |
| 2026-08-31 16:00:00:00 | 178 | 4.1% |
| 2026-08-31 17:00:00:00 | 180 | 4.2% |
| 2026-08-31 18:00:00:00 | 180 | 4.2% |
| 2026-08-31 19:00:00:00 | 181 | 4.2% |
| 2026-08-31 20:00:00:00 | 180 | 4.2% |
| 2026-08-31 21:00:00:00 | 180 | 4.2% |
| 2026-08-31 22:00:00:00 | 180 | 4.2% |
| 2026-08-31 23:00:00:00 | 180 | 4.2% |
| 2026-09-01 00:00:00:00 | 178 | 4.1% |
| 2026-09-01 01:00:00:00 | 183 | 4.2% |
| 2026-09-01 02:00:00:00 | 180 | 4.2% |
| 2026-09-01 03:00:00:00 | 177 | 4.1% |
| 2026-09-01 04:00:00:00 | 47 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Andorra la Vella, Andorra | 469 | 64.3% |
| 2 | Frankfurt am Main, Germany | 82 | 11.2% |
| 3 | Gravelines, France | 73 | 10.0% |
| 4 | Helsingborg, Sweden | 49 | 6.7% |
| 5 | Dublin, United States | 36 | 4.9% |
| 6 | Surrey, Canada | 10 | 1.4% |
| 7 | North Bergen, United States | 10 | 1.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `93.123.109.124` | 469 | 64.3% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 2 | `2.26.60.164` | 71 | 9.7% | Germany / Hesse / Frankfurt am Main / Xorek.Cloud Frankfurt | No apparent signal |
| 3 | `192.176.173.186` | 49 | 6.7% | Sweden / Skåne County / Helsingborg / Kepler Technologies AB | No apparent signal |
| 4 | `85.217.140.22` | 15 | 2.1% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 5 | `85.217.140.18` | 14 | 1.9% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 6 | `18.190.15.50` | 12 | 1.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `85.217.140.28` | 12 | 1.6% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 8 | `18.119.209.50` | 12 | 1.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 9 | `3.131.24.55` | 12 | 1.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `151.243.11.240` | 11 | 1.5% | Germany / Hesse / Frankfurt am Main / Private Customer | No apparent signal |
| 11 | `85.217.140.20` | 11 | 1.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 12 | `85.217.140.6` | 11 | 1.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `24.86.234.67` | 10 | 1.4% | Canada / British Columbia / Surrey / Shaw Communications Inc. | No apparent signal |
| 14 | `85.217.140.27` | 10 | 1.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 15 | `167.172.129.109` | 10 | 1.4% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `18.190.15.50` | 12 | 26.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 2 | `18.119.209.50` | 12 | 26.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 3 | `3.131.24.55` | 12 | 26.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 4 | `167.172.129.109` | 10 | 21.7% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
