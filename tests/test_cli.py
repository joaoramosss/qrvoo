from qrvoo.cli import main


def test_cli_gera_arquivo(tmp_path, capsys):
    saida = tmp_path / "voo.png"
    codigo = main(["GRU", "LIS", "2026-12-10", "--volta", "2026-12-20", "-o", str(saida)])
    assert codigo == 0
    assert saida.exists()
    assert "skyscanner" in capsys.readouterr().out


def test_cli_erro_validacao(tmp_path, capsys):
    codigo = main(["GRU", "GRU", "2026-12-10", "-o", str(tmp_path / "x.png")])
    assert codigo == 1
    assert "Erro" in capsys.readouterr().out
