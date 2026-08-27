#!/usr/bin/env python3
"""
normaliza_nomes.py — normalização de nomes para exibição.
"""

CONECTORES = {"da", "de", "do", "das", "dos", "e", "d'", "d’"}

def _capitaliza_palavra(palavra: str, manter_minusculo: bool) -> str:
    """Capitaliza palavra, preservando hífen e apóstrofo."""
    if manter_minusculo:
        return palavra.lower()
    def cap(parte: str) -> str:
        return parte[:1].upper() + parte[1:].lower() if parte else ""
    if "-" in palavra:
        return "-".join(cap(p) for p in palavra.split("-"))
    if "'" in palavra:
        return "'".join(cap(p) for p in palavra.split("'"))
    if "’" in palavra:
        return "’".join(cap(p) for p in palavra.split("’"))
    return cap(palavra)


def normalizar_nome(nome: str) -> str:
    """
    Normaliza nome para exibição.

    - remove espaços no início/fim (strip)
    - colapsa múltiplos espaços/\\t/\\n em um só
    - capitaliza cada palavra (title case)
    - mantém conectores em minúsculo: da, de, do, das, dos, e
      (exceto quando são a primeira palavra)

    Ex:
        "  ana  MARIA silva " -> "Ana Maria Silva"
        "JOSE DOS SANTOS" -> "Jose dos Santos"
        "maria  da  CONCEICAO" -> "Maria da Conceicao"
    """
    if not isinstance(nome, str):
        raise TypeError(f"nome deve ser str, recebido {type(nome).__name__}")
    partes = nome.strip().split()
    if not partes:
        return ""
    normalizadas: list[str] = []
    for i, p in enumerate(partes):
        eh_conector = p.lower() in CONECTORES
        manter_minusculo = eh_conector and i != 0
        normalizadas.append(_capitaliza_palavra(p, manter_minusculo))
    return " ".join(normalizadas)


if __name__ == "__main__":
    testes = [
        ("  ana  MARIA silva ", "Ana Maria Silva"),
        ("JOSE DOS SANTOS", "Jose dos Santos"),
        ("PEDRO DE ALCANTARA e SILVA", "Pedro de alcantara e Silva"),
    ]
    for entrada, esperado in testes:
        saida = normalizar_nome(entrada)
        status = "OK" if saida == esperado else "FALHOU"
        print(f"{status}: {entrada!r} -> {saida!r} (esperado {esperado!r})")
