# Como contribuir e manter esta base

Este repositório é uma base de conhecimento derivada de planilhas. A regra que sustenta a
confiabilidade dele é simples e não negociável:

> **A planilha é a fonte da verdade. O Markdown reproduz o que ela diz.**

Alterar um número, um limiar ou um procedimento diretamente no Markdown, sem alterar a planilha
correspondente, faz o conteúdo do repositório deixar de corresponder à fonte — que é exatamente o
que a rastreabilidade desta base promete evitar.

## Neste documento

- [Quais arquivos derivam de dados e quais não derivam](#quais-arquivos-derivam-de-dados-e-quais-não-derivam)
- [Padrão estrutural dos documentos](#padrão-estrutural-dos-documentos)
- [Regras de conteúdo](#regras-de-conteúdo)
- [Fluxo de alteração](#fluxo-de-alteração)
- [Onde estão as pendências abertas](#onde-estão-as-pendências-abertas)
- [Autoria](#autoria)

---

## Quais arquivos derivam de dados e quais não derivam

### Derivados das planilhas

Todo campo técnico destes documentos é transcrição literal de uma célula. Eles trazem, na primeira
linha, um comentário HTML indicando a aba de origem.

| Arquivo | Aba de origem |
| --- | --- |
| [`docs/06-fluxo-post.md`](docs/06-fluxo-post.md) | `Fluxo de Diagnóstico` |
| [`docs/07-fluxo-sistemico.md`](docs/07-fluxo-sistemico.md) | `FLUXO_LOGICO` |
| [`docs/08-diagnostico-por-camada.md`](docs/08-diagnostico-por-camada.md) | `Camadas de Diagnóstico` |
| [`docs/09-codigos-post/`](docs/09-codigos-post/00-indice-codigos.md) | `Tabela Diagnóstico POST` |
| [`docs/10-cenarios/`](docs/10-cenarios/00-indice-cenarios.md) | `TABELA_PRINCIPAL` + `INDICE_CENARIOS` |
| [`docs/11-ambiguidades.md`](docs/11-ambiguidades.md) | `Ambiguidade de Códigos` |
| [`docs/12-correlacoes.md`](docs/12-correlacoes.md) | `CORRELACOES` |
| [`docs/13-validacao-final.md`](docs/13-validacao-final.md) | `VALIDACAO_FINAL` |
| [`docs/14-ferramentas/`](docs/14-ferramentas/00-indice-ferramentas.md) | `REF_Victoria`, `REF_AIDA64`, `REF_MemTest86` |
| [`docs/18-indices-cruzados.md`](docs/18-indices-cruzados.md) | derivado das colunas de classificação |
| [`docs/19-comandos.md`](docs/19-comandos.md) | coluna `Comandos Técnicos` |

> [!IMPORTANT]
> Nestes arquivos, **não altere valores técnicos** — códigos, tensões, limiares, tempos, comandos,
> nomes de componente. Corrija a planilha e traga a correção para cá, registrando a mudança no
> [changelog](docs/references/changelog.md). Correções de link, formatação ou erro de transcrição
> podem ser feitas diretamente.

### Redigidos

Estes documentos organizam, explicam e sinalizam. Não transcrevem células, e podem ser editados
diretamente — desde que nenhuma afirmação nova entre sem fonte.

[`README.md`](README.md), este arquivo,
[`docs/00-indice.md`](docs/00-indice.md),
[`01`](docs/01-visao-geral.md), [`02`](docs/02-arquitetura.md),
[`03`](docs/03-taxonomia-camadas.md), [`04`](docs/04-requisitos-e-ferramentas.md),
[`05`](docs/05-utilizacao.md), [`15`](docs/15-limitacoes.md), [`16`](docs/16-faq.md),
[`17`](docs/17-glossario.md) e [`docs/references/`](docs/references/fontes.md).

---

## Padrão estrutural dos documentos

Todo documento de `docs/` segue a mesma estrutura, na mesma ordem. Ao criar ou alterar um
documento, mantenha-a — é ela que permite ao leitor saber onde procurar sem reaprender o formato a
cada arquivo.

| # | Elemento | Obrigatório |
| --- | --- | --- |
| 1 | Comentário HTML com a aba de origem, na primeira linha | documentos derivados |
| 2 | Trilha de navegação de volta ao README | sim |
| 3 | Título e resumo de uma linha | sim |
| 4 | **Aplica-se a** | quando faz sentido |
| 5 | **Neste documento** — sumário com link para cada seção | sim |
| 6 | Contexto, Escopo, Fora do escopo, Relação com outros documentos | sim |
| 7 | Fluxograma | quando o documento resolve uma decisão |
| 8 | Conteúdo | sim |
| 9 | **Próximos passos** | sim |
| 10 | Rodapé com fonte, confiança, autoria e versão | sim |

### Trilha de navegação

A trilha aponta para uma das seções do [README](README.md): *Comece aqui*, *Diagnostique*,
*Resolva*, *Feche o atendimento*, *Opere as ferramentas*, *Consulte a referência* ou *Manutenção e
rastreabilidade*. Se criar uma seção nova no README, confira que a âncora usada na trilha existe.

O número de `../` depende da profundidade: documentos em `docs/` usam `../README.md`; documentos em
subpasta, como `docs/10-cenarios/`, usam `../../README.md`.

### Avisos

Use os callouts do GitHub, com significado fixo.

| Callout | Quando usar |
| --- | --- |
| `> [!NOTE]` | Procedência, nível de confiança, observação de leitura |
| `> [!TIP]` | Atalho de navegação |
| `> [!IMPORTANT]` | Pré-requisito ou regra que muda o resultado |
| `> [!WARNING]` | Risco de erro de diagnóstico ou de perda de tempo |
| `> [!CAUTION]` | Risco elétrico, perda de dados ou dano a componente |

### Procedimentos

Fichas de código e de cenário agrupam os campos em fases, nesta ordem: **Identificação** →
**Pré-requisitos** → **Diagnóstico** → **Execução da correção** → **Resultado esperado** →
**Risco e impacto** → **Origem** → **Próximos passos**. Os nomes dos campos dentro de cada fase são
os da planilha e não devem ser alterados.

### Fluxogramas

- Escreva em Mermaid, dentro de bloco ```` ```mermaid ````. O GitHub renderiza nativamente.
- Use linguagem descritiva nos rótulos ("liga, mas a tela fica preta"), não jargão. O fluxograma
  precisa ser legível por quem não domina a terminologia.
- O diagrama **resume**; o conteúdo integral vem logo abaixo, sem cortes.
- Quando o diagrama condensar ou reorganizar o que a fonte declara, registre isso em um
  `> [!NOTE]` com o nível de confiança.
- Confira a renderização no GitHub depois de publicar: um bloco com cerca desbalanceada quebra o
  restante da página.

### Duplicação

Cada assunto tem um dono. A entrada por sintoma, por exemplo, vive no [README](README.md); os
demais documentos remetem a ela. Antes de acrescentar uma tabela ou explicação, verifique se ela já
existe em outro documento — se existir, use um link.

---

## Regras de conteúdo

Estas regras existem porque a base é usada para decidir se um componente vai para o lixo ou para a
bancada. Um dado inventado aqui custa uma peça boa descartada — ou uma ruim devolvida ao cliente.

1. **Não invente.** Funcionalidade, comando, código de erro, tensão, limiar, tempo, compatibilidade,
   versão — nada entra sem estar na fonte.
2. **Lacuna se declara.** Campo sem informação vira
   *"Informação não identificada na fonte analisada"*, nunca uma dedução plausível.
3. **Conflito se registra, não se resolve por conta própria.** Se duas fontes divergem, documente as
   duas e abra uma pendência em [pendencias.md](docs/references/pendencias.md). A base já carrega
   quatro divergências assim.
4. **Inferência se marca.** Conclusão derivada leva o rótulo **Inferido** no ponto de uso.
5. **Versão se preserva.** `MemTest86 v10+`, `ATX12V v2.53`, `UEFI 2.10` — copie exatamente como
   está. Não atualize por conta própria.
6. **Nome técnico não se troca por sinônimo.** `Q-Code`, `Debug LED`, `power drain`, `boot mínimo`
   têm grafia estabelecida na base.
7. **Fonte externa não preenche lacuna da fonte primária.** Se a planilha não diz, a documentação
   não diz.

---

## Fluxo de alteração

### 1. Identifique a natureza da alteração

| Se a alteração é… | Então… |
| --- | --- |
| valor técnico em documento derivado | corrija primeiro a planilha, depois traga a correção para o Markdown |
| texto explicativo em documento redigido | edite o Markdown diretamente |
| link, formatação ou erro de transcrição | edite o Markdown diretamente |

### 2. Confira antes de publicar

- [ ] Os links relativos apontam para arquivos que existem, com o número correto de `../`.
- [ ] As âncoras existem no documento de destino — confira o texto exato do cabeçalho.
- [ ] O sumário **Neste documento** cobre as seções de conteúdo do arquivo.
- [ ] A trilha de navegação aponta para uma seção que existe no README.
- [ ] O documento termina com **Próximos passos** e com o rodapé de fonte.
- [ ] Os blocos de código estão balanceados e os fluxogramas renderizam no GitHub.
- [ ] Nenhum título de nível 2 aparece duas vezes no mesmo arquivo — âncoras duplicadas confundem
      os links.
- [ ] As contagens citadas continuam batendo com o conteúdo: 54 códigos, 13 cenários, 7 etapas de
      POST, 17 nós, 5 ambiguidades, 6 correlações, 10 componentes de validação, 43 termos e
      64 etapas de ferramentas.

### 3. Registre

Toda alteração entra no [changelog](docs/references/changelog.md), com versão, data, o que mudou e
qual aba foi afetada. Pendência resolvida é **marcada como fechada**, não apagada — o histórico da
decisão vale mais que a lista limpa.

Versionamento da documentação:

- **maior** (`2.0.0`) — arquivos renomeados, removidos ou reorganizados;
- **menor** (`1.1.0`) — conteúdo novo, pendência fechada, documento acrescentado;
- **correção** (`1.0.1`) — link, formatação ou erro de transcrição.

Ao mudar a versão, atualize o rodapé de todos os documentos, a tabela de identidade em
[01-visao-geral.md](docs/01-visao-geral.md) e o cabeçalho do [README](README.md).

---

## Onde estão as pendências abertas

[`docs/references/pendencias.md`](docs/references/pendencias.md) lista o que precisa de decisão
humana. As de maior impacto:

- **[P-03](docs/references/pendencias.md#p-03--duas-taxonomias-de-camada-incompatíveis)** — os dois
  arquivos-fonte numeram as camadas de forma incompatível;
- **[P-02](docs/references/pendencias.md#p-02--versão-do-conteúdo-técnico)** — o conteúdo técnico
  não é versionado;
- **[P-17](docs/references/pendencias.md#p-17--planilhas-de-origem-não-versionadas-no-repositório)**
  — as planilhas de origem não estão versionadas, o que impede auditar uma alteração de conteúdo
  técnico pelo histórico do Git.

Antes de abrir uma pendência nova, confira a seção
[*O que não ficou pendente*](docs/references/pendencias.md#o-que-não-ficou-pendente), no fim do
mesmo arquivo — ela registra o que já foi verificado.

---

## Autoria

**Edsilas** — autor e responsável pelo projeto ([`edsilas`](https://github.com/edsilas)).

Licença: MIT, conforme o arquivo
[`LICENSE`](https://github.com/edsilas/base-diagnostico-hardware/blob/main/LICENSE) do
repositório.
