import os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
os.makedirs(f"{OUT}/references", exist_ok=True)
cod = read(F_COD)
flu = read(F_FLU)

# =========================================================================
# 15 — Limitações
# =========================================================================
t = doc_header(
    "Limitações conhecidas",
    "Verificação direta sobre ambos os arquivos-fonte",
    "Registro honesto do que esta base **não** entrega. Cada item foi verificado contra os arquivos "
    "de origem; nenhum é suposição.",
    "Lacunas de metadados, conflitos entre fontes, campos vazios, cobertura técnica ausente e "
    "limites de uso.",
    "Itens que exigem decisão do proprietário do projeto — esses estão em "
    "[references/pendencias.md](references/pendencias.md).",
    [
        "[Pendências](references/pendencias.md)",
        "[Taxonomia de camadas](03-taxonomia-camadas.md)",
        "[Fontes](references/fontes.md)",
        "[FAQ](16-faq.md)",
    ],
    secao="referencia", nivel=0,
    resumo="O que esta base não entrega, verificado item a item contra os arquivos de origem.",
    aplica_se="Avaliação de confiança antes de decidir com base neste material",
)

t += """## 1. Metadados do projeto ausentes

Os dois arquivos `.xlsx` não contêm `docProps/core.xml` — o registro interno onde autor, título,
data de criação e revisão são gravados. Consequência direta:

| Informação | Situação |
| --- | --- |
| Nome oficial do projeto | Não identificada na fonte analisada |
| Versão | Não identificada na fonte analisada |
| Autor / responsável técnico | Não identificada na fonte analisada |
| Licença de uso | Não identificada na fonte analisada |
| Data de elaboração | Não identificada na fonte analisada |

Nenhum desses campos foi preenchido por dedução.

## 2. Conflito de taxonomia entre as fontes

Os dois arquivos numeram as camadas de diagnóstico de forma **incompatível**. Camada 3 é *Memória*
em um e *CPU* no outro. Detalhamento e regra de uso em
[03-taxonomia-camadas.md](03-taxonomia-camadas.md).

O modelo de 10 camadas usado pelo arquivo de fluxo **não possui tabela de definição** em nenhuma
aba: foi reconstruído a partir das ocorrências literais. As camadas 2 (*Firmware*), 8
(*Periféricos*) e 10 (*Drivers*) aparecem apenas na aba `CORRELACOES`; a camada 7 (*Placa-mãe*)
aparece apenas em `TABELA_PRINCIPAL`. Nenhuma delas tem ficha técnica equivalente ao
[documento 08](08-diagnostico-por-camada.md).

## 3. Divergências de procedimento entre as fontes

Quatro divergências foram identificadas e **não foram resolvidas** — ambas as versões estão
preservadas nos documentos correspondentes:

| Tema | Versão A | Versão B |
| --- | --- | --- |
| Duração do *power drain* | 30 s (`CODIGOS_DE_ERROS`, vários registros) | 10 s (`FLUXO_DIAGNOSTICO`, NL-01) |
| Composição do *boot mínimo* | "CPU + 1 RAM + fonte"; "CPU+RAM+Vídeo apenas" (`CODIGOS_DE_ERROS`) | "CPU+Cooler+1RAM+PSU apenas" (`FLUXO_DIAGNOSTICO`, F02b) |
| Limiar térmico em idle | ">60 °C em idle → problema térmico confirmado" (SA-01) | ">90 °C em idle → problema térmico" (COR-04) |
| Critério FAIL de temperatura | Linha *CPU*: Temp > 95 °C | Linha *Térmico*: Temp > 90 °C (mesma aba `VALIDACAO_FINAL`) |

Registro completo em [references/pendencias.md](references/pendencias.md).

## 4. Campos vazios na origem

| Aba | Campo | Vazios |
| --- | --- | --- |
| `REF_Victoria` | Atalho de Teclado | 6 de 9 etapas |
| `REF_AIDA64` | Atalho de Teclado | 42 de 45 etapas |
| `REF_AIDA64` | Alternativa Segura | 4 de 45 etapas |
| `REF_MemTest86` | Atalho de Teclado | 8 de 10 etapas |
| `REF_MemTest86` | Alternativa Segura | 6 de 10 etapas |

As demais colunas das abas `Tabela Diagnóstico POST` e `TABELA_PRINCIPAL` estão **100 %
preenchidas**. Onde há vazio, o documento correspondente registra
*"Informação não identificada na fonte analisada"* em vez de omitir a seção.

## 5. Anomalias estruturais nas fontes

- **`REF_MemTest86`, última linha:** contém um bloco de critérios de decisão pós-teste ocupando a
  coluna `Nº da Etapa`. Não é uma etapa do procedimento. Preservado como seção própria em
  [memtest86.md](14-ferramentas/memtest86.md).
- **`FLUXO_LOGICO`, nós F06 e F08:** não possuem ID de cenário associado (campo preenchido com "—").
- **`TABELA_PRINCIPAL`, ID FI-01:** existe na tabela e no índice de cenários, mas **não é alcançado
  por nenhum nó** do fluxo sistêmico.
- **Códigos de POST não possuem identificador na fonte.** O campo `POST-NN` usado nesta
  documentação foi criado para permitir link estável e está sempre acompanhado do código literal.

## 6. Cobertura técnica ausente

Verificado por leitura integral das fontes:

- **Sem procedimento para reparo em nível de componente.** A fonte cita "reparo em nível de
  componente (BGA, capacitor, etc.)" apenas como escalação final, sem detalhar.
- **Lenovo SmartBeep sem procedimento próprio.** O registro correspondente traz "Variável" na
  maior parte dos campos e remete ao aplicativo Lenovo PC Diagnostics.
- **Beep contínuo de teclado (AMI) sem ficha.** A aba de ambiguidades menciona que, em algumas
  versões AMI, beep contínuo indica tecla presa — mas não há entrada correspondente no catálogo de
  códigos, que registra beep contínuo apenas para Award (memória).
- **Sem cobertura de memória ECC, servidores com BMC/IPMI, plataformas ARM ou Apple Silicon.** O
  material Apple documentado cobre Mac com processador Intel.
- **Sem procedimento para notebooks além do que aparece pontualmente** dentro de registros
  específicos (Dell LCD/eDP, Acer cabo flat, compartimento SO-DIMM).
- **Sem dados de custo, tempo médio de reparo ou disponibilidade de peças.**

## 7. Limites de uso do material

- Os procedimentos envolvem medição elétrica e abertura de equipamento. A fonte registra riscos
  ("Crítico", "Alto", "Médio", "Baixo") por procedimento, mas **não contém instruções de segurança
  do trabalho** além das menções pontuais nos próprios registros.
- Vários procedimentos são **destrutivos para dados** — em especial as etapas de escrita e
  zero-fill do guia Victoria. A fonte alerta nos campos de risco de cada etapa.
- A base **não substitui** o manual do fabricante da placa-mãe ou do equipamento. Vários registros
  remetem explicitamente a ele (pinagem de front panel, seção Q-Code, QVL, lista de CPUs
  suportadas).

## 8. Limite desta documentação

Esta base reflete **apenas** o conteúdo das duas planilhas na data de análise. Não houve consulta
a fontes externas, nem verificação independente das afirmações técnicas contra a documentação
oficial dos fabricantes citados — embora a fonte declare basear-se nela e informe a referência em
cada registro.
"""
t += doc_footer("Verificação direta sobre ambos os arquivos-fonte",
                conf="Confirmado — cada item verificado contra a origem", proximos=[
    ("quer o que exige decisão sua", "[Pendências](references/pendencias.md)"),
    ("quer entender o conflito de camadas", "[Taxonomia de camadas](03-taxonomia-camadas.md)"),
    ("quer conferir a origem de uma informação", "[Fontes](references/fontes.md)"),
])
open(f"{OUT}/15-limitacoes.md", "w").write(t)

# =========================================================================
# 16 — FAQ
# =========================================================================
t = doc_header(
    "Perguntas frequentes",
    "Ambos os arquivos-fonte",
    "Perguntas derivadas exclusivamente de conteúdo já documentado. Cada resposta remete ao "
    "documento que trata o assunto em profundidade.",
    "Dúvidas de navegação, de interpretação de código e de decisão de procedimento que a fonte "
    "responde.",
    "Dúvidas não cobertas pelas fontes — essas estão em [15-limitacoes.md](15-limitacoes.md).",
    [
        "[Como utilizar](05-utilizacao.md)",
        "[Limitações](15-limitacoes.md)",
        "[Glossário](17-glossario.md)",
    ],
    secao="referencia", nivel=0,
    resumo="Dúvidas derivadas de ambiguidade, armadilha ou decisão explicitamente registrada nas "
           "fontes, com link para o documento que trata cada assunto.",
    aplica_se="Consulta rápida durante o atendimento",
)

t += """> Nenhuma pergunta abaixo foi criada para aumentar o volume da documentação. Todas derivam de
> ambiguidade, armadilha ou decisão explicitamente registrada nas fontes.

## Sobre navegação

### Por onde começo se o equipamento não dá sinal nenhum?

Pela Etapa 1 do [fluxo de POST](06-fluxo-post.md), que verifica energia antes de qualquer outra
coisa, e pela ficha do cenário [Não liga](10-cenarios/nao-liga.md).

### Qual a diferença entre o fluxo de POST e o fluxo sistêmico?

O [fluxo de POST](06-fluxo-post.md) atua enquanto o firmware ainda tem o controle, e sua saída é a
identificação de um código de erro. O [fluxo sistêmico](07-fluxo-sistemico.md) vai do botão Power
até a validação final, cobrindo também o comportamento depois que o sistema operacional carrega.
Eles se sobrepõem na faixa inicial.

### O número da camada significa a mesma coisa em toda a documentação?

Não. Existem dois modelos com numerações diferentes, um por arquivo-fonte. *Camada 3* é *Memória*
em um e *CPU* no outro. Ver [03-taxonomia-camadas.md](03-taxonomia-camadas.md).

## Sobre interpretação de códigos

### O mesmo beep aparece com dois significados. Como decidir?

Identificando primeiro o fabricante do BIOS. O caso "1 Longo + 2 Curtos", por exemplo, é falha de
vídeo em AMI e Award, mas erro de interface de vídeo (cabo flat) em Acer/Insyde. Os cinco casos
registrados e os critérios de diferenciação estão em [11-ambiguidades.md](11-ambiguidades.md).

### O Q-Code mostra FF. É falha ou é normal?

Depende de **quando** o FF aparece. Se surge imediatamente ao ligar e fica fixo, é tratado como
falha grave. Se aparece ao final de uma progressão de códigos, indica que o controle passou ao
sistema. O critério completo e o teste para distinguir estão em
[11-ambiguidades.md](11-ambiguidades.md).

### O código que observei não está no catálogo. E agora?

O fluxo de POST prevê essa situação nas Etapas 4 e 5: anotar o padrão exatamente como observado e
consultar a documentação do fabricante da placa-mãe. Ver [06-fluxo-post.md](06-fluxo-post.md).

### Por que os códigos têm um identificador `POST-NN` que não vejo em lugar nenhum?

Porque a fonte não numera os códigos. O `POST-NN` foi criado nesta documentação apenas para
permitir link estável entre documentos, e sempre aparece junto do código literal. Ver
[02-arquitetura.md](02-arquitetura.md).

## Sobre decisão de procedimento

### Troquei a memória e o problema continua. O que verificar?

As [correlações em cascata](12-correlacoes.md) tratam exatamente disso. COR-01 registra que
instabilidade de fonte provoca bit-flips na memória e corrupção no disco — trocar RAM não resolve,
e o problema retorna com componentes novos.

### Formatei o Windows e os erros voltaram. Por quê?

COR-02 registra esse caso: memória defeituosa corrompe dados durante a gravação, e o sistema
corrompido é sintoma, não causa. A recomendação da fonte é executar MemTest86 antes de reformatar.

### O sistema fica lento e desliga sozinho. É a fonte?

Pode ser térmico. COR-04 registra que uma CPU em throttling contínuo produz lentidão que parece
problema de software, e que a proteção térmica causa desligamento abrupto idêntico a falha de
fonte. A fonte recomenda monitorar temperatura antes de diagnosticar lentidão.

### Quando um componente está condenado?

O critério registrado no fluxo de POST é o teste cruzado: componente que falha em dois sistemas
está condenado; componente que funciona em outro sistema aponta a placa-mãe como culpada. Ver
Etapa 7 em [06-fluxo-post.md](06-fluxo-post.md).

### Quantas passagens de MemTest86 são necessárias?

Os critérios de decisão pós-teste registrados na fonte usam **4 passes** como referência, e
detalham o destino do módulo conforme a quantidade e o padrão de erros. Ver
[memtest86.md](14-ferramentas/memtest86.md).

## Sobre encerramento do atendimento

### Como sei que o reparo está concluído?

Pelo [documento 13](13-validacao-final.md), que define, para cada um dos 10 componentes, o teste
pós-correção, o critério PASS, o critério FAIL e o tempo de observação exigido.

### O que fazer se a validação reprovar?

Cada linha do documento 13 traz o campo *Ação se FAIL* com o encaminhamento previsto.

## Sobre a própria base

### Posso confiar que nada foi inventado?

Os documentos técnicos foram **gerados programaticamente** a partir das células das planilhas, sem
redação intermediária. Onde a origem é omissa, o texto registra a lacuna. A rastreabilidade está em
[references/matriz-rastreabilidade.md](references/matriz-rastreabilidade.md).

### Qual é a versão e quem é o autor deste material?

Informação não identificada na fonte analisada. Os arquivos não contêm metadados de autoria ou
versão. Ver [15-limitacoes.md](15-limitacoes.md).
"""
t += doc_footer("Ambos os arquivos-fonte",
                conf="Confirmado (respostas) — perguntas derivadas do conteúdo", proximos=[
    ("não encontrou sua dúvida aqui", "[Limitações](15-limitacoes.md)"),
    ("quer entrar pelo sintoma", "[README](../README.md)"),
    ("não reconheceu um termo", "[Glossário](17-glossario.md)"),
])
open(f"{OUT}/16-faq.md", "w").write(t)
print("15 e 16 gerados")
