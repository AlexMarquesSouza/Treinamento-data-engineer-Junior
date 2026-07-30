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
2. Explique driver, executors, job, stage, task e transformação/ação.
3. Crie DataFrame de objetos Python com schema explícito.
4. Compare schema inferido e explícito em dados ambíguos.
5. Leia CSV com opções e capture registros malformados.
6. Leia JSON multilinha e inspecione estruturas aninhadas.
7. Leia/escreva Parquet e compare schema/tamanho com CSV.
8. Selecione e renomeie colunas sem strings SQL desnecessárias.
9. Crie colunas com expressões e `when`.
10. Converta tipos e identifique conversões que viram nulo.
11. Filtre por intervalos, listas, datas e nulos.
12. Use funções de texto para normalização.
13. Analise e formate timestamps com fuso.
14. Trate nulos com regras por coluna.
15. Remova duplicatas por todas as colunas e por chave.
16. Ordene globalmente e discuta seu custo.
17. Agregue vendas por múltiplas dimensões.
18. Use `countDistinct`, `approx_count_distinct` e compare.
19. Faça `groupBy` com várias métricas.
20. Use `rollup`, `cube` e `grouping`.
21. Faça inner/left/full/semi/anti join.
22. Evite colunas ambíguas em joins.
23. Valide cardinalidade antes/depois do join.
24. Use `unionByName` com ordem diferente.
25. Alinhe schemas evoluídos antes de unir.
26. Trabalhe com array usando `explode`.
27. Acesse struct aninhado e reconstrua-o.
28. Converta map em linhas.
29. Registre temp view e consulte com Spark SQL.
30. Reescreva a mesma transformação em API DataFrame e SQL.
31. Explique lazy evaluation observando quando o job executa.
32. Inspecione plano com `explain`.
33. Compare `show`, `collect`, `take` e riscos no driver.
34. Grave saída particionada por data.
35. Compare modos `append`, `overwrite`, `ignore` e `error`.
36. Controle número de arquivos com `repartition` e `coalesce`.
37. Use cache, materialize e libere; meça efeito.
38. Crie funções de transformação encadeáveis.
39. Teste DataFrame esperado com pequeno dataset.
40. Projeto: limpar e agregar vendas CSV para Parquet particionado.

## Intermediário — 40 exercícios

1. Numere registros por cliente com janela.
2. Selecione último evento por chave.
3. Calcule acumulado e média móvel.
4. Use `lag`/`lead` para variação e intervalo.
5. Resolva gaps and islands.
6. Faça pivot/unpivot de indicadores.
7. Achate JSON profundamente aninhado preservando IDs.
8. Reagrupe linhas em arrays ordenados.
9. Use funções higher-order em arrays sem `explode`.
10. Manipule mapas com funções nativas.
11. Compare UDF Python e função nativa em correção/desempenho.
12. Crie pandas UDF somente para lógica não disponível nativamente.
13. Use `mapInPandas` com schema e lotes controlados.
14. Leia muitos arquivos pequenos e meça impacto.
15. Explique partições de entrada e de shuffle.
16. Compare `repartition`, `coalesce` e repartição por chave.
17. Ajuste `spark.sql.shuffle.partitions` com evidência.
18. Faça broadcast join de dimensão pequena.
19. Observe estratégia de join no plano físico.
20. Detecte duplicação após join e crie assertion.
21. Trate nomes/tipos divergentes em schema drift conhecido.
22. Implemente regra de schema evolution controlada.
23. Use `partitionBy` sem criar partições de alta cardinalidade.
24. Demonstre partition pruning.
25. Demonstre predicate e projection pushdown.
26. Compare Parquet com CSV para consulta seletiva.
27. Implemente agregação parcial eficiente.
28. Use `approxQuantile` para perfil de grandes dados.
29. Gere métricas de qualidade em uma única agregação.
30. Separe válidos e quarentena sem recalcular toda a pipeline.
31. Crie teste de schema, conteúdo e invariantes.
32. Teste transformação com dataset vazio.
33. Teste nulos, duplicados e timestamps extremos.
34. Use configuração injetável sem globais ocultas.
35. Empacote job PySpark como aplicação Python.
36. Execute com `spark-submit` e parâmetros.
37. Registre logs correlacionados sem `print`.
38. Capture métricas de entrada, saída e rejeição.
39. Gere dados sintéticos para teste de volume.
40. Projeto: pipeline modular com joins, janelas, qualidade e testes.

## Avançado — 40 exercícios

1. Relacione consulta a jobs, stages e tasks na Spark UI.
2. Identifique shuffle boundaries no DAG/plano.
3. Leia métricas de spill, GC, shuffle e duração.
4. Diagnostique stage lento por poucas tasks.
5. Diagnostique skew por distribuição das tasks.
6. Gere skew intencional em uma chave.
7. Corrija skew com broadcast quando aplicável.
8. Corrija skew com salting e reconcilie o resultado.
9. Avalie Adaptive Query Execution.
10. Compare estratégias de join com/sem hints.
11. Escolha número de partições baseado em volume e recursos.
12. Investigue small files e faça compactação.
13. Compare persistência MEMORY/DISK e custo.
14. Remova cache desnecessário de uma pipeline.
15. Evite `collect`/`toPandas` que exceda o driver.
16. Compare serialização e custo de UDF.
17. Perfilie código executado no driver.
18. Configure memória/cores em experimento controlado.
19. Explique locality e data skew sem depender de memorização.
20. Crie baseline e benchmark reprodutível.
21. Leia stream de arquivos com schema explícito.
22. Faça agregação streaming sem estado ilimitado.
23. Use event time e watermark.
24. Teste evento atrasado antes/depois do watermark.
25. Faça deduplicação streaming com watermark.
26. Faça stream-stream join dentro de limites temporais.
27. Use checkpoint e reinicie sem perder progresso.
28. Compare triggers disponíveis.
29. Escreva em sink idempotente com `foreachBatch`.
30. Implemente batch e streaming com a mesma transformação.
31. Monitore input rate, processing rate e backlog.
32. Simule falha e demonstre recuperação.
33. Evite mudança incompatível de query/state após checkpoint.
34. Crie estratégia de dead-letter/quarentena.
35. Teste streaming com fonte controlada.
36. Empacote dependências para cluster.
37. Defina configurações por ambiente.
38. Crie runbook para OOM, skew e atraso.
39. Faça revisão de custo versus latência.
40. Projeto: job batch + streaming otimizado, observável e recuperável.

## Dados — 40 exercícios

1. Ingerir arquivos brutos adicionando metadados de origem.
2. Preservar raw imutável e reprocessável.
3. Criar Bronze tipada com coluna de conteúdo corrompido.
4. Criar Silver com normalização e deduplicação.
5. Criar Gold com métricas de negócio.
6. Definir contrato de dados e validar schema.
7. Detectar breaking versus non-breaking schema change.
8. Quarentenar registros com múltiplos motivos.
9. Calcular score de qualidade por lote.
10. Criar reconciliação Bronze/Silver/Gold.
11. Implementar carga incremental por partição/data.
12. Implementar watermark com período de sobreposição.
13. Processar evento atrasado e corrigir saída.
14. Garantir idempotência por chave e batch.
15. Implementar upsert em formato/tabela que suporte a operação.
16. Aplicar CDC com inserts, updates e deletes.
17. Implementar SCD tipo 1 distribuída.
18. Implementar SCD tipo 2 distribuída.
19. Tratar dimensão atrasada.
20. Construir fato e dimensões a partir de eventos.
21. Reparticionar sem perder balanceamento.
22. Escolher partições físicas evitando alta cardinalidade.
23. Compactar small files e validar ganho.
24. Otimizar leitura com pruning/pushdown.
25. Processar snapshot histórico grande com backfill.
26. Executar backfill sem afetar lote corrente.
27. Criar checkpoint por partição e retomada.
28. Tornar publicação atômica para consumidores.
29. Registrar lineage por dataset e execução.
30. Propagar `run_id` por todas as etapas.
31. Medir freshness, completude, volume e duração.
32. Detectar anomalia simples de volume.
33. Definir SLA e alerta acionável.
34. Mascarar dados pessoais antes de ambiente de desenvolvimento.
35. Testar permissões conceitualmente por camada.
36. Criar testes unitários, integração e reconciliação.
37. Testar arquivo vazio, duplicado, atrasado e corrompido.
38. Comparar custo/latência de batch e streaming.
39. Documentar arquitetura, grão, contrato e operação.
40. Projeto: medallion local com batch/stream, qualidade e observabilidade.

## Critério de saída

O aluno explica o plano, identifica shuffle/skew, escolhe funções nativas, testa DataFrames e entrega pipeline batch/stream idempotente e observável sem trazer dados grandes ao driver.
