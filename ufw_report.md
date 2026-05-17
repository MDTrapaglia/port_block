# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 608
- Unique source IPs: 503
- Unique countries/cities (24h): 140
- Unique destination ports: 423

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `27015` | 33 | 5.4% |
| 2 | `23` | 30 | 4.9% |
| 3 | `8080` | 12 | 2.0% |
| 4 | `1723` | 10 | 1.6% |
| 5 | `45004` | 7 | 1.2% |
| 6 | `3389` | 6 | 1.0% |
| 7 | `22` | 6 | 1.0% |
| 8 | `60006` | 6 | 1.0% |
| 9 | `8082` | 4 | 0.7% |
| 10 | `1433` | 4 | 0.7% |
| 11 | `27017` | 4 | 0.7% |
| 12 | `8081` | 4 | 0.7% |
| 13 | `35193` | 4 | 0.7% |
| 14 | `50106` | 4 | 0.7% |
| 15 | `82` | 3 | 0.5% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 510 | 83.9% |
| 2 | `UDP` | 96 | 15.8% |
| 3 | `4` | 1 | 0.2% |
| 4 | `47` | 1 | 0.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.73` | 31 | 5.1% |
| 2 | `198.199.75.230` | 12 | 2.0% |
| 3 | `43.228.157.8` | 4 | 0.7% |
| 4 | `193.70.84.26` | 4 | 0.7% |
| 5 | `74.241.240.74` | 3 | 0.5% |
| 6 | `46.149.191.249` | 3 | 0.5% |
| 7 | `185.224.128.16` | 3 | 0.5% |
| 8 | `34.197.70.90` | 3 | 0.5% |
| 9 | `18.119.209.50` | 3 | 0.5% |
| 10 | `3.142.170.60` | 3 | 0.5% |
| 11 | `3.83.245.221` | 3 | 0.5% |
| 12 | `71.6.134.230` | 3 | 0.5% |
| 13 | `72.255.32.67` | 3 | 0.5% |
| 14 | `5.61.209.33` | 3 | 0.5% |
| 15 | `91.224.92.118` | 3 | 0.5% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 510 | 100.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 608 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `198.199.75.230` -> `23` | 12 | 2.0% |
| 2 | `216.180.246.73` -> `1723` | 10 | 1.6% |
| 3 | `216.180.246.73` -> `45004` | 7 | 1.2% |
| 4 | `216.180.246.73` -> `60006` | 6 | 1.0% |
| 5 | `193.70.84.26` -> `23` | 4 | 0.7% |
| 6 | `216.180.246.73` -> `35193` | 4 | 0.7% |
| 7 | `216.180.246.73` -> `50106` | 4 | 0.7% |
| 8 | `72.255.32.67` -> `8080` | 3 | 0.5% |
| 9 | `5.61.209.33` -> `8080` | 3 | 0.5% |
| 10 | `154.0.30.137` -> `3389` | 2 | 0.3% |
| 11 | `105.158.38.171` -> `23` | 2 | 0.3% |
| 12 | `185.242.3.226` -> `259` | 2 | 0.3% |
| 13 | `118.71.66.65` -> `27015` | 2 | 0.3% |
| 14 | `34.53.152.168` -> `21` | 2 | 0.3% |
| 15 | `141.98.83.48` -> `3283` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-05-17 00:00:00:00 | 21 | 3.5% |
| 2026-05-17 01:00:00:00 | 182 | 29.9% |
| 2026-05-17 02:00:00:00 | 180 | 29.6% |
| 2026-05-17 03:00:00:00 | 180 | 29.6% |
| 2026-05-17 04:00:00:00 | 45 | 7.4% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 31 | 36.9% |
| 2 | North Bergen, United States | 12 | 14.3% |
| 3 | Amsterdam, The Netherlands | 6 | 7.1% |
| 4 | Ashburn, United States | 6 | 7.1% |
| 5 | Dublin, United States | 6 | 7.1% |
| 6 | Singapore, Singapore | 4 | 4.8% |
| 7 | Roubaix, France | 4 | 4.8% |
| 8 | Gävle, Sweden | 3 | 3.6% |
| 9 | Kalush, Ukraine | 3 | 3.6% |
| 10 | Las Vegas, United States | 3 | 3.6% |
| 11 | Lahore, Pakistan | 3 | 3.6% |
| 12 | Vilnius, Lithuania | 3 | 3.6% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.73` | 31 | 36.9% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `198.199.75.230` | 12 | 14.3% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 3 | `43.228.157.8` | 4 | 4.8% | Singapore / North West / Singapore / Gaditek Associates | No apparent signal |
| 4 | `193.70.84.26` | 4 | 4.8% | France / Hauts-de-France / Roubaix / OVH | Hosting/Cloud (ovh) |
| 5 | `74.241.240.74` | 3 | 3.6% | Sweden / Gävleborg County / Gävle / Microsoft Azure Cloud (swedencentral) | Hosting/Cloud (azure) |
| 6 | `46.149.191.249` | 3 | 3.6% | Ukraine / Ivano-Frankivsk Oblast / Kalush / Kalush Information Network LTD | No apparent signal |
| 7 | `185.224.128.16` | 3 | 3.6% | The Netherlands / North Holland / Amsterdam / Alsycon B.V | No apparent signal |
| 8 | `34.197.70.90` | 3 | 3.6% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 9 | `18.119.209.50` | 3 | 3.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `3.142.170.60` | 3 | 3.6% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 11 | `3.83.245.221` | 3 | 3.6% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 12 | `71.6.134.230` | 3 | 3.6% | United States / Nevada / Las Vegas / CariNet, Inc. | No apparent signal |
| 13 | `72.255.32.67` | 3 | 3.6% | Pakistan / Punjab / Lahore / Cyber Internet Services Pakistan | No apparent signal |
| 14 | `5.61.209.33` | 3 | 3.6% | The Netherlands / North Holland / Amsterdam / Amarutu Technology Ltd. Network | No apparent signal |
| 15 | `91.224.92.118` | 3 | 3.6% | Lithuania / Vilnius / Vilnius / UAB Host Baltic | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.73` | 31 | 50.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `198.199.75.230` | 12 | 19.4% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 3 | `193.70.84.26` | 4 | 6.5% | Hosting/Cloud (ovh) | France / Hauts-de-France / Roubaix / OVH |
| 4 | `74.241.240.74` | 3 | 4.8% | Hosting/Cloud (azure) | Sweden / Gävleborg County / Gävle / Microsoft Azure Cloud (swedencentral) |
| 5 | `34.197.70.90` | 3 | 4.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 6 | `18.119.209.50` | 3 | 4.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `3.142.170.60` | 3 | 4.8% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 8 | `3.83.245.221` | 3 | 4.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
