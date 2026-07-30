# Projeto final — Lakehouse de e-commerce

## Cenário

Uma empresa fictícia possui clientes, produtos, pedidos e itens no SQL Server. Eventos de navegação chegam como JSON e arquivos de transportadoras chegam diariamente em CSV. O negócio quer dados confiáveis de receita, conversão, prazo de entrega e recompra.

## Arquitetura esperada

```text
SQL Server + JSON + CSV
        ↓ ingestão full/incremental, auditável
Landing/Raw → Bronze Delta → Silver Delta → Gold
                    ↓ qualidade/quarentena
              Jobs + alertas + lineage
                              ↓
                   Databricks SQL/consulta BI
```

## Entregas

1. Repositório com issues, branches, PRs, tags e releases.
2. Diagrama, decisões arquiteturais, contrato e catálogo de dados.
3. Infraestrutura/recursos descritos sem segredos.
4. Gerador de dados sintéticos, incluindo falhas controladas.
5. Banco SQL Server com modelo transacional e seed.
6. Ingestão full inicial e incremental com inserts, updates e deletes.
7. Bronze que preserva origem e metadados.
8. Silver tipada, deduplicada, validada e com quarentena.
9. Gold dimensional com pelo menos uma fato e quatro dimensões.
10. SCD tipo 2 para cliente ou produto.
11. Job multi-task parametrizado, com retries e alertas coerentes.
12. Testes unitários, integração, contrato e reconciliação.
13. Métricas de volume, qualidade, freshness e duração.
14. Dashboard operacional e consultas de negócio.
15. Evidência de idempotência, recuperação e backfill.
16. Análise de plano/performance e uma otimização comprovada.
17. Segurança mínima, mascaramento de PII e política de retenção.
18. Runbook de operação e apresentação de 20 minutos.

## Casos de falha obrigatórios

- arquivo vazio, duplicado e corrompido;
- coluna nova compatível e mudança incompatível;
- evento atrasado e fora de ordem;
- falha no meio da execução;
- indisponibilidade temporária da origem;
- duplicidade de chave;
- permissão insuficiente;
- volume muito acima do normal.

O aluno deve demonstrar o comportamento antes e depois da correção.

## Critérios de aceite

- Reexecutar o mesmo lote não duplica dados.
- Contagens e valores financeiros reconciliam com a origem.
- Registros rejeitados são rastreáveis e podem ser reprocessados.
- Nenhum segredo ou dado sensível aparece no Git/log.
- Código principal não depende de execução manual de células anteriores.
- O Job é parametrizado por ambiente e data/lote.
- Um novo desenvolvedor consegue executar o projeto seguindo o README.
- O aluno explica onde há shuffle, como o incremental funciona, o grão das fatos, como recuperar falhas e quais decisões afetam custo.

## Avaliação (100 pontos)

| Área | Pontos |
|---|---:|
| Arquitetura e modelagem | 15 |
| Correção e incremental/idempotência | 20 |
| Qualidade, testes e reconciliação | 20 |
| Spark/Delta e performance | 15 |
| Orquestração, observabilidade e recuperação | 10 |
| Segurança e governança | 10 |
| Git, documentação e apresentação | 10 |

Nota mínima: 80, sem falhas críticas em segurança, perda/duplicação de dados ou reexecução.

