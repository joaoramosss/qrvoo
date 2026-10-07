# QRVoo

Gerador de QR Code que abre direto a busca de passagens aéreas no Skyscanner, Kayak, Momondo ou Google Flights. Você informa origem, destino e datas; o QRVoo monta o link e devolve o QR Code em PNG.

![CI](https://github.com/joaoramosss/qrvoo/actions/workflows/ci.yml/badge.svg)

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
```

### Linha de comando

```bash
qrvoo GRU LIS 2026-12-10 --volta 2026-12-20 --site skyscanner -o viagem.png
```

Sites disponíveis: `skyscanner`, `kayak`, `momondo`, `google`.

### Interface web

```bash
flask --app qrvoo.web run --port 8000
```

Acesse http://localhost:8000. Também existe o endpoint direto:
`/qr.png?origem=GRU&destino=LIS&ida=2026-12-10&site=kayak`

### Docker

```bash
docker build -t qrvoo .
docker run -p 8000:8000 qrvoo
```

## Testes e qualidade

```bash
ruff check .
pytest --cov --cov-fail-under=80
bandit -r src -ll
pip-audit -r requirements.txt
```

## Estrutura

```
src/qrvoo/         código da aplicação (links, qr, cli, web)
tests/             testes automatizados (pytest)
.github/workflows/ pipelines de CI e release (CD)
infra/             docker-compose do ambiente de homologação
docs/adr/          decisões de arquitetura
```

## Fluxo de contribuição

1. Crie uma issue e uma branch `feature/<issue>-<descricao>`.
2. Commits no padrão Conventional Commits (`feat:`, `fix:`, `docs:`...).
3. Abra um Pull Request para `main`; o merge só acontece com o CI verde.
4. Para lançar uma versão: `git tag v1.1.0 && git push origin v1.1.0`.

## Licença

MIT
