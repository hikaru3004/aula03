# Especificação: Sistema de Acompanhamento de Notas

## 1. Decisões de Arquitetura
* **Plataforma:** Interface de Linha de Comando (CLI).
* **Persistência:** Arquivos JSON locais em `data/`.
* **Arredondamento:** 2 casas decimais (padrão half-up).
* **Avaliações Pendentes:** Excluídas do cálculo da média e da soma de pesos. Sem notas exibe status `Pendente`.

## 2. Requisitos Funcionais
* **RF01 - Cadastros:** Gestão de Turmas (com limites de aprovação/exame e pesos), Alunos e Avaliações.
* **RF02 - Lançamento de Notas:** Registro e edição de notas de 0.0 a 10.0.
* **RF03 - Cálculo de Média:** Média ponderada apenas sobre avaliações lançadas e classificação (*Aprovado*, *Exame*, *Reprovado*).
* **RF04 - Estatísticas:** Média da turma, mediana, distribuição percentual e alerta para alunos a < 0,50 ponto da aprovação.
* **RF05 - Persistência:** Carregamento e salvamento automático dos dados.
* **RF06 - Validação:** Rejeição de entradas inválidas com mensagens descritivas.

## 3. Critérios de Aceite Verificáveis
1. Entrada inválida: Nota -1 ou 11 exibe erro e rejeita a operação.
2. Cálculo com pesos: Em turma com P1 (peso 2) e P2 (peso 3), notas 8.0 e 6.0 geram média 6.80.
3. Média parcial: Se apenas P1 (nota 8.0, peso 2) for lançada e P2 estiver pendente, a média é 8.00.
4. Alerta de risco: Para limite 7.0, aluno com média 6.60 entra na "Zona de Risco"; aluno com 6.40 não entra.
5. Persistência: Reiniciar o sistema mantém todos os registros salvos.
