<!-- Gerado a partir de Esta documentação. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Manutenção e rastreabilidade](../../README.md#manutenção-e-rastreabilidade) › **Histórico da documentação**

# Histórico da documentação

> O que mudou em cada versão desta documentação, com o que foi fechado e o que permanece aberto.


**Aplica-se a:** Versionamento da documentação — não do conteúdo técnico das planilhas

## Neste documento

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

Versão do projeto documentado — **não identificada na fonte analisada** (ver [pendencias.md](pendencias.md), P-02).

## Relação com outros documentos

- [Pendências](pendencias.md)
- [Fontes](fontes.md)
- [Arquitetura da documentação](../02-arquitetura.md)

---

> **Atenção ao escopo do versionamento.** Os números abaixo versionam a **documentação**. O
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

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer o que ainda está aberto | [Pendências](pendencias.md) |
| vai registrar uma mudança | [Como contribuir](../../CONTRIBUTING.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Esta documentação |
| **Status de confiança** | Confirmado |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.3.0` |
