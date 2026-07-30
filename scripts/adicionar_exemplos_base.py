#!/usr/bin/env python3
"""Insere um exemplo análogo em cada exercício das trilhas (execução idempotente)."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"^(\d+)\.\s+(.+)$")

# A primeira palavra encontrada escolhe um exemplo mínimo. O domínio é
# propositalmente diferente do enunciado para não entregar a solução.
RULES = [
    (("git config", "identidade"), "Em um repositório descartável, configure um usuário fictício e confirme com `git config --list`."),
    (("repositório", "inicialize"), "Crie `lista-compras`, adicione um README de duas linhas e faça um commit chamado `cria lista`."),
    (("histórico", "log"), "Altere um cardápio em três commits e visualize-os com `git log --oneline`."),
    (("diff", "diferen"), "Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`."),
    (("branch",), "Crie `exemplo/adiciona-cha`, altere um cardápio e volte à branch principal para comparar."),
    (("conflito",), "Em duas branches, mude o preço do mesmo café; faça merge e escolha o valor final."),
    (("pull request", "github flow", "issue"), "Abra uma issue `adicionar sobremesa`, implemente em branch e descreva no PR como validar."),
    (("stash",), "Edite um cardápio, guarde com `stash`, corrija outro arquivo e recupere a edição."),
    (("tag", "release"), "Marque um repositório de exemplo como `v0.1.0` e confira o commit apontado."),
    (("temperatura",), "Converta apenas `0 °C` para Fahrenheit; usando `c * 9/5 + 32`, espere `32`."),
    (("salário", "imposto"), "Aplique um único desconto de 10% sobre `1000`; espere `900` antes de criar faixas."),
    (("par", "primo", "positivo"), "Receba `8` e informe somente se é par; depois teste `7` e `0`."),
    (("segundos",), "Converta `125` segundos em `2 minutos e 5 segundos` usando divisão e resto."),
    (("calculadora",), "Implemente primeiro `somar(2, 3) → 5`; depois acrescente outra operação."),
    (("tabuada",), "Gere apenas `3×1`, `3×2`, `3×3`, esperando `3, 6, 9`."),
    (("sentinela",), "Leia `4`, `6`, `0`, usando zero para parar; a soma deve ser `10`."),
    (("senha",), "Teste só o mínimo de oito caracteres: `abc` falha e `abcdefgh` passa."),
    (("vogais",), "Conte as vogais de `Data`; o resultado é `2`, ignorando maiúsculas."),
    (("normalize", "normaliz"), "Transforme `  ana   silva ` em `Ana Silva`."),
    (("palíndromo",), "Remova espaços de `Ame a ema`, use minúsculas e compare com o texto invertido."),
    (("média", "mediana", "moda", "estatíst"), "Com `[2,4,6]`, calcule média `4`, mínimo `2` e máximo `6`."),
    (("duplic",), "Transforme `[\"a\",\"b\",\"a\"]` em `[\"a\",\"b\"]`, preservando ordem."),
    (("segundo maior",), "Em `[5,2,5,3]`, o segundo maior valor distinto é `3`."),
    (("rotacione",), "Rotacione `[1,2,3]` uma posição à direita para obter `[3,1,2]`."),
    (("interseção", "união"), "Compare `{1,2}` e `{2,3}`: interseção `{2}`, união `{1,2,3}`."),
    (("frequência", "counter"), "Em `azul azul verde`, produza `{\"azul\":2,\"verde\":1}`."),
    (("estoque",), "Use lápis: 3×R$2 e caderno: 2×R$10; o total esperado é R$26."),
    (("ordene", "ordenação"), "Ordene três livros por autor e depois título usando uma tupla como chave."),
    (("comprehension", "map", "filter"), "De `[1,2,3,4]`, produza o quadrado dos pares: `[4,16]`."),
    (("csv",), "Leia `nome,idade\\nAna,20` e produza `Ana tem 20 anos`."),
    (("json",), "Leia `[{\"item\":\"livro\",\"qtd\":2}]` e obtenha quantidade total `2`."),
    (("arquivo", "txt", "pathlib"), "Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras."),
    (("exceç", "erro", "inválid"), "Converta `\"abc\"` para inteiro, capture `ValueError` e retorne mensagem curta."),
    (("datetime", "data"), "Calcule a diferença entre `2026-01-01` e `2026-01-03`: dois dias."),
    (("classe", "dataclass", "modele"), "Modele `Livro(titulo=\"Duna\", paginas=500)` e rejeite páginas negativas."),
    (("iterador", "generator", "yield"), "Produza 1, 2 e 3 com `yield` e consuma um valor por vez."),
    (("context manager",), "Use `with cronometro():` em um bloco curto e registre início e fim."),
    (("type", "tipagem", "protocol"), "Anote `def dobro(valor: int) -> int` e verifique inteiro e texto."),
    (("teste", "pytest", "fixture", "mock"), "Teste `somar(2,3)==5` e um caso de erro antes da função maior."),
    (("logging", "log"), "Registre `etapa=inicio run_id=abc` e `etapa=fim linhas=3` sem `print`."),
    (("api", "http", "download"), "Transforme uma resposta simulada `{\"pagina\":1,\"itens\":[1,2]}` sem acessar a rede."),
    (("retry", "backoff"), "Simule uma função que falha uma vez e funciona na segunda; valide duas tentativas."),
    (("regex",), "Extraia `INFO` e `42` de `INFO pedido=42`."),
    (("fuso", "utc"), "Converta `2026-01-01 10:00 -03:00` para `13:00 UTC`."),
    (("decorator",), "Aplique `@registrar` a `dobro(3)` e preserve nome, entrada e saída."),
    (("thread", "process", "async", "concorr"), "Execute três esperas fictícias com limite de duas tarefas simultâneas."),
    (("memória", "perfil", "benchmark"), "Compare somar `range(1000)` usando lista e generator antes do volume real."),
    (("checkpoint", "retom"), "Grave `pagina_processada=2`, simule falha e reinicie na página 3."),
    (("idempot"), "Envie a chave `A1` duas vezes e confirme uma única versão no destino."),
    (("schema", "contrato"), "Aceite `{id:1,nome:\"Ana\"}` e rejeite `{id:\"x\"}` indicando campo e tipo."),
    (("join",), "Una clientes `[(1,Ana),(2,Bia)]` a pedidos `[(1,10)]`; no left join Bia permanece."),
    (("row_number", "rank", "janela"), "Para notas 7 e 9 de Ana, ordene descrescente e marque 9 como posição 1."),
    (("acumulado", "móvel", "lag", "lead"), "Com vendas `[10,20,5]`, produza acumulado `[10,30,35]`."),
    (("cte", "subquer"), "Crie uma CTE com 1, 2 e 3 e selecione apenas valores maiores que 1."),
    (("transa", "rollback", "commit"), "Debite 10 de uma conta em transação; valide e execute rollback na primeira vez."),
    (("índice", "plano", "tuning"), "Consulte três livros por código, veja o plano, crie índice de laboratório e compare."),
    (("bloqueio", "deadlock", "isolamento"), "Em duas sessões, deixe uma atualização sem commit e observe a segunda aguardar."),
    (("scd tipo 1", "scd1"), "Cliente 1 muda de A para B; substitua A por B sem histórico."),
    (("scd tipo 2", "scd2"), "Encerre a versão A do cliente e crie B marcada como atual."),
    (("watermark", "incremental"), "Após processar até 10:00, leia eventos posteriores com pequena sobreposição."),
    (("reconcil",), "Origem tem 3 linhas e soma 60; confira as mesmas métricas no destino."),
    (("quarentena", "rejeitad"), "Separe `{id:1}` como válido e `{id:null}` com motivo `id_obrigatorio`."),
    (("qualidade", "completude", "unicidade"), "Em três linhas com um ID nulo, a completude do ID é `2/3`."),
    (("dataframe", "spark"), "Crie DataFrame de dois livros `(id:int,titulo:string)` e confira schema e linhas."),
    (("parquet",), "Grave três livros em Parquet, leia só `titulo` e confirme três linhas."),
    (("repartition", "coalesce", "partiç"), "Distribua seis linhas em duas partições e confira a quantidade antes de gravar."),
    (("cache", "persist"), "Use um DataFrame pequeno duas vezes, materialize o cache e execute `unpersist()`."),
    (("explain", "lazy"), "Filtre três linhas, chame `explain()` e localize `Filter` antes da ação."),
    (("broadcast",), "Una seis vendas a uma dimensão de dois itens e confirme broadcast no plano."),
    (("skew", "salting"), "Crie dez linhas, oito com chave `A`, e conte por chave para ver o desequilíbrio."),
    (("stream",), "Processe dois lotes mínimos de eventos com checkpoint temporário."),
    (("delta", "time travel"), "Crie Delta com dois livros, atualize um título e consulte versões 0 e 1."),
    (("merge", "upsert"), "Destino `{1:A}` e fonte `{1:B,2:C}` devem produzir uma atualização e uma inserção."),
    (("bronze", "silver", "gold", "medalh"), "Bronze guarda `\" ANA \"`; Silver produz `Ana`; Gold conta um cliente."),
    (("job", "task", "schedule"), "Crie Job `gerar → validar` usando somente três registros."),
    (("secret", "credencial"), "Leia segredo pelo mecanismo do ambiente e use-o sem imprimir ou versionar."),
    (("unity", "catálogo", "permiss", "grant"), "Conceda apenas `SELECT` de uma tabela de laboratório a um grupo de teste."),
    (("custo", "compute", "cluster", "warehouse"), "Registre duração e tempo ocioso de uma leitura mínima no compute autorizado."),
    (("lineage",), "Crie `saida_exemplo` de `entrada_exemplo` e confira a dependência no lineage."),
    (("alerta", "observabilidade", "métrica"), "Para volume esperado 10, gere alerta fictício quando chegarem menos de 5."),
    (("ci/cd", "deploy", "promo"), "Execute lint e um teste pequeno antes de simular promoção para teste."),
]

FALLBACK = {
    "01": "Use um README de duas linhas em repositório descartável; observe `git status` antes e depois.",
    "02": "Resolva primeiro com três livros fictícios e escreva manualmente a saída esperada.",
    "03": "Use duas tabelas de laboratório com três linhas; preveja o resultado antes de executar.",
    "04": "Use um DataFrame de três livros com schema explícito e valide schema, contagem e conteúdo.",
    "05": "Use uma tabela Delta de três livros no schema de laboratório e compare estado antes/depois.",
}


def choose(filename: str, text: str) -> str:
    lowered = text.casefold()
    for words, example in RULES:
        if filename != "04-spark.md" and any(
            marker in example
            for marker in ("DataFrame", "partições", "broadcast no plano", "checkpoint temporário")
        ):
            continue
        if filename != "05-databricks.md" and any(
            marker in example
            for marker in ("Compute", "compute autorizado", "tabela Delta", "Crie Delta", "Unity", "Job `")
        ):
            continue
        candidates = (words,) if isinstance(words, str) else words
        if any(
            (
                re.search(rf"(?<!\w){re.escape(word.casefold())}(?!\w)", lowered)
                if len(word) <= 5
                else word.casefold() in lowered
            )
            for word in candidates
        ):
            return example
    return FALLBACK[filename[:2]]


def process(path: Path) -> int:
    # Regera os exemplos para que ajustes nas regras sejam aplicados sem
    # duplicação. Somente linhas identificadas pelo marcador são substituídas.
    lines = [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if not line.strip().startswith("- **Exemplo-base:**")
    ]
    output, added = [], 0
    for index, line in enumerate(lines):
        output.append(line)
        match = PATTERN.match(line)
        if not match:
            continue
        output.append(f"   - **Exemplo-base:** {choose(path.name, match.group(2))}")
        added += 1
    path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return added


total = 0
for track in sorted((ROOT / "trilhas").glob("*.md")):
    count = process(track)
    total += count
    print(f"{track.name}: {count}")
print(f"total: {total}")
