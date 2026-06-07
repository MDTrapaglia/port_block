# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 660
- Unique source IPs: 525
- Unique countries/cities (24h): 109
- Unique destination ports: 515

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 16 | 2.4% |
| 2 | `53` | 8 | 1.2% |
| 3 | `8080` | 7 | 1.1% |
| 4 | `22` | 6 | 0.9% |
| 5 | `5060` | 6 | 0.9% |
| 6 | `8443` | 6 | 0.9% |
| 7 | `5432` | 5 | 0.8% |
| 8 | `27017` | 5 | 0.8% |
| 9 | `5900` | 5 | 0.8% |
| 10 | `993` | 4 | 0.6% |
| 11 | `27015` | 4 | 0.6% |
| 12 | `88` | 4 | 0.6% |
| 13 | `9200` | 4 | 0.6% |
| 14 | `2375` | 4 | 0.6% |
| 15 | `1521` | 4 | 0.6% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 578 | 87.6% |
| 2 | `UDP` | 81 | 12.3% |
| 3 | `4` | 1 | 0.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `80.94.92.12` | 30 | 4.5% |
| 2 | `116.118.9.41` | 25 | 3.8% |
| 3 | `178.128.147.121` | 8 | 1.2% |
| 4 | `167.99.107.57` | 4 | 0.6% |
| 5 | `31.59.160.12` | 4 | 0.6% |
| 6 | `17.57.144.149` | 4 | 0.6% |
| 7 | `192.241.179.233` | 4 | 0.6% |
| 8 | `162.216.150.25` | 3 | 0.5% |
| 9 | `18.119.209.50` | 3 | 0.5% |
| 10 | `18.221.179.104` | 3 | 0.5% |
| 11 | `159.89.97.40` | 3 | 0.5% |
| 12 | `143.198.171.91` | 3 | 0.5% |
| 13 | `17.57.144.155` | 3 | 0.5% |
| 14 | `35.205.176.164` | 2 | 0.3% |
| 15 | `35.203.211.172` | 2 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 567 | 98.1% |
| 2 | `ACK+PSH` | 11 | 1.9% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 660 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `178.128.147.121` -> `23` | 8 | 1.2% |
| 2 | `192.241.179.233` -> `23` | 4 | 0.6% |
| 3 | `34.78.6.115` -> `990` | 2 | 0.3% |
| 4 | `159.89.97.40` -> `6000` | 2 | 0.3% |
| 5 | `17.57.144.153` -> `63597` | 2 | 0.3% |
| 6 | `17.57.144.149` -> `25041` | 2 | 0.3% |
| 7 | `172.110.223.185` -> `5060` | 2 | 0.3% |
| 8 | `107.22.131.209` -> `8443` | 2 | 0.3% |
| 9 | `17.57.144.149` -> `25121` | 2 | 0.3% |
| 10 | `18.212.56.204` -> `8443` | 2 | 0.3% |
| 11 | `54.89.180.28` -> `9200` | 2 | 0.3% |
| 12 | `17.57.144.155` -> `25125` | 2 | 0.3% |
| 13 | `34.227.22.208` -> `8080` | 2 | 0.3% |
| 14 | `205.210.31.193` -> `54041` | 1 | 0.2% |
| 15 | `45.33.52.85` -> `993` | 1 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-06-07 00:00:00:00 | 74 | 11.2% |
| 2026-06-07 01:00:00:00 | 179 | 27.1% |
| 2026-06-07 02:00:00:00 | 181 | 27.4% |
| 2026-06-07 03:00:00:00 | 180 | 27.3% |
| 2026-06-07 04:00:00:00 | 46 | 7.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Amsterdam, The Netherlands | 30 | 29.7% |
| 2 | Hanoi, Vietnam | 25 | 24.8% |
| 3 | North Bergen, United States | 11 | 10.9% |
| 4 | Cupertino, United States | 7 | 6.9% |
| 5 | Dublin, United States | 6 | 5.9% |
| 6 | Santa Clara, United States | 4 | 4.0% |
| 7 | Abu Dhabi, United Arab Emirates | 4 | 4.0% |
| 8 | Secaucus, United States | 4 | 4.0% |
| 9 | North Charleston, United States | 3 | 3.0% |
| 10 | Frankfurt am Main, Germany | 3 | 3.0% |
| 11 | Brussels, Belgium | 2 | 2.0% |
| 12 | London, United Kingdom | 2 | 2.0% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `80.94.92.12` | 30 | 29.7% | The Netherlands / North Holland / Amsterdam / Techoff SRV Limited | No apparent signal |
| 2 | `116.118.9.41` | 25 | 24.8% | Vietnam / Hanoi / Hanoi / SPT | No apparent signal |
| 3 | `178.128.147.121` | 8 | 7.9% | United States / New Jersey / North Bergen / Digitalocean | Hosting/Cloud (digitalocean) |
| 4 | `167.99.107.57` | 4 | 4.0% | United States / California / Santa Clara / Digital Ocean | Hosting/Cloud (digitalocean) |
| 5 | `31.59.160.12` | 4 | 4.0% | United Arab Emirates / Abu Dhabi / Abu Dhabi / GoldIPv4 | No apparent signal |
| 6 | `17.57.144.149` | 4 | 4.0% | United States / California / Cupertino / Apple Inc | No apparent signal |
| 7 | `192.241.179.233` | 4 | 4.0% | United States / New Jersey / Secaucus / Digital Ocean | Hosting/Cloud (digitalocean) |
| 8 | `162.216.150.25` | 3 | 3.0% | United States / South Carolina / North Charleston / Google Cloud (us-east1) | Hosting/Cloud (google cloud) |
| 9 | `18.119.209.50` | 3 | 3.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `18.221.179.104` | 3 | 3.0% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `159.89.97.40` | 3 | 3.0% | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 12 | `143.198.171.91` | 3 | 3.0% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 13 | `17.57.144.155` | 3 | 3.0% | United States / California / Cupertino / Apple Inc | No apparent signal |
| 14 | `35.205.176.164` | 2 | 2.0% | Belgium / Brussels Capital / Brussels / Google Cloud (europe-west1) | Hosting/Cloud (google cloud) |
| 15 | `35.203.211.172` | 2 | 2.0% | United Kingdom / England / London / Google Cloud (europe-west2) | Hosting/Cloud (google cloud) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `178.128.147.121` | 8 | 22.9% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / Digitalocean |
| 2 | `167.99.107.57` | 4 | 11.4% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / Digital Ocean |
| 3 | `192.241.179.233` | 4 | 11.4% | Hosting/Cloud (digitalocean) | United States / New Jersey / Secaucus / Digital Ocean |
| 4 | `162.216.150.25` | 3 | 8.6% | Hosting/Cloud (google cloud) | United States / South Carolina / North Charleston / Google Cloud (us-east1) |
| 5 | `18.119.209.50` | 3 | 8.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `18.221.179.104` | 3 | 8.6% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `159.89.97.40` | 3 | 8.6% | Hosting/Cloud (digitalocean) | Germany / Hesse / Frankfurt am Main / DigitalOcean, LLC |
| 8 | `143.198.171.91` | 3 | 8.6% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 9 | `35.205.176.164` | 2 | 5.7% | Hosting/Cloud (google cloud) | Belgium / Brussels Capital / Brussels / Google Cloud (europe-west1) |
| 10 | `35.203.211.172` | 2 | 5.7% | Hosting/Cloud (google cloud) | United Kingdom / England / London / Google Cloud (europe-west2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
