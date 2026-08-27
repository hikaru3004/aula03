#!/usr/bin/env python3
"""
soma_csv.py — Soma a coluna 'valor' de um CSV com colunas data,produto,valor.

Uso:
    python soma_csv.py dados.csv
    python soma_csv.py  # usa dados.csv no mesmo diretório por padrão

Requisitos: apenas biblioteca padrão (csv, sys).
"""

import csv
import sys


def somar_valores(caminho: str) -> float:
    total = 0.0
    with open(caminho, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        if leitor.fieldnames is None:
            raise ValueError(f"arquivo vazio ou sem cabeçalho: {caminho}")
        if "valor" not in leitor.fieldnames:
            raise ValueError(
                f"coluna 'valor' não encontrada. Colunas disponíveis: {', '.join(leitor.fieldnames)}"
            )
        for i, linha in enumerate(leitor, start=2):
            raw = linha.get("valor", "")
            if raw is None or raw.strip() == "":
                continue
            # aceita vírgula como separador decimal (ex: "10,5")
            texto = raw.strip().replace(",", ".")
            try:
                total += float(texto)
            except ValueError:
                raise ValueError(f"valor inválido na linha {i}: {raw!r}")
    return total


def main() -> None:
    caminho = sys.argv[1] if len(sys.argv) > 1 else "dados.csv"
    if len(sys.argv) > 2:
        print(f"Uso: python {sys.argv[0]} [arquivo.csv]", file=sys.stderr)
        sys.exit(1)
    try:
        total = somar_valores(caminho)
    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado '{caminho}'", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

    # imprime apenas o total
    # mantém .2f se quiser formatação monetária, mas imprime float cru para não inventar formato
    print(total)


if __name__ == "__main__":
    main()
