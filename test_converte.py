import pytest

from converte import ZERO_ABSOLUTO_C, de_celsius, main, para_celsius, validar_unidade, validar_valor


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("25", 25.0),
        ("-40", -40.0),
        ("-40,5", -40.5),
        ("0", 0.0),
        ("1e3", 1000.0),
        (" 36,6 ", 36.6),
    ],
)
def test_validar_valor_aceita(texto, esperado):
    assert validar_valor(texto) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "texto",
    [
        "abc",
        "",
        "12c",
        "--5",
        "nan",
        "NaN",
        "inf",
        "-inf",
        "infinity",
    ],
)
def test_validar_valor_rejeita(texto):
    with pytest.raises(ValueError):
        validar_valor(texto)


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("c", "C"),
        ("f", "F"),
        ("K", "K"),
    ],
)
def test_validar_unidade_aceita(texto, esperado):
    assert validar_unidade(texto, "origem") == esperado


def test_validar_unidade_rejeita_desconhecida():
    with pytest.raises(ValueError, match="desconhecida"):
        validar_unidade("X", "origem")


@pytest.mark.parametrize(
    "valor, unidade, esperado",
    [
        (100, "C", 100.0),
        (212, "F", 100.0),
        (0, "K", -273.15),
    ],
)
def test_para_celsius(valor, unidade, esperado):
    assert para_celsius(valor, unidade) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "valor_c, unidade, esperado",
    [
        (100, "C", 100.0),
        (100, "F", 212.0),
        (-273.15, "K", 0.0),
    ],
)
def test_de_celsius(valor_c, unidade, esperado):
    assert de_celsius(valor_c, unidade) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "argumentos, esperado",
    [
        (["100", "C", "F"], 212.0),
        (["32", "F", "C"], 0.0),
        (["-40", "c", "f"], -40.0),
        (["36,6", "C", "F"], 97.88),
        (["0", "k", "c"], -273.15),
        ([str(ZERO_ABSOLUTO_C), "C", "K"], 0.0),
    ],
)
def test_main_conversao_valida(capsys, argumentos, esperado):
    assert main(argumentos) == 0
    capturado = capsys.readouterr()
    assert float(capturado.out.strip()) == pytest.approx(esperado)
    assert capturado.err == ""


@pytest.mark.parametrize(
    "argumentos, trecho_esperado",
    [
        (["25"], "Uso"),
        (["25", "C"], "Uso"),
        (["25", "C", "F", "extra"], "Uso"),
        (["abc", "C", "F"], "não é um número válido"),
        (["", "C", "F"], "não é um número válido"),
        (["12c", "C", "F"], "não é um número válido"),
        (["nan", "C", "F"], "não é um número finito"),
        (["inf", "K", "C"], "não é um número finito"),
        (["25", "X", "F"], "unidade de origem 'X' é desconhecida"),
        (["25", "x", "F"], "unidade de origem 'X' é desconhecida"),
        (["25", "C", "X"], "unidade de destino 'X' é desconhecida"),
        (["-300", "C", "F"], "abaixo do zero absoluto"),
        (["-500", "F", "K"], "abaixo do zero absoluto"),
    ],
)
def test_main_rejeita_entrada_invalida(capsys, argumentos, trecho_esperado):
    assert main(argumentos) == 1
    capturado = capsys.readouterr()
    assert trecho_esperado in capturado.err
    assert capturado.out == ""
