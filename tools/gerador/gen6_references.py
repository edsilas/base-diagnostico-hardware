import os, sys, json, hashlib, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs/references"
os.makedirs(OUT, exist_ok=True)
cod = read(F_COD)
flu = read(F_FLU)

def sha(f):
    return hashlib.sha256(open(UP + f, "rb").read()).hexdigest()

TAM = {F_COD: os.path.getsize(UP + F_COD), F_FLU: os.path.getsize(UP + F_FLU)}

# Inventário: (arquivo, aba, linhas úteis, linhas de dados, colunas, o que contém, documento)
INV = [
    (F_COD, "Tabela Diagnóstico POST", 57, 54, 16,
     "Catálogo de códigos de POST com 16 campos por código",
     "`09-codigos-post/`"),
    (F_COD, "Fluxo de Diagnóstico", 9, 7, 6,
     "Fluxograma condicional de POST, 7 etapas",
     "`06-fluxo-post.md`"),
    (F_COD, "Camadas de Diagnóstico", 9, 7, 7,
     "Hierarquia de 7 subsistemas com componentes, testes e indicadores",
     "`08-diagnostico-por-camada.md`, `03-taxonomia-camadas.md`, `04-requisitos-e-ferramentas.md`"),
    (F_COD, "Ambiguidade de Códigos", 7, 5, 9,
     "Códigos com múltiplos significados e critério de diferenciação",
     "`11-ambiguidades.md`"),
    (F_FLU, "TABELA_PRINCIPAL", 14, 13, 17,
     "Cenários de falha com 17 campos por cenário",
     "`10-cenarios/`"),
    (F_FLU, "FLUXO_LOGICO", 18, 17, 7,
     "Árvore de decisão F01–F14 com ramos e ferramentas",
     "`07-fluxo-sistemico.md`"),
    (F_FLU, "CORRELACOES", 7, 6, 9,
     "Efeitos em cascata entre camadas, armadilhas e diferenciação",
     "`12-correlacoes.md`"),
    (F_FLU, "VALIDACAO_FINAL", 11, 10, 8,
     "Critérios PASS/FAIL por componente",
     "`13-validacao-final.md`"),
    (F_FLU, "INDICE_CENARIOS", 10, 9, 5,
     "Entrada por sintoma: camada primária, primeiro teste, ferramentas",
     "`10-cenarios/00-indice-cenarios.md`, `04-requisitos-e-ferramentas.md`"),
    (F_FLU, "REF_Victoria", 10, 9, 20,
     "Procedimento operacional do Victoria, 20 campos por etapa",
     "`14-ferramentas/victoria.md`"),
    (F_FLU, "REF_AIDA64", 46, 45, 20,
     "Procedimento operacional do AIDA64, 20 campos por etapa",
     "`14-ferramentas/aida64-etapas-*.md`"),
    (F_FLU, "REF_MemTest86", 12, 10, 20,
     "Procedimento operacional do MemTest86 + bloco de critérios de decisão",
     "`14-ferramentas/memtest86.md`"),
]

# =========================================================================
# fontes.md
# =========================================================================
t = doc_header(
    "Fontes",
    "Inventário direto dos arquivos recebidos",
    "Registro de origem de todo o conteúdo desta base. Identifica os arquivos, seu conteúdo por "
    "aba e o que foi extraído de cada um.",
    "Inventário dos arquivos-fonte, hash de verificação, conteúdo por aba e destino documental.",
    "Rastreabilidade campo a campo — está em "
    "[matriz-rastreabilidade.md](matriz-rastreabilidade.md).",
    [
        "[Matriz de rastreabilidade](matriz-rastreabilidade.md)",
        "[Pendências](pendencias.md)",
        "[Arquitetura da documentação](../02-arquitetura.md)",
    ],
    secao="manutencao", nivel=1,
    resumo="De onde veio cada informação desta base: arquivos, hash de verificação, conteúdo por "
           "aba e destino documental.",
    aplica_se="Auditoria de origem e verificação de integridade",
)

t += f"""## Nível 1 — Fontes primárias

Toda a documentação técnica desta base deriva **exclusivamente** dos dois arquivos abaixo.

### Fonte 1

- **Arquivo:** `{F_COD}`
- **Tipo:** Planilha Excel (Office Open XML)
- **Tamanho:** {TAM[F_COD]:,} bytes
- **SHA-256:** `{sha(F_COD)}`
- **Abas:** 4
- **Data interna dos componentes do pacote:** 2026-08-07 16:40
- **Metadados de autoria/versão (`docProps/core.xml`):** ausentes
- **Escopo:** sinais de erro emitidos durante o POST e o procedimento associado
- **Status:** Confirmado

### Fonte 2

- **Arquivo:** `{F_FLU}`
- **Tipo:** Planilha Excel (Office Open XML)
- **Tamanho:** {TAM[F_FLU]:,} bytes
- **SHA-256:** `{sha(F_FLU)}`
- **Abas:** 8
- **Data interna dos componentes do pacote:** 2026-08-07 16:40
- **Metadados de autoria/versão (`docProps/core.xml`):** ausentes
- **Escopo:** cenários de falha pós-boot, fluxo sistêmico e procedimentos de ferramentas
- **Status:** Confirmado

## Inventário por aba

| Arquivo | Aba | Linhas úteis | Registros | Colunas | Conteúdo | Documento de destino |
| --- | --- | --- | --- | --- | --- | --- |
"""
for arq, aba, lu, ld, nc, cont, doc in INV:
    t += f"| `{arq}` | `{aba}` | {lu} | {ld} | {nc} | {cont} | {doc} |\n"

t += """
> "Linhas úteis" inclui linhas de título e de cabeçalho; "Registros" conta apenas linhas de dados.

## Nível 2 — Informações fornecidas pelo proprietário

O proprietário do projeto informou o endereço do repositório oficial:

- **URL:** `https://github.com/edsilas/base-diagnostico-hardware`
- **Informado em:** 2026-08-07
- **Status:** Confirmado

Dessa informação decorre a identificação do projeto (nome, proprietário, licença), obtida por
consulta direta ao repositório — registrada no Nível 3 abaixo.

Permanece **não fornecida** a versão do conteúdo técnico das planilhas.

## Nível 3 — Fontes externas

### Repositório oficial do projeto

- **Fonte:** página pública do repositório no GitHub
- **Organização:** GitHub, Inc. (hospedagem) / `edsilas` (proprietário)
- **URL:** `https://github.com/edsilas/base-diagnostico-hardware`
- **Data de consulta:** 2026-08-07
- **Informações utilizadas:**

| Informação | Valor obtido | Onde é usada |
| --- | --- | --- |
| Nome do repositório | `base-diagnostico-hardware` | `README.md`, `01-visao-geral.md` |
| Proprietário | `edsilas` | `README.md`, `01-visao-geral.md` |
| Descrição oficial | "Base estruturada de conhecimento para diagnóstico de hardware, com fluxos, sintomas, códigos de erro, causas e procedimentos de análise e solução." | `README.md`, `01-visao-geral.md` |
| Licença | MIT (arquivo `LICENSE` presente na raiz) | `README.md`, `01-visao-geral.md` |
| Visibilidade | Público | — |
| Conteúdo no momento da consulta | 1 commit, branch `main`, arquivos `LICENSE` e `README.md` | `references/changelog.md` |

- **Status:** Confirmado

> O nome de exibição **Base de Diagnóstico de Hardware** é a forma legível do identificador
> `base-diagnostico-hardware` (acentuação e maiúsculas aplicadas). O identificador canônico
> continua sendo o nome do repositório.

### Documentação de fabricantes

**Nenhuma fonte de fabricante foi consultada** na elaboração desta documentação.

As planilhas citam, em campos próprios (`FONTE OFICIAL`, `Fonte Oficial`, `Fonte`), referências a
documentação de fabricantes e a normas. Essas citações foram **transcritas como estão** e não
foram verificadas contra os documentos originais. Aparecem nas fichas dos documentos 09, 10 e 12.

Referências citadas pelas fontes, agrupadas:

"""
refs = set()
for r in cod["Tabela Diagnóstico POST"][3:]:
    refs.add(r[15])
for r in flu["TABELA_PRINCIPAL"][1:]:
    refs.add(r[16])
for r in flu["CORRELACOES"][1:]:
    refs.add(r[8])
for x in sorted(refs):
    t += f"- {cell(x)}\n"

t += """
> **Status dessas referências: Não confirmado.** Elas são declarações da fonte primária, não
> verificações independentes. Para elevar a "Oficial", cada uma precisaria ser confrontada com o
> documento original do fabricante.

## Nível 4 — Inferências desta documentação

Toda inferência está sinalizada no ponto de uso. As de maior alcance são:

| Inferência | Onde | Justificativa |
| --- | --- | --- |
| Forma legível do nome (`Base de Diagnóstico de Hardware`) | README, `01-visao-geral.md` | Acentuação e capitalização do identificador `base-diagnostico-hardware` |
| Identificadores `POST-01` … `POST-54` | `09-codigos-post/` | A fonte não numera os códigos; necessário para link estável |
| Rótulos "Modelo A" e "Modelo B" para as taxonomias de camada | `03-taxonomia-camadas.md` | Necessário para poder distinguir os dois modelos sem ambiguidade |
| Diagrama dos dois eixos (pré-boot / pós-boot) | `02-arquitetura.md` | Derivado da leitura dos dois fluxos |
| Divisão do guia AIDA64 em três arquivos | `14-ferramentas/` | Divisão puramente numérica por faixa de etapas |
| Agrupamento dos 13 IDs em 9 arquivos de cenário | `10-cenarios/` | Agrupamento definido pela própria coluna `IDs Relacionados` |
| Roteiro de navegação por situação | `05-utilizacao.md` | Derivado das condições de entrada dos fluxos |
"""
t += doc_footer("Inventário direto dos arquivos recebidos", proximos=[
    ("quer o mapeamento campo a campo", "[Matriz de rastreabilidade](matriz-rastreabilidade.md)"),
    ("quer o que ainda não foi confirmado", "[Pendências](pendencias.md)"),
    ("quer entender como os documentos são gerados",
     "[Arquitetura da documentação](../02-arquitetura.md)"),
])
open(f"{OUT}/fontes.md", "w").write(t)

# =========================================================================
# matriz-rastreabilidade.md
# =========================================================================
t = doc_header(
    "Matriz de rastreabilidade",
    "Ambos os arquivos-fonte",
    "Permite ir de qualquer informação da documentação até a célula de origem, e vice-versa. É o "
    "instrumento de auditoria da base.",
    "Mapeamento informação → aba de origem → documento → nível de confiança, no nível de "
    "coluna/campo.",
    "O conteúdo em si; a análise de conflitos, que está em [pendencias.md](pendencias.md).",
    [
        "[Fontes](fontes.md)",
        "[Pendências](pendencias.md)",
        "[Índice da documentação](../00-indice.md)",
    ],
    secao="manutencao", nivel=1,
    resumo="Caminho de ida e volta entre qualquer informação da documentação e a coluna de origem "
           "na planilha.",
    aplica_se="Auditoria da base e verificação de nível de confiança",
)

t += """## Como ler

Cada linha descreve **um grupo de informação**, identificado pela coluna de origem na planilha.
O nível de confiança segue a convenção definida em [00-indice.md](../00-indice.md).

## Documentos gerados a partir de dados

| Informação | Fonte (arquivo → aba → coluna) | Documento | Confiança |
| --- | --- | --- | --- |
"""

ROWS = []


def add(info, arq, aba, col, doc, conf="Confirmado"):
    ROWS.append((info, f"`{arq}` → `{aba}` → `{col}`", doc, conf))


A, B = F_COD, F_FLU
POSTDOC = "`09-codigos-post/*`"
for col, info in [
    ("FABRICANTE BIOS", "Família de BIOS de cada código"),
    ("FABRICANTE / PLATAFORMA", "Plataforma de aplicação do código"),
    ("TIPO DE SINAL", "Natureza do sinal (beep, hex, LED, tom)"),
    ("CÓDIGO", "Valor literal do código"),
    ("INTERPRETAÇÃO OFICIAL", "Significado declarado do código"),
    ("COMPONENTE AFETADO", "Componente indicado pelo código"),
    ("CAMADA DE DIAGNÓSTICO", "Camada (modelo A) do código"),
    ("FASE POST", "Fase do POST em que o código ocorre"),
    ("CAUSA RAIZ (Documentação Oficial)", "Causa raiz declarada"),
    ("CONDIÇÕES QUE GERAM O ERRO", "Condições que produzem o erro"),
    ("MÉTODO DE DIAGNÓSTICO TÉCNICO", "Procedimento de diagnóstico"),
    ("FERRAMENTAS OFICIAIS", "Ferramentas exigidas pelo código"),
    ("PROCEDIMENTO DE CORREÇÃO (Passo a Passo)", "Procedimento de correção"),
    ("CRITÉRIO DE VALIDAÇÃO", "Critério de validação do reparo"),
    ("RISCO / CRITICIDADE", "Classificação de risco"),
    ("FONTE OFICIAL", "Referência declarada pela fonte"),
]:
    conf = "Não confirmado" if col == "FONTE OFICIAL" else "Confirmado"
    add(info, A, "Tabela Diagnóstico POST", col, POSTDOC, conf)

add("Identificador POST-NN", A, "Tabela Diagnóstico POST", "(ordem das linhas)",
    POSTDOC, "**Inferido (organizacional)**")

for col, info in [
    ("ETAPA", "Número da etapa do fluxo de POST"),
    ("CONDIÇÃO / PERGUNTA", "Pergunta de decisão da etapa"),
    ("AÇÃO SE SIM", "Ramo afirmativo"),
    ("AÇÃO SE NÃO", "Ramo negativo"),
    ("PRÓXIMA ETAPA", "Encadeamento entre etapas"),
    ("OBSERVAÇÕES", "Observações da etapa"),
]:
    add(info, A, "Fluxo de Diagnóstico", col, "`06-fluxo-post.md`")

for col, info in [
    ("CAMADA", "Número da camada (modelo A)"),
    ("NOME", "Nome da camada"),
    ("COMPONENTES", "Componentes da camada"),
    ("SINTOMAS TÍPICOS", "Sintomas típicos da camada"),
    ("TESTES PRIMÁRIOS", "Testes primários da camada"),
    ("FERRAMENTAS", "Ferramentas da camada"),
    ("INDICADORES DE FALHA", "Indicadores de falha da camada"),
]:
    doc = "`08-diagnostico-por-camada.md`"
    if col == "FERRAMENTAS":
        doc += ", `04-requisitos-e-ferramentas.md`"
    if col in ("CAMADA", "NOME"):
        doc += ", `03-taxonomia-camadas.md`"
    add(info, A, "Camadas de Diagnóstico", col, doc)

for col, info in [
    ("CÓDIGO AMBÍGUO", "Sinal com mais de um significado"),
    ("FABRICANTE 1/2/3 e SIGNIFICADO 1/2/3", "Significados concorrentes por fabricante"),
    ("CRITÉRIO DE DIFERENCIAÇÃO", "Como distinguir os significados"),
    ("TESTE PARA IDENTIFICAR CAUSA", "Teste de desempate"),
]:
    add(info, A, "Ambiguidade de Códigos", col, "`11-ambiguidades.md`")

for col, info in [
    ("ID", "Identificador do cenário"),
    ("Sintoma Observado", "Sintoma relatado"),
    ("Camada Afetada", "Camada (modelo B) do cenário"),
    ("Componente Suspeito", "Componente suspeito"),
    ("Condição de Ocorrência", "Condição em que o sintoma aparece"),
    ("Causa Raiz", "Causa raiz declarada"),
    ("Método de Diagnóstico (Passo a Passo)", "Procedimento de diagnóstico"),
    ("Ferramentas Oficiais", "Ferramentas exigidas"),
    ("Comandos Técnicos", "Comandos a executar"),
    ("Procedimento de Correção (Detalhado)", "Procedimento de correção"),
    ("Ordem de Execução", "Prioridade de execução"),
    ("Dependências", "Pré-requisitos entre cenários"),
    ("Critério de Validação Técnica", "Critério de validação"),
    ("Evidência de Sucesso", "Evidência mensurável de sucesso"),
    ("Risco Associado", "Classificação de risco"),
    ("Impacto no Sistema", "Impacto da falha"),
    ("Fonte Oficial", "Referência declarada pela fonte"),
]:
    conf = "Não confirmado" if col == "Fonte Oficial" else "Confirmado"
    add(info, B, "TABELA_PRINCIPAL", col, "`10-cenarios/*`", conf)

for col, info in [
    ("Nó", "Identificador do nó de decisão"),
    ("Condição / Pergunta", "Pergunta do nó"),
    ("SE Verdadeiro → / SE Falso →", "Ramos do nó"),
    ("Ação", "Ação a executar no nó"),
    ("Ferramentas", "Ferramentas do nó"),
    ("Referência (ID)", "Cenário associado ao nó"),
]:
    add(info, B, "FLUXO_LOGICO", col, "`07-fluxo-sistemico.md`")

for col, info in [
    ("ID", "Identificador da correlação"),
    ("Falha Primária (Camada) / Efeito Cascata (Camada)", "Camadas envolvidas (modelo B)"),
    ("Mecanismo de Propagação", "Como a falha se propaga"),
    ("Sintoma Resultante", "Sintoma percebido"),
    ("Diagnóstico Diferencial", "Ordem de teste recomendada"),
    ("Armadilha Comum", "Erro frequente de diagnóstico"),
    ("Como Distinguir", "Critério de desempate"),
    ("Fonte", "Referência declarada pela fonte"),
]:
    conf = "Não confirmado" if col == "Fonte" else "Confirmado"
    add(info, B, "CORRELACOES", col, "`12-correlacoes.md`", conf)

for col, info in [
    ("Componente", "Componente validado"),
    ("Teste Pós-Correção", "Teste a executar após o reparo"),
    ("Ferramenta de Validação", "Ferramenta do teste"),
    ("Indicador de Sucesso", "Indicador observável"),
    ("Tempo de Observação", "Duração exigida"),
    ("Critério PASS / Critério FAIL", "Limiares de aprovação e reprovação"),
    ("Ação se FAIL", "Encaminhamento em caso de reprovação"),
]:
    doc = "`13-validacao-final.md`"
    if col == "Ferramenta de Validação":
        doc += ", `04-requisitos-e-ferramentas.md`"
    add(info, B, "VALIDACAO_FINAL", col, doc)

for col, info in [
    ("Cenário", "Nome do cenário"),
    ("IDs Relacionados", "Agrupamento dos IDs por cenário"),
    ("Camada Primária", "Camada de entrada (modelo B)"),
    ("Primeiro Teste", "Teste inicial recomendado"),
    ("Ferramentas Necessárias", "Ferramentas do cenário"),
]:
    doc = "`10-cenarios/00-indice-cenarios.md`"
    if col == "Ferramentas Necessárias":
        doc += ", `04-requisitos-e-ferramentas.md`"
    add(info, B, "INDICE_CENARIOS", col, doc)

for aba, doc in [("REF_Victoria", "`14-ferramentas/victoria.md`"),
                 ("REF_AIDA64", "`14-ferramentas/aida64-etapas-*.md`"),
                 ("REF_MemTest86", "`14-ferramentas/memtest86.md`")]:
    add("Etapas operacionais (20 campos: objetivo, ação, caminho, atalho, configurações, "
        "verificação prévia, erros, causa, identificação, correção, validação, risco, impacto, "
        "tempo, observações, boas práticas, alternativa, checklist)",
        B, aba, "(todas as colunas)", doc)

add("Critérios de decisão pós-teste", B, "REF_MemTest86", "última linha, coluna `Nº da Etapa`",
    "`14-ferramentas/memtest86.md`")

for info, fonte, doc, conf in ROWS:
    t += f"| {info} | {fonte} | {doc} | {conf} |\n"

t += """
## Documentos redigidos manualmente

Estes documentos não transcrevem células: organizam, explicam e sinalizam. Cada afirmação técnica
que contêm remete a um documento gerado.

| Documento | Natureza | Confiança |
| --- | --- | --- |
| `README.md` | Apresentação e navegação | Confirmado |
| `00-indice.md` | Mapa da documentação | Confirmado (estrutura) |
| `01-visao-geral.md` | Descrição do projeto e contagens | Confirmado (contagens e identificação) / Necessita validação (versão do conteúdo técnico) |
| `02-arquitetura.md` | Organização e mapa de origem | Confirmado (mapa) / Inferido (diagrama de eixos) |
| `03-taxonomia-camadas.md` | Registro de conflito entre modelos | Confirmado (modelo A) / Necessita validação (modelo B) |
| `04-requisitos-e-ferramentas.md` | Agregação de colunas de ferramentas | Confirmado |
| `05-utilizacao.md` | Roteiro de navegação | Inferido sobre conteúdo Confirmado |
| `15-limitacoes.md` | Lacunas e divergências verificadas | Confirmado |
| `16-faq.md` | Perguntas derivadas do conteúdo | Confirmado (respostas) |
| `17-glossario.md` | Termos com definição da fonte | Confirmado / sinalizado por termo |
| `references/*` | Rastreabilidade e auditoria | Confirmado |

## Contagens verificáveis

| Métrica | Valor |
| --- | --- |
| Códigos de POST | 54 |
| Cenários (IDs) | 13 |
| Cenários (agrupamentos) | 9 |
| Camadas modelo A | 7 |
| Camadas modelo B observadas | 9 números distintos (1–7, 9, 10) |
| Etapas do fluxo de POST | 7 |
| Nós do fluxo sistêmico | 17 |
| Casos de ambiguidade | 5 |
| Correlações | 6 |
| Componentes na validação final | 10 |
| Etapas de ferramentas | 64 |
| Referências externas citadas pelas fontes | """ + str(len(refs)) + """ (não verificadas) |
| Fontes externas consultadas por esta documentação | 1 (repositório oficial) |
"""
t += doc_footer("Ambos os arquivos-fonte", proximos=[
    ("quer os arquivos de origem e seus hashes", "[Fontes](fontes.md)"),
    ("encontrou uma informação sem confirmação", "[Pendências](pendencias.md)"),
    ("vai alterar a documentação", "[Como contribuir](../../CONTRIBUTING.md)"),
])
open(f"{OUT}/matriz-rastreabilidade.md", "w").write(t)
print("fontes e matriz gerados; linhas na matriz:", len(ROWS))
