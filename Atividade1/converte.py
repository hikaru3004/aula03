#!/usr/bin/env python3
"""
converte.py — Conversor de temperatura via linha de comando.

Converte entre Celsius (C), Fahrenheit (F) e Kelvin (K).

Uso:
    python converte.py <valor> <origem> <destino>
Exemplos:
    python converte.py 100 C F   -> 212.0
    python converte.py 0 C K     -> 273.15
    python converte.py 32 F C    -> 0.0

Validações (intencionais para aula):
    - número de argumentos
    - valor numérico
    - unidade conhecida (lista as válidas)
    - temperatura abaixo do zero absoluto (mensagem própria)
"""

import sys

UNIDADES_VALIDAS = ("C", "F", "K")
# Zero absoluto em cada escala
ZERO_ABSOLUTO = {
    "C": -273.15,
    "F": -459.67,
    "K": 0.0,
}


def celsius_para_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def fahrenheit_para_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_para_kelvin(c: float) -> float:
    return c + 273.15


def kelvin_para_celsius(k: float) -> float:
    return k - 273.15


def converter(valor: float, origem: str, destino: str) -> float:
    """Converte valor de origem para destino. Assume unidades já validadas."""
    if origem == destino:
        return float(valor)

    # normaliza para Celsius
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = fahrenheit_para_celsius(valor)
    elif origem == "K":
        celsius = kelvin_para_celsius(valor)
    else:
        # não deve chegar aqui se validação foi feita antes
        raise ValueError(f"Unidade desconhecida '{origem}'. Unidades válidas: {', '.join(UNIDADES_VALIDAS)}.")

    if destino == "C":
        return float(celsius)
    elif destino == "F":
        return float(celsius_para_fahrenheit(celsius))
    elif destino == "K":
        return float(celsius_para_kelvin(celsius))
    else:
        raise ValueError(f"Unidade desconhecida '{destino}'. Unidades válidas: {', '.join(UNIDADES_VALIDAS)}.")


def validar_unidade(unidade: str) -> str:
    """Valida e normaliza unidade. Retorna unidade em maiúsculo ou levanta ValueError."""
    u = unidade.strip().upper()
    if u not in UNIDADES_VALIDAS:
        raise ValueError(
            f"Erro: unidade desconhecida '{unidade}'. Unidades válidas: {', '.join(UNIDADES_VALIDAS)}."
        )
    return u


def validar_zero_absoluto(valor: float, unidade: str) -> None:
    """Recusa temperaturas abaixo do zero absoluto com mensagem própria."""
    limite = ZERO_ABSOLUTO[unidade]
    # pequena tolerância para erro de ponto flutuante
    if valor < limite - 1e-9:
        raise ValueError(
            f"Erro: temperatura abaixo do zero absoluto ({limite} {unidade}). "
            f"Zero absoluto = -273.15 C = -459.67 F = 0 K."
        )


def parse_valor(texto: str) -> float:
    """Converte texto para float, aceitando vírgula como separador decimal."""
    try:
        # aceita "25,5" como "25.5" para conveniência no Brasil
        return float(texto.strip().replace(",", "."))
    except ValueError:
        raise ValueError(
            f"Erro: valor de temperatura inválido '{texto}'. Use um número. Exemplo: 100"
        )


def imprimir_uso(erro: str | None = None) -> None:
    if erro:
        print(erro, file=sys.stderr)
    print("Uso: python converte.py <valor> <origem> <destino>", file=sys.stderr)
    print(f"  <valor>   : número (ex: 100, -40, 273.15)", file=sys.stderr)
    print(f"  <origem>  : unidade de origem ({', '.join(UNIDADES_VALIDAS)})", file=sys.stderr)
    print(f"  <destino> : unidade de destino ({', '.join(UNIDADES_VALIDAS)})", file=sys.stderr)
    print(f"Exemplo: python converte.py 100 C F", file=sys.stderr)


def main() -> None:
    args = sys.argv[1:]

    # ajuda
    if len(args) == 1 and args[0] in ("-h", "--help", "ajuda", "--ajuda"):
        imprimir_uso()
        sys.exit(0)

    if len(args) != 3:
        imprimir_uso(f"Erro: esperados 3 argumentos (<valor> <origem> <destino>), recebidos {len(args)}.")
        sys.exit(1)

    valor_txt, origem_txt, destino_txt = args

    # 1) valida valor numérico
    try:
        valor = parse_valor(valor_txt)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    # 2) valida unidades (mensagem lista as válidas)
    try:
        origem = validar_unidade(origem_txt)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    try:
        destino = validar_unidade(destino_txt)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    # 3) valida zero absoluto — mensagem própria e distinta
    try:
        validar_zero_absoluto(valor, origem)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    # 4) converte e imprime apenas o número (ex: 212.0)
    try:
        resultado = converter(valor, origem, destino)
    except ValueError as e:
        # fallback — não deve ocorrer pois já validamos
        print(e, file=sys.stderr)
        sys.exit(1)

    # Imprime como float para garantir "212.0" em vez de "212"
    # Mantém representação padrão do Python; ex: 212.0, 273.15, 0.0
    print(float(resultado))


if __name__ == "__main__":
    main()
