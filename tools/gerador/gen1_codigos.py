import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
SRC = "`HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`"

cod = read(F_COD)
rows = cod["Tabela Diagnóstico POST"]
HDR = rows[2]
BODY = rows[3:]

C = {h: i for i, h in enumerate(HDR)}

FAMILIAS = [
    ("AMI (Legacy BIOS)", "ami-legacy", "AMI BIOS Legacy"),
    ("AMI (UEFI/Aptio V)", "ami-uefi-aptio", "AMI UEFI / Aptio V"),
    ("AMI (Q-Code Hex)", "ami-q-code", "AMI Q-Code Hex"),
    ("Award BIOS", "award", "Award BIOS"),
    ("Phoenix BIOS", "phoenix", "Phoenix BIOS"),
    ("Proprietário Dell", "dell", "Dell (LED de diagnóstico)"),
    ("Proprietário HP", "hp", "HP (LED piscante)"),
    ("Proprietário Lenovo", "lenovo", "Lenovo (SmartBeep / beep binário)"),
    ("Apple (EFI)", "apple", "Apple EFI (Mac Intel)"),
    ("Proprietário Acer / Insyde", "acer-insyde", "Acer / Insyde"),
    ("Genérico (Múltiplos)", "generico-debug-led", "Genérico — Debug LED"),
]

# ID de documentação (POST-NN) derivado da ordem da linha na planilha
regs = []
for n, r in enumerate(BODY, start=1):
    regs.append({"pid": f"POST-{n:02d}", "row": r})

os.makedirs(f"{OUT}/09-codigos-post", exist_ok=True)

FIELDS = [
    ("Interpretação oficial", "INTERPRETAÇÃO OFICIAL"),
    ("Componente afetado", "COMPONENTE AFETADO"),
    ("Camada de diagnóstico", "CAMADA DE DIAGNÓSTICO"),
    ("Fase POST", "FASE POST"),
    ("Causa raiz (documentação oficial)", "CAUSA RAIZ (Documentação Oficial)"),
    ("Condições que geram o erro", "CONDIÇÕES QUE GERAM O ERRO"),
    ("Método de diagnóstico técnico", "MÉTODO DE DIAGNÓSTICO TÉCNICO"),
    ("Ferramentas oficiais", "FERRAMENTAS OFICIAIS"),
    ("Procedimento de correção (passo a passo)", "PROCEDIMENTO DE CORREÇÃO (Passo a Passo)"),
    ("Critério de validação", "CRITÉRIO DE VALIDAÇÃO"),
    ("Risco / criticidade", "RISCO / CRITICIDADE"),
    ("Fonte oficial", "FONTE OFICIAL"),
]


MAPA_CAMADA = {
    "Camada 1: Energia": "camada-1--energia-psuvrm",
    "Camada 2: CPU": "camada-2--cpu-processador",
    "Camada 3: Memória": "camada-3--memória-ram",
    "Camada 4: Vídeo": "camada-4--vídeo-gpuigpu",
    "Camada 5: Chipset / Motherboard": "camada-5--chipset--motherboard",
    "Camada 6: Firmware": "camada-6--firmware-biosuefi",
    "Camada 7: Periféricos Críticos": "camada-7--periféricos-críticos",
}
# códigos citados na aba de ambiguidades, pelo valor literal do código
AMBIGUOS = {"1 Longo + 2 Curtos", "1 Longo + 3 Curtos", "FF"}
AMB_ANCORA = {"1 Longo + 2 Curtos": "1-longo--2-curtos",
              "1 Longo + 3 Curtos": "1-longo--3-curtos",
              "FF": "q-code-ff"}


def ficha(reg):
    r = reg["row"]
    codigo = r[C["CÓDIGO"]]
    out = [f"## {reg['pid']} — {cell(codigo)}\n"]
    out.append(f"**Fabricante BIOS:** {cell(r[C['FABRICANTE BIOS']])}  ")
    out.append(f"**Fabricante / plataforma:** {cell(r[C['FABRICANTE / PLATAFORMA']])}  ")
    out.append(f"**Tipo de sinal:** {cell(r[C['TIPO DE SINAL']])}  ")
    out.append(f"**Código:** `{cell(codigo)}`\n")
    GRUPOS = [
        ("Identificação", ["Interpretação oficial", "Componente afetado",
                           "Camada de diagnóstico", "Fase POST"]),
        ("Diagnóstico", ["Causa raiz (documentação oficial)", "Condições que geram o erro",
                         "Método de diagnóstico técnico", "Ferramentas oficiais"]),
        ("Execução da correção", ["Procedimento de correção (passo a passo)"]),
        ("Resultado esperado", ["Critério de validação"]),
        ("Risco e origem", ["Risco / criticidade", "Fonte oficial"]),
    ]
    por_titulo = dict(FIELDS)
    for grupo, titulos in GRUPOS:
        out.append(f"### {grupo}\n")
        for titulo in titulos:
            out.append(field(titulo, r[C[por_titulo[titulo]]], level=4))

    # --- referências cruzadas derivadas das colunas de classificação ---
    refs = []
    camada = r[C["CAMADA DE DIAGNÓSTICO"]].strip()
    if camada in MAPA_CAMADA:
        refs.append(f"- Ficha da camada: [{cell(camada)}]"
                    f"(../08-diagnostico-por-camada.md#{MAPA_CAMADA[camada]})")
    elif camada:
        refs.append(f"- Camada declarada: `{cell(camada)}` — valor composto ou variável; "
                    "ver [Taxonomia de camadas](../03-taxonomia-camadas.md)")
    cod_lit = codigo.strip()
    if cod_lit in AMBIGUOS:
        refs.append(f"- **Código ambíguo.** Confira o critério de diferenciação em "
                    f"[Ambiguidade de códigos](../11-ambiguidades.md#{AMB_ANCORA[cod_lit]}) "
                    "antes de aplicar o procedimento.")
    refs.append(f"- Outros códigos do mesmo componente ou risco: "
                f"[Índices cruzados](../18-indices-cruzados.md)")
    refs.append("- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)")
    out.append("### Próximos passos\n\n" + "\n".join(refs) + "\n")
    return "\n".join(out) + "\n---\n"


# ---- arquivos por família -------------------------------------------------
indice_linhas = []
for fam, sl, nome in FAMILIAS:
    sel = [x for x in regs if x["row"][C["FABRICANTE BIOS"]] == fam]
    if not sel:
        continue
    path = f"{OUT}/09-codigos-post/{sl}.md"
    txt = doc_header(
        f"Códigos POST — {nome}",
        SRC,
        f"Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `{fam}`. "
        "Cada ficha reproduz integralmente os campos registrados na planilha de origem.",
        f"Os {len(sel)} código(s) da família `{fam}` presentes na fonte, com interpretação, causa raiz, "
        "método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.",
        "Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.",
        [
            "[Índice de códigos POST](00-indice-codigos.md)",
            "[Fluxo de diagnóstico POST](../06-fluxo-post.md)",
            "[Camadas de diagnóstico](../08-diagnostico-por-camada.md)",
            "[Ambiguidade de códigos](../11-ambiguidades.md)",
        ],
        secao="resolver", nivel=1,
        resumo=f"Fichas completas dos códigos de POST da família {nome}, com causa raiz, "
               "diagnóstico, correção e critério de validação.",
        aplica_se=f"Equipamentos com BIOS `{fam}`",
)
    txt += "\n".join(ficha(x) for x in sel)
    txt += doc_footer(SRC, proximos=[
        ("não encontrou o código aqui",
         "[Índice de códigos POST](00-indice-codigos.md) — catálogo completo"),
        ("suspeita que o código tem outro significado",
         "[Ambiguidade de códigos](../11-ambiguidades.md)"),
        ("quer saber o que testar naquele subsistema",
         "[Diagnóstico por camada](../08-diagnostico-por-camada.md)"),
        ("aplicou a correção e precisa fechar o atendimento",
         "[Validação final por componente](../13-validacao-final.md)"),
    ])
    open(path, "w").write(txt)
    for x in sel:
        indice_linhas.append((x["pid"], x["row"], f"{sl}.md"))

# ---- índice de códigos ----------------------------------------------------
hdr = "| ID doc. | Código | Tipo de sinal | Fabricante BIOS | Plataforma | Componente afetado | Camada | Risco | Ficha |"
sep = "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"
linhas = [hdr, sep]
for pid, r, arq in indice_linhas:
    linhas.append(
        f"| {pid} | {tcell(r[C['CÓDIGO']])} | {tcell(r[C['TIPO DE SINAL']])} | "
        f"{tcell(r[C['FABRICANTE BIOS']])} | {tcell(r[C['FABRICANTE / PLATAFORMA']])} | "
        f"{tcell(r[C['COMPONENTE AFETADO']])} | {tcell(r[C['CAMADA DE DIAGNÓSTICO']])} | "
        f"{tcell(r[C['RISCO / CRITICIDADE']])} | "
        f"[{pid}]({arq}#{gh_anchor(pid + ' — ' + cell(r[C['CÓDIGO']]))}) |")

idx = doc_header(
    "Índice de códigos POST",
    SRC,
    "Ponto de entrada do catálogo de códigos de POST. Lista todos os códigos registrados na fonte "
    "e aponta para a ficha completa de cada um.",
    f"Índice único dos {len(indice_linhas)} códigos presentes na fonte, agrupados por família de BIOS.",
    "Conteúdo detalhado das fichas (ver arquivos por família); fluxos; cenários pós-boot.",
    [
        "[Fluxo de diagnóstico POST](../06-fluxo-post.md) — como chegar até um código",
        "[Ambiguidade de códigos](../11-ambiguidades.md) — códigos com mais de um significado",
        "[Camadas de diagnóstico](../08-diagnostico-por-camada.md) — subsistema de cada código",
    ],
    secao="resolver", nivel=1,
    resumo="Ponto de entrada do catálogo: localize o código que o equipamento está emitindo e "
           "vá direto para a ficha.",
    aplica_se="Falhas anteriores ao carregamento do sistema operacional",
)

idx += """## Como localizar o código

```mermaid
flowchart TD
    A(["O equipamento está<br/>emitindo algum sinal"]) --> B{"Que tipo<br/>de sinal?"}
    B -->|"Bipes pelo alto-falante"| C{"Qual fabricante<br/>de BIOS?"}
    B -->|"Dois dígitos num<br/>display na placa"| QC["Q-Code hexadecimal"]
    B -->|"LED aceso na placa<br/>ou no gabinete"| LD{"LED de onde?"}
    B -->|"Melodia"| LN["Lenovo SmartBeep"]

    C -->|"AMI antigo"| F1["AMI Legacy"]
    C -->|"AMI moderno / UEFI"| F2["AMI UEFI / Aptio V"]
    C -->|"Award"| F3["Award"]
    C -->|"Phoenix<br/>padrão X-X-X-X"| F4["Phoenix"]
    C -->|"Acer / Insyde"| F5["Acer / Insyde"]
    C -->|"Apple / Mac Intel"| F6["Apple EFI"]

    LD -->|"CPU, DRAM, VGA ou BOOT<br/>na placa-mãe"| F7["Debug LED genérico"]
    LD -->|"Âmbar e branco<br/>piscando"| F8["Dell"]
    LD -->|"Caps Lock ou<br/>Num Lock piscando"| F9["HP"]

    QC --> F10["AMI Q-Code Hex"]
    LN --> F11["Lenovo"]

    F1 & F2 & F3 & F4 & F5 & F6 & F7 & F8 & F9 & F10 & F11 --> Z(["Abrir a ficha do código<br/>no catálogo abaixo"])
```

> [!TIP]
> Não sabe identificar o fabricante do BIOS? A tela de abertura antes do erro, o adesivo na
> placa-mãe e o manual do fabricante trazem essa informação. O
> [fluxo de diagnóstico POST](../06-fluxo-post.md) percorre essa identificação passo a passo.

> [!IMPORTANT]
> O mesmo padrão sonoro pode significar coisas diferentes conforme o fabricante. Antes de aplicar
> o procedimento, confira se o código está em [Ambiguidade de códigos](../11-ambiguidades.md).

## Identificadores

O campo **ID doc.** (`POST-NN`) é um identificador criado **nesta documentação** para permitir
referência cruzada estável entre documentos. Ele **não existe na planilha de origem** e segue a
ordem das linhas da aba `Tabela Diagnóstico POST`. O campo **Código** é o valor literal da fonte.

> Nível de confiança do campo `ID doc.`: **Inferido (organizacional)**.
> Nível de confiança de todos os demais campos: **Confirmado**.

## Arquivos por família de BIOS

"""
for fam, sl, nome in FAMILIAS:
    n = len([x for x in indice_linhas if x[1][C["FABRICANTE BIOS"]] == fam])
    if n:
        idx += f"- [{nome}]({sl}.md) — {n} código(s)\n"

idx += "\n## Catálogo completo\n\n" + "\n".join(linhas) + "\n"
idx += doc_footer(SRC, proximos=[
    ("ainda não sabe qual é o código", "[Fluxo de diagnóstico POST](../06-fluxo-post.md)"),
    ("quer buscar por componente, risco ou ferramenta",
     "[Índices cruzados](../18-indices-cruzados.md)"),
    ("o equipamento liga e carrega o sistema, mas falha depois",
     "[Índice de cenários](../10-cenarios/00-indice-cenarios.md)"),
    ("precisa do significado de um termo", "[Glossário](../17-glossario.md)"),
])
open(f"{OUT}/09-codigos-post/00-indice-codigos.md", "w").write(idx)

json.dump([[p, r[C["CÓDIGO"]], r[C["FABRICANTE BIOS"]], a] for p, r, a in indice_linhas],
          open("/home/claude/gen/_codigos.json", "w"), ensure_ascii=False)
print("códigos gerados:", len(indice_linhas))
