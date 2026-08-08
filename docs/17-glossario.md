<!-- Gerado a partir de Ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../README.md) › [Consulte a referência](../README.md#consulte-a-referência) › **Glossário**

# Glossário

> 47 termos técnicos usados no material, com a definição empregada nesta base e a expansão de cada sigla.


**Aplica-se a:** Leitura de qualquer documento desta base

## Neste documento

- [5VSB (standby 5 V)](#5vsb-standby-5-v)
- [BDS (Boot Device Selection)](#bds-boot-device-selection)
- [BIST (Built-In Self-Test)](#bist-built-in-self-test)
- [Boot mínimo (minimal boot)](#boot-mínimo-minimal-boot)
- [Camada](#camada)
- [CH341A](#ch341a)
- [Debug LED](#debug-led)
- [DDU (Display Driver Uninstaller)](#ddu-display-driver-uninstaller)
- [IMC (Integrated Memory Controller)](#imc-integrated-memory-controller)
- [Kernel-Power 41](#kernel-power-41)
- [Known-good](#known-good)
- [PCH (Platform Controller Hub)](#pch-platform-controller-hub)
- [Pass (MemTest86)](#pass-memtest86)
- [Power drain](#power-drain)
- [PROCHOT](#prochot)
- [Q-Code](#q-code)
- [QVL (Qualified Vendor List)](#qvl-qualified-vendor-list)
- [Remap](#remap)
- [Reseat](#reseat)
- [Ripple](#ripple)
- [S.M.A.R.T. — IDs 05, C5 e C6](#smart--ids-05-c5-e-c6)
- [ACPI (Advanced Configuration and Power Interface)](#acpi-advanced-configuration-and-power-interface)
- [BDA (BIOS Data Area) e IVT (Interrupt Vector Table)](#bda-bios-data-area-e-ivt-interrupt-vector-table)
- [DXE (Driver Execution Environment)](#dxe-driver-execution-environment)
- [G-List (Growth Defect List)](#g-list-growth-defect-list)
- [GOP (Graphics Output Protocol)](#gop-graphics-output-protocol)
- [HMM (Hardware Maintenance Manual)](#hmm-hardware-maintenance-manual)
- [KBC (Keyboard Controller)](#kbc-keyboard-controller)
- [ME (Management Engine)](#me-management-engine)
- [OCP (Over Current Protection) e OPP (Over Power Protection)](#ocp-over-current-protection-e-opp-over-power-protection)
- [Row Hammer](#row-hammer)
- [SmartBeep](#smartbeep)
- [SPD (Serial Presence Detect)](#spd-serial-presence-detect)
- [TPM (Trusted Platform Module)](#tpm-trusted-platform-module)
- [TDR (Timeout Detection and Recovery)](#tdr-timeout-detection-and-recovery)
- [Teste cruzado](#teste-cruzado)
- [Teste paperclip](#teste-paperclip)
- [TjMax (Tjunction max)](#tjmax-tjunction-max)
- [Vdrop / voltage droop](#vdrop--voltage-droop)
- [Wear Level](#wear-level)
- [WinDbg (Windows Debugging Tools)](#windbg-windows-debugging-tools)
- [WinPE](#winpe)
- [XMP / EXPO / DOCP](#xmp--expo--docp)
- [ESD (Electrostatic Discharge)](#esd-electrostatic-discharge)
- [Flea power](#flea-power)
- [Hammer Test (Teste 13)](#hammer-test-teste-13)
- [PSREF (Product Specifications Reference)](#psref-product-specifications-reference)
- [Siglas de fase do POST](#siglas-de-fase-do-post)
- [Siglas expandidas fora da fonte primária](#siglas-expandidas-fora-da-fonte-primária)
- [Próximos passos](#próximos-passos)

## Contexto

Termos técnicos efetivamente usados no material, definidos a partir do que as fontes dizem sobre eles. Termos que a fonte usa sem definir estão marcados como tal.

## Escopo

Definição, nível de confiança e documento onde o termo é aplicado.

## Fora do escopo

Termos genéricos de informática sem relação com os procedimentos documentados; expansões de siglas que a fonte não fornece.

## Relação com outros documentos

- [Índice da documentação](00-indice.md)
- [Taxonomia de camadas](03-taxonomia-camadas.md)
- [Segurança e boas práticas](15-seguranca-e-boas-praticas.md)

---

> **Critério de inclusão.** Só entram termos que aparecem nas fontes e cuja definição pode ser
> sustentada pelo que elas dizem. Onde a fonte usa a sigla sem expandi-la, isso está registrado no
> nível de confiança em vez de completado por conhecimento externo.

## 5VSB (standby 5 V)

Tensão de standby presente no conector ATX de 24 pinos com o cabo AC conectado, mesmo com o equipamento desligado. A fonte localiza a medição no pino 9, fio roxo, e define 5,0 V ±5% como valor esperado. Sua ausência é o primeiro indicador de fonte morta ou cabo AC com problema.

**Nível de confiança:** Confirmado  
**Aplicado em:** 08-diagnostico-por-camada.md, 10-cenarios/nao-liga.md

---

## BDS (Boot Device Selection)

Fase do POST em que o firmware seleciona o dispositivo de boot. Expansão fornecida pela própria fonte no campo `FASE POST`.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/

---

## BIST (Built-In Self-Test)

Autoteste embutido. A base o cita em dois usos: o autoteste da fonte de alimentação, acionado por
botão próprio na traseira de desktops Dell, e um autoteste de tela acionado por `D` + Power. No
autoteste de fonte, o critério publicado pela Dell é **LED sólido e ventoinha girando**; ventoinha
parada reprova o teste mesmo com o LED aceso.

**Nível de confiança:** Confirmado (uso, pela fonte primária) / Confirmado (expansão e critério, por documentação Dell)  
**Aplicado em:** 09-codigos-post/dell.md

---

## Boot mínimo (minimal boot)

Configuração reduzida para isolar a falha. A base define **duas composições nomeadas**:
*boot mínimo absoluto* (CPU + cooler + 1 RAM no slot primário + PSU) e *boot mínimo com vídeo* (o
anterior mais saída de vídeo e monitor), escolhidas conforme o equipamento tenha ou não Debug LED,
Q-Code ou speaker. O cooler é obrigatório nas duas.

**Nível de confiança:** Confirmado — composições definidas em [15-seguranca-e-boas-praticas.md](15-seguranca-e-boas-praticas.md#boot-mínimo-as-duas-composições-canônicas)  
**Aplicado em:** 06-fluxo-post.md, 07-fluxo-sistemico.md, 15-seguranca-e-boas-praticas.md

---

## Camada

Agrupamento de subsistemas usado para localizar a origem de uma falha. A base usa **dois modelos**,
um por escopo: o *modelo POST* (7 camadas, notação `Camada N: NOME`) e o *modelo sistêmico*
(10 camadas, notação `N - Nome`). O formato do texto identifica o modelo; os números **não** se
correspondem entre eles.

**Nível de confiança:** Confirmado  
**Aplicado em:** 03-taxonomia-camadas.md

---

## CH341A

Programadora de EPROM citada para regravação física do chip de BIOS, usada com clamp SOIC-8 e software de gravação (a fonte cita flashrom e AsProgrammer).

**Nível de confiança:** Confirmado  
**Aplicado em:** 08-diagnostico-por-camada.md

---

## Debug LED

LEDs de diagnóstico presentes em placas-mãe, que a fonte descreve seguindo a sequência CPU → DRAM → VGA → BOOT. O LED em que a sequência trava indica a camada com problema.

**Nível de confiança:** Confirmado  
**Aplicado em:** 06-fluxo-post.md, 09-codigos-post/generico-debug-led.md

---

## DDU (Display Driver Uninstaller)

Utilitário citado para remoção completa de driver de vídeo em Modo de Segurança, antes de instalar driver limpo. Expansão fornecida pela fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 12-correlacoes.md

---

## IMC (Integrated Memory Controller)

Controladora de memória integrada à CPU. A fonte a aponta como suspeita quando módulos *known-good* falham em todos os slots. Expansão fornecida pela fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 12-correlacoes.md, 10-cenarios/

---

## Kernel-Power 41

Evento do Visualizador de Eventos do Windows usado pela fonte como evidência de reinício sem desligamento limpo. O critério PASS de fonte exige zero ocorrências.

**Nível de confiança:** Confirmado  
**Aplicado em:** 13-validacao-final.md, 10-cenarios/reinicializacao-aleatoria.md

---

## Known-good

Componente comprovadamente funcional, usado como referência em teste cruzado. A fonte exige que o substituto tenha a mesma especificação (frequência, CL, tensão).

**Nível de confiança:** Confirmado  
**Aplicado em:** 06-fluxo-post.md, 09-codigos-post/

---

## PCH (Platform Controller Hub)

Chipset da placa-mãe. Expansão fornecida pela fonte na descrição da camada de chipset.

**Nível de confiança:** Confirmado  
**Aplicado em:** 08-diagnostico-por-camada.md

---

## Pass (MemTest86)

Ciclo completo da bateria de testes. Segundo a documentação do desenvolvedor, a bateria padrão executa os testes **0 a 13 — quatorze
testes**. O critério de aprovação adotado pela base é zero erro em **4 passes**.

**Nível de confiança:** Confirmado (critério, pela fonte primária; contagem de testes, pela documentação PassMark)  
**Aplicado em:** 14-ferramentas/memtest86.md

---

## Power drain

Descarga dos capacitores residuais antes de manipular componentes — chamado *flea power* pela Dell
e *residual electrical charge* pela HP. A base adota **30 s** com o botão Power pressionado e o
cabo AC removido, valor que satisfaz e supera os mínimos publicados por Dell (15–20 s) e HP (≈15 s).

**Nível de confiança:** Confirmado — ver [procedimento canônico](15-seguranca-e-boas-praticas.md#procedimento-canônico-de-power-drain)  
**Aplicado em:** 09-codigos-post/, 10-cenarios/nao-liga.md, 15-seguranca-e-boas-praticas.md

---

## PROCHOT

Proteção térmica que, segundo a fonte, em caso extremo provoca desligamento abrupto indistinguível de falha de fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 12-correlacoes.md

---

## Q-Code

Código hexadecimal de dois dígitos exibido em display na placa-mãe. A fonte distingue código **fixo** (travamento — consultar a ficha) de código **progredindo** (POST em andamento).

**Nível de confiança:** Confirmado  
**Aplicado em:** 06-fluxo-post.md, 09-codigos-post/ami-q-code.md

---

## QVL (Qualified Vendor List)

Lista de módulos de memória homologados pelo fabricante da placa-mãe. Expansão fornecida pela fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 08-diagnostico-por-camada.md

---

## Remap

Ação que força a controladora do disco a remapear blocos defeituosos para a área de reserva. A fonte a associa ao atributo S.M.A.R.T. C5.

**Nível de confiança:** Confirmado  
**Aplicado em:** 14-ferramentas/victoria.md

---

## Reseat

Reencaixe do componente no slot, com pressão uniforme. Aparece como primeiro procedimento em falhas de memória e de vídeo.

**Nível de confiança:** Confirmado  
**Aplicado em:** 08-diagnostico-por-camada.md

---

## Ripple

Ondulação residual na saída da fonte. A fonte define tolerância de 120 mV pico a pico na linha +12 V e indica osciloscópio para a medição.

**Nível de confiança:** Confirmado  
**Aplicado em:** 08-diagnostico-por-camada.md

---

## S.M.A.R.T. — IDs 05, C5 e C6

Atributos críticos de saúde do disco. A fonte os identifica como ID 05 (*Reallocated Sectors*), C5 (*Current Pending*) e C6 (*Uncorrectable*), e exige valor zero nos três como critério de aprovação.

**Nível de confiança:** Confirmado  
**Aplicado em:** 13-validacao-final.md, 07-fluxo-sistemico.md, 10-cenarios/bsod.md

---

## ACPI (Advanced Configuration and Power Interface)

Conjunto de tabelas de firmware que descrevem o hardware ao sistema operacional. A fonte registra que erros de ACPI levam a falhas de suspensão/hibernação e à tela azul DRIVER_POWER_STATE_FAILURE, e que atualizar a BIOS costuma corrigir tabelas corrompidas.

**Nível de confiança:** Confirmado  
**Aplicado em:** 14-ferramentas/aida64-etapas-16-30.md, 12-correlacoes.md

---

## BDA (BIOS Data Area) e IVT (Interrupt Vector Table)

Estruturas alojadas nos primeiros 64 KB de memória. A fonte explica que essa região é crítica justamente por contê-las, o que torna sua falha impeditiva do POST.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/ami-legacy.md

---

## DXE (Driver Execution Environment)

Fase do POST em que os drivers do firmware são executados. A fonte registra que travamento nessa fase indica que a CPU começou a executar mas não concluiu. Expansão fornecida pela fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/ami-q-code.md

---

## G-List (Growth Defect List)

Área de reserva do disco para onde o comando de Remap move endereços LBA defeituosos. A fonte registra que, quando a G-List lota, o disco deixa de aceitar novos remapeamentos.

**Nível de confiança:** Confirmado  
**Aplicado em:** 14-ferramentas/victoria.md

---

## GOP (Graphics Output Protocol)

Protocolo de saída de vídeo em ambiente UEFI. A fonte o cita como causa de tela preta ao tentar iniciar o MemTest86 em placas incompatíveis.

**Nível de confiança:** Confirmado  
**Aplicado em:** 14-ferramentas/memtest86.md

---

## HMM (Hardware Maintenance Manual)

Manual de manutenção do fabricante. A fonte o indica, junto ao Lenovo PSREF, como consulta final quando o procedimento documentado não resolve.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/lenovo.md

---

## KBC (Keyboard Controller)

Controlador de teclado. A fonte registra que ele comanda o Gate A20 e que, em sistemas legados, era responsável por habilitar a linha de endereço correspondente — daí falhas de teclado bloquearem o POST.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/ami-legacy.md

---

## ME (Management Engine)

Firmware listado pela fonte entre os componentes da camada de firmware, ao lado do SPI Flash, da EEPROM, da NVRAM do CMOS, das Option ROMs e dos patches de microcode.

**Nível de confiança:** Confirmado  
**Aplicado em:** 08-diagnostico-por-camada.md

---

## OCP (Over Current Protection) e OPP (Over Power Protection)

Proteções da fonte de alimentação: a primeira atua por excesso de corrente numa linha, a segunda
por excesso de potência total. A base registra o disparo de OCP/OPP como causa de a PSU não
sustentar carga de pico, e o desarme por OCP como erro possível durante stress test.

**Nível de confiança:** Confirmado (uso) / Inferido (expansão de OPP, pela nomenclatura corrente do setor)  
**Aplicado em:** 10-cenarios/reinicializacao-aleatoria.md, 14-ferramentas/aida64-etapas-01-15.md

---

## Row Hammer

Falha em que o acesso repetido a uma linha de memória faz a carga elétrica vazar para a linha vizinha e inverter um bit. A fonte a verifica pelo Teste 13 do MemTest86 e registra que módulos DDR3/DDR4 antigos costumam não ter proteção.

**Nível de confiança:** Confirmado  
**Aplicado em:** 14-ferramentas/memtest86.md

---

## SmartBeep

Sinal sonoro em forma de melodia usado por equipamentos Lenovo, interpretável pelo aplicativo Lenovo PC Diagnostics.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/lenovo.md

---

## SPD (Serial Presence Detect)

Chip do módulo de memória que guarda as temporizações. A fonte o cita como origem de incompatibilidade com a controladora e indica o AIDA64 para ler seus dados brutos. Expansão fornecida pela fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/, 14-ferramentas/aida64-etapas-01-15.md

---

## TPM (Trusted Platform Module)

Chip de segurança. A fonte registra seu uso em ThinkPads para criptografia BitLocker e autenticação, lista as causas de falha (firmware corrompido, desabilitação incorreta, defeito físico, reset após atualização de BIOS) e define o critério de validação: TPM reconhecido no BIOS e `tpm.msc` reportando o chip pronto.

**Nível de confiança:** Confirmado  
**Aplicado em:** 09-codigos-post/lenovo.md, 14-ferramentas/aida64-etapas-16-30.md

---

## TDR (Timeout Detection and Recovery)

Mecanismo cujo disparo reinicia o driver de vídeo, podendo gerar tela azul. A fonte o usa como indicador de problema de driver, não de hardware. Expansão fornecida pela fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 12-correlacoes.md

---

## Teste cruzado

Instalação do componente suspeito em outro sistema. A fonte define o critério de decisão: falha em dois sistemas condena o componente; funcionamento em outro sistema condena a placa-mãe.

**Nível de confiança:** Confirmado  
**Aplicado em:** 06-fluxo-post.md

---

## Teste paperclip

Acionamento da fonte fora da placa-mãe, curto-circuitando PS_ON (pino 16, fio verde) ao COM (pino 17, fio preto) do conector de 24 pinos.

**Nível de confiança:** Confirmado  
**Aplicado em:** 10-cenarios/nao-liga.md

---

## TjMax (Tjunction max)

Temperatura de junção máxima do processador: o ponto em que ele aciona os próprios mecanismos de
controle térmico para reduzir potência e limitar temperatura. A fonte cita a faixa 100–105 °C ao
descrever o sintoma de superaquecimento; a Intel informa que o limite varia por produto e fica
entre **100 °C e 110 °C**. É o teto físico que ancora a escala de limiares desta base — não uma
meta operacional.

**Nível de confiança:** Confirmado (uso, pela fonte primária; faixa por produto, pela documentação Intel)  
**Aplicado em:** 10-cenarios/superaquecimento.md, 13-validacao-final.md, 15-seguranca-e-boas-praticas.md

---

## Vdrop / voltage droop

Queda de tensão sob carga. A fonte a associa à proteção OCP/OPP da fonte e ao VRM que não sustenta a carga da CPU.

**Nível de confiança:** Confirmado  
**Aplicado em:** 10-cenarios/, 12-correlacoes.md

---

## Wear Level

Indicador de desgaste de SSD lido via S.M.A.R.T. O critério FAIL registrado é acima de 90 %; o indicador de sucesso é abaixo de 80 %.

**Nível de confiança:** Confirmado  
**Aplicado em:** 13-validacao-final.md

---

## WinDbg (Windows Debugging Tools)

Depurador usado pela fonte para analisar o minidump gerado por uma tela azul. O comando registrado é `!analyze -v`, para identificar o driver em falha. Expansão fornecida pela fonte.

**Nível de confiança:** Confirmado  
**Aplicado em:** 10-cenarios/bsod.md, 19-comandos.md

---

## WinPE

Ambiente de execução independente do Windows instalado, recomendado pela fonte para rodar o Victoria sem interferência do sistema hospedeiro (a fonte cita Sergei Strelec como exemplo).

**Nível de confiança:** Confirmado  
**Aplicado em:** 14-ferramentas/victoria.md

---

## XMP / EXPO / DOCP

Perfis de desempenho de memória gravados no chip SPD do módulo, que substituem os valores JEDEC
padrão por frequência, temporizações e tensão validadas pelo fabricante da memória:

| Sigla | Expansão | Origem |
| --- | --- | --- |
| XMP | *Extreme Memory Profile* | Intel |
| EXPO | *EXtended Profiles for Overclocking* | AMD |
| DOCP | *Direct Over Clock Profile* | ASUS |

A base exige que o perfil esteja **ativo** durante o teste com MemTest86, para não mascarar
instabilidade que só aparece na frequência anunciada.

**Nível de confiança:** Confirmado (uso, pela fonte primária; expansões, por documentação ASUS)  
**Aplicado em:** 14-ferramentas/memtest86.md

---

## ESD (Electrostatic Discharge)

Descarga eletrostática. A norma de referência do setor, ANSI/ESD S20.20, trata como sensíveis os
componentes suscetíveis a partir de **100 V** no modelo de corpo humano e **200 V** no modelo de
dispositivo carregado — valores abaixo do limiar que uma pessoa percebe. Daí a regra de bancada:
não sentir choque não significa que não houve descarga.

**Nível de confiança:** Confirmado — ANSI/ESD S20.20-2021 (EOS/ESD Association)  
**Aplicado em:** 15-seguranca-e-boas-praticas.md, 04-requisitos-e-ferramentas.md

---

## Flea power

Nome usado pela Dell para a carga residual retida nos capacitores depois de o equipamento ser
desligado. A HP chama o mesmo fenômeno de *residual electrical charge*. Ver
[Power drain](#power-drain).

**Nível de confiança:** Confirmado — documentação de suporte da Dell e da HP  
**Aplicado em:** 15-seguranca-e-boas-praticas.md

---

## Hammer Test (Teste 13)

Teste do MemTest86 que verifica a suscetibilidade do módulo a
[Row Hammer](#row-hammer). É o último da bateria padrão, que vai do teste 0 ao teste 13.

**Nível de confiança:** Confirmado — documentação PassMark  
**Aplicado em:** 14-ferramentas/memtest86.md

---

## PSREF (Product Specifications Reference)

Base pública de especificações de produto da Lenovo, citada pela fonte como consulta final quando o
procedimento documentado não resolve, ao lado do [HMM](#hmm-hardware-maintenance-manual).

**Nível de confiança:** Confirmado (uso, pela fonte primária; expansão, pelo portal Lenovo)  
**Aplicado em:** 09-codigos-post/lenovo.md

---

## Siglas de fase do POST

A fonte usa `SEC`, `PEI`, `DXE` e `BDS` no campo `FASE POST`, sempre nesta ordem de execução.

| Sigla | Expansão | O que acontece na fase |
| --- | --- | --- |
| SEC | *Security* | Primeira fase: trata os eventos de reinício, cria armazenamento temporário e serve como raiz de confiança |
| PEI | *Pre-EFI Initialization* | Inicializa CPU, chipset e memória permanente, para que a fase seguinte possa ser carregada |
| DXE | *Driver Execution Environment* | Executa os drivers do firmware e inicializa o restante do hardware |
| BDS | *Boot Device Selection* | Seleciona o dispositivo de boot e passa o controle ao carregador do sistema |

**Nível de confiança:** Confirmado — DXE e BDS expandidos pela própria fonte; SEC e PEI conferidos
na *Platform Initialization Specification* do UEFI Forum. A ordem SEC → PEI → DXE → BDS é a
declarada pela especificação e coincide com a usada no campo `FASE POST`.

## Siglas expandidas fora da fonte primária

As siglas abaixo são usadas pelas planilhas sem expansão. Cada uma foi conferida na publicação de
quem a define, e a expansão está registrada aqui em vez de ficar em aberto. O registro das
consultas está em
[Fontes](references/fontes.md#verificações-independentes-realizadas).

| Termo | Situação | Onde foi confirmado |
| --- | --- | --- |
| BIST | *Built-In Self-Test* | Documentação de suporte da Dell |
| XMP / EXPO / DOCP | *Extreme Memory Profile* / *EXtended Profiles for Overclocking* / *Direct Over Clock Profile* | Documentação de suporte da ASUS |
| SEC, PEI | *Security* e *Pre-EFI Initialization* | *Platform Initialization Specification*, UEFI Forum |
| OPP | *Over Power Protection* — nomenclatura corrente do setor, ao lado de OCP | Inferido pelo uso |
| PSREF | *Product Specifications Reference* — base pública de especificações da Lenovo | Portal PSREF da Lenovo |
| QVL | *Qualified Vendor List* — obtida na página do modelo da placa-mãe, no site do fabricante | Expandida pela própria fonte |

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| o termo era um número de camada | [Taxonomia de camadas](03-taxonomia-camadas.md) |
| o termo era uma ferramenta | [Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md) |
| o termo não está aqui | [Índices cruzados](18-indices-cruzados.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Ambos os arquivos-fonte |
| **Status de confiança** | Confirmado para os termos definidos pela fonte; lacunas sinalizadas por termo |
| **Última verificação contra a fonte** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
