import os, sys, collections, re
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
cod, flu = read(F_COD), read(F_FLU)

post = cod["Tabela Diagnóstico POST"]
HP = {h: i for i, h in enumerate(post[2])}
CODIGOS = []
FAM_ARQ = {
    "AMI (Legacy BIOS)": "ami-legacy", "AMI (UEFI/Aptio V)": "ami-uefi-aptio",
    "AMI (Q-Code Hex)": "ami-q-code", "Award BIOS": "award", "Phoenix BIOS": "phoenix",
    "Proprietário Dell": "dell", "Proprietário HP": "hp", "Proprietário Lenovo": "lenovo",
    "Apple (EFI)": "apple", "Proprietário Acer / Insyde": "acer-insyde",
    "Genérico (Múltiplos)": "generico-debug-led",
}
for n, r in enumerate(post[3:], start=1):
    pid = f"POST-{n:02d}"
    arq = FAM_ARQ[r[HP["FABRICANTE BIOS"]]]
    CODIGOS.append({
        "pid": pid, "codigo": r[HP["CÓDIGO"]], "arq": arq,
        "link": f"09-codigos-post/{arq}.md#{gh_anchor(pid + ' — ' + cell(r[HP['CÓDIGO']]))}",
        "comp": r[HP["COMPONENTE AFETADO"]], "camada": r[HP["CAMADA DE DIAGNÓSTICO"]],
        "fase": r[HP["FASE POST"]], "risco": r[HP["RISCO / CRITICIDADE"]],
        "sinal": r[HP["TIPO DE SINAL"]], "fam": r[HP["FABRICANTE BIOS"]],
        "plat": r[HP["FABRICANTE / PLATAFORMA"]], "ferr": r[HP["FERRAMENTAS OFICIAIS"]],
        "interp": r[HP["INTERPRETAÇÃO OFICIAL"]],
    })

tp = flu["TABELA_PRINCIPAL"]
HT = {h: i for i, h in enumerate(tp[0])}
SLUGS = {"NL": "nao-liga", "SV": "liga-sem-video", "RA": "reinicializacao-aleatoria",
         "BS": "bsod", "TR": "travamentos-freeze", "DN": "disco-nao-reconhecido",
         "SA": "superaquecimento", "AU": "alto-uso-cpu-gpu", "FI": "falhas-intermitentes"}
CENARIOS = []
for r in tp[1:]:
    cid = r[HT["ID"]]
    CENARIOS.append({
        "id": cid, "arq": SLUGS[cid.split("-")[0]],
        "link": f"10-cenarios/{SLUGS[cid.split('-')[0]]}.md#{gh_anchor(cid)}",
        "sintoma": r[HT["Sintoma Observado"]], "camada": r[HT["Camada Afetada"]],
        "comp": r[HT["Componente Suspeito"]], "ordem": r[HT["Ordem de Execução"]],
        "dep": r[HT["Dependências"]], "risco": r[HT["Risco Associado"]],
        "ferr": r[HT["Ferramentas Oficiais"]], "cmd": r[HT["Comandos Técnicos"]],
    })

# =========================================================================
# 18 — Índices cruzados
# =========================================================================
SRC = "Derivado das colunas de `Tabela Diagnóstico POST` e `TABELA_PRINCIPAL`"
t = doc_header(
    "Índices cruzados",
    SRC,
    "Reagrupamentos do mesmo conteúdo por outros eixos de busca. Nenhuma informação nova: são "
    "recortes das colunas de classificação já presentes nas fichas, montados para quem chega por "
    "um caminho diferente do sintoma.",
    "Índices por componente afetado, por camada, por risco, por fase do POST, por tipo de sinal e "
    "por ferramenta exigida.",
    "Conteúdo das fichas; entrada por sintoma (ver índices de códigos e de cenários).",
    [
        "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md) — entrada por código",
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md) — entrada por sintoma",
        "[Requisitos e ferramentas](04-requisitos-e-ferramentas.md) — inventário do instrumental",
        "[Taxonomia de camadas](03-taxonomia-camadas.md) — os dois modelos de numeração",
    ],
    secao="referencia", nivel=0,
    resumo="Os mesmos registros reagrupados por componente, camada, risco, fase do POST, tipo de "
           "sinal e ferramenta — para quem não chega pelo sintoma.",
    aplica_se="Busca por outro eixo que não o sintoma",
)

t += """## Por qual eixo buscar

```mermaid
flowchart TD
    A(["O que você<br/>já sabe?"]) --> B{"Ponto de<br/>partida"}
    B -->|"Sei qual peça<br/>estou investigando"| C["Índice por componente"]
    B -->|"Sei qual subsistema<br/>o código apontou"| D["Índice por camada"]
    B -->|"Preciso priorizar<br/>o que é mais grave"| E["Índice por risco"]
    B -->|"Sei em que momento<br/>do boot travou"| F["Índice por fase do POST"]
    B -->|"Sei o que o equipamento<br/>está emitindo"| G["Índice por tipo de sinal"]
    B -->|"Tenho apenas certas<br/>ferramentas disponíveis"| H["Índice por ferramenta"]
    B -->|"Preciso saber o que<br/>testar primeiro"| I["Cadeia de dependências"]

    C & D & E & F & G & H & I --> Z(["Abre a ficha<br/>correspondente"])
```

> [!TIP]
> Se o seu ponto de partida é o **sintoma**, não use esta página: vá pelo
> [README](../README.md#por-onde-começar) ou pelo
> [índice de cenários](10-cenarios/00-indice-cenarios.md).

> [!NOTE]
> Cada tabela agrupa registros pelo valor literal de uma coluna de origem. Nenhum registro foi
> reclassificado, e nenhuma categoria foi criada. Quando um registro declara mais de uma categoria
> (por exemplo `Camada 1: Energia / Camada 2: CPU`), ele aparece sob o valor completo, exatamente
> como está na fonte.

## Índice por componente afetado — códigos de POST

"""


def agrupar(itens, chave):
    g = collections.OrderedDict()
    for x in sorted(itens, key=lambda y: y[chave]):
        g.setdefault(x[chave], []).append(x)
    return g


for comp, itens in agrupar(CODIGOS, "comp").items():
    links = ", ".join(f"[{x['pid']}]({x['link']})" for x in itens)
    t += f"- **{cell(comp)}** ({len(itens)}) — {links}\n"

t += "\n## Índice por componente suspeito — cenários\n\n"
for comp, itens in agrupar(CENARIOS, "comp").items():
    links = ", ".join(f"[{x['id']}]({x['link']})" for x in itens)
    t += f"- **{cell(comp)}** — {links}\n"

t += """
## Índice por camada de diagnóstico

### Códigos de POST (modelo A — `Camada N: Nome`)

| Camada declarada | Códigos | Ficha da camada |
| --- | --- | --- |
"""
mapa_camada_doc = {
    "Camada 1: Energia": "08-diagnostico-por-camada.md#camada-1--energia-psuvrm",
    "Camada 2: CPU": "08-diagnostico-por-camada.md#camada-2--cpu-processador",
    "Camada 3: Memória": "08-diagnostico-por-camada.md#camada-3--memória-ram",
    "Camada 4: Vídeo": "08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu",
    "Camada 5: Chipset / Motherboard": "08-diagnostico-por-camada.md#camada-5--chipset--motherboard",
    "Camada 6: Firmware": "08-diagnostico-por-camada.md#camada-6--firmware-biosuefi",
    "Camada 7: Periféricos Críticos": "08-diagnostico-por-camada.md#camada-7--periféricos-críticos",
}
for camada, itens in agrupar(CODIGOS, "camada").items():
    links = ", ".join(f"[{x['pid']}]({x['link']})" for x in itens)
    ficha = f"[ver ficha]({mapa_camada_doc[camada]})" if camada in mapa_camada_doc else "— (valor composto ou variável)"
    t += f"| {tcell(camada)} | {links} | {ficha} |\n"

t += """
### Cenários (modelo B — `N - Nome`)

| Camada declarada | Cenários |
| --- | --- |
"""
for camada, itens in agrupar(CENARIOS, "camada").items():
    links = ", ".join(f"[{x['id']}]({x['link']})" for x in itens)
    t += f"| {tcell(camada)} | {links} |\n"

t += """
> Os dois blocos acima usam numerações **diferentes e incompatíveis**. Ver
> [03-taxonomia-camadas.md](03-taxonomia-camadas.md).

## Índice por risco declarado

### Códigos de POST

| Risco | Quantidade | Códigos |
| --- | --- | --- |
"""
ORDEM_RISCO = ["Crítico", "Alto", "Médio", "Baixo", "Variável"]
g = agrupar(CODIGOS, "risco")
for risco in ORDEM_RISCO:
    if risco in g:
        links = ", ".join(f"[{x['pid']}]({x['link']})" for x in g[risco])
        t += f"| **{risco}** | {len(g[risco])} | {links} |\n"

t += "\n### Cenários\n\n| Risco | Quantidade | Cenários |\n| --- | --- | --- |\n"
g = agrupar(CENARIOS, "risco")
for risco in ORDEM_RISCO:
    if risco in g:
        links = ", ".join(f"[{x['id']}]({x['link']})" for x in g[risco])
        t += f"| **{risco}** | {len(g[risco])} | {links} |\n"

t += """
> A escala de risco é a declarada pela fonte em `RISCO / CRITICIDADE` e `Risco Associado`. A fonte
> não define o significado de cada nível.

## Índice por fase do POST

Ordem de execução do firmware, conforme declarada na coluna `FASE POST`.

| Fase declarada | Códigos |
| --- | --- |
"""
for fase, itens in agrupar(CODIGOS, "fase").items():
    links = ", ".join(f"[{x['pid']}]({x['link']})" for x in itens)
    t += f"| {tcell(fase)} | {links} |\n"

t += """
## Índice por tipo de sinal

Use este índice quando a pergunta for "o equipamento está emitindo *isto*; o que consulto?".

| Tipo de sinal | Códigos | Onde observar |
| --- | --- | --- |
"""
ONDE = {
    "Beep Sonoro": "Speaker interno da placa-mãe",
    "Beep Sonoro (Sequência)": "Speaker interno, contando pausas entre grupos",
    "Beep Sonoro (Binário)": "Speaker interno",
    "Hex Q-Code (Display)": "Display de 2 dígitos na placa-mãe",
    "LED Diagnóstico (Âmbar/Branco)": "LED de status do gabinete/placa",
    "LED Piscante (Caps/Num Lock)": "LEDs do teclado",
    "LED de Diagnóstico (cor fixa)": "LEDs CPU/DRAM/VGA/BOOT da placa-mãe",
    "Tom Sonoro": "Speaker interno",
    "SmartBeep (Melodia)": "Speaker interno, interpretado por aplicativo",
}
for sinal, itens in agrupar(CODIGOS, "sinal").items():
    links = ", ".join(f"[{x['pid']}]({x['link']})" for x in itens)
    onde = ONDE.get(sinal, "—")
    t += f"| {tcell(sinal)} | {links} | {onde} |\n"

t += """
> A coluna *Onde observar* resume o local físico do sinal a partir do próprio nome do tipo
> declarado na fonte e das descrições das fichas. Nível de confiança: **Inferido**.

## Índice por ferramenta

Onde cada ferramenta é exigida. Os nomes seguem a grafia das colunas `FERRAMENTAS OFICIAIS` e
`Ferramentas Oficiais`; a busca é por ocorrência do nome dentro do texto da célula.

| Ferramenta | Códigos de POST | Cenários |
| --- | --- | --- |
"""
FERRAMENTAS = [
    ("Multímetro", r"[Mm]ultímetro"),
    ("Osciloscópio", r"[Oo]sciloscópio"),
    ("MemTest86", r"MemTest86"),
    ("AIDA64", r"AIDA64"),
    ("Victoria", r"Victoria"),
    ("CrystalDiskInfo", r"CrystalDiskInfo"),
    ("WinDbg", r"WinDbg"),
    ("BlueScreenView", r"BlueScreenView"),
    ("Programadora CH341A", r"CH341[AB]|Programadora"),
    ("Lupa", r"[Ll]upa"),
    ("POST Card", r"POST Card"),
    ("Testador de PSU", r"[Tt]estador de (PSU|fonte)|Dr\. Power"),
    ("CPU-Z", r"CPU-Z"),
    ("FurMark", r"FurMark"),
    ("Process Explorer", r"Process Explorer"),
    ("Pendrive / mídia bootável", r"[Pp]endrive|boot USB|bootável"),
    ("Componente known-good", r"known-good"),
]
for nome, pat in FERRAMENTAS:
    rx = re.compile(pat)
    c1 = [x for x in CODIGOS if rx.search(x["ferr"])]
    c2 = [x for x in CENARIOS if rx.search(x["ferr"])]
    if not c1 and not c2:
        continue
    l1 = ", ".join(f"[{x['pid']}]({x['link']})" for x in c1) or "—"
    l2 = ", ".join(f"[{x['id']}]({x['link']})" for x in c2) or "—"
    t += f"| **{nome}** | {l1} | {l2} |\n"

t += """
> Este índice cobre apenas as colunas de ferramentas das duas tabelas principais. Ferramentas
> citadas dentro de procedimentos, das fichas de camada ou dos guias operacionais não entram aqui —
> para o inventário completo, ver
> [04-requisitos-e-ferramentas.md](04-requisitos-e-ferramentas.md).

## Cadeia de dependências entre cenários

Ordem declarada na coluna `Ordem de Execução`, com os pré-requisitos da coluna `Dependências`.

| Ordem | Cenário | Depende de |
| --- | --- | --- |
"""
for x in sorted(CENARIOS, key=lambda y: int(y["ordem"]) if y["ordem"].isdigit() else 99):
    t += f"| {tcell(x['ordem'])} | [{x['id']}]({x['link']}) — {tcell(x['sintoma'])} | {tcell(x['dep'])} |\n"

t += doc_footer(SRC, conf="Confirmado (agrupamentos) / Inferido (coluna *Onde observar*)",
                proximos=[
                    ("localizou o código e quer a ficha",
                     "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md)"),
                    ("localizou o cenário e quer o procedimento",
                     "[Índice de cenários](10-cenarios/00-indice-cenarios.md)"),
                    ("quer o comando exato", "[Referência de comandos](19-comandos.md)"),
                    ("está montando a bancada",
                     "[Requisitos e ferramentas](04-requisitos-e-ferramentas.md)"),
                ])
open(f"{OUT}/18-indices-cruzados.md", "w").write(t)

# =========================================================================
# 19 — Referência de comandos
# =========================================================================
SRC19 = "`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL`, coluna `Comandos Técnicos`"
t = doc_header(
    "Referência de comandos técnicos",
    SRC19,
    "Todos os comandos declarados na coluna `Comandos Técnicos` dos cenários, reunidos em um só "
    "lugar. Serve para consulta rápida durante o atendimento, sem abrir cada ficha.",
    "Comandos por cenário, transcritos literalmente, com o contexto de uso e o link para a ficha "
    "completa.",
    "Comandos citados dentro de outros campos (método de diagnóstico, correção) — esses permanecem "
    "nas fichas; procedimentos de interface gráfica das ferramentas (ver `14-ferramentas/`).",
    [
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md) — fichas completas",
        "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)",
        "[Validação final por componente](13-validacao-final.md)",
    ],
    secao="referencia", nivel=0,
    resumo="Todos os comandos declarados nos cenários, reunidos com camada, risco e link para a "
           "ficha completa.",
    aplica_se="Consulta rápida durante a execução de um procedimento",
)

t += """> [!CAUTION]
> Os comandos abaixo são transcrição literal da fonte e vários **alteram o sistema**:
> `chkdsk /r /f` e `sfc /scannow`, por exemplo, modificam disco e arquivos de sistema. Consulte a
> ficha do cenário antes de executar — ela traz pré-requisitos, risco declarado e critério de
> validação.

> [!NOTE]
> Onde a fonte registra `N/A`, o diagnóstico é físico (medição elétrica, inspeção, substituição) e
> não há comando a executar.

## Comandos por cenário

"""
for x in CENARIOS:
    t += f"### [{x['id']}]({x['link']}) — {cell(x['sintoma'])}\n\n"
    t += f"**Camada declarada:** {cell(x['camada'])} · **Risco:** {cell(x['risco'])}\n\n"
    linhas = [l.strip() for l in x["cmd"].split("\n") if l.strip()]
    if len(linhas) == 1 and linhas[0].startswith("N/A"):
        t += f"Sem comando: {block(x['cmd'])}\n\n"
    else:
        t += "```text\n" + "\n".join(linhas) + "\n```\n\n"
    t += "---\n\n"

t += """## Comandos que aparecem em mais de um cenário

Agrupamento por ocorrência do nome do executável ou utilitário no texto acima.

| Comando / utilitário | Cenários |
| --- | --- |
"""
UTILS = [
    ("`eventvwr.msc`", r"eventvwr"),
    ("`mdsched.exe`", r"mdsched"),
    ("`chkdsk`", r"chkdsk"),
    ("`sfc /scannow`", r"sfc /scannow"),
    ("`DISM`", r"DISM|dism"),
    ("`diskmgmt.msc`", r"diskmgmt"),
    ("`wmic`", r"wmic"),
    ("PowerShell (`Get-*`)", r"Get-[A-Z]"),
    ("WinDbg (`!analyze -v`)", r"analyze -v|WinDbg"),
    ("`tasklist`", r"tasklist"),
    ("MemTest86 (boot USB)", r"MemTest86"),
    ("AIDA64", r"AIDA64"),
]
for nome, pat in UTILS:
    rx = re.compile(pat)
    sel = [x for x in CENARIOS if rx.search(x["cmd"])]
    if len(sel) >= 1:
        links = ", ".join(f"[{x['id']}]({x['link']})" for x in sel)
        t += f"| {nome} | {links} |\n"

t += """
> A tabela acima é montada por correspondência de texto sobre a mesma coluna transcrita acima.
> Nível de confiança: **Confirmado** (os comandos) / **Inferido** (o agrupamento).
"""
t += doc_footer(SRC19, proximos=[
    ("precisa do procedimento completo do cenário",
     "[Índice de cenários](10-cenarios/00-indice-cenarios.md)"),
    ("o comando é de uma ferramenta com guia próprio",
     "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)"),
    ("executou e precisa validar", "[Validação final por componente](13-validacao-final.md)"),
])
open(f"{OUT}/19-comandos.md", "w").write(t)
print("18 e 19 gerados |", len(CODIGOS), "códigos |", len(CENARIOS), "cenários")
