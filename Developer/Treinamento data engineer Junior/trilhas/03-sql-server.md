# SQL Server e T-SQL para Engenharia de Dados

## Divisão e ambiente

- **Básico:** modelo relacional, DDL/DML, `SELECT`, filtros, joins, agregações e funções.
- **Intermediário:** subqueries, CTEs, janelas, views, procedures, transações e modelagem.
- **Avançado:** planos, índices, concorrência, segurança, particionamento, CDC e operação.
- **Dados:** staging, ETL/ELT, incremental, SCD, qualidade, reconciliação e warehouse.

Use SQL Server Developer/Express e o banco de exemplo [AdventureWorks](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure). Teoria: [trilha T-SQL da Microsoft](https://learn.microsoft.com/en-us/training/paths/get-started-querying-with-transact-sql/), [referência T-SQL](https://learn.microsoft.com/en-us/sql/t-sql/language-reference) e [guia de índices](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes).

Cada exercício deve incluir script reexecutável, dados de teste, consulta de validação e explicação do resultado.

## Básico — 40 exercícios

Use o [roteiro guiado de SQL Server básico](../docs/roteiro-nivel-basico.md#sql-server-básico--roteiro-dos-40-exercícios). Ele separa setup, solução e validação e inclui uma rotina segura para alterações de dados.

1. Crie banco e schemas `raw`, `stg` e `dbo` com convenção documentada.
2. Modele clientes com tipos, nulabilidade, `PRIMARY KEY`, `UNIQUE` e `CHECK`.
3. Modele pedidos/itens com chaves estrangeiras e regra de quantidade/preço.
4. Insira dados válidos e provoque cada restrição para observar os erros.
5. Use `SELECT`, aliases e expressões para calcular total de item.
6. Filtre datas, faixas, listas, padrões e nulos com semântica correta.
7. Ordene e pagine resultados de modo determinístico.
8. Elimine duplicados com `DISTINCT` e explique quando ele mascara problema.
9. Classifique pedidos com `CASE`.
10. Trate nulos com `COALESCE` e `NULLIF`.
11. Use funções de texto para normalizar nomes.
12. Extraia partes de datas e calcule prazos.
13. Converta tipos com `CAST`, `CONVERT`, `TRY_CAST` e compare falhas.
14. Agregue vendas com `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`.
15. Agrupe por mês e categoria.
16. Filtre grupos com `HAVING`.
17. Compare `COUNT(*)`, `COUNT(coluna)` e `COUNT(DISTINCT ...)`.
18. Faça `INNER JOIN` de pedidos, clientes e itens.
19. Use `LEFT JOIN` para localizar clientes sem pedidos.
20. Demonstre `RIGHT`/`FULL JOIN` e reescreva de forma mais legível.
21. Use self join para hierarquia de funcionários.
22. Identifique multiplicação indevida de linhas em um join N:N.
23. Combine conjuntos com `UNION` e `UNION ALL`.
24. Compare `EXCEPT` e `INTERSECT` para reconciliação.
25. Use subquery escalar para comparar venda com média.
26. Use `EXISTS` e `NOT EXISTS` para presença/ausência.
27. Compare `IN` e `EXISTS`, incluindo nulos.
28. Insira linhas explicitando colunas e capture IDs gerados.
29. Atualize apenas linhas-alvo e valide antes/depois.
30. Exclua com segurança dentro de transação.
31. Use `TRUNCATE` em tabela de laboratório e compare com `DELETE`.
32. Copie resultado para nova tabela com `SELECT INTO` e discuta limites.
33. Crie tabela temporária para relatório em duas etapas.
34. Use variável de tabela em caso pequeno e compare propósito.
35. Crie view de vendas detalhadas.
36. Consulte metadados de tabelas, colunas e restrições.
37. Gere calendário de 30 dias com CTE recursiva simples.
38. Crie script idempotente de seed.
39. Resolva dez perguntas de negócio no AdventureWorks.
40. Entregue um banco OLTP pequeno com modelo, carga e relatório.

## Intermediário — 40 exercícios

1. Reescreva consulta aninhada usando CTE para clareza.
2. Encadeie CTEs para etapas de transformação.
3. Percorra hierarquia com CTE recursiva e limite seguro.
4. Numere vendas com `ROW_NUMBER`.
5. Compare `ROW_NUMBER`, `RANK` e `DENSE_RANK`.
6. Selecione o registro mais recente por cliente.
7. Calcule acumulado com janela.
8. Calcule média móvel de sete dias.
9. Compare período atual com anterior usando `LAG`.
10. Encontre intervalos entre eventos usando `LEAD`.
11. Calcule participação no total com janela.
12. Use `FIRST_VALUE`/`LAST_VALUE` definindo frame corretamente.
13. Resolva gaps and islands de dias consecutivos.
14. Faça pivot de vendas por trimestre.
15. Reverta colunas para linhas com `UNPIVOT` ou `CROSS APPLY`.
16. Quebre string/JSON em linhas e valide tipos.
17. Gere JSON hierárquico a partir de tabelas relacionais.
18. Crie view com `SCHEMABINDING` e investigue restrições.
19. Crie função inline table-valued e compare com view.
20. Crie procedure de relatório com parâmetros opcionais seguros.
21. Retorne status e mensagem de uma procedure.
22. Use transação explícita para transferência entre contas.
23. Trate erro com `TRY/CATCH`, `THROW` e rollback.
24. Demonstre `XACT_STATE()` após falha.
25. Compare níveis de isolamento em duas sessões.
26. Reproduza dirty read e explique por que evitá-lo.
27. Reproduza bloqueio e identifique a sessão bloqueadora.
28. Crie sequência e compare com `IDENTITY`.
29. Modele relacionamento N:N corretamente.
30. Normalize planilha desnormalizada até 3FN.
31. Modele estrela com fato e dimensões.
32. Defina grão de uma fato antes de criar colunas.
33. Crie índices clustered/nonclustered básicos.
34. Compare plano e leituras antes/depois de um índice.
35. Crie índice composto e teste ordem das chaves.
36. Use colunas `INCLUDE` para cobrir uma consulta.
37. Identifique conversão implícita que impede seek.
38. Evite função sobre coluna filtrada e torne consulta sargable.
39. Teste procedure e transformação com tSQLt ou harness de assertions.
40. Entregue um mart dimensional com procedures e consultas analíticas.

## Avançado — 40 exercícios

1. Leia plano estimado e real e explique operadores principais.
2. Meça `STATISTICS IO/TIME` de uma consulta.
3. Corrija estimativa ruim atualizando/investigando estatísticas.
4. Reproduza parameter sniffing e compare estratégias de correção.
5. Detecte spill de sort/hash e reduza sua causa.
6. Compare nested loops, merge e hash join em cenários controlados.
7. Crie índice filtrado para subconjunto seletivo.
8. Crie coluna calculada persistida e indexe-a.
9. Avalie fragmentação sem automatizar rebuild indiscriminado.
10. Investigue índices ausentes e redundantes com DMVs.
11. Crie tabela particionada por data em laboratório.
12. Faça manutenção de partição com estratégia de janela deslizante.
13. Teste compressão row/page e impacto.
14. Crie columnstore em fato analítica e compare agregações.
15. Use batch mode e analise o plano disponível.
16. Crie deadlock intencional em laboratório e corrija ordem de acesso.
17. Implemente retry de deadlock no cliente.
18. Use snapshot isolation e compare bloqueio/version store.
19. Discuta atomicidade de DDL/DML em uma migração.
20. Crie procedure idempotente de upsert sem corrida.
21. Compare `MERGE` com `UPDATE` + `INSERT` e escolha com justificativa.
22. Use application lock para serializar etapa crítica.
23. Implemente auditoria temporal com temporal table.
24. Habilite Change Tracking e extraia alterações.
25. Habilite CDC em laboratório e interprete operações.
26. Crie usuário, role e princípio de menor privilégio.
27. Implemente row-level security para dois tenants.
28. Aplique dynamic data masking e explique seus limites.
29. Proteja valores sensíveis e evite registrá-los em logs.
30. Audite acessos/alterações relevantes.
31. Crie job no SQL Server Agent com etapas e alertas.
32. Faça backup/restore de laboratório e valide recuperação.
33. Investigue crescimento de log causado por transação longa.
34. Carregue alto volume em lotes e compare tamanho de batch.
35. Use `BULK INSERT`/BCP em arquivo controlado.
36. Consulte Parquet/arquivo externo com recurso disponível e documente pré-requisitos.
37. Crie estratégia de migração de schema compatível com rollback.
38. Capture regressão de consulta com Query Store.
39. Monte runbook de lentidão, bloqueio e falha de carga.
40. Faça tuning completo de uma carga, provando ganho e ausência de regressão.

## Dados — 40 exercícios

1. Crie tabelas `raw` que preservem valores recebidos.
2. Crie staging tipada e tabela de rejeições com motivo.
3. Carregue CSV para staging e valide contagem/encoding/delimitador.
4. Converta dados com `TRY_CONVERT` sem abortar todo o lote.
5. Registre execução, início, fim, status e contagens.
6. Implemente carga completa reexecutável.
7. Implemente incremental por watermark.
8. Trate registros atrasados usando janela de sobreposição.
9. Implemente incremental por Change Tracking.
10. Implemente incremental por CDC.
11. Deduplicate staging com regra determinística.
12. Faça upsert de dimensão com chave de negócio.
13. Implemente dimensão SCD tipo 1.
14. Implemente dimensão SCD tipo 2.
15. Crie surrogate keys e trate membro desconhecido.
16. Carregue fato respeitando o grão.
17. Trate late-arriving dimension.
18. Gere dimensão data completa.
19. Modele fato transacional.
20. Modele periodic snapshot.
21. Modele accumulating snapshot.
22. Crie tabela ponte para relacionamento multivalorado.
23. Implemente soft delete vindo da origem.
24. Reconcilie origem/destino por contagem, soma e hash.
25. Crie regras de qualidade em tabela orientada a metadados.
26. Coloque falhas críticas em quarentena e alerte.
27. Meça completude, unicidade, validade e integridade.
28. Detecte mudança de schema antes da carga.
29. Garanta idempotência por `batch_id` e chave.
30. Retome carga interrompida a partir de checkpoint.
31. Processe partições em paralelo sem sobreposição.
32. Faça swap seguro de tabela para publicação.
33. Crie camada semântica de views Gold.
34. Implemente segurança por domínio/tenant no mart.
35. Documente lineage coluna a coluna.
36. Defina SLA, RPO, RTO e retenção do pipeline.
37. Crie consultas operacionais de atraso, volume e erro.
38. Teste carga com arquivo vazio, duplicado, corrompido e fora de ordem.
39. Compare ETL e ELT para o mesmo caso.
40. Projeto: SQL Server `raw → staging → dimensional`, incremental e auditável.

## Critério de saída

O aluno modela um mart, escreve consultas analíticas, implementa carga incremental/SCD, prova idempotência e reconciliação, interpreta plano e diagnostica bloqueio sem aplicar “soluções mágicas”.
