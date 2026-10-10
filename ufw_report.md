# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4458
- Unique source IPs: 2421
- Unique countries/cities (24h): 297
- Unique destination ports: 2660

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 140 | 3.1% |
| 2 | `22` | 63 | 1.4% |
| 3 | `8080` | 42 | 0.9% |
| 4 | `1433` | 34 | 0.8% |
| 5 | `5060` | 33 | 0.7% |
| 6 | `3389` | 28 | 0.6% |
| 7 | `8443` | 21 | 0.5% |
| 8 | `2222` | 19 | 0.4% |
| 9 | `53` | 17 | 0.4% |
| 10 | `81` | 16 | 0.4% |
| 11 | `3306` | 16 | 0.4% |
| 12 | `5900` | 15 | 0.3% |
| 13 | `5432` | 15 | 0.3% |
| 14 | `123` | 15 | 0.3% |
| 15 | `8081` | 15 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4089 | 91.7% |
| 2 | `UDP` | 364 | 8.2% |
| 3 | `47` | 3 | 0.1% |
| 4 | `4` | 1 | 0.0% |
| 5 | `41` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.9` | 174 | 3.9% |
| 2 | `93.123.101.248` | 86 | 1.9% |
| 3 | `151.101.218.13` | 36 | 0.8% |
| 4 | `113.57.146.66` | 34 | 0.8% |
| 5 | `68.183.130.245` | 18 | 0.4% |
| 6 | `208.109.212.211` | 17 | 0.4% |
| 7 | `151.101.219.52` | 15 | 0.3% |
| 8 | `91.231.89.205` | 14 | 0.3% |
| 9 | `195.184.76.220` | 13 | 0.3% |
| 10 | `45.198.224.125` | 13 | 0.3% |
| 11 | `195.184.76.116` | 13 | 0.3% |
| 12 | `195.184.76.198` | 13 | 0.3% |
| 13 | `91.231.89.130` | 13 | 0.3% |
| 14 | `91.231.89.87` | 12 | 0.3% |
| 15 | `85.217.140.28` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3901 | 95.4% |
| 2 | `ACK+FIN+PSH` | 116 | 2.8% |
| 3 | `ACK+PSH` | 34 | 0.8% |
| 4 | `ACK+FIN` | 24 | 0.6% |
| 5 | `SYN+ECE+CWR` | 11 | 0.3% |
| 6 | `ACK` | 3 | 0.1% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4458 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `208.109.212.211` -> `23` | 17 | 0.4% |
| 2 | `216.180.246.9` -> `20800` | 10 | 0.2% |
| 3 | `216.180.246.9` -> `22225` | 10 | 0.2% |
| 4 | `216.180.246.9` -> `22280` | 10 | 0.2% |
| 5 | `216.180.246.9` -> `22022` | 9 | 0.2% |
| 6 | `216.180.246.9` -> `25080` | 9 | 0.2% |
| 7 | `216.180.246.9` -> `23231` | 8 | 0.2% |
| 8 | `216.180.246.9` -> `24442` | 8 | 0.2% |
| 9 | `216.180.246.9` -> `25565` | 8 | 0.2% |
| 10 | `45.198.224.124` -> `81` | 7 | 0.2% |
| 11 | `45.205.1.160` -> `6036` | 7 | 0.2% |
| 12 | `151.101.218.13` -> `52924` | 7 | 0.2% |
| 13 | `151.101.218.13` -> `54186` | 7 | 0.2% |
| 14 | `2.23.164.170` -> `49039` | 7 | 0.2% |
| 15 | `216.180.246.9` -> `23270` | 7 | 0.2% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-09 04:00:00:00 | 133 | 3.0% |
| 2026-10-09 05:00:00:00 | 179 | 4.0% |
| 2026-10-09 06:00:00:00 | 182 | 4.1% |
| 2026-10-09 07:00:00:00 | 178 | 4.0% |
| 2026-10-09 08:00:00:00 | 181 | 4.1% |
| 2026-10-09 09:00:00:00 | 179 | 4.0% |
| 2026-10-09 10:00:00:00 | 182 | 4.1% |
| 2026-10-09 11:00:00:00 | 180 | 4.0% |
| 2026-10-09 12:00:00:00 | 191 | 4.3% |
| 2026-10-09 13:00:00:00 | 181 | 4.1% |
| 2026-10-09 14:00:00:00 | 203 | 4.6% |
| 2026-10-09 15:00:00:00 | 183 | 4.1% |
| 2026-10-09 16:00:00:00 | 193 | 4.3% |
| 2026-10-09 17:00:00:00 | 193 | 4.3% |
| 2026-10-09 18:00:00:00 | 178 | 4.0% |
| 2026-10-09 19:00:00:00 | 181 | 4.1% |
| 2026-10-09 20:00:00:00 | 179 | 4.0% |
| 2026-10-09 21:00:00:00 | 220 | 4.9% |
| 2026-10-09 22:00:00:00 | 181 | 4.1% |
| 2026-10-09 23:00:00:00 | 181 | 4.1% |
| 2026-10-10 00:00:00:00 | 179 | 4.0% |
| 2026-10-10 01:00:00:00 | 198 | 4.4% |
| 2026-10-10 02:00:00:00 | 199 | 4.5% |
| 2026-10-10 03:00:00:00 | 179 | 4.0% |
| 2026-10-10 04:00:00:00 | 45 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 174 | 36.0% |
| 2 | Frankfurt am Main, Germany | 86 | 17.8% |
| 3 | Buenos Aires, Argentina | 51 | 10.6% |
| 4 | Gravelines, France | 51 | 10.6% |
| 5 | Warrenton, United States | 39 | 8.1% |
| 6 | Wuhan, China | 34 | 7.0% |
| 7 | North Bergen, United States | 18 | 3.7% |
| 8 | Tempe, United States | 17 | 3.5% |
| 9 | Stockholm, Sweden | 13 | 2.7% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.9` | 174 | 36.0% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 2 | `93.123.101.248` | 86 | 17.8% | Germany / Hesse / Frankfurt am Main / Soulful Hosting LTD | No apparent signal |
| 3 | `151.101.218.13` | 36 | 7.5% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 4 | `113.57.146.66` | 34 | 7.0% | China / Hubei / Wuhan / CNC Group CHINA169 Hubei Province Network | No apparent signal |
| 5 | `68.183.130.245` | 18 | 3.7% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 6 | `208.109.212.211` | 17 | 3.5% | United States / Arizona / Tempe / GoDaddy.com, LLC | No apparent signal |
| 7 | `151.101.219.52` | 15 | 3.1% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 8 | `91.231.89.205` | 14 | 2.9% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 9 | `195.184.76.220` | 13 | 2.7% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 10 | `45.198.224.125` | 13 | 2.7% | Sweden / Stockholm County / Stockholm / Vpsvault.host LTD | No apparent signal |
| 11 | `195.184.76.116` | 13 | 2.7% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 12 | `195.184.76.198` | 13 | 2.7% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 13 | `91.231.89.130` | 13 | 2.7% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 14 | `91.231.89.87` | 12 | 2.5% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `85.217.140.28` | 12 | 2.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.9` | 174 | 71.6% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 2 | `151.101.218.13` | 36 | 14.8% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 3 | `68.183.130.245` | 18 | 7.4% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 4 | `151.101.219.52` | 15 | 6.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
