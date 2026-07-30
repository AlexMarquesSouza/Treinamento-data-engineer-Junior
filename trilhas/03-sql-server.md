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
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
2. Modele clientes com tipos, nulabilidade, `PRIMARY KEY`, `UNIQUE` e `CHECK`.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
3. Modele pedidos/itens com chaves estrangeiras e regra de quantidade/preço.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
4. Insira dados válidos e provoque cada restrição para observar os erros.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
5. Use `SELECT`, aliases e expressões para calcular total de item.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
6. Filtre datas, faixas, listas, padrões e nulos com semântica correta.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
7. Ordene e pagine resultados de modo determinístico.
   - **Exemplo-base:** Ordene três livros por autor e depois título usando uma tupla como chave.
8. Elimine duplicados com `DISTINCT` e explique quando ele mascara problema.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
9. Classifique pedidos com `CASE`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
10. Trate nulos com `COALESCE` e `NULLIF`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
11. Use funções de texto para normalizar nomes.
   - **Exemplo-base:** Transforme `  ana   silva ` em `Ana Silva`.
12. Extraia partes de datas e calcule prazos.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
13. Converta tipos com `CAST`, `CONVERT`, `TRY_CAST` e compare falhas.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
14. Agregue vendas com `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
15. Agrupe por mês e categoria.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
16. Filtre grupos com `HAVING`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
17. Compare `COUNT(*)`, `COUNT(coluna)` e `COUNT(DISTINCT ...)`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
18. Faça `INNER JOIN` de pedidos, clientes e itens.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
19. Use `LEFT JOIN` para localizar clientes sem pedidos.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
20. Demonstre `RIGHT`/`FULL JOIN` e reescreva de forma mais legível.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
21. Use self join para hierarquia de funcionários.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
22. Identifique multiplicação indevida de linhas em um join N:N.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
23. Combine conjuntos com `UNION` e `UNION ALL`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
24. Compare `EXCEPT` e `INTERSECT` para reconciliação.
   - **Exemplo-base:** Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino.
25. Use subquery escalar para comparar venda com média.
   - **Exemplo-base:** Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`.
26. Use `EXISTS` e `NOT EXISTS` para presença/ausência.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
27. Compare `IN` e `EXISTS`, incluindo nulos.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
28. Insira linhas explicitando colunas e capture IDs gerados.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
29. Atualize apenas linhas-alvo e valide antes/depois.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
30. Exclua com segurança dentro de transação.
   - **Exemplo-base:** Debite 10 de uma conta em transação; valide e execute rollback na primeira vez.
31. Use `TRUNCATE` em tabela de laboratório e compare com `DELETE`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
32. Copie resultado para nova tabela com `SELECT INTO` e discuta limites.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
33. Crie tabela temporária para relatório em duas etapas.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
34. Use variável de tabela em caso pequeno e compare propósito.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
35. Crie view de vendas detalhadas.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
36. Consulte metadados de tabelas, colunas e restrições.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
37. Gere calendário de 30 dias com CTE recursiva simples.
   - **Exemplo-base:** Crie uma CTE com 1, 2 e 3 e selecione apenas valores maiores que 1.
38. Crie script idempotente de seed.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
39. Resolva dez perguntas de negócio no AdventureWorks.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
40. Entregue um banco OLTP pequeno com modelo, carga e relatório.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.

## Intermediário — 40 exercícios

1. Reescreva consulta aninhada usando CTE para clareza.
   - **Exemplo-base:** Crie uma CTE com 1, 2 e 3 e selecione apenas valores maiores que 1.
2. Encadeie CTEs para etapas de transformação.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
3. Percorra hierarquia com CTE recursiva e limite seguro.
   - **Exemplo-base:** Crie uma CTE com 1, 2 e 3 e selecione apenas valores maiores que 1.
4. Numere vendas com `ROW_NUMBER`.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
5. Compare `ROW_NUMBER`, `RANK` e `DENSE_RANK`.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
6. Selecione o registro mais recente por cliente.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
7. Calcule acumulado com janela.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
8. Calcule média móvel de sete dias.
   - **Exemplo-base:** Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`.
9. Compare período atual com anterior usando `LAG`.
   - **Exemplo-base:** Com vendas `[10,20,5]`, produza acumulado `[10,30,35]`.
10. Encontre intervalos entre eventos usando `LEAD`.
   - **Exemplo-base:** Com vendas `[10,20,5]`, produza acumulado `[10,30,35]`.
11. Calcule participação no total com janela.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
12. Use `FIRST_VALUE`/`LAST_VALUE` definindo frame corretamente.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
13. Resolva gaps and islands de dias consecutivos.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
14. Faça pivot de vendas por trimestre.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
15. Reverta colunas para linhas com `UNPIVOT` ou `CROSS APPLY`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
16. Quebre string/JSON em linhas e valide tipos.
   - **Exemplo-base:** Leia `[{"item":"livro","qtd":2}]` e obtenha quantidade total `2`.
17. Gere JSON hierárquico a partir de tabelas relacionais.
   - **Exemplo-base:** Leia `[{"item":"livro","qtd":2}]` e obtenha quantidade total `2`.
18. Crie view com `SCHEMABINDING` e investigue restrições.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
19. Crie função inline table-valued e compare com view.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
20. Crie procedure de relatório com parâmetros opcionais seguros.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
21. Retorne status e mensagem de uma procedure.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
22. Use transação explícita para transferência entre contas.
   - **Exemplo-base:** Debite 10 de uma conta em transação; valide e execute rollback na primeira vez.
23. Trate erro com `TRY/CATCH`, `THROW` e rollback.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
24. Demonstre `XACT_STATE()` após falha.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
25. Compare níveis de isolamento em duas sessões.
   - **Exemplo-base:** Em duas sessões, deixe uma atualização sem commit e observe a segunda aguardar.
26. Reproduza dirty read e explique por que evitá-lo.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
27. Reproduza bloqueio e identifique a sessão bloqueadora.
   - **Exemplo-base:** Em duas sessões, deixe uma atualização sem commit e observe a segunda aguardar.
28. Crie sequência e compare com `IDENTITY`.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
29. Modele relacionamento N:N corretamente.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
30. Normalize planilha desnormalizada até 3FN.
   - **Exemplo-base:** Transforme `  ana   silva ` em `Ana Silva`.
31. Modele estrela com fato e dimensões.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
32. Defina grão de uma fato antes de criar colunas.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
33. Crie índices clustered/nonclustered básicos.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
34. Compare plano e leituras antes/depois de um índice.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
35. Crie índice composto e teste ordem das chaves.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
36. Use colunas `INCLUDE` para cobrir uma consulta.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
37. Identifique conversão implícita que impede seek.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
38. Evite função sobre coluna filtrada e torne consulta sargable.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
39. Teste procedure e transformação com tSQLt ou harness de assertions.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
40. Entregue um mart dimensional com procedures e consultas analíticas.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.

## Avançado — 40 exercícios

1. Leia plano estimado e real e explique operadores principais.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
2. Meça `STATISTICS IO/TIME` de uma consulta.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
3. Corrija estimativa ruim atualizando/investigando estatísticas.
   - **Exemplo-base:** Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`.
4. Reproduza parameter sniffing e compare estratégias de correção.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
5. Detecte spill de sort/hash e reduza sua causa.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
6. Compare nested loops, merge e hash join em cenários controlados.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
7. Crie índice filtrado para subconjunto seletivo.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
8. Crie coluna calculada persistida e indexe-a.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
9. Avalie fragmentação sem automatizar rebuild indiscriminado.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
10. Investigue índices ausentes e redundantes com DMVs.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
11. Crie tabela particionada por data em laboratório.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
12. Faça manutenção de partição com estratégia de janela deslizante.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
13. Teste compressão row/page e impacto.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
14. Crie columnstore em fato analítica e compare agregações.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
15. Use batch mode e analise o plano disponível.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
16. Crie deadlock intencional em laboratório e corrija ordem de acesso.
   - **Exemplo-base:** Em duas sessões, deixe uma atualização sem commit e observe a segunda aguardar.
17. Implemente retry de deadlock no cliente.
   - **Exemplo-base:** Simule uma função que falha uma vez e funciona na segunda; valide duas tentativas.
18. Use snapshot isolation e compare bloqueio/version store.
   - **Exemplo-base:** Em duas sessões, deixe uma atualização sem commit e observe a segunda aguardar.
19. Discuta atomicidade de DDL/DML em uma migração.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
20. Crie procedure idempotente de upsert sem corrida.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
21. Compare `MERGE` com `UPDATE` + `INSERT` e escolha com justificativa.
   - **Exemplo-base:** Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção.
22. Use application lock para serializar etapa crítica.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
23. Implemente auditoria temporal com temporal table.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
24. Habilite Change Tracking e extraia alterações.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
25. Habilite CDC em laboratório e interprete operações.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
26. Crie usuário, role e princípio de menor privilégio.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
27. Implemente row-level security para dois tenants.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
28. Aplique dynamic data masking e explique seus limites.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
29. Proteja valores sensíveis e evite registrá-los em logs.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
30. Audite acessos/alterações relevantes.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
31. Crie job no SQL Server Agent com etapas e alertas.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
32. Faça backup/restore de laboratório e valide recuperação.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
33. Investigue crescimento de log causado por transação longa.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.
34. Carregue alto volume em lotes e compare tamanho de batch.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
35. Use `BULK INSERT`/BCP em arquivo controlado.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
36. Consulte Parquet/arquivo externo com recurso disponível e documente pré-requisitos.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
37. Crie estratégia de migração de schema compatível com rollback.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
38. Capture regressão de consulta com Query Store.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
39. Monte runbook de lentidão, bloqueio e falha de carga.
   - **Exemplo-base:** Em duas sessões, deixe uma atualização sem commit e observe a segunda aguardar.
40. Faça tuning completo de uma carga, provando ganho e ausência de regressão.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.

## Dados — 40 exercícios

1. Crie tabelas `raw` que preservem valores recebidos.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
2. Crie staging tipada e tabela de rejeições com motivo.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
3. Carregue CSV para staging e valide contagem/encoding/delimitador.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
4. Converta dados com `TRY_CONVERT` sem abortar todo o lote.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
5. Registre execução, início, fim, status e contagens.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
6. Implemente carga completa reexecutável.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
7. Implemente incremental por watermark.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
8. Trate registros atrasados usando janela de sobreposição.
   - **Exemplo-base:** Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1.
9. Implemente incremental por Change Tracking.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
10. Implemente incremental por CDC.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
11. Deduplicate staging com regra determinística.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
12. Faça upsert de dimensão com chave de negócio.
   - **Exemplo-base:** Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção.
13. Implemente dimensão SCD tipo 1.
   - **Exemplo-base:** Cliente 1 muda de A para B; substitua A por B sem histórico.
14. Implemente dimensão SCD tipo 2.
   - **Exemplo-base:** Encerre a versão A do cliente e crie B marcada como atual.
15. Crie surrogate keys e trate membro desconhecido.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
16. Carregue fato respeitando o grão.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
17. Trate late-arriving dimension.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
18. Gere dimensão data completa.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
19. Modele fato transacional.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
20. Modele periodic snapshot.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
21. Modele accumulating snapshot.
   - **Exemplo-base:** Modele `Livro(titulo="Duna", paginas=500)` e rejeite páginas negativas.
22. Crie tabela ponte para relacionamento multivalorado.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
23. Implemente soft delete vindo da origem.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
24. Reconcilie origem/destino por contagem, soma e hash.
   - **Exemplo-base:** Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino.
25. Crie regras de qualidade em tabela orientada a metadados.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
26. Coloque falhas críticas em quarentena e alerte.
   - **Exemplo-base:** Separe `{id:1}` como válido e `{id:null}` com motivo `id_obrigatorio`.
27. Meça completude, unicidade, validade e integridade.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
28. Detecte mudança de schema antes da carga.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
29. Garanta idempotência por `batch_id` e chave.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
30. Retome carga interrompida a partir de checkpoint.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
31. Processe partições em paralelo sem sobreposição.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
32. Faça swap seguro de tabela para publicação.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
33. Crie camada semântica de views Gold.
   - **Exemplo-base:** Bronze guarda `" ANA "`; Silver produz `Ana`; Gold conta um cliente.
34. Implemente segurança por domínio/tenant no mart.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
35. Documente lineage coluna a coluna.
   - **Exemplo-base:** Crie `saida_exemplo` de `entrada_exemplo` e confira a dependência no lineage.
36. Defina SLA, RPO, RTO e retenção do pipeline.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
37. Crie consultas operacionais de atraso, volume e erro.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
38. Teste carga com arquivo vazio, duplicado, corrompido e fora de ordem.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
39. Compare ETL e ELT para o mesmo caso.
   - **Exemplo-base:** Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.
40. Projeto: SQL Server `raw → staging → dimensional`, incremental e auditável.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.

## Critério de saída

O aluno modela um mart, escreve consultas analíticas, implementa carga incremental/SCD, prova idempotência e reconciliação, interpreta plano e diagnostica bloqueio sem aplicar “soluções mágicas”.
