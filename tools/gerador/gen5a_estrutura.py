import os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
cod = read(F_COD)
flu = read(F_FLU)

post = cod["Tabela Diagnóstico POST"][3:]
fam = collections.Counter(r[0] for r in post)
sinal = collections.Counter(r[2] for r in post)

# =========================================================================
# 03 — Taxonomia de camadas (documento de conflito)
# =========================================================================
SRC = "Ambos os arquivos-fonte (ver corpo do documento)"
cd = cod["Camadas de Diagnóstico"]
camadas_a = [(r[0], r[1]) for r in cd[2:]]

# Modelo B reconstruído a partir do uso literal nas células
usos_b = {}
for sh in ["TABELA_PRINCIPAL", "INDICE_CENARIOS", "CORRELACOES", "FLUXO_LOGICO"]:
    for r in flu[sh]:
        for c in r:
            for m in re.finditer(r"(\d{1,2})\s*-\s*([A-Za-zÀ-ÿ]+(?:-[A-Za-zÀ-ÿ]+)?)", c):
                n, nome = m.group(1), m.group(2)
                if nome.lower() in {"energia", "firmware", "cpu", "memória", "armazenamento",
                                    "gpu", "placa", "placa-mãe", "periféricos", "so", "drivers"}:
                    if nome.lower().startswith("placa"):
                        nome = "Placa-mãe"
                    usos_b.setdefault(int(n), {"nome": nome, "abas": set()})["abas"].add(sh)

t = doc_header(
    "Taxonomia de camadas — dois modelos coexistentes",
    SRC,
    "As duas planilhas-fonte usam a palavra **camada** com numerações diferentes e incompatíveis. "
    "Este documento registra os dois modelos, indica onde cada um é usado e alerta para o risco de "
    "leitura cruzada equivocada. É leitura obrigatória antes de usar qualquer número de camada.",
    "Definição, origem e alcance de cada modelo de camadas; tabela de equivalência possível; "
    "regra de uso adotada nesta documentação.",
    "Detalhamento técnico das camadas (ver documento 08); fichas de código; cenários.",
    [
        "[Diagnóstico por camada (modelo POST)](08-diagnostico-por-camada.md)",
        "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md) — usa o modelo A",
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md) — usa o modelo B",
        "[Correlações entre camadas](12-correlacoes.md) — usa o modelo B",
        "[Pendências](references/pendencias.md)",
    ],
    secao="comecar", nivel=0,
    resumo="Os dois arquivos-fonte numeram as camadas de forma incompatível. Leia antes de usar "
           "qualquer número de camada.",
    aplica_se="Toda a documentação — os números de camada aparecem em códigos, cenários e correlações",
)

t += """> [!CAUTION]
> O número de uma camada **não significa a mesma coisa** nos dois arquivos-fonte.
> Exemplo: **camada 3** é *Memória* no modelo A e *CPU* no modelo B. Usar o número errado leva a
> testar o subsistema errado.
>
> A documentação **não escolhe** um dos modelos como correto: preserva ambos, identifica a origem
> de cada um e exige que o número da camada venha sempre acompanhado do modelo.
>
> **Status: Necessita validação** pelo proprietário do projeto —
> [P-03 em pendências](references/pendencias.md).

## Como saber qual modelo estou lendo

O formato do texto identifica o modelo. Não é preciso decorar as duas listas.

```mermaid
flowchart TD
    A(["Você encontrou um<br/>número de camada"]) --> B{"Como ele<br/>está escrito?"}
    B -->|"Camada 3: Memória<br/>(com a palavra 'Camada'<br/>e dois-pontos)"| MA["MODELO A — 7 camadas<br/>Escopo: POST"]
    B -->|"3 - CPU<br/>(número, hífen, nome)"| MB["MODELO B — camadas do fluxo<br/>Escopo: sistêmico"]

    MA --> MA1["Fichas de código de POST<br/>Fichas de camada"]
    MB --> MB1["Fichas de cenário<br/>Correlações<br/>Índice de cenários"]

    MA1 --> Z(["Use a lista do modelo<br/>correspondente, abaixo"])
    MB1 --> Z
```

> [!TIP]
> Regra prática: se o texto começa com a palavra **Camada**, é o modelo de 7 camadas do POST.
> Se começa com o número seguido de hífen, é o modelo do fluxo sistêmico.

## Modelo A — 7 camadas (escopo POST)

**Origem:** `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx`, abas `Camadas de Diagnóstico` (tabela de definição)
e `Tabela Diagnóstico POST` (coluna `CAMADA DE DIAGNÓSTICO`).
**Formato literal na fonte:** `Camada N: Nome`.
**Status: Confirmado** — existe tabela de definição explícita.

| Nº | Nome (literal na fonte) |
| --- | --- |
"""
for n, nome in camadas_a:
    t += f"| {tcell(n)} | {tcell(nome)} |\n"

t += """
Ficha técnica completa de cada camada: [08-diagnostico-por-camada.md](08-diagnostico-por-camada.md).

## Modelo B — camadas do fluxo sistêmico

**Origem:** `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx`, colunas `Camada Afetada` (`TABELA_PRINCIPAL`),
`Camada Primária` (`INDICE_CENARIOS`) e `Falha Primária / Efeito Cascata` (`CORRELACOES`).
**Formato literal na fonte:** `N - Nome` ou `N-Nome`.
**Status: Reconstruído a partir do uso.** Não existe, em nenhuma das abas, uma tabela que defina
este modelo. A lista abaixo foi montada varrendo todas as ocorrências literais nas células.

| Nº | Nome (literal na fonte) | Abas onde aparece |
| --- | --- | --- |
"""
for n in sorted(usos_b):
    t += f"| {n} | {tcell(usos_b[n]['nome'])} | {', '.join(sorted(usos_b[n]['abas']))} |\n"

t += """
> As camadas do modelo B **não possuem ficha técnica** equivalente ao documento 08: a fonte não
> descreve componentes, testes primários nem indicadores de falha para elas.
> Registrado em [Pendências](references/pendencias.md).

## Comparação direta dos números

| Nº | Modelo A (POST) | Modelo B (sistêmico) | Coincide? |
| --- | --- | --- | --- |
"""
mapa_a = {int(n): nome for n, nome in camadas_a}
for i in range(1, 11):
    a = mapa_a.get(i, "— (não existe)")
    b = usos_b.get(i, {}).get("nome", "— (não observado)")
    ok = "Sim" if (i in mapa_a and i in usos_b and
                   slug(a).startswith(slug(b)[:4])) else "**Não**"
    if i not in mapa_a or i not in usos_b:
        ok = "n/a"
    t += f"| {i} | {tcell(a)} | {tcell(b)} | {ok} |\n"

t += """
Apenas a camada 1 (*Energia*) coincide entre os dois modelos. As demais divergem.

## Regra de uso adotada nesta documentação

1. Todo número de camada é sempre reproduzido **exatamente como está na fonte**, incluindo o
   formato (`Camada 3: Memória` vs `3 - CPU`). O formato já identifica o modelo.
2. Nenhum número de camada foi convertido de um modelo para o outro.
3. Os nomes *Modelo A* e *Modelo B* existem **apenas nesta documentação**, para poder falar dos
   dois sem ambiguidade. Não estão na fonte.

> [!NOTE]
> Os rótulos "Modelo A" e "Modelo B" existem apenas nesta documentação, para permitir falar dos
> dois sem ambiguidade. Nível de confiança: **Inferido (organizacional)**.
"""
t += doc_footer(SRC, conf="Confirmado (modelo A) / Necessita validação (modelo B)", proximos=[
    ("quer a ficha técnica de uma camada do modelo A",
     "[Diagnóstico por camada](08-diagnostico-por-camada.md)"),
    ("está consultando um código de POST",
     "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md)"),
    ("está consultando um cenário de falha",
     "[Índice de cenários](10-cenarios/00-indice-cenarios.md)"),
    ("quer acompanhar a resolução do conflito",
     "[Pendências — P-03](references/pendencias.md)"),
])
open(f"{OUT}/03-taxonomia-camadas.md", "w").write(t)

# =========================================================================
# 04 — Requisitos e ferramentas
# =========================================================================
SRC4 = ("`HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Camadas de Diagnóstico`; "
        "`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `INDICE_CENARIOS` e `VALIDACAO_FINAL`")
t = doc_header(
    "Requisitos e ferramentas",
    SRC4,
    "Inventário das ferramentas, instrumentos e insumos citados nas fontes, organizado por onde a "
    "exigência aparece. Serve para montar a bancada antes de iniciar um atendimento.",
    "Ferramentas por camada de diagnóstico, por cenário de falha e por componente na validação "
    "final, transcritas das colunas correspondentes.",
    "Passo a passo de operação das ferramentas (ver `14-ferramentas/`); onde comprar, preços, "
    "versões suportadas ou requisitos de sistema — não constam nas fontes.",
    [
        "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md) — operação detalhada de Victoria, AIDA64 e MemTest86",
        "[Diagnóstico por camada](08-diagnostico-por-camada.md)",
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md)",
        "[Validação final por componente](13-validacao-final.md)",
    ],
    secao="comecar", nivel=0,
    resumo="Inventário do instrumental exigido pelos procedimentos, organizado por camada, por "
           "cenário e por componente na validação.",
    aplica_se="Preparação da bancada antes de iniciar um atendimento",
)

t += """> [!NOTE]
> O projeto é uma base de conhecimento documental. Não há software a instalar, compilar ou
> configurar. "Requisito", aqui, significa o instrumental necessário para executar os
> procedimentos documentados.
>
> Requisitos de sistema, versões mínimas de sistema operacional e requisitos de licenciamento das
> ferramentas **não constam nas fontes analisadas**, exceto onde citados pontualmente nos guias
> (por exemplo, a exigência de UEFI pelo MemTest86 v10+ e a licença Engineer do AIDA64).

## O que separar antes de começar

O instrumental depende de até onde o equipamento chega. Use o fluxo abaixo para decidir o que levar
para a bancada.

```mermaid
flowchart TD
    A(["Qual o estado<br/>do equipamento?"]) --> B{"Ele liga?"}
    B -->|"Não"| E1["Instrumentos elétricos:<br/>multímetro, testador de PSU,<br/>chave de fenda"]
    B -->|"Liga, mas não<br/>mostra imagem"| E2["Acima, mais:<br/>peças known-good,<br/>manual da placa-mãe, lupa"]
    B -->|"Liga e carrega<br/>o sistema"| E3["Software:<br/>AIDA64, MemTest86,<br/>Victoria, pendrive bootável"]

    E1 --> F{"Suspeita de<br/>firmware corrompido?"}
    F -->|"Sim"| G["Programadora CH341A,<br/>clamp SOIC-8, pendrive FAT32"]
    F -->|"Não"| H(["Consulte as tabelas<br/>por camada e por cenário"])
    E2 --> H
    E3 --> H
    G --> H
```

> [!NOTE]
> O agrupamento acima deriva das colunas de ferramentas por camada e por cenário, reproduzidas
> integralmente abaixo. Nível de confiança: **Confirmado** (as ferramentas) /
> **Inferido** (o agrupamento por estado do equipamento).

## Ferramentas por camada de diagnóstico (modelo A)

| Camada | Nome | Ferramentas (literal na fonte) |
| --- | --- | --- |
"""
H8 = {h: i for i, h in enumerate(cd[1])}
for r in cd[2:]:
    t += f"| {tcell(r[H8['CAMADA']])} | {tcell(r[H8['NOME']])} | {tcell(r[H8['FERRAMENTAS']])} |\n"

t += "\n## Ferramentas por cenário de falha\n\n| Cenário | Ferramentas necessárias (literal na fonte) |\n| --- | --- |\n"
ic = flu["INDICE_CENARIOS"]
IH = {h: i for i, h in enumerate(ic[0])}
for r in ic[1:]:
    t += f"| {tcell(r[IH['Cenário']])} | {tcell(r[IH['Ferramentas Necessárias']])} |\n"

t += "\n## Ferramentas de validação por componente\n\n| Componente | Ferramenta de validação (literal na fonte) |\n| --- | --- |\n"
vf = flu["VALIDACAO_FINAL"]
VH = {h: i for i, h in enumerate(vf[0])}
for r in vf[1:]:
    t += f"| {tcell(r[VH['Componente']])} | {tcell(r[VH['Ferramenta de Validação']])} |\n"

t += """
## Ferramentas com guia operacional próprio

Apenas três ferramentas possuem procedimento passo a passo nas fontes:

| Ferramenta | Etapas documentadas | Guia |
| --- | --- | --- |
| Victoria (HDD/SSD) | 9 | [victoria.md](14-ferramentas/victoria.md) |
| MemTest86 | 10 + critérios de decisão | [memtest86.md](14-ferramentas/memtest86.md) |
| AIDA64 | 45 | [01–15](14-ferramentas/aida64-etapas-01-15.md) · [16–30](14-ferramentas/aida64-etapas-16-30.md) · [31–45](14-ferramentas/aida64-etapas-31-45.md) |

As demais ferramentas citadas (multímetro, osciloscópio, programadora CH341A, CrystalDiskInfo,
WinDbg, Process Explorer, FurMark, entre outras) aparecem apenas como menção dentro de
procedimentos, sem guia próprio.

> [!NOTE]
> Nível de confiança: **Confirmado** para todas as tabelas acima — transcrição literal das
> colunas de origem.
"""
t += doc_footer(SRC4, proximos=[
    ("precisa do passo a passo de uma ferramenta",
     "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)"),
    ("quer saber qual ferramenta cada código exige",
     "[Índices cruzados](18-indices-cruzados.md)"),
    ("está pronto para começar o diagnóstico",
     "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md)"),
])
open(f"{OUT}/04-requisitos-e-ferramentas.md", "w").write(t)

print("03 e 04 gerados")
