# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4359
- Unique source IPs: 2949
- Unique countries/cities (24h): 451
- Unique destination ports: 2006

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 1275 | 29.2% |
| 2 | `22` | 47 | 1.1% |
| 3 | `53` | 39 | 0.9% |
| 4 | `8080` | 32 | 0.7% |
| 5 | `5060` | 31 | 0.7% |
| 6 | `8443` | 21 | 0.5% |
| 7 | `3389` | 19 | 0.4% |
| 8 | `500` | 15 | 0.3% |
| 9 | `2222` | 15 | 0.3% |
| 10 | `8081` | 14 | 0.3% |
| 11 | `1433` | 14 | 0.3% |
| 12 | `8000` | 13 | 0.3% |
| 13 | `3306` | 12 | 0.3% |
| 14 | `123` | 12 | 0.3% |
| 15 | `9200` | 12 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4082 | 93.6% |
| 2 | `UDP` | 271 | 6.2% |
| 3 | `132` | 3 | 0.1% |
| 4 | `47` | 2 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `192.158.226.31` | 55 | 1.3% |
| 2 | `104.237.132.58` | 44 | 1.0% |
| 3 | `45.33.12.231` | 38 | 0.9% |
| 4 | `139.177.206.6` | 16 | 0.4% |
| 5 | `104.248.127.214` | 12 | 0.3% |
| 6 | `3.131.24.55` | 11 | 0.3% |
| 7 | `45.33.96.214` | 11 | 0.3% |
| 8 | `2.22.149.145` | 11 | 0.3% |
| 9 | `3.147.122.184` | 10 | 0.2% |
| 10 | `2.22.149.137` | 10 | 0.2% |
| 11 | `100.49.117.77` | 9 | 0.2% |
| 12 | `91.230.168.129` | 8 | 0.2% |
| 13 | `195.184.76.198` | 8 | 0.2% |
| 14 | `18.217.208.51` | 8 | 0.2% |
| 15 | `3.15.230.87` | 8 | 0.2% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 4029 | 98.7% |
| 2 | `ACK+FIN+PSH` | 27 | 0.7% |
| 3 | `ACK+PSH` | 12 | 0.3% |
| 4 | `ACK+FIN` | 12 | 0.3% |
| 5 | `SYN+ECE+CWR` | 2 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4359 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `177.56.225.41` -> `23` | 8 | 0.2% |
| 2 | `2.22.149.145` -> `51798` | 7 | 0.2% |
| 3 | `66.132.172.188` -> `554` | 5 | 0.1% |
| 4 | `160.119.76.189` -> `5060` | 5 | 0.1% |
| 5 | `151.101.219.52` -> `54356` | 5 | 0.1% |
| 6 | `59.180.169.249` -> `23` | 5 | 0.1% |
| 7 | `179.199.134.236` -> `557` | 4 | 0.1% |
| 8 | `200.69.43.104` -> `23` | 4 | 0.1% |
| 9 | `151.243.11.230` -> `53` | 4 | 0.1% |
| 10 | `2.22.149.137` -> `53234` | 4 | 0.1% |
| 11 | `41.60.248.110` -> `23` | 4 | 0.1% |
| 12 | `66.132.172.101` -> `8443` | 4 | 0.1% |
| 13 | `66.132.195.253` -> `53` | 4 | 0.1% |
| 14 | `154.80.128.231` -> `1900` | 3 | 0.1% |
| 15 | `113.221.73.54` -> `23` | 3 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-24 04:00:00:00 | 135 | 3.1% |
| 2026-11-24 05:00:00:00 | 180 | 4.1% |
| 2026-11-24 06:00:00:00 | 180 | 4.1% |
| 2026-11-24 07:00:00:00 | 186 | 4.3% |
| 2026-11-24 08:00:00:00 | 180 | 4.1% |
| 2026-11-24 09:00:00:00 | 179 | 4.1% |
| 2026-11-24 10:00:00:00 | 190 | 4.4% |
| 2026-11-24 11:00:00:00 | 179 | 4.1% |
| 2026-11-24 12:00:00:00 | 182 | 4.2% |
| 2026-11-24 13:00:00:00 | 181 | 4.2% |
| 2026-11-24 14:00:00:00 | 181 | 4.2% |
| 2026-11-24 15:00:00:00 | 180 | 4.1% |
| 2026-11-24 16:00:00:00 | 190 | 4.4% |
| 2026-11-24 17:00:00:00 | 180 | 4.1% |
| 2026-11-24 18:00:00:00 | 180 | 4.1% |
| 2026-11-24 19:00:00:00 | 181 | 4.2% |
| 2026-11-24 20:00:00:00 | 190 | 4.4% |
| 2026-11-24 21:00:00:00 | 179 | 4.1% |
| 2026-11-24 22:00:00:00 | 181 | 4.2% |
| 2026-11-24 23:00:00:00 | 180 | 4.1% |
| 2026-11-25 00:00:00:00 | 180 | 4.1% |
| 2026-11-25 01:00:00:00 | 179 | 4.1% |
| 2026-11-25 02:00:00:00 | 180 | 4.1% |
| 2026-11-25 03:00:00:00 | 180 | 4.1% |
| 2026-11-25 04:00:00:00 | 46 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Richardson, United States | 82 | 31.7% |
| 2 | Charlotte, United States | 55 | 21.2% |
| 3 | Dublin, United States | 29 | 11.2% |
| 4 | Atlanta, United States | 27 | 10.4% |
| 5 | Buenos Aires, Argentina | 21 | 8.1% |
| 6 | North Bergen, United States | 12 | 4.6% |
| 7 | Ashburn, United States | 9 | 3.5% |
| 8 | Hillsboro, United States | 8 | 3.1% |
| 9 | Warrenton, United States | 8 | 3.1% |
| 10 | Columbus, United States | 8 | 3.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `192.158.226.31` | 55 | 21.2% | United States / North Carolina / Charlotte / H4Y Technologies LLC | No apparent signal |
| 2 | `104.237.132.58` | 44 | 17.0% | United States / Texas / Richardson / Linode | Hosting/Cloud (linode) |
| 3 | `45.33.12.231` | 38 | 14.7% | United States / Texas / Richardson / Linode | Hosting/Cloud (linode) |
| 4 | `139.177.206.6` | 16 | 6.2% | United States / Georgia / Atlanta / Linode | Hosting/Cloud (linode) |
| 5 | `104.248.127.214` | 12 | 4.6% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 6 | `3.131.24.55` | 11 | 4.2% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 7 | `45.33.96.214` | 11 | 4.2% | United States / Georgia / Atlanta / Linode | Hosting/Cloud (linode) |
| 8 | `2.22.149.145` | 11 | 4.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 9 | `3.147.122.184` | 10 | 3.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 10 | `2.22.149.137` | 10 | 3.9% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 11 | `100.49.117.77` | 9 | 3.5% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 12 | `91.230.168.129` | 8 | 3.1% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 13 | `195.184.76.198` | 8 | 3.1% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `18.217.208.51` | 8 | 3.1% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 15 | `3.15.230.87` | 8 | 3.1% | United States / Ohio / Columbus / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `104.237.132.58` | 44 | 23.4% | Hosting/Cloud (linode) | United States / Texas / Richardson / Linode |
| 2 | `45.33.12.231` | 38 | 20.2% | Hosting/Cloud (linode) | United States / Texas / Richardson / Linode |
| 3 | `139.177.206.6` | 16 | 8.5% | Hosting/Cloud (linode) | United States / Georgia / Atlanta / Linode |
| 4 | `104.248.127.214` | 12 | 6.4% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 5 | `3.131.24.55` | 11 | 5.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `45.33.96.214` | 11 | 5.9% | Hosting/Cloud (linode) | United States / Georgia / Atlanta / Linode |
| 7 | `2.22.149.145` | 11 | 5.9% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 8 | `3.147.122.184` | 10 | 5.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 9 | `2.22.149.137` | 10 | 5.3% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |
| 10 | `100.49.117.77` | 9 | 4.8% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 11 | `18.217.208.51` | 8 | 4.3% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 12 | `3.15.230.87` | 8 | 4.3% | Hosting/Cloud (aws) | United States / Ohio / Columbus / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
