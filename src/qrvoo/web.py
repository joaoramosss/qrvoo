"""Interface web (Flask)."""

from __future__ import annotations

from datetime import date

from flask import Flask, Response, render_template, request

from qrvoo import __version__
from qrvoo.links import SITES, BuscaVoo, montar_url
from qrvoo.qr import gerar_png, png_base64


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "ok", "versao": __version__}

    @app.route("/", methods=["GET", "POST"])
    def index():
        contexto = {"sites": SITES, "versao": __version__, "form": request.form}
        if request.method == "POST":
            try:
                busca = _busca_do_form(request.form)
                url = montar_url(request.form.get("site", "skyscanner"), busca)
                contexto.update(url=url, qr=png_base64(url))
            except ValueError as erro:
                contexto["erro"] = str(erro)
        return render_template("index.html", **contexto)

    @app.get("/qr.png")
    def qr_png():
        try:
            busca = _busca_do_form(request.args)
            url = montar_url(request.args.get("site", "skyscanner"), busca)
        except ValueError as erro:
            return {"erro": str(erro)}, 400
        return Response(gerar_png(url), mimetype="image/png")

    return app


def _busca_do_form(dados) -> BuscaVoo:
    try:
        ida = date.fromisoformat(dados.get("ida", ""))
        volta_txt = dados.get("volta") or ""
        volta = date.fromisoformat(volta_txt) if volta_txt else None
        adultos = int(dados.get("adultos", 1))
    except (TypeError, ValueError) as exc:
        raise ValueError("Datas ou número de adultos inválidos.") from exc
    return BuscaVoo(dados.get("origem", ""), dados.get("destino", ""), ida, volta, adultos)


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # nosec B104
