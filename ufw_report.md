# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4320
- Unique source IPs: 2517
- Unique countries/cities (24h): 298
- Unique destination ports: 2393

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 107 | 2.5% |
| 2 | `22` | 85 | 2.0% |
| 3 | `8080` | 48 | 1.1% |
| 4 | `5060` | 44 | 1.0% |
| 5 | `53` | 35 | 0.8% |
| 6 | `3389` | 34 | 0.8% |
| 7 | `9034` | 26 | 0.6% |
| 8 | `8443` | 24 | 0.6% |
| 9 | `161` | 21 | 0.5% |
| 10 | `3306` | 19 | 0.4% |
| 11 | `21` | 19 | 0.4% |
| 12 | `123` | 18 | 0.4% |
| 13 | `389` | 17 | 0.4% |
| 14 | `993` | 17 | 0.4% |
| 15 | `2222` | 16 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3981 | 92.2% |
| 2 | `UDP` | 328 | 7.6% |
| 3 | `47` | 6 | 0.1% |
| 4 | `132` | 4 | 0.1% |
| 5 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `62.210.142.179` | 144 | 3.3% |
| 2 | `195.178.110.92` | 24 | 0.6% |
| 3 | `195.178.110.89` | 20 | 0.5% |
| 4 | `68.183.28.69` | 20 | 0.5% |
| 5 | `45.198.224.125` | 15 | 0.3% |
| 6 | `91.231.89.117` | 14 | 0.3% |
| 7 | `45.77.61.56` | 14 | 0.3% |
| 8 | `3.83.245.221` | 13 | 0.3% |
| 9 | `91.231.89.238` | 13 | 0.3% |
| 10 | `195.184.76.220` | 12 | 0.3% |
| 11 | `91.230.168.142` | 12 | 0.3% |
| 12 | `195.184.76.62` | 12 | 0.3% |
| 13 | `18.221.179.104` | 12 | 0.3% |
| 14 | `185.242.226.90` | 12 | 0.3% |
| 15 | `91.230.168.252` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3976 | 99.9% |
| 2 | `SYN+ECE+CWR` | 2 | 0.1% |
| 3 | `ACK` | 2 | 0.1% |
| 4 | `ACK+PSH` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4320 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `91.224.92.45` -> `34567` | 9 | 0.2% |
| 2 | `154.80.128.163` -> `17000` | 9 | 0.2% |
| 3 | `62.210.142.179` -> `39868` | 8 | 0.2% |
| 4 | `62.210.142.179` -> `40205` | 8 | 0.2% |
| 5 | `62.210.114.99` -> `3389` | 7 | 0.2% |
| 6 | `45.198.224.125` -> `9090` | 7 | 0.2% |
| 7 | `62.210.142.179` -> `45003` | 7 | 0.2% |
| 8 | `62.210.142.179` -> `40000` | 6 | 0.1% |
| 9 | `62.210.142.179` -> `40202` | 6 | 0.1% |
| 10 | `62.210.142.179` -> `41800` | 6 | 0.1% |
| 11 | `62.210.142.179` -> `44300` | 6 | 0.1% |
| 12 | `62.210.142.179` -> `45000` | 6 | 0.1% |
| 13 | `62.210.142.179` -> `45057` | 6 | 0.1% |
| 14 | `118.212.132.226` -> `22` | 5 | 0.1% |
| 15 | `45.198.224.125` -> `8080` | 5 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-09 04:00:00:00 | 135 | 3.1% |
| 2026-11-09 05:00:00:00 | 179 | 4.1% |
| 2026-11-09 06:00:00:00 | 181 | 4.2% |
| 2026-11-09 07:00:00:00 | 178 | 4.1% |
| 2026-11-09 08:00:00:00 | 182 | 4.2% |
| 2026-11-09 09:00:00:00 | 179 | 4.1% |
| 2026-11-09 10:00:00:00 | 180 | 4.2% |
| 2026-11-09 11:00:00:00 | 179 | 4.1% |
| 2026-11-09 12:00:00:00 | 182 | 4.2% |
| 2026-11-09 13:00:00:00 | 179 | 4.1% |
| 2026-11-09 14:00:00:00 | 181 | 4.2% |
| 2026-11-09 15:00:00:00 | 180 | 4.2% |
| 2026-11-09 16:00:00:00 | 179 | 4.1% |
| 2026-11-09 17:00:00:00 | 181 | 4.2% |
| 2026-11-09 18:00:00:00 | 179 | 4.1% |
| 2026-11-09 19:00:00:00 | 181 | 4.2% |
| 2026-11-09 20:00:00:00 | 180 | 4.2% |
| 2026-11-09 21:00:00:00 | 180 | 4.2% |
| 2026-11-09 22:00:00:00 | 178 | 4.1% |
| 2026-11-09 23:00:00:00 | 181 | 4.2% |
| 2026-11-10 00:00:00:00 | 181 | 4.2% |
| 2026-11-10 01:00:00:00 | 180 | 4.2% |
| 2026-11-10 02:00:00:00 | 179 | 4.1% |
| 2026-11-10 03:00:00:00 | 181 | 4.2% |
| 2026-11-10 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Paris, France | 144 | 41.3% |
| 2 | Andorra la Vella, Andorra | 44 | 12.6% |
| 3 | Gravelines, France | 27 | 7.7% |
| 4 | Warrenton, United States | 24 | 6.9% |
| 5 | Hillsboro, United States | 24 | 6.9% |
| 6 | North Bergen, United States | 20 | 5.7% |
| 7 | Stockholm, Sweden | 15 | 4.3% |
| 8 | Aubervilliers, France | 14 | 4.0% |
| 9 | Ashburn, United States | 13 | 3.7% |
| 10 | Dublin, United States | 12 | 3.4% |
| 11 | Amsterdam, The Netherlands | 12 | 3.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.179` | 144 | 41.3% | France / Île-de-France / Paris / ONLINE | Hosting/Cloud (scaleway) |
| 2 | `195.178.110.92` | 24 | 6.9% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 3 | `195.178.110.89` | 20 | 5.7% | Andorra / Andorra la Vella / Andorra la Vella / Techoff SRV Limited | No apparent signal |
| 4 | `68.183.28.69` | 20 | 5.7% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `45.198.224.125` | 15 | 4.3% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 6 | `91.231.89.117` | 14 | 4.0% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 7 | `45.77.61.56` | 14 | 4.0% | France / Île-de-France / Aubervilliers / Vultr Holdings, LLC | Hosting/Cloud (vultr) |
| 8 | `3.83.245.221` | 13 | 3.7% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 9 | `91.231.89.238` | 13 | 3.7% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 10 | `195.184.76.220` | 12 | 3.4% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 11 | `91.230.168.142` | 12 | 3.4% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 12 | `195.184.76.62` | 12 | 3.4% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 13 | `18.221.179.104` | 12 | 3.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 14 | `185.242.226.90` | 12 | 3.4% | The Netherlands / North Holland / Amsterdam / AI Spera | No apparent signal |
| 15 | `91.230.168.252` | 12 | 3.4% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `62.210.142.179` | 144 | 70.9% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / ONLINE |
| 2 | `68.183.28.69` | 20 | 9.9% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 3 | `45.77.61.56` | 14 | 6.9% | Hosting/Cloud (vultr) | France / Île-de-France / Aubervilliers / Vultr Holdings, LLC |
| 4 | `3.83.245.221` | 13 | 6.4% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `18.221.179.104` | 12 | 5.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
