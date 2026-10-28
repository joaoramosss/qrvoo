# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [SemVer](https://semver.org/lang/pt-BR/).
A partir da v1.0.0, as notas de cada release são geradas automaticamente pelo pipeline.

## [1.1.0] - 2026-10-28
### Adicionado
- Environment `staging` no CI (publicação da imagem `sha`/`latest` no GHCR) e `production` no release, com revisor obrigatório.
- PGCS publicado no repositório como item de configuração (`docs/PGCS_QRVoo.pdf`).
- Evidência da recusa de push direto na `main` (`docs/evidencias/`).
### Alterado
- CI passa a usar Python 3.14, mesma versão da imagem Docker.

## [1.0.1] - 2026-09-24
### Alterado
- Atualizações de dependências e actions via Dependabot (pytest, pytest-cov, ruff, pip-audit, checkout, setup-python, login-action, imagem base python 3.14-slim).

## [1.0.0] - 2026-09-22
### Adicionado
- Geração de QR Code para Skyscanner, Kayak, Momondo e Google Flights.
- CLI `qrvoo` e interface web Flask com endpoint `/qr.png` e `/health`.
- Pipelines de CI (lint, testes, SAST, SCA, imagem Docker) e de release (CD).
