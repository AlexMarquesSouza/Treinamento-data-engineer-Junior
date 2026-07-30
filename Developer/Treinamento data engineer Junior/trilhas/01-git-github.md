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
2. **Primeiro repositório:** inicialize um repositório, crie `README.md`, inspecione os três estados de arquivo e faça dois commits atômicos.
3. **Histórico legível:** faça cinco alterações relacionadas e investigue o histórico com formatos resumido, gráfico, autor e intervalo de datas.
4. **Diferenças:** compare working tree, staging e último commit; explique em texto o que cada `diff` mostra.
5. **`.gitignore`:** gere arquivos de log, ambiente e segredo fictício; ignore-os, mas mantenha um `.env.example`.
6. **Repositório remoto:** crie um projeto no GitHub, configure `origin`, envie `main`, clone em outra pasta e valide o histórico.
7. **Branches:** implemente duas mudanças independentes em branches diferentes e integre-as em `main`.
8. **Conflito controlado:** produza propositalmente um conflito na mesma linha, resolva-o, teste o resultado e registre a causa.
9. **GitHub Flow:** abra uma issue, crie branch vinculada, faça commits, abra PR com checklist, revise e faça merge.
10. **Sincronização:** simule mudanças em dois clones; use `fetch`, compare branches e atualize o clone atrasado com segurança.
11. **Correção segura:** reverta um commit já publicado com `git revert`; compare com restaurar um arquivo ainda não publicado.
12. **Stash:** interrompa uma mudança incompleta, guarde-a, corrija uma tarefa urgente e recupere o trabalho.
13. **Tags e release:** marque uma versão semântica, publique a tag e crie uma release com notas e artefato fictício.
14. **Colaboração:** faça fork de um repositório de treino, mantenha um remote `upstream` e proponha uma contribuição por PR.
15. **Auditoria final:** use `log`, `show`, `blame` e busca no histórico para identificar quando, por quem e por que uma linha mudou; entregue um guia de diagnóstico.

## Critério de saída

Sem consultar um roteiro, o aluno cria um repositório, trabalha em branch, resolve um conflito, abre um PR claro e recupera uma alteração sem perder trabalho. O histórico deve ter commits pequenos e nenhuma credencial.
