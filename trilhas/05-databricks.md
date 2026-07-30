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
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
2. Crie compute conforme política e registre runtime/limites/custo.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
3. Execute notebook Python, SQL e Markdown.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
4. Use células parametrizadas e reinicie o estado para provar reprodutibilidade.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
5. Organize código em módulo, não apenas em notebook monolítico.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
6. Conecte Git folder/repositório e trabalhe em branch.
   - **Exemplo-base:** Crie `lista-compras`, adicione um README de duas linhas e faça um commit chamado `cria lista`.
7. Resolva conflito simples sem perder alterações do notebook.
   - **Exemplo-base:** Em duas branches, mude o preço do mesmo café; faça merge e escolha o valor final.
8. Crie catálogo/schema conforme permissões disponíveis.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
9. Explique tabela managed, external e volume.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
10. Grave e leia arquivo de Volume sem caminhos pessoais.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
11. Leia CSV com schema explícito.
   - **Exemplo-base:** Leia `nome,idade\nAna,20` e produza `Ana tem 20 anos`.
12. Grave Parquet particionado.
   - **Exemplo-base:** Grave três livros em Parquet, leia só `titulo` e confirme três linhas.
13. Crie tabela Delta managed.
   - **Exemplo-base:** Crie Delta com dois livros, atualize um título e consulte versões 0 e 1.
14. Consulte tabela com Databricks SQL.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
15. Use `DESCRIBE DETAIL` e `DESCRIBE HISTORY`.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
16. Faça append e valide versão.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
17. Atualize e exclua linhas Delta em laboratório.
   - **Exemplo-base:** Crie Delta com dois livros, atualize um título e consulte versões 0 e 1.
18. Consulte versão anterior com time travel.
   - **Exemplo-base:** Crie Delta com dois livros, atualize um título e consulte versões 0 e 1.
19. Restaure ou recrie estado a partir do histórico.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.
20. Demonstre schema enforcement.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
21. Evolua schema de forma controlada.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
22. Faça `MERGE` simples por chave.
   - **Exemplo-base:** Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção.
23. Garanta que reexecutar o `MERGE` não duplica.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
24. Crie temp view e view persistente.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
25. Use SQL warehouse e compare finalidade com all-purpose compute.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
26. Parametrize notebook por data de processamento.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
27. Instale dependência conforme política e fixe versão.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
28. Use secrets scope fornecido sem revelar o valor.
   - **Exemplo-base:** Leia segredo pelo mecanismo do ambiente e use-o sem imprimir ou versionar.
29. Acesse SQL Server por JDBC com credenciais seguras.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
30. Leia tabela SQL Server com particionamento apropriado.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
31. Grave resultado pequeno em SQL Server com transação/estratégia documentada.
   - **Exemplo-base:** Debite 10 de uma conta em transação; valide e execute rollback na primeira vez.
32. Crie Bronze a partir de arquivos raw.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
33. Crie Silver limpa e deduplicada.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
34. Crie Gold agregada para uma pergunta de negócio.
   - **Exemplo-base:** Bronze guarda `" ANA "`; Silver produz `Ana`; Gold conta um cliente.
35. Acrescente colunas de auditoria e `run_id`.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
36. Separe registros inválidos em quarentena.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
37. Gere métricas de entrada/saída/rejeição.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
38. Execute notebook do início ao fim em sessão limpa.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
39. Documente custo, segurança, inputs e outputs.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
40. Projeto: pipeline manual SQL Server/arquivos → Bronze → Silver → Gold.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.

## Intermediário — 40 exercícios

1. Converta notebook em Job com uma task.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
2. Crie Job multi-task com dependências.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
3. Passe parâmetros entre execução e task.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
4. Use valores de task/saídas pequenas sem acoplamento frágil.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
5. Configure schedule e timezone corretamente.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
6. Configure retry apenas para erro transitório.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
7. Configure timeout e notificações.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
8. Execute reparo apenas das tasks falhas.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
9. Use job compute conforme política e compare custo.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
10. Implemente biblioteca Wheel usada pelo Job.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
11. Crie configuração dev/test/prod sem duplicar código.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
12. Ingerir diretório incrementalmente com Auto Loader.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
13. Defina schema location e checkpoint separados.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
14. Capture dados resgatados/malformados.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
15. Evolua coluna aditiva de forma controlada.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
16. Interrompa alteração incompatível com erro claro.
   - **Exemplo-base:** Converta `"abc"` para inteiro, capture `ValueError` e retorne mensagem curta.
17. Use trigger adequado para micro-batch disponível.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
18. Reinicie Auto Loader e prove exactly-once no sink Delta.
   - **Exemplo-base:** Crie Delta com dois livros, atualize um título e consulte versões 0 e 1.
19. Implemente `foreachBatch` idempotente.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
20. Faça `MERGE` com inserts e updates.
   - **Exemplo-base:** Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção.
21. Propague deletes vindos do SQL Server.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
22. Implemente SCD tipo 1 em Delta.
   - **Exemplo-base:** Cliente 1 muda de A para B; substitua A por B sem histórico.
23. Implemente SCD tipo 2 em Delta.
   - **Exemplo-base:** Encerre a versão A do cliente e crie B marcada como atual.
24. Trate eventos fora de ordem.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
25. Use expectativas/regras de qualidade disponíveis.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
26. Separe regras críticas e avisos.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
27. Publique métricas de qualidade por execução.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
28. Crie testes unitários de funções Spark.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
29. Crie teste de integração sobre schema temporário.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
30. Use dados sintéticos e limpe recursos do teste.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
31. Analise plano e aplique broadcast quando comprovado.
   - **Exemplo-base:** Consulte três livros por código, veja o plano, crie índice de laboratório e compare.
32. Execute `OPTIMIZE` em laboratório e compare arquivos.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
33. Avalie `ZORDER`/clustering conforme recurso e padrão de consulta.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
34. Demonstre data skipping e pruning.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
35. Evite `VACUUM` agressivo e explique retenção/time travel.
   - **Exemplo-base:** Crie Delta com dois livros, atualize um título e consulte versões 0 e 1.
36. Consulte histórico para auditar alteração.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.
37. Configure permissões mínimas em catálogo/schema/tabela de laboratório.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
38. Verifique lineage disponível no Unity Catalog.
   - **Exemplo-base:** Conceda apenas `SELECT` de uma tabela de laboratório a um grupo de teste.
39. Crie dashboard SQL operacional simples.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
40. Projeto: Job incremental, testado, com qualidade e alertas.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.

## Avançado — 40 exercícios

1. Compare compute clássico, serverless e SQL warehouse disponíveis.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
2. Escolha política/autoscaling para três workloads e justifique.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
3. Analise custo por execução com tags/métricas disponíveis.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
4. Reduza tempo ocioso e prove economia.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
5. Use Spark UI para diagnosticar stage lento.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
6. Corrija skew em join e compare duração.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
7. Corrija small files com estratégia preventiva e corretiva.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
8. Avalie liquid clustering/particionamento para tabela grande.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
9. Otimize `MERGE` restringindo o conjunto alvo.
   - **Exemplo-base:** Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção.
10. Compare Photon ligado/desligado onde disponível.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
11. Defina propriedades e retenção de tabela com justificativa.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
12. Execute `VACUUM` seguro e prove que política foi respeitada.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
13. Monitore streaming query, backlog e throughput.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
14. Configure watermark e teste evento atrasado.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
15. Faça stream-stream join limitado por tempo.
   - **Exemplo-base:** Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece.
16. Recupere streaming após falha mantendo checkpoint.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
17. Planeje mudança incompatível de estado/checkpoint.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
18. Implemente backfill separado do fluxo corrente.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
19. Implemente CDC com múltiplas mudanças da mesma chave.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
20. Ordene eventos por sequência confiável.
   - **Exemplo-base:** Ordene três livros por autor e depois título usando uma tupla como chave.
21. Use Change Data Feed em laboratório.
   - **Exemplo-base:** Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias.
22. Construa consumidor incremental de CDF.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
23. Crie materialização Gold incremental.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
24. Compare pipeline declarativa disponível e Job imperativo.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
25. Defina isolamento por catálogo e ambiente.
   - **Exemplo-base:** Em duas sessões, deixe uma atualização sem commit e observe a segunda aguardar.
26. Crie service principal/identidade gerenciada conceitualmente ou em sandbox.
   - **Exemplo-base:** Em um repositório descartável, configure um usuário fictício e confirme com `git config --list`.
27. Aplique grants mínimos e teste negações.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
28. Use external location/storage credential conforme autorização.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
29. Implemente view dinâmica para filtro por usuário/grupo.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
30. Mascare coluna sensível por política/view.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
31. Audite acessos com system tables/logs disponíveis.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
32. Versione notebook, código, configuração e definição de Job.
   - **Exemplo-base:** Crie Job `gerar → validar` usando somente três registros.
33. Configure lint/test/build em CI.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
34. Faça deploy automatizado em ambiente de teste.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
35. Promova artefato imutável para outro ambiente.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
36. Teste rollback de código e compatibilidade de dados.
   - **Exemplo-base:** Teste `somar(2,3)==5` e um caso de erro antes da função maior.
37. Crie SLI/SLO de freshness, sucesso e qualidade.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
38. Crie alerta com runbook e responsável.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
39. Faça game day de falha de origem, schema e permissão.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
40. Projeto: pipeline produtivo seguro, otimizado, implantável e recuperável.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.

## Dados — 40 exercícios

1. Desenhe domínios, fontes, consumidores, SLA e classificação.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
2. Defina catálogo/schema para Bronze, Silver e Gold.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
3. Crie landing zone e convenção de caminhos.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
4. Preserve raw imutável com metadados de ingestão.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
5. Ingerir SQL Server full load inicial.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
6. Ingerir SQL Server incremental por watermark.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
7. Ingerir SQL Server por CDC/Change Tracking quando disponível.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
8. Reconciliar snapshot inicial e incremental.
   - **Exemplo-base:** Após processar até 10:00, leia eventos posteriores com pequena sobreposição.
9. Tratar registros atrasados e fora de ordem.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
10. Capturar deletes físicos/lógicos.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
11. Criar Bronze Delta idempotente.
   - **Exemplo-base:** Envie a chave `A1` duas vezes e confirme uma única versão no destino.
12. Criar Silver com contrato, tipos e deduplicação.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
13. Criar quarentena reprocessável.
   - **Exemplo-base:** Execute três esperas fictícias com limite de duas tarefas simultâneas.
14. Implementar chaves e regras de integridade.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
15. Criar dimensões conformadas.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
16. Implementar SCD1.
   - **Exemplo-base:** Cliente 1 muda de A para B; substitua A por B sem histórico.
17. Implementar SCD2.
   - **Exemplo-base:** Encerre a versão A do cliente e crie B marcada como atual.
18. Tratar dimensão atrasada.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
19. Criar fato no grão documentado.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
20. Criar Gold para BI sem duplicar regra.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
21. Publicar produto com owner, SLA e descrição.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
22. Registrar lineage e dependências.
   - **Exemplo-base:** Crie `saida_exemplo` de `entrada_exemplo` e confira a dependência no lineage.
23. Medir volume, completude, unicidade e validade.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
24. Medir freshness ponta a ponta.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
25. Detectar anomalia de volume/esquema.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
26. Criar alertas com contexto acionável.
   - **Exemplo-base:** Para volume esperado 10, gere alerta fictício quando chegarem menos de 5.
27. Realizar backfill de período histórico.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.
28. Reprocessar lote falho sem duplicação.
   - **Exemplo-base:** Transforme `["a","b","a"]` em `["a","b"]`, preservando ordem.
29. Recuperar de checkpoint perdido com procedimento seguro.
   - **Exemplo-base:** Grave `pagina_processada=2`, simule falha e reinicie na página 3.
30. Testar disaster recovery conceitual de metadados/dados/código.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
31. Otimizar layout baseado em consultas reais.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
32. Controlar custo por workload e ambiente.
   - **Exemplo-base:** Registre duração e tempo ocioso de uma leitura mínima no compute autorizado.
33. Aplicar retenção e descarte conforme requisito.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
34. Proteger PII com acesso mínimo e mascaramento.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
35. Criar testes de contrato para produtor/consumidor.
   - **Exemplo-base:** Aceite `{id:1,nome:"Ana"}` e rejeite `{id:"x"}` indicando campo e tipo.
36. Criar testes de reconciliação SQL Server versus Delta.
   - **Exemplo-base:** Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino.
37. Criar dashboard operacional e de qualidade.
   - **Exemplo-base:** Em três linhas com um ID nulo, a completude do ID é `2/3`.
38. Documentar runbook, ownership e escalação.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.
39. Demonstrar CI/CD e promoção entre ambientes.
   - **Exemplo-base:** Execute lint e um teste pequeno antes de simular promoção para teste.
40. Projeto: produto de dados SQL Server → lakehouse governado → BI.
   - **Exemplo-base:** Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.

## Critério de saída

O aluno entrega no Azure Databricks um produto incremental e idempotente, orquestrado por Jobs, governado no Unity Catalog, com Delta, testes, qualidade, lineage, alertas, CI/CD e explicação de custo/performance.
