import os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
cod = read(F_COD)
flu = read(F_FLU)
post = cod["Tabela Diagnóstico POST"][3:]
fam = collections.Counter(r[0] for r in post)
sinal = collections.Counter(r[2] for r in post)

INVENTARIO = [
    ("HW_HARDWARE_CODIGOS_DE_ERROS.xlsx", "Tabela Diagnóstico POST", "54 códigos",
     "[09-codigos-post/](09-codigos-post/00-indice-codigos.md)"),
    ("HW_HARDWARE_CODIGOS_DE_ERROS.xlsx", "Fluxo de Diagnóstico", "7 etapas",
     "[06-fluxo-post.md](06-fluxo-post.md)"),
    ("HW_HARDWARE_CODIGOS_DE_ERROS.xlsx", "Camadas de Diagnóstico", "7 camadas",
     "[08-diagnostico-por-camada.md](08-diagnostico-por-camada.md)"),
    ("HW_HARDWARE_CODIGOS_DE_ERROS.xlsx", "Ambiguidade de Códigos", "5 casos",
     "[11-ambiguidades.md](11-ambiguidades.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "TABELA_PRINCIPAL", "13 cenários (IDs)",
     "[10-cenarios/](10-cenarios/00-indice-cenarios.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "FLUXO_LOGICO", "17 nós",
     "[07-fluxo-sistemico.md](07-fluxo-sistemico.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "CORRELACOES", "6 correlações",
     "[12-correlacoes.md](12-correlacoes.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "VALIDACAO_FINAL", "10 componentes",
     "[13-validacao-final.md](13-validacao-final.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "INDICE_CENARIOS", "9 cenários",
     "[10-cenarios/00-indice-cenarios.md](10-cenarios/00-indice-cenarios.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "REF_Victoria", "9 etapas",
     "[14-ferramentas/victoria.md](14-ferramentas/victoria.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "REF_AIDA64", "45 etapas",
     "[14-ferramentas/aida64-etapas-01-15.md](14-ferramentas/aida64-etapas-01-15.md)"),
    ("HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx", "REF_MemTest86", "10 etapas + critérios",
     "[14-ferramentas/memtest86.md](14-ferramentas/memtest86.md)"),
]

# =========================================================================
# 01 — Visão geral
# =========================================================================
t = doc_header(
    "Visão geral",
    "Ambos os arquivos-fonte",
    "Primeiro documento a ler. Explica o que esta base de conhecimento é, o que ela cobre, para "
    "quem foi escrita e o que ela deliberadamente não faz.",
    "Identidade do projeto, propósito, público, conteúdo consolidado e origem dos dados.",
    "Estrutura interna da documentação (ver documento 02); procedimentos técnicos; limitações "
    "detalhadas (ver documento 15).",
    [
        "[Arquitetura da documentação](02-arquitetura.md)",
        "[Como utilizar](05-utilizacao.md)",
        "[Limitações](15-limitacoes.md)",
        "[Fontes](references/fontes.md)",
    ],
    secao="comecar", nivel=0,
    resumo="O que esta base é, o que cobre, para quem foi escrita e o que ela deliberadamente "
           "não faz.",
    aplica_se="Primeira leitura de quem chega ao projeto",
)

t += f"""## Identidade oficial

| Item | Valor |
| --- | --- |
| Nome | {PROJ_NOME} |
| Autor | {PROJ_AUTOR} |
| Repositório | [`{PROJ_OWNER}/{PROJ_REPO}`]({PROJ_URL}) |
| Descrição oficial | {PROJ_DESC} |
| Licença | {PROJ_LICENCA} |
| Proprietário do repositório | `{PROJ_OWNER}` |
| Versão desta documentação | `{DOC_VERSAO}` |

**Nível de confiança: Confirmado.** Todos os valores acima vêm do repositório informado pelo
proprietário e consultado em {DOC_DATA}. Ver [references/fontes.md](references/fontes.md).

## O que é

Base de conhecimento técnica para **diagnóstico de falhas de hardware em computadores**,
convertida a partir de duas planilhas de referência. Reúne, em um único corpo consultável:

- o catálogo de sinais de erro emitidos durante o POST (beeps, Q-Codes, LEDs de diagnóstico) e o
  procedimento associado a cada um;
- os cenários de falha observados após o boot (não liga, tela azul, reinício aleatório,
  superaquecimento, entre outros), com método de diagnóstico e correção;
- os fluxos de decisão que ligam sintoma a procedimento;
- os critérios objetivos de aprovação e reprovação usados para fechar o atendimento;
- os procedimentos operacionais completos de três ferramentas: Victoria, AIDA64 e MemTest86.

## O que as planilhas de origem declaram sobre si

| Item | Situação nas planilhas | Situação após consulta ao repositório |
| --- | --- | --- |
| Nome do projeto | Não declarado | **Confirmado** — ver identidade oficial acima |
| Autor / responsável | Não declarado | **Confirmado** — {PROJ_AUTOR} |
| Licença | Não declarada | **Confirmado** — MIT |
| Versão do conteúdo técnico | Não declarada | **Ainda não declarada** — pendência P-02 |
| Idioma | Português (Brasil), com terminologia técnica em inglês preservada | Confirmado |

> Os arquivos `.xlsx` não contêm `docProps/core.xml`, o registro interno onde o Excel grava autor,
> título e datas. A identificação do projeto foi obtida do repositório, não das planilhas.
> A **versão do conteúdo técnico** continua sem declaração — ver
> [P-02 em references/pendencias.md](references/pendencias.md#p-02--versão-do-conteúdo-técnico).

## Propósito

A subtítulo declarado na primeira planilha define o nível pretendido:

> *"Referência Técnica Tier-3 — Baseado em documentação oficial AMI, Phoenix, Award, Dell, HP,
> Lenovo, Apple, ASUS, Gigabyte"*

O material assume um técnico capaz de operar multímetro, abrir equipamento, medir tensões em
conector ATX e interpretar S.M.A.R.T. Não é material de suporte ao usuário final.

## Conteúdo consolidado

| Conteúdo | Quantidade |
| --- | --- |
| Códigos de POST catalogados | 54 |
| Famílias de BIOS / fabricantes cobertos | 11 |
| Tipos de sinal distintos | 9 |
| Cenários de falha (IDs) | 13, agrupados em 9 cenários |
| Camadas de diagnóstico (modelo POST) | 7 |
| Etapas do fluxo de POST | 7 |
| Nós do fluxo sistêmico | 17 |
| Casos de ambiguidade documentados | 5 |
| Correlações em cascata entre camadas | 6 |
| Componentes com critério de validação final | 10 |
| Etapas operacionais de ferramentas | 64 |

### Distribuição dos códigos por família de BIOS

| Família (literal na fonte) | Códigos |
| --- | --- |
"""
for k, v in fam.most_common():
    t += f"| {tcell(k)} | {v} |\n"

t += "\n### Distribuição por tipo de sinal\n\n| Tipo de sinal | Códigos |\n| --- | --- |\n"
for k, v in sinal.most_common():
    t += f"| {tcell(k)} | {v} |\n"

t += """
## Público-alvo

- Técnicos de manutenção de hardware em bancada.
- Equipes de suporte de nível 2 e 3 que precisam decidir entre reparo, troca de componente e RMA.
- Sistemas de IA que precisem consultar procedimentos de diagnóstico com rastreabilidade de origem.

## O que esta base não faz

- Não substitui o manual do fabricante da placa-mãe ou do equipamento.
- Não cobre reparo em nível de componente (BGA, retrabalho, rebobinamento) — a fonte apenas o
  cita como escalação possível, sem procedimento.
- Não emite recomendação comercial de peças ou fornecedores.
- Não versiona o próprio conteúdo técnico: não há como saber, pela planilha, se um procedimento
  foi revisado.

Ver [Limitações](15-limitacoes.md) para a lista completa e verificada.
"""
t += doc_footer("Ambos os arquivos-fonte", proximos=[
    ("vai usar a base num atendimento", "[Como utilizar](05-utilizacao.md)"),
    ("precisa entender os números de camada", "[Taxonomia de camadas](03-taxonomia-camadas.md)"),
    ("quer saber onde a base é frágil", "[Limitações](15-limitacoes.md)"),
    ("vai manter ou alterar a documentação", "[Arquitetura da documentação](02-arquitetura.md)"),
])
open(f"{OUT}/01-visao-geral.md", "w").write(t)

# =========================================================================
# 02 — Arquitetura
# =========================================================================
t = doc_header(
    "Arquitetura da documentação",
    "Ambos os arquivos-fonte",
    "Explica como o conhecimento foi organizado: quais eixos existem, o que cada documento carrega "
    "e de qual aba de planilha cada documento saiu. É o mapa para quem vai manter a base.",
    "Eixos de organização, princípio de responsabilidade única por documento, mapa "
    "aba-de-origem → documento e convenções adotadas.",
    "Conteúdo técnico em si; procedimentos; navegação por tarefa (ver documento 05).",
    [
        "[Índice da documentação](00-indice.md)",
        "[Visão geral](01-visao-geral.md)",
        "[Fontes](references/fontes.md)",
        "[Matriz de rastreabilidade](references/matriz-rastreabilidade.md)",
    ],
    secao="manutencao", nivel=0,
    resumo="Como o conhecimento foi organizado, de qual aba cada documento saiu e quais "
           "convenções todos seguem.",
    aplica_se="Manutenção da base e auditoria de origem",
)

t += """## Os dois eixos do material

As fontes se organizam em dois eixos que **se encontram no momento do boot**:

**Eixo 1 — pré-boot (POST).** O equipamento ainda não entregou controle ao sistema operacional. O
único canal de informação é o sinal que o firmware emite: beep, código hexadecimal em display,
LED de diagnóstico. Origem: `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx`.

**Eixo 2 — pós-boot (sistêmico).** O equipamento liga e carrega o sistema, mas falha em uso: trava,
reinicia, exibe tela azul, superaquece. O canal de informação passa a ser software: logs, S.M.A.R.T.,
sensores, stress test. Origem: `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx`.

```mermaid
flowchart TD
    P(["Botão Power"]) --> E1

    subgraph E1["EIXO 1 — POST (pré-boot)"]
        direction LR
        A1["06 Fluxo de POST"] --> A2["09 Códigos de POST"]
        A2 --> A3["08 Camadas"]
        A2 --> A4["11 Ambiguidades"]
    end

    E1 -->|"POST concluído"| E2

    subgraph E2["EIXO 2 — sistêmico (pós-boot)"]
        direction LR
        B1["07 Fluxo sistêmico"] --> B2["10 Cenários"]
        B2 --> B3["12 Correlações"]
        B2 --> B4["14 Ferramentas"]
    end

    E2 -->|"correção aplicada"| E3["13 Validação final<br/>fecha o atendimento"]
    E3 --> Z(["Laudo"])
```

> [!NOTE]
> O diagrama acima é uma **representação organizacional** desta documentação. A fonte não contém
> diagrama equivalente. Nível de confiança: **Inferido**, derivado da leitura dos fluxos
> (Etapa 1→7 no eixo 1; F01→F14 no eixo 2).

## Princípio de responsabilidade única

Cada documento tem um dono de assunto. Informação não é duplicada entre documentos: quando um
documento precisa de conteúdo de outro, ele **referencia** em vez de copiar.

| Documento | Responsabilidade exclusiva |
| --- | --- |
| `01-visao-geral.md` | O que o projeto é e o que não é |
| `02-arquitetura.md` | Como a documentação está organizada |
| `03-taxonomia-camadas.md` | Significado dos números de camada e o conflito entre os dois modelos |
| `04-requisitos-e-ferramentas.md` | Instrumental necessário |
| `05-utilizacao.md` | Por onde entrar conforme a situação |
| `06-fluxo-post.md` | Sequência de decisão antes do boot |
| `07-fluxo-sistemico.md` | Sequência de decisão de ponta a ponta |
| `08-diagnostico-por-camada.md` | O que testar em cada subsistema (modelo A) |
| `09-codigos-post/` | Ficha de cada código de erro |
| `10-cenarios/` | Ficha de cada cenário de falha |
| `11-ambiguidades.md` | Códigos com mais de um significado |
| `12-correlacoes.md` | Falha em uma camada que aparece como sintoma em outra |
| `13-validacao-final.md` | Critérios de aprovação e reprovação pós-reparo |
| `14-ferramentas/` | Operação passo a passo de Victoria, AIDA64 e MemTest86 |
| `15-limitacoes.md` | O que a base não cobre e onde ela é frágil |
| `16-faq.md` | Perguntas derivadas do conteúdo documentado |
| `17-glossario.md` | Termos técnicos usados no material |
| `references/` | Origem dos dados, rastreabilidade, pendências e histórico |

## Mapa aba de origem → documento

| Arquivo-fonte | Aba | Volume | Documento gerado |
| --- | --- | --- | --- |
"""
for arq, aba, vol, doc in INVENTARIO:
    t += f"| `{arq}` | `{aba}` | {vol} | {doc} |\n"

t += """
## Convenções adotadas

**Fidelidade ao texto de origem.** Todo campo técnico é transcrição literal da célula
correspondente. Os documentos das pastas `09-codigos-post/`, `10-cenarios/` e `14-ferramentas/`,
mais os documentos 06, 07, 08, 11, 12, 13, 18 e 19, foram **gerados programaticamente** a partir
das planilhas — não foram redigidos manualmente. Isso elimina a possibilidade de paráfrase
acidental. O gerador está no repositório, em `tools/gerar_documentacao.py`.

**Referências cruzadas derivadas.** As ligações entre documentos — código → ficha da camada,
camada → códigos atribuídos, cenário → nós do fluxo que o alcançam, cenário → dependências — não
foram escritas à mão: são calculadas a partir das colunas de classificação e ligação das próprias
planilhas. Se a fonte mudar, elas mudam junto.

**Diagramas.** Os fluxogramas em Mermaid nos documentos 06 e 07 reproduzem a topologia declarada
nas colunas de encadeamento. Os rótulos foram condensados para caber no diagrama; o texto integral
está sempre logo abaixo, sem cortes.

**Identificadores.** Os IDs de cenário (`NL-01`, `SV-02`, …), de nó de fluxo (`F01`…`F14`) e de
correlação (`COR-01`…`COR-06`) **existem na fonte** e foram preservados. O identificador de código
de POST (`POST-01`…`POST-54`) **não existe na fonte**: foi criado nesta documentação, seguindo a
ordem das linhas, para permitir link estável. Está sempre acompanhado do código literal.

**Camadas.** O número de camada é sempre reproduzido no formato original, porque o formato
identifica qual dos dois modelos está em uso. Ver [03-taxonomia-camadas.md](03-taxonomia-camadas.md).

**Lacunas.** Campo vazio na origem gera, no documento, a marcação explícita
*"Informação não identificada na fonte analisada"*. Nenhuma lacuna foi preenchida por dedução.

**Links.** Todos os links entre documentos são relativos.

## Como manter

1. A fonte da verdade continua sendo o arquivo `.xlsx`. Alterações de conteúdo técnico devem ser
   feitas na planilha, não no Markdown.
2. Documentos gerados trazem, na primeira linha, um comentário HTML indicando a aba de origem.
3. Documentos redigidos manualmente (README, 00, 01, 02, 03, 04, 05, 15, 16, 17 e `references/`)
   podem ser editados diretamente, desde que nenhuma afirmação nova seja introduzida sem fonte.
4. Toda mudança deve ser registrada em [references/changelog.md](references/changelog.md).
"""
t += doc_footer("Ambos os arquivos-fonte",
                conf="Confirmado (mapa e volumes) / Inferido (diagrama de eixos)", proximos=[
    ("vai alterar conteúdo técnico", "[Como contribuir](../CONTRIBUTING.md)"),
    ("quer rastrear uma informação até a célula", "[Matriz de rastreabilidade](references/matriz-rastreabilidade.md)"),
    ("quer ver o histórico de mudanças", "[Changelog](references/changelog.md)"),
])
open(f"{OUT}/02-arquitetura.md", "w").write(t)

# =========================================================================
# 05 — Utilização
# =========================================================================
t = doc_header(
    "Como utilizar esta base",
    "Ambos os arquivos-fonte",
    "Roteiro de entrada. Diz por onde começar conforme o que está acontecendo com o equipamento e "
    "em que ordem percorrer os documentos.",
    "Pontos de entrada por situação, ordem de leitura recomendada e regras de uso do material.",
    "Conteúdo técnico dos procedimentos; organização interna da documentação (ver documento 02).",
    [
        "[Índice da documentação](00-indice.md)",
        "[Fluxo de diagnóstico POST](06-fluxo-post.md)",
        "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md)",
        "[Índice de cenários](10-cenarios/00-indice-cenarios.md)",
    ],
    secao="comecar", nivel=0,
    resumo="Roteiro de entrada: por onde começar conforme o sintoma, em que ordem ler e quais "
           "regras seguir ao aplicar os procedimentos.",
    aplica_se="Uso da base durante um atendimento",
)

t += """## Antes de qualquer coisa

Leia [Taxonomia de camadas](03-taxonomia-camadas.md). Os dois arquivos-fonte numeram as camadas
de forma diferente, e usar o número errado leva a testar o subsistema errado.

## Entrada por sintoma

> [!TIP]
> A entrada por sintoma fica no [README](../README.md#por-onde-começar), que é o ponto de entrada
> da base: lá estão o fluxograma de triagem e a tabela completa de situação → documento.
> Esta página trata do **como usar** o material: em que ordem ler, que regras seguir e como um
> agente de IA deve consultá-lo.

## Ordem de leitura para quem está chegando agora

```mermaid
flowchart TD
    A["01 Visão geral<br/>o que é este material"] --> B["03 Taxonomia de camadas<br/>o conflito de numeração"]
    B --> C["04 Requisitos<br/>o que precisa estar na bancada"]
    C --> D{"O equipamento<br/>carrega o sistema?"}
    D -->|"Não"| E["06 Fluxo de POST<br/>a decisão antes do boot"]
    D -->|"Sim"| F["07 Fluxo sistêmico<br/>a decisão de ponta a ponta"]
    E --> G["08 Camadas<br/>o que testar em cada subsistema"]
    F --> G
    G --> H["09 e 10<br/>as fichas, sob demanda"]
    H --> I["13 Validação final<br/>como fechar"]
    I --> J["15 Limitações<br/>onde não confiar"]
```

> [!IMPORTANT]
> A etapa **03 Taxonomia de camadas** não é opcional. Ela é o único ponto da base em que o
> conflito entre os dois modelos de numeração é explicado, e todo número de camada que você
> encontrar depois depende dela.

## Regras de uso do material

1. **Não pule a camada de energia.** Os dois fluxos começam por ela, e a correlação
   [COR-01](12-correlacoes.md#cor-01) registra que instabilidade de fonte se manifesta como falha de
   memória, de disco e de sistema operacional.
2. **Anote o sinal exatamente como observado.** A Etapa 3 do fluxo de POST exige registrar número
   de beeps, duração (curto/longo) e pausas. Sem isso, a consulta ao catálogo não converge.
3. **Identifique o fabricante do BIOS antes de interpretar um beep.** O mesmo padrão sonoro tem
   significados diferentes entre AMI, Award e Acer/Insyde.
4. **Não conclua o atendimento sem validar.** O documento 13 traz critério PASS e FAIL por
   componente, com tempo de observação.
5. **Onde a documentação disser "Informação não identificada na fonte analisada", trate como
   lacuna real** — não como algo que possa ser preenchido por analogia com outro registro.

## Uso por sistemas de IA

Cada documento é autocontido: traz contexto, escopo, fora de escopo, relação com outros documentos
e a aba de origem no rodapé. Um agente pode carregar apenas o documento relevante sem perder a
noção de onde ele se encaixa. Os documentos gerados trazem, na primeira linha, um comentário HTML
com a aba de origem.

Para rastrear qualquer afirmação até a célula de origem, use
[references/matriz-rastreabilidade.md](references/matriz-rastreabilidade.md).
"""
t += doc_footer("Ambos os arquivos-fonte",
                conf="Inferido (roteiro de navegação) sobre conteúdo Confirmado", proximos=[
    ("o equipamento não carrega o sistema", "[Fluxo de diagnóstico POST](06-fluxo-post.md)"),
    ("o equipamento carrega e falha em uso",
     "[Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md)"),
    ("quer a lista completa de documentos", "[Índice da documentação](00-indice.md)"),
])
open(f"{OUT}/05-utilizacao.md", "w").write(t)

print("01, 02, 05 gerados")
