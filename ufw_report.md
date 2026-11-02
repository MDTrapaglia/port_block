# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4378
- Unique source IPs: 2521
- Unique countries/cities (24h): 292
- Unique destination ports: 2337

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 129 | 2.9% |
| 2 | `41641` | 99 | 2.3% |
| 3 | `22` | 92 | 2.1% |
| 4 | `1433` | 61 | 1.4% |
| 5 | `3389` | 43 | 1.0% |
| 6 | `5060` | 43 | 1.0% |
| 7 | `53` | 38 | 0.9% |
| 8 | `8080` | 38 | 0.9% |
| 9 | `123` | 26 | 0.6% |
| 10 | `3306` | 22 | 0.5% |
| 11 | `8443` | 22 | 0.5% |
| 12 | `8081` | 21 | 0.5% |
| 13 | `5353` | 18 | 0.4% |
| 14 | `5038` | 18 | 0.4% |
| 15 | `1723` | 17 | 0.4% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 3899 | 89.1% |
| 2 | `UDP` | 475 | 10.8% |
| 3 | `47` | 3 | 0.1% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.191` | 143 | 3.3% |
| 2 | `186.123.164.151` | 98 | 2.2% |
| 3 | `220.249.82.190` | 66 | 1.5% |
| 4 | `60.174.231.133` | 36 | 0.8% |
| 5 | `167.99.207.12` | 24 | 0.5% |
| 6 | `151.101.218.13` | 22 | 0.5% |
| 7 | `103.122.221.179` | 20 | 0.5% |
| 8 | `34.197.70.90` | 16 | 0.4% |
| 9 | `45.198.224.125` | 16 | 0.4% |
| 10 | `37.72.140.44` | 16 | 0.4% |
| 11 | `3.151.116.231` | 15 | 0.3% |
| 12 | `18.221.179.104` | 14 | 0.3% |
| 13 | `62.210.114.99` | 11 | 0.3% |
| 14 | `149.33.19.95` | 11 | 0.3% |
| 15 | `151.101.218.73` | 11 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3814 | 97.8% |
| 2 | `ACK+FIN+PSH` | 50 | 1.3% |
| 3 | `ACK+PSH` | 22 | 0.6% |
| 4 | `ACK+FIN` | 8 | 0.2% |
| 5 | `SYN+ECE+CWR` | 4 | 0.1% |
| 6 | `ACK` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4378 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `186.123.164.151` -> `41641` | 95 | 2.2% |
| 2 | `60.174.231.133` -> `1433` | 36 | 0.8% |
| 3 | `216.180.246.191` -> `5140` | 12 | 0.3% |
| 4 | `62.210.114.99` -> `3389` | 11 | 0.3% |
| 5 | `216.180.246.191` -> `5090` | 11 | 0.3% |
| 6 | `216.180.246.191` -> `4950` | 10 | 0.2% |
| 7 | `216.180.246.191` -> `5122` | 10 | 0.2% |
| 8 | `154.80.128.160` -> `6036` | 9 | 0.2% |
| 9 | `216.180.246.191` -> `5062` | 9 | 0.2% |
| 10 | `216.180.246.191` -> `5242` | 9 | 0.2% |
| 11 | `216.180.246.191` -> `5353` | 9 | 0.2% |
| 12 | `216.180.246.191` -> `5001` | 8 | 0.2% |
| 13 | `216.180.246.191` -> `5038` | 8 | 0.2% |
| 14 | `216.180.246.191` -> `5123` | 8 | 0.2% |
| 15 | `45.198.224.125` -> `8080` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-11-01 04:00:00:00 | 134 | 3.1% |
| 2026-11-01 05:00:00:00 | 180 | 4.1% |
| 2026-11-01 06:00:00:00 | 180 | 4.1% |
| 2026-11-01 07:00:00:00 | 180 | 4.1% |
| 2026-11-01 08:00:00:00 | 180 | 4.1% |
| 2026-11-01 09:00:00:00 | 178 | 4.1% |
| 2026-11-01 10:00:00:00 | 182 | 4.2% |
| 2026-11-01 11:00:00:00 | 194 | 4.4% |
| 2026-11-01 12:00:00:00 | 183 | 4.2% |
| 2026-11-01 13:00:00:00 | 193 | 4.4% |
| 2026-11-01 14:00:00:00 | 180 | 4.1% |
| 2026-11-01 15:00:00:00 | 186 | 4.2% |
| 2026-11-01 16:00:00:00 | 202 | 4.6% |
| 2026-11-01 17:00:00:00 | 179 | 4.1% |
| 2026-11-01 18:00:00:00 | 180 | 4.1% |
| 2026-11-01 19:00:00:00 | 181 | 4.1% |
| 2026-11-01 20:00:00:00 | 180 | 4.1% |
| 2026-11-01 21:00:00:00 | 177 | 4.0% |
| 2026-11-01 22:00:00:00 | 181 | 4.1% |
| 2026-11-01 23:00:00:00 | 181 | 4.1% |
| 2026-11-02 00:00:00:00 | 181 | 4.1% |
| 2026-11-02 01:00:00:00 | 180 | 4.1% |
| 2026-11-02 02:00:00:00 | 180 | 4.1% |
| 2026-11-02 03:00:00:00 | 178 | 4.1% |
| 2026-11-02 04:00:00:00 | 48 | 1.1% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 143 | 27.6% |
| 2 | Córdoba, Argentina | 98 | 18.9% |
| 3 | Wuhan, China | 66 | 12.7% |
| 4 | Hefei, China | 36 | 6.9% |
| 5 | Buenos Aires, Argentina | 33 | 6.4% |
| 6 | Dublin, United States | 29 | 5.6% |
| 7 | Slough, United Kingdom | 24 | 4.6% |
| 8 | Da Nang, Vietnam | 20 | 3.9% |
| 9 | Ashburn, United States | 16 | 3.1% |
| 10 | Stockholm, Sweden | 16 | 3.1% |
| 11 | St Petersburg, Russia | 16 | 3.1% |
| 12 | Paris, France | 11 | 2.1% |
| 13 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 11 | 2.1% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.191` | 143 | 27.6% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `186.123.164.151` | 98 | 18.9% | Argentina / Cordoba / Córdoba / AMX Argentina S.A | No apparent signal |
| 3 | `220.249.82.190` | 66 | 12.7% | China / Hubei / Wuhan / CNC Group CHINA169 Hubei Province Network | No apparent signal |
| 4 | `60.174.231.133` | 36 | 6.9% | China / Anhui / Hefei / Chinanet AH | No apparent signal |
| 5 | `167.99.207.12` | 24 | 4.6% | United Kingdom / England / Slough / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 6 | `151.101.218.13` | 22 | 4.2% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `103.122.221.179` | 20 | 3.9% | Vietnam / Da Nang City / Da Nang / HA SON Technology ONE Member Limited Company | No apparent signal |
| 8 | `34.197.70.90` | 16 | 3.1% | United States / Virginia / Ashburn / AWS EC2 (us-east-1) | Hosting/Cloud (aws) |
| 9 | `45.198.224.125` | 16 | 3.1% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 10 | `37.72.140.44` | 16 | 3.1% | Russia / St.-Petersburg / St Petersburg / Galeon LLC | No apparent signal |
| 11 | `3.151.116.231` | 15 | 2.9% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 12 | `18.221.179.104` | 14 | 2.7% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |
| 13 | `62.210.114.99` | 11 | 2.1% | France / Île-de-France / Paris / Online SAS | Hosting/Cloud (scaleway) |
| 14 | `149.33.19.95` | 11 | 2.1% | Argentina / Buenos Aires F.D. / Buenos Aires / 3NT SOLUTIONS LLP | No apparent signal |
| 15 | `151.101.218.73` | 11 | 2.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.191` | 143 | 55.9% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `167.99.207.12` | 24 | 9.4% | Hosting/Cloud (digitalocean) | United Kingdom / England / Slough / DigitalOcean, LLC |
| 3 | `151.101.218.13` | 22 | 8.6% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `34.197.70.90` | 16 | 6.2% | Hosting/Cloud (aws) | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 5 | `3.151.116.231` | 15 | 5.9% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 6 | `18.221.179.104` | 14 | 5.5% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |
| 7 | `62.210.114.99` | 11 | 4.3% | Hosting/Cloud (scaleway) | France / Île-de-France / Paris / Online SAS |
| 8 | `151.101.218.73` | 11 | 4.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
