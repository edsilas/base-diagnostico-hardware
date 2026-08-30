---
title: Como contribuir e manter esta base
description: Regras de conteúdo, padrão estrutural dos documentos e fluxo de alteração desta base de conhecimento.
author: Edsilas
date: 2026-08-30
---

# Como contribuir e manter esta base

Este repositório é uma base de conhecimento técnico. A regra que sustenta a confiabilidade dele é
simples e não negociável:

> **Valor técnico não se altera por conveniência de redação.**

Código de erro, tensão, limiar, tempo e comando são o que a base promete entregar certo. Alterar
qualquer um deles sem necessidade técnica comprovada é o que ela existe para impedir.

## Neste documento

- [Quais arquivos carregam valor técnico](#quais-arquivos-carregam-valor-técnico)
- [Padrão estrutural dos documentos](#padrão-estrutural-dos-documentos)
- [Regras de conteúdo](#regras-de-conteúdo)
- [Fluxo de alteração](#fluxo-de-alteração)
- [Autoria](#autoria)

---

## Quais arquivos carregam valor técnico

### Documentos técnicos

Estes documentos contêm os valores que o reparo usa — códigos, tensões, limiares, tempos, comandos
e nomes de componente.

| Arquivo | Conteúdo |
| --- | --- |
| [`docs/06-fluxo-post.md`](docs/06-fluxo-post.md) | Fluxo de diagnóstico de POST |
| [`docs/07-fluxo-sistemico.md`](docs/07-fluxo-sistemico.md) | Fluxo de diagnóstico sistêmico |
| [`docs/08-diagnostico-por-camada.md`](docs/08-diagnostico-por-camada.md) | Camadas de diagnóstico |
| [`docs/09-codigos-post/`](docs/09-codigos-post/00-indice-codigos.md) | Fichas dos códigos de POST |
| [`docs/10-cenarios/`](docs/10-cenarios/00-indice-cenarios.md) | Fichas dos cenários de falha |
| [`docs/11-ambiguidades.md`](docs/11-ambiguidades.md) | Códigos com mais de um significado |
| [`docs/12-correlacoes.md`](docs/12-correlacoes.md) | Falhas em cascata entre camadas |
| [`docs/13-validacao-final.md`](docs/13-validacao-final.md) | Critérios PASS / FAIL por componente |
| [`docs/14-ferramentas/`](docs/14-ferramentas/00-indice-ferramentas.md) | Guias operacionais das ferramentas |
| [`docs/18-indices-cruzados.md`](docs/18-indices-cruzados.md) | Agrupamentos por classificação |
| [`docs/19-comandos.md`](docs/19-comandos.md) | Comandos técnicos reunidos |
| [`docs/20-dispositivos-windows.md`](docs/20-dispositivos-windows.md) | Códigos do Gerenciador de Dispositivos |

> [!IMPORTANT]
> Nestes arquivos, **não altere valores técnicos** — códigos, tensões, limiares, tempos, comandos,
> nomes de componente — sem necessidade técnica comprovada, e registre a mudança no
> [changelog](docs/references/changelog.md). Correções de link, formatação ou erro de digitação
> podem ser feitas diretamente.

### Documentos de organização

Estes documentos organizam, explicam e sinalizam. Não carregam valor técnico próprio e podem ser
editados diretamente — desde que nenhuma afirmação nova entre sem base.

[`README.md`](README.md), este arquivo,
[`docs/00-indice.md`](docs/00-indice.md),
[`01`](docs/01-visao-geral.md), [`02`](docs/02-arquitetura.md),
[`03`](docs/03-taxonomia-camadas.md), [`04`](docs/04-requisitos-e-ferramentas.md),
[`05`](docs/05-utilizacao.md), [`15`](docs/15-seguranca-e-boas-praticas.md), [`16`](docs/16-faq.md),
[`17`](docs/17-glossario.md) e [`docs/references/`](docs/references/changelog.md).

---

## Padrão estrutural dos documentos

Todo documento de `docs/` segue a mesma estrutura, na mesma ordem. Ao criar ou alterar um
documento, mantenha-a — é ela que permite ao leitor saber onde procurar sem reaprender o formato a
cada arquivo.

| # | Elemento | Obrigatório |
| --- | --- | --- |
| 1 | Front matter YAML — `title`, `description`, `author`, `date` | sim |
| 2 | Trilha de navegação de volta ao README | sim |
| 3 | Título e resumo de uma linha | sim |
| 4 | **Aplica-se a** | quando faz sentido |
| 5 | **Neste documento** — sumário com link para cada seção | sim |
| 6 | Contexto, Escopo, Fora do escopo, Relação com outros documentos | sim |
| 7 | Fluxograma | quando o documento resolve uma decisão |
| 8 | Conteúdo | sim |
| 9 | **Próximos passos** | sim |
| 10 | Rodapé com autoria e versão | sim |

### Front matter

Todo documento abre com um bloco YAML de quatro chaves, nesta ordem:

```yaml
---
title: <o mesmo texto do título de nível 1>
description: <resumo de uma linha, sem marcação>
author: Edsilas
date: <AAAA-MM-DD da última revisão do documento>
---
```

Valores que contenham `: ` vão entre aspas duplas. Datas ficam sem aspas.

### Convenções de apresentação

Uniformes em toda a base, para que o material seja lido como um só documento.

| Elemento | Convenção | Por quê |
| --- | --- | --- |
| Marcador de lista | `-` | Um único marcador em toda a base |
| Separador de tabela | `\| --- \|` | O alinhamento à esquerda já é o padrão; `:---` não muda a renderização |
| Cabeçalho de tabela | Sempre nomeado — nunca `\| \| \|` | Célula de cabeçalho vazia deixa a tabela sem rótulo para leitor de tela |
| Cabeçalho do rodapé | `\| Atributo \| Valor \|` | Mesmo motivo |
| Rótulos do rodapé | *Autoria* e *Versão da documentação* | Nomes fixos |
| Identificador de ficha | O título de nível 2 começa pelo ID — `## POST-31 — 2 Âmbar + 1 Branco` | É o ID que as referências cruzadas usam como âncora. O nome descritivo vem em negrito na linha seguinte |

> [!IMPORTANT]
> Não altere o texto de um título de nível 2 que carregue um ID. A âncora que ele gera é o destino
> de dezenas de links vindos do índice de códigos, de
> [`08-diagnostico-por-camada.md`](docs/08-diagnostico-por-camada.md) e de
> [`18-indices-cruzados.md`](docs/18-indices-cruzados.md). Para renomear a parte descritiva, edite a
> linha em negrito abaixo do título.

### Trilha de navegação

A trilha aponta para uma das seções do [README](README.md): *Comece aqui*, *Diagnostique*,
*Resolva*, *Feche o atendimento*, *Opere as ferramentas*, *Consulte a referência* ou *Manutenção*.
Se criar uma seção nova no README, confira que a âncora usada na trilha existe.

O número de `../` depende da profundidade: documentos em `docs/` usam `../README.md`; documentos em
subpasta, como `docs/10-cenarios/`, usam `../../README.md`.

### Avisos

Use os callouts do GitHub, com significado fixo.

| Callout | Quando usar |
| --- | --- |
| `> [!NOTE]` | Observação de leitura |
| `> [!TIP]` | Atalho de navegação |
| `> [!IMPORTANT]` | Pré-requisito ou regra que muda o resultado |
| `> [!WARNING]` | Risco de erro de diagnóstico ou de perda de tempo |
| `> [!CAUTION]` | Risco elétrico, perda de dados ou dano a componente |

### Procedimentos

Fichas de código e de cenário agrupam os campos em fases, nesta ordem: **Identificação** →
**Pré-requisitos** → **Diagnóstico** → **Execução da correção** → **Resultado esperado** →
**Risco e impacto** → **Próximos passos**. Os nomes dos campos dentro de cada fase são fixos e não
devem ser alterados.

### Fluxogramas

- Escreva em Mermaid, dentro de bloco ```` ```mermaid ````. O GitHub renderiza nativamente.
- Use linguagem descritiva nos rótulos ("liga, mas a tela fica preta"), não jargão. O fluxograma
  precisa ser legível por quem não domina a terminologia.
- O diagrama **resume**; o conteúdo integral vem logo abaixo, sem cortes.
- Quando o diagrama condensar ou reorganizar o conteúdo, registre isso em um `> [!NOTE]`.
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
   versão — nada entra sem base técnica.
2. **Lacuna se declara.** Campo sem informação vira *"Informação não identificada"*, nunca uma
   dedução plausível.
3. **Divergência não convive.** Se dois pontos da base trouxerem valores diferentes para o mesmo
   procedimento, não deixe as duas versões conviverem no texto e não crie lista paralela de itens em
   aberto. Adote um valor, aplique-o em toda a base e explique o critério no ponto de uso. Registre
   a decisão no [changelog](docs/references/changelog.md).
4. **Inferência se marca.** Conclusão derivada leva o rótulo **Inferido** no ponto de uso.
5. **Versão se preserva.** `MemTest86 v10+`, `ATX12V v2.53`, `UEFI 2.10` — copie exatamente como
   está. Não atualize por conta própria.
6. **Nome técnico não se troca por sinônimo.** `Q-Code`, `Debug LED`, `power drain`, `boot mínimo`
   têm grafia estabelecida na base.
7. **Contagem se confere.** Números citados no texto — de códigos, cenários, termos, etapas — devem
   bater com o conteúdo. Ao acrescentar ou remover um item, atualize toda ocorrência da contagem.

---

## Fluxo de alteração

### 1. Identifique a natureza da alteração

| Se a alteração é… | Então… |
| --- | --- |
| valor técnico em documento técnico | confirme a necessidade, aplique em toda a base e registre no changelog |
| divergência entre dois pontos da base | adote um valor, aplique em toda a base e explique o critério no ponto de uso |
| texto explicativo em documento de organização | edite o Markdown diretamente |
| link, formatação ou erro de digitação | edite o Markdown diretamente |

### 2. Confira antes de publicar

- [ ] Os links relativos apontam para arquivos que existem, com o número correto de `../`.
- [ ] As âncoras existem no documento de destino — confira o texto exato do cabeçalho.
- [ ] O sumário **Neste documento** cobre as seções de conteúdo do arquivo.
- [ ] A trilha de navegação aponta para uma seção que existe no README.
- [ ] O documento termina com **Próximos passos** e com o rodapé de autoria e versão.
- [ ] Os blocos de código estão balanceados e os fluxogramas renderizam no GitHub.
- [ ] Nenhum título de nível 2 aparece duas vezes no mesmo arquivo — âncoras duplicadas confundem
      os links.
- [ ] As contagens citadas continuam batendo com o conteúdo: 54 códigos, 13 cenários, 7 etapas de
      POST, 17 nós, 5 ambiguidades, 6 correlações, 10 componentes de validação, 47 termos e
      64 etapas de ferramentas.

### 3. Registre

Toda alteração entra no [changelog](docs/references/changelog.md), com versão, data, o que mudou e
qual aba foi afetada. Quando a alteração resolve uma divergência, registre também **qual valor foi
adotado e contra qual documento oficial** — é o que permite auditar a decisão depois.

Versionamento da documentação:

- **maior** (`3.0.0`) — arquivos renomeados, removidos ou reorganizados;
- **menor** (`2.1.0`) — conteúdo novo ou documento acrescentado;
- **correção** (`2.0.1`) — link, formatação ou erro de digitação.

Ao mudar a versão, atualize o rodapé de todos os documentos e a tabela de identidade em
[01-visao-geral.md](docs/01-visao-geral.md).

---

## Autoria

**Edsilas** — autor e responsável pelo projeto ([`edsilas`](https://github.com/edsilas)).

Licença: MIT, conforme o arquivo [`LICENSE`](LICENSE) na raiz do repositório.
