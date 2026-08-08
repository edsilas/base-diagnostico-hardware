import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
cod = read(F_COD)
flu = read(F_FLU)

# =========================================================================
# 06 — Fluxo de diagnóstico POST (arquivo 1, aba "Fluxo de Diagnóstico")
# =========================================================================
SRC6 = "`HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Fluxo de Diagnóstico`"
fd = cod["Fluxo de Diagnóstico"]
titulo_fonte = fd[0][0]
H = {h: i for i, h in enumerate(fd[1])}
etapas = fd[2:]

t = doc_header(
    "Fluxo de diagnóstico POST",
    SRC6,
    "Fluxo condicional aplicado **antes** de o sistema operacional carregar. Vai da verificação de "
    "energia até a identificação do tipo de sinal de diagnóstico (beep, Q-Code, LED, SmartBeep) e o "
    "encaminhamento para a ficha do código correspondente.",
    "As 7 etapas do fluxograma de POST registradas na fonte, com condição, ação em caso afirmativo, "
    "ação em caso negativo, próxima etapa e observações.",
    "Diagnóstico após o boot do sistema operacional (ver fluxo sistêmico); conteúdo das fichas de "
    "código; guias de ferramentas.",
    [
        "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md) — continua depois que o POST conclui",
        "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md) — destino das Etapas 4, 5 e 6",
        "[Camadas de diagnóstico](08-diagnostico-por-camada.md) — subsistemas citados nas ações",
        "[Ambiguidade de códigos](11-ambiguidades.md) — tratamento citado na Etapa 4",
    ],
    secao="diagnosticar", nivel=0,
    resumo="Sequência de decisão para equipamentos que não concluem o POST, da verificação de "
           "energia até a identificação do código de erro.",
    aplica_se="Desktops, notebooks e servidores que não chegam a carregar o sistema operacional",
)

t += f"## Objetivo\n\nTítulo declarado na fonte: **{cell(titulo_fonte)}**\n\n"
t += """## Quando utilizar

Quando o equipamento não conclui o POST: não liga, liga sem vídeo, emite beeps, exibe Q-Code fixo
ou acende LED de diagnóstico. A Etapa 1 é o ponto de entrada obrigatório.

## Pré-requisitos

Os pré-requisitos não estão declarados em campo próprio na fonte. As ferramentas citadas nas ações
de cada etapa estão reproduzidas abaixo, no texto original.

> Nível de confiança: **Confirmado** para o conteúdo das etapas; a seção "Quando utilizar" acima é
> **Inferida** a partir da condição da Etapa 1.

## Visão geral das etapas

| Etapa | Condição / pergunta | Próxima etapa |
| --- | --- | --- |
"""
for r in etapas:
    t += f"| {tcell(r[H['ETAPA']])} | {tcell(r[H['CONDIÇÃO / PERGUNTA']])} | {tcell(r[H['PRÓXIMA ETAPA']])} |\n"

t += """
## Diagrama do fluxo

Reprodução visual das colunas `ETAPA`, `CONDIÇÃO / PERGUNTA` e `PRÓXIMA ETAPA`. O texto integral
de cada etapa está na seção seguinte.

```mermaid
flowchart TD
    E1["Etapa 1<br/>O sistema liga?"]
    E2["Etapa 2<br/>Há beep, Q-Code,<br/>LED ou som de POST?"]
    E3["Etapa 3<br/>Qual o TIPO de sinal?"]
    E4["Etapa 4<br/>BEEP CODE<br/>Identificar fabricante do BIOS"]
    E5["Etapa 5<br/>Q-CODE HEX<br/>Fixo ou progredindo?"]
    E6["Etapa 6<br/>LED DIAGNÓSTICO<br/>Qual LED está aceso?"]
    SB["SMARTBEEP<br/>App Lenovo PC Diagnostics"]
    E7["Etapa 7<br/>POST completou?"]
    C1["CAMADA 1 - ENERGIA<br/>cabo AC, tomada, fonte,<br/>botão power, front panel"]
    NP["SISTEMA SILENCIOSO<br/>speaker, Q-Code, Debug LED,<br/>boot mínimo"]
    OK["SUCESSO<br/>BIOS, boot, diagnósticos,<br/>stress test, documentar"]
    FALHA["FALHA PERSISTENTE<br/>teste isolado, teste cruzado,<br/>escalação"]

    E1 -->|Sim| E2
    E1 -->|Não| C1
    E2 -->|Sim| E3
    E2 -->|Não| NP
    NP --> E7
    E3 -->|Beep| E4
    E3 -->|Q-Code hex| E5
    E3 -->|LED| E6
    E3 -->|SmartBeep| SB
    E4 --> E7
    E5 --> E7
    E6 --> E7
    E7 -->|Sim| OK
    E7 -->|Não| FALHA
```

> O diagrama é uma representação das colunas de encadeamento da fonte. Os rótulos das setas e os
> textos dos nós são resumos das células; o conteúdo integral está abaixo, sem cortes.
> Nível de confiança: **Confirmado** (topologia) / **Inferido** (condensação dos rótulos).

---

## Fluxo detalhado

"""
for r in etapas:
    t += f"### Etapa {cell(r[H['ETAPA']])}\n\n"
    t += field("Condição / pergunta", r[H["CONDIÇÃO / PERGUNTA"]], 4) + "\n"
    t += field("Ação se SIM", r[H["AÇÃO SE SIM"]], 4) + "\n"
    t += field("Ação se NÃO", r[H["AÇÃO SE NÃO"]], 4) + "\n"
    t += field("Próxima etapa", r[H["PRÓXIMA ETAPA"]], 4) + "\n"
    t += field("Observações", r[H["OBSERVAÇÕES"]], 4) + "\n---\n\n"

t += """## Quando interromper

A fonte registra, na Etapa 7, dois desfechos: **SUCESSO** (POST completo, seguido de validação e
documentação) e **FALHA PERSISTENTE** (escalação para teste de hardware isolado e teste cruzado).
Ambos estão transcritos integralmente na Etapa 7 acima.

## Observações

A Etapa 4 remete à "Tabela Diagnóstico POST (Aba 1)" da planilha de origem. Nesta documentação,
esse conteúdo está em [09-codigos-post/](09-codigos-post/00-indice-codigos.md).
"""
t += doc_footer(SRC6, proximos=[
    ("identificou o código e quer a ficha",
     "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md)"),
    ("o código tem mais de um significado", "[Ambiguidade de códigos](11-ambiguidades.md)"),
    ("quer saber o que testar em cada subsistema",
     "[Diagnóstico por camada](08-diagnostico-por-camada.md)"),
    ("o POST concluiu e a falha aparece em uso",
     "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md)"),
])
open(f"{OUT}/06-fluxo-post.md", "w").write(t)

# =========================================================================
# 07 — Fluxo sistêmico (arquivo 2, aba FLUXO_LOGICO)
# =========================================================================
SRC7 = "`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `FLUXO_LOGICO`"
fl = flu["FLUXO_LOGICO"]
H7 = {h: i for i, h in enumerate(fl[0])}
nos = fl[1:]

t = doc_header(
    "Fluxo de diagnóstico sistêmico (F01 → F14)",
    SRC7,
    "Árvore de decisão de ponta a ponta: parte do acionamento do botão Power e termina na validação "
    "completa do sistema. Cada nó aponta o próximo nó ou uma ação terminal, e referencia o ID do "
    "cenário correspondente.",
    "Os 17 nós de decisão registrados na fonte (rótulos F01 a F14, incluindo os sub-nós F02b, "
    "F09b e F09c), com condição, ramo verdadeiro, ramo "
    "falso, ação, ferramentas e ID de cenário referenciado.",
    "Detalhamento dos cenários (ver fichas em `10-cenarios/`); códigos de POST; passo a passo das "
    "ferramentas.",
    [
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md) — destino dos IDs referenciados",
        "[Fluxo de diagnóstico POST](06-fluxo-post.md) — detalhamento da faixa pré-boot",
        "[Validação final por componente](13-validacao-final.md) — critérios usados no nó F14",
        "[Correlações entre camadas](12-correlacoes.md) — armadilhas que este fluxo não cobre",
    ],
    secao="diagnosticar", nivel=0,
    resumo="Árvore de decisão de ponta a ponta: do botão Power até o laudo final, passando por "
           "energia, vídeo, boot, estabilidade, disco e memória.",
    aplica_se="Qualquer atendimento, do primeiro contato ao encerramento",
)

t += """## Objetivo

Conduzir o diagnóstico do estado elétrico até a validação final, sem saltar etapas, registrando em
cada nó a decisão tomada.

## Quando utilizar

A partir do nó **F01**, em qualquer atendimento. O fluxo cobre tanto a faixa pré-boot (F01–F05)
quanto o comportamento pós-boot (F06–F14).

## Pré-requisitos

Os pré-requisitos não estão declarados em campo próprio na fonte. As ferramentas exigidas por nó
estão na coluna *Ferramentas*, reproduzida abaixo.

## Mapa de nós

| Nó | Condição / pergunta | SE verdadeiro → | SE falso → | ID de cenário |
| --- | --- | --- | --- | --- |
"""
for r in nos:
    t += (f"| {tcell(r[H7['Nó']])} | {tcell(r[H7['Condição / Pergunta']])} | "
          f"{tcell(r[H7['SE Verdadeiro →']])} | {tcell(r[H7['SE Falso →']])} | "
          f"{tcell(r[H7['Referência (ID)']])} |\n")

t += """
## Diagrama do fluxo

Reprodução visual das colunas `Nó`, `Condição / Pergunta`, `SE Verdadeiro →` e `SE Falso →`.
O texto integral de cada nó está na seção seguinte.

```mermaid
flowchart TD
    F01{"F01<br/>O equipamento liga?"}
    F02{"F02<br/>PSU passa no teste<br/>de paperclip?"}
    F02b{"F02b<br/>Placa responde ao curto<br/>do PWR_SW?"}
    F03{"F03<br/>O sistema exibe vídeo?"}
    F04{"F04<br/>Debug LED indica DRAM?"}
    F05{"F05<br/>Debug LED indica VGA?"}
    F06{"F06<br/>Boot do SO completa?"}
    F07{"F07<br/>BSOD durante boot?"}
    F08{"F08<br/>Opera estável em<br/>uso normal?"}
    F09{"F09<br/>Reinício aleatório?"}
    F09b{"F09b<br/>Freeze completo?"}
    F09c{"F09c<br/>Lentidão com alto<br/>uso de CPU?"}
    F10{"F10<br/>Discos reconhecidos?"}
    F11{"F11<br/>Temperaturas em spec?"}
    F12{"F12<br/>S.M.A.R.T. saudável?"}
    F13{"F13<br/>MemTest86 4 passes<br/>sem erros?"}
    F14(["F14<br/>DIAGNÓSTICO COMPLETO<br/>Sistema validado"])

    A02["Substituir PSU"]
    A02b1["Substituir botão / front panel"]
    A02b2["Inspecionar placa-mãe<br/>Substituir se danificada"]
    A04["Reencaixar RAM<br/>1 módulo, slot primário"]
    A05a["Remover GPU dedicada<br/>Testar iGPU / teste cruzado"]
    A05b["CMOS Clear<br/>Verificar CPU / firmware"]
    A07a["Analisar código de BSOD"]
    A07b["Verificar logs de boot"]
    A09["Testar PSU<br/>senão MemTest86"]
    A09b["Verificar temperatura"]
    A09c["Process Explorer<br/>Verificar malware"]
    A10["Cabos SATA, portas,<br/>BIOS AHCI, teste cruzado"]
    A11["Manutenção térmica"]
    A12["Backup imediato<br/>Victoria Scan + Remap"]
    A13["Isolar pente defeituoso<br/>RMA"]

    F01 -->|Sim| F03
    F01 -->|Não| F02
    F02 -->|Sim| F02b
    F02 -->|Não| A02
    F02b -->|Sim| A02b1
    F02b -->|Não| A02b2
    F03 -->|Sim| F06
    F03 -->|Não| F04
    F04 -->|Sim| A04
    F04 -->|Não| F05
    F05 -->|Sim| A05a
    F05 -->|Não| A05b
    F06 -->|Sim| F08
    F06 -->|Não| F07
    F07 -->|Sim| A07a
    F07 -->|Não| A07b
    F08 -->|Sim| F10
    F08 -->|Não| F09
    F09 -->|Sim| A09
    F09 -->|Não| F09b
    F09b -->|Sim| A09b
    F09b -->|Não| F09c
    F09c -->|Sim| A09c
    F09c -->|Não| F10
    F10 -->|Sim| F11
    F10 -->|Não| A10
    F11 -->|Sim| F12
    F11 -->|Não| A11
    F12 -->|Sim| F13
    F12 -->|Não| A12
    F13 -->|Sim| F14
    F13 -->|Não| A13
```

> Losangos são nós de decisão; retângulos são ações terminais declaradas na fonte. Os textos foram
> condensados para caber no diagrama — o conteúdo integral está abaixo, sem cortes.
> Nível de confiança: **Confirmado** (topologia e ramos) / **Inferido** (condensação dos rótulos).

---

## Nós detalhados

"""
for r in nos:
    t += f"### {cell(r[H7['Nó']])}\n\n"
    t += field("Condição / pergunta", r[H7["Condição / Pergunta"]], 4) + "\n"
    t += field("SE verdadeiro →", r[H7["SE Verdadeiro →"]], 4) + "\n"
    t += field("SE falso →", r[H7["SE Falso →"]], 4) + "\n"
    t += field("Ação", r[H7["Ação"]], 4) + "\n"
    t += field("Ferramentas", r[H7["Ferramentas"]], 4) + "\n"
    ref = r[H7["Referência (ID)"]]
    t += "#### Referência (ID)\n\n"
    if ref.strip() and ref.strip() != "—":
        links = []
        for i in [x.strip() for x in ref.split(",") if x.strip()]:
            links.append(f"[{i}](10-cenarios/00-indice-cenarios.md)")
        t += ", ".join(links) + "\n\n"
    else:
        t += f"{cell(ref) or '—'} (sem cenário associado na fonte)\n\n"
    t += "---\n\n"

t += """## Quando interromper

O nó **F14** é terminal: a fonte o descreve como "DIAGNÓSTICO COMPLETO. Sistema validado." e
determina a geração de relatório final com classificação em *Saudável*, *Manutenção Preventiva* ou
*Condenado*.

## Observações

Os nós **F06** e **F08** não possuem ID de cenário associado na fonte (campo preenchido com "—").
"""
t += doc_footer(SRC7, proximos=[
    ("chegou a uma ação e quer o procedimento detalhado",
     "[Índice de cenários](10-cenarios/00-indice-cenarios.md)"),
    ("está antes do boot e precisa interpretar um sinal",
     "[Fluxo de diagnóstico POST](06-fluxo-post.md)"),
    ("chegou ao nó F14", "[Validação final por componente](13-validacao-final.md)"),
    ("o sintoma parece apontar para a peça errada",
     "[Correlações entre camadas](12-correlacoes.md)"),
])
open(f"{OUT}/07-fluxo-sistemico.md", "w").write(t)

# =========================================================================
# 08 — Camadas de diagnóstico
# =========================================================================
SRC8 = "`HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Camadas de Diagnóstico`"
cd = cod["Camadas de Diagnóstico"]
H8 = {h: i for i, h in enumerate(cd[1])}
camadas = cd[2:]

t = doc_header(
    "Diagnóstico por camada (modelo POST, 7 camadas)",
    SRC8,
    "Ficha técnica de cada subsistema do modelo de camadas usado pelo catálogo de códigos de POST. "
    "É a referência para saber *o que testar* depois que um código apontou uma camada.",
    "As 7 camadas registradas na fonte, com componentes, sintomas típicos, testes primários, "
    "ferramentas e indicadores de falha.",
    "O modelo de camadas de 10 níveis usado pelo arquivo de fluxo sistêmico (ver taxonomia); "
    "fichas de código; cenários pós-boot.",
    [
        "[Taxonomia de camadas](03-taxonomia-camadas.md) — **leia antes**: existem dois modelos distintos",
        "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md) — cada código aponta uma camada",
        "[Fluxo de diagnóstico POST](06-fluxo-post.md)",
    ],
    secao="diagnosticar", nivel=0,
    resumo="O que testar em cada subsistema: componentes, sintomas típicos, testes primários, "
           "ferramentas e indicadores de falha.",
    aplica_se="Consulta após um código de POST apontar uma camada",
)

t += f"""> [!IMPORTANT]
> As camadas descritas aqui pertencem ao modelo de **7 camadas** do arquivo
> `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx`. O arquivo `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` usa uma
> numeração **diferente e incompatível**: camada 3 é *Memória* aqui e *CPU* lá.
> Confira sempre o formato do número antes de usá-lo — ver
> [Taxonomia de camadas](03-taxonomia-camadas.md).

## Ordem de verificação das camadas

O firmware inicializa os subsistemas em sequência. Uma camada só é alcançada se a anterior
respondeu, e é por isso que a ordem abaixo também é a ordem de teste: não adianta investigar
memória enquanto a alimentação da CPU não estiver confirmada.

```mermaid
flowchart LR
    C1["1<br/>ENERGIA<br/>PSU e VRM"] --> C2["2<br/>CPU<br/>Processador"]
    C2 --> C3["3<br/>MEMÓRIA<br/>RAM"]
    C3 --> C4["4<br/>VÍDEO<br/>GPU e iGPU"]
    C4 --> C7["7<br/>PERIFÉRICOS<br/>Disco, USB, PCIe"]
    C5["5<br/>CHIPSET<br/>Placa-mãe"] -.->|"sustenta<br/>todas"| C1
    C6["6<br/>FIRMWARE<br/>BIOS e UEFI"] -.->|"controla<br/>a sequência"| C2
```

> [!NOTE]
> As camadas 1 a 4 e a 7 seguem a sequência de inicialização declarada nas fichas
> (`Fase POST`: energia → CPU → memória → vídeo → periféricos). As camadas 5 e 6 aparecem
> tracejadas porque a fonte as descreve como transversais: falham em qualquer ponto da sequência.
> Nível de confiança: **Confirmado** (as sete camadas e seus conteúdos) /
> **Inferido** (a representação da ordem).

## Título declarado na fonte

**{cell(cd[0][0])}**

## Resumo das camadas

| Camada | Nome | Sintomas típicos |
| --- | --- | --- |
"""
for r in camadas:
    t += f"| {tcell(r[H8['CAMADA']])} | {tcell(r[H8['NOME']])} | {tcell(r[H8['SINTOMAS TÍPICOS']])} |\n"

# códigos atribuídos a cada camada (coluna CAMADA DE DIAGNÓSTICO do catálogo)
FAM_ARQ = {
    "AMI (Legacy BIOS)": "ami-legacy", "AMI (UEFI/Aptio V)": "ami-uefi-aptio",
    "AMI (Q-Code Hex)": "ami-q-code", "Award BIOS": "award", "Phoenix BIOS": "phoenix",
    "Proprietário Dell": "dell", "Proprietário HP": "hp", "Proprietário Lenovo": "lenovo",
    "Apple (EFI)": "apple", "Proprietário Acer / Insyde": "acer-insyde",
    "Genérico (Múltiplos)": "generico-debug-led",
}
_post = cod["Tabela Diagnóstico POST"]
_HP = {h: i for i, h in enumerate(_post[2])}
CODIGOS_POR_CAMADA = {}
for _n, _r in enumerate(_post[3:], start=1):
    _pid = f"POST-{_n:02d}"
    _arq = FAM_ARQ[_r[_HP["FABRICANTE BIOS"]]]
    _lnk = f"09-codigos-post/{_arq}.md#{gh_anchor(_pid + ' — ' + cell(_r[_HP['CÓDIGO']]))}"
    for _cam in [x.strip() for x in _r[_HP["CAMADA DE DIAGNÓSTICO"]].split("/")]:
        _num = re.match(r"Camada (\d+)", _cam)
        if _num:
            CODIGOS_POR_CAMADA.setdefault(_num.group(1), []).append(
                (_pid, _r[_HP["CÓDIGO"]], _lnk))

t += "\n---\n\n## Fichas de camada\n\n"
for r in camadas:
    t += f"### Camada {cell(r[H8['CAMADA']])} — {cell(r[H8['NOME']])}\n\n"
    t += field("Componentes", r[H8["COMPONENTES"]], 4) + "\n"
    t += field("Sintomas típicos", r[H8["SINTOMAS TÍPICOS"]], 4) + "\n"
    t += field("Testes primários", r[H8["TESTES PRIMÁRIOS"]], 4) + "\n"
    t += field("Ferramentas", r[H8["FERRAMENTAS"]], 4) + "\n"
    t += field("Indicadores de falha", r[H8["INDICADORES DE FALHA"]], 4) + "\n"
    _cods = CODIGOS_POR_CAMADA.get(r[H8["CAMADA"]].strip(), [])
    t += "#### Códigos de POST atribuídos a esta camada\n\n"
    if _cods:
        t += (f"{len(_cods)} código(s), conforme a coluna `CAMADA DE DIAGNÓSTICO` do catálogo:\n\n")
        for _pid, _cd, _lnk in _cods:
            t += f"- [{_pid}]({_lnk}) — `{cell(_cd)}`\n"
        t += "\n"
    else:
        t += "Nenhum código do catálogo aponta exclusivamente para esta camada.\n\n"
    t += "---\n\n"

t += doc_footer(SRC8, proximos=[
    ("quer a ficha do código que apontou esta camada",
     "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md)"),
    ("não sabe qual modelo de camada está lendo",
     "[Taxonomia de camadas](03-taxonomia-camadas.md)"),
    ("precisa montar a bancada", "[Requisitos e ferramentas](04-requisitos-e-ferramentas.md)"),
    ("terminou o teste e quer validar",
     "[Validação final por componente](13-validacao-final.md)"),
])
open(f"{OUT}/08-diagnostico-por-camada.md", "w").write(t)

# =========================================================================
# 11 — Ambiguidade de códigos
# =========================================================================
SRC11 = "`HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Ambiguidade de Códigos`"
am = cod["Ambiguidade de Códigos"]
H11 = {h: i for i, h in enumerate(am[1])}
ambs = am[2:]

t = doc_header(
    "Ambiguidade de códigos",
    SRC11,
    "Alguns sinais de POST têm significados diferentes conforme o fabricante do BIOS ou o momento em "
    "que aparecem. Este documento reúne os casos registrados na fonte e o critério para diferenciá-los.",
    f"Os {len(ambs)} códigos ambíguos registrados, com os significados concorrentes por fabricante, "
    "o critério de diferenciação e o teste para identificar a causa.",
    "Fichas completas dos códigos (ver catálogo); fluxos; cenários pós-boot.",
    [
        "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md)",
        "[Fluxo de diagnóstico POST](06-fluxo-post.md) — Etapa 4 remete a este tratamento",
        "[Camadas de diagnóstico](08-diagnostico-por-camada.md)",
    ],
    secao="resolver", nivel=0,
    resumo="Sinais que significam coisas diferentes conforme o fabricante ou o momento em que "
           "aparecem, e o critério para diferenciá-los.",
    aplica_se="Beeps, Q-Codes e LEDs cujo significado depende do contexto",
)
t += """## Como desempatar

```mermaid
flowchart TD
    A(["Você anotou o sinal"]) --> B{"O sinal está<br/>nesta página?"}
    B -->|"Não"| N["Siga a ficha do código<br/>no catálogo — sem ambiguidade registrada"]
    B -->|"Sim"| C{"Que tipo<br/>de sinal?"}

    C -->|"Bipes"| D{"Qual fabricante<br/>de BIOS?"}
    C -->|"Q-Code FF"| E{"O FF apareceu<br/>quando?"}
    C -->|"LED CPU aceso,<br/>sem POST"| F["Verifique o conector EPS<br/>de 8 pinos primeiro"]

    D -->|"Não sei"| G["Identifique pela tela de abertura,<br/>pelo adesivo na placa<br/>ou pelo manual"]
    D -->|"Já sei"| H["Aplique o significado<br/>daquele fabricante"]

    E -->|"Imediatamente ao ligar,<br/>e ficou parado"| I["Trate como falha grave"]
    E -->|"Depois de outros códigos<br/>passarem na tela"| J["Comportamento normal:<br/>verifique vídeo e monitor"]

    G --> H
    F --> K(["Aplique o teste de<br/>identificação da ficha"])
    H --> K
    I --> K
    J --> K
```

> [!TIP]
> Todo caso desta página traz um campo **Teste para identificar a causa**: é uma sequência curta
> que resolve o empate na prática, sem depender de saber o fabricante de antemão.

## Título declarado na fonte

""" + f"**{cell(am[0][0])}**\n\n---\n\n"

for r in ambs:
    t += f"## {cell(r[H11['CÓDIGO AMBÍGUO']])}\n\n"
    t += "### Significados concorrentes\n\n| Fabricante | Significado |\n| --- | --- |\n"
    for a, b in [("FABRICANTE 1", "SIGNIFICADO 1"), ("FABRICANTE 2", "SIGNIFICADO 2"),
                 ("FABRICANTE 3", "SIGNIFICADO 3")]:
        fab, sig = r[H11[a]], r[H11[b]]
        if fab.strip() and fab.strip() != "—":
            t += f"| {tcell(fab)} | {tcell(sig)} |\n"
    t += "\n"
    t += field("Critério de diferenciação", r[H11["CRITÉRIO DE DIFERENCIAÇÃO"]], 3) + "\n"
    t += field("Teste para identificar a causa", r[H11["TESTE PARA IDENTIFICAR CAUSA"]], 3) + "\n---\n\n"

t += doc_footer(SRC11, proximos=[
    ("desempatou e quer o procedimento completo",
     "[Índice de códigos POST](09-codigos-post/00-indice-codigos.md)"),
    ("ainda não identificou o tipo de sinal", "[Fluxo de diagnóstico POST](06-fluxo-post.md)"),
    ("quer saber o que testar naquele subsistema",
     "[Diagnóstico por camada](08-diagnostico-por-camada.md)"),
])
open(f"{OUT}/11-ambiguidades.md", "w").write(t)

# =========================================================================
# 12 — Correlações
# =========================================================================
SRC12 = "`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `CORRELACOES`"
co = flu["CORRELACOES"]
H12 = {h: i for i, h in enumerate(co[0])}
cors = co[1:]

t = doc_header(
    "Correlações entre camadas (efeitos em cascata)",
    SRC12,
    "Casos em que a falha de uma camada produz sintoma em outra, levando o técnico a trocar o "
    "componente errado. Cada registro traz o mecanismo de propagação, a armadilha comum e como "
    "distinguir causa de sintoma.",
    f"As {len(cors)} correlações registradas na fonte (COR-01 a COR-{len(cors):02d}).",
    "Procedimentos de correção (ver cenários); códigos de POST; validação pós-reparo.",
    [
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md)",
        "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md)",
        "[Validação final por componente](13-validacao-final.md)",
        "[Taxonomia de camadas](03-taxonomia-camadas.md) — as camadas citadas aqui seguem o modelo sistêmico",
    ],
    secao="resolver", nivel=0,
    resumo="Falhas que se manifestam em outro subsistema e levam à troca do componente errado, "
           "com o critério para separar causa de sintoma.",
    aplica_se="Casos em que o problema retorna depois da troca de peça",
)
t += """## Quando desconfiar de uma cascata

```mermaid
flowchart TD
    A(["Você trocou a peça<br/>que o sintoma apontava"]) --> B{"O problema<br/>voltou?"}
    B -->|"Não"| OK(["Diagnóstico correto.<br/>Siga para a validação final"])
    B -->|"Sim"| C{"Qual era<br/>o sintoma?"}

    C -->|"Tela azul variada,<br/>arquivos corrompidos"| D["Verifique a fonte antes<br/>da memória — COR-01"]
    C -->|"Windows corrompe<br/>toda hora"| E["Teste a memória antes<br/>de formatar — COR-02"]
    C -->|"Peça nova não<br/>é reconhecida"| F["Atualize a BIOS antes<br/>de devolver a peça — COR-03"]
    C -->|"Lentidão extrema<br/>e desligamento"| G["Meça a temperatura antes<br/>de culpar a fonte — COR-04"]
    C -->|"Tela azul de memória,<br/>mas MemTest passa"| H["Verifique o S.M.A.R.T.<br/>do disco — COR-05"]
    C -->|"Tela preta rápida,<br/>driver de vídeo cai"| I["Reinstale o driver antes<br/>de acusar a GPU — COR-06"]
```

> [!WARNING]
> Todo caso desta página começa com um técnico trocando uma peça boa. O prejuízo não é só a peça:
> o problema real segue no equipamento e volta para a bancada.

## Resumo

| ID | Falha primária | Efeito cascata | Sintoma resultante |
| --- | --- | --- | --- |
"""
for r in cors:
    t += (f"| [{tcell(r[H12['ID']])}](#{gh_anchor(r[H12['ID']])}) | {tcell(r[H12['Falha Primária (Camada)']])} | "
          f"{tcell(r[H12['Efeito Cascata (Camada)']])} | {tcell(r[H12['Sintoma Resultante']])} |\n")
t += "\n---\n\n"

for r in cors:
    t += f"## {cell(r[H12['ID']])}\n\n"
    t += f"**Falha primária (camada):** {cell(r[H12['Falha Primária (Camada)']])}  \n"
    t += f"**Efeito cascata (camada):** {cell(r[H12['Efeito Cascata (Camada)']])}\n\n"
    t += field("Mecanismo de propagação", r[H12["Mecanismo de Propagação"]], 3) + "\n"
    t += field("Sintoma resultante", r[H12["Sintoma Resultante"]], 3) + "\n"
    t += field("Diagnóstico diferencial", r[H12["Diagnóstico Diferencial"]], 3) + "\n"
    t += field("Armadilha comum", r[H12["Armadilha Comum"]], 3) + "\n"
    t += field("Como distinguir", r[H12["Como Distinguir"]], 3) + "\n"
    t += field("Fonte", r[H12["Fonte"]], 3) + "\n---\n\n"

t += doc_footer(SRC12, proximos=[
    ("confirmou a causa real e quer o procedimento",
     "[Índice de cenários](10-cenarios/00-indice-cenarios.md)"),
    ("precisa comprovar antes de trocar a peça",
     "[Validação final por componente](13-validacao-final.md)"),
    ("quer monitorar tensões ou temperatura",
     "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)"),
])
open(f"{OUT}/12-correlacoes.md", "w").write(t)

# =========================================================================
# 13 — Validação final
# =========================================================================
SRC13 = "`HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `VALIDACAO_FINAL`"
vf = flu["VALIDACAO_FINAL"]
H13 = {h: i for i, h in enumerate(vf[0])}
vals = vf[1:]

t = doc_header(
    "Validação final por componente",
    SRC13,
    "Critérios objetivos de aprovação e reprovação aplicados **depois** da correção, por componente. "
    "É o que fecha o atendimento e sustenta o laudo.",
    f"Os {len(vals)} componentes com teste pós-correção, ferramenta, indicador de sucesso, tempo de "
    "observação, critério PASS, critério FAIL e ação em caso de reprovação.",
    "Como chegar ao diagnóstico (ver fluxos e cenários); operação detalhada das ferramentas.",
    [
        "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md) — nó F14 usa estes critérios",
        "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)",
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md)",
    ],
    secao="fechar", nivel=0,
    resumo="Critérios objetivos de aprovação e reprovação por componente, com tempo de observação "
           "e encaminhamento em caso de falha.",
    aplica_se="Encerramento de atendimento e emissão de laudo",
)
t += """## Como fechar o atendimento

```mermaid
flowchart TD
    A(["Correção aplicada"]) --> B["Escolha o componente<br/>na matriz abaixo"]
    B --> C["Execute o teste<br/>pós-correção indicado"]
    C --> D["Observe pelo tempo<br/>exigido na ficha"]
    D --> E{"Atendeu ao<br/>critério PASS?"}
    E -->|"Sim"| F["Registre a evidência<br/>no laudo"]
    E -->|"Não"| G["Aplique a<br/>Ação se FAIL"]
    G --> H{"A ação resolveu?"}
    H -->|"Sim"| C
    H -->|"Não"| I["Componente condenado:<br/>substituição ou RMA"]
    F --> J{"Faltam outros<br/>componentes?"}
    J -->|"Sim"| B
    J -->|"Não"| K(["Sistema validado"])
    I --> J
```

> [!IMPORTANT]
> O tempo de observação faz parte do critério. Vários componentes exigem acompanhamento por 48 h
> ou 72 h de uso normal **depois** do teste de bancada: aprovar antes disso devolve ao cliente um
> equipamento não validado.

## Matriz de validação

"""
t += "| Componente | Critério PASS | Critério FAIL | Tempo de observação |\n| --- | --- | --- | --- |\n"
for r in vals:
    t += (f"| [{tcell(r[H13['Componente']])}](#{gh_anchor(r[H13['Componente']])}) | {tcell(r[H13['Critério PASS']])} | "
          f"{tcell(r[H13['Critério FAIL']])} | {tcell(r[H13['Tempo de Observação']])} |\n")
t += "\n---\n\n## Detalhamento\n\n"
for r in vals:
    t += f"## {cell(r[H13['Componente']])}\n\n"
    t += field("Teste pós-correção", r[H13["Teste Pós-Correção"]], 3) + "\n"
    t += field("Ferramenta de validação", r[H13["Ferramenta de Validação"]], 3) + "\n"
    t += field("Indicador de sucesso", r[H13["Indicador de Sucesso"]], 3) + "\n"
    t += field("Tempo de observação", r[H13["Tempo de Observação"]], 3) + "\n"
    t += field("Critério PASS", r[H13["Critério PASS"]], 3) + "\n"
    t += field("Critério FAIL", r[H13["Critério FAIL"]], 3) + "\n"
    t += field("Ação se FAIL", r[H13["Ação se FAIL"]], 3) + "\n---\n\n"

t += doc_footer(SRC13, proximos=[
    ("reprovou e precisa reabrir o diagnóstico",
     "[Índice de cenários](10-cenarios/00-indice-cenarios.md)"),
    ("desconfia que a causa está em outra camada",
     "[Correlações entre camadas](12-correlacoes.md)"),
    ("precisa operar a ferramenta de validação",
     "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)"),
    ("quer conferir onde a validação entra no fluxo",
     "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md)"),
])
open(f"{OUT}/13-validacao-final.md", "w").write(t)

print("fluxos/camadas/ambiguidades/correlações/validação gerados")
