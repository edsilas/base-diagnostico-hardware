<!-- Gerado a partir de Verificação direta sobre ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Manutenção e rastreabilidade](../../README.md#manutenção-e-rastreabilidade) › **Pendências e itens que exigem validação humana**

# Pendências e itens que exigem validação humana

> Tudo que não pôde ser resolvido a partir das fontes: informação ausente, conflitante ou que exige decisão do proprietário.


**Aplica-se a:** Planejamento de manutenção da base

## Neste documento

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

## Resumo

| # | Pendência | Tipo | Severidade |
| --- | --- | --- | --- |
| ~~P-01~~ | ~~Nome oficial do projeto~~ | Ausência | **FECHADA em doc-1.1.0** |
| P-02 | Versão do conteúdo técnico | Ausência | Média |
| P-03 | Duas taxonomias de camada incompatíveis | Conflito | Alta |
| P-04 | Modelo de camadas B sem tabela de definição | Ausência | Alta |
| P-05 | Duração do *power drain*: 30 s vs 10 s | Conflito | Média |
| P-06 | Composição do *boot mínimo* divergente | Conflito | Média |
| P-07 | Limiar térmico em idle: 60 °C vs 90 °C | Conflito | Média |
| P-08 | Critério FAIL de temperatura: 95 °C vs 90 °C | Conflito | Média |
| P-09 | FI-01 inalcançável pelo fluxo sistêmico | Inconsistência | Média |
| P-10 | Beep contínuo de teclado (AMI) sem ficha no catálogo | Lacuna | Média |
| P-11 | Lenovo SmartBeep sem procedimento | Lacuna | Baixa |
| P-12 | Campos `Atalho de Teclado` e `Alternativa Segura` vazios | Lacuna | Baixa |
| P-13 | Bloco de critérios do MemTest86 fora da estrutura de etapas | Estrutura | Baixa |
| P-14 | Nós F06 e F08 sem cenário associado | Estrutura | Baixa |
| P-15 | Referências externas citadas mas não verificadas | Verificação | Média |
| P-16 | Identificador `POST-NN` criado por esta documentação | Decisão | Baixa |
| P-17 | Planilhas de origem não versionadas no repositório | Rastreabilidade | Média |

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

**Status:** Necessita validação.

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

**O que foi feito.** Nenhum modelo foi escolhido. Ambos estão documentados em
[03-taxonomia-camadas.md](../03-taxonomia-camadas.md), e todo número de camada é reproduzido no
formato original, que identifica o modelo.

**Para fechar.** Unificar a numeração na fonte (planilhas) e propagar a correção para a
documentação, **ou**
declarar formalmente que os dois modelos coexistem por escopo distinto.

**Status:** Necessita validação.

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

**Status:** Necessita validação.

---

## P-05 — Duração do *power drain*

**Situação.**

| Fonte | Instrução literal |
| --- | --- |
| `CODIGOS_DE_ERROS` → `Tabela Diagnóstico POST` | "Power drain completo (desligar, remover cabo AC, segurar power 30s)" e "Segurar botão power 30 segundos (descarga capacitores)" |
| `FLUXO_DIAGNOSTICO` → `TABELA_PRINCIPAL` (NL-01) | "Descarregar capacitores residuais (pressionar Power 10s com cabo desconectado)" |

**Impacto.** Médio. Descarga insuficiente pode manter tensão residual durante a manipulação.

**Para fechar.** Definir a duração de referência e uniformizar nas duas planilhas.

**Status:** Necessita validação. Ambas as versões estão preservadas nos documentos.

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

**Status:** Necessita validação.

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

**Status:** Necessita validação.

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

**Status:** Necessita validação.

---

## P-09 — FI-01 inalcançável pelo fluxo sistêmico

**Situação.** O ID `FI-01` (*Falhas intermitentes*) existe em `TABELA_PRINCIPAL` e em
`INDICE_CENARIOS`, mas **nenhum nó de `FLUXO_LOGICO` o referencia**. Todos os outros 12 IDs são
alcançados por pelo menos um nó.

**Impacto.** Médio. Quem seguir apenas o fluxo nunca chega ao cenário de falhas intermitentes.

**Para fechar.** Acrescentar ao fluxo um nó que conduza a FI-01, ou documentar que o cenário é de
entrada direta pelo índice.

**Mitigação aplicada em `doc-1.2.0`.** A ficha de FI-01 passou a exibir, nas referências cruzadas,
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

**Para fechar.** Documentar as melodias e seus significados, se essa informação existir.

**Status:** Necessita validação.

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

> [!NOTE]
> **Correção aplicada em `doc-1.4.0`.** As duas linhas de `REF_MemTest86` registravam *8 de 10* e
> *6 de 10*. A contagem campo a campo sobre
> [memtest86.md](../14-ferramentas/memtest86.md) — as dez etapas do procedimento — devolve **7** e
> **5**: os atalhos faltam nas etapas 1, 4, 5, 6, 7, 8 e 10; a alternativa segura falta nas
> etapas 2, 4, 5, 6 e 10. As linhas de `REF_Victoria` e `REF_AIDA64` conferem exatamente.
>
> A diferença é de **+1 em ambos os campos**, o que é compatível com uma contagem feita sobre as
> onze linhas de conteúdo da aba — as dez etapas mais o bloco de critérios de decisão descrito em
> [P-13](#p-13--bloco-de-critérios-do-memtest86-fora-da-estrutura), cujos campos também estão
> vazios. **Essa explicação não pôde ser confirmada**, porque a planilha não está versionada
> ([P-17](#p-17--planilhas-de-origem-não-versionadas-no-repositório)). O registro passou a trazer o
> valor verificável na documentação; a conferência contra a célula continua pendente.

**Impacto.** Baixo. É plausível que muitas etapas simplesmente não tenham atalho, mas a fonte não
distingue "não existe" de "não preenchido".

**Para fechar.** Preencher com `N/A` onde não houver atalho, para eliminar a ambiguidade, e
confirmar contra a planilha se o denominador correto de `REF_MemTest86` são as 10 etapas ou as 11
linhas de conteúdo da aba.

**Status:** Necessita validação. Nos documentos, esses campos exibem
*"Informação não identificada na fonte analisada"*.

---

## P-13 — Bloco de critérios do MemTest86 fora da estrutura

**Situação.** A última linha de `REF_MemTest86` não é uma etapa: é um bloco de critérios de decisão
pós-teste ocupando a coluna `Nº da Etapa`.

**Impacto.** Baixo, mas quebra a estrutura tabular da aba e prejudica processamento automático.

**O que foi feito.** O bloco foi extraído e apresentado como seção própria, com aviso explícito,
em [memtest86.md](../14-ferramentas/memtest86.md).

**Para fechar.** Mover o bloco para uma aba ou coluna própria na planilha.

**Status:** Necessita validação.

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
outras. Nenhuma foi confrontada com o documento original.

**Impacto.** Médio. As referências sustentam afirmações técnicas específicas (valores de tensão,
tolerância de ripple, intervalos de refresh).

**Para fechar.** Verificar cada referência contra o documento oficial e elevar o nível de confiança
de "Não confirmado" para "Oficial" onde a verificação for bem-sucedida.

**Status:** Não confirmado. A lista está em [fontes.md](fontes.md).

---

## P-16 — Identificador `POST-NN` criado por esta documentação

**Situação.** Os códigos de POST não têm identificador na fonte. Para permitir link estável entre
documentos, foi criado o identificador `POST-01` … `POST-54`, seguindo a ordem das linhas.

**Impacto.** Baixo, mas com um risco de manutenção: inserir uma linha no meio da planilha
**desloca todos os identificadores seguintes**.

**Para fechar.** Adotar uma coluna `ID` na planilha de origem, com valores estáveis, e passar a
gerar a documentação a partir dela.

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
