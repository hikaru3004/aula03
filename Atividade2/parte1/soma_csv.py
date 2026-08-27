#!/usr/bin/env python3
"""
soma_csv.py — Soma coluna 'valor' de CSV com colunas data,produto,valor.
Sem bibliotecas externas (apenas csv da biblioteca padrão).

Uso:
    python soma_csv.py dados.csv
    python soma_csv.py dados.csv --coluna valor
"""

import csv
import sys


def somar_valores(caminho: str, coluna: str = "valor") -> float:
    """Lê CSV e soma valores da coluna informada. Retorna float."""
    total = 0.0
    with open(caminho, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)

        if leitor.fieldnames is None:
            raise ValueError("CSV vazio ou sem cabeçalho")

        # normaliza nomes para detectar coluna (case-insensitive / strip)
        mapa = {h.strip().lower(): h for h in leitor.fieldnames}
        chave = mapa.get(coluna.strip().lower())
        if chave is None:
            raise ValueError(
                f"Coluna '{coluna}' não encontrada. Colunas disponíveis: {', '.join(leitor.fieldnames)}"
            )

        for i, linha in enumerate(leitor, start=2):
            raw = linha.get(chave, "")
            if raw is None or str(raw).strip() == "":
                continue  # ignora linha vazia
            texto = str(raw).strip().replace(",", ".")
            try:
                total += float(texto)
            except ValueError:
                raise ValueError(
                    f"Valor inválido na linha {i}, coluna '{chave}': '{raw}'"
                )
    return total


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(f"Uso: python {sys.argv[0]} <arquivo.csv> [coluna]", file=sys.stderr)
        print("Exemplo: python soma_csv.py dados.csv", file=sys.stderr)
        sys.exit(0 if len(sys.argv) >= 2 else 1)

    caminho = sys.argv[1]
    coluna = sys.argv[2] if len(sys.argv) >= 3 else "valor"

    # suporte a --coluna valor
    if coluna == "--coluna" and len(sys.argv) >= 4:
        coluna = sys.argv[3]

    try:
        total = somar_valores(caminho, coluna)
    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado '{caminho}'", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

    print(total)


if __name__ == "__main__":
    main()
