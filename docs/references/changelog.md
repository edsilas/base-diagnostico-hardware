---
title: Histórico da documentação
description: O que mudou em cada versão desta documentação.
author: Edsilas
date: 2026-08-30
---

[Início](../../README.md) › [Manutenção](../../README.md#manutenção) › **Histórico da documentação**

# Histórico da documentação

> O que mudou em cada versão desta documentação.


**Aplica-se a:** Versionamento da documentação

## Neste documento

- [doc-3.0.0 — 2026-08-30](#doc-300--2026-08-30)
- [doc-2.2.0 — 2026-08-30](#doc-220--2026-08-30)
- [doc-2.1.0 — 2026-08-30](#doc-210--2026-08-30)
- [doc-2.0.0 — 2026-08-08](#doc-200--2026-08-08)
- [doc-1.4.0 — 2026-08-07](#doc-140--2026-08-07)
- [doc-1.3.0 — 2026-08-07](#doc-130--2026-08-07)
- [doc-1.2.0 — 2026-08-07](#doc-120--2026-08-07)
- [doc-1.1.0 — 2026-08-07](#doc-110--2026-08-07)
- [doc-1.0.0 — 2026-08-07](#doc-100--2026-08-07)
- [Convenção de versionamento desta documentação](#convenção-de-versionamento-desta-documentação)
- [Como registrar mudanças futuras](#como-registrar-mudanças-futuras)
- [Próximos passos](#próximos-passos)

## Contexto

Registro de mudanças **desta base de conhecimento**.

## Escopo

Versões da documentação e escopo de cada geração.

## Fora do escopo

Conteúdo técnico em si, que vive nos documentos correspondentes.

## Relação com outros documentos

- [Arquitetura da documentação](../02-arquitetura.md)
- [Como contribuir](../../CONTRIBUTING.md)

---

> **Escopo do versionamento.** A partir de `doc-2.0.0`, o número versiona o conjunto publicado —
> estrutura **e** conteúdo técnico. A convenção está em
> [Arquitetura da documentação](../02-arquitetura.md#versionamento-do-conteúdo).

## doc-3.0.0 — 2026-08-30

Reorganização do material de referência e simplificação do rodapé. Mudança **maior** porque dois
arquivos deixaram de existir.

**Sem regressão:** nenhum documento técnico foi removido, nenhuma ficha perdeu campo e nenhum valor
técnico foi alterado — a conferência cobriu todos os trechos entre crases e todos os blocos de
código dos 49 documentos. As contagens permanecem idênticas: 54 códigos de POST, 18 códigos do
Gerenciador de Dispositivos, 13 cenários, 7 etapas de POST, 17 nós, 5 ambiguidades, 6 correlações,
10 componentes de validação, 47 termos e 64 etapas de ferramentas.

### Removido

Dois documentos auxiliares de `docs/references/` deixaram de existir. Nenhum dos dois carregava
conteúdo técnico próprio; a única tabela reaproveitável — o inventário de contagens — foi
preservada em [Conteúdo da base](../00-indice.md#conteúdo-da-base).

### Alterado

| Onde | Antes | Agora |
| --- | --- | --- |
| Rodapé de 49 documentos | Cinco campos de metadados | **Autoria** e **Versão da documentação** |
| [`00-indice.md`](../00-indice.md) | Seção *Convenção de níveis de confiança* | Seção [Conteúdo da base](../00-indice.md#conteúdo-da-base), com as contagens do material |
| [`CONTRIBUTING.md`](../../CONTRIBUTING.md) | Regras 1 a 9, organizadas em torno da procedência | Sete regras, organizadas em torno do valor técnico |
| [`02-arquitetura.md`](../02-arquitetura.md) | Seção de mapeamento auxiliar | Removida; as convenções de organização permanecem |
| [`01-visao-geral.md`](../01-visao-geral.md) | Seção sobre a procedência do material | Removida; a identidade oficial e as fronteiras de cobertura permanecem |
| `README.md` | Seção de manutenção com dois itens auxiliares | *Manutenção*, sem eles |
| 4 trechos de `10-cenarios/` | Construções em português europeu (*aceder*, *a indexar*, *a causar*, *a impedir*) | Português brasileiro |

### Verificação executada

Auditoria mecânica dos 49 documentos e das 1.943 referências relativas: arquivo de destino
existente, âncora existente no destino, sumário presente, trilha de navegação, *Próximos passos*,
rodapé, front matter, cercas de código balanceadas e ausência de título de nível 2 repetido.
**Resultado: nenhuma pendência.**

## doc-2.2.0 — 2026-08-30

Expansão de cobertura para a **camada de sistema operacional**, e padronização de apresentação em
todos os documentos.

**Sem regressão:** nenhum documento foi removido ou renomeado, nenhuma ficha perdeu campo e nenhum
valor técnico foi alterado. As contagens permanecem idênticas — 54 códigos de POST, 13 cenários,
7 etapas de POST, 17 nós, 5 ambiguidades, 6 correlações, 10 componentes de validação, 47 termos e
64 etapas de ferramentas. Os 18 códigos novos formam um catálogo próprio e não entram nessas
contagens.

### Acrescentado

[`20-dispositivos-windows.md`](../20-dispositivos-windows.md) — os 18 códigos do Gerenciador de
Dispositivos do Windows que descrevem falha de hardware, de driver ou de configuração de
dispositivo: 1, 10, 12, 14, 18, 19, 22, 24, 28, 29, 31, 32, 37, 39, 43, 45, 48 e 52.

O documento cobre a lacuna declarada em
[Fronteiras de cobertura](../01-visao-geral.md#fronteiras-de-cobertura): o equipamento que passa do
POST, carrega o Windows, e ali reporta o problema.

| Item | Como foi tratado |
| --- | --- |
| Comandos | `pnputil /enum-devices /problem`, `/enable-device`, `/scan-devices`, `/add-driver … /install`, com a disponibilidade de cada opção por versão do Windows |
| Mensagens de erro | Registradas em inglês, como o sistema as define. A base **não publica** tradução da string do Windows; o identificador estável declarado é o número do código |
| Escala de risco | Própria deste documento, por **reversibilidade da ação de correção** — declarada em [Escala de risco](../20-dispositivos-windows.md#escala-de-risco-deste-documento) |

### Padronizado

| Onde | Antes | Agora |
| --- | --- | --- |
| 34 documentos | Sem front matter; 16 documentos tinham | Front matter em todos, com `title`, `description`, `author` e `date` |
| 10 documentos | Marcador de lista `*` | `-` — 256 linhas |
| 26 documentos | Separador de tabela `\| :--- \|` | `\| --- \|` — 231 células. O alinhamento à esquerda já era o padrão, então a renderização não muda |
| 32 tabelas | Cabeçalho vazio, `\| \| \|` | `\| Atributo \| Valor \|`. Célula de cabeçalho vazia deixa a tabela sem rótulo para leitor de tela |
| 10 fichas de código | *Consulte também* e *Próximos passos* lado a lado, com os mesmos quatro links repetidos | Uma seção só — *Próximos passos*, com a tabela de decisão e um bloco *Para aprofundar* para os links que a tabela não cobre |

As convenções ficaram registradas em
[CONTRIBUTING](../../CONTRIBUTING.md#convenções-de-apresentação), com o motivo de cada uma.

### Verificação executada

Auditoria mecânica de todos os documentos e de suas referências relativas, contra a lista de
[CONTRIBUTING](../../CONTRIBUTING.md#2-confira-antes-de-publicar). Além dela, conferência de
integridade contra o estado anterior: **nenhum trecho entre crases e nenhum bloco de código
desapareceu de qualquer documento**, e nenhum documento encolheu. **Resultado: nenhuma pendência.**

## doc-2.1.0 — 2026-08-30

Reescrita editorial das fichas de código de POST, dos cenários e dos guias de ferramentas — 26
documentos ganharam texto mais direto, voltado a quem não é técnico —, seguida da **restauração dos
contratos que essa reescrita havia rompido**.

**Sem regressão:** nenhuma ficha perdeu campo, nenhum valor técnico foi alterado — a conferência
cobriu todos os trechos entre crases e todos os blocos de código — e as contagens permanecem
idênticas a `doc-2.0.0`.

### Corrigido

| Onde | Antes | Agora |
| --- | --- | --- |
| 10 fichas de `09-codigos-post/` | Títulos sem o identificador (`## 2 Âmbar + 1 Branco: …`), o que invalidava **423 referências cruzadas** vindas do índice de códigos, de `08-diagnostico-por-camada.md` e de `18-indices-cruzados.md` | `## POST-31 — 2 Âmbar + 1 Branco`, com o nome descritivo preservado logo abaixo. As 423 âncoras voltaram a resolver |
| 10 fichas de `09-codigos-post/` | Sem *Contexto*, *Escopo*, *Fora do escopo*, *Relação com outros documentos* nem *Próximos passos* | Estrutura canônica restaurada, no modelo de [`lenovo.md`](../09-codigos-post/lenovo.md), único arquivo da pasta que a preservava |
| [`acer-insyde.md`](../09-codigos-post/acer-insyde.md) | Sem sumário e sem cabeçalho de código; a ficha começava em *Visão geral do erro* | Sumário restaurado e ficha ancorada em `## POST-49 — 1 Longo + 2 Curtos` |
| 9 fichas de `10-cenarios/` | Grafia europeia: *registado*, *detetado*, *ficheiros*, *sistema operativo*, *ecrã*, *noutro*, *os seus campos* | Grafia brasileira |
| 2 fichas de `10-cenarios/` | *Gestor de Discos* | **Gerenciamento de Disco** — nome real do console `diskmgmt.msc` no Windows em português do Brasil. O rótulo anterior não existe nessa versão do sistema e levava o leitor a procurar algo inexistente |
| 15 documentos de `10-cenarios/` e `14-ferramentas/` | *Fora do escopo* rebaixado a linha em negrito dentro de *Escopo* | Seção `## Fora do escopo` restaurada, com entrada no sumário |
| 16 documentos | Sumário intitulado *Neste artigo* | *Neste documento*, conforme o padrão estrutural |
| 24 documentos | *sistémico* | *sistêmico* |

### Verificação executada

Conferência mecânica de todos os documentos e referências relativas contra a lista de
[CONTRIBUTING](../../CONTRIBUTING.md#2-confira-antes-de-publicar): arquivos de destino existentes,
âncoras existentes no destino, sumário presente, trilha de navegação, *Próximos passos*, rodapé,
cercas de código balanceadas e ausência de título de nível 2 repetido. **Resultado: nenhuma
pendência.**

## doc-2.0.0 — 2026-08-08

Consolidação da base. As divergências que antes eram apenas registradas passaram a ser
**resolvidas**, e a decisão foi incorporada ao ponto de uso. Os registros temporários de
acompanhamento — a lista de pendências e o documento de limitações — deixaram de existir: o que
neles era problema em aberto virou conteúdo; o que era fronteira de escopo foi para
[Visão geral](../01-visao-geral.md#fronteiras-de-cobertura); o que era precaução virou
[Segurança e boas práticas](../15-seguranca-e-boas-praticas.md).

**Sem regressão:** nenhuma ficha técnica perdeu campo, e todas as contagens permaneceram idênticas.

### Divergências resolvidas

| Divergência | Como estava | Decisão adotada |
| --- | --- | --- |
| Duração da descarga de energia residual | 30 s em um registro, 10 s no outro | **30 s**, valor que satisfaz e supera todos os mínimos aplicáveis |
| Composição do *boot mínimo* | Três definições literais concorrentes | **Duas composições nomeadas** — *absoluto* e *com vídeo* —, com o cooler obrigatório nas duas, porque o controle térmico da CPU atua já na faixa de Tjunction max |
| Limiar térmico em repouso | 60 °C em um registro, 90 °C em outro | **Escala de dois estágios:** 60 °C abre a investigação, 90 °C confirma a falha térmica |
| Critério FAIL de temperatura | 95 °C na linha *CPU*, 90 °C na linha *Térmico* | **Sujeitos diferentes.** 95 °C julga a CPU como peça; 90 °C julga o subsistema de refrigeração. Para liberar o equipamento prevalece o mais restritivo |

### Corrigido

| Onde | Antes | Agora |
| --- | --- | --- |
| [09-codigos-post/lenovo.md](../09-codigos-post/lenovo.md) | Procedimento do SmartBeep sem o passo de reemissão | Acrescentado o passo de **pressionar Fn** para reemitir o bipe |
| [14-ferramentas/memtest86.md](../14-ferramentas/memtest86.md) | Bateria padrão descrita como 13 algoritmos | Registrada a contagem correta: **testes 0 a 13 — quatorze**, sendo o 13 o *Hammer Test* |
| [17-glossario.md](../17-glossario.md) | SEC, PEI, BIST e XMP/EXPO/DOCP sem expansão | Expansões incorporadas |

### Acrescentado

- [15-seguranca-e-boas-praticas.md](../15-seguranca-e-boas-praticas.md) — precauções de bancada e
  os procedimentos transversais canônicos: descarga de energia residual, boot mínimo e leitura dos
  limiares térmicos.
- Seção *Fronteiras de cobertura* em [01-visao-geral.md](../01-visao-geral.md#fronteiras-de-cobertura).

### Terminologia unificada

`power drain`, `boot mínimo`, `Q-Code` e `Debug LED` passaram a ter grafia única em toda a base.

### Removido

Os registros temporários de acompanhamento, cujo conteúdo foi incorporado aos documentos
definitivos citados acima.

## doc-1.4.0 — 2026-08-07

Revisão de integridade: três divergências entre documentos foram corrigidas e uma contradição foi
resolvida. **Sem regressão:** nenhum documento foi removido ou renomeado, nenhuma ficha perdeu
campo, e todas as contagens técnicas permaneceram idênticas a `doc-1.3.0`.

A contagem de etapas do MemTest86 foi refeita campo a campo sobre as dez etapas de
[memtest86.md](../14-ferramentas/memtest86.md), e a contagem de camadas do modelo sistêmico foi
acertada em **dez números (1–10)**, como já documentavam
[03-taxonomia-camadas.md](../03-taxonomia-camadas.md) e os demais pontos da base.

## doc-1.3.0 — 2026-08-07

Navegação centralizada no README e fluxogramas estratégicos. **Sem regressão:** nenhum documento
foi removido, nenhuma ficha perdeu campo, e todas as contagens técnicas permaneceram idênticas.

**README como ponto de entrada.** Reescrito para funcionar como central de navegação de toda a
base: fluxograma mestre de triagem do sintoma até o laudo, tabela **situação → documento** com
14 entradas, e agrupamento dos documentos por etapa do atendimento.

**Fluxogramas.** Diagramas em Mermaid acrescentados aos documentos que resolvem uma decisão, com
rótulos em linguagem descritiva em vez de jargão.

## doc-1.2.0 — 2026-08-07

Expansão de acesso ao conteúdo. **Sem regressão:** nenhuma ficha técnica perdeu conteúdo; as
contagens de códigos, cenários, camadas, ambiguidades, correlações e etapas permaneceram idênticas.

**Adicionado**

- [18-indices-cruzados.md](../18-indices-cruzados.md) — os mesmos registros reagrupados por
  componente afetado, camada, risco declarado, fase do POST, tipo de sinal e ferramenta exigida,
  mais a cadeia de dependências entre cenários.
- [19-comandos.md](../19-comandos.md) — os comandos técnicos reunidos, com camada, risco e link
  para a ficha.

## doc-1.1.0 — 2026-08-07

Identificação oficial do projeto. **Sem regressão:** nenhum conteúdo técnico foi alterado, removido
ou reescrito. As contagens, os textos das fichas e a estrutura de arquivos permaneceram idênticos a
`doc-1.0.0`.

**Alterado**

- Nome do projeto: identificador provisório `HW_HARDWARE` substituído por
  **Base de Diagnóstico de Hardware** (`base-diagnostico-hardware`).
- [README.md](../../README.md): título, descrição oficial, licença, instruções de clonagem, seção
  de manutenção e créditos.
- [01-visao-geral.md](../01-visao-geral.md): nova seção *Identidade oficial*.

## doc-1.0.0 — 2026-08-07

Geração inicial da base de conhecimento.

**Adicionado**

- Estrutura modular com 18 documentos de nível raiz e 3 diretórios temáticos.
- Catálogo de 54 códigos de POST, dividido em 11 arquivos por família de BIOS.
- 13 fichas de cenário de falha, agrupadas em 9 arquivos.
- Fluxo de POST (7 etapas) e fluxo sistêmico (17 nós).
- Fichas das 7 camadas de diagnóstico do modelo POST.
- 5 casos de ambiguidade e 6 correlações em cascata.
- Matriz de validação final com 10 componentes.
- Guias operacionais de Victoria, AIDA64 e MemTest86, com 64 etapas no total.
- Glossário, FAQ e índice geral.

---

## Convenção de versionamento desta documentação

| Escala | Quando |
| --- | --- |
| **maior** (`3.0.0`) | Arquivos renomeados, removidos ou reorganizados |
| **menor** (`2.1.0`) | Conteúdo novo ou documento acrescentado |
| **correção** (`2.0.1`) | Link, formatação ou erro de digitação |

## Como registrar mudanças futuras

Toda alteração entra aqui, com versão, data e o que mudou. Quando a alteração resolve uma
divergência, registre também **qual valor foi adotado e com que critério** — é o que permite
auditar a decisão depois. Ao mudar a versão, atualize o rodapé de todos os documentos e a tabela de
identidade em [01-visao-geral.md](../01-visao-geral.md#identidade-oficial).

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| vai alterar a documentação | [Como contribuir](../../CONTRIBUTING.md) |
| quer entender como a base está organizada | [Arquitetura da documentação](../02-arquitetura.md) |
| quer o mapa de todos os documentos | [Índice da documentação](../00-indice.md) |

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
