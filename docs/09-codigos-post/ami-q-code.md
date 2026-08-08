<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — AMI Q-Code Hex**

# Códigos POST — AMI Q-Code Hex

> Fichas completas dos códigos de POST da família AMI Q-Code Hex, com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `AMI (Q-Code Hex)`

## Neste documento

- [POST-13 — 00 / D0](#post-13--00--d0)
- [POST-14 — 50 — 55](#post-14--50--55)
- [POST-15 — 63 — 67](#post-15--63--67)
- [POST-16 — 99 / 9A / 9C](#post-16--99--9a--9c)
- [POST-17 — A0 — A2](#post-17--a0--a2)
- [POST-18 — B4](#post-18--b4)
- [POST-19 — D6 / D7](#post-19--d6--d7)
- [POST-20 — FE](#post-20--fe)
- [POST-21 — FF](#post-21--ff)
- [POST-50 — 7F](#post-50--7f)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `AMI (Q-Code Hex)`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 10 código(s) da família `AMI (Q-Code Hex)` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-13 — 00 / D0

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `00 / D0`

### Identificação

#### Interpretação oficial

CPU Initialization Error — Microcode não encontrado ou CPU não responde

#### Componente afetado

CPU

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

SEC Phase (CPU Init)

### Diagnóstico

#### Causa raiz (documentação oficial)

A CPU não é inicializada. O BIOS não encontra microcode compatível para o stepping da CPU, ou a CPU fisicamente não responde. Código 00 no Q-Code geralmente indica que o POST nem iniciou.

#### Condições que geram o erro

1. CPU não suportada pela versão do BIOS instalada.  
2. Pinos do socket LGA tortos.  
3. Conector EPS 8-pin (CPU power) desconectado.  
4. VRM da placa com defeito.  
5. CPU fisicamente danificada.

#### Método de diagnóstico técnico

1. Verificar lista de compatibilidade CPU × BIOS no site do fabricante.  
2. Inspecionar pinos do socket com lupa.  
3. Medir tensão 12V no conector EPS.  
4. Verificar se LEDs de diagnóstico da placa indicam CPU.  
5. Se CPU nova em placa antiga: BIOS Flashback para atualizar sem CPU.

#### Ferramentas oficiais

Multímetro (12V EPS, VCore) / Lupa 10x / BIOS Flashback

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Verificar compatibilidade CPU-BIOS no site do fabricante.  
2. Se CPU requer BIOS mais nova:  

   ASUS: USB BIOS Flashback (pendrive FAT32, porta USB designada, botão 3s).  
   GIGABYTE: Q-Flash Plus (procedimento similar).  
3. Inspecionar socket LGA — pinos tortos = tentar realinhar ou condenar placa.  
4. Verificar conector EPS 8-pin firmemente conectado.  
5. Medir 12V no conector EPS.  
6. Se tudo OK: teste cruzado de CPU.

### Resultado esperado

#### Critério de validação

Q-Code avança além de 00/D0. CPU reconhecida no BIOS. POST completa.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

ASUS Q-Code Reference / GIGABYTE Debug Code List

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-14 — 50 — 55

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `50 — 55`

### Identificação

#### Interpretação oficial

Memory Initialization Error — RAM não detectada ou treinamento falhou (55 mais comum)

#### Componente afetado

RAM / Controladora de Memória

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

PEI (Memory Training)

### Diagnóstico

#### Causa raiz (documentação oficial)

Erro durante a inicialização e treinamento da memória. O código 55 é o mais frequente e indica que nenhum módulo DIMM foi detectado ou que o treinamento de memória falhou completamente.

#### Condições que geram o erro

1. Nenhum módulo instalado.  
2. Módulos nos slots errados.  
3. Contatos da CPU sujos (controladora de memória está na CPU).  
4. Cooler com pressão excessiva empenando pinos do socket.  
5. Módulo incompatível (fora da QVL).

#### Método de diagnóstico técnico

1. Limpar contatos LGA da CPU com isopropanol e escova antiestática.  
2. Afrouxar cooler 1/4 de volta (pressão excessiva pode empurrar CPU contra pinos).  
3. Testar slot único com módulo known-good.  
4. Verificar QVL.  
5. Reset CMOS.

#### Ferramentas oficiais

Isopropanol 99% / Lupa 10x / Escova antiestática / QVL do fabricante

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain.  
2. Remover cooler da CPU.  
3. Remover CPU cuidadosamente.  
4. Limpar contatos LGA da CPU (parte inferior) com isopropanol 99% e escova macia.  
5. Inspecionar socket com lupa (debris, pinos tortos).  
6. Reinstalar CPU e cooler (NÃO apertar excessivamente).  
7. Inserir 1 módulo no slot A2.  
8. Reset CMOS.  
9. Ligar e aguardar (DDR5: até 3 min).  
10. Se persistir: módulo ou slot defeituoso.

### Resultado esperado

#### Critério de validação

Q-Code avança além de 55. RAM reconhecida com capacidade correta. MemTest86 sem erros.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

ASUS Q-Code Reference / AMI Aptio Status Codes

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-15 — 63 — 67

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `63 — 67`

### Identificação

#### Interpretação oficial

CPU DXE Initialization Started — Travamento indica falha VCore/VRM

#### Componente afetado

CPU / VRM

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

DXE Phase

### Diagnóstico

#### Causa raiz (documentação oficial)

A fase DXE (Driver Execution Environment) da CPU iniciou mas travou. Indica que a CPU começou a executar mas encontrou instabilidade, geralmente relacionada a VCore insuficiente ou VRM com defeito.

#### Condições que geram o erro

1. VRM da placa com capacitores defeituosos (inchados, vazando).  
2. VCore instável ou insuficiente.  
3. CPU com defeito parcial.  
4. BIOS corrompida (parcialmente funcional).

#### Método de diagnóstico técnico

1. Inspeção visual dos capacitores VRM (inchados? vazando?).  
2. Medir VCore nos pontos de teste da placa.  
3. Reset CMOS.  
4. Teste cruzado de CPU.  
5. Se VRM com defeito visual: placa condenada (reparo avançado).

#### Ferramentas oficiais

Multímetro (VCore) / Inspeção visual VRM / Lupa

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Reset CMOS para defaults.  
2. Inspecionar VRM visualmente:  

   — Capacitores inchados/vazando = placa condenada ou reparo SMD.  
   — MOSFETs queimados (marcas escuras) = placa condenada.  
3. Medir VCore (tipicamente 0.8-1.4V sob carga).  
4. Testar outra CPU known-good.  
5. Se CPU boa funciona: CPU original com defeito.  
6. Se CPU boa também trava: placa com defeito (VRM/PCH).

### Resultado esperado

#### Critério de validação

Q-Code avança além de 67. POST completa. CPU estável sob carga.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

ASUS Q-Code Reference

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-16 — 99 / 9A / 9C

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `99 / 9A / 9C`

### Identificação

#### Interpretação oficial

Super IO Initialization / USB Detect — Problema em periféricos ou portas

#### Componente afetado

Super I/O / USB / PCIe

#### Camada de diagnóstico

Camada 7: Periféricos Críticos

#### Fase POST

DXE I/O Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O sistema está na fase de inicialização do Super I/O e detecção de dispositivos USB/PCIe. Travamento nesta fase indica conflito ou curto em dispositivo conectado.

#### Condições que geram o erro

1. Dispositivo USB com defeito ou em curto.  
2. Front Panel USB/Audio com conector danificado.  
3. Dispositivo PCIe causando conflito.  
4. Super I/O chip com defeito.

#### Método de diagnóstico técnico

1. Desconectar TODOS os dispositivos USB.  
2. Desconectar headers do front panel (USB, Audio).  
3. Testar boot mínimo (CPU+RAM+Vídeo apenas).  
4. Se POST OK: reconectar um por um para isolar.  
5. Verificar portas USB fisicamente (pinos tortos, debris).

#### Ferramentas oficiais

Inspeção Visual das portas / Boot mínimo (bare minimum)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desconectar todos os dispositivos USB (front e rear).  
2. Desconectar headers internos: F_USB1, F_USB2, F_AUDIO, F_PANEL (se possível).  
3. Ligar apenas com CPU + RAM + GPU + Fonte.  
4. Se POST OK: reconectar headers um a um, ligando entre cada um.  
5. Quando falhar: último header conectado é o culpado.  
6. Inspecionar conector/cabo do header.  
7. Se falhar mesmo sem nada: Super I/O chip defeituoso.

### Resultado esperado

#### Critério de validação

Q-Code avança além de 9C. Todos os dispositivos USB reconhecidos. Sem travamentos na inicialização.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

ASUS Q-Code Reference / AMI Aptio Status Codes

### Próximos passos

- Ficha da camada: [Camada 7: Periféricos Críticos](../08-diagnostico-por-camada.md#camada-7--periféricos-críticos)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-17 — A0 — A2

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `A0 — A2`

### Identificação

#### Interpretação oficial

IDE/SATA Initialization — Travamento indica falha em disco/SSD

#### Componente afetado

SATA / M.2 / NVMe

#### Camada de diagnóstico

Camada 7: Periféricos Críticos

#### Fase POST

DXE Storage Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O BIOS está inicializando controladores IDE/SATA/NVMe. Travamento indica dispositivo de armazenamento com defeito, cabo SATA ruim, ou M.2 mal encaixado.

#### Condições que geram o erro

1. SSD/HDD com firmware travado (busy/hung).  
2. Cabo SATA defeituoso ou mal conectado.  
3. M.2 NVMe mal encaixado no slot.  
4. Porta SATA da placa com defeito.  
5. Fonte sem alimentação SATA suficiente.

#### Método de diagnóstico técnico

1. Desconectar todos os discos (SATA e M.2).  
2. Se POST OK sem discos: reconectar um a um.  
3. Trocar cabo SATA.  
4. Verificar encaixe do M.2 (parafuso de fixação).  
5. Verificar SMART do disco em outro sistema.

#### Ferramentas oficiais

Teste SMART (CrystalDiskInfo) / Cabos SATA novos / Chave M.2

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desconectar TODOS os dispositivos de armazenamento (SATA + M.2).  
2. Ligar sistema — deve POST sem discos.  
3. Se POST OK: reconectar discos um a um:  

   a. Ligar, conectar 1 disco SATA, reiniciar.  
   b. Se travar: disco com defeito ou cabo ruim.  
   c. Trocar cabo SATA e retestar.  
4. Para M.2: remover, limpar contatos com isopropanol, reinserir, apertar parafuso.  
5. Se nenhum disco funciona: porta SATA/M.2 da placa com defeito.

### Resultado esperado

#### Critério de validação

Q-Code avança. Discos reconhecidos no BIOS. SMART OK (CrystalDiskInfo). Boot normal.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

ASUS Q-Code Reference

### Próximos passos

- Ficha da camada: [Camada 7: Periféricos Críticos](../08-diagnostico-por-camada.md#camada-7--periféricos-críticos)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-18 — B4

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `B4`

### Identificação

#### Interpretação oficial

USB Hot Plug Error — Dispositivo USB em curto ou porta danificada

#### Componente afetado

USB

#### Camada de diagnóstico

Camada 7: Periféricos Críticos

#### Fase POST

DXE USB Init

### Diagnóstico

#### Causa raiz (documentação oficial)

Erro durante hot-plug de dispositivo USB. Indica que um dispositivo USB conectado está em curto-circuito ou que uma porta USB está fisicamente danificada.

#### Condições que geram o erro

1. Dispositivo USB com curto interno (hub, pen drive, etc.).  
2. Porta USB traseira ou frontal com pinos tortos/curto.  
3. Cabo USB interno (header) com fio rompido.

#### Método de diagnóstico técnico

1. Remover todos dispositivos USB.  
2. Inspecionar todas as portas USB (detritos, pinos tortos).  
3. Testar sem headers USB frontais.  
4. Reconectar dispositivos um a um.

#### Ferramentas oficiais

Inspeção Visual / Multímetro (curto nos pinos USB)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Remover TODOS os dispositivos USB.  
2. Inspecionar portas USB traseiras com lanterna (pinos tortos, debris metálico).  
3. Desconectar headers USB frontais da placa-mãe.  
4. Ligar sistema.  
5. Se POST OK: reconectar dispositivos/headers um a um.  
6. Se porta específica causa falha: porta danificada — desabilitar no BIOS ou reparo físico.

### Resultado esperado

#### Critério de validação

POST completa. Todos os dispositivos USB reconhecidos sem erros. Sem desconexões aleatórias.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

ASUS Q-Code Reference

### Próximos passos

- Ficha da camada: [Camada 7: Periféricos Críticos](../08-diagnostico-por-camada.md#camada-7--periféricos-críticos)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-19 — D6 / D7

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `D6 / D7`

### Identificação

#### Interpretação oficial

No Console Output Devices Found — GPU não detectada para saída de vídeo

#### Componente afetado

GPU / Saída de Vídeo

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

DXE Console Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O BIOS não encontrou nenhum dispositivo de saída de console (GPU) para exibir vídeo. Diferente do erro de VRAM — aqui a GPU simplesmente não é detectada no barramento.

#### Condições que geram o erro

1. GPU não encaixada corretamente no slot PCIe.  
2. GPU com BIOS dual (chave seletora Silent/OC na posição errada).  
3. Slot PCIe com defeito.  
4. BIOS configurada para saída por iGPU mas somente GPU dedicada presente.  
5. GPU incompatível (muito antiga para UEFI).

#### Método de diagnóstico técnico

1. Limpar slot PCIe e contatos da GPU.  
2. Verificar chave seletora de BIOS na GPU (se existir).  
3. Testar GPU em outro slot PCIe (se disponível).  
4. Testar outra GPU.  
5. Verificar se monitor está na saída correta.

#### Ferramentas oficiais

Teste Monitor Externo / GPU known-good / Cabo de vídeo alternativo

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain.  
2. Remover GPU, limpar contatos, limpar slot.  
3. Reinserir GPU firmemente.  
4. Verificar chave de BIOS na GPU (ex: ASUS Dual BIOS switch).  
5. Conectar monitor diretamente à GPU (não à placa-mãe).  
6. Testar cabo de vídeo alternativo (HDMI → DP ou vice-versa).  
7. Se persistir: testar outra GPU.  
8. Se nenhuma GPU funciona neste slot: testar outro slot PCIe x16.  
9. Reset CMOS — verificar Primary Display = PCIe.

### Resultado esperado

#### Critério de validação

Q-Code avança. Vídeo funcional. GPU reconhecida corretamente no BIOS.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

ASUS Q-Code Reference

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-20 — FE

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `FE`

### Identificação

#### Interpretação oficial

Reserved / Pre-POST Hang — Travamento antes do POST iniciar

#### Componente afetado

Placa-mãe (Estrutural)

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

Pre-SEC

### Diagnóstico

#### Causa raiz (documentação oficial)

Código reservado pela AMI. Na prática, indica que o sistema travou antes de iniciar o POST. Geralmente causado por curto-circuito grave no chipset, falha estrutural da placa-mãe, ou problema de alimentação primária.

#### Condições que geram o erro

1. Curto-circuito no PCH/Chipset.  
2. VRM com componente em curto.  
3. Trilha rompida em camada interna da PCB.  
4. Capacitor em curto-circuito.  
5. Fonte de alimentação com defeito.

#### Método de diagnóstico técnico

1. Teste de fonte: verificar standby 5VSB e 12V com multímetro.  
2. Teste olfativo (componente queimado?).  
3. Inspecionar placa com lupa (capacitores, MOSFETs, marcas de queimado).  
4. Boot mínimo absoluto (CPU + 1 RAM + fonte, sem GPU).  
5. Se persistir: placa condenada.

#### Ferramentas oficiais

Multímetro (5VSB, 12V, 3.3V, 5V) / Inspeção visual / Lupa

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desconectar TUDO exceto CPU e fonte.  
2. Medir 5VSB no conector 24-pin (pino 9, fio roxo) — deve ser 5V com AC conectado.  
3. Se 5VSB ausente: fonte com defeito.  
4. Se 5VSB OK: ligar e medir 12V, 5V, 3.3V.  
5. Se todas as tensões OK mas código FE persiste: placa-mãe com curto interno.  
6. Inspecionar visualmente (capacitores, MOSFETs, marcas de queimado).  
7. Se não há sinal visual: condenação da placa.  

SERVIDOR: Substituir system board. Testar CPU e RAM em placa substituta.

### Resultado esperado

#### Critério de validação

Se placa condenada: N/A. Se fonte era o problema: POST completa com fonte nova. Todas as tensões dentro de spec ATX.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

AMI Reserved Codes / ASUS Debug Reference

### Próximos passos

- Ficha da camada: [Camada 5: Chipset / Motherboard](../08-diagnostico-por-camada.md#camada-5--chipset--motherboard)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-21 — FF

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** AMI Q-Code — ASUS / GIGABYTE Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `FF`

### Identificação

#### Interpretação oficial

Recovery/Boot — Comportamento depende do momento: fixo=falha / final=boot OK

#### Componente afetado

Variável

#### Camada de diagnóstico

Camada 6: Firmware / Camada 2: CPU

#### Fase POST

Variável

### Diagnóstico

#### Causa raiz (documentação oficial)

FF no Q-Code tem significado duplo: se aparece fixo imediatamente ao ligar, indica falha grave (CPU/VRM/BIOS morta). Se aparece após sequência de outros códigos e o sistema inicia, é o código final indicando que o controle foi passado ao OS.

#### Condições que geram o erro

Se fixo ao ligar:  
1. VRM com defeito.  
2. CPU morta.  
3. BIOS completamente corrompida.  
4. Fonte sem potência.  

Se final após sequência:  
1. Normal — sistema está iniciando o OS.

#### Método de diagnóstico técnico

1. Observar QUANDO o FF aparece:  

   — Imediato e fixo = falha grave.  
   — Após sequência (00→55→A0→FF) = normal.  
2. Se fixo: seguir diagnóstico de código FE.  
3. Verificar LED de diagnóstico da placa (CPU/DRAM/VGA/BOOT).

#### Ferramentas oficiais

Observação do comportamento do Q-Code / LEDs de diagnóstico

### Execução da correção

#### Procedimento de correção (passo a passo)

Se FF fixo ao ligar:  
1. Seguir procedimento completo de código FE (curto/placa condenada).  
2. Tentar BIOS Flashback (pode ser BIOS corrompida).  
3. Teste cruzado CPU.  

Se FF após sequência normal:  
1. Não é erro — sistema está funcionando.  
2. Se não há vídeo mas Q-Code mostra FF após sequência: problema de saída de vídeo (monitor, cabo, GPU).

### Resultado esperado

#### Critério de validação

Se fixo: depende da causa raiz encontrada. Se normal: OS carrega, sistema operacional funcional.

### Risco e origem

#### Risco / criticidade

Variável

#### Fonte oficial

ASUS Q-Code Reference

### Próximos passos

- Camada declarada: `Camada 6: Firmware / Camada 2: CPU` — valor composto ou variável; ver [Taxonomia de camadas](../03-taxonomia-camadas.md)
- **Código ambíguo.** Confira o critério de diferenciação em [Ambiguidade de códigos](../11-ambiguidades.md#q-code-ff) antes de aplicar o procedimento.
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-50 — 7F

**Fabricante BIOS:** AMI (Q-Code Hex)  
**Fabricante / plataforma:** ASUS / GIGABYTE — Desktop  
**Tipo de sinal:** Hex Q-Code (Display)  
**Código:** `7F`

### Identificação

#### Interpretação oficial

Check User Input (Waiting) — Sistema aguardando input do usuário

#### Componente afetado

Teclado / BIOS Setup

#### Camada de diagnóstico

Camada 7: Periféricos Críticos

#### Fase POST

BDS (Boot Device Selection)

### Diagnóstico

#### Causa raiz (documentação oficial)

O sistema está pausado aguardando interação do usuário. Geralmente aparece quando o BIOS requer que o usuário pressione F1 (para continuar com erro) ou Del/F2 (para entrar no Setup). NÃO é um erro.

#### Condições que geram o erro

1. BIOS detectou configuração alterada e pede confirmação.  
2. Overclocking falhou e BIOS pede F1 para defaults.  
3. Novo hardware detectado.  
4. Erro anterior não crítico registrado.

#### Método de diagnóstico técnico

1. Verificar se há teclado funcional conectado.  
2. Pressionar F1 ou Del conforme mensagem na tela.  
3. Se não há mensagem: verificar vídeo.

#### Ferramentas oficiais

Teclado funcional conectado

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Conectar teclado USB funcional.  
2. Pressionar F1 para continuar ou Del/F2 para entrar no BIOS Setup.  
3. Se aparece repetidamente:  

   a. Entrar no BIOS e verificar se há warnings.  
   b. Verificar se OC falhou (BIOS pode ter revertido para defaults).  
   c. Salvar configurações e reiniciar (F10 → Save & Exit).  
4. Se teclado não responde: testar outra porta USB ou teclado PS/2.

### Resultado esperado

#### Critério de validação

Sistema avança para boot do OS. Q-Code passa de 7F para códigos de boot.

### Risco e origem

#### Risco / criticidade

Baixo

#### Fonte oficial

ASUS Q-Code Reference / GIGABYTE Debug Code List

### Próximos passos

- Ficha da camada: [Camada 7: Periféricos Críticos](../08-diagnostico-por-camada.md#camada-7--periféricos-críticos)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou o código aqui | [Índice de códigos POST](00-indice-codigos.md) — catálogo completo |
| suspeita que o código tem outro significado | [Ambiguidade de códigos](../11-ambiguidades.md) |
| quer saber o que testar naquele subsistema | [Diagnóstico por camada](../08-diagnostico-por-camada.md) |
| aplicou a correção e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
