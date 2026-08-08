import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs/14-ferramentas"
os.makedirs(OUT, exist_ok=True)
flu = read(F_FLU)

FIELDS = [
    ("Objetivo da etapa", "Objetivo da Etapa"),
    ("Ação exata a executar", "Ação Exata a Executar"),
    ("Caminho no software", "Caminho no Software"),
    ("Atalho de teclado", "Atalho de Teclado"),
    ("Configurações recomendadas", "Configurações Recomendadas"),
    ("Verificação antes de executar", "Verificação Antes de Executar"),
    ("Possíveis erros", "Possíveis Erros"),
    ("Causa técnica do erro", "Causa Técnica do Erro"),
    ("Como identificar o erro", "Como Identificar o Erro"),
    ("Como corrigir (passo a passo)", "Como Corrigir (Passo a Passo)"),
    ("Validação pós-correção", "Validação Pós-Correção"),
    ("Risco", "Risco"),
    ("Impacto se ignorado", "Impacto se Ignorado"),
    ("Tempo estimado", "Tempo Estimado"),
    ("Observações técnicas", "Observações Técnicas"),
    ("Boas práticas", "Boas Práticas"),
    ("Alternativa segura", "Alternativa Segura"),
    ("Checklist de confirmação", "Checklist de Confirmação"),
]


def num(v):
    try:
        return f"{float(v):g}"
    except ValueError:
        return v


def etapa_md(r, H):
    n = num(r[H["Nº da Etapa"]])
    t = f"## Etapa {n} — {cell(r[H['Fase do Processo']])}\n\n"
    for titulo, coluna in FIELDS:
        t += field(titulo, r[H[coluna]], 3) + "\n"
    return t + "---\n\n"


def gerar(sheet, arquivo, nome, contexto, escopo, faixa=None, extra_head="", extra_tail="",
          resumo_doc=None, aplica_doc=None, proximos=None,
):
    src = f"`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `{sheet}`"
    sh = flu[sheet]
    H = {h: i for i, h in enumerate(sh[0])}
    body = [r for r in sh[1:] if r[H["Fase do Processo"]].strip()]
    if faixa:
        body = [r for r in body if faixa[0] <= float(r[H["Nº da Etapa"]]) <= faixa[1]]
    t = doc_header(
        nome, src,
        contexto, escopo,
        "Interpretação clínica dos resultados fora do que a fonte declara; procedimentos de outras "
        "ferramentas; critérios de validação por componente (ver documento 13).",
        [
            "[Índice de ferramentas](00-indice-ferramentas.md)",
            "[Validação final por componente](../13-validacao-final.md)",
            "[Índice de cenários](../10-cenarios/00-indice-cenarios.md)",
        ],
        secao="ferramentas", nivel=1,
        resumo=resumo_doc,
        aplica_se=aplica_doc,
)
    t += extra_head
    t += "## Etapas\n\n| Nº | Fase do processo | Risco | Tempo estimado |\n| --- | --- | --- | --- |\n"
    for r in body:
        n = num(r[H["Nº da Etapa"]])
        t += (f"| [{n}](#{gh_anchor('Etapa ' + n + ' — ' + cell(r[H['Fase do Processo']]))}) | "
              f"{tcell(r[H['Fase do Processo']])} | {tcell(r[H['Risco']])} | "
              f"{tcell(r[H['Tempo Estimado']])} |\n")
    t += "\n---\n\n"
    for r in body:
        t += etapa_md(r, H)
    t += extra_tail
    t += doc_footer(src, proximos=proximos or [
        ("terminou o teste e precisa fechar o atendimento",
         "[Validação final por componente](../13-validacao-final.md)"),
        ("quer o procedimento do sintoma que motivou o teste",
         "[Índice de cenários](../10-cenarios/00-indice-cenarios.md)"),
        ("precisa de outra ferramenta", "[Índice de ferramentas](00-indice-ferramentas.md)"),
    ])
    open(f"{OUT}/{arquivo}", "w").write(t)
    return len(body)


# ---- Victoria -------------------------------------------------------------
n_vic = gerar(
    "REF_Victoria", "victoria.md", "Guia operacional — Victoria (HDD/SSD)",
    "Procedimento completo de uso do Victoria para diagnóstico de armazenamento, da preparação do "
    "ambiente à geração de relatório. Cada etapa registra também os erros possíveis, sua causa e a "
    "correção.",
    "As 9 etapas do procedimento registradas na fonte, com todos os campos originais.",
    resumo_doc="Procedimento em 9 etapas para diagnosticar e reparar unidades de armazenamento, "
               "da preparação do ambiente à geração do relatório.",
    aplica_doc="HDDs e SSDs — leitura de S.M.A.R.T., varredura de superfície e remapeamento",
)

# ---- MemTest86 ------------------------------------------------------------
mt = flu["REF_MemTest86"]
Hm = {h: i for i, h in enumerate(mt[0])}
criterios = [r for r in mt[1:] if not r[Hm["Fase do Processo"]].strip()]
tail = ""
if criterios:
    bruto = criterios[0][Hm["Nº da Etapa"]]
    partes = bruto.split("\n", 1)
    titulo_bloco = partes[0].strip()
    tail = ("## Critérios de decisão pós-MemTest86\n\n"
            "> Este bloco ocupa, na planilha de origem, a última linha da aba, na coluna "
            "`Nº da Etapa`. **Não é uma etapa do procedimento** — é um critério de decisão. "
            f"Título literal na fonte: **{titulo_bloco}**. Reproduzido integralmente abaixo.\n\n"
            + block(partes[1] if len(partes) > 1 else bruto) + "\n")

n_mem = gerar(
    "REF_MemTest86", "memtest86.md", "Guia operacional — MemTest86",
    "Procedimento completo de teste de memória com MemTest86, da criação da mídia bootável à "
    "restauração do boot, incluindo os critérios de decisão sobre o destino dos módulos testados.",
    "As 10 etapas do procedimento registradas na fonte, mais o bloco de critérios de decisão "
    "pós-teste presente na última linha da aba.",
    resumo_doc="Procedimento em 10 etapas para testar memória fora do sistema operacional, com os "
               "critérios de decisão sobre o destino dos módulos.",
    aplica_doc="Módulos DIMM e SO-DIMM — teste em ambiente bootável, com XMP ativo",
    extra_tail=tail,
)

# ---- AIDA64 (dividido por faixa numérica de etapas) -----------------------
aida_head = ("> Este guia foi dividido em três arquivos **apenas pela numeração das etapas de "
             "origem** (1–15, 16–30, 31–45). A divisão é organizacional; a fonte não define grupos.\n\n")
faixas = [(1, 15, "aida64-etapas-01-15.md"), (16, 30, "aida64-etapas-16-30.md"),
          (31, 45, "aida64-etapas-31-45.md")]
n_aida = 0
for a, b, arq in faixas:
    n_aida += gerar(
        "REF_AIDA64", arq, f"Guia operacional — AIDA64 (etapas {a:02d} a {b:02d})",
        "Procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e "
        "auditoria. Esta parte cobre a faixa de etapas indicada no título.",
        f"As etapas {a} a {b} registradas na fonte, com todos os campos originais.",
        resumo_doc=f"Etapas {a} a {b} do procedimento de uso do AIDA64 para monitoramento, teste "
                   "de estabilidade, benchmark e auditoria.",
        aplica_doc="Sistemas que carregam o Windows — sensores, stress test e relatórios",
        faixa=(a, b), extra_head=aida_head,
)

# ---- índice de ferramentas ------------------------------------------------
SRC = "`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `REF_Victoria`, `REF_AIDA64`, `REF_MemTest86`"
t = doc_header(
    "Índice de guias de ferramentas",
    SRC,
    "Ponto de entrada dos procedimentos operacionais detalhados das três ferramentas que possuem "
    "guia próprio na fonte.",
    "Lista dos guias disponíveis e da estrutura de campos comum a todas as etapas.",
    "Ferramentas citadas apenas de passagem em outras abas (ver documento de requisitos); "
    "critérios de validação por componente (documento 13).",
    [
        "[Requisitos e ferramentas](../04-requisitos-e-ferramentas.md) — inventário completo de ferramentas citadas",
        "[Validação final por componente](../13-validacao-final.md)",
        "[Índice de cenários](../10-cenarios/00-indice-cenarios.md)",
    ],
    secao="ferramentas", nivel=1,
    resumo="Qual ferramenta usar para cada tipo de verificação, e onde está o procedimento "
           "passo a passo de cada uma.",
    aplica_se="Victoria, AIDA64 e MemTest86 — as três com guia próprio na fonte",
)
t += """## Qual ferramenta usar

```mermaid
flowchart TD
    A(["O que você<br/>precisa verificar?"]) --> B{"Qual<br/>subsistema?"}
    B -->|"Disco: setores,<br/>S.M.A.R.T., reparo"| V["Victoria"]
    B -->|"Memória: erros<br/>de célula"| M["MemTest86"]
    B -->|"Temperatura, tensão,<br/>estabilidade, benchmark"| AI["AIDA64"]
    B -->|"Inventário de hardware<br/>e relatório de entrega"| AI

    V --> V1["Guia do Victoria<br/>9 etapas"]
    M --> M1["Guia do MemTest86<br/>10 etapas + critérios"]
    AI --> A1["Guia do AIDA64<br/>45 etapas, em 3 partes"]
```

> [!IMPORTANT]
> MemTest86 roda **fora** do Windows, a partir de mídia bootável. AIDA64 e Victoria rodam **dentro**
> do Windows — e o Victoria exige privilégio de administrador para acessar o disco em baixo nível.

> [!CAUTION]
> As etapas 7 e 8 do guia do Victoria alteram o disco: remapeamento e escrita/zero-fill.
> A etapa 8 **destrói os dados**. Leia o campo *Risco* de cada etapa antes de executá-la.

## Guias disponíveis

""" + f"""

| Ferramenta | Guia | Etapas |
| --- | --- | --- |
| Victoria (HDD/SSD) | [victoria.md](victoria.md) | {n_vic} |
| MemTest86 | [memtest86.md](memtest86.md) | {n_mem} (+ critérios de decisão) |
| AIDA64 | [etapas 01–15](aida64-etapas-01-15.md) · [16–30](aida64-etapas-16-30.md) · [31–45](aida64-etapas-31-45.md) | {n_aida} |

## Estrutura comum das etapas

Todas as etapas dos três guias seguem o mesmo conjunto de 20 campos definido na fonte:

"""
for titulo, coluna in [("Nº da etapa", "Nº da Etapa"), ("Fase do processo", "Fase do Processo")] + FIELDS:
    t += f"- **{titulo}** (`{coluna}`)\n"

t += """
## Observação sobre completude

O campo **Atalho de teclado** está vazio na maioria das etapas dos três guias, e o campo
**Alternativa segura** está vazio em parte das etapas de AIDA64 e MemTest86. Nesses pontos a
documentação registra explicitamente a ausência, em vez de preencher. Ver
[Limitações](../15-limitacoes.md).
"""
t += doc_footer(SRC, proximos=[
    ("quer o inventário completo do instrumental",
     "[Requisitos e ferramentas](../04-requisitos-e-ferramentas.md)"),
    ("precisa dos critérios de aprovação por componente",
     "[Validação final por componente](../13-validacao-final.md)"),
    ("quer saber qual ferramenta cada cenário exige",
     "[Índices cruzados](../18-indices-cruzados.md)"),
])
open(f"{OUT}/00-indice-ferramentas.md", "w").write(t)
print("ferramentas:", n_vic, n_mem, n_aida)
