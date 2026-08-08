import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs/references"
os.makedirs(OUT, exist_ok=True)

# =========================================================================
# pendencias.md
# =========================================================================
t = doc_header(
    "Pendências e itens que exigem validação humana",
    "Verificação direta sobre ambos os arquivos-fonte",
    "Lista de tudo que não pôde ser resolvido a partir das fontes: informação ausente, informação "
    "conflitante e decisão que só o proprietário do projeto pode tomar. Nada aqui foi preenchido "
    "por suposição.",
    "Pendências classificadas por tipo, com evidência, impacto e o que é necessário para fechar.",
    "Limitações estruturais do material, que estão em [15-limitacoes.md](../15-limitacoes.md).",
    [
        "[Limitações](../15-limitacoes.md)",
        "[Taxonomia de camadas](../03-taxonomia-camadas.md)",
        "[Fontes](fontes.md)",
        "[Matriz de rastreabilidade](matriz-rastreabilidade.md)",
    ],
    secao="manutencao", nivel=1,
    resumo="Tudo que não pôde ser resolvido a partir das fontes: informação ausente, conflitante "
           "ou que exige decisão do proprietário.",
    aplica_se="Planejamento de manutenção da base",
)

t += """## Resumo

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

**Para fechar.** Unificar a numeração na fonte (planilhas) e regerar a documentação, **ou**
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
o aviso de que nenhum nó do fluxo conduz até ela, com link para esta pendência. O aviso é gerado
automaticamente: se um nó passar a referenciar FI-01 na planilha, ele desaparece sozinho.

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

| Aba | Campo | Vazios |
| --- | --- | --- |
| `REF_Victoria` | Atalho de Teclado | 6 de 9 |
| `REF_AIDA64` | Atalho de Teclado | 42 de 45 |
| `REF_AIDA64` | Alternativa Segura | 4 de 45 |
| `REF_MemTest86` | Atalho de Teclado | 8 de 10 |
| `REF_MemTest86` | Alternativa Segura | 6 de 10 |

**Impacto.** Baixo. É plausível que muitas etapas simplesmente não tenham atalho, mas a fonte não
distingue "não existe" de "não preenchido".

**Para fechar.** Preencher com `N/A` onde não houver atalho, para eliminar a ambiguidade.

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

- não é possível regerar a documentação a partir do histórico;
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
"""
t += doc_footer("Verificação direta sobre ambos os arquivos-fonte",
                conf="Confirmado — cada pendência verificada contra a origem", proximos=[
    ("quer as limitações estruturais da base", "[Limitações](../15-limitacoes.md)"),
    ("vai resolver uma pendência na planilha", "[Como contribuir](../../CONTRIBUTING.md)"),
    ("quer registrar a resolução", "[Changelog](changelog.md)"),
])
open(f"{OUT}/pendencias.md", "w").write(t)

# =========================================================================
# changelog.md
# =========================================================================
t = doc_header(
    "Histórico da documentação",
    "Esta documentação",
    "Registro de mudanças **desta base de conhecimento**, não do projeto documentado.",
    "Versões da documentação, escopo de cada geração e origem usada.",
    "Versão do projeto documentado — **não identificada na fonte analisada** "
    "(ver [pendencias.md](pendencias.md), P-02).",
    [
        "[Pendências](pendencias.md)",
        "[Fontes](fontes.md)",
        "[Arquitetura da documentação](../02-arquitetura.md)",
    ],
    secao="manutencao", nivel=1,
    resumo="O que mudou em cada versão desta documentação, com o que foi fechado e o que "
           "permanece aberto.",
    aplica_se="Versionamento da documentação — não do conteúdo técnico das planilhas",
)

t += """> **Atenção ao escopo do versionamento.** Os números abaixo versionam a **documentação**. O
> material de origem não declara versão, e nenhuma foi atribuída a ele. Ver
> [P-02 em pendencias.md](pendencias.md#p-02--versão-do-conteúdo-técnico).

## doc-1.3.0 — 2026-08-07

Navegação centralizada no README e fluxogramas estratégicos. **Sem regressão:** nenhum documento
foi removido, nenhuma ficha perdeu campo, e todas as contagens técnicas permanecem idênticas.

**README como ponto de entrada**

Reescrito para funcionar como central de navegação de toda a base. A partir dele o usuário
identifica a situação, chega ao documento certo e segue até a solução sem abrir arquivo por
arquivo. Passou a conter:

- fluxograma mestre de triagem, do sintoma até o laudo;
- tabela **situação → documento** com 14 entradas;
- seções fixas *Comece aqui*, *Diagnostique*, *Resolva*, *Feche o atendimento*,
  *Opere as ferramentas*, *Consulte a referência* e *Manutenção e rastreabilidade*, cada uma com
  a lista de documentos e o que cada um resolve;
- descrição do padrão que todos os documentos seguem.

**Fluxogramas**

14 fluxogramas em Mermaid, renderizados nativamente pelo GitHub, cobrindo as decisões que cada
documento resolve:

| Documento | O que o fluxograma decide |
| --- | --- |
| `README.md` | Triagem inicial: situação → caminho |
| `docs/00-indice.md` | Mapa de dependência entre os grupos de documentos |
| `docs/02-arquitetura.md` | Os dois eixos, pré-boot e pós-boot |
| `docs/03-taxonomia-camadas.md` | Como identificar qual modelo de camada está sendo lido |
| `docs/04-requisitos-e-ferramentas.md` | Que instrumental separar conforme o estado do equipamento |
| `docs/05-utilizacao.md` | Ordem de leitura para quem chega agora |
| `docs/06-fluxo-post.md` | Etapas 1 a 7 (já existia em `doc-1.2.0`) |
| `docs/07-fluxo-sistemico.md` | Nós F01 a F14 (já existia em `doc-1.2.0`) |
| `docs/08-diagnostico-por-camada.md` | Ordem de verificação das sete camadas |
| `docs/09-codigos-post/00-indice-codigos.md` | Tipo de sinal → família de BIOS → ficha |
| `docs/10-cenarios/00-indice-cenarios.md` | Sintoma → cenário |
| `docs/11-ambiguidades.md` | Critério de desempate por tipo de sinal |
| `docs/12-correlacoes.md` | Quando desconfiar de efeito em cascata |
| `docs/13-validacao-final.md` | Ciclo PASS/FAIL até o laudo |
| `docs/14-ferramentas/00-indice-ferramentas.md` | Qual ferramenta usar |
| `docs/18-indices-cruzados.md` | Por qual eixo buscar |

Os rótulos usam linguagem descritiva ("liga, mas a tela fica preta") em vez de jargão, para que o
fluxo seja legível também por quem não domina a terminologia. O conteúdo integral permanece sempre
abaixo do diagrama, sem cortes.

**Padrão estrutural aplicado a todos os documentos**

- **Trilha de navegação** no topo, de volta ao README e à seção correspondente;
- **Resumo** de uma linha e **Aplica-se a**;
- **Neste documento** — sumário com link para cada seção, gerado automaticamente;
- **Próximos passos** ao final, em tabela *Se você… → Vá para*;
- **Avisos padronizados** em callouts do GitHub, com convenção fixa: `NOTE` para procedência e
  nível de confiança, `TIP` para atalho de navegação, `IMPORTANT` para pré-requisito que muda o
  resultado, `WARNING` para risco de erro de diagnóstico, `CAUTION` para risco elétrico, perda de
  dados ou dano a componente.

**Fichas reorganizadas em fases de procedimento**

As 54 fichas de código e as 13 de cenário passaram a agrupar seus campos nas fases padrão. Nenhum
campo foi renomeado, removido ou reescrito — apenas agrupado:

| Fase | Campos agrupados nas fichas de cenário |
| --- | --- |
| Identificação | Sintoma observado, Camada afetada, Componente suspeito, Condição de ocorrência |
| Pré-requisitos | Dependências, Ordem de execução, Ferramentas oficiais |
| Diagnóstico | Causa raiz, Método de diagnóstico, Comandos técnicos |
| Execução da correção | Procedimento de correção |
| Resultado esperado | Critério de validação técnica, Evidência de sucesso |
| Risco e impacto | Risco associado, Impacto no sistema |
| Origem | Fonte oficial |
| Próximos passos | Referências cruzadas calculadas |

**Duplicação removida**

A tabela de entrada por sintoma existia em `README.md` e em `docs/05-utilizacao.md`. Passou a ter
um único dono — o README, que é o ponto de entrada — e o documento 05 remete a ele, concentrando-se
em ordem de leitura, regras de uso e consulta por agentes de IA. Nenhuma informação foi perdida: a
versão do README é mais completa que a anterior.

**Validador reforçado**

Passou a verificar, além de links e âncoras: trilha de navegação, seção *Próximos passos*, sumário
preenchido, blocos Mermaid balanceados e títulos de nível 2 duplicados no mesmo arquivo. Também
foi acrescentada a etapa `gen9_sumarios.py` ao gerador, que preenche os sumários.

## doc-1.2.0 — 2026-08-07

Expansão de acesso ao conteúdo e empacotamento do gerador. **Sem regressão:** nenhuma ficha
técnica perdeu conteúdo; as contagens de códigos, cenários, camadas, ambiguidades, correlações e
etapas permanecem idênticas.

**Adicionado**

- `docs/18-indices-cruzados.md` — os mesmos registros reagrupados por componente afetado, camada,
  risco declarado, fase do POST, tipo de sinal e ferramenta exigida, mais a cadeia de dependências
  entre cenários. Todos os agrupamentos derivam de colunas de classificação já existentes.
- `docs/19-comandos.md` — os comandos da coluna `Comandos Técnicos` reunidos, com camada, risco e
  link para a ficha.
- **Referências cruzadas calculadas** ao fim de cada ficha: código → ficha da camada e aviso de
  ambiguidade; camada → códigos atribuídos a ela; cenário → nós do fluxo que o alcançam,
  dependências e cenários dependentes.
- **Diagramas Mermaid** dos dois fluxos, em `06-fluxo-post.md` e `07-fluxo-sistemico.md`,
  reproduzindo a topologia das colunas de encadeamento.
- `tools/gerar_documentacao.py` e `tools/gerador/` — o gerador que reconstrói a documentação a
  partir das planilhas, até então externo ao repositório.
- `CONTRIBUTING.md` — regras de conteúdo, fluxo de alteração e mapa arquivo → script.
- Rodapé de cada documento passou a registrar autoria e versão da documentação.

**Corrigido**

Duas siglas estavam marcadas como não expandidas pela fonte quando a fonte as expande:

| Sigla | Antes | Agora |
| --- | --- | --- |
| SPD | "expansão não fornecida" | **Serial Presence Detect** — expandida em `REF_AIDA64` |
| DXE | "expansão não fornecida" | **Driver Execution Environment** — expandida em `Tabela Diagnóstico POST` |

**Glossário expandido** de 31 para 43 termos. Os 12 novos têm expansão fornecida pela própria
fonte: ACPI, BDA/IVT, DXE, G-List, GOP, HMM, KBC, ME, OCP, Row Hammer, TPM e WinDbg. Acrescentada
também a seção *Termos usados sem definição na fonte*, que registra explicitamente BIST,
XMP/EXPO/DOCP, SEC, PEI, OPP e PSREF como não expandidos.

**Autoria**

Autor do projeto registrado como **Edsilas** em `README.md`, `docs/01-visao-geral.md`,
`CONTRIBUTING.md` e no rodapé de todos os documentos.

## doc-1.1.0 — 2026-08-07

Identificação oficial do projeto. **Sem regressão:** nenhum conteúdo técnico foi alterado,
removido ou reescrito. As contagens, os textos das fichas e a estrutura de arquivos permanecem
idênticos a `doc-1.0.0`.

**Alterado**

- Nome do projeto: identificador provisório `HW_HARDWARE` substituído por
  **Base de Diagnóstico de Hardware** (`base-diagnostico-hardware`).
- `README.md`: título, descrição oficial, licença, instruções de clonagem, seção de manutenção
  e créditos.
- `01-visao-geral.md`: nova seção *Identidade oficial*; a tabela de metadados passou a distinguir
  o que as planilhas declaram do que foi confirmado pelo repositório.
- `references/fontes.md`: Níveis 2 e 3 preenchidos com o repositório oficial e as informações dele
  extraídas.
- `references/matriz-rastreabilidade.md`: nível de confiança de `README.md` e `01-visao-geral.md`
  elevado; inferência do nome substituída por fonte confirmada.

**Adicionado**

- `tools/validar_documentacao.py` — validador de links internos, âncoras, cabeçalhos de contexto
  e rodapés de fonte.
- `.github/workflows/validar-docs.yml` — executa o validador a cada push que toque `docs/`.
- `.gitignore`.
- Pendência **P-17**: planilhas de origem não versionadas no repositório.

**Fechado**

- **P-01 — Nome oficial do projeto.** Confirmado por consulta ao repositório informado pelo
  proprietário.
- **P-02, parcialmente.** Autor (`edsilas`) e licença (MIT) confirmados; a versão do conteúdo
  técnico permanece aberta.

**Fonte da atualização**

Repositório `https://github.com/edsilas/base-diagnostico-hardware`, consultado em 2026-08-07.
Estado no momento da consulta: público, branch `main`, 1 commit, arquivos `LICENSE` e `README.md`.

## doc-1.0.0 — 2026-08-07

Geração inicial da base de conhecimento a partir de dois arquivos `.xlsx`.

**Adicionado**

- Estrutura modular com 18 documentos de nível raiz e 3 diretórios temáticos.
- Catálogo de 54 códigos de POST, dividido em 11 arquivos por família de BIOS.
- 13 fichas de cenário de falha, agrupadas em 9 arquivos.
- Fluxo de POST (7 etapas) e fluxo sistêmico (17 nós).
- Fichas das 7 camadas de diagnóstico do modelo POST.
- 5 casos de ambiguidade e 6 correlações em cascata.
- Matriz de validação final com 10 componentes.
- Guias operacionais de Victoria (9 etapas), MemTest86 (10 etapas + critérios) e AIDA64
  (45 etapas, em 3 arquivos).
- Glossário com 31 termos e o bloco de siglas de fase do POST.
- Rastreabilidade completa em `references/`.

**Registrado como conflito (não resolvido)**

- Duas taxonomias de camada incompatíveis entre os arquivos-fonte.
- Divergências de *power drain*, *boot mínimo* e limiares térmicos.

Detalhamento em [pendencias.md](pendencias.md).

**Decisões de documentação**

- Documentos técnicos gerados programaticamente a partir das células, sem redação intermediária.
- Identificador `POST-NN` criado para link estável, sempre acompanhado do código literal.
- Campos vazios na origem marcados como *"Informação não identificada na fonte analisada"*.
- Nenhuma consulta a fonte externa.
- Única normalização aplicada ao texto de origem: o número da etapa dos guias de ferramentas, que
  o Excel armazena como decimal (`4.0`), é exibido como inteiro (`4`). Nenhum outro valor foi
  reformatado.

**Origem**

| Arquivo | Abas | Registros |
| --- | --- | --- |
| `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` | 4 | 73 |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | 8 | 119 |

**Autoria**

Documentação de autoria de Edsilas, derivada de planilhas de sua autoria.

## Convenção de versionamento desta documentação

- **maior** (`2.0.0`): mudança estrutural — arquivos renomeados, removidos ou reorganizados.
- **menor** (`1.1.0`): conteúdo novo, pendência fechada, documento acrescentado.
- **correção** (`1.0.1`): correção de link, formatação ou erro de transcrição.

## Como registrar mudanças futuras

1. Alterar o conteúdo técnico **na planilha**, não no Markdown.
2. Regerar os documentos derivados.
3. Acrescentar aqui uma entrada com: versão, data, o que mudou, qual aba mudou e se alguma
   pendência foi fechada.
4. Se uma pendência de [pendencias.md](pendencias.md) for resolvida, marcá-la como fechada em vez
   de removê-la, preservando o histórico da decisão.
"""
t += doc_footer("Esta documentação", conf="Confirmado", proximos=[
    ("quer o que ainda está aberto", "[Pendências](pendencias.md)"),
    ("vai registrar uma mudança", "[Como contribuir](../../CONTRIBUTING.md)"),
])
open(f"{OUT}/changelog.md", "w").write(t)
print("pendencias e changelog gerados")
