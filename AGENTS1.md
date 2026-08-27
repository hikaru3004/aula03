# AGENTS.md

## Estrutura e Arquivos
- `converte.py`: CLI de conversão de temperatura (C, F, K).
- `test_converte.py`: Suíte de testes do conversor.
- `media_ponderada.py`: Cálculo de média ponderada (contém testes inline em `__main__`).

## Comandos Principais
```bash
# Rodar todos os testes
pytest

# Executar CLI
python converte.py <valor> <origem> <destino>