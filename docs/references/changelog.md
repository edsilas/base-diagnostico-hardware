<!-- Gerado a partir de Esta documentação. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Manutenção e rastreabilidade](../../README.md#manutenção-e-rastreabilidade) › **Histórico da documentação**

# Histórico da documentação

> O que mudou em cada versão desta documentação, com o que foi fechado e o que permanece aberto.


**Aplica-se a:** Versionamento da documentação — não do conteúdo técnico das planilhas

## Neste documento

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

Registro de mudanças **desta base de conhecimento**, não do projeto documentado.

## Escopo

Versões da documentação, escopo de cada geração e origem usada.

## Fora do escopo

Conteúdo técnico em si; origem campo a campo, que está em
[matriz-rastreabilidade.md](matriz-rastreabilidade.md).

## Relação com outros documentos

- [Fontes](fontes.md)
- [Matriz de rastreabilidade](matriz-rastreabilidade.md)
- [Arquitetura da documentação](../02-arquitetura.md)

---

> **Escopo do versionamento.** A partir de `doc-2.0.0`, o número versiona o conjunto publicado —
> estrutura **e** conteúdo técnico. A convenção está em
> [Arquitetura da documentação](../02-arquitetura.md#versionamento-do-conteúdo).

## doc-2.0.0 — 2026-08-08

Consolidação da base. As divergências que antes eram apenas registradas passaram a ser
**resolvidas contra documentação oficial**, e a decisão foi incorporada ao ponto de uso. Os
registros temporários de acompanhamento — a lista de pendências e o documento de limitações —
deixaram de existir: o que neles era problema em aberto virou conteúdo; o que era fronteira de
escopo foi para [Visão geral](../01-visao-geral.md#fronteiras-de-cobertura); o que era precaução
virou [Segurança e boas práticas](../15-seguranca-e-boas-praticas.md).

**Sem regressão:** nenhuma ficha técnica perdeu campo, e todas as contagens permanecem idênticas —
54 códigos, 13 cenários, 7 etapas de POST, 17 nós, 5 ambiguidades, 6 correlações, 10 componentes de
validação e 64 etapas de ferramentas.

### Divergências resolvidas

Cada linha foi decidida contra a publicação de quem edita o documento de referência. O registro
completo das consultas está em
[fontes.md](fontes.md#verificações-independentes-realizadas).

| Divergência | Como estava | Decisão adotada |
| --- | --- | --- |
| Duração da descarga de energia residual | 30 s em um arquivo, 10 s no outro | **30 s.** Dell publica 15–20 s e HP publica ≈15 s; 30 s satisfaz e supera todos os mínimos publicados, e 10 s fica abaixo de qualquer um deles |
| Composição do *boot mínimo* | Três definições literais concorrentes | **Duas composições nomeadas** — *absoluto* e *com vídeo* —, com o cooler obrigatório nas duas, porque o controle térmico da CPU atua já na faixa de Tjunction max declarada pela Intel |
| Limiar térmico em repouso | 60 °C em um registro, 90 °C em outro | **Escala de dois estágios:** 60 °C abre a investigação, 90 °C confirma a falha térmica |
| Critério FAIL de temperatura | 95 °C na linha *CPU*, 90 °C na linha *Térmico* | **Sujeitos diferentes.** 95 °C julga a CPU como peça; 90 °C julga o subsistema de refrigeração. Para liberar o equipamento prevalece o mais restritivo |

### Corrigido

| Onde | Antes | Agora |
| --- | --- | --- |
| [fontes.md](fontes.md) | Citação *ATX12V PSU Design Guide v2.53* | Identificada como capítulo *ATX12V Specific Guidelines* do documento Intel nº 336521 — o título citado não corresponde a nenhum documento autônomo |
| [fontes.md](fontes.md) | UEFI Specification 2.10 como referência corrente | Registrada a versão vigente: **2.11**, de dezembro de 2024 |
| [fontes.md](fontes.md) | JEDEC JESD79-5 sem revisão | Registrada a revisão mais recente: **JESD79-5D**, de novembro de 2025 |
| [09-codigos-post/lenovo.md](../09-codigos-post/lenovo.md) | Procedimento do SmartBeep sem o passo de reemissão | Acrescentado o passo oficial de **pressionar Fn** para reemitir o bipe, conforme o manual do fabricante |
| [14-ferramentas/memtest86.md](../14-ferramentas/memtest86.md) | Bateria padrão descrita como 13 algoritmos | Registrada a contagem oficial: **testes 0 a 13 — quatorze**, sendo o 13 o *Hammer Test* |
| [16-faq.md](../16-faq.md) | Resposta afirmava que autor e versão não estavam identificados | Corrigida: contradizia o README e o documento 01, que declaram autoria e licença desde `doc-1.1.0` |
| [17-glossario.md](../17-glossario.md) | SEC, PEI, BIST, XMP/EXPO/DOCP e PSREF sem expansão | Expansões confirmadas em fonte oficial e incorporadas |

### Acrescentado

- [15-seguranca-e-boas-praticas.md](../15-seguranca-e-boas-praticas.md) — descarga de energia
  residual, proteção contra descarga eletrostática, medição com o equipamento energizado,
  procedimentos destrutivos, leitura dos limiares térmicos e registro do atendimento. Cobre a
  lacuna de orientação de segurança que a base antes apenas declarava.
- Ficha de referência das **10 camadas do modelo sistêmico** em
  [03-taxonomia-camadas.md](../03-taxonomia-camadas.md), com componentes, cenários de entrada,
  primeiro teste e ferramentas — o equivalente, para esse modelo, do que o documento 08 oferece
  para o modelo POST.
- **Regra de entrada do cenário FI-01** em [07-fluxo-sistemico.md](../07-fluxo-sistemico.md):
  o cenário é alcançado a partir de F08 quando a instabilidade não se reproduz sob demanda em F09,
  F09b e F09c. O cenário deixou de ser inalcançável pelo fluxo.
- Arquivo [`LICENSE`](../../LICENSE) na raiz, com o texto MIT que o README já referenciava.
- Registro das **verificações independentes** em
  [fontes.md](fontes.md#verificações-independentes-realizadas).

### Terminologia unificada

Os rótulos *modelo A* e *modelo B* foram substituídos por **modelo POST** e **modelo sistêmico**,
que dizem o escopo de cada um em vez de exigir a memorização de uma letra. A troca é de rótulo: os
números, os nomes das camadas e a notação literal (`Camada N: NOME` e `N - Nome`) permanecem
idênticos.

### Removido

| Removido | Para onde foi |
| --- | --- |
| `docs/references/pendencias.md` | Divergências resolvidas acima; verificações em [fontes.md](fontes.md); decisões de convenção em [02-arquitetura.md](../02-arquitetura.md) |
| `docs/15-limitacoes.md` | Fronteiras de cobertura em [01-visao-geral.md](../01-visao-geral.md#fronteiras-de-cobertura); precauções em [15-seguranca-e-boas-praticas.md](../15-seguranca-e-boas-praticas.md) |

Nenhum fato foi descartado no processo: cada item das duas listas foi resolvido, incorporado a um
documento definitivo ou registrado neste histórico.

## doc-1.4.0 — 2026-08-07

Revisão de integridade da documentação: três divergências entre documentos foram corrigidas, uma
contradição foi resolvida e o material passou a ser autossuficiente para publicação. **Sem
regressão:** nenhum documento foi removido ou renomeado, nenhuma ficha perdeu campo, e todas as
contagens técnicas — 54 códigos, 13 cenários, 7 etapas de POST, 17 nós, 5 ambiguidades,
6 correlações, 10 componentes de validação, 43 termos, 64 etapas de ferramentas — permanecem
idênticas a `doc-1.3.0`.

**Corrigido**

| Onde | Antes | Agora |
| --- | --- | --- |
| `P-12` e `15-limitacoes.md` | `REF_MemTest86`, Atalho de Teclado: 8 de 10 | **7 de 10** |
| `P-12` e `15-limitacoes.md` | `REF_MemTest86`, Alternativa Segura: 6 de 10 | **5 de 10** |
| [matriz-rastreabilidade.md](matriz-rastreabilidade.md) | Camadas do modelo B observadas: 9 números (1–7, 9, 10) | **10 números (1–10)** |

A contagem de `REF_MemTest86` foi refeita campo a campo sobre as dez etapas de
[memtest86.md](../14-ferramentas/memtest86.md): faltam atalhos nas etapas 1, 4, 5, 6, 7, 8 e 10, e
alternativa segura nas etapas 2, 4, 5, 6 e 10. `REF_Victoria` (6 de 9) e `REF_AIDA64` (42 de 45 e
4 de 45) conferiam e não foram alteradas. O desvio de +1 em ambos os campos é compatível com uma
contagem sobre as onze linhas de conteúdo da aba — as dez etapas mais o bloco de critérios de
`P-13`, cujos campos também
estão vazios —, mas **isso não pôde ser confirmado** sem a planilha, e ficou registrado como
hipótese, não como fato.

A contagem do modelo B contradizia [03-taxonomia-camadas.md](../03-taxonomia-camadas.md),
`P-04` e
`15-limitacoes.md`, que documentam dez camadas — a 8 (*Periféricos*) aparece
em `CORRELACOES`. A matriz era o único documento a omiti-la.

**Contradição resolvida**

[02-arquitetura.md](../02-arquitetura.md), em *Como manter*, e
[CONTRIBUTING.md](../../CONTRIBUTING.md) davam orientações opostas sobre a edição dos documentos
redigidos. As duas páginas foram alinhadas: documentos derivados têm o valor técnico corrigido na
planilha; documentos redigidos podem ser editados diretamente, sem afirmação nova sem fonte.

**Reorganizado**

- `README.md`: seção **Como esta base é mantida**, que dá cabeçalho a um parágrafo que estava
  órfão entre *Limitações relevantes* e *Licença*, e resume as três regras que sustentam a
  confiabilidade do material. A árvore do repositório passou a refletir exatamente o que é
  publicado.
- `CONTRIBUTING.md`: reorganizado em cinco blocos — separação entre documentos derivados e
  redigidos, padrão estrutural, regras de conteúdo, fluxo de alteração e pendências abertas. Ganhou
  sumário próprio, links diretos para cada documento citado e uma lista de conferência antes de
  publicar. As regras de conteúdo, o significado dos callouts, a ordem das fases das fichas e as
  convenções de fluxograma foram preservadas sem alteração.
- A documentação passou a ser **autossuficiente**: não depende de nenhum recurso externo ao
  repositório para ser lida, conferida ou publicada.

**Pendências verificadas em fonte oficial**

Duas pendências avançaram por conferência contra a documentação de quem publica cada referência.
Nenhuma informação externa entrou nas fichas técnicas: a conferência apura a **identidade** do
documento citado, não o conteúdo atribuído a ele.

| Pendência | O que foi apurado |
| --- | --- |
| `P-11` | A Lenovo **não publica** tabela de melodia → significado do SmartBeep; a decodificação é feita pelo aplicativo. O manual oficial descreve um passo que a base não registrava: pressionar **Fn** para reemitir o bipe |
| `P-15` | UEFI 2.10 e JEDEC JESD79-4/79-5 confirmadas. A citação *ATX12V PSU Design Guide v2.53* nomeia um documento inexistente sob esse título: o correto é o capítulo *ATX12V Specific Guidelines 2.53* do guia de fontes da Intel (documento nº 336521). AMI, Phoenix e Award não são verificáveis como citadas, por falta de número e versão |

`pendencias.md` ganhou a seção *Como ler esta lista*, que define os campos de cada ficha e os
quatro valores de **Status**; a tabela-resumo passou a trazer o status de cada item e link direto
para a ficha correspondente. [fontes.md](fontes.md) e
[matriz-rastreabilidade.md](matriz-rastreabilidade.md) registram a conferência sem alterar a
declaração de que nenhuma fonte de fabricante alimentou o conteúdo técnico.

**Navegação unificada**

A base usava três vocabulários diferentes para os mesmos grupos de documento: os sete nomes do
[README](../../README.md) — que são os mesmos da trilha que abre cada página —, dez nomes na seção
*Documentos* de [00-indice.md](../00-indice.md) e onze num bloco *Ordem lógica* do mesmo arquivo.
Quem chegava por uma trilha *Início › Resolva › …* não encontrava "Resolva" no índice.

- `00-indice.md` passou a usar **exclusivamente os sete nomes canônicos**, na seção
  *Todos os documentos*. Os rótulos do fluxograma do mapa foram alinhados aos mesmos sete.
- O bloco *Ordem lógica* foi retirado: era um terceiro vocabulário que repetia o catálogo logo
  abaixo. A ordem de leitura tem dono único —
  [05-utilizacao.md](../05-utilizacao.md#ordem-de-leitura-para-quem-está-chegando-agora) —, para
  onde o índice agora remete.
- Em `05-utilizacao.md`, a seção *Entrada por sintoma* era um título sem conteúdo, apenas com um
  aviso de redirecionamento. Virou *Onde entrar conforme o sintoma*, que declara o que a página
  cobre e o que fica no README.

**Segurança e aplicação prática**

O README levava direto do sintoma ao procedimento, sem nada entre a triagem e a execução. Nova
seção **Antes de executar qualquer procedimento**, com o que conferir antes de encostar no
equipamento: o risco declarado da ficha, os pré-requisitos e o instrumental. Traz um aviso
`> [!CAUTION]` sobre medição energizada, manipulação de fonte e regravação de firmware, e registra
que a escala de risco é ordem relativa — a fonte não define o significado dos níveis.

A tabela de triagem ganhou uma coluna intermediária, *Como isso costuma aparecer*, com a
manifestação observável de cada situação, e três entradas novas: visor de dois caracteres, LED
piscando em cores alternadas e melodia no lugar de bipes. Todas as pistas citadas — `00`, `B4`,
`FF`, *1 longo + 2 curtos*, *1-1-1-3*, *2 âmbar + 1 branco*, LEDs CPU/DRAM/VGA/BOOT — são valores
literais das fichas correspondentes.

**Limitações conhecidas reestruturado**

`15-limitacoes.md` foi reorganizado para leitura por quem não conhece a
estrutura interna das planilhas. Os **oito grupos originais foram mantidos**, com os mesmos
títulos e âncoras; nenhum fato, valor ou link foi perdido.

- Três seções novas: *Para que serve esta página*, *O que exige atenção antes de decidir* — as
  quatro limitações que podem mudar um diagnóstico — e *Quando consultar outro documento*.
- Cada grupo passou a declarar **tipo** (informação ausente, conflito entre fontes, divergência
  não resolvida, anomalia da fonte, cobertura ausente, limitação de uso, limitação da
  documentação) e **estado** (confirmado, não identificado, conflitante, não verificado,
  pendente), com legenda própria.
- Cada grupo segue agora **Situação → Impacto → Como proceder**, e cada limitação individual
  aponta para a pendência correspondente: 15 âncoras diretas, contra 3 links genéricos antes.
- Parágrafos densos das seções 5, 6 e 7 viraram tabelas; termos técnicos ganharam explicação na
  primeira ocorrência (*power drain*, *boot mínimo*, `docProps/core.xml`).

**Corrigido em `15-limitacoes.md`**

| Onde | Antes | Agora |
| --- | --- | --- |
| Seção 1 | Nome, autor e licença listados como *"Não identificada"*, sem ressalva | Coluna *Situação atual* distingue o que falta na planilha do que foi confirmado fora dela (`P-01`, `P-02`) |
| Seção 3 | "ambas as versões", para quatro divergências — e o *boot mínimo* tem **três** definições | Redação corrigida, com nota explicitando que a linha condensa três definições (`P-06`) |
| Seção 8 | "Não houve consulta a fontes externas" | Corrigido: registra as duas conferências bibliográficas de `doc-2.0.0` e mantém, em destaque, que **nenhuma informação técnica veio de documentação de fabricante** |

A seção 1 dizia que o nome do projeto não estava identificado, enquanto P-01 está fechada desde
`doc-1.1.0` e o README declara autor e licença — a página era o único documento a não registrar
isso. A seção 8 contradizia [fontes.md](fontes.md),
[matriz-rastreabilidade.md](matriz-rastreabilidade.md) e as pendências P-11 e P-15, atualizadas
nesta mesma versão.

**Preservado**

Fichas de código, de cenário e de ferramenta, fluxogramas de diagnóstico, índices cruzados e
glossário não foram tocados, exceto pelo carimbo de versão no rodapé. Nenhuma linha do catálogo de
documentos foi perdida no reagrupamento: os mesmos arquivos continuam listados, sob os sete nomes.
Em `15-limitacoes.md`, os 8 links originais continuam presentes e as âncoras da versão anterior
continuam resolvendo.

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

**Sumários preenchidos**

A seção *Neste documento* passou a listar, em todos os documentos, as seções de conteúdo do
arquivo, com link para cada uma.

## doc-1.2.0 — 2026-08-07

Expansão de acesso ao conteúdo. **Sem regressão:** nenhuma ficha
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
- `CONTRIBUTING.md` — regras de conteúdo, padrão dos documentos e fluxo de alteração.
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

Detalhamento em `pendencias.md`.

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
2. Trazer a correção para os documentos derivados, preservando a transcrição literal da célula.
3. Acrescentar aqui uma entrada com: versão, data, o que mudou, qual aba mudou e se alguma
   pendência foi fechada.
4. Se uma divergência entre fontes for resolvida, registrar aqui **qual valor foi adotado e contra
   qual documento oficial**, e incorporar a decisão ao ponto de uso — não a um registro separado.

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer conferir a origem de uma informação | [Fontes](fontes.md) |
| vai registrar uma mudança | [Como contribuir](../../CONTRIBUTING.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Esta documentação |
| **Status de confiança** | Confirmado |
| **Última verificação contra a fonte** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
