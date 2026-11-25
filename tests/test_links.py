from datetime import date, timedelta

import pytest

from qrvoo.links import DURACAO_MAXIMA_DIAS, SITES, BuscaVoo, montar_url

IDA = date(2026, 12, 10)
VOLTA = date(2026, 12, 20)


def test_skyscanner_ida_e_volta():
    url = montar_url("skyscanner", BuscaVoo("gru", "lis", IDA, VOLTA, 2))
    assert url == (
        "https://www.skyscanner.com.br/transporte/passagens-aereas/gru/lis/261210/261220/?adultsv2=2"
    )


def test_skyscanner_so_ida():
    url = montar_url("skyscanner", BuscaVoo("GRU", "LIS", IDA))
    assert url.endswith("/gru/lis/261210/?adultsv2=1")


def test_kayak_e_momondo():
    b = BuscaVoo("JOI", "GRU", IDA, VOLTA)
    assert montar_url("kayak", b) == "https://www.kayak.com.br/flights/JOI-GRU/2026-12-10/2026-12-20/1adults"
    assert montar_url("momondo", b).startswith("https://www.momondo.com.br/flight-search/JOI-GRU/")


def test_google_flights_codifica_consulta():
    url = montar_url("google", BuscaVoo("GRU", "LIS", IDA))
    assert "Flights%20from%20GRU%20to%20LIS" in url


@pytest.mark.parametrize("site", list(SITES))
def test_todos_os_sites_geram_https(site):
    assert montar_url(site, BuscaVoo("GRU", "LIS", IDA)).startswith("https://")


@pytest.mark.parametrize(
    "args",
    [
        ("GR", "LIS", IDA, None, 1),
        ("GRU", "GRU", IDA, None, 1),
        ("GRU", "LIS", VOLTA, IDA, 1),
        ("GRU", "LIS", IDA, None, 0),
        ("GRU", "LIS", IDA, None, 10),
    ],
)
def test_validacoes(args):
    with pytest.raises(ValueError):
        BuscaVoo(*args)


def test_site_invalido():
    with pytest.raises(ValueError):
        montar_url("decolar", BuscaVoo("GRU", "LIS", IDA))


def test_viagem_com_duracao_maxima_e_aceita():
    volta = IDA + timedelta(days=DURACAO_MAXIMA_DIAS)
    assert BuscaVoo("GRU", "LIS", IDA, volta).volta == volta


def test_viagem_acima_da_duracao_maxima_e_recusada():
    volta = IDA + timedelta(days=DURACAO_MAXIMA_DIAS + 1)
    with pytest.raises(ValueError, match="mais de 365 dias"):
        BuscaVoo("GRU", "LIS", IDA, volta)
