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
2. Converta temperatura entre Celsius, Fahrenheit e Kelvin, validando limites físicos.
3. Calcule salário líquido com faixas fictícias de imposto.
4. Classifique um número como positivo/negativo, par/ímpar e primo/não primo.
5. Converta segundos em dias, horas, minutos e segundos.
6. Crie uma calculadora com menu, `match` ou condicionais e divisão segura.
7. Gere uma tabuada escolhida pelo usuário com `for`.
8. Some números até receber um sentinela usando `while`.
9. Imprima FizzBuzz parametrizável para dois divisores.
10. Valide senha por comprimento, maiúscula, minúscula, dígito e símbolo.
11. Conte vogais, consoantes, dígitos e espaços em uma frase.
12. Normalize um nome removendo espaços duplicados e capitalização inconsistente.
13. Detecte palíndromos ignorando pontuação e caixa.
14. Gere estatísticas de uma lista sem usar bibliotecas externas.
15. Remova duplicados preservando a ordem original.
16. Encontre o segundo maior valor distinto e trate casos insuficientes.
17. Rotacione uma lista `n` posições à direita e à esquerda.
18. Calcule a interseção, união e diferença de duas listas com conjuntos.
19. Conte frequência de palavras e mostre as cinco mais comuns.
20. Agrupe nomes pela primeira letra em um dicionário.
21. Modele um pequeno estoque como lista de dicionários e calcule seu valor.
22. Atualize quantidades do estoque sem aceitar resultado negativo.
23. Implemente busca de produto por termo parcial.
24. Ordene registros por dois campos e explique `key`.
25. Escreva funções de média, mediana e moda com docstrings.
26. Crie uma função com argumentos posicionais, nomeados e valores padrão.
27. Use `*args` para somar valores e `**kwargs` para montar uma configuração.
28. Escreva uma função recursiva para percorrer uma estrutura aninhada simples.
29. Use comprehensions para filtrar e transformar uma coleção de vendas.
30. Refaça o exercício anterior sem comprehension e compare legibilidade.
31. Leia um TXT, conte linhas/palavras/caracteres e trate arquivo inexistente.
32. Grave e recupere uma agenda em CSV usando a biblioteca `csv`.
33. Leia um JSON de pedidos e calcule total por cliente.
34. Crie uma cópia normalizada do JSON sem alterar a entrada.
35. Trate entradas inválidas com exceções específicas, sem `except` genérico.
36. Crie uma exceção `SaldoInsuficienteError` em uma simulação bancária.
37. Use `pathlib` para listar arquivos por extensão e tamanho.
38. Use `datetime` para calcular atrasos e agrupar eventos por dia.
39. Faça um programa CLI simples com `argparse`.
40. Integre arquivos, funções e validações em um relatório diário de vendas.

## Intermediário — 40 exercícios

1. Separe o relatório de vendas em módulos de leitura, regras e saída.
2. Crie um pacote instalável localmente com `pyproject.toml`.
3. Modele `Cliente`, `Produto` e `Pedido` com classes.
4. Refaça os modelos com `dataclass`, validação em `__post_init__` e tipos.
5. Use composição para representar pedido e itens, evitando herança desnecessária.
6. Crie uma classe abstrata `Leitor` e implementações CSV e JSON.
7. Implemente propriedades para impedir estados inválidos.
8. Defina `__repr__`, `__eq__` e ordenação para um registro de evento.
9. Implemente um iterador que leia um arquivo grande linha a linha.
10. Escreva um generator que produza lotes de tamanho configurável.
11. Monte uma pipeline preguiçosa com generators para filtrar e transformar logs.
12. Crie um context manager que meça e registre o tempo de uma etapa.
13. Crie um context manager para uma transação fictícia com commit/rollback.
14. Use `map`, `filter`, `zip` e `enumerate`; compare com comprehensions.
15. Agrupe registros com `defaultdict` e conte com `Counter`.
16. Use `deque` para uma janela móvel de eventos.
17. Crie funções puras para regras de transformação e teste invariantes.
18. Adicione type hints completos e execute verificação estática.
19. Modele configurações com `TypedDict`, `Literal` ou `Protocol`.
20. Valide dados de entrada com uma biblioteca apropriada e reporte todos os erros.
21. Escreva testes unitários para casos normal, limite e erro.
22. Use fixtures e parametrização para testar dez combinações.
23. Faça mock de relógio e de uma API externa.
24. Meça cobertura e acrescente testes úteis, sem perseguir 100% artificial.
25. Configure logging estruturado com nível e identificador de execução.
26. Leia configurações de ambiente sem versionar segredos.
27. Consuma uma API paginada com timeout e tratamento de status.
28. Implemente retry com backoff apenas para falhas transitórias.
29. Faça download em streaming, calcule hash e valide integridade.
30. Crie cache local com prazo de validade para respostas HTTP.
31. Consulte SQLite com parâmetros, nunca concatenando entrada em SQL.
32. Implemente transação com rollback quando um registro falhar.
33. Compare serialização CSV, JSON e Parquet em tamanho e tipos.
34. Use regex para extrair campos de logs e catalogue linhas rejeitadas.
35. Normalize datas com fusos horários diferentes para UTC.
36. Crie uma CLI com subcomandos `ingest`, `transform` e `report`.
37. Use `subprocess` com segurança para executar uma ferramenta e capturar resultado.
38. Crie uma tarefa agendada idempotente por arquivo de controle.
39. Documente a API pública do pacote e gere exemplos executáveis.
40. Entregue um mini-ETL modular com testes, logs, configuração e CLI.

## Avançado — 40 exercícios

1. Escreva um decorator que registre duração, sucesso e falha.
2. Crie um decorator parametrizável de retry e teste seu comportamento.
3. Preserve metadados com `functools.wraps` e prove por teste.
4. Implemente um descriptor que valide campos numéricos.
5. Investigue resolução de métodos e uso correto de `super`.
6. Crie classes imutáveis e avalie custo/benefício.
7. Use `Protocol` para desacoplar pipeline de armazenamento.
8. Escreva uma função genérica tipada para particionar sequências.
9. Crie um plugin carregado dinamicamente por configuração.
10. Implemente injeção de dependência simples para leitores e escritores.
11. Compare cópia rasa, profunda e estruturas imutáveis em um bug reproduzível.
12. Encontre e corrija um argumento padrão mutável.
13. Inspecione referências e coleta de lixo em um pequeno experimento.
14. Meça memória de lista versus generator.
15. Perfilie uma transformação e otimize o gargalo comprovado.
16. Compare algoritmo quadrático e linear com volumes crescentes.
17. Use `lru_cache` em cálculo repetido e meça o ganho.
18. Processe tarefas I/O-bound com `ThreadPoolExecutor`.
19. Processe tarefas CPU-bound com `ProcessPoolExecutor`.
20. Refaça um consumidor de APIs com `asyncio` e limite de concorrência.
21. Implemente cancelamento e timeout em tarefas assíncronas.
22. Evite race condition protegendo estado compartilhado.
23. Construa produtor/consumidor com fila e finalização limpa.
24. Manipule sinais para encerrar um pipeline sem corromper saída.
25. Implemente escrita atômica usando arquivo temporário e rename.
26. Crie checkpoint para retomar processamento interrompido.
27. Garanta idempotência por chave de negócio e hash do conteúdo.
28. Implemente padrão Strategy para formatos de entrada.
29. Implemente Adapter para duas APIs incompatíveis.
30. Refatore um “God object” em camadas com responsabilidades claras.
31. Crie testes baseados em propriedades para uma transformação.
32. Use mutation testing ou injete defeitos para avaliar a suíte.
33. Faça teste de integração com banco efêmero.
34. Configure lint, format, tipos e testes em hooks locais.
35. Crie build do pacote e instale-o em ambiente limpo.
36. Use versionamento semântico e gere changelog de uma versão.
37. Analise dependências vulneráveis e fixe versões com critério.
38. Crie benchmark reprodutível de duas implementações.
39. Adicione métricas de contagem, duração e rejeição a um pipeline.
40. Entregue uma aplicação de dados concorrente, retomável e empacotada.

## Dados — 40 exercícios

1. Faça profiling de CSV: esquema, nulos, cardinalidade e estatísticas.
2. Detecte delimitador, encoding e cabeçalho com validação posterior.
3. Converta tipos explicitamente e envie registros inválidos à quarentena.
4. Normalize nomes, e-mails, telefones e datas sem destruir o valor bruto.
5. Deduplicate clientes por chave e regra determinística de sobrevivência.
6. Valide chaves, domínios, intervalos e integridade referencial.
7. Gere relatório de qualidade com métricas e exemplos de falha.
8. Compare processamento inteiro versus chunks em arquivo grande.
9. Una vários CSVs com esquemas ligeiramente diferentes.
10. Achate JSON aninhado preservando relacionamentos e arrays.
11. Consulte uma API paginada e grave respostas brutas auditáveis.
12. Faça ingestão incremental usando watermark de atualização.
13. Faça ingestão incremental por hash quando não há timestamp confiável.
14. Garanta reexecução sem duplicar registros.
15. Particione uma saída por data e explique o tamanho de arquivo escolhido.
16. Converta CSV em Parquet e compare tipos, compressão e leitura seletiva.
17. Leia apenas colunas necessárias e meça a diferença.
18. Use pandas para filtrar, selecionar, renomear e tipar um dataset.
19. Faça `groupby` de vendas por período, loja e categoria.
20. Faça joins 1:1, 1:N e N:N e valide a cardinalidade antes/depois.
21. Trate nulos com regras diferentes por coluna, sem preenchimento indiscriminado.
22. Detecte outliers e separe detecção de decisão de negócio.
23. Calcule janela móvel, acumulado e comparação com período anterior.
24. Modele dimensões e fatos a partir de dados transacionais.
25. Gere uma dimensão calendário.
26. Implemente SCD tipo 1 em memória/arquivos.
27. Implemente SCD tipo 2 com início, fim e indicador atual.
28. Carregue dados em SQL Server em lotes e transação.
29. Extraia SQL Server com consulta parametrizada e leitura em chunks.
30. Faça upsert seguro com tabela de estágio e valide contagens.
31. Crie reconciliação entre origem e destino por contagem, soma e hash.
32. Implemente contrato de dados versionado para um dataset.
33. Detecte mudança inesperada de esquema e interrompa com mensagem útil.
34. Masque dados pessoais em uma cópia para desenvolvimento.
35. Crie lineage simples registrando origem, etapa, destino e execução.
36. Publique métricas e logs correlacionados por `run_id`.
37. Crie alertas locais para atraso, volume anormal e falha de qualidade.
38. Teste o pipeline com dados vazios, duplicados, atrasados e malformados.
39. Crie DAG conceitual e identifique dependências, SLA e pontos de recuperação.
40. Projeto: pipeline batch `raw → clean → analytics`, incremental, testado e documentado.

## Critério de saída

O aluno recebe arquivos e uma API desconhecida, constrói uma pipeline modular e idempotente, valida qualidade, grava em banco/Parquet, cria testes e explica escolhas de esquema, particionamento, erros e reexecução.
