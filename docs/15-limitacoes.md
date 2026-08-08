<!-- Gerado a partir de Verificação direta sobre ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../README.md) › [Consulte a referência](../README.md#consulte-a-referência) › **Limitações conhecidas**

# Limitações conhecidas

> O que esta base não entrega, verificado item a item contra os arquivos de origem.


**Aplica-se a:** Avaliação de confiança antes de decidir com base neste material

## Neste documento

- [1. Metadados do projeto ausentes](#1-metadados-do-projeto-ausentes)
- [2. Conflito de taxonomia entre as fontes](#2-conflito-de-taxonomia-entre-as-fontes)
- [3. Divergências de procedimento entre as fontes](#3-divergências-de-procedimento-entre-as-fontes)
- [4. Campos vazios na origem](#4-campos-vazios-na-origem)
- [5. Anomalias estruturais nas fontes](#5-anomalias-estruturais-nas-fontes)
- [6. Cobertura técnica ausente](#6-cobertura-técnica-ausente)
- [7. Limites de uso do material](#7-limites-de-uso-do-material)
- [8. Limite desta documentação](#8-limite-desta-documentação)
- [Próximos passos](#próximos-passos)

## Contexto

Registro honesto do que esta base **não** entrega. Cada item foi verificado contra os arquivos de origem; nenhum é suposição.

## Escopo

Lacunas de metadados, conflitos entre fontes, campos vazios, cobertura técnica ausente e limites de uso.

## Fora do escopo

Itens que exigem decisão do proprietário do projeto — esses estão em [references/pendencias.md](references/pendencias.md).

## Relação com outros documentos

- [Pendências](references/pendencias.md)
- [Taxonomia de camadas](03-taxonomia-camadas.md)
- [Fontes](references/fontes.md)
- [FAQ](16-faq.md)

---

## 1. Metadados do projeto ausentes

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

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer o que exige decisão sua | [Pendências](references/pendencias.md) |
| quer entender o conflito de camadas | [Taxonomia de camadas](03-taxonomia-camadas.md) |
| quer conferir a origem de uma informação | [Fontes](references/fontes.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Verificação direta sobre ambos os arquivos-fonte |
| **Status de confiança** | Confirmado — cada item verificado contra a origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.3.0` |
