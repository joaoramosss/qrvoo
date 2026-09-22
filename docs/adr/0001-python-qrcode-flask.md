# ADR 0001 — Python + qrcode + Flask

**Status:** aceito — 2026-09

## Contexto
O projeto precisa gerar QR Codes que abram buscas de passagens aéreas e ser simples de testar, empacotar e publicar.

## Decisão
- Python 3.12 com a biblioteca `qrcode` (backend Pillow) para gerar PNG.
- Flask para a interface web e Gunicorn como servidor no container.
- Interface de linha de comando (argparse) para uso sem navegador.
- Links montados a partir de padrões públicos de URL de cada site, sem uso de APIs pagas.

## Consequências
- Nenhuma credencial externa é necessária, logo não há segredos na aplicação.
- Se algum site mudar o formato de URL, basta ajustar a função correspondente em `links.py` e o teste associado.
