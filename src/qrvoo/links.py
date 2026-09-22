"""Montagem de URLs de busca de voos para cada site suportado."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from urllib.parse import quote

IATA_RE = re.compile(r"^[A-Z]{3}$")


@dataclass(frozen=True)
class BuscaVoo:
    origem: str
    destino: str
    ida: date
    volta: date | None = None
    adultos: int = 1

    def __post_init__(self) -> None:
        origem = self.origem.strip().upper()
        destino = self.destino.strip().upper()
        if not IATA_RE.match(origem) or not IATA_RE.match(destino):
            raise ValueError("Origem e destino devem ser códigos IATA de 3 letras (ex.: GRU, LIS).")
        if origem == destino:
            raise ValueError("Origem e destino não podem ser iguais.")
        if self.volta and self.volta < self.ida:
            raise ValueError("A data de volta não pode ser anterior à de ida.")
        if not 1 <= self.adultos <= 9:
            raise ValueError("Número de adultos deve estar entre 1 e 9.")
        object.__setattr__(self, "origem", origem)
        object.__setattr__(self, "destino", destino)


def _skyscanner(b: BuscaVoo) -> str:
    fmt = "%y%m%d"
    url = (
        "https://www.skyscanner.com.br/transporte/passagens-aereas/"
        f"{b.origem.lower()}/{b.destino.lower()}/{b.ida.strftime(fmt)}/"
    )
    if b.volta:
        url += f"{b.volta.strftime(fmt)}/"
    return url + f"?adultsv2={b.adultos}"


def _kayak(b: BuscaVoo) -> str:
    url = f"https://www.kayak.com.br/flights/{b.origem}-{b.destino}/{b.ida.isoformat()}"
    if b.volta:
        url += f"/{b.volta.isoformat()}"
    return url + f"/{b.adultos}adults"


def _momondo(b: BuscaVoo) -> str:
    url = f"https://www.momondo.com.br/flight-search/{b.origem}-{b.destino}/{b.ida.isoformat()}"
    if b.volta:
        url += f"/{b.volta.isoformat()}"
    return url + f"/{b.adultos}adults"


def _google_flights(b: BuscaVoo) -> str:
    consulta = f"Flights from {b.origem} to {b.destino} on {b.ida.isoformat()}"
    if b.volta:
        consulta += f" returning {b.volta.isoformat()}"
    return f"https://www.google.com/travel/flights?q={quote(consulta)}&hl=pt-BR"


SITES = {
    "skyscanner": ("Skyscanner", _skyscanner),
    "kayak": ("Kayak", _kayak),
    "momondo": ("Momondo", _momondo),
    "google": ("Google Flights", _google_flights),
}


def montar_url(site: str, busca: BuscaVoo) -> str:
    try:
        _, builder = SITES[site.lower()]
    except KeyError as exc:
        raise ValueError(f"Site não suportado: {site}. Opções: {', '.join(SITES)}") from exc
    return builder(busca)
