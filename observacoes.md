# Observações — Aula 03
Atividade 1, 2 e 3
Modelo usado: Muse Spark 1.2 Free

Atividade 4, 5, 6, 7
Modelo usado: NVIDIA Nemotron modelo free e ox alpha free

Ex4 (Delimitadores): Sem delimitador, ele classificou o texto e comentou a tentativa por ter identificado a injeção de prompt; com delimitador, ele limitou-se a interpretar o conteúdo dentro das tags e o classificou como misto.  

Ex5 (Critério de Aceite): Sem critério de aceite, ele apenas gerou a função e parou para pedir permissão para salvar o arquivo; com o aceite verificável, ele criou o arquivo diretamente e executou o código funcional completo.  

Ex6 (Pensar antes de agir): No modo Plan, ele levantou as seguintes dúvidas antes de implementar:  
Escopo: Qual a abrangência exata da mudança proposta em converte.py?  
Validação de entradas: Devem-se rejeitar explicitamente valores como 'nan', 'inf' e '-inf' como temperaturas válidas?  
Cobertura de testes: Deve-se incluir a cobertura dos casos de sucesso (caminho feliz), além das validações de erro?  

Ex7 (Auto-correção): Na verificação autônoma contra o critério de aceite, ele identificou os seguintes pontos pendentes:  Divergência de escopo:  Ausência de estrutura Pytest: Os testes haviam sido implementados apenas como validações assert em bloco __main__, sem a criação do arquivo dedicado test_media_ponderada.py.  
Casos-limite não tratados: Entradas inválidas, como pesos com soma negativa (ex: [2, -1]), eram aceitas sem erro, e valores NaN nas notas propagavam silenciosamente.  