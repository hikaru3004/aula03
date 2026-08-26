import math
import sys

ZERO_ABSOLUTO_C = -273.15
UNIDADES_VALIDAS = ("C", "F", "K")


def validar_valor(texto):
    try:
        valor = float(texto.replace(",", "."))
    except ValueError:
        raise ValueError(f"'{texto}' não é um número válido.") from None
    if not math.isfinite(valor):
        raise ValueError(f"'{texto}' não é um número finito.")
    return valor


def validar_unidade(texto, rotulo):
    unidade = texto.upper()
    if unidade not in UNIDADES_VALIDAS:
        raise ValueError(f"unidade de {rotulo} '{unidade}' é desconhecida.")
    return unidade


def para_celsius(valor, unidade):
    if unidade == "F":
        return (valor - 32) * 5 / 9
    if unidade == "K":
        return valor - 273.15
    return valor


def de_celsius(valor_c, unidade):
    if unidade == "F":
        return valor_c * 9 / 5 + 32
    if unidade == "K":
        return valor_c + 273.15
    return valor_c


def mostrar_uso():
    print("Uso: python converte.py <temperatura> <origem> <destino>", file=sys.stderr)
    print(f"Unidades válidas: {', '.join(UNIDADES_VALIDAS)}", file=sys.stderr)


def main(argumentos):
    if len(argumentos) != 3:
        mostrar_uso()
        return 1

    texto_valor, origem, destino = argumentos

    try:
        valor = validar_valor(texto_valor)
    except ValueError as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1

    lista_unidades = ", ".join(UNIDADES_VALIDAS)

    try:
        origem = validar_unidade(origem, "origem")
        destino = validar_unidade(destino, "destino")
    except ValueError as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        print(f"Unidades válidas: {lista_unidades}", file=sys.stderr)
        return 1

    valor_c = para_celsius(valor, origem)
    if valor_c < ZERO_ABSOLUTO_C:
        print(
            f"Erro: {valor} °{origem} equivale a {valor_c:.2f} °C, "
            f"abaixo do zero absoluto ({ZERO_ABSOLUTO_C} °C).",
            file=sys.stderr,
        )
        return 1

    resultado = de_celsius(valor_c, destino)
    print(round(resultado, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
