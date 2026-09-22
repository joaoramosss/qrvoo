# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [SemVer](https://semver.org/lang/pt-BR/).
A partir da v1.0.0, as notas de cada release são geradas automaticamente pelo pipeline.

## [1.0.0] - 2026-09-22
### Adicionado
- Geração de QR Code para Skyscanner, Kayak, Momondo e Google Flights.
- CLI `qrvoo` e interface web Flask com endpoint `/qr.png` e `/health`.
- Pipelines de CI (lint, testes, SAST, SCA, imagem Docker) e de release (CD).
