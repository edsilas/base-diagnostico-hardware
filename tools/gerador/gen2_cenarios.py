import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
SRC = "`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`"

flu = read(F_FLU)
tp = flu["TABELA_PRINCIPAL"]
H = {h: i for i, h in enumerate(tp[0])}
BODY = tp[1:]

ic = flu["INDICE_CENARIOS"]
IH = {h: i for i, h in enumerate(ic[0])}
CEN = ic[1:]

# Mapa prefixo -> (nome do cenário na fonte, linha do INDICE_CENARIOS)
pref_map = {}
for r in CEN:
    for i in [x.strip() for x in r[IH["IDs Relacionados"]].split(",")]:
        if i:
            pref_map[i.split("-")[0]] = (r[IH["Cenário"]], r)

fl = flu["FLUXO_LOGICO"]
FH = {h: i for i, h in enumerate(fl[0])}
NOS_POR_ID = {}
for r in fl[1:]:
    for i in [x.strip() for x in r[FH["Referência (ID)"]].split(",") if x.strip() and x.strip() != "—"]:
        NOS_POR_ID.setdefault(i, []).append(r[FH["Nó"]])

# cenários que dependem de um dado ID (coluna Dependências)
DEPENDENTES = {}
for r in BODY:
    for outro in BODY:
        if outro[H["ID"]] != r[H["ID"]] and outro[H["ID"]] in r[H["Dependências"]]:
            DEPENDENTES.setdefault(outro[H["ID"]], []).append(r[H["ID"]])

SLUGS = {
    "NL": "nao-liga",
    "SV": "liga-sem-video",
    "RA": "reinicializacao-aleatoria",
    "BS": "bsod",
    "TR": "travamentos-freeze",
    "DN": "disco-nao-reconhecido",
    "SA": "superaquecimento",
    "AU": "alto-uso-cpu-gpu",
    "FI": "falhas-intermitentes",
}

FIELDS = [
    ("Sintoma observado", "Sintoma Observado"),
    ("Camada afetada", "Camada Afetada"),
    ("Componente suspeito", "Componente Suspeito"),
    ("Condição de ocorrência", "Condição de Ocorrência"),
    ("Causa raiz", "Causa Raiz"),
    ("Método de diagnóstico (passo a passo)", "Método de Diagnóstico (Passo a Passo)"),
    ("Ferramentas oficiais", "Ferramentas Oficiais"),
    ("Comandos técnicos", "Comandos Técnicos"),
    ("Procedimento de correção (detalhado)", "Procedimento de Correção (Detalhado)"),
    ("Ordem de execução", "Ordem de Execução"),
    ("Dependências", "Dependências"),
    ("Critério de validação técnica", "Critério de Validação Técnica"),
    ("Evidência de sucesso", "Evidência de Sucesso"),
    ("Risco associado", "Risco Associado"),
    ("Impacto no sistema", "Impacto no Sistema"),
    ("Fonte oficial", "Fonte Oficial"),
]

os.makedirs(f"{OUT}/10-cenarios", exist_ok=True)
indice = []

for pref, sl in SLUGS.items():
    sel = [r for r in BODY if r[H["ID"]].startswith(pref + "-")]
    if not sel:
        continue
    nome, cenrow = pref_map[pref]
    txt = doc_header(
        f"Cenário — {nome}",
        SRC,
        f"Fichas de diagnóstico do cenário `{nome}` conforme registrado na fonte. "
        "Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.",
        f"IDs {', '.join(r[H['ID']] for r in sel)} — sintoma, causa raiz, método de diagnóstico, "
        "comandos, correção, validação, risco e fonte oficial.",
        "Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.",
        [
            "[Índice de cenários](00-indice-cenarios.md)",
            "[Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)",
            "[Correlações entre camadas](../12-correlacoes.md)",
            "[Validação final por componente](../13-validacao-final.md)",
        ],
        secao="resolver", nivel=1,
        resumo=f"Procedimento completo para o cenário {nome}: pré-requisitos, diagnóstico, "
               "correção, resultado esperado e riscos.",
        aplica_se="Equipamentos que concluem o POST — falhas percebidas em uso",
)
    txt += "## Entrada rápida (registro do índice de cenários)\n\n"
    txt += f"- **Cenário (fonte):** {cell(cenrow[IH['Cenário']])}\n"
    txt += f"- **IDs relacionados:** {cell(cenrow[IH['IDs Relacionados']])}\n"
    txt += f"- **Camada primária:** {cell(cenrow[IH['Camada Primária']])}\n"
    txt += f"- **Primeiro teste:** {cell(cenrow[IH['Primeiro Teste']])}\n"
    txt += f"- **Ferramentas necessárias:** {cell(cenrow[IH['Ferramentas Necessárias']])}\n\n---\n\n"

    for r in sel:
        cid = r[H["ID"]]
        txt += f"## {cid}\n\n"
        GRUPOS = [
            ("Identificação", ["Sintoma observado", "Camada afetada", "Componente suspeito",
                               "Condição de ocorrência"]),
            ("Pré-requisitos", ["Dependências", "Ordem de execução", "Ferramentas oficiais"]),
            ("Diagnóstico", ["Causa raiz", "Método de diagnóstico (passo a passo)",
                             "Comandos técnicos"]),
            ("Execução da correção", ["Procedimento de correção (detalhado)"]),
            ("Resultado esperado", ["Critério de validação técnica", "Evidência de sucesso"]),
            ("Risco e impacto", ["Risco associado", "Impacto no sistema"]),
            ("Origem", ["Fonte oficial"]),
        ]
        por_titulo = dict(FIELDS)
        for grupo, titulos in GRUPOS:
            txt += f"### {grupo}\n\n"
            for titulo in titulos:
                txt += field(titulo, r[H[por_titulo[titulo]]], level=4) + "\n"

        # --- referências cruzadas derivadas das colunas de ligação ---
        refs = []
        nos = NOS_POR_ID.get(cid, [])
        if nos:
            refs.append("- Alcançado pelos nós "
                        + ", ".join(f"[{n}](../07-fluxo-sistemico.md#{gh_anchor(n)})" for n in nos)
                        + " do fluxo sistêmico")
        else:
            refs.append("- **Nenhum nó do fluxo sistêmico conduz a este cenário.** Entrada apenas "
                        "pelo [índice de cenários](00-indice-cenarios.md). "
                        "Ver [P-09 em pendências](../references/pendencias.md)")
        dep = r[H["Dependências"]].strip()
        ids_dep = [x["row"][H["ID"]] if isinstance(x, dict) else x for x in []]
        alvos = [o[H["ID"]] for o in BODY if o[H["ID"]] != cid and o[H["ID"]] in dep]
        if alvos:
            refs.append("- Depende de "
                        + ", ".join(f"[{a}]({SLUGS[a.split('-')[0]]}.md#{gh_anchor(a)})" for a in alvos)
                        + " — execute-os antes")
        seg = DEPENDENTES.get(cid, [])
        if seg:
            refs.append("- É pré-requisito de "
                        + ", ".join(f"[{a}]({SLUGS[a.split('-')[0]]}.md#{gh_anchor(a)})" for a in seg))
        refs.append("- Comando desta ficha na "
                    "[referência consolidada de comandos](../19-comandos.md#"
                    + gh_anchor(f"{cid} — {cell(r[H['Sintoma Observado']])}") + ")")
        refs.append("- Critérios de encerramento: "
                    "[Validação final por componente](../13-validacao-final.md)")
        txt += "### Próximos passos\n\n" + "\n".join(refs) + "\n\n"
        txt += "---\n\n"
        indice.append((cid, r, sl, nome))
    txt += doc_footer(SRC, proximos=[
        ("o problema voltou depois da troca de peça",
         "[Correlações entre camadas](../12-correlacoes.md)"),
        ("aplicou a correção e precisa validar",
         "[Validação final por componente](../13-validacao-final.md)"),
        ("precisa operar AIDA64, MemTest86 ou Victoria",
         "[Guias de ferramentas](../14-ferramentas/00-indice-ferramentas.md)"),
        ("quer conferir onde este cenário entra no fluxo",
         "[Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)"),
    ])
    open(f"{OUT}/10-cenarios/{sl}.md", "w").write(txt)

# ---- índice de cenários ---------------------------------------------------
idx = doc_header(
    "Índice de cenários de falha",
    SRC,
    "Ponto de entrada por sintoma. Quem chega com uma queixa ('não liga', 'tela azul', "
    "'reinicia sozinho') começa aqui e é direcionado à ficha correspondente.",
    f"Os {len(CEN)} cenários e os {len(BODY)} IDs de diagnóstico registrados na fonte, "
    "com camada primária, primeiro teste e ferramentas necessárias.",
    "Conteúdo detalhado das fichas (ver arquivos por cenário); códigos de POST; fluxos completos.",
    [
        "[Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md) — sequência F01→F14",
        "[Índice de códigos POST](../09-codigos-post/00-indice-codigos.md) — quando o sistema nem chega ao SO",
        "[Correlações entre camadas](../12-correlacoes.md) — quando o sintoma engana",
    ],
    secao="resolver", nivel=1,
    resumo="Ponto de entrada por sintoma. Descreva o que o equipamento faz e vá direto para o "
           "procedimento.",
    aplica_se="Falhas percebidas depois que o sistema operacional carrega",
)

idx += """## Qual é o seu sintoma?

```mermaid
flowchart TD
    A(["O que o equipamento<br/>está fazendo?"]) --> B{"Ele liga?"}
    B -->|"Não dá sinal de vida"| NL["Não liga<br/>NL-01, NL-02"]
    B -->|"Liga, mas a tela<br/>fica preta"| SV["Liga sem vídeo<br/>SV-01, SV-02"]
    B -->|"Liga e aparece imagem"| C{"O sistema<br/>carrega?"}

    C -->|"Trava ou reinicia<br/>antes de abrir"| BS["BSOD<br/>BS-01, BS-02"]
    C -->|"Carrega normalmente"| D{"O que acontece<br/>durante o uso?"}

    D -->|"Reinicia sozinho,<br/>sem tela azul"| RA["Reinicialização aleatória<br/>RA-01, RA-02"]
    D -->|"Congela: mouse e<br/>teclado param"| TR["Travamentos<br/>TR-01"]
    D -->|"Tela azul"| BS
    D -->|"Fica muito quente<br/>ou desliga sozinho"| SA["Superaquecimento<br/>SA-01"]
    D -->|"Está lento, CPU<br/>ou GPU no máximo"| AU["Alto uso CPU/GPU<br/>AU-01"]
    D -->|"Um disco sumiu<br/>do sistema"| DN["Disco não reconhecido<br/>DN-01"]
    D -->|"Falha de vez em quando,<br/>sem padrão"| FI["Falhas intermitentes<br/>FI-01"]
```

> [!IMPORTANT]
> Se o equipamento **não chega a carregar o sistema**, o caminho é outro: comece pelo
> [fluxo de diagnóstico POST](../06-fluxo-post.md) e pelo
> [catálogo de códigos](../09-codigos-post/00-indice-codigos.md).

> [!WARNING]
> Um sintoma pode ter origem em outra camada. Trocar a peça que o sintoma aponta, sem
> verificar a cadeia, é o erro mais comum registrado nesta base — ver
> [Correlações entre camadas](../12-correlacoes.md).

## Tabela de entrada por sintoma

"""
idx += "| Cenário | IDs relacionados | Camada primária | Primeiro teste | Ferramentas necessárias | Fichas |\n"
idx += "| --- | --- | --- | --- | --- | --- |\n"
for r in CEN:
    ids = [x.strip() for x in r[IH["IDs Relacionados"]].split(",") if x.strip()]
    sl = SLUGS[ids[0].split("-")[0]]
    links = ", ".join(f"[{i}]({sl}.md#{gh_anchor(i)})" for i in ids)
    idx += (f"| {tcell(r[IH['Cenário']])} | {tcell(r[IH['IDs Relacionados']])} | "
            f"{tcell(r[IH['Camada Primária']])} | {tcell(r[IH['Primeiro Teste']])} | "
            f"{tcell(r[IH['Ferramentas Necessárias']])} | {links} |\n")

idx += "\n## Ordem de execução declarada na fonte\n\n"
idx += "| ID | Sintoma observado | Camada afetada | Componente suspeito | Ordem de execução | Dependências | Risco |\n"
idx += "| --- | --- | --- | --- | --- | --- | --- |\n"
for cid, r, sl, nome in sorted(indice, key=lambda x: (int(x[1][H["Ordem de Execução"]]) if x[1][H["Ordem de Execução"]].isdigit() else 99, x[0])):
    idx += (f"| [{cid}]({sl}.md#{gh_anchor(cid)}) | {tcell(r[H['Sintoma Observado']])} | "
            f"{tcell(r[H['Camada Afetada']])} | {tcell(r[H['Componente Suspeito']])} | "
            f"{tcell(r[H['Ordem de Execução']])} | {tcell(r[H['Dependências']])} | "
            f"{tcell(r[H['Risco Associado']])} |\n")

idx += "\n## Arquivos por cenário\n\n"
for r in CEN:
    ids = [x.strip() for x in r[IH["IDs Relacionados"]].split(",") if x.strip()]
    sl = SLUGS[ids[0].split("-")[0]]
    idx += f"- [{cell(r[IH['Cenário']])}]({sl}.md) — {', '.join(ids)}\n"

idx += doc_footer(SRC, proximos=[
    ("o equipamento não chega a carregar o sistema",
     "[Fluxo de diagnóstico POST](../06-fluxo-post.md)"),
    ("quer percorrer o diagnóstico do início ao fim",
     "[Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)"),
    ("precisa do comando exato de um cenário",
     "[Referência de comandos](../19-comandos.md)"),
    ("quer buscar por componente, risco ou ferramenta",
     "[Índices cruzados](../18-indices-cruzados.md)"),
])
open(f"{OUT}/10-cenarios/00-indice-cenarios.md", "w").write(idx)
print("cenários gerados:", len(indice), "| arquivos:", len(set(x[2] for x in indice)))
