<!-- Gerado a partir de Verificação direta sobre ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Manutenção e rastreabilidade](../../README.md#manutenção-e-rastreabilidade) › **Pendências e itens que exigem validação humana**

# Pendências e itens que exigem validação humana

> Tudo que não pôde ser resolvido a partir das fontes: informação ausente, conflitante ou que exige decisão do proprietário.


**Aplica-se a:** Planejamento de manutenção da base

## Neste documento

- [Como ler esta lista](#como-ler-esta-lista)
- [Resumo](#resumo)
- [~~P-01 — Nome oficial do projeto~~ · FECHADA](#p-01--nome-oficial-do-projeto--fechada)
- [P-02 — Versão do conteúdo técnico](#p-02--versão-do-conteúdo-técnico)
- [P-03 — Duas taxonomias de camada incompatíveis](#p-03--duas-taxonomias-de-camada-incompatíveis)
- [P-04 — Modelo de camadas B sem tabela de definição](#p-04--modelo-de-camadas-b-sem-tabela-de-definição)
- [P-05 — Duração do *power drain*](#p-05--duração-do-power-drain)
- [P-06 — Composição do *boot mínimo*](#p-06--composição-do-boot-mínimo)
- [P-07 — Limiar térmico em idle](#p-07--limiar-térmico-em-idle)
- [P-08 — Critério FAIL de temperatura na validação final](#p-08--critério-fail-de-temperatura-na-validação-final)
- [P-09 — FI-01 inalcançável pelo fluxo sistêmico](#p-09--fi-01-inalcançável-pelo-fluxo-sistêmico)
- [P-10 — Beep contínuo de teclado (AMI) sem ficha no catálogo](#p-10--beep-contínuo-de-teclado-ami-sem-ficha-no-catálogo)
- [P-11 — Lenovo SmartBeep sem procedimento](#p-11--lenovo-smartbeep-sem-procedimento)
- [P-12 — Campos vazios nos guias de ferramentas](#p-12--campos-vazios-nos-guias-de-ferramentas)
- [P-13 — Bloco de critérios do MemTest86 fora da estrutura](#p-13--bloco-de-critérios-do-memtest86-fora-da-estrutura)
- [P-14 — Nós F06 e F08 sem cenário associado](#p-14--nós-f06-e-f08-sem-cenário-associado)
- [P-15 — Referências externas citadas mas não verificadas](#p-15--referências-externas-citadas-mas-não-verificadas)
- [P-16 — Identificador `POST-NN` criado por esta documentação](#p-16--identificador-post-nn-criado-por-esta-documentação)
- [P-17 — Planilhas de origem não versionadas no repositório](#p-17--planilhas-de-origem-não-versionadas-no-repositório)
- [O que **não** ficou pendente](#o-que-não-ficou-pendente)
- [Próximos passos](#próximos-passos)

## Contexto

Lista de tudo que não pôde ser resolvido a partir das fontes: informação ausente, informação conflitante e decisão que só o proprietário do projeto pode tomar. Nada aqui foi preenchido por suposição.

## Escopo

Pendências classificadas por tipo, com evidência, impacto e o que é necessário para fechar.

## Fora do escopo

Limitações estruturais do material, que estão em [15-limitacoes.md](../15-limitacoes.md).

## Relação com outros documentos

- [Limitações](../15-limitacoes.md)
- [Taxonomia de camadas](../03-taxonomia-camadas.md)
- [Fontes](fontes.md)
- [Matriz de rastreabilidade](matriz-rastreabilidade.md)

---

## Como ler esta lista

Cada pendência traz os mesmos campos, na mesma ordem:

| Campo | O que informa |
| --- | --- |
| **Situação** | O que foi encontrado nas fontes, com a citação literal quando ela é o próprio problema |
| **Impacto** | O efeito prático no diagnóstico, e para quem |
| **O que já foi feito** | A mitigação aplicada na documentação, quando existe. Mitigação não fecha a pendência |
| **Para fechar** | A ação concreta que resolve o item — quase sempre na planilha de origem |
| **Status** | Em que estágio o item está |

Nas pendências fechadas, **O que já foi feito** é substituído por **Como foi resolvida**.

O campo **Status** usa quatro valores:

| Status | Significa |
| --- | --- |
| **Fechada** | Resolvida e registrada no [changelog](changelog.md). Mantida na lista para preservar o histórico da decisão |
| **Necessita validação** | Depende de conferência contra a fonte ou de confirmação de que o comportamento é intencional |
| **Decisão pendente** | Depende de uma escolha do proprietário do projeto; não há resposta certa a apurar |
| **Parcialmente verificada** | Parte do item foi confirmada; o restante continua em aberto |

## Resumo

| # | Pendência | Tipo | Severidade | Status |
| --- | --- | --- | --- | --- |
| [~~P-01~~](#p-01--nome-oficial-do-projeto--fechada) | ~~Nome oficial do projeto~~ | Ausência | — | **Fechada** em `doc-1.1.0` |
| [P-02](#p-02--versão-do-conteúdo-técnico) | Versão do conteúdo técnico | Ausência | Média | Decisão pendente |
| [P-03](#p-03--duas-taxonomias-de-camada-incompatíveis) | Duas taxonomias de camada incompatíveis | Conflito | **Alta** | Decisão pendente |
| [P-04](#p-04--modelo-de-camadas-b-sem-tabela-de-definição) | Modelo de camadas B sem tabela de definição | Ausência | **Alta** | Decisão pendente |
| [P-05](#p-05--duração-do-power-drain) | Duração do *power drain*: 30 s vs 10 s | Conflito | Média | Decisão pendente |
| [P-06](#p-06--composição-do-boot-mínimo) | Composição do *boot mínimo* divergente | Conflito | Média | Decisão pendente |
| [P-07](#p-07--limiar-térmico-em-idle) | Limiar térmico em idle: 60 °C vs 90 °C | Conflito | Média | Decisão pendente |
| [P-08](#p-08--critério-fail-de-temperatura-na-validação-final) | Critério FAIL de temperatura: 95 °C vs 90 °C | Conflito | Média | Decisão pendente |
| [P-09](#p-09--fi-01-inalcançável-pelo-fluxo-sistêmico) | FI-01 inalcançável pelo fluxo sistêmico | Inconsistência | Média | Necessita validação |
| [P-10](#p-10--beep-contínuo-de-teclado-ami-sem-ficha-no-catálogo) | Beep contínuo de teclado (AMI) sem ficha no catálogo | Lacuna | Média | Necessita validação |
| [P-11](#p-11--lenovo-smartbeep-sem-procedimento) | Lenovo SmartBeep sem procedimento | Lacuna | Baixa | Parcialmente verificada |
| [P-12](#p-12--campos-vazios-nos-guias-de-ferramentas) | Campos `Atalho de Teclado` e `Alternativa Segura` vazios | Lacuna | Baixa | Necessita validação |
| [P-13](#p-13--bloco-de-critérios-do-memtest86-fora-da-estrutura) | Bloco de critérios do MemTest86 fora da estrutura de etapas | Estrutura | Baixa | Decisão pendente |
| [P-14](#p-14--nós-f06-e-f08-sem-cenário-associado) | Nós F06 e F08 sem cenário associado | Estrutura | Baixa | Necessita validação |
| [P-15](#p-15--referências-externas-citadas-mas-não-verificadas) | Referências externas citadas mas não verificadas | Verificação | Média | Parcialmente verificada |
| [P-16](#p-16--identificador-post-nn-criado-por-esta-documentação) | Identificador `POST-NN` criado por esta documentação | Decisão | Baixa | Decisão pendente |
| [P-17](#p-17--planilhas-de-origem-não-versionadas-no-repositório) | Planilhas de origem não versionadas no repositório | Rastreabilidade | Média | Decisão pendente |

**16 pendências abertas, 1 fechada.** As duas de severidade alta — P-03 e P-04 — tratam do mesmo
assunto: a numeração de camadas. Resolver a taxonomia na fonte fecha as duas.

---

## ~~P-01 — Nome oficial do projeto~~ · FECHADA

**Situação original.** Nenhuma das 12 abas declarava o nome do projeto. Na versão `doc-1.0.0` foi
usado o identificador provisório `HW_HARDWARE`, derivado do prefixo comum dos nomes de arquivo e
marcado como necessitando validação.

**Como foi resolvida.** O proprietário informou o repositório oficial
`https://github.com/edsilas/base-diagnostico-hardware`. A consulta ao repositório, em 2026-08-07,
confirmou nome, proprietário, descrição oficial e licença.

| Item | Valor confirmado |
| --- | --- |
| Identificador canônico | `base-diagnostico-hardware` |
| Nome de exibição | Base de Diagnóstico de Hardware |
| Proprietário | `edsilas` |
| Descrição oficial | "Base estruturada de conhecimento para diagnóstico de hardware, com fluxos, sintomas, códigos de erro, causas e procedimentos de análise e solução." |
| Licença | MIT |

O identificador provisório `HW_HARDWARE` foi substituído em `README.md`, `01-visao-geral.md` e
`references/fontes.md`. O prefixo `HW_HARDWARE_` permanece apenas nos **nomes dos arquivos-fonte**,
onde é literal e não deve ser alterado.

**Status:** **Fechada em `doc-1.1.0`.** Mantida no registro para preservar o histórico da decisão.

---

## P-02 — Versão do conteúdo técnico

**Situação.** Os arquivos `.xlsx` não contêm `docProps/core.xml`, onde o Excel grava autor, título
e datas, e nenhuma aba tem campo de versão.

**Parcialmente resolvida em `doc-1.1.0`:**

| Item | Situação anterior | Situação atual |
| --- | --- | --- |
| Autor / responsável | Não identificado | **Confirmado** — `edsilas`, proprietário do repositório |
| Licença | Não identificada | **Confirmado** — MIT |
| Versão do conteúdo técnico | Não identificada | **Continua não identificada** |

**O que permanece aberto.** Não há como saber, ao olhar uma planilha, se um procedimento foi
revisado, quando, e em relação a qual versão anterior. A documentação versiona a si mesma
(`doc-1.x.y`), mas isso **não** é a versão do conteúdo técnico.

**Impacto.** Médio. Um procedimento desatualizado é indistinguível de um atualizado.

**Para fechar.** Adotar um campo de versão nas planilhas — uma aba `METADADOS` com versão, data de
revisão e responsável resolveria — e passar a marcar releases no repositório (`git tag`).

**Status:** Decisão pendente.

---

## P-03 — Duas taxonomias de camada incompatíveis

**Situação.** `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` usa 7 camadas no formato `Camada N: Nome`;
`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` usa outra numeração no formato `N - Nome`. Somente a
camada 1 (*Energia*) coincide.

Exemplos de divergência direta:

| Nº | Modelo A | Modelo B |
| --- | --- | --- |
| 2 | CPU | Firmware |
| 3 | Memória | CPU |
| 4 | Vídeo | Memória |
| 5 | Chipset / Motherboard | Armazenamento |
| 6 | Firmware | GPU |
| 7 | Periféricos Críticos | Placa-mãe |

**Impacto.** Alto. Um técnico que leia "camada 3" sem saber a origem testa o subsistema errado.

**O que já foi feito.** Nenhum modelo foi escolhido. Ambos estão documentados em
[03-taxonomia-camadas.md](../03-taxonomia-camadas.md), e todo número de camada é reproduzido no
formato original, que identifica o modelo.

**Para fechar.** Unificar a numeração na fonte (planilhas) e propagar a correção para a
documentação, **ou**
declarar formalmente que os dois modelos coexistem por escopo distinto.

**Status:** Decisão pendente.

---

## P-04 — Modelo de camadas B sem tabela de definição

**Situação.** O modelo de camadas do arquivo de fluxo não possui aba de definição. Foi
reconstruído varrendo as ocorrências literais nas células. Consequências:

- as camadas **2 (Firmware)**, **8 (Periféricos)** e **10 (Drivers)** aparecem apenas na aba
  `CORRELACOES`;
- a camada **7 (Placa-mãe)** aparece apenas em `TABELA_PRINCIPAL`;
- **nenhuma** camada do modelo B tem ficha técnica com componentes, testes primários e indicadores
  de falha, ao contrário do modelo A.

**Para fechar.** Criar, na planilha de origem, uma aba de definição equivalente a
`Camadas de Diagnóstico`, cobrindo as 10 camadas do modelo B.

**Status:** Decisão pendente.

---

## P-05 — Duração do *power drain*

**Situação.**

| Fonte | Instrução literal |
| --- | --- |
| `CODIGOS_DE_ERROS` → `Tabela Diagnóstico POST` | "Power drain completo (desligar, remover cabo AC, segurar power 30s)" e "Segurar botão power 30 segundos (descarga capacitores)" |
| `FLUXO_DIAGNOSTICO` → `TABELA_PRINCIPAL` (NL-01) | "Descarregar capacitores residuais (pressionar Power 10s com cabo desconectado)" |

**Impacto.** Médio. Descarga insuficiente pode manter tensão residual durante a manipulação.

**Para fechar.** Definir a duração de referência e uniformizar nas duas planilhas.

**Status:** Decisão pendente. Ambas as versões estão preservadas nos documentos.

---

## P-06 — Composição do *boot mínimo*

**Situação.** Três definições diferentes coexistem:

| Fonte | Definição literal |
| --- | --- |
| `CODIGOS_DE_ERROS` → `Fluxo de Diagnóstico`, Etapa 2 | "boot mínimo (CPU + 1 RAM + fonte)" |
| `CODIGOS_DE_ERROS` → `Tabela Diagnóstico POST` | "Testar boot mínimo (CPU+RAM+Vídeo apenas)" e "Boot mínimo absoluto (CPU + 1 RAM + fonte, sem GPU)" |
| `FLUXO_DIAGNOSTICO` → `FLUXO_LOGICO`, F02b | "Minimal boot: CPU+Cooler+1RAM+PSU apenas" |

**Impacto.** Médio. A presença ou ausência de cooler e de vídeo muda o resultado do teste.

**Para fechar.** Definir uma composição canônica e, se necessário, variantes nomeadas.

**Status:** Decisão pendente. As três definições estão preservadas nos documentos.

---

## P-07 — Limiar térmico em idle

**Situação.** Dois limiares para o mesmo julgamento:

| Registro | Limiar |
| --- | --- |
| `TABELA_PRINCIPAL` → SA-01, método de diagnóstico | "SE > 60°C em idle → problema térmico confirmado" |
| `TABELA_PRINCIPAL` → SA-01, sintoma observado | "CPU operando acima de 90°C em idle" |
| `CORRELACOES` → COR-04 | "SE CPU > 90°C em idle → problema térmico (não de software)" |

**Impacto.** Médio. Define se um equipamento é ou não encaminhado para manutenção térmica.

**Para fechar.** Definir o limiar de decisão em idle e, se houver faixas distintas (alerta vs
confirmação), nomeá-las.

**Status:** Decisão pendente. Os dois limiares estão preservados nos documentos.

---

## P-08 — Critério FAIL de temperatura na validação final

**Situação.** Dentro da **mesma aba** `VALIDACAO_FINAL`:

| Linha | Critério FAIL |
| --- | --- |
| CPU | "Temp > 95°C" |
| Térmico | "Temp > 90°C" |

**Impacto.** Médio. Um equipamento a 92 °C é aprovado por uma linha e reprovado por outra.

**Para fechar.** Definir se os limiares são intencionalmente diferentes (componente vs sistema
térmico) e explicitar essa distinção na fonte.

**Status:** Decisão pendente.

---

## P-09 — FI-01 inalcançável pelo fluxo sistêmico

**Situação.** O ID `FI-01` (*Falhas intermitentes*) existe em `TABELA_PRINCIPAL` e em
`INDICE_CENARIOS`, mas **nenhum nó de `FLUXO_LOGICO` o referencia**. Todos os outros 12 IDs são
alcançados por pelo menos um nó.

**Impacto.** Médio. Quem seguir apenas o fluxo nunca chega ao cenário de falhas intermitentes.

**Para fechar.** Acrescentar ao fluxo um nó que conduza a FI-01, ou documentar que o cenário é de
entrada direta pelo índice.

**O que já foi feito.** Desde `doc-1.2.0`, a ficha de FI-01 exibe, nas referências cruzadas,
o aviso de que nenhum nó do fluxo conduz até ela, com link para esta pendência. O aviso deve ser
removido quando algum nó do fluxo passar a referenciar FI-01.

**Status:** Necessita validação.

---

## P-10 — Beep contínuo de teclado (AMI) sem ficha no catálogo

**Situação.** A aba `Ambiguidade de Códigos` registra que, em algumas versões AMI, beep contínuo
indica tecla presa ou erro de teclado. O catálogo de códigos, porém, só tem entrada de beep
contínuo para Award (memória não instalada/não detectada).

**Impacto.** Médio. O técnico que consultar apenas o catálogo não encontra a hipótese de teclado.

**Para fechar.** Criar a entrada correspondente na aba `Tabela Diagnóstico POST`, ou confirmar
que o tratamento fica restrito ao documento de ambiguidades.

**Status:** Necessita validação. O caso está documentado em
[11-ambiguidades.md](../11-ambiguidades.md).

---

## P-11 — Lenovo SmartBeep sem procedimento

**Situação.** O registro do SmartBeep traz "Variável" nos campos de componente, camada, fase e
risco, e remete ao aplicativo Lenovo PC Diagnostics. Não há procedimento próprio.

**Impacto.** Baixo — a fonte indica a ferramenta correta —, mas a ficha fica sem conteúdo
acionável offline.

**O que a documentação oficial da Lenovo informa.** A pergunta original desta pendência era se
existiria uma tabela melodia → significado a documentar. A consulta ao manual oficial do
fabricante responde que **não**: a decodificação é feita pelo aplicativo, e a Lenovo não publica a
correspondência em forma de tabela. O procedimento publicado tem quatro passos:

1. Acessar `https://support.lenovo.com/smartbeep`.
2. Instalar o aplicativo de diagnóstico no smartphone.
3. Executar o aplicativo com o smartphone próximo ao computador.
4. Pressionar **Fn** no computador para emitir o bipe novamente; o aplicativo decodifica o erro e
   apresenta as soluções possíveis.

O recurso se aplica a sintomas de tela preta acompanhados de bipes, em modelos ThinkPad e
ThinkStation compatíveis.

> [!NOTE]
> Esta verificação foi feita contra o manual do fabricante — *ThinkPad P15v / T15p Gen 3 User
> Guide*, Lenovo, julho de 2023, tópico *Beep errors* — e **não** contra a planilha de origem. Ela
> confirma que a informação pedida não existe em forma tabular, mas não é fonte primária desta
> base: nada dela foi incorporado às fichas técnicas. Ver
> [regras de conteúdo](../../CONTRIBUTING.md#regras-de-conteúdo), item 7.

**Para fechar.** Decidir se o passo operacional confirmado acima — pressionar **Fn** para reemitir
o bipe — entra na planilha de origem como procedimento do registro SmartBeep. Se entrar, a ficha
deixa de ficar sem conteúdo acionável; se não entrar, registrar que a remissão ao aplicativo é o
tratamento definitivo.

**Status:** Parcialmente verificada. A existência da tabela de melodias foi descartada em fonte
oficial; a decisão sobre o procedimento continua aberta.

---

## P-12 — Campos vazios nos guias de ferramentas

**Situação.**

| Aba | Campo | Vazios (nas etapas) |
| --- | --- | --- |
| `REF_Victoria` | Atalho de Teclado | 6 de 9 |
| `REF_AIDA64` | Atalho de Teclado | 42 de 45 |
| `REF_AIDA64` | Alternativa Segura | 4 de 45 |
| `REF_MemTest86` | Atalho de Teclado | 7 de 10 |
| `REF_MemTest86` | Alternativa Segura | 5 de 10 |

Em [memtest86.md](../14-ferramentas/memtest86.md), os atalhos faltam nas etapas 1, 4, 5, 6, 7, 8 e
10; a alternativa segura falta nas etapas 2, 4, 5, 6 e 10.

> [!NOTE]
> **O denominador de `REF_MemTest86` é ambíguo.** A aba tem onze linhas de conteúdo: as dez etapas
> do procedimento mais o bloco de critérios de decisão descrito em
> [P-13](#p-13--bloco-de-critérios-do-memtest86-fora-da-estrutura), cujos campos também estão
> vazios. Uma contagem sobre as onze linhas devolve 8 e 6; sobre as dez etapas, 7 e 5. A tabela
> acima usa as dez etapas, que é o recorte verificável nos documentos. Qual dos dois recortes a
> planilha considera não pôde ser confirmado, porque ela não está versionada
> ([P-17](#p-17--planilhas-de-origem-não-versionadas-no-repositório)).

**Impacto.** Baixo. É plausível que muitas etapas simplesmente não tenham atalho, mas a fonte não
distingue "não existe" de "não preenchido".

**O que já foi feito.** Nos documentos, esses campos exibem
*"Informação não identificada na fonte analisada"*, em vez de a seção ser omitida.

**Para fechar.** Preencher com `N/A` onde não houver atalho, para eliminar a ambiguidade, e
definir se o bloco de critérios conta como linha de `REF_MemTest86` — o que também resolve P-13.

**Status:** Necessita validação.

---

## P-13 — Bloco de critérios do MemTest86 fora da estrutura

**Situação.** A última linha de `REF_MemTest86` não é uma etapa: é um bloco de critérios de decisão
pós-teste ocupando a coluna `Nº da Etapa`.

**Impacto.** Baixo, mas quebra a estrutura tabular da aba e prejudica processamento automático.

**O que já foi feito.** O bloco foi extraído e apresentado como seção própria, com aviso explícito,
em [memtest86.md](../14-ferramentas/memtest86.md).

**Para fechar.** Mover o bloco para uma aba ou coluna própria na planilha.

**Status:** Decisão pendente.

---

## P-14 — Nós F06 e F08 sem cenário associado

**Situação.** Os nós `F06` ("O sistema completa o boot do SO normalmente?") e `F08` ("Sistema opera
estável em uso normal?") têm o campo `Referência (ID)` preenchido com "—".

**Impacto.** Baixo. São nós de bifurcação pura, sem ação própria; a ausência pode ser intencional.

**Para fechar.** Confirmar que é intencional.

**Status:** Necessita validação.

---

## P-15 — Referências externas citadas mas não verificadas

**Situação.** As planilhas citam documentação de fabricantes e normas nos campos de fonte —
AMI, Phoenix, Award, Intel ATX12V PSU Design Guide v2.53, JEDEC, UEFI Specification 2.10, entre
outras. A lista completa está em [fontes.md](fontes.md).

**Impacto.** Médio. As referências sustentam afirmações técnicas específicas (valores de tensão,
tolerância de ripple, intervalos de refresh).

**Verificação bibliográfica.** As designações citadas foram conferidas contra os órgãos que
publicam cada documento. Isso confirma **que o documento existe e como ele se chama** — não que a
afirmação técnica atribuída a ele esteja lá.

| Referência como citada | Situação | Observação |
| --- | --- | --- |
| UEFI Specification 2.10 | **Existe** | Publicada pelo UEFI Forum em agosto de 2022; Errata A em agosto de 2024. Substituída pela versão 2.11, de dezembro de 2024 |
| JEDEC JESD79-4 (DDR4) e JESD79-5 (DDR5) | **Existem** | Designações oficiais JEDEC. A JESD79-5 é de julho de 2020; a revisão mais recente, JESD79-5D, é de novembro de 2025 |
| Intel ATX12V PSU Design Guide v2.53 | **Existe, com ressalva** | Ver abaixo |
| AMI, Phoenix e Award (manuais de beep e status codes) | **Não verificável como citado** | As citações trazem títulos genéricos, sem número de documento nem versão |

> [!IMPORTANT]
> **A citação do guia da Intel está imprecisa.** Não existe um documento independente chamado
> *ATX12V Power Supply Design Guide* na versão 2.53 — essa série autônoma parou na versão 2.4.
> O que existe é o capítulo **ATX12V Specific Guidelines 2.53**, dentro do *ATX Multi Rail Desktop
> Platform Power Supply Design Guide* da Intel (documento nº 336521). A versão **2.53 está
> correta**; o que está errado é o título, que sugere um documento que não existe sob esse nome.

**Impacto da imprecisão.** Baixo para o diagnóstico, alto para quem tentar localizar a fonte: uma
busca pelo título citado não encontra o documento.

**O que continua em aberto.** Nenhuma **afirmação técnica** foi confrontada com o texto original.
Saber que a UEFI 2.10 existe não confirma que o código de POST atribuído a ela conste da
especificação. É essa conferência, campo a campo, que eleva o nível de confiança de
"Não confirmado" para "Oficial".

**Para fechar.**

1. Corrigir, na planilha de origem, o título da referência ao guia da Intel.
2. Acrescentar número de documento e versão às citações de AMI, Phoenix e Award.
3. Conferir cada afirmação técnica contra a seção correspondente do documento original.

**Status:** Parcialmente verificada. A identidade de três referências foi confirmada; o conteúdo
atribuído a todas elas continua não confirmado.

---

## P-16 — Identificador `POST-NN` criado por esta documentação

**Situação.** Os códigos de POST não têm identificador na fonte. Para permitir link estável entre
documentos, foi criado o identificador `POST-01` … `POST-54`, seguindo a ordem das linhas.

**Impacto.** Baixo, mas com um risco de manutenção: inserir uma linha no meio da planilha
**desloca todos os identificadores seguintes**.

**Para fechar.** Adotar uma coluna `ID` na planilha de origem, com valores estáveis, e passar a
usá-la como identificador nos documentos, no lugar da posição da linha.

**Status:** Decisão pendente.

---

## P-17 — Planilhas de origem não versionadas no repositório

**Situação.** No momento da consulta (2026-08-07), o repositório continha apenas `LICENSE` e
`README.md`. Os arquivos `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` e
`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` — que são a fonte da verdade de toda a documentação — não
estavam versionados.

**Impacto.** Médio. Sem as planilhas no repositório:

- não é possível reconstruir o estado da fonte a partir do histórico;
- não é possível auditar uma alteração de conteúdo técnico via `git diff`;
- a rastreabilidade descrita em [matriz-rastreabilidade.md](matriz-rastreabilidade.md) aponta para
  arquivos que só existem fora do repositório.

**Para fechar.** Versionar as duas planilhas — por exemplo em `fontes/` — e registrar o hash
SHA-256 de cada uma em [fontes.md](fontes.md) a cada atualização. Os hashes da versão usada nesta
documentação já estão registrados lá.

**Status:** Decisão pendente.

---

## O que **não** ficou pendente

Registrado para evitar releitura desnecessária:

- **Referências cruzadas de IDs:** todos os 13 IDs de cenário citados em `FLUXO_LOGICO` e
  `INDICE_CENARIOS` existem em `TABELA_PRINCIPAL`. Nenhuma referência quebrada.
- **Completude das tabelas principais:** `Tabela Diagnóstico POST` (54 × 16) e `TABELA_PRINCIPAL`
  (13 × 17) estão 100 % preenchidas.
- **Consistência de pinagem:** a medição de 5VSB (pino 9, fio roxo) e o teste paperclip
  (PS_ON pino 16 verde → COM pino 17 preto) são coerentes entre as duas fontes.
- **Versões de terceiros:** MemTest86 v10+ e v4.3.7, ATX12V v2.53, UEFI 2.10 aparecem de forma
  consistente e foram preservadas exatamente como escritas.
- **Identificação do projeto:** nome, proprietário, descrição oficial e licença estão confirmados
  desde `doc-1.1.0` (ver P-01).

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer as limitações estruturais da base | [Limitações](../15-limitacoes.md) |
| vai resolver uma pendência na planilha | [Como contribuir](../../CONTRIBUTING.md) |
| quer registrar a resolução | [Changelog](changelog.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Verificação direta sobre ambos os arquivos-fonte |
| **Status de confiança** | Confirmado — cada pendência verificada contra a origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
