"""Interface de linha de comando: python -m qrvoo GRU LIS 2026-12-10 --volta 2026-12-20"""

from __future__ import annotations

import argparse
from datetime import date

from qrvoo import __version__
from qrvoo.links import SITES, BuscaVoo, montar_url
from qrvoo.qr import salvar_png


def criar_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="qrvoo", description="Gera QR Code para busca de passagens aéreas.")
    p.add_argument("origem", help="Código IATA de origem (ex.: GRU)")
    p.add_argument("destino", help="Código IATA de destino (ex.: LIS)")
    p.add_argument("ida", type=date.fromisoformat, help="Data de ida (AAAA-MM-DD)")
    p.add_argument("--volta", type=date.fromisoformat, default=None, help="Data de volta (AAAA-MM-DD)")
    p.add_argument("--adultos", type=int, default=1)
    p.add_argument("--site", choices=list(SITES), default="skyscanner")
    p.add_argument("-o", "--saida", default="qrcode_voo.png", help="Arquivo PNG de saída")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return p


def main(argv: list[str] | None = None) -> int:
    args = criar_parser().parse_args(argv)
    try:
        busca = BuscaVoo(args.origem, args.destino, args.ida, args.volta, args.adultos)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return 1
    url = montar_url(args.site, busca)
    caminho = salvar_png(url, args.saida)
    print(f"URL: {url}")
    print(f"QR Code salvo em: {caminho}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
