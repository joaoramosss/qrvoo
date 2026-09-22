"""Geração da imagem do QR Code."""

from __future__ import annotations

import base64
import io
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M


def gerar_png(conteudo: str, tamanho_caixa: int = 10, borda: int = 4) -> bytes:
    if not conteudo:
        raise ValueError("Conteúdo do QR Code não pode ser vazio.")
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=tamanho_caixa, border=borda)
    qr.add_data(conteudo)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()


def salvar_png(conteudo: str, destino: str | Path) -> Path:
    caminho = Path(destino)
    caminho.write_bytes(gerar_png(conteudo))
    return caminho


def png_base64(conteudo: str) -> str:
    return base64.b64encode(gerar_png(conteudo)).decode("ascii")
