import os, sys, collections, hashlib
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
os.makedirs(f"{OUT}/references", exist_ok=True)
cod = read(F_COD)
flu = read(F_FLU)

# =========================================================================
# README
# =========================================================================
t = f"""# {PROJ_NOME}

> {PROJ_DESC}

**Autor:** {PROJ_AUTOR} · **Repositório:** [`{PROJ_OWNER}/{PROJ_REPO}`]({PROJ_URL}) · **Licença:** {PROJ_LICENCA} · **Documentação:** `{DOC_VERSAO}`

Referência técnica para diagnóstico de falhas de hardware em computadores, do sinal de erro emitido
no POST até a validação final que fecha o atendimento. Esta página é o **ponto de entrada**: a
partir daqui você chega a qualquer procedimento sem precisar abrir arquivo por arquivo.

---

## Por onde começar

Escolha o caminho pelo que o equipamento está fazendo agora.

```mermaid
flowchart TD
    A(["Qual é a situação?"]) --> B{{"O equipamento<br/>liga?"}}

    B -->|"Não dá sinal de vida"| P1["Fluxo de POST<br/>Etapa 1 — Energia"]
    B -->|"Liga, mas a tela<br/>fica preta"| P2["Fluxo de POST<br/>Etapa 2 — Sinais"]
    B -->|"Emite bipes, mostra código<br/>ou acende LED"| P3["Catálogo de códigos<br/>54 códigos de POST"]
    B -->|"Liga e carrega<br/>o sistema"| C{{"Funciona<br/>bem?"}}

    C -->|"Trava, reinicia, tela azul,<br/>esquenta, está lento"| S1["Cenários de falha<br/>13 procedimentos"]
    C -->|"Sim, quero apenas<br/>validar o equipamento"| V1["Validação final<br/>PASS / FAIL por componente"]

    P1 --> S1
    P2 --> P3
    P3 --> R{{"Aplicou a<br/>correção?"}}
    S1 --> R
    R -->|"Sim"| V1
    R -->|"O problema voltou"| X["Correlações entre camadas<br/>a peça trocada não era a causa"]
    X --> S1
    V1 --> Z(["Laudo emitido"])
```

| Situação | Vá para |
| --- | --- |
| Não dá sinal de vida | [Fluxo de diagnóstico POST](docs/06-fluxo-post.md) |
| Liga, mas não aparece imagem | [Fluxo de diagnóstico POST](docs/06-fluxo-post.md) → [Liga sem vídeo](docs/10-cenarios/liga-sem-video.md) |
| Está emitindo bipes | [Catálogo de códigos](docs/09-codigos-post/00-indice-codigos.md) |
| Mostra código hexadecimal no display | [AMI Q-Code](docs/09-codigos-post/ami-q-code.md) |
| Há um LED de diagnóstico aceso | [Debug LED genérico](docs/09-codigos-post/generico-debug-led.md) |
| O mesmo bipe tem dois significados | [Ambiguidade de códigos](docs/11-ambiguidades.md) |
| Trava, reinicia ou dá tela azul | [Cenários de falha](docs/10-cenarios/00-indice-cenarios.md) |
| Esquenta demais ou desliga sozinho | [Superaquecimento](docs/10-cenarios/superaquecimento.md) |
| Um disco sumiu do sistema | [Disco não reconhecido](docs/10-cenarios/disco-nao-reconhecido.md) |
| Troquei a peça e o problema voltou | [Correlações entre camadas](docs/12-correlacoes.md) |
| Terminei o reparo, preciso validar | [Validação final](docs/13-validacao-final.md) |
| Preciso do comando exato | [Referência de comandos](docs/19-comandos.md) |
| Quero buscar por componente, risco ou ferramenta | [Índices cruzados](docs/18-indices-cruzados.md) |
| Não reconheço um termo | [Glossário](docs/17-glossario.md) |

> [!IMPORTANT]
> Antes de usar qualquer número de camada, leia
> [Taxonomia de camadas](docs/03-taxonomia-camadas.md). Os dois arquivos-fonte numeram as camadas
> de forma incompatível: *camada 3* é **Memória** em um e **CPU** no outro.

---

## O que há aqui

- **54 códigos de POST** catalogados (bipes, Q-Codes hexadecimais, LEDs de diagnóstico), cobrindo
  11 famílias de BIOS e fabricantes, cada um com causa raiz, método de diagnóstico, procedimento
  de correção e critério de validação.
- **13 cenários de falha pós-boot** (não liga, tela azul, reinício aleatório, superaquecimento,
  disco não reconhecido, entre outros), com comandos técnicos e evidência de sucesso.
- **Dois fluxos de decisão**: um para a fase de POST (7 etapas) e um sistêmico de ponta a ponta
  (17 nós, F01 a F14).
- **5 casos de ambiguidade** — o mesmo sinal com significados diferentes conforme o fabricante.
- **6 correlações em cascata** — falhas que aparecem como sintoma de outro subsistema.
- **10 critérios de validação final** por componente, com PASS, FAIL e tempo de observação.
- **64 etapas operacionais** dos guias de Victoria, AIDA64 e MemTest86.

---

## Comece aqui

Leitura de primeira vez, na ordem.

| Documento | O que resolve |
| --- | --- |
| [Visão geral](docs/01-visao-geral.md) | O que esta base é, o que cobre e o que deliberadamente não faz. |
| [Taxonomia de camadas](docs/03-taxonomia-camadas.md) | **Leitura obrigatória.** Como saber qual dos dois modelos de camada você está lendo. |
| [Requisitos e ferramentas](docs/04-requisitos-e-ferramentas.md) | O que separar para a bancada antes de começar. |
| [Como utilizar](docs/05-utilizacao.md) | Por onde entrar conforme o sintoma e em que ordem ler. |
| [Índice completo](docs/00-indice.md) | Mapa de todos os documentos, com uma linha por arquivo. |

---

## Diagnostique

Do sintoma até a identificação da causa.

| Documento | O que resolve |
| --- | --- |
| [Fluxo de diagnóstico POST](docs/06-fluxo-post.md) | 7 etapas para equipamentos que não carregam o sistema. Termina na identificação do código. |
| [Fluxo de diagnóstico sistêmico](docs/07-fluxo-sistemico.md) | 17 nós, do botão Power ao laudo. Cobre também o comportamento depois do boot. |
| [Diagnóstico por camada](docs/08-diagnostico-por-camada.md) | O que testar em cada subsistema: componentes, testes primários, indicadores de falha. |

---

## Resolva

Da causa identificada até a correção aplicada.

| Documento | O que resolve |
| --- | --- |
| [Catálogo de códigos de POST](docs/09-codigos-post/00-indice-codigos.md) | Ficha completa dos 54 códigos, agrupados por família de BIOS. |
| [Cenários de falha](docs/10-cenarios/00-indice-cenarios.md) | Os 13 procedimentos pós-boot, com pré-requisitos, comandos e evidência de sucesso. |
| [Ambiguidade de códigos](docs/11-ambiguidades.md) | Os 5 sinais que significam coisas diferentes, e o teste que desempata. |
| [Correlações entre camadas](docs/12-correlacoes.md) | As 6 falhas que aparecem em outro subsistema e fazem trocar a peça errada. |

---

## Feche o atendimento

| Documento | O que resolve |
| --- | --- |
| [Validação final por componente](docs/13-validacao-final.md) | Critério PASS, critério FAIL, tempo de observação e ação em caso de reprovação, para 10 componentes. |

---

## Opere as ferramentas

| Documento | O que resolve |
| --- | --- |
| [Índice de ferramentas](docs/14-ferramentas/00-indice-ferramentas.md) | Qual ferramenta usar para cada verificação. |
| [Victoria](docs/14-ferramentas/victoria.md) | 9 etapas: S.M.A.R.T., varredura de superfície, remapeamento, relatório. |
| [MemTest86](docs/14-ferramentas/memtest86.md) | 10 etapas + critérios de decisão sobre o destino dos módulos. |
| [AIDA64](docs/14-ferramentas/aida64-etapas-01-15.md) | 45 etapas em três partes: [01–15](docs/14-ferramentas/aida64-etapas-01-15.md) · [16–30](docs/14-ferramentas/aida64-etapas-16-30.md) · [31–45](docs/14-ferramentas/aida64-etapas-31-45.md). |

---

## Consulte a referência

| Documento | O que resolve |
| --- | --- |
| [Índices cruzados](docs/18-indices-cruzados.md) | Os mesmos registros por componente, camada, risco, fase do POST, tipo de sinal e ferramenta. |
| [Referência de comandos](docs/19-comandos.md) | Todos os comandos técnicos dos cenários, com contexto e risco. |
| [Glossário](docs/17-glossario.md) | 43 termos, definidos pelo que a fonte diz sobre eles. |
| [Perguntas frequentes](docs/16-faq.md) | Dúvidas derivadas do conteúdo documentado. |
| [Limitações](docs/15-limitacoes.md) | O que esta base não cobre e onde ela é frágil. |

---

## Manutenção e rastreabilidade

| Documento | O que resolve |
| --- | --- |
| [Arquitetura da documentação](docs/02-arquitetura.md) | Como o conhecimento está organizado e de qual aba cada documento saiu. |
| [Fontes](docs/references/fontes.md) | Inventário das fontes, com hash de verificação. |
| [Matriz de rastreabilidade](docs/references/matriz-rastreabilidade.md) | Informação → coluna de origem → documento → nível de confiança. |
| [Pendências](docs/references/pendencias.md) | O que precisa de decisão humana, com severidade e o que falta para fechar. |
| [Histórico](docs/references/changelog.md) | O que mudou em cada versão da documentação. |
| [Como contribuir](CONTRIBUTING.md) | Regras de conteúdo, fluxo de alteração e mapa arquivo → script. |

---

## Como obter

```bash
git clone {PROJ_URL}.git
cd {PROJ_REPO}
```

A documentação é lida diretamente no GitHub ou em qualquer leitor de Markdown. Não há software a
instalar para consultá-la.

## Requisitos

O material é documental: o "requisito" é o instrumental de bancada exigido pelos procedimentos —
multímetro, osciloscópio, programadora CH341A, mídia bootável, componentes *known-good*, entre
outros. Inventário completo em
[Requisitos e ferramentas](docs/04-requisitos-e-ferramentas.md).

## Estrutura do repositório

```text
docs/
├── 00-indice.md                    Mapa da documentação
├── 01-visao-geral.md               O que é o projeto
├── 02-arquitetura.md               Como a documentação está organizada
├── 03-taxonomia-camadas.md         Os dois modelos de camadas (leitura obrigatória)
├── 04-requisitos-e-ferramentas.md  Instrumental necessário
├── 05-utilizacao.md                Por onde entrar conforme a situação
├── 06-fluxo-post.md                Decisão antes do boot (Etapas 1–7)
├── 07-fluxo-sistemico.md           Decisão de ponta a ponta (F01–F14)
├── 08-diagnostico-por-camada.md    O que testar em cada subsistema
├── 09-codigos-post/                Fichas dos 54 códigos, por família de BIOS
├── 10-cenarios/                    Fichas dos 13 cenários de falha
├── 11-ambiguidades.md              Códigos com mais de um significado
├── 12-correlacoes.md               Falhas em cascata entre camadas
├── 13-validacao-final.md           Critérios PASS / FAIL por componente
├── 14-ferramentas/                 Victoria, AIDA64, MemTest86
├── 15-limitacoes.md                O que a base não cobre
├── 16-faq.md                       Perguntas derivadas do conteúdo
├── 17-glossario.md                 Termos técnicos
├── 18-indices-cruzados.md          Busca por componente, camada, risco, fase, sinal, ferramenta
├── 19-comandos.md                  Todos os comandos técnicos reunidos
└── references/
    ├── fontes.md                   Origem de cada informação
    ├── matriz-rastreabilidade.md   Informação → fonte → documento → confiança
    ├── pendencias.md               O que precisa de validação humana
    └── changelog.md                Histórico desta documentação

CONTRIBUTING.md                     Como alterar e regerar a documentação
tools/gerar_documentacao.py         Regera docs/ a partir das planilhas
tools/validar_documentacao.py       Valida links, âncoras e estrutura
.github/workflows/validar-docs.yml  Executa o validador a cada push
```

## Padrão dos documentos

Todo documento segue a mesma estrutura, para que você saiba onde procurar sem reaprender o formato:

1. **Trilha de navegação** de volta a esta página;
2. **Resumo** de uma linha e **Aplica-se a**;
3. **Neste documento** — sumário com links para cada seção;
4. **Contexto, Escopo, Fora do escopo, Relação com outros documentos**;
5. **Fluxograma** da decisão que o documento resolve, quando aplicável;
6. **Conteúdo**, com procedimentos organizados em identificação → pré-requisitos → diagnóstico →
   execução → resultado esperado → risco → próximos passos;
7. **Próximos passos** — para onde ir a partir dali;
8. **Rodapé** com fonte primária, nível de confiança, autoria e versão.

Os avisos seguem convenção fixa: **NOTE** para procedência e nível de confiança, **TIP** para
atalhos de navegação, **IMPORTANT** para pré-requisito que muda o resultado, **WARNING** para risco
de erro de diagnóstico e **CAUTION** para risco elétrico, perda de dados ou dano a componente.

## Origem dos dados

Toda a base foi derivada de dois arquivos:

| Arquivo | Abas | Conteúdo |
| --- | --- | --- |
| `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` | 4 | Códigos de POST, fluxo de POST, camadas, ambiguidades |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | 8 | Cenários, fluxo sistêmico, correlações, validação, guias de ferramentas |

Nenhuma informação foi acrescentada, deduzida ou completada por fonte externa. Onde a origem é
omissa, a documentação registra a lacuna explicitamente. Detalhes em
[fontes](docs/references/fontes.md).

## Limitações relevantes

- Os dois arquivos-fonte usam **numerações de camada incompatíveis entre si**. A documentação
  preserva ambas e sinaliza o conflito; não escolhe uma delas.
- Há divergências pontuais de procedimento entre as fontes (duração do *power drain*, composição
  do *boot mínimo*, limiares de temperatura). Todas registradas em
  [pendências](docs/references/pendencias.md).
- Alguns campos estão vazios na origem — em especial *Atalho de teclado* nos guias de ferramentas.

Lista completa: [Limitações](docs/15-limitacoes.md).

## Manutenção

A fonte da verdade é a planilha, não o Markdown. Conteúdo técnico se altera nos arquivos `.xlsx`;
a documentação é então regerada:

```bash
pip install openpyxl
python tools/gerar_documentacao.py --fontes ./fontes --saida .
python tools/validar_documentacao.py
```

O gerador reconstrói os documentos derivados diretamente das células, o que elimina paráfrase
acidental. O validador confere links internos, âncoras, cabeçalhos de contexto, trilha de
navegação, próximos passos e rodapés de fonte, e sai com código diferente de zero se encontrar
link quebrado.

Procedimento completo em [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

{PROJ_LICENCA}, conforme o arquivo [`LICENSE`]({PROJ_URL}/blob/main/LICENSE) do repositório.

> [!NOTE]
> O arquivo `LICENSE` já existe no repositório e **não** faz parte deste pacote de documentação —
> para não sobrescrever o original.

## Autoria e créditos

**{PROJ_AUTOR}** — autor e responsável pelo projeto
([`{PROJ_OWNER}`](https://github.com/{PROJ_OWNER})).

O conteúdo técnico deriva de duas planilhas de referência de autoria de {PROJ_AUTOR}. As
referências a documentação de fabricantes citadas dentro do material são declarações da fonte
original e não foram verificadas de forma independente — ver
[fontes](docs/references/fontes.md).
"""
open(f"{OUT}/../README.md", "w").write(t)

# =========================================================================
# 00 — Índice
# =========================================================================
t = doc_header(
    "Índice da base de conhecimento",
    "Ambos os arquivos-fonte",
    "Mapa completo da documentação, na ordem lógica de uso. Cada documento tem uma descrição de "
    "uma linha.",
    "Listagem ordenada de todos os documentos, com finalidade e origem.",
    "Conteúdo técnico; detalhes de estrutura interna (ver documento 02).",
    [
        "[README](../README.md)",
        "[Visão geral](01-visao-geral.md)",
        "[Como utilizar](05-utilizacao.md)",
    ],
    secao="comecar", nivel=0,
    resumo="Mapa completo da documentação, na ordem lógica de uso, com uma linha por documento.",
    aplica_se="Navegação — complementa o README com a lista exaustiva",
)

t += """> [!TIP]
> Para navegar **pelo sintoma**, use o [README](../README.md) — ele tem o fluxograma de entrada.
> Esta página lista **todos** os documentos, para quando você já sabe o que procura.

## Mapa da documentação

```mermaid
flowchart LR
    subgraph EN["Comece aqui"]
        A1["01 Visão geral"] --> A2["03 Taxonomia<br/>de camadas"] --> A3["04 Requisitos"] --> A4["05 Utilização"]
    end
    subgraph DI["Diagnostique"]
        B1["06 Fluxo POST"]
        B2["07 Fluxo sistêmico"]
        B3["08 Camadas"]
    end
    subgraph RE["Resolva"]
        C1["09 Códigos<br/>de POST"]
        C2["10 Cenários"]
        C3["11 Ambiguidades"]
        C4["12 Correlações"]
    end
    subgraph FE["Feche"]
        D1["13 Validação final"]
    end
    subgraph FR["Ferramentas"]
        E1["14 Victoria<br/>AIDA64<br/>MemTest86"]
    end
    subgraph RF["Referência"]
        F1["17 Glossário"]
        F2["18 Índices cruzados"]
        F3["19 Comandos"]
        F4["15 Limitações"]
        F5["16 FAQ"]
    end
    subgraph MA["Rastreabilidade"]
        G1["02 Arquitetura"]
        G2["references/"]
    end

    EN --> DI
    B1 --> C1
    B1 --> C3
    B2 --> C2
    B3 --> C1
    C1 --> D1
    C2 --> D1
    C4 --> C2
    C2 --> E1
    D1 --> E1
    RE -.-> RF
    D1 -.-> MA
```

## Ordem lógica

```text
Comece aqui        → README, 00-indice
Entenda o projeto  → 01-visao-geral, 02-arquitetura, 03-taxonomia-camadas
Prepare-se         → 04-requisitos-e-ferramentas
Saiba navegar      → 05-utilizacao
Diagnostique       → 06-fluxo-post, 07-fluxo-sistemico, 08-diagnostico-por-camada
Resolva            → 09-codigos-post/, 10-cenarios/, 11-ambiguidades, 12-correlacoes
Feche o caso       → 13-validacao-final
Opere a ferramenta → 14-ferramentas/
Conheça os limites → 15-limitacoes, 16-faq, 17-glossario
Busque de outro jeito → 18-indices-cruzados, 19-comandos
Rastreie a origem  → references/
```

## Documentos

### Comece aqui

| Documento | Finalidade |
| --- | --- |
| [README](../README.md) | Porta de entrada do repositório: o que é, o que há, início rápido. |
| [00-indice.md](00-indice.md) | Este documento: mapa completo da base. |

### Entenda o projeto

| Documento | Finalidade |
| --- | --- |
| [01-visao-geral.md](01-visao-geral.md) | O que a base é, o que cobre, para quem e o que não faz. |
| [02-arquitetura.md](02-arquitetura.md) | Como o conhecimento foi organizado e de onde cada documento veio. |
| [03-taxonomia-camadas.md](03-taxonomia-camadas.md) | Os dois modelos de camadas coexistentes e o conflito entre eles. **Leitura obrigatória.** |

### Prepare-se e navegue

| Documento | Finalidade |
| --- | --- |
| [04-requisitos-e-ferramentas.md](04-requisitos-e-ferramentas.md) | Inventário do instrumental exigido, por camada, por cenário e por componente. |
| [05-utilizacao.md](05-utilizacao.md) | Por onde entrar conforme o sintoma e em que ordem ler. |

### Diagnostique

| Documento | Finalidade |
| --- | --- |
| [06-fluxo-post.md](06-fluxo-post.md) | Fluxo condicional de 7 etapas para falhas antes do boot. |
| [07-fluxo-sistemico.md](07-fluxo-sistemico.md) | Árvore de decisão de 17 nós, do botão Power à validação final. |
| [08-diagnostico-por-camada.md](08-diagnostico-por-camada.md) | Ficha de cada um dos 7 subsistemas: componentes, testes, indicadores de falha. |

### Resolva

| Documento | Finalidade |
| --- | --- |
| [09-codigos-post/](09-codigos-post/00-indice-codigos.md) | Catálogo dos 54 códigos de POST, com ficha completa de cada um. |
| [10-cenarios/](10-cenarios/00-indice-cenarios.md) | Fichas dos 13 cenários de falha pós-boot. |
| [11-ambiguidades.md](11-ambiguidades.md) | Os 5 sinais com mais de um significado e como diferenciá-los. |
| [12-correlacoes.md](12-correlacoes.md) | As 6 falhas que se manifestam em outra camada e as armadilhas associadas. |

### Feche o atendimento

| Documento | Finalidade |
| --- | --- |
| [13-validacao-final.md](13-validacao-final.md) | Critérios PASS e FAIL por componente, com tempo de observação e ação em caso de reprovação. |

### Opere as ferramentas

| Documento | Finalidade |
| --- | --- |
| [14-ferramentas/](14-ferramentas/00-indice-ferramentas.md) | Índice dos guias operacionais. |
| [victoria.md](14-ferramentas/victoria.md) | 9 etapas: da preparação do ambiente ao relatório final. |
| [memtest86.md](14-ferramentas/memtest86.md) | 10 etapas + critérios de decisão sobre o destino dos módulos. |
| [aida64-etapas-01-15.md](14-ferramentas/aida64-etapas-01-15.md) | AIDA64, etapas 1 a 15. |
| [aida64-etapas-16-30.md](14-ferramentas/aida64-etapas-16-30.md) | AIDA64, etapas 16 a 30. |
| [aida64-etapas-31-45.md](14-ferramentas/aida64-etapas-31-45.md) | AIDA64, etapas 31 a 45. |

### Conheça os limites

| Documento | Finalidade |
| --- | --- |
| [15-limitacoes.md](15-limitacoes.md) | O que a base não cobre, lacunas e divergências verificadas. |
| [16-faq.md](16-faq.md) | Perguntas derivadas exclusivamente do conteúdo documentado. |
| [17-glossario.md](17-glossario.md) | Termos técnicos usados no material, com a definição que a fonte dá. |

### Busque de outro jeito

| Documento | Finalidade |
| --- | --- |
| [18-indices-cruzados.md](18-indices-cruzados.md) | Os mesmos registros reagrupados por componente, camada, risco, fase do POST, tipo de sinal e ferramenta. |
| [19-comandos.md](19-comandos.md) | Todos os comandos técnicos dos cenários reunidos, com contexto e risco. |

### Rastreie a origem

| Documento | Finalidade |
| --- | --- |
| [references/fontes.md](references/fontes.md) | Inventário das fontes e do que foi extraído de cada aba. |
| [references/matriz-rastreabilidade.md](references/matriz-rastreabilidade.md) | Informação → fonte → documento → nível de confiança. |
| [references/pendencias.md](references/pendencias.md) | Tudo que precisa de validação humana. |
| [references/changelog.md](references/changelog.md) | Histórico desta documentação. |

## Convenção de níveis de confiança

| Nível | Significado |
| --- | --- |
| **Confirmado** | Identificado diretamente na fonte primária (célula da planilha). |
| **Oficial** | Confirmado por documentação oficial de fabricante citada pela própria fonte. |
| **Inferido** | Conclusão técnica ou organizacional derivada das informações, sempre sinalizada. |
| **Não confirmado** | Informação encontrada, mas sem evidência suficiente. |
| **Necessita validação** | Informação insuficiente, ausente ou conflitante entre fontes. |
"""
t += doc_footer("Ambos os arquivos-fonte", conf="Confirmado (estrutura) — documento organizacional",
                proximos=[
                    ("quer entrar pelo sintoma", "[README](../README.md)"),
                    ("vai alterar a documentação", "[Como contribuir](../CONTRIBUTING.md)"),
                    ("quer rastrear uma informação até a célula de origem",
                     "[Matriz de rastreabilidade](references/matriz-rastreabilidade.md)"),
                ])
open(f"{OUT}/00-indice.md", "w").write(t)
print("README e 00-indice gerados")
