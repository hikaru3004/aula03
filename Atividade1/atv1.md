# Exercício 1 — Conversor de Temperatura

## Passo 1 

Foi criado o arquivo:

```text
converte.py
```

---

## Passo 2 

### Especificações definidas

- **Linguagem:** Python.
- **Unidades:** Celsius (°C), Fahrenheit (°F) e Kelvin (K).
- **Formato de saída:** o valor deve ser apresentado com duas casas decimais.
  - Exemplo: `25.00°C = 77.00°F`.
- **Entrada inválida:** o programa deve capturar erros utilizando `try/except` e apresentar uma mensagem de erro, em vez de encerrar imediatamente.

### Decisões adicionadas pelo agente

Além do que foi solicitado, o código incorporou algumas funcionalidades e decisões por conta própria:

- Interface interativa pelo terminal.
- Opção `"sair"`.
- Conversão de vírgula para ponto em números decimais, como `25,5`.
- Mensagens adicionais, como `"Até logo!"`.
- Tratamento de `Ctrl+C` e `EOF`.
- Criação de uma função genérica `converter()`.
- Aceitação de letras minúsculas e espaços nas escalas.

---

## Passo 3

Foi criado o arquivo:

```text
conversor_temperatura.py
```

---

## Passo 4

### Exemplo 1 — Prompt: “crie um conversor de temperatura”

Nesse caso, o pedido era bastante aberto. Por isso, o agente precisou tomar praticamente todas as decisões relacionadas à especificação e ao funcionamento do sistema.

O agente decidiu:

- Utilizar **Python**.
- Criar conversões entre **Celsius, Fahrenheit e Kelvin**.
- Desenvolver uma interface interativa no terminal.
- Solicitar ao usuário o valor, a unidade de origem e a unidade de destino.
- Criar a opção `"sair"`.
- Aceitar vírgula em números decimais.
- Formatar os resultados com duas casas decimais.
- Definir as mensagens de erro.
- Criar uma função genérica `converter()`.

**Principal decisão:** como o pedido era muito aberto, o agente teve que inventar praticamente toda a especificação do sistema.

---

### Exemplo 2 — Prompt detalhado

No prompt detalhado, a IA definiu previamente diversos aspectos do sistema, incluindo:

- Linguagem de programação.
- Arquivo a ser criado.
- Funcionamento esperado.
- Validações.
- Critérios de aceite.

Mesmo com uma especificação mais detalhada, o agente ainda tomou algumas decisões de implementação por conta própria:

- Aceitar unidades em letras minúsculas.
- Aceitar vírgula como separador decimal.
- Criar as opções `--help`, `-h`, `ajuda` e `--ajuda`.
- Definir códigos de saída `0` e `1`.
- Enviar mensagens de erro para `stderr`.
- Validar o zero absoluto também em Fahrenheit e Kelvin.
- Adicionar uma tolerância de `1e-9` para comparações.
- Criar uma estrutura interna composta por várias funções de validação.
