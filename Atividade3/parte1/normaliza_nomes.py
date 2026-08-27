#!/usr/bin/env python3
"""
normaliza_nomes.py — normalização mínima de nomes para exibição.
Decisões explicitadas abaixo (não estavam no pedido).
"""

CONECTORES = {"da", "de", "do", "das", "dos", "e", "d'", "d’"}

def _capitaliza_palavra(palavra: str, manter_minusculo: bool) -> str:
    """Capitaliza palavra, preservando hífen e apóstrofo."""
    if manter_minusculo:
        return palavra.lower()
    # trata hífen: maria-joana -> Maria-Joana
    # e apóstrofo: d'ávila -> D'Ávila
    # str.title() já faz isso corretamente para ASCII, mas implementamos
    # manualmente para controle
    def cap(parte: str) -> str:
        return parte[:1].upper() + parte[1:].lower() if parte else ""

    # separa por hífen mas preserva hífen
    if "-" in palavra:
        return "-".join(cap(p) for p in palavra.split("-"))
    if "'" in palavra:
        return "'".join(cap(p) for p in palavra.split("'"))
    if "’" in palavra:  # apóstrofo curvo
        return "’".join(cap(p) for p in palavra.split("’"))
    return cap(palavra)


def normalizar_nome(nome: str) -> str:
    """
    Normaliza nome para exibição.

    Comportamento:
    - remove espaços no início/fim (strip)
    - colapsa múltiplos espaços/\\t/\\n em um só
    - capitaliza cada palavra (title case)
    - mantém conectores em minúsculo: da, de, do, das, dos, e
      (exceto quando são a primeira palavra)
    - preserva hífen: "maria-joana" -> "Maria-Joana"

    Ex:
        "  MARIA   da  SILVA " -> "Maria da Silva"
        "joão   de souza" -> "João de Souza"
        "ANA PAULA" -> "Ana Paula"

    Decisões explicitadas (não estavam no pedido):
    - conectores escolhidos para padrão brasileiro ABNT
    - TypeError se entrada não for str
    - retorna "" para string vazia/só espaços
    """
    if not isinstance(nome, str):
        raise TypeError(f"nome deve ser str, recebido {type(nome).__name__}")
    # strip + split colapsa espaços (inclui \t, \n)
    partes = nome.strip().split()
    if not partes:
        return ""
    normalizadas: list[str] = []
    for i, p in enumerate(partes):
        eh_conector = p.lower() in CONECTORES
        manter_minusculo = eh_conector and i != 0
        # title para comparação, mas usa capitalização controlada
        # para não perder hífen/apóstrofo
        normalizadas.append(_capitaliza_palavra(p, manter_minusculo))
    return " ".join(normalizadas)


if __name__ == "__main__":
    exemplos = [
        "  MARIA   da  SILVA ",
        "joão   de souza",
        "ANA PAULA",
        "  ",
        "maria-joana dos santos",
        "  JOÃO  D'ÁVILA  ",
        "CARLOS e SILVA",
        "PEDRO DE ALCANTARA e SILVA",  # conector na 1ª posição fica capitalizado
    ]
    for e in exemplos:
        print(f"{e!r} -> {normalizar_nome(e)!r}")
