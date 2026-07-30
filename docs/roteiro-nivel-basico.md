# Roteiro guiado para os níveis básicos

Este documento acompanha os exercícios básicos das cinco trilhas. O aluno não precisa adivinhar como começar: deve seguir o roteiro indicado para a faixa do exercício e usar o enunciado como objetivo final.

## Regra para todos os exercícios

Antes de programar:

1. Crie uma issue copiando o enunciado.
2. Acrescente à issue uma seção “O que entra?” e outra “O que deve sair?”.
3. Crie a branch indicada no arquivo da trilha.
4. Crie uma pasta própria para o exercício.
5. Escreva no `README.md` um exemplo pequeno feito à mão.

Durante:

1. Faça primeiro o menor caso que funciona.
2. Teste um caso normal.
3. Teste um caso de limite, como lista vazia, zero ou data na virada do mês.
4. Teste uma entrada inválida.
5. Leia a mensagem de erro inteira antes de pesquisar.
6. Faça commits pequenos; não espere terminar tudo.

Para concluir:

1. Execute novamente em ambiente limpo.
2. Compare o resultado com o exemplo calculado à mão.
3. Remova prints temporários, senhas e arquivos gerados.
4. Documente como executar e o que aprendeu.
5. Abra PR usando o checklist abaixo.

```markdown
## O que foi feito

## Como executar

## Como validei
- [ ] caso normal
- [ ] caso de limite
- [ ] entrada inválida
- [ ] reexecução

## Dificuldades e aprendizados
```

Se ficar bloqueado por 30 minutos, registre:

- o resultado esperado;
- o resultado obtido;
- a mensagem de erro completa;
- duas tentativas realizadas;
- a menor dúvida possível.

Só então peça ajuda. Isso ensina a formular um problema técnico sem deixar o aluno abandonado.

---

# Git e GitHub — roteiro dos 15 exercícios

## Preparação

Instale Git e VS Code, crie uma conta GitHub com autenticação em dois fatores e configure nome/e-mail. Crie a pasta `fase-1/git`. Nunca use um repositório corporativo para os experimentos.

Para cada exercício:

1. Leia o enunciado em [Git e GitHub](../trilhas/01-git-github.md).
2. Antes do comando, execute `git status`.
3. Execute um comando por vez e novamente `git status`.
4. Registre no `README.md` o estado anterior e posterior.
5. Use arquivos fictícios; nunca teste recuperação com trabalho importante.

## Exercícios 1–5: trabalhando localmente

**Contexto:** você começou um pequeno projeto e precisa guardar seu histórico com segurança.

1. Crie `fase-1/git/laboratorio-local`.
2. Faça a configuração pedida pelo exercício.
3. Crie ou altere apenas um arquivo por etapa.
4. Observe working tree, staging area e repositório.
5. Desenhe no README o caminho `arquivo → git add → git commit`.
6. Termine com `git log --oneline`.

**Validação:** outra pessoa deve entender, pelo histórico, o que mudou em cada commit.

## Exercícios 6–10: colaboração

**Contexto:** o projeto passa a ter uma cópia no GitHub e duas pessoas trabalhando.

1. Crie um repositório remoto de laboratório.
2. Use duas pastas locais para simular dois desenvolvedores.
3. Crie uma issue antes da alteração.
4. Trabalhe em branch, faça push e abra PR.
5. No conflito, leia os marcadores `<<<<<<<`, `=======` e `>>>>>>>`.
6. Execute/inspecione o resultado antes do merge.

**Validação:** os dois clones terminam sincronizados e o PR explica a mudança.

## Exercícios 11–15: recuperação e auditoria

**Contexto:** uma equipe precisa corrigir enganos e descobrir a origem de mudanças.

1. Produza o erro proposital em um arquivo sem valor.
2. Confirme se a mudança está apenas local, commitada ou publicada.
3. Escolha o comando de recuperação correspondente.
4. Confira conteúdo e histórico após recuperar.
5. Documente por que `revert` é seguro para histórico publicado.
6. Finalize com tag/release quando solicitado.

**Validação:** nenhum commit desaparece sem explicação e nenhum arquivo importante é perdido.

---

# Python básico — roteiro dos 40 exercícios

## Preparação

Crie e ative um ambiente virtual. Cada pasta terá `README.md`, código em `main.py` e, a partir do exercício 10, testes simples em `test_main.py`.

```text
fase-1/python/basico/exercicio-01/
├── README.md
├── main.py
└── test_main.py
```

Execute com `python main.py`. Quando houver funções, importe-as no teste e execute `pytest`.

## Exercícios 1–10: decisões e repetições

**Contexto:** você está criando pequenos utilitários para a equipe administrativa de uma loja.

1. Copie três exemplos de entrada e saída para o README.
2. Declare entradas com nomes claros e converta seus tipos.
3. Calcule o resultado em etapas; não coloque tudo em um único `print`.
4. Use `if/elif/else`, `for`, `while` ou `match` conforme o enunciado.
5. Separe o cálculo da interação com o usuário em uma função.
6. Teste valor normal, zero/limite e texto inválido.
7. Mostre mensagem compreensível em vez de traceback para erro esperado.

**Pronto quando:** os três exemplos funcionam e a função principal pode ser testada sem digitação manual.

**Pistas:** `input()` sempre retorna texto; converta com `int()`/`float()` dentro de tratamento de erro. Use nomes como `salario_bruto`, não `x`.

## Exercícios 11–20: textos e coleções

**Contexto:** chegaram listas de nomes, frases e códigos com inconsistências.

1. Crie uma entrada pequena contendo repetição, espaços, caixa diferente e valor vazio.
2. Percorra ou transforme a coleção sem modificar a entrada durante a iteração.
3. Escolha a estrutura: lista mantém ordem; conjunto favorece unicidade; dicionário associa chave e valor.
4. Normalize antes de comparar.
5. Calcule manualmente o resultado de pelo menos um exemplo.
6. Teste lista vazia e valores repetidos.

**Pronto quando:** a ordem e a regra de duplicidade estão explicitamente documentadas.

**Pistas:** comece com um laço claro; só depois avalie comprehension. Para frequência, use um dicionário e incremente a contagem.

## Exercícios 21–30: registros e funções

**Contexto:** produtos e vendas precisam ser representados e processados sem duplicar lógica.

1. Monte três registros pequenos como dicionários.
2. Liste os campos obrigatórios e seus tipos no README.
3. Crie uma função para cada regra: buscar, atualizar, calcular ou ordenar.
4. Não use variável global dentro das funções.
5. Faça a função retornar o resultado; deixe `print` para a camada de apresentação.
6. Adicione docstring com propósito, parâmetros e retorno.
7. Teste produto inexistente, quantidade zero e valor negativo.

**Pronto quando:** mudar a interface de terminal não exige reescrever as regras.

## Exercícios 31–40: arquivos e miniaplicação

**Contexto:** a loja envia arquivos TXT, CSV e JSON que precisam virar um relatório diário.

1. Coloque dados pequenos em `data/input` e saída em `data/output`.
2. Use `pathlib`; não codifique caminho absoluto da sua máquina.
3. Abra arquivos com encoding explícito.
4. Leia, valide, transforme e grave em funções separadas.
5. Crie a pasta de saída se necessário.
6. Trate arquivo ausente e conteúdo inválido.
7. Reexecute e verifique se o comportamento é previsível.
8. No exercício 40, conecte as funções anteriores em uma única CLI.

**Pronto quando:** um colega clona o repositório, executa o comando do README e obtém o mesmo relatório.

---

# SQL Server básico — roteiro dos 40 exercícios

## Preparação

Use somente um banco de laboratório. Crie um arquivo por exercício:

```text
fase-1/sql-server/basico/exercicio-01/
├── README.md
├── 01_setup.sql
├── 02_solution.sql
└── 03_validation.sql
```

Todo script destrutivo deve conferir o banco atual. Nunca pratique `DROP`, `DELETE` ou `TRUNCATE` em banco compartilhado.

## Exercícios 1–10: criando e consultando tabelas

**Contexto:** você vai montar o banco transacional de uma loja fictícia.

1. Desenhe primeiro as tabelas e relacionamentos.
2. Crie o banco/schemas/tabelas com nomes claros.
3. Insira entre 5 e 15 linhas, incluindo casos de limite.
4. Execute `SELECT *` apenas para explorar; na solução liste colunas.
5. Acrescente filtros/expressões um por vez.
6. Antes de `UPDATE` ou `DELETE`, execute o mesmo `WHERE` em um `SELECT`.
7. Rode o script duas vezes ou documente exatamente como reiniciar.

**Pronto quando:** restrições rejeitam dados ruins e a consulta retorna o resultado calculado manualmente.

## Exercícios 11–20: funções, agregações e joins

**Contexto:** a área comercial quer relatórios de vendas e clientes.

1. Escreva a pergunta de negócio em português.
2. Identifique a tabela que define o grão do resultado.
3. Adicione uma tabela por vez ao join.
4. Conte linhas antes e depois de cada join.
5. Só então adicione agregações.
6. Verifique nulos e clientes sem pedidos.
7. Ordene deterministicamente para facilitar a validação.

**Pronto quando:** não há multiplicação acidental de valores e o README explica o grão.

## Exercícios 21–30: conjuntos, subqueries e alterações

**Contexto:** é necessário comparar listas e manter os dados operacionais.

1. Crie dois conjuntos pequenos com itens comuns, exclusivos e nulos.
2. Prediga o resultado de `UNION`, `EXCEPT`, `INTERSECT`, `EXISTS` ou `IN`.
3. Execute e compare com a previsão.
4. Para alterações, abra transação explícita.
5. Consulte linhas afetadas antes e depois.
6. Faça rollback na primeira execução.
7. Faça commit apenas depois de validar.

**Pronto quando:** o aluno explica por que o resultado muda com duplicados e nulos.

## Exercícios 31–40: objetos auxiliares e projeto OLTP

**Contexto:** consultas maiores precisam ser organizadas e o banco precisa ser reproduzível.

1. Use tabela temporária apenas quando houver uma etapa intermediária clara.
2. Crie views com nomes de negócio e sem `SELECT *`.
3. Consulte metadados para verificar o que foi criado.
4. Separe `setup`, solução e validação.
5. No projeto final do nível, recrie o banco do zero.
6. Responda pelo menos cinco perguntas de negócio.
7. Capture uma imagem ou saída textual das validações, sem publicar dados sensíveis.

**Pronto quando:** o mentor executa os scripts em ordem em uma instância vazia sem correção manual.

---

# Spark básico — roteiro dos 40 exercícios

## Preparação

Complete primeiro Python básico. Use datasets com 10–100 linhas para entender o resultado; desempenho será estudado depois. Crie funções que recebem e retornam DataFrames.

```text
fase-2/spark/basico/exercicio-01/
├── README.md
├── data/input/
├── src/job.py
└── tests/test_job.py
```

## Exercícios 1–10: sessão, leitura e colunas

**Contexto:** arquivos da loja cresceram e o pipeline será migrado para processamento distribuído.

1. Inicie uma `SparkSession` local.
2. Crie primeiro um DataFrame minúsculo em memória.
3. Defina schema explicitamente.
4. Execute `printSchema()` e `show()`.
5. Aplique uma única transformação por etapa.
6. Não use `collect()` para implementar a regra.
7. Compare resultado com uma versão calculada à mão.

**Pronto quando:** tipos estão corretos e cada coluna criada tem regra explicada.

## Exercícios 11–20: limpeza e agregação

**Contexto:** os dados possuem datas, textos, nulos, duplicados e precisam gerar indicadores.

1. Faça profiling simples antes de limpar.
2. Defina regra por coluna; não preencha todos os nulos igualmente.
3. Preserve ou conte rejeitados.
4. Deduplicate usando chave e critério documentados.
5. Agrupe apenas depois de confirmar o grão.
6. Valide contagem, soma e número de chaves antes/depois.

**Pronto quando:** a transformação não esconde perda de registros.

## Exercícios 21–30: joins e estruturas complexas

**Contexto:** pedidos, clientes e eventos JSON precisam ser combinados.

1. Crie datasets pequenos com chave encontrada, ausente e duplicada.
2. Conte chaves repetidas antes do join.
3. Escolha `inner`, `left`, `semi` ou `anti` conforme a pergunta.
4. Use aliases para eliminar ambiguidade.
5. Compare contagem antes/depois.
6. Para arrays/structs, trabalhe primeiro com um único registro.
7. Refaça uma consulta em DataFrame API e SQL.

**Pronto quando:** o aluno consegue prever quais linhas entram e saem do join.

## Exercícios 31–40: execução, arquivos e projeto

**Contexto:** a pipeline precisa gravar dados reutilizáveis e ser executada por outra pessoa.

1. Observe que transformações são preguiçosas até uma ação.
2. Execute `explain()` e localize leitura, filtro, agregação e troca de dados.
3. Grave em pasta temporária do exercício.
4. Leia a saída novamente e valide schema/contagem/soma.
5. Experimente `repartition`/`coalesce` apenas no laboratório.
6. Limpe cache quando não for mais necessário.
7. No projeto 40, una leitura, limpeza, agregação, escrita e testes.

**Pronto quando:** `spark-submit` ou comando documentado executa tudo do zero.

---

# Databricks básico — roteiro dos 40 exercícios

## Preparação e segurança

Complete Spark básico antes. O mentor deve fornecer workspace, política de compute, catálogo/schema de laboratório e orçamento. O aluno nunca cria recurso fora desse escopo.

Antes de cada sessão:

1. Confirme catálogo, schema, compute e ambiente.
2. Verifique se há compute ocioso.
3. Use apenas dados fictícios.
4. Não cole token, senha ou connection string em notebook.
5. Ao terminar, desligue o recurso quando a política exigir.

## Exercícios 1–10: conhecendo a plataforma

**Contexto:** você entrou no workspace da empresa e precisa trabalhar sem afetar outros ambientes.

1. Localize workspace, compute, SQL warehouse, catálogo e storage.
2. Desenhe onde código, processamento e dados residem.
3. Crie notebook de laboratório em pasta/repositório próprio.
4. Execute células do topo ao fim.
5. Reinicie a sessão e repita para revelar dependências ocultas.
6. Trabalhe em branch e publique apenas código/configuração segura.

**Pronto quando:** o notebook é reprodutível e o aluno explica a finalidade de cada componente.

## Exercícios 11–20: arquivos e Delta Lake

**Contexto:** arquivos brutos precisam virar tabelas confiáveis com histórico.

1. Coloque arquivo pequeno no Volume/local autorizado.
2. Leia com schema explícito e registre metadados da origem.
3. Grave tabela Delta no catálogo/schema de laboratório.
4. Faça uma mudança por vez.
5. Consulte `DESCRIBE DETAIL` e histórico após cada mudança.
6. Teste schema incompatível em tabela descartável.
7. Use time travel para comparar versões.

**Pronto quando:** o aluno demonstra a versão anterior sem apagar o histórico.

## Exercícios 21–30: idempotência, parâmetros e SQL Server

**Contexto:** a pipeline será reexecutada e deverá buscar dados de um SQL Server sem expor credenciais.

1. Crie dados com chave de negócio e uma atualização.
2. Execute `MERGE`.
3. Execute novamente com a mesma entrada.
4. Compare contagem e conteúdo; nada deve duplicar.
5. Parametrize data/lote em vez de editar notebook.
6. Obtenha credencial pelo mecanismo seguro fornecido.
7. Teste JDBC primeiro com consulta pequena.
8. Nunca imprima objeto/configuração que contenha segredo.

**Pronto quando:** duas execuções iguais produzem o mesmo estado e o segredo não aparece no Git/log.

## Exercícios 31–40: primeira arquitetura medalhão

**Contexto:** a loja quer transformar fontes brutas em um produto analítico.

1. Bronze: preserve o recebido e adicione origem, horário e `run_id`.
2. Silver: converta tipos, normalize, deduplicate e separe rejeitados.
3. Gold: responda uma pergunta de negócio com grão documentado.
4. Registre contagens de entrada, saída e quarentena.
5. Compare totais entre camadas.
6. Reexecute o lote e valide idempotência.
7. Execute tudo do início ao fim em sessão limpa.
8. Documente custo, permissões, entradas, saídas e recuperação.

**Pronto quando:** outra pessoa encontra as tabelas, entende o lineage e reproduz a execução pelo README.

---

# Modelo de README para cada exercício básico

```markdown
# Exercício XX — título

## Contexto
Por que este problema existe?

## Entrada
Campos, tipos e três exemplos pequenos.

## Saída esperada
Resultado calculado manualmente.

## Passos
1. ...
2. ...
3. ...

## Como executar
Comando exato.

## Como validei
Caso normal, limite, inválido e reexecução.

## Decisões
Por que escolhi esta abordagem?

## Dificuldades e aprendizados
Erro, tentativas e solução.
```

