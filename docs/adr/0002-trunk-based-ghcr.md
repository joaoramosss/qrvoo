# ADR 0002 — Trunk-based development e GHCR

**Status:** aceito — 2026-09

## Decisão
Branch `main` protegida, branches `feature/*` de vida curta, GitHub Actions para CI/CD e GitHub Container Registry (GHCR) como registro de imagens. Releases são criadas por tag SemVer `vX.Y.Z`, que promove a imagem já testada sem recompilação.
