# Apache Spark com PySpark

## Divisão

- **Básico:** arquitetura, sessão, DataFrames, schemas, leitura, transformação e escrita.
- **Intermediário:** joins, janelas, particionamento, planos, testes e funções avançadas.
- **Avançado:** execução distribuída, tuning, skew, streaming, estado, observabilidade e deploy.
- **Dados:** pipelines lakehouse, incremental, CDC, qualidade, contratos, batch/stream e operação.

Teoria: [PySpark Getting Started](https://spark.apache.org/docs/latest/api/python/getting_started/index.html), [Spark SQL/DataFrames](https://spark.apache.org/docs/latest/sql-programming-guide.html), [tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) e [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html).

## Básico — 40 exercícios

Use o [roteiro guiado de Spark básico](../docs/roteiro-nivel-basico.md#spark-básico--roteiro-dos-40-exercícios). Ele começa com DataFrames minúsculos, validação manual e funções testáveis antes de introduzir volume e otimização.

1. Instale PySpark local, crie `SparkSession` e registre versões.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
2. Explique driver, executors, job, stage, task e transformação/ação.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
3. Crie DataFrame de objetos Python com schema explícito.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
4. Compare schema inferido e explícito em dados ambíguos.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
5. Leia CSV com opções e capture registros malformados.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
6. Leia JSON multilinha e inspecione estruturas aninhadas.
   - **Exemplo-base:** Leia `[{"item":"livro","qtd":2}]` e obtenha quantidade total `2`.
7. Leia/escreva Parquet e compare schema/tamanho com CSV.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
8. Selecione e renomeie colunas sem strings SQL desnecessárias.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
9. Crie colunas com expressões e `when`.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
10. Converta tipos e identifique conversões que viram nulo.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
11. Filtre por intervalos, listas, datas e nulos.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
12. Use funções de texto para normalização.
   - **Exemplo-base:** Transforme `  ana   silva ` em `Ana Silva`.
13. Analise e formate timestamps com fuso.
   - **Exemplo-base:** Converta `2026-01-01 10:00 -03:00` para `13:00 UTC`.
14. Trate nulos com regras por coluna.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
15. Remova duplicatas por todas as colunas e por chave.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
16. Ordene globalmente e discuta seu custo.
   - **Exemplo-base:** Ordene três livros por autor e depois título usando uma tupla como chave.
17. Agregue vendas por múltiplas dimensões.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
18. Use `countDistinct`, `approx_count_distinct` e compare.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
19. Faça `groupBy` com várias métricas.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
20. Use `rollup`, `cube` e `grouping`.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
21. Faça inner/left/full/semi/anti join.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
22. Evite colunas ambíguas em joins.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
23. Valide cardinalidade antes/depois do join.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
24. Use `unionByName` com ordem diferente.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
25. Alinhe schemas evoluídos antes de unir.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
26. Trabalhe com array usando `explode`.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
27. Acesse struct aninhado e reconstrua-o.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
28. Converta map em linhas.
   - **Exemplo-base:** De `[1,2,3,4]`, produza o quadrado dos pares: `[4,16]`.
29. Registre temp view e consulte com Spark SQL.
   - **Exemplo-base:** Crie DataFrame de dois livros `(id:int,titulo:string)` e confira schema e linhas.
30. Reescreva a mesma transformação em API DataFrame e SQL.
   - **Exemplo-base:** Transforme uma resposta simulada `{"pagina":1,"itens":[1,2]}` sem acessar a rede.
31. Explique lazy evaluation observando quando o job executa.
   - **Exemplo-base:** Filtre três linhas, chame `explain()` e localize `Filter` antes da ação.
32. Inspecione plano com `explain`.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
33. Compare `show`, `collect`, `take` e riscos no driver.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
34. Grave saída particionada por data.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
35. Compare modos `append`, `overwrite`, `ignore` e `error`.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
36. Controle número de arquivos com `repartition` e `coalesce`.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
37. Use cache, materialize e libere; meça efeito.
   - **Exemplo-base:** Use um DataFrame pequeno duas vezes, materialize o cache e execute `unpersist()`.
38. Crie funções de transformação encadeáveis.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
39. Teste DataFrame esperado com pequeno dataset.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
40. Projeto: limpar e agregar vendas CSV para Parquet particionado.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.

## Intermediário — 40 exercícios

1. Numere registros por cliente com janela.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
2. Selecione último evento por chave.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
3. Calcule acumulado e média móvel.
   - **Exemplo-base:** Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`.
4. Use `lag`/`lead` para variação e intervalo.
   - **Exemplo-base:** Com vendas `[10,20,5]`, produza acumulado `[10,30,35]`.
5. Resolva gaps and islands.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
6. Faça pivot/unpivot de indicadores.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
7. Achate JSON profundamente aninhado preservando IDs.
   - **Exemplo-base:** Leia `[{"item":"livro","qtd":2}]` e obtenha quantidade total `2`.
8. Reagrupe linhas em arrays ordenados.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
9. Use funções higher-order em arrays sem `explode`.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
10. Manipule mapas com funções nativas.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
11. Compare UDF Python e função nativa em correção/desempenho.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
12. Crie pandas UDF somente para lógica não disponível nativamente.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
13. Use `mapInPandas` com schema e lotes controlados.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
14. Leia muitos arquivos pequenos e meça impacto.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
15. Explique partições de entrada e de shuffle.
   - **Exemplo-base:** Distribua seis linhas em duas partições e confira a quantidade antes de gravar.
16. Compare `repartition`, `coalesce` e repartição por chave.
   - **Exemplo-base:** Distribua seis linhas em duas partições e confira a quantidade antes de gravar.
17. Ajuste `spark.sql.shuffle.partitions` com evidência.
   - **Exemplo-base:** Crie DataFrame de dois livros `(id:int,titulo:string)` e confira schema e linhas.
18. Faça broadcast join de dimensão pequena.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
19. Observe estratégia de join no plano físico.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
20. Detecte duplicação após join e crie assertion.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
21. Trate nomes/tipos divergentes em schema drift conhecido.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
22. Implemente regra de schema evolution controlada.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
23. Use `partitionBy` sem criar partições de alta cardinalidade.
   - **Exemplo-base:** Distribua seis linhas em duas partições e confira a quantidade antes de gravar.
24. Demonstre partition pruning.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
25. Demonstre predicate e projection pushdown.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
26. Compare Parquet com CSV para consulta seletiva.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
27. Implemente agregação parcial eficiente.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
28. Use `approxQuantile` para perfil de grandes dados.
   - **Exemplo-base:** Compare somar `range(1000)` usando lista e generator antes do volume real.
29. Gere métricas de qualidade em uma única agregação.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
30. Separe válidos e quarentena sem recalcular toda a pipeline.
   - **Exemplo-base:** Separe `{id:1}` como válido e `{id:null}` com motivo `id_obrigatorio`.
31. Crie teste de schema, conteúdo e invariantes.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
32. Teste transformação com dataset vazio.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
33. Teste nulos, duplicados e timestamps extremos.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
34. Use configuração injetável sem globais ocultas.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
35. Empacote job PySpark como aplicação Python.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
36. Execute com `spark-submit` e parâmetros.
   - **Exemplo-base:** Crie DataFrame de dois livros `(id:int,titulo:string)` e confira schema e linhas.
37. Registre logs correlacionados sem `print`.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
38. Capture métricas de entrada, saída e rejeição.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
39. Gere dados sintéticos para teste de volume.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
40. Projeto: pipeline modular com joins, janelas, qualidade e testes.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.

## Avançado — 40 exercícios

1. Relacione consulta a jobs, stages e tasks na Spark UI.
   - **Exemplo-base:** Crie DataFrame de dois livros `(id:int,titulo:string)` e confira schema e linhas.
2. Identifique shuffle boundaries no DAG/plano.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
3. Leia métricas de spill, GC, shuffle e duração.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
4. Diagnostique stage lento por poucas tasks.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
5. Diagnostique skew por distribuição das tasks.
   - **Exemplo-base:** Crie dez linhas, oito com chave `A`, e conte por chave para ver o desequilíbrio.
6. Gere skew intencional em uma chave.
   - **Exemplo-base:** Crie dez linhas, oito com chave `A`, e conte por chave para ver o desequilíbrio.
7. Corrija skew com broadcast quando aplicável.
   - **Exemplo-base:** Una seis vendas a uma dimensão de dois itens e confirme broadcast no plano.
8. Corrija skew com salting e reconcilie o resultado.
   - **Exemplo-base:** Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino.
9. Avalie Adaptive Query Execution.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
10. Compare estratégias de join com/sem hints.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
11. Escolha número de partições baseado em volume e recursos.
   - **Exemplo-base:** Distribua seis linhas em duas partições e confira a quantidade antes de gravar.
12. Investigue small files e faça compactação.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
13. Compare persistência MEMORY/DISK e custo.
   - **Exemplo-base:** Use um DataFrame pequeno duas vezes, materialize o cache e execute `unpersist()`.
14. Remova cache desnecessário de uma pipeline.
   - **Exemplo-base:** Use um DataFrame pequeno duas vezes, materialize o cache e execute `unpersist()`.
15. Evite `collect`/`toPandas` que exceda o driver.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
16. Compare serialização e custo de UDF.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
17. Perfilie código executado no driver.
   - **Exemplo-base:** Compare somar `range(1000)` usando lista e generator antes do volume real.
18. Configure memória/cores em experimento controlado.
   - **Exemplo-base:** Compare somar `range(1000)` usando lista e generator antes do volume real.
19. Explique locality e data skew sem depender de memorização.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
20. Crie baseline e benchmark reprodutível.
   - **Exemplo-base:** Compare somar `range(1000)` usando lista e generator antes do volume real.
21. Leia stream de arquivos com schema explícito.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
22. Faça agregação streaming sem estado ilimitado.
   - **Exemplo-base:** Processe dois lotes mínimos de eventos com checkpoint temporário.
23. Use event time e watermark.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
24. Teste evento atrasado antes/depois do watermark.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
25. Faça deduplicação streaming com watermark.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
26. Faça stream-stream join dentro de limites temporais.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
27. Use checkpoint e reinicie sem perder progresso.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
28. Compare triggers disponíveis.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
29. Escreva em sink idempotente com `foreachBatch`.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
30. Implemente batch e streaming com a mesma transformação.
   - **Exemplo-base:** Processe dois lotes mínimos de eventos com checkpoint temporário.
31. Monitore input rate, processing rate e backlog.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
32. Simule falha e demonstre recuperação.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
33. Evite mudança incompatível de query/state após checkpoint.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
34. Crie estratégia de dead-letter/quarentena.
   - **Exemplo-base:** Separe `{id:1}` como válido e `{id:null}` com motivo `id_obrigatorio`.
35. Teste streaming com fonte controlada.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
36. Empacote dependências para cluster.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
37. Defina configurações por ambiente.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
38. Crie runbook para OOM, skew e atraso.
   - **Exemplo-base:** Crie dez linhas, oito com chave `A`, e conte por chave para ver o desequilíbrio.
39. Faça revisão de custo versus latência.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
40. Projeto: job batch + streaming otimizado, observável e recuperável.
   - **Exemplo-base:** Processe dois lotes mínimos de eventos com checkpoint temporário.

## Dados — 40 exercícios

1. Ingerir arquivos brutos adicionando metadados de origem.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
2. Preservar raw imutável e reprocessável.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
3. Criar Bronze tipada com coluna de conteúdo corrompido.
   - **Exemplo-base:** Bronze guarda `" ANA "`; Silver produz `Ana`; Gold conta um cliente.
4. Criar Silver com normalização e deduplicação.
   - **Exemplo-base:** Transforme `  ana   silva ` em `Ana Silva`.
5. Criar Gold com métricas de negócio.
   - **Exemplo-base:** Bronze guarda `" ANA "`; Silver produz `Ana`; Gold conta um cliente.
6. Definir contrato de dados e validar schema.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
7. Detectar breaking versus non-breaking schema change.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
8. Quarentenar registros com múltiplos motivos.
   - **Exemplo-base:** Separe `{id:1}` como válido e `{id:null}` com motivo `id_obrigatorio`.
9. Calcular score de qualidade por lote.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
10. Criar reconciliação Bronze/Silver/Gold.
   - **Exemplo-base:** Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino.
11. Implementar carga incremental por partição/data.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
12. Implementar watermark com período de sobreposição.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
13. Processar evento atrasado e corrigir saída.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
14. Garantir idempotência por chave e batch.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
15. Implementar upsert em formato/tabela que suporte a operação.
   - **Exemplo-base:** Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção.
16. Aplicar CDC com inserts, updates e deletes.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
17. Implementar SCD tipo 1 distribuída.
   - **Exemplo-base:** Cliente 1 muda de A para B; substitua A por B sem histórico.
18. Implementar SCD tipo 2 distribuída.
   - **Exemplo-base:** Encerre a versão A do cliente e crie B marcada como atual.
19. Tratar dimensão atrasada.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
20. Construir fato e dimensões a partir de eventos.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
21. Reparticionar sem perder balanceamento.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
22. Escolher partições físicas evitando alta cardinalidade.
   - **Exemplo-base:** Distribua seis linhas em duas partições e confira a quantidade antes de gravar.
23. Compactar small files e validar ganho.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
24. Otimizar leitura com pruning/pushdown.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
25. Processar snapshot histórico grande com backfill.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.
26. Executar backfill sem afetar lote corrente.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
27. Criar checkpoint por partição e retomada.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
28. Tornar publicação atômica para consumidores.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
29. Registrar lineage por dataset e execução.
   - **Exemplo-base:** Crie `saida_exemplo` de `entrada_exemplo` e confira a dependência no lineage.
30. Propagar `run_id` por todas as etapas.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
31. Medir freshness, completude, volume e duração.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
32. Detectar anomalia simples de volume.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
33. Definir SLA e alerta acionável.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
34. Mascarar dados pessoais antes de ambiente de desenvolvimento.
   - **Exemplo-base:** Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.
35. Testar permissões conceitualmente por camada.
   - **Exemplo-base:** Conceda apenas `SELECT` de uma tabela de laboratório a um grupo de teste.
36. Criar testes unitários, integração e reconciliação.
   - **Exemplo-base:** Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino.
37. Testar arquivo vazio, duplicado, atrasado e corrompido.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
38. Comparar custo/latência de batch e streaming.
   - **Exemplo-base:** Processe dois lotes mínimos de eventos com checkpoint temporário.
39. Documentar arquitetura, grão, contrato e operação.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
40. Projeto: medallion local com batch/stream, qualidade e observabilidade.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.

## Critério de saída

O aluno explica o plano, identifica shuffle/skew, escolhe funções nativas, testa DataFrames e entrega pipeline batch/stream idempotente e observável sem trazer dados grandes ao driver.
