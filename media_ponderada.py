def media_ponderada(notas, pesos):
    if len(notas) != len(pesos):
        raise ValueError("notas e pesos devem ter o mesmo tamanho")
    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        raise ValueError("a soma dos pesos não pode ser zero")
    return sum(n * p for n, p in zip(notas, pesos)) / soma_pesos


if __name__ == "__main__":
    assert media_ponderada([8, 7, 9], [3, 3, 4]) == 8.1
    try:
        media_ponderada([8, 7], [3, 3, 4])
    except ValueError:
        pass
    else:
        raise AssertionError("deveria levantar ValueError")
    try:
        media_ponderada([8, 7, 9], [1, -1, 0])
    except ValueError:
        pass
    else:
        raise AssertionError("deveria levantar ValueError")
    print("todos os testes passaram")
