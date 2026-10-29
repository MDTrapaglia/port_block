# UFW Block Report

- Log: `/var/log/ufw.log`
- Window: last 24.0 hours
- Total blocks: 4431
- Unique source IPs: 2134
- Unique countries/cities (24h): 268
- Unique destination ports: 2268

## Top destination ports
| # | Destination port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `23` | 607 | 13.7% |
| 2 | `22` | 78 | 1.8% |
| 3 | `8080` | 40 | 0.9% |
| 4 | `5060` | 35 | 0.8% |
| 5 | `3389` | 29 | 0.7% |
| 6 | `53` | 25 | 0.6% |
| 7 | `1433` | 24 | 0.5% |
| 8 | `123` | 18 | 0.4% |
| 9 | `8081` | 16 | 0.4% |
| 10 | `8443` | 16 | 0.4% |
| 11 | `3306` | 15 | 0.3% |
| 12 | `3128` | 15 | 0.3% |
| 13 | `1723` | 15 | 0.3% |
| 14 | `161` | 13 | 0.3% |
| 15 | `27017` | 13 | 0.3% |

## Top protocols
| # | Protocol | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `TCP` | 4095 | 92.4% |
| 2 | `UDP` | 330 | 7.4% |
| 3 | `47` | 5 | 0.1% |
| 4 | `4` | 1 | 0.0% |

## Top source IPs
| # | Source IP | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `167.172.66.238` | 469 | 10.6% |
| 2 | `77.239.124.2` | 145 | 3.3% |
| 3 | `216.180.246.245` | 69 | 1.6% |
| 4 | `167.71.209.241` | 69 | 1.6% |
| 5 | `216.180.246.226` | 35 | 0.8% |
| 6 | `151.101.218.13` | 23 | 0.5% |
| 7 | `151.101.218.73` | 23 | 0.5% |
| 8 | `195.182.16.183` | 20 | 0.5% |
| 9 | `138.226.239.21` | 16 | 0.4% |
| 10 | `2.22.149.171` | 16 | 0.4% |
| 11 | `195.184.76.116` | 15 | 0.3% |
| 12 | `200.46.176.186` | 14 | 0.3% |
| 13 | `195.184.76.71` | 12 | 0.3% |
| 14 | `91.231.89.130` | 12 | 0.3% |
| 15 | `91.231.89.87` | 12 | 0.3% |

## Top TCP flag patterns
| # | Flags | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `SYN` | 3952 | 96.5% |
| 2 | `ACK+FIN+PSH` | 98 | 2.4% |
| 3 | `ACK+PSH` | 32 | 0.8% |
| 4 | `ACK+FIN` | 12 | 0.3% |
| 5 | `SYN+ECE+CWR` | 1 | 0.0% |

## Top inbound interfaces (IN)
| # | Interface | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `eth0` | 4430 | 100.0% |
| 2 | `wlan0` | 1 | 0.0% |

## Top source IP -> destination port
| # | Source IP -> port | Count | % |
| ---: | --- | ---: | ---: |
| 1 | `167.172.66.238` -> `23` | 469 | 10.6% |
| 2 | `200.46.176.186` -> `23` | 14 | 0.3% |
| 3 | `216.180.246.245` -> `63345` | 8 | 0.2% |
| 4 | `130.45.31.42` -> `7680` | 8 | 0.2% |
| 5 | `151.101.218.13` -> `10659` | 8 | 0.2% |
| 6 | `216.180.246.245` -> `62857` | 7 | 0.2% |
| 7 | `216.180.246.245` -> `63041` | 7 | 0.2% |
| 8 | `216.180.246.245` -> `63045` | 7 | 0.2% |
| 9 | `216.180.246.226` -> `22` | 7 | 0.2% |
| 10 | `93.123.109.6` -> `1723` | 6 | 0.1% |
| 11 | `216.180.246.245` -> `62163` | 6 | 0.1% |
| 12 | `62.210.114.99` -> `3389` | 6 | 0.1% |
| 13 | `216.180.246.245` -> `63014` | 6 | 0.1% |
| 14 | `216.180.246.245` -> `63256` | 6 | 0.1% |
| 15 | `68.209.56.42` -> `22` | 6 | 0.1% |

## Blocks per hour (UTC)
| Hour (UTC) | Count | % |
| :--- | ---: | ---: |
| 2026-10-28 04:00:00:00 | 133 | 3.0% |
| 2026-10-28 05:00:00:00 | 181 | 4.1% |
| 2026-10-28 06:00:00:00 | 180 | 4.1% |
| 2026-10-28 07:00:00:00 | 181 | 4.1% |
| 2026-10-28 08:00:00:00 | 179 | 4.0% |
| 2026-10-28 09:00:00:00 | 180 | 4.1% |
| 2026-10-28 10:00:00:00 | 181 | 4.1% |
| 2026-10-28 11:00:00:00 | 178 | 4.0% |
| 2026-10-28 12:00:00:00 | 182 | 4.1% |
| 2026-10-28 13:00:00:00 | 180 | 4.1% |
| 2026-10-28 14:00:00:00 | 180 | 4.1% |
| 2026-10-28 15:00:00:00 | 180 | 4.1% |
| 2026-10-28 16:00:00:00 | 189 | 4.3% |
| 2026-10-28 17:00:00:00 | 189 | 4.3% |
| 2026-10-28 18:00:00:00 | 180 | 4.1% |
| 2026-10-28 19:00:00:00 | 179 | 4.0% |
| 2026-10-28 20:00:00:00 | 192 | 4.3% |
| 2026-10-28 21:00:00:00 | 205 | 4.6% |
| 2026-10-28 22:00:00:00 | 218 | 4.9% |
| 2026-10-28 23:00:00:00 | 180 | 4.1% |
| 2026-10-29 00:00:00:00 | 195 | 4.4% |
| 2026-10-29 01:00:00:00 | 184 | 4.2% |
| 2026-10-29 02:00:00:00 | 179 | 4.0% |
| 2026-10-29 03:00:00:00 | 180 | 4.1% |
| 2026-10-29 04:00:00:00 | 46 | 1.0% |

## Top source countries/cities
| # | Location | Count | % |
| ---: | --- | ---: | ---: |
| 1 | Singapore, Singapore | 538 | 56.6% |
| 2 | Paris, France | 145 | 15.3% |
| 3 | Massy, France | 104 | 10.9% |
| 4 | Buenos Aires, Argentina | 39 | 4.1% |
| 5 | Warrenton, United States | 27 | 2.8% |
| 6 | Gravelines, France | 24 | 2.5% |
| 7 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | 23 | 2.4% |
| 8 | Frankfurt am Main, Germany | 20 | 2.1% |
| 9 | Port Vila, Vanuatu | 16 | 1.7% |
| 10 | Panama City, Panama | 14 | 1.5% |

## Geolocation (max 15 IPs)
| # | Source IP | Count | % | Location | Network / hint |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `167.172.66.238` | 469 | 49.4% | Singapore / South West / Singapore / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 2 | `77.239.124.2` | 145 | 15.3% | France / Île-de-France / Paris / RocketCloud | No apparent signal |
| 3 | `216.180.246.245` | 69 | 7.3% | France / Île-de-France / Massy / Internet Utilities NA LLC | Hosting/Cloud (google llc) |
| 4 | `167.71.209.241` | 69 | 7.3% | Singapore / South West / Singapore / DigitalOcean, LLC | Hosting/Cloud (digitalocean) |
| 5 | `216.180.246.226` | 35 | 3.7% | France / Île-de-France / Massy / Google LLC | Hosting/Cloud (google llc) |
| 6 | `151.101.218.13` | 23 | 2.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 7 | `151.101.218.73` | 23 | 2.4% | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. | CDN/Edge (fastly) |
| 8 | `195.182.16.183` | 20 | 2.1% | Germany / Hesse / Frankfurt am Main / Amarutu Technology Ltd | No apparent signal |
| 9 | `138.226.239.21` | 16 | 1.7% | Vanuatu / Shefa Province / Port Vila / Vertex Horizon Technology | No apparent signal |
| 10 | `2.22.149.171` | 16 | 1.7% | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies | CDN/Edge (akamai) |
| 11 | `195.184.76.116` | 15 | 1.6% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 12 | `200.46.176.186` | 14 | 1.5% | Panama / Provincia de Panamá / Panama City / Cable Onda | No apparent signal |
| 13 | `195.184.76.71` | 12 | 1.3% | United States / Virginia / Warrenton / ONYPHE | No apparent signal |
| 14 | `91.231.89.130` | 12 | 1.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |
| 15 | `91.231.89.87` | 12 | 1.3% | France / Hauts-de-France / Gravelines / ONYPHE | No apparent signal |

## VPN/Proxy/Hosting suspicion (heuristic)
| # | Source IP | Count | % | Suspicion | Location |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `167.172.66.238` | 469 | 66.6% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / DigitalOcean, LLC |
| 2 | `216.180.246.245` | 69 | 9.8% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Internet Utilities NA LLC |
| 3 | `167.71.209.241` | 69 | 9.8% | Hosting/Cloud (digitalocean) | Singapore / South West / Singapore / DigitalOcean, LLC |
| 4 | `216.180.246.226` | 35 | 5.0% | Hosting/Cloud (google llc) | France / Île-de-France / Massy / Google LLC |
| 5 | `151.101.218.13` | 23 | 3.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 6 | `151.101.218.73` | 23 | 3.3% | CDN/Edge (fastly) | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 7 | `2.22.149.171` | 16 | 2.3% | CDN/Edge (akamai) | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies |

## Charts
![Top destination ports](ufw_plots/ufw_top_ports.jpg)
![Top source countries/cities](ufw_plots/ufw_top_locations.jpg)
![Blocks per hour (UTC)](ufw_plots/ufw_hourly.jpg)
![Block map](ufw_plots/ufw_geo_map.jpg)
