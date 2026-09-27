# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 609
- Unique source IPs: 483
- Unique countries/cities (24h): 103
- Unique destination ports: 458

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 18 | 3.0% |
| 2 | `22` | 12 | 2.0% |
| 3 | `3777` | 9 | 1.5% |
| 4 | `1433` | 7 | 1.1% |
| 5 | `55254` | 6 | 1.0% |
| 6 | `8443` | 6 | 1.0% |
| 7 | `57892` | 6 | 1.0% |
| 8 | `3380` | 5 | 0.8% |
| 9 | `3389` | 5 | 0.8% |
| 10 | `59556` | 5 | 0.8% |
| 11 | `3541` | 5 | 0.8% |
| 12 | `60350` | 4 | 0.7% |
| 13 | `8000` | 4 | 0.7% |
| 14 | `8333` | 4 | 0.7% |
| 15 | `3400` | 4 | 0.7% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 557 | 91.5% |
| 2 | `UDP` | 51 | 8.4% |
| 3 | `132` | 1 | 0.2% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.147` | 25 | 4.1% |
| 2 | `149.154.166.120` | 9 | 1.5% |
| 3 | `149.154.167.222` | 6 | 1.0% |
| 4 | `165.227.7.48` | 6 | 1.0% |
| 5 | `151.101.216.157` | 6 | 1.0% |
| 6 | `141.98.83.48` | 5 | 0.8% |
| 7 | `165.22.9.15` | 4 | 0.7% |
| 8 | `159.100.13.116` | 4 | 0.7% |
| 9 | `85.217.140.3` | 4 | 0.7% |
| 10 | `185.12.59.118` | 4 | 0.7% |
| 11 | `185.73.23.133` | 3 | 0.5% |
| 12 | `85.217.140.34` | 3 | 0.5% |
| 13 | `91.230.168.211` | 3 | 0.5% |
| 14 | `186.123.128.53` | 3 | 0.5% |
| 15 | `3.131.24.55` | 3 | 0.5% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 532 | 95.5% |
| 2 | `ACK` | 15 | 2.7% |
| 3 | `ACK+FIN+PSH` | 8 | 1.4% |
| 4 | `ACK+PSH` | 2 | 0.4% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 609 | 100.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `216.180.246.147` -> `3777` | 9 | 1.5% |
| 2 | `149.154.167.222` -> `55254` | 6 | 1.0% |
| 3 | `151.101.216.157` -> `57892` | 6 | 1.0% |
| 4 | `216.180.246.147` -> `3380` | 5 | 0.8% |
| 5 | `149.154.166.120` -> `59556` | 5 | 0.8% |
| 6 | `216.180.246.147` -> `3541` | 5 | 0.8% |
| 7 | `149.154.166.120` -> `60350` | 4 | 0.7% |
| 8 | `216.180.246.147` -> `3400` | 4 | 0.7% |
| 9 | `186.123.128.53` -> `1433` | 3 | 0.5% |
| 10 | `69.17.52.1` -> `8333` | 3 | 0.5% |
| 11 | `199.45.154.118` -> `135` | 3 | 0.5% |
| 12 | `89.42.231.200` -> `34567` | 3 | 0.5% |
| 13 | `151.101.217.44` -> `48550` | 3 | 0.5% |
| 14 | `216.180.246.147` -> `3389` | 2 | 0.3% |
| 15 | `66.132.172.204` -> `8299` | 2 | 0.3% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-09-27 00:00:00:00 | 16 | 2.6% |
| 2026-09-27 01:00:00:00 | 180 | 29.6% |
| 2026-09-27 02:00:00:00 | 178 | 29.2% |
| 2026-09-27 03:00:00:00 | 190 | 31.2% |
| 2026-09-27 04:00:00:00 | 45 | 7.4% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Massy, France | 25 | 28.4% |
| 2 | Amsterdam, Netherlands | 9 | 10.2% |
| 3 | Frankfurt am Main, Germany | 7 | 8.0% |
| 4 | Gravelines, France | 7 | 8.0% |
| 5 | Amsterdam, The Netherlands | 6 | 6.8% |
| 6 | Santa Clara, United States | 6 | 6.8% |
| 7 | Buenos Aires, Argentina | 6 | 6.8% |
| 8 | Panama City, Panama | 5 | 5.7% |
| 9 | North Bergen, United States | 4 | 4.5% |
| 10 | Oslo, Norway | 4 | 4.5% |
| 11 | Hillsboro, United States | 3 | 3.4% |
| 12 | Godoy Cruz, Argentina | 3 | 3.4% |
| 13 | Dublin, United States | 3 | 3.4% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.147` | 25 | 28.4% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 2 | `149.154.166.120` | 9 | 10.2% | Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 3 | `149.154.167.222` | 6 | 6.8% | The Netherlands / North Holland / Amsterdam / Telegram Messenger Amsterdam Network | No apparent signal |
| 4 | `165.227.7.48` | 6 | 6.8% | United States / California / Santa Clara / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `151.101.216.157` | 6 | 6.8% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 6 | `141.98.83.48` | 5 | 5.7% | Panama / Provincia de Panamá / Panama City / GLOBALHOST | Hosting/Cloud (servers) |
| 7 | `165.22.9.15` | 4 | 4.5% | United States / New Jersey / North Bergen / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 8 | `159.100.13.116` | 4 | 4.5% | Germany / Hesse / Frankfurt am Main / UltaHost Inc | No apparent signal |
| 9 | `85.217.140.3` | 4 | 4.5% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 10 | `185.12.59.118` | 4 | 4.5% | Norway / Oslo / Oslo / Blixcust10463 | No apparent signal |
| 11 | `185.73.23.133` | 3 | 3.4% | Germany / Hesse / Frankfurt am Main / RUB LIR Inet2 | No apparent signal |
| 12 | `85.217.140.34` | 3 | 3.4% | France / Hauts-de-France / Gravelines / Modat B.V | No apparent signal |
| 13 | `91.230.168.211` | 3 | 3.4% | United States / Oregon / Hillsboro / ONYPHE | No apparent signal |
| 14 | `186.123.128.53` | 3 | 3.4% | Argentina / Mendoza / Godoy Cruz / AMX Argentina S.A | No apparent signal |
| 15 | `3.131.24.55` | 3 | 3.4% | United States / Ohio / Dublin / AWS EC2 (us-east-2) | Hosting/Cloud (aws) |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `216.180.246.147` | 25 | 51.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 2 | `165.227.7.48` | 6 | 12.2% | Hosting/Cloud (digitalocean) | United States / California / Santa Clara / DigitalOcean, LLC |
| 3 | `151.101.216.157` | 6 | 12.2% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 4 | `141.98.83.48` | 5 | 10.2% | Hosting/Cloud (servers) | Panama / Provincia de Panamá / Panama City / GLOBALHOST |
| 5 | `165.22.9.15` | 4 | 8.2% | Hosting/Cloud (digitalocean) | United States / New Jersey / North Bergen / DigitalOcean, LLC |
| 6 | `3.131.24.55` | 3 | 6.1% | Hosting/Cloud (aws) | United States / Ohio / Dublin / AWS EC2 (us-east-2) |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
