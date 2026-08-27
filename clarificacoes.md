# clarificações.md

> + Thought: 9.1s

## Análise de Gaps: Spec.md vs Código Atual

### Estado Atual do Repositório

| Arquivo | Descrição | Relacionado ao Spec? |
| :--- | :--- | :--- |
| `converte.py` | Conversor de temperatura CLI | ❌ Não relacionado |
| `media_ponderada.py` | Função simples de média ponderada | ⚠️ Parcial (apenas cálculo base) |
| `test_converte.py` | Testes do conversor | ❌ Não relacionado |

---

### O que falta implementar (baseado no spec.md)

+ **Entidades/Cadastros (RF01):**
  + **Turma:** nome, limite aprovação, limite exame, avaliações com pesos
  + **Aluno:** nome, turma, notas por avaliação
  + **Avaliação:** nome, peso
+ **Lançamento de Notas (RF02):**
  + CRUD de notas (0.0 a 10.0) por aluno/avaliação
  + Validação de range
+ **Cálculo de Média (RF03):**
  + Média ponderada apenas sobre avaliações lançadas (pendentes excluídas)
  + Classificação: Aprovado / Exame / Reprovado
  + Status "Pendente" se sem notas
+ **Estatísticas (RF04):**
  + Média da turma, mediana
  + Distribuição percentual (Aprovado/Exame/Reprovado)
  + Alerta "Zona de Risco": média ≥ (limite_aprovação - 0.50)
+ **Persistência (RF05):**
  + JSON em `data/` com load/save automático
+ **Validação (RF06):**
  + Entradas inválidas com mensagens descritivas

---

### Decisões Técnicas a Confirmar

| Decisão | Opções | Recomendação |
| :--- | :--- | :--- |
| Estrutura de módulos | Monolito `main.py` vs pacote `core/` + `cli/` | Pacote separado (business logic separada da CLI) |
| Formato JSON | Um arquivo `data/sistema.json` vs múltiplos | Arquivo único com estrutura aninhada |
| CLI Framework | `argparse` (stdlib) vs `click`/`typer` (externo) | `argparse` (conforme "Nunca: bibliotecas externas") |
| IDs de entidades | UUID vs inteiro auto-incremento | Inteiro sequencial (simplicidade) |
| Mediana | `statistics.median` (stdlib) vs implementação manual | `statistics.median` (stdlib disponível) |

---

### Perguntas Diretas

1. O `converte.py` e `test_converte.py` devem ser removidos? São irrelevantes para o spec.
2. O `media_ponderada.py` deve ser reaproveitado ou reescrito? A função atual não trata "avaliações pendentes" nem validação 0-10.
3. Estrutura de pastas preferida?

```text
aula03/
├── main.py           # entrypoint CLI
├── core/
│   ├── models.py     # dataclasses: Turma, Aluno, Avaliacao
│   ├── storage.py    # JSON load/save
│   ├── calculos.py   # média, classificação, estatísticas
│   └── validacao.py  # validadores
├── cli/
│   └── commands.py   # argparse handlers
└── data/             # JSON persistido
```

   Como lidar com "turma" no CLI? Um sistema multi-turma ou single-turma ativa por execução?
5. Critério "Zona de Risco" (CA4): Alerta só para alunos com média entre [limite-0.50, limite)? Confirma: 6.60 entra (limite 7.0), 6.40 não entra?

---

### Plano de Execução em Etapas

+ **Etapa 1: Fundação e Modelos**
  + Remover `converte.py`, `test_converte.py` (confirmar)
  + Criar estrutura de pastas `core/`, `cli/`, `data/`
  + Definir dataclasses em `core/models.py`: Turma, Aluno, Avaliacao, Nota
  + Implementar `core/storage.py`: `carregar()`, `salvar()`, `inicializar_data()`
  + Testes: persistência round-trip (CA5)
+ **Etapa 2: Validação e Cadastros (RF01, RF06)**
  + `core/validacao.py`: validadores de nota (0-10), peso (>0), limites
  + CLI commands: `turma criar`, `turma listar`, `aluno adicionar`, `avaliacao adicionar`
  + Testes: rejeição nota -1 e 11 (CA1)
+ **Etapa 3: Lançamento de Notas (RF02)**
  + CLI: `nota lancar <aluno> <avaliacao> <valor>`, `nota editar`, `nota remover`
  + Validação: aluno existe, avaliação existe na turma, nota 0-10
  + Persistência automática após cada operação
+ **Etapa 4: Cálculo de Média e Classificação (RF03, CA2, CA3)**
  + `core/calculos.py`: `calcular_media(aluno, turma)` → ignora pendentes
  + `classificar(media, turma)` → Aprovado/Exame/Reprovado
  + Testes: CA2 (pesos 2+3, notas 8+6 = 6.80), CA3 (parcial apenas P1 = 8.00)
+ **Etapa 5: Estatísticas e Alertas (RF04, CA4)**
  + `estatisticas_turma(turma)` → média, mediana, distribuição %, zona de risco
  + CLI: `relatorio turma`, `relatorio aluno <id>`
  + Testes: CA4 (limite 7.0, 6.60 = risco, 6.40 = sem risco)
+ **Etapa 6: Integração e Testes Finais**
  + `main.py` entrypoint com `argparse` subcommands
  + Testes E2E: fluxo completo turma → alunos → avaliações → notas → relatório
  + Verificar todos os 5 Critérios de Aceite passam

---

### Estimativa de Esforço

| Etapa | Complexidade |
| :--- | :--- |
| 1. Fundação | Baixa |
| 2. Cadastros/Validação | Média |
| 3. Lançamento Notas | Média |
| 4. Cálculo/Classificação | Média |
| 5. Estatísticas | Alta |
| 6. Integração | Baixa |
| **Total** | **~40-70 testes** |

**Próximo passo:** Confirmar as 5 perguntas acima e autorizar início da Etapa 1.

---

### Respostas do Usuário

1. não devem, fazem parte de outro processo, pode manter esses arquivos na pasta.
2. crie outro arquivo este foi utilizado para outro fluxo também.
3. pode seguir essa estrutura
4. pode ser single-turma
5. pode aumentar o limite para cobrir a área de risco de reprovação então entre 5,0 e 4,0

---

> + Thought: 1m 18s

Obrigado pelas respostas. Tenho uma dúvida crítica sobre o Critério de Aceite 4 (Zona de Risco):

### Ponto de Conflito: CA4 - Zona de Risco

+ **Spec.md (linha 21):**
  "Para limite 7.0, aluno com média 6.60 entra na 'Zona de Risco'; aluno com 6.40 não entra"
  → Regra: risco = [limite - 0.50, limite) → faixa de 0.50 ponto
+ **Sua resposta:**
  "pode aumentar o limite para cobrir a área de risco de reprovação então entre 5,0 e 4,0"
  → Faixa de 1.0 ponto (4.0 a 5.0), não 0.50

**Pergunta Decisiva**
Qual deve ser a regra implementada?

| Opção | Limite Aprovação |
| :--- | :--- |
| **A (Spec original)** | Configurável (ex: 7.0) |
| **B (Sua sugestão)** | 5.0 fixo |
| **C (Híbrida)** | Configurável (padrão 5.0) |

Recomendo Opção C - limite configurável por turma (conforme RF01), risco sempre 0.50 abaixo do limite. O CA4 valida a lógica, não o valor fixo.

---

## Plano Atualizado (incorporando suas respostas)

### Estrutura Final

```text
aula03/
├── main.py                 # entrypoint CLI (argparse)
├── core/
│   ├── __init__.py
│   ├── models.py           # Turma, Aluno, Avaliacao, Nota (dataclasses)
│   ├── storage.py          # JSON load/save em data/
│   ├── calculos.py         # média ponderada, classificação, estatísticas
│   └── validacao.py        # validadores 0-10, pesos, limites
├── cli/
│   ├── __init__.py
│   └── commands.py         # handlers dos subcomandos
├── data/                   # JSON persistido (gitignored)
├── converte.py             # mantido (outro processo)
├── test_converte.py        # mantido (outro processo)
├── media_ponderada.py      # mantido (outro fluxo)
└── test_notas.py           # NOVO - testes do sistema de notas
```

### Fluxo Single-Turma

+ Sistema carrega/cria `data/sistema.json` com uma turma ativa
+ Todos comandos operam sobre essa turma
+ `turma configurar` permite alterar limites/pesos

### Critérios de Aceite - Mapeamento para Testes

| CA | Teste |
| :--- | :--- |
| **CA1** | `test_nota_rejeita_fora_faixa(-1)`, `test_nota_rejeita_fora_faixa(11)` |
| **CA2** | `test_media_ponderada_pesos_2_e_3()` → 6.80 |
| **CA3** | `test_media_parcial_apenas_p1()` → 8.00 |
| **CA4** | `test_zona_risco_limite_7_entra(6.60)`, `test_zona_risco_limite_7_nao_entra(6.40)` |
| **CA5** | `test_persistencia_reinicio_mantem_dados()` |

### Próximos Passos

1. Confirmar Opção C para Zona de Risco (regra 0.50, limite configurável)
2. Autorizar início da Etapa 1: Fundação e Modelos

Quer que eu prossiga com a Opção C?
