# AGENTS.md

## Visão Geral do Projeto
Exercícios Python da "aula03". Dois módulos principais:
- `converte.py` - Conversor CLI de temperatura (C/F/K)
- `media_ponderada.py` - Função de média ponderada

## Comandos
```bash
# Executar testes (pytest)
pytest

# Executar arquivo de teste específico
pytest test_converte.py

# Executar teste único
pytest test_converte.py::test_validar_valor_aceita

# Executar CLI do converte.py
python converte.py <temp> <origem> <destino>
# Exemplo: python converte.py 100 C F
```

## Testes
- Usa pytest com `pytest.approx` para comparações de float
- Testes em `test_converte.py` cobrem validação, lógica de conversão e CLI main()
- `media_ponderada.py` tem asserts inline no `__main__` (sem arquivo de teste separado)

## Convenções
- Mensagens de erro e nomes de variáveis em português
- Vírgula como separador decimal aceita (ex: "36,6")
- Unidades válidas: C, F, K (case-insensitive)
- Validação de zero absoluto (-273.15°C)

## Arquivos a ignorar
- `__pycache__/`
- `.pytest_cache/`