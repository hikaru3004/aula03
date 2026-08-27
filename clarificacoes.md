# correcao.md

## 1. Análise de Gaps: `spec.md` vs. Código Atual

### Estado Atual do Repositório

| Arquivo | Descrição | Relacionado ao Spec? |
| :--- | :--- | :---: |
| `converte.py` | Conversor de temperatura CLI | ❌ Não |
| `media_ponderada.py` | Função simples de média ponderada | ⚠️ Parcial (apenas cálculo base) |
| `test_converte.py` | Testes do conversor | ❌ Não |

---

### O que Falta Implementar (Baseado no `spec.md`)

* **Entidades e Cadastros (RF01):**
  * **Turma:** Nome, limite de aprovação, limite de exame, avaliações com pesos.
  * **Aluno:** Nome, turma, notas por avaliação.
  * **Avaliação:** Nome, peso.
* **Lançamento de Notas (RF02):**
  * CRUD de notas (0.0 a 10.0) por aluno e avaliação.
  * Validação de intervalo de valores.
* **Cálculo de Média (RF03):**
  * Média ponderada considerando apenas avaliações lançadas (excluindo pendentes).
  * Classificação em Aprovado, Exame ou Reprovado.
  * Definir status como "Pendente" para alunos sem notas.
* **Estatísticas (RF04):**
  * Média geral da turma e mediana.
  * Distribuição percentual de status.
  * Alerta de "Zona de Risco": média no intervalo $[limite - 0.50, limite)$.
* **Persistência (RF05):**
  * Leitura e gravação automática em arquivo JSON na pasta `data/`.
* **Validação (RF06):**
  * Rejeição de entradas inválidas com mensagens explicativas.

---

## 2. Decisões Técnicas e Clarificações

### Matriz de Decisões Técnicas

| Decisão | Opções | Recomendação |
| :--- | :--- | :--- |
| **Estrutura de Módulos** | Monolito (`main.py`) vs. Pacote (`core/` + `cli/`) | Pacote separado (Business logic isolada da CLI) |
| **Formato JSON** | Arquivo único (`data/sistema.json`) vs. Múltiplos | Arquivo único com estrutura aninhada |
| **CLI Framework** | `argparse` (stdlib) vs. `click`/`typer` (externo) | `argparse` (conforme diretriz de zero dependências externas) |
| **IDs de Entidades** | UUID vs. Inteiro auto-incremento | Inteiro sequencial (simplicidade) |
| **Mediana** | `statistics.median` (stdlib) vs. Implementação manual | `statistics.median` |

---

### Respostas às Perguntas Diretas

1. **Remoção de `converte.py` e `test_converte.py`:** Não remover. Fazem parte de outro processo e devem continuar no repositório.
2. **Reaproveitamento de `media_ponderada.py`:** Criar um novo módulo em `core/calculos.py`. O arquivo atual foi utilizado em outro fluxo.
3. **Estrutura de Pastas:** Mantida a arquitetura modular em `core/` e `cli/`.
4. **Escopo de Turmas:** Execução em modo *single-turma* ativa.
5. **Zona de Risco:** Ajustar a lógica para cobrir a faixa crítica de risco.

---

## 3. Ponto de Conflito: Critério de Aceite 4 (Zona de Risco)

* **`spec.md` (Original):** Para limite 7.0, um aluno com média 6.60 entra na Zona de Risco, enquanto 6.40 fica fora.
  $$\text{Risco} = [limite - 0.50, limite)$$
* **Ajuste Solicitado:** Faixa cobrindo de 4.0 a 5.0.

### Opções de Implementação

| Opção | Limite de Aprovação | Faixa de Risco |
| :--- | :--- | :--- |
| **A (Spec Original)** | Configurável (ex: 7.0) | Margem fixa de $0.50$ ponto abaixo do limite |
| **B (Sugestão)** | Fixo em 5.0 | Intervalo de 1.0 ponto ($4.0$ a $5.0$) |
| **C (Híbrida - Selecionada)** | Configurável (padrão 5.0) | Margem fixa de $0.50$ ponto abaixo do limite configurado |

> **Decisão:** Adotada a **Opção C**. O limite de aprovação permanece configurável por turma (conforme RF01), mantendo a régua da Zona de Risco em $0.50$ ponto abaixo do limite estabelecido.

---

## 4. Plano de Execução Atualizado

### Estrutura de Arquivos do Projeto

```text
aula03/
├── main.py                 # Entrypoint CLI (argparse)
├── core/
│   ├── __init__.py
│   ├── models.py           # Dataclasses: Turma, Aluno, Avaliacao, Nota
│   ├── storage.py          # Leitura e escrita JSON em data/
│   ├── calculos.py         # Média ponderada, classificação e estatísticas
│   └── validacao.py        # Validadores de faixa (0-10), pesos e limites
├── cli/
│   ├── __init__.py
│   └── commands.py         # Handlers dos subcomandos argparse
├── data/                   # Arquivo JSON persistido (data/sistema.json)
├── converte.py             # Mantido
├── test_converte.py        # Mantido
├── media_ponderada.py      # Mantido
└── test_notas.py           # Testes automatizados do sistema de notas
