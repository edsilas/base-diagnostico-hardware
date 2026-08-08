<!-- Gerado a partir de Inventário direto dos arquivos recebidos. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Manutenção e rastreabilidade](../../README.md#manutenção-e-rastreabilidade) › **Fontes**

# Fontes

> De onde veio cada informação desta base: arquivos, hash de verificação, conteúdo por aba e destino documental.


**Aplica-se a:** Auditoria de origem e verificação de integridade

## Neste documento

- [Nível 1 — Fontes primárias](#nível-1--fontes-primárias)
- [Inventário por aba](#inventário-por-aba)
- [Nível 2 — Informações fornecidas pelo proprietário](#nível-2--informações-fornecidas-pelo-proprietário)
- [Nível 3 — Fontes externas](#nível-3--fontes-externas)
- [Nível 4 — Inferências desta documentação](#nível-4--inferências-desta-documentação)
- [Próximos passos](#próximos-passos)

## Contexto

Registro de origem de todo o conteúdo desta base. Identifica os arquivos, seu conteúdo por aba e o que foi extraído de cada um.

## Escopo

Inventário dos arquivos-fonte, hash de verificação, conteúdo por aba e destino documental.

## Fora do escopo

Rastreabilidade campo a campo — está em [matriz-rastreabilidade.md](matriz-rastreabilidade.md).

## Relação com outros documentos

- [Matriz de rastreabilidade](matriz-rastreabilidade.md)
- [Pendências](pendencias.md)
- [Arquitetura da documentação](../02-arquitetura.md)

---

## Nível 1 — Fontes primárias

Toda a documentação técnica desta base deriva **exclusivamente** dos dois arquivos abaixo.

### Fonte 1

- **Arquivo:** `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx`
- **Tipo:** Planilha Excel (Office Open XML)
- **Tamanho:** 76,348 bytes
- **SHA-256:** `7b68d430d8be036549993e8f24dd8bb363883b59f4d13eda85a7822c114dcd7d`
- **Abas:** 4
- **Data interna dos componentes do pacote:** 2026-08-07 16:40
- **Metadados de autoria/versão (`docProps/core.xml`):** ausentes
- **Escopo:** sinais de erro emitidos durante o POST e o procedimento associado
- **Status:** Confirmado

### Fonte 2

- **Arquivo:** `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx`
- **Tipo:** Planilha Excel (Office Open XML)
- **Tamanho:** 265,689 bytes
- **SHA-256:** `3c3416952b83152f19aeeff901a21c57cd9cd2ef274385f7a7b926e0ceae7679`
- **Abas:** 8
- **Data interna dos componentes do pacote:** 2026-08-07 16:40
- **Metadados de autoria/versão (`docProps/core.xml`):** ausentes
- **Escopo:** cenários de falha pós-boot, fluxo sistêmico e procedimentos de ferramentas
- **Status:** Confirmado

## Inventário por aba

| Arquivo | Aba | Linhas úteis | Registros | Colunas | Conteúdo | Documento de destino |
| --- | --- | --- | --- | --- | --- | --- |
| `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` | `Tabela Diagnóstico POST` | 57 | 54 | 16 | Catálogo de códigos de POST com 16 campos por código | `09-codigos-post/` |
| `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` | `Fluxo de Diagnóstico` | 9 | 7 | 6 | Fluxograma condicional de POST, 7 etapas | `06-fluxo-post.md` |
| `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` | `Camadas de Diagnóstico` | 9 | 7 | 7 | Hierarquia de 7 subsistemas com componentes, testes e indicadores | `08-diagnostico-por-camada.md`, `03-taxonomia-camadas.md`, `04-requisitos-e-ferramentas.md` |
| `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` | `Ambiguidade de Códigos` | 7 | 5 | 9 | Códigos com múltiplos significados e critério de diferenciação | `11-ambiguidades.md` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `TABELA_PRINCIPAL` | 14 | 13 | 17 | Cenários de falha com 17 campos por cenário | `10-cenarios/` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `FLUXO_LOGICO` | 18 | 17 | 7 | Árvore de decisão F01–F14 com ramos e ferramentas | `07-fluxo-sistemico.md` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `CORRELACOES` | 7 | 6 | 9 | Efeitos em cascata entre camadas, armadilhas e diferenciação | `12-correlacoes.md` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `VALIDACAO_FINAL` | 11 | 10 | 8 | Critérios PASS/FAIL por componente | `13-validacao-final.md` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `INDICE_CENARIOS` | 10 | 9 | 5 | Entrada por sintoma: camada primária, primeiro teste, ferramentas | `10-cenarios/00-indice-cenarios.md`, `04-requisitos-e-ferramentas.md` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `REF_Victoria` | 10 | 9 | 20 | Procedimento operacional do Victoria, 20 campos por etapa | `14-ferramentas/victoria.md` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `REF_AIDA64` | 46 | 45 | 20 | Procedimento operacional do AIDA64, 20 campos por etapa | `14-ferramentas/aida64-etapas-*.md` |
| `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` | `REF_MemTest86` | 12 | 10 | 20 | Procedimento operacional do MemTest86 + bloco de critérios de decisão | `14-ferramentas/memtest86.md` |

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

- AMI Aptio V Status Codes
- AMI Aptio V Status Codes / Fabricante da placa-mãe
- AMI BIOS Beep Code Reference
- AMI BIOS Beep Code Reference / Intel CPU Spec
- AMI BIOS Beep Code Reference / Intel LGA Socket Spec
- AMI BIOS Beep Code Reference / Intel PCH Datasheet
- AMI BIOS Beep Code Reference / Super I/O Datasheet
- AMI BIOS Beep Code Reference — AMI Technical Documentation
- AMI BIOS Recovery Procedures / Fabricante da placa-mãe
- AMI Reserved Codes / ASUS Debug Reference
- ASUS Q-Code Reference
- ASUS Q-Code Reference / AMI Aptio Status Codes
- ASUS Q-Code Reference / GIGABYTE Debug Code List
- ATX12V PSU Design Guide v2.53 (Intel); Microsoft Docs: Kernel-Power Event ID 41; AIDA64 Documentation
- ATX12V PSU Design Guide v2.53 (Transient Response); Microsoft Docs: Kernel-Power 41; AIDA64 Sensor Logging Documentation
- ATX12V PSU Design Guide v2.53 §3.2.1; Intel Voltage Regulator Module Guidelines
- Acer Service Manual / Insyde BIOS Reference
- Apple Support - Mac Startup Tones
- Apple Support - Restore Firmware / Apple Configurator 2 Guide
- Award BIOS Beep Code Reference
- Award BIOS Reference
- Award BIOS Reference / ATX PSU Specification
- Dell BIOS Recovery Guide / Dell Support
- Dell OptiPlex Service Manual
- Dell OptiPlex Service Manual / Dell LED Diagnostic Codes
- Dell Service Manual
- Dell Service Manual / Dell LCD Diagnostics
- Dell Service Manual / Dell LED Codes
- Dell Service Manual / Dell Power Supply Specs
- HP BIOS Recovery Guide / HP LED Flash Codes
- HP LED Flash Codes
- HP LED Flash Codes / HP Power Supply Specs
- HP LED Flash Codes / HP Service Manual
- HP LED Flash Codes / HP Thermal Design Guide
- Intel 13th/14th Gen Datasheet Vol.1 (Thermal Design); AMD Ryzen Processor Technical Reference; AIDA64 Documentation
- Intel ATX12V PSU Design Guide v2.53; IEC 62368-1 (Segurança Elétrica)
- Intel Microcode Update Guidance; AMD AGESA Changelog; UEFI Specification 2.10; OEM BIOS Release Notes
- Intel Thermal Design Guide (TDP/TjMax); AMD Ryzen Thermal Solution Design Guide; Noctua Application Notes
- Intel Thermal Design Guide; AMD Ryzen Thermal Solution Design Guide
- JEDEC JESD79-4/5 (DDR4/DDR5 Standards); Intel MRC; Manual OEM da placa-mãe (Memory QVL)
- JEDEC JESD79-4/5; Microsoft Docs: sfc /scannow; MemTest86 Documentation
- Lenovo SmartBeep Documentation / Lenovo HMM
- Lenovo ThinkPad HMM / Lenovo BIOS Guide
- Manual da placa-mãe / DDR5 JEDEC Specification
- Manual da placa-mãe / Microsoft Boot Recovery Guide
- Manual da placa-mãe do fabricante
- Manual de Manutenção OEM (Dell/HP/Lenovo); ASUS/Gigabyte/MSI Motherboard User Manual (Front Panel Header pinout)
- MemTest86 User Guide (PassMark); JEDEC JESD79-4/5; Intel/AMD Memory OC Guides; Manual OEM (Memory QVL)
- Microsoft Docs: Bug Check 0x1A MEMORY_MANAGEMENT; Microsoft Docs: Bug Check 0x0A IRQL_NOT_LESS_OR_EQUAL; WinDbg Documentation
- Microsoft Docs: Bug Check 0x7A; Seagate Knowledge Base: SMART Attributes; Western Digital SMART Reference; Victoria HDD Documentation
- Microsoft Docs: Bug Check 0x7A; Seagate SMART Attribute Reference; Victoria Documentation
- Microsoft Docs: TDR Registry Keys; NVIDIA/AMD Driver Release Notes; DDU Documentation
- Microsoft Docs: Troubleshoot high CPU usage; Sysinternals Process Explorer Documentation; Microsoft Security Intelligence
- PCI Express Base Spec Rev 5.0; NVIDIA/AMD GPU User Guides; Manual OEM da placa-mãe
- Phoenix BIOS Technical Reference Manual
- SATA-IO Serial ATA Revision 3.5; NVM Express Specification Rev 2.0; Manual OEM da Placa-mãe (M.2 Compatibility Chart)

> **Status dessas referências: Não confirmado.** Elas são declarações da fonte primária, não
> verificações independentes. Para elevar a "Oficial", cada uma precisaria ser confrontada com o
> documento original do fabricante.

**Conferência bibliográfica.** A designação de parte dessas referências — não o conteúdo atribuído
a elas — foi conferida contra os órgãos que as publicam. A conferência apurou que a citação
*ATX12V PSU Design Guide v2.53* nomeia um documento que não existe sob esse título, embora a versão
esteja correta. O resultado completo está em
[P-15](pendencias.md#p-15--referências-externas-citadas-mas-não-verificadas).

Isso **não altera** o que está escrito acima: nenhuma informação técnica desta base veio de
documentação de fabricante. A conferência apenas verifica se os documentos citados pelas planilhas
existem e como se chamam.

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

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer o mapeamento campo a campo | [Matriz de rastreabilidade](matriz-rastreabilidade.md) |
| quer o que ainda não foi confirmado | [Pendências](pendencias.md) |
| quer entender como os documentos são gerados | [Arquitetura da documentação](../02-arquitetura.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Inventário direto dos arquivos recebidos |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
