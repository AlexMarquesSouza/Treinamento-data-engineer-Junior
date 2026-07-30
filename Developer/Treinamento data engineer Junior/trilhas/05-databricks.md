# Azure Databricks para Engenharia de Dados

> Interpretação adotada: Azure Databricks usando Python/PySpark, Databricks SQL e integração com SQL Server.

## Divisão

- **Básico:** workspace, compute, notebooks, DBFS/Volumes, SQL, Delta e Git folders.
- **Intermediário:** Jobs, parâmetros, Auto Loader, `MERGE`, qualidade, testes e custos.
- **Avançado:** streaming, performance, governança, segurança, CI/CD e operação.
- **Dados:** arquitetura lakehouse, CDC, SCD, contratos, observabilidade e produto de dados.

Teoria: [Introdução](https://learn.microsoft.com/en-us/azure/databricks/introduction/), [arquitetura](https://learn.microsoft.com/en-us/azure/databricks/getting-started/architecture), [Delta Lake](https://learn.microsoft.com/en-us/azure/databricks/delta/), [Jobs](https://learn.microsoft.com/en-us/azure/databricks/jobs/), [Unity Catalog](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/) e [arquitetura medalhão](https://learn.microsoft.com/en-us/azure/databricks/lakehouse/medallion).

Use recursos da conta definidos pelo mentor, políticas de compute e orçamento. Desligue compute quando não estiver em uso. Nunca coloque segredo em notebook ou Git.

## Básico — 40 exercícios

Use o [roteiro guiado de Databricks básico](../docs/roteiro-nivel-basico.md#databricks-básico--roteiro-dos-40-exercícios). Ele inclui limites de ambiente, segurança, controle de custo, passos de execução e critérios de conclusão.

1. Navegue pelo workspace e desenhe control plane, compute e storage.
2. Crie compute conforme política e registre runtime/limites/custo.
3. Execute notebook Python, SQL e Markdown.
4. Use células parametrizadas e reinicie o estado para provar reprodutibilidade.
5. Organize código em módulo, não apenas em notebook monolítico.
6. Conecte Git folder/repositório e trabalhe em branch.
7. Resolva conflito simples sem perder alterações do notebook.
8. Crie catálogo/schema conforme permissões disponíveis.
9. Explique tabela managed, external e volume.
10. Grave e leia arquivo de Volume sem caminhos pessoais.
11. Leia CSV com schema explícito.
12. Grave Parquet particionado.
13. Crie tabela Delta managed.
14. Consulte tabela com Databricks SQL.
15. Use `DESCRIBE DETAIL` e `DESCRIBE HISTORY`.
16. Faça append e valide versão.
17. Atualize e exclua linhas Delta em laboratório.
18. Consulte versão anterior com time travel.
19. Restaure ou recrie estado a partir do histórico.
20. Demonstre schema enforcement.
21. Evolua schema de forma controlada.
22. Faça `MERGE` simples por chave.
23. Garanta que reexecutar o `MERGE` não duplica.
24. Crie temp view e view persistente.
25. Use SQL warehouse e compare finalidade com all-purpose compute.
26. Parametrize notebook por data de processamento.
27. Instale dependência conforme política e fixe versão.
28. Use secrets scope fornecido sem revelar o valor.
29. Acesse SQL Server por JDBC com credenciais seguras.
30. Leia tabela SQL Server com particionamento apropriado.
31. Grave resultado pequeno em SQL Server com transação/estratégia documentada.
32. Crie Bronze a partir de arquivos raw.
33. Crie Silver limpa e deduplicada.
34. Crie Gold agregada para uma pergunta de negócio.
35. Acrescente colunas de auditoria e `run_id`.
36. Separe registros inválidos em quarentena.
37. Gere métricas de entrada/saída/rejeição.
38. Execute notebook do início ao fim em sessão limpa.
39. Documente custo, segurança, inputs e outputs.
40. Projeto: pipeline manual SQL Server/arquivos → Bronze → Silver → Gold.

## Intermediário — 40 exercícios

1. Converta notebook em Job com uma task.
2. Crie Job multi-task com dependências.
3. Passe parâmetros entre execução e task.
4. Use valores de task/saídas pequenas sem acoplamento frágil.
5. Configure schedule e timezone corretamente.
6. Configure retry apenas para erro transitório.
7. Configure timeout e notificações.
8. Execute reparo apenas das tasks falhas.
9. Use job compute conforme política e compare custo.
10. Implemente biblioteca Wheel usada pelo Job.
11. Crie configuração dev/test/prod sem duplicar código.
12. Ingerir diretório incrementalmente com Auto Loader.
13. Defina schema location e checkpoint separados.
14. Capture dados resgatados/malformados.
15. Evolua coluna aditiva de forma controlada.
16. Interrompa alteração incompatível com erro claro.
17. Use trigger adequado para micro-batch disponível.
18. Reinicie Auto Loader e prove exactly-once no sink Delta.
19. Implemente `foreachBatch` idempotente.
20. Faça `MERGE` com inserts e updates.
21. Propague deletes vindos do SQL Server.
22. Implemente SCD tipo 1 em Delta.
23. Implemente SCD tipo 2 em Delta.
24. Trate eventos fora de ordem.
25. Use expectativas/regras de qualidade disponíveis.
26. Separe regras críticas e avisos.
27. Publique métricas de qualidade por execução.
28. Crie testes unitários de funções Spark.
29. Crie teste de integração sobre schema temporário.
30. Use dados sintéticos e limpe recursos do teste.
31. Analise plano e aplique broadcast quando comprovado.
32. Execute `OPTIMIZE` em laboratório e compare arquivos.
33. Avalie `ZORDER`/clustering conforme recurso e padrão de consulta.
34. Demonstre data skipping e pruning.
35. Evite `VACUUM` agressivo e explique retenção/time travel.
36. Consulte histórico para auditar alteração.
37. Configure permissões mínimas em catálogo/schema/tabela de laboratório.
38. Verifique lineage disponível no Unity Catalog.
39. Crie dashboard SQL operacional simples.
40. Projeto: Job incremental, testado, com qualidade e alertas.

## Avançado — 40 exercícios

1. Compare compute clássico, serverless e SQL warehouse disponíveis.
2. Escolha política/autoscaling para três workloads e justifique.
3. Analise custo por execução com tags/métricas disponíveis.
4. Reduza tempo ocioso e prove economia.
5. Use Spark UI para diagnosticar stage lento.
6. Corrija skew em join e compare duração.
7. Corrija small files com estratégia preventiva e corretiva.
8. Avalie liquid clustering/particionamento para tabela grande.
9. Otimize `MERGE` restringindo o conjunto alvo.
10. Compare Photon ligado/desligado onde disponível.
11. Defina propriedades e retenção de tabela com justificativa.
12. Execute `VACUUM` seguro e prove que política foi respeitada.
13. Monitore streaming query, backlog e throughput.
14. Configure watermark e teste evento atrasado.
15. Faça stream-stream join limitado por tempo.
16. Recupere streaming após falha mantendo checkpoint.
17. Planeje mudança incompatível de estado/checkpoint.
18. Implemente backfill separado do fluxo corrente.
19. Implemente CDC com múltiplas mudanças da mesma chave.
20. Ordene eventos por sequência confiável.
21. Use Change Data Feed em laboratório.
22. Construa consumidor incremental de CDF.
23. Crie materialização Gold incremental.
24. Compare pipeline declarativa disponível e Job imperativo.
25. Defina isolamento por catálogo e ambiente.
26. Crie service principal/identidade gerenciada conceitualmente ou em sandbox.
27. Aplique grants mínimos e teste negações.
28. Use external location/storage credential conforme autorização.
29. Implemente view dinâmica para filtro por usuário/grupo.
30. Mascare coluna sensível por política/view.
31. Audite acessos com system tables/logs disponíveis.
32. Versione notebook, código, configuração e definição de Job.
33. Configure lint/test/build em CI.
34. Faça deploy automatizado em ambiente de teste.
35. Promova artefato imutável para outro ambiente.
36. Teste rollback de código e compatibilidade de dados.
37. Crie SLI/SLO de freshness, sucesso e qualidade.
38. Crie alerta com runbook e responsável.
39. Faça game day de falha de origem, schema e permissão.
40. Projeto: pipeline produtivo seguro, otimizado, implantável e recuperável.

## Dados — 40 exercícios

1. Desenhe domínios, fontes, consumidores, SLA e classificação.
2. Defina catálogo/schema para Bronze, Silver e Gold.
3. Crie landing zone e convenção de caminhos.
4. Preserve raw imutável com metadados de ingestão.
5. Ingerir SQL Server full load inicial.
6. Ingerir SQL Server incremental por watermark.
7. Ingerir SQL Server por CDC/Change Tracking quando disponível.
8. Reconciliar snapshot inicial e incremental.
9. Tratar registros atrasados e fora de ordem.
10. Capturar deletes físicos/lógicos.
11. Criar Bronze Delta idempotente.
12. Criar Silver com contrato, tipos e deduplicação.
13. Criar quarentena reprocessável.
14. Implementar chaves e regras de integridade.
15. Criar dimensões conformadas.
16. Implementar SCD1.
17. Implementar SCD2.
18. Tratar dimensão atrasada.
19. Criar fato no grão documentado.
20. Criar Gold para BI sem duplicar regra.
21. Publicar produto com owner, SLA e descrição.
22. Registrar lineage e dependências.
23. Medir volume, completude, unicidade e validade.
24. Medir freshness ponta a ponta.
25. Detectar anomalia de volume/esquema.
26. Criar alertas com contexto acionável.
27. Realizar backfill de período histórico.
28. Reprocessar lote falho sem duplicação.
29. Recuperar de checkpoint perdido com procedimento seguro.
30. Testar disaster recovery conceitual de metadados/dados/código.
31. Otimizar layout baseado em consultas reais.
32. Controlar custo por workload e ambiente.
33. Aplicar retenção e descarte conforme requisito.
34. Proteger PII com acesso mínimo e mascaramento.
35. Criar testes de contrato para produtor/consumidor.
36. Criar testes de reconciliação SQL Server versus Delta.
37. Criar dashboard operacional e de qualidade.
38. Documentar runbook, ownership e escalação.
39. Demonstrar CI/CD e promoção entre ambientes.
40. Projeto: produto de dados SQL Server → lakehouse governado → BI.

## Critério de saída

O aluno entrega no Azure Databricks um produto incremental e idempotente, orquestrado por Jobs, governado no Unity Catalog, com Delta, testes, qualidade, lineage, alertas, CI/CD e explicação de custo/performance.
