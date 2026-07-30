# Formação de Data Engineer Júnior

Roadmap prático para levar uma pessoa com pouca experiência até o nível de engenheiro de dados júnior. O foco é aprender construindo, explicar decisões e publicar evidências no GitHub.

## Resultado esperado

Ao concluir, o aluno deverá conseguir:

- usar Git e GitHub no fluxo diário de uma equipe;
- programar e testar aplicações de dados em Python;
- modelar, consultar e transformar dados com T-SQL no SQL Server;
- processar dados em lote e streaming com PySpark;
- construir um lakehouse no Azure Databricks com camadas Bronze, Silver e Gold;
- criar pipelines idempotentes, observáveis, testáveis e documentados;
- explicar ingestão, armazenamento, transformação, qualidade, orquestração, segurança e consumo.

## Estrutura

| Fase | Trilha | Exercícios | Entrega principal |
|---|---|---:|---|
| I | [Git e GitHub](trilhas/01-git-github.md) | 15 | Fluxo completo com issue, branch, PR e revisão |
| I | [Python](trilhas/02-python.md) | 160 | Pipeline local testado e empacotado |
| I | [SQL Server / T-SQL](trilhas/03-sql-server.md) | 160 | Data warehouse e carga incremental |
| II | [Apache Spark / PySpark](trilhas/04-spark.md) | 160 | Pipeline distribuído batch e streaming |
| II | [Azure Databricks](trilhas/05-databricks.md) | 160 | Lakehouse Bronze–Silver–Gold operacional |
| Final | [Projeto integrador](projetos/projeto-final.md) | — | Fonte → lakehouse → modelo analítico |

Total: **655 exercícios**, além dos projetos integradores.

## Como estudar

Carga sugerida: 12 a 15 horas por semana durante 8 a 10 meses. O prazo é uma referência; domínio vale mais que velocidade.

Nos níveis Básicos, o aluno deve usar o [roteiro guiado](docs/roteiro-nivel-basico.md). Ele fornece contexto, preparação, passos, validação, pistas e um modelo de entrega para cada faixa de exercícios. A ajuda diminui nos níveis seguintes para desenvolver autonomia de forma gradual.

Em todas as trilhas, cada exercício contém um **Exemplo-base**. Ele usa outro domínio ou um conjunto mínimo de dados para demonstrar o conceito sem resolver o desafio. O aluno deve executar e compreender o exemplo, mas adaptar o raciocínio em vez de copiá-lo como solução.

Para cada bloco:

1. Estude a teoria indicada por 20–40 minutos.
2. Reproduza um exemplo sem copiar e colar.
3. Resolva o exercício sem IA por pelo menos 30 minutos.
4. Se usar ajuda, registre no `README.md` o erro, a pista e o aprendizado.
5. Escreva ou automatize testes.
6. Faça commit pequeno, abra pull request e explique suas decisões.
7. Só avance quando atingir o critério de saída.

Distribuição recomendada: 20% teoria, 65% prática, 15% revisão e explicação.

## Ritmo semanal

- Segunda: teoria curta, exemplo e planejamento.
- Terça e quarta: exercícios.
- Quinta: exercício de integração e testes.
- Sexta: refatoração, documentação e pull request.
- Revisão do mentor: uma sessão de 45 minutos, pedindo que o aluno execute e explique o código.

Não avaliar por quantidade de comandos memorizados. Avaliar se ele consegue decompor o problema, consultar documentação, testar hipóteses, interpretar erros e justificar escolhas.

## Regras de entrega no GitHub

O aluno deve criar um repositório chamado `formacao-data-engineer` com esta estrutura:

```text
formacao-data-engineer/
├── README.md
├── docs/
│   ├── diario-de-aprendizado.md
│   └── arquitetura/
├── fase-1/
│   ├── git/
│   ├── python/
│   └── sql-server/
├── fase-2/
│   ├── spark/
│   └── databricks/
├── projetos/
├── data/
│   ├── sample/
│   └── README.md
├── tests/
├── .gitignore
└── requirements.txt
```

Cada exercício deve conter:

- enunciado e critérios de aceite;
- um exemplo-base pequeno e análogo;
- código executável;
- dados pequenos ou instrução para obtê-los;
- testes ou consultas de validação;
- `README.md` com execução, decisões e aprendizados;
- nenhuma senha, token, dado pessoal ou arquivo grande versionado.

Fluxo obrigatório: issue → branch `exercicio/<trilha>-<numero>` → commits → pull request → revisão → merge. Uma entrega por PR ou por pequeno grupo de exercícios relacionados.

## Critério de conclusão de um nível

Pontuação mínima: 80/100.

| Dimensão | Pontos |
|---|---:|
| Correção e critérios de aceite | 35 |
| Legibilidade e organização | 15 |
| Testes e validação de dados | 20 |
| Git, commits e PR | 10 |
| Documentação e explicação oral | 10 |
| Tratamento de erros, segurança e reexecução | 10 |

Além da nota, o aluno precisa corrigir todos os problemas críticos. Para avançar, deve resolver sem ajuda dois exercícios sorteados do nível e explicar um terceiro.

## Ambiente sugerido

- Git, GitHub e VS Code;
- Python 3.11+ com ambiente virtual, `pytest`, `ruff` e `mypy` gradualmente;
- SQL Server Developer ou Express em Docker e SQL Server Management Studio/Azure Data Studio;
- PySpark local; alinhar a versão do Python à versão do Spark utilizada;
- Azure Databricks quando a Fase II começar. Manter exercícios Spark executáveis localmente sempre que possível para controlar custo.

## Datasets

Use inicialmente dados sintéticos pequenos. Depois, trabalhe com fontes públicas e registre origem/licença. Domínios sugeridos: e-commerce, logística, mobilidade, clima, finanças fictícias e IoT. Nunca publicar credenciais ou dados corporativos.

## Projetos de passagem

- Python: consumir arquivos e API, validar, transformar e gerar uma saída particionada com testes.
- SQL: criar modelo dimensional, carga incremental, histórico e consultas de negócio.
- Spark: reimplementar o pipeline Python para volume maior, analisar plano e otimizar.
- Databricks: colocar o fluxo em Jobs, Delta Lake e Unity Catalog, com qualidade e observabilidade.

O [projeto final](projetos/projeto-final.md) conecta SQL Server a uma arquitetura lakehouse e demonstra o processo completo de engenharia de dados.

## Fontes oficiais

- [GitHub Docs — primeiros passos com Git](https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git)
- [Tutorial oficial do Python](https://docs.python.org/3/tutorial/)
- [Microsoft Learn — consultar e modificar dados com T-SQL](https://learn.microsoft.com/en-us/training/paths/get-started-querying-with-transact-sql/)
- [Documentação oficial do PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
- [Microsoft Learn — introdução ao Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/introduction/)
- [Microsoft Learn — arquitetura medalhão](https://learn.microsoft.com/en-us/azure/databricks/lakehouse/medallion)
