# UFW Block Report

- Log: `/var/log/ufw.log`
- Ventana: últimas 24.0 horas
- Total de bloqueos: 63
- IPs de origen únicas: 42
- Puertos destino únicos: 44

## Top puertos destino
| Puerto destino | Conteo |
| --- | ---: |
| 44489 | 6 |
| 8333 | 4 |
| 44532 | 4 |
| 45034 | 3 |
| 56664 | 3 |
| 2375 | 2 |
| 62082 | 2 |
| 56726 | 2 |
| 44499 | 2 |
| 52311 | 1 |
| 7574 | 1 |
| 23 | 1 |
| 8081 | 1 |
| 31926 | 1 |
| 31478 | 1 |

## Top IPs origen
| IP origen | Conteo |
| --- | ---: |
| 151.101.218.73 | 6 |
| 184.31.2.80 | 5 |
| 185.133.35.14 | 4 |
| 79.124.62.230 | 3 |
| 54.224.145.4 | 3 |
| 185.133.35.13 | 3 |
| 194.180.49.70 | 2 |
| 17.57.144.152 | 2 |
| 100.24.10.103 | 2 |
| 85.217.149.13 | 1 |
| 120.85.117.185 | 1 |
| 59.127.12.31 | 1 |
| 193.34.213.150 | 1 |
| 206.168.34.128 | 1 |
| 23.94.31.42 | 1 |

## Top IP origen -> puerto destino
| IP origen -> puerto | Conteo |
| --- | ---: |
| 151.101.218.73 -> 44489 | 6 |
| 185.133.35.14 -> 44532 | 4 |
| 54.224.145.4 -> 45034 | 3 |
| 184.31.2.80 -> 56664 | 3 |
| 17.57.144.152 -> 62082 | 2 |
| 100.24.10.103 -> 8333 | 2 |
| 184.31.2.80 -> 56726 | 2 |
| 185.133.35.13 -> 44499 | 2 |
| 85.217.149.13 -> 52311 | 1 |
| 120.85.117.185 -> 7574 | 1 |
| 59.127.12.31 -> 23 | 1 |
| 193.34.213.150 -> 8081 | 1 |
| 206.168.34.128 -> 31926 | 1 |
| 79.124.62.230 -> 31478 | 1 |
| 23.94.31.42 -> 5061 | 1 |

## Bloqueos por hora (UTC)
| Hora | Conteo |
| --- | ---: |
| 2025-12-10 16:00:00:00 | 24 |
| 2025-12-10 17:00:00:00 | 36 |
| 2025-12-10 19:00:00:00 | 3 |

## Geolocalización (máx 15 IPs)
| IP origen | Conteo | Ubicación |
| --- | ---: | --- |
| 151.101.218.73 | 6 | Argentina / Buenos Aires F.D. / Buenos Aires / Fastly, Inc. |
| 184.31.2.80 | 5 | Argentina / Buenos Aires F.D. / Buenos Aires / Akamai Technologies, Inc. |
| 185.133.35.14 | 4 | Brazil / São Paulo / Casa Verde / Linked Store Brasil Criacao E Desenvol De Software |
| 79.124.62.230 | 3 | Seychelles / La Rivière Anglaise / Victoria / Internet Solutions & Innovations LTD |
| 54.224.145.4 | 3 | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 185.133.35.13 | 3 | Brazil / São Paulo / Casa Verde / Linked Store Brasil Criacao E Desenvol De Software |
| 194.180.49.70 | 2 | Germany / Bavaria / Berngau / HostSlick |
| 17.57.144.152 | 2 | United States / California / Cupertino / Apple Inc |
| 100.24.10.103 | 2 | United States / Virginia / Ashburn / AWS EC2 (us-east-1) |
| 85.217.149.13 | 1 | United States / New York / New York / Modat B.V |
| 120.85.117.185 | 1 | China / Guangdong / Guangzhou |
| 59.127.12.31 | 1 | Taiwan / Pingtung / Pingtung City / Chunghwa Telecom Co. Ltd. |
| 193.34.213.150 | 1 | Poland / Mazovia / Warsaw / SKYTECHNOLOGY |
| 206.168.34.128 | 1 | United States / Illinois / Chicago / Censys, Inc. |
| 23.94.31.42 | 1 | United States / New York / Buffalo |

## Gráficos
![Top puertos destino](ufw_plots/ufw_top_ports.jpg)
![Top IPs origen](ufw_plots/ufw_top_ips.jpg)
![Bloqueos por hora (UTC)](ufw_plots/ufw_hourly.jpg)
