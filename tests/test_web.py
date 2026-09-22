import pytest

from qrvoo.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_pagina_inicial(client):
    assert b"QRVoo" in client.get("/").data


def test_post_gera_qr(client):
    r = client.post("/", data={"origem": "GRU", "destino": "LIS", "ida": "2026-12-10", "site": "kayak"})
    assert b"data:image/png;base64" in r.data
    assert b"kayak.com.br" in r.data


def test_post_invalido_mostra_erro(client):
    r = client.post("/", data={"origem": "GRU", "destino": "LIS", "ida": "data-errada"})
    assert "inválidos".encode() in r.data


def test_endpoint_png(client):
    r = client.get("/qr.png?origem=GRU&destino=LIS&ida=2026-12-10")
    assert r.status_code == 200
    assert r.mimetype == "image/png"


def test_endpoint_png_invalido(client):
    assert client.get("/qr.png?origem=GRU&destino=GRU&ida=2026-12-10").status_code == 400
