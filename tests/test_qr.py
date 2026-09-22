import base64

import pytest

from qrvoo.qr import gerar_png, png_base64, salvar_png

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def test_gerar_png():
    assert gerar_png("https://example.com").startswith(PNG_MAGIC)


def test_png_base64():
    assert base64.b64decode(png_base64("abc")).startswith(PNG_MAGIC)


def test_salvar_png(tmp_path):
    caminho = salvar_png("https://example.com", tmp_path / "qr.png")
    assert caminho.read_bytes().startswith(PNG_MAGIC)


def test_conteudo_vazio():
    with pytest.raises(ValueError):
        gerar_png("")
