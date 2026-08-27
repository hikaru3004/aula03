Exercicio 1
Passo 1
Criou o arquivo converte.py

Passo 2. 
Linguagem: Python.
Unidades: Celsius (°C), Fahrenheit (°F) e Kelvin (K).
Formato de saída: mostra o valor com duas casas decimais, por exemplo: 25.00°C = 77.00°F.
Entrada inválida: o programa captura o erro com try/except e mostra uma mensagem de erro, em vez de encerrar imediatamente.
O que não estava no pedido: o código adicionou várias decisões por conta própria, como:
interface interativa pelo terminal;
opção "sair";
conversão de vírgula para ponto (25,5);
mensagens como "Até logo!";
tratamento de Ctrl+C e EOF;
função genérica converter();
aceitação de letras minúsculas e espaços nas escalas.

Passo 3
Criou o arquivo conversor_temperatura.py

Passo 4  
Exemplo 1 — “crie um conversor de temperatura”

O agente decidiu sozinho como o conversor funcionaria, pois o pedido era muito aberto. Ele escolheu:

usar Python;
criar conversões entre C, F e K;
fazer uma interface interativa no terminal;
pedir valor, origem e destino ao usuário;
criar a opção "sair";
aceitar vírgula em números decimais;
formatar o resultado com duas casas decimais;
definir as mensagens de erro;
criar uma função genérica converter().

Principal decisão: o agente teve que inventar praticamente toda a especificação do sistema.

Exemplo 2 — Prompt detalhado

Aqui você já definiu linguagem, arquivo, funcionamento, validações e critérios de aceite. Mesmo assim, o agente decidiu sozinho alguns detalhes, como:

aceitar unidades em letras minúsculas;
aceitar vírgula como separador decimal;
criar --help, -h, ajuda e --ajuda;
definir códigos de saída 0 e 1;
enviar erros para stderr;
validar o zero absoluto também em Fahrenheit e Kelvin;
adicionar tolerância 1e-9 para comparação;
criar uma estrutura interna com várias funções de validação.
