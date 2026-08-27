#!/usr/bin/env python3
"""
Conversor de Temperatura - Aula 03
Converte entre Celsius (C), Fahrenheit (F) e Kelvin (K).

Uso como módulo:
    from conversor_temperatura import celsius_para_fahrenheit

Uso via CLI:
    python conversor_temperatura.py
"""

def celsius_para_fahrenheit(c: float) -> float:
    return c * 9/5 + 32

def fahrenheit_para_celsius(f: float) -> float:
    return (f - 32) * 5/9

def celsius_para_kelvin(c: float) -> float:
    return c + 273.15

def kelvin_para_celsius(k: float) -> float:
    return k - 273.15

def fahrenheit_para_kelvin(f: float) -> float:
    return celsius_para_kelvin(fahrenheit_para_celsius(f))

def kelvin_para_fahrenheit(k: float) -> float:
    return celsius_para_fahrenheit(kelvin_para_celsius(k))

# Função genérica para qualquer conversão
def converter(valor: float, origem: str, destino: str) -> float:
    """
    Converte temperatura entre escalas.
    origem/destino: 'C', 'F' ou 'K' (case-insensitive)
    """
    origem = origem.upper().strip()
    destino = destino.upper().strip()

    if origem == destino:
        return valor

    # Normaliza para Celsius e depois converte para destino
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = fahrenheit_para_celsius(valor)
    elif origem == "K":
        celsius = kelvin_para_celsius(valor)
    else:
        raise ValueError(f"Escala de origem inválida: {origem}. Use C, F ou K.")

    if destino == "C":
        return celsius
    elif destino == "F":
        return celsius_para_fahrenheit(celsius)
    elif destino == "K":
        return celsius_para_kelvin(celsius)
    else:
        raise ValueError(f"Escala de destino inválida: {destino}. Use C, F ou K.")


def main():
    print("=== Conversor de Temperatura ===")
    print("Escalas disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")
    print("Digite 'sair' para encerrar.\n")

    while True:
        try:
            entrada = input("Valor (ou 'sair'): ").strip()
            if entrada.lower() == "sair":
                print("Até logo!")
                break

            valor = float(entrada.replace(",", "."))

            origem = input("Escala de origem (C/F/K): ").strip()
            destino = input("Escala de destino (C/F/K): ").strip()

            resultado = converter(valor, origem, destino)
            print(f"\n>> {valor:.2f}°{origem.upper()} = {resultado:.2f}°{destino.upper()}\n")

        except ValueError as e:
            print(f"Erro: {e}\n")
        except KeyboardInterrupt:
            print("\nEncerrado.")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
