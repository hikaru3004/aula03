# spec.md

# Especificação Funcional: Sistema de Acompanhamento de Notas

## 1. Visão Geral e Arquitetura
* **Plataforma:** Interface de Linha de Comando (CLI) baseada em Python.
* **Persistência:** Arquivos JSON locais armazenados no diretório `data/` (`data/sistema.json`).
* **Arredondamento:** Médias calculadas e exibidas com 2 casas decimais via arredondamento padrão *half-up* (`ROUND_HALF_UP`).
* **Avaliações Pendentes:** Excluídas do cálculo da média ponderada e do somatório de pesos. Alunos sem nenhuma nota lançada assumem status `Pendente`.

---

## 2. Requisitos Funcionais

| Código | Requisito | Descrição Detalhada |
| :---: | :--- | :--- |
| **RF01** | **Cadastros** | Gestão de Turmas (com limites de aprovação e exame configuráveis, além de avaliações com pesos flexíveis), Alunos e Avaliações. |
| **RF02** | **Lançamento de Notas** | Registro, edição e remoção de notas no intervalo de $0.0$ a $10.0$. |
| **RF03** | **Cálculo de Média** | Cálculo de média ponderada apenas sobre avaliações lançadas e classificação automática (*Aprovado*, *Exame*, *Reprovado*). |
| **RF04** | **Estatísticas** | Exibição da média geral da turma, mediana, distribuição percentual de status e alerta para alunos situados na Zona de Risco. |
| **RF05** | **Persistência** | Carregamento e salvamento automático do arquivo JSON a cada alteração efetuada. |
| **RF06** | **Validação** | Rejeição de entradas inválidas (notas fora da faixa, nomes/CPFs duplicados) com mensagens descritivas. |

---

## 3. Regras de Negócio e Definições Matemáticas

### 3.1. Cálculo da Média Ponderada Parcial
$$\text{Média} = \frac{\sum (\text{Nota}_i \times \text{Peso}_i)}{\sum \text{Peso}_i}$$
*(Considerando apenas as avaliações $i$ que possuem nota efetivamente registrada).*

### 3.2. Regras de Classificação
* **Aprovado:** $\text{Média} \ge \text{Limite de Aprovação}$
* **Exame:** $\text{Limite de Exame} \le \text{Média} < \text{Limite de Aprovação}$
* **Reprovado:** $\text{Média} < \text{Limite de Exame}$
* **Pendente:** Nenhuma avaliação com nota lançada.

### 3.3. Intervalo da Zona de Risco
$$\text{Zona de Risco} = [\text{Limite de Aprovação} - 0.50, \text{Limite de Aprovação})$$

---

## 4. Critérios de Aceite Verificáveis (CA)

1. **CA1 - Validação de Faixa de Nota:**
   * Tentar registrar notas como $-1.0$ ou $11.0$ exibe mensagem de erro explicativa e rejeita a alteração.

2. **CA2 - Cálculo de Média Ponderada:**
   * Em uma turma com P1 (peso 2) e P2 (peso 3), as notas $8.0$ e $6.0$ geram a média **$6.80$** ($\frac{8\cdot2 + 6\cdot3}{2+3} = 6.80$).

3. **CA3 - Média Parcial com Notas Pendentes:**
   * Se apenas a P1 (nota $8.0$, peso 2) estiver lançada e a P2 pendente, a média parcial resulta em **$8.00$**.

4. **CA4 - Alerta de Zona de Risco:**
   * Para uma turma com limite de aprovação de $7.0$:
     * Média $6.60$ é incluída na "Zona de Risco" ($6.60 \in [6.50, 7.00)$).
     * Média $6.40$ não entra na "Zona de Risco" ($6.40 < 6.50$).

5. **CA5 - Persistência de Dados:**
   * O encerramento e reinício da aplicação mantém a integridade de todos os dados armazenados em `data/sistema.json`.
  