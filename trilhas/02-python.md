# Python para Engenharia de Dados

## Divisão

- **Básico:** sintaxe, tipos, controle de fluxo, coleções, funções, arquivos e erros.
- **Intermediário:** módulos, orientação a objetos, iteradores, contexto, tipagem, testes, logging e APIs.
- **Avançado:** modelo de objetos, decorators, concorrência, desempenho, arquitetura e empacotamento.
- **Dados:** ingestão, qualidade, transformação, formatos, bancos, pipelines incrementais e observabilidade.

Teoria principal: [Tutorial oficial](https://docs.python.org/3/tutorial/), [biblioteca padrão](https://docs.python.org/3/library/), [ambientes e pacotes](https://packaging.python.org/en/latest/tutorials/installing-packages/) e [pytest](https://docs.pytest.org/en/stable/getting-started.html).

## Básico — 40 exercícios

Use o [roteiro guiado de Python básico](../docs/roteiro-nivel-basico.md#python-básico--roteiro-dos-40-exercícios). Para cada exercício, ele orienta a pasta, exemplos, implementação incremental, testes, tratamento de erros e entrega no GitHub.

1. Exiba uma ficha de aluno usando variáveis, `print` e f-strings.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
2. Converta temperatura entre Celsius, Fahrenheit e Kelvin, validando limites físicos.
   - **Exemplo-base:** Converta apenas `0 °C` para Fahrenheit; usando `c * 9/5 + 32`, espere `32`.
3. Calcule salário líquido com faixas fictícias de imposto.
   - **Exemplo-base:** Aplique um único desconto de 10% sobre `1000`; espere `900` antes de criar faixas.
4. Classifique um número como positivo/negativo, par/ímpar e primo/não primo.
   - **Exemplo-base:** Receba `8` e informe somente se é par; depois teste `7` e `0`.
5. Converta segundos em dias, horas, minutos e segundos.
   - **Exemplo-base:** Converta `125` segundos em `2 minutos e 5 segundos` usando divisão e resto.
6. Crie uma calculadora com menu, `match` ou condicionais e divisão segura.
   - **Exemplo-base:** Implemente primeiro `somar(2, 3) → 5`; depois acrescente outra operação.
7. Gere uma tabuada escolhida pelo usuário com `for`.
   - **Exemplo-base:** Gere apenas `3×1`, `3×2`, `3×3`, esperando `3, 6, 9`.
8. Some números até receber um sentinela usando `while`.
   - **Exemplo-base:** Leia `4`, `6`, `0`, usando zero para parar; a soma deve ser `10`.
9. Imprima FizzBuzz parametrizável para dois divisores.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
10. Valide senha por comprimento, maiúscula, minúscula, dígito e símbolo.
   - **Exemplo-base:** Teste só o mínimo de oito caracteres: `abc` falha e `abcdefgh` passa.
11. Conte vogais, consoantes, dígitos e espaços em uma frase.
   - **Exemplo-base:** Conte as vogais de `Data`; o resultado é `2`, ignorando maiúsculas.
12. Normalize um nome removendo espaços duplicados e capitalização inconsistente.
   - **Exemplo-base:** Transforme `  ana   silva ` em `Ana Silva`.
13. Detecte palíndromos ignorando pontuação e caixa.
   - **Exemplo-base:** Remova espaços de `Ame a ema`, use minúsculas e compare com o texto invertido.
14. Gere estatísticas de uma lista sem usar bibliotecas externas.
   - **Exemplo-base:** Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`.
15. Remova duplicados preservando a ordem original.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
16. Encontre o segundo maior valor distinto e trate casos insuficientes.
   - **Exemplo-base:** Em `[5,2,5,3]`, o segundo maior valor distinto é `3`.
17. Rotacione uma lista `n` posições à direita e à esquerda.
   - **Exemplo-base:** Rotacione `[1,2,3]` uma posição à direita para obter `[3,1,2]`.
18. Calcule a interseção, união e diferença de duas listas com conjuntos.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
19. Conte frequência de palavras e mostre as cinco mais comuns.
   - **Exemplo-base:** Em `azul azul verde`, produza `{"azul":2,"verde":1}`.
20. Agrupe nomes pela primeira letra em um dicionário.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
21. Modele um pequeno estoque como lista de dicionários e calcule seu valor.
   - **Exemplo-base:** Use lápis: 3×R$2 e caderno: 2×R$10; o total esperado é R$26.
22. Atualize quantidades do estoque sem aceitar resultado negativo.
   - **Exemplo-base:** Use lápis: 3×R$2 e caderno: 2×R$10; o total esperado é R$26.
23. Implemente busca de produto por termo parcial.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
24. Ordene registros por dois campos e explique `key`.
   - **Exemplo-base:** Ordene três livros por autor e depois título usando uma tupla como chave.
25. Escreva funções de média, mediana e moda com docstrings.
   - **Exemplo-base:** Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`.
26. Crie uma função com argumentos posicionais, nomeados e valores padrão.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
27. Use `*args` para somar valores e `**kwargs` para montar uma configuração.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
28. Escreva uma função recursiva para percorrer uma estrutura aninhada simples.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
29. Use comprehensions para filtrar e transformar uma coleção de vendas.
   - **Exemplo-base:** De `[1,2,3,4]`, produza o quadrado dos pares: `[4,16]`.
30. Refaça o exercício anterior sem comprehension e compare legibilidade.
   - **Exemplo-base:** De `[1,2,3,4]`, produza o quadrado dos pares: `[4,16]`.
31. Leia um TXT, conte linhas/palavras/caracteres e trate arquivo inexistente.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
32. Grave e recupere uma agenda em CSV usando a biblioteca `csv`.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
33. Leia um JSON de pedidos e calcule total por cliente.
   - **Exemplo-base:** Leia `[{"item":"livro","qtd":2}]` e obtenha quantidade total `2`.
34. Crie uma cópia normalizada do JSON sem alterar a entrada.
   - **Exemplo-base:** Transforme `  ana   silva ` em `Ana Silva`.
35. Trate entradas inválidas com exceções específicas, sem `except` genérico.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
36. Crie uma exceção `SaldoInsuficienteError` em uma simulação bancária.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
37. Use `pathlib` para listar arquivos por extensão e tamanho.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
38. Use `datetime` para calcular atrasos e agrupar eventos por dia.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
39. Faça um programa CLI simples com `argparse`.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
40. Integre arquivos, funções e validações em um relatório diário de vendas.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.

## Intermediário — 40 exercícios

1. Separe o relatório de vendas em módulos de leitura, regras e saída.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
2. Crie um pacote instalável localmente com `pyproject.toml`.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
3. Modele `Cliente`, `Produto` e `Pedido` com classes.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
4. Refaça os modelos com `dataclass`, validação em `__post_init__` e tipos.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
5. Use composição para representar pedido e itens, evitando herança desnecessária.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
6. Crie uma classe abstrata `Leitor` e implementações CSV e JSON.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
7. Implemente propriedades para impedir estados inválidos.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
8. Defina `__repr__`, `__eq__` e ordenação para um registro de evento.
   - **Exemplo-base:** Ordene três livros por autor e depois título usando uma tupla como chave.
9. Implemente um iterador que leia um arquivo grande linha a linha.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
10. Escreva um generator que produza lotes de tamanho configurável.
   - **Exemplo-base:** Produza 1, 2 e 3 com `yield` e consuma um valor por vez.
11. Monte uma pipeline preguiçosa com generators para filtrar e transformar logs.
   - **Exemplo-base:** Produza 1, 2 e 3 com `yield` e consuma um valor por vez.
12. Crie um context manager que meça e registre o tempo de uma etapa.
   - **Exemplo-base:** Use `with cronometro():` em um bloco curto e registre início e fim.
13. Crie um context manager para uma transação fictícia com commit/rollback.
   - **Exemplo-base:** Use `with cronometro():` em um bloco curto e registre início e fim.
14. Use `map`, `filter`, `zip` e `enumerate`; compare com comprehensions.
   - **Exemplo-base:** De `[1,2,3,4]`, produza o quadrado dos pares: `[4,16]`.
15. Agrupe registros com `defaultdict` e conte com `Counter`.
   - **Exemplo-base:** Em `azul azul verde`, produza `{"azul":2,"verde":1}`.
16. Use `deque` para uma janela móvel de eventos.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
17. Crie funções puras para regras de transformação e teste invariantes.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
18. Adicione type hints completos e execute verificação estática.
   - **Exemplo-base:** Anote `def dobro(valor: int) -> int` e verifique inteiro e texto.
19. Modele configurações com `TypedDict`, `Literal` ou `Protocol`.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
20. Valide dados de entrada com uma biblioteca apropriada e reporte todos os erros.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
21. Escreva testes unitários para casos normal, limite e erro.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
22. Use fixtures e parametrização para testar dez combinações.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
23. Faça mock de relógio e de uma API externa.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
24. Meça cobertura e acrescente testes úteis, sem perseguir 100% artificial.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
25. Configure logging estruturado com nível e identificador de execução.
   - **Exemplo-base:** Registre `etapa=inicio run_id=abc` e `etapa=fim linhas=3` sem `print`.
26. Leia configurações de ambiente sem versionar segredos.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
27. Consuma uma API paginada com timeout e tratamento de status.
   - **Exemplo-base:** Transforme uma resposta simulada `{"pagina":1,"itens":[1,2]}` sem acessar a rede.
28. Implemente retry com backoff apenas para falhas transitórias.
   - **Exemplo-base:** Simule uma função que falha uma vez e funciona na segunda; valide duas tentativas.
29. Faça download em streaming, calcule hash e valide integridade.
   - **Exemplo-base:** Transforme uma resposta simulada `{"pagina":1,"itens":[1,2]}` sem acessar a rede.
30. Crie cache local com prazo de validade para respostas HTTP.
   - **Exemplo-base:** Transforme uma resposta simulada `{"pagina":1,"itens":[1,2]}` sem acessar a rede.
31. Consulte SQLite com parâmetros, nunca concatenando entrada em SQL.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
32. Implemente transação com rollback quando um registro falhar.
   - **Exemplo-base:** Debite 10 de uma conta em transação; valide e execute rollback na primeira vez.
33. Compare serialização CSV, JSON e Parquet em tamanho e tipos.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
34. Use regex para extrair campos de logs e catalogue linhas rejeitadas.
   - **Exemplo-base:** Extraia `INFO` e `42` de `INFO pedido=42`.
35. Normalize datas com fusos horários diferentes para UTC.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
36. Crie uma CLI com subcomandos `ingest`, `transform` e `report`.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
37. Use `subprocess` com segurança para executar uma ferramenta e capturar resultado.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
38. Crie uma tarefa agendada idempotente por arquivo de controle.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
39. Documente a API pública do pacote e gere exemplos executáveis.
   - **Exemplo-base:** Transforme uma resposta simulada `{"pagina":1,"itens":[1,2]}` sem acessar a rede.
40. Entregue um mini-ETL modular com testes, logs, configuração e CLI.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.

## Avançado — 40 exercícios

1. Escreva um decorator que registre duração, sucesso e falha.
   - **Exemplo-base:** Aplique `@registrar` a `dobro(3)` e preserve nome, entrada e saída.
2. Crie um decorator parametrizável de retry e teste seu comportamento.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
3. Preserve metadados com `functools.wraps` e prove por teste.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
4. Implemente um descriptor que valide campos numéricos.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
5. Investigue resolução de métodos e uso correto de `super`.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
6. Crie classes imutáveis e avalie custo/benefício.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
7. Use `Protocol` para desacoplar pipeline de armazenamento.
   - **Exemplo-base:** Anote `def dobro(valor: int) -> int` e verifique inteiro e texto.
8. Escreva uma função genérica tipada para particionar sequências.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
9. Crie um plugin carregado dinamicamente por configuração.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
10. Implemente injeção de dependência simples para leitores e escritores.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
11. Compare cópia rasa, profunda e estruturas imutáveis em um bug reproduzível.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
12. Encontre e corrija um argumento padrão mutável.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
13. Inspecione referências e coleta de lixo em um pequeno experimento.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
14. Meça memória de lista versus generator.
   - **Exemplo-base:** Produza 1, 2 e 3 com `yield` e consuma um valor por vez.
15. Perfilie uma transformação e otimize o gargalo comprovado.
   - **Exemplo-base:** Compare somar `range(1000)` usando lista e generator antes do volume real.
16. Compare algoritmo quadrático e linear com volumes crescentes.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
17. Use `lru_cache` em cálculo repetido e meça o ganho.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
18. Processe tarefas I/O-bound com `ThreadPoolExecutor`.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
19. Processe tarefas CPU-bound com `ProcessPoolExecutor`.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
20. Refaça um consumidor de APIs com `asyncio` e limite de concorrência.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
21. Implemente cancelamento e timeout em tarefas assíncronas.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
22. Evite race condition protegendo estado compartilhado.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
23. Construa produtor/consumidor com fila e finalização limpa.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
24. Manipule sinais para encerrar um pipeline sem corromper saída.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
25. Implemente escrita atômica usando arquivo temporário e rename.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
26. Crie checkpoint para retomar processamento interrompido.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
27. Garanta idempotência por chave de negócio e hash do conteúdo.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
28. Implemente padrão Strategy para formatos de entrada.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
29. Implemente Adapter para duas APIs incompatíveis.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
30. Refatore um “God object” em camadas com responsabilidades claras.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
31. Crie testes baseados em propriedades para uma transformação.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
32. Use mutation testing ou injete defeitos para avaliar a suíte.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
33. Faça teste de integração com banco efêmero.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
34. Configure lint, format, tipos e testes em hooks locais.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
35. Crie build do pacote e instale-o em ambiente limpo.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
36. Use versionamento semântico e gere changelog de uma versão.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
37. Analise dependências vulneráveis e fixe versões com critério.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
38. Crie benchmark reprodutível de duas implementações.
   - **Exemplo-base:** Compare somar `range(1000)` usando lista e generator antes do volume real.
39. Adicione métricas de contagem, duração e rejeição a um pipeline.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
40. Entregue uma aplicação de dados concorrente, retomável e empacotada.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.

## Dados — 40 exercícios

1. Faça profiling de CSV: esquema, nulos, cardinalidade e estatísticas.
   - **Exemplo-base:** Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`.
2. Detecte delimitador, encoding e cabeçalho com validação posterior.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
3. Converta tipos explicitamente e envie registros inválidos à quarentena.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
4. Normalize nomes, e-mails, telefones e datas sem destruir o valor bruto.
   - **Exemplo-base:** Transforme `  ana   silva ` em `Ana Silva`.
5. Deduplicate clientes por chave e regra determinística de sobrevivência.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
6. Valide chaves, domínios, intervalos e integridade referencial.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
7. Gere relatório de qualidade com métricas e exemplos de falha.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
8. Compare processamento inteiro versus chunks em arquivo grande.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
9. Una vários CSVs com esquemas ligeiramente diferentes.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
10. Achate JSON aninhado preservando relacionamentos e arrays.
   - **Exemplo-base:** Leia `[{"item":"livro","qtd":2}]` e obtenha quantidade total `2`.
11. Consulte uma API paginada e grave respostas brutas auditáveis.
   - **Exemplo-base:** Transforme uma resposta simulada `{"pagina":1,"itens":[1,2]}` sem acessar a rede.
12. Faça ingestão incremental usando watermark de atualização.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
13. Faça ingestão incremental por hash quando não há timestamp confiável.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
14. Garanta reexecução sem duplicar registros.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
15. Particione uma saída por data e explique o tamanho de arquivo escolhido.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
16. Converta CSV em Parquet e compare tipos, compressão e leitura seletiva.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
17. Leia apenas colunas necessárias e meça a diferença.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
18. Use pandas para filtrar, selecionar, renomear e tipar um dataset.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
19. Faça `groupby` de vendas por período, loja e categoria.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
20. Faça joins 1:1, 1:N e N:N e valide a cardinalidade antes/depois.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
21. Trate nulos com regras diferentes por coluna, sem preenchimento indiscriminado.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
22. Detecte outliers e separe detecção de decisão de negócio.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
23. Calcule janela móvel, acumulado e comparação com período anterior.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
24. Modele dimensões e fatos a partir de dados transacionais.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
25. Gere uma dimensão calendário.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
26. Implemente SCD tipo 1 em memória/arquivos.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
27. Implemente SCD tipo 2 com início, fim e indicador atual.
   - **Exemplo-base:** Encerre a versão A do cliente e crie B marcada como atual.
28. Carregue dados em SQL Server em lotes e transação.
   - **Exemplo-base:** Debite 10 de uma conta em transação; valide e execute rollback na primeira vez.
29. Extraia SQL Server com consulta parametrizada e leitura em chunks.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
30. Faça upsert seguro com tabela de estágio e valide contagens.
   - **Exemplo-base:** Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção.
31. Crie reconciliação entre origem e destino por contagem, soma e hash.
   - **Exemplo-base:** Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino.
32. Implemente contrato de dados versionado para um dataset.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
33. Detecte mudança inesperada de esquema e interrompa com mensagem útil.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
34. Masque dados pessoais em uma cópia para desenvolvimento.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
35. Crie lineage simples registrando origem, etapa, destino e execução.
   - **Exemplo-base:** Crie `saida_exemplo` de `entrada_exemplo` e confira a dependência no lineage.
36. Publique métricas e logs correlacionados por `run_id`.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
37. Crie alertas locais para atraso, volume anormal e falha de qualidade.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
38. Teste o pipeline com dados vazios, duplicados, atrasados e malformados.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
39. Crie DAG conceitual e identifique dependências, SLA e pontos de recuperação.
   - **Exemplo-base:** Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.
40. Projeto: pipeline batch `raw → clean → analytics`, incremental, testado e documentado.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.

## Critério de saída

O aluno recebe arquivos e uma API desconhecida, constrói uma pipeline modular e idempotente, valida qualidade, grava em banco/Parquet, cria testes e explica escolhas de esquema, particionamento, erros e reexecução.
