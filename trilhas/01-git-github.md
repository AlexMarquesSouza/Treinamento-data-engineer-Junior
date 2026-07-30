# Git e GitHub

## Objetivo e teoria

Entender versionamento, repositório local/remoto, working tree, staging area, commit, branch, merge, conflito, pull request e colaboração.

Estude:

- [Configurar o Git](https://docs.github.com/en/get-started/git-basics/set-up-git)
- [Primeiros passos com Git](https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git)
- [Recursos de aprendizagem Git/GitHub](https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources)
- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Sintaxe básica de Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

Comandos mínimos: `git config`, `init`, `clone`, `status`, `add`, `commit`, `log`, `diff`, `branch`, `switch`, `merge`, `remote`, `fetch`, `pull`, `push`, `restore`, `revert`, `tag` e `stash`. O aluno deve entender o efeito antes de usar comandos que reescrevem histórico.

## 15 exercícios

Antes de começar, siga o [roteiro guiado de Git e GitHub](../docs/roteiro-nivel-basico.md#git-e-github--roteiro-dos-15-exercícios). Ele explica o cenário, a preparação, os passos e como validar cada faixa.

1. **Identidade e ajuda:** configure nome/e-mail, descubra versões, use `git help` e documente onde ficam as configurações local e global.
   - **Exemplo-base:** Em um repositório descartável, configure um usuário fictício e confirme com `git config --list`.
2. **Primeiro repositório:** inicialize um repositório, crie `README.md`, inspecione os três estados de arquivo e faça dois commits atômicos.
   - **Exemplo-base:** Crie `lista-compras`, adicione um README de duas linhas e faça um commit chamado `cria lista`.
3. **Histórico legível:** faça cinco alterações relacionadas e investigue o histórico com formatos resumido, gráfico, autor e intervalo de datas.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.
4. **Diferenças:** compare working tree, staging e último commit; explique em texto o que cada `diff` mostra.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
5. **`.gitignore`:** gere arquivos de log, ambiente e segredo fictício; ignore-os, mas mantenha um `.env.example`.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.
6. **Repositório remoto:** crie um projeto no GitHub, configure `origin`, envie `main`, clone em outra pasta e valide o histórico.
   - **Exemplo-base:** Crie `lista-compras`, adicione um README de duas linhas e faça um commit chamado `cria lista`.
7. **Branches:** implemente duas mudanças independentes em branches diferentes e integre-as em `main`.
   - **Exemplo-base:** Troque `azul` por `verde` em um TXT e observe o diff antes e depois de `git add`.
8. **Conflito controlado:** produza propositalmente um conflito na mesma linha, resolva-o, teste o resultado e registre a causa.
   - **Exemplo-base:** Em duas branches, mude o preço do mesmo café; faça merge e escolha o valor final.
9. **GitHub Flow:** abra uma issue, crie branch vinculada, faça commits, abra PR com checklist, revise e faça merge.
   - **Exemplo-base:** Crie `exemplo/adiciona-cha`, altere um cardápio e volte à branch principal para comparar.
10. **Sincronização:** simule mudanças em dois clones; use `fetch`, compare branches e atualize o clone atrasado com segurança.
   - **Exemplo-base:** Crie `exemplo/adiciona-cha`, altere um cardápio e volte à branch principal para comparar.
11. **Correção segura:** reverta um commit já publicado com `git revert`; compare com restaurar um arquivo ainda não publicado.
   - **Exemplo-base:** Leia um TXT com `ola mundo`; valide 1 linha e 2 palavras.
12. **Stash:** interrompa uma mudança incompleta, guarde-a, corrija uma tarefa urgente e recupere o trabalho.
   - **Exemplo-base:** Edite um cardápio, guarde com `stash`, corrija outro arquivo e recupere a edição.
13. **Tags e release:** marque uma versão semântica, publique a tag e crie uma release com notas e artefato fictício.
   - **Exemplo-base:** Marque um repositório de exemplo como `v0.1.0` e confira o commit apontado.
14. **Colaboração:** faça fork de um repositório de treino, mantenha um remote `upstream` e proponha uma contribuição por PR.
   - **Exemplo-base:** Crie `lista-compras`, adicione um README de duas linhas e faça um commit chamado `cria lista`.
15. **Auditoria final:** use `log`, `show`, `blame` e busca no histórico para identificar quando, por quem e por que uma linha mudou; entregue um guia de diagnóstico.
   - **Exemplo-base:** Altere um cardápio em três commits e visualize-os com `git log --oneline`.

## Critério de saída

Sem consultar um roteiro, o aluno cria um repositório, trabalha em branch, resolve um conflito, abre um PR claro e recupera uma alteração sem perder trabalho. O histórico deve ter commits pequenos e nenhuma credencial.
