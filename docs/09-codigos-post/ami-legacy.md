<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — AMI BIOS Legacy**

# Códigos POST — AMI BIOS Legacy

> Fichas completas dos códigos de POST da família AMI BIOS Legacy, com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `AMI (Legacy BIOS)`

## Neste documento

- [POST-01 — 1 Beep Curto](#post-01--1-beep-curto)
- [POST-02 — 2 ou 3 Beeps Curtos](#post-02--2-ou-3-beeps-curtos)
- [POST-03 — 4 Beeps Curtos](#post-03--4-beeps-curtos)
- [POST-04 — 5 Beeps Curtos](#post-04--5-beeps-curtos)
- [POST-05 — 6 Beeps Curtos](#post-05--6-beeps-curtos)
- [POST-06 — 7 Beeps Curtos](#post-06--7-beeps-curtos)
- [POST-07 — 8 Beeps Curtos](#post-07--8-beeps-curtos)
- [POST-08 — 9 Beeps Curtos](#post-08--9-beeps-curtos)
- [POST-09 — 10 Beeps Curtos](#post-09--10-beeps-curtos)
- [POST-10 — 11 Beeps Curtos](#post-10--11-beeps-curtos)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `AMI (Legacy BIOS)`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 10 código(s) da família `AMI (Legacy BIOS)` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-01 — 1 Beep Curto

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `1 Beep Curto`

### Identificação

#### Interpretação oficial

DRAM Refresh Failure — Falha no circuito de refresh da DRAM

#### Componente afetado

RAM (Módulos DIMM)

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Init (PEI)

### Diagnóstico

#### Causa raiz (documentação oficial)

Circuito de refresh da DRAM não responde. Timer de refresh (controladora de memória integrada à CPU em plataformas modernas, ou northbridge em legadas) não consegue atualizar os capacitores das células DRAM dentro do intervalo especificado (tipicamente 64ms).

#### Condições que geram o erro

1. Módulo DIMM com defeito físico (célula morta).  
2. Slot DIMM com oxidação ou pino torto.  
3. Tensão VDRAM fora de especificação (DDR4: 1.2V ±5%).  
4. Incompatibilidade de timing SPD vs controladora.

#### Método de diagnóstico técnico

1. Power drain completo (desligar, remover cabo AC, segurar power 30s).  
2. Inspecionar visualmente slots DIMM com lupa (pinos tortos, oxidação).  
3. Medir VDRAM no slot com multímetro (pinos de alimentação do DIMM).  
4. Testar módulo individual em cada slot (isolar slot vs módulo).  
5. Verificar SPD com CPU-Z ou equivalente se POST parcial.

#### Ferramentas oficiais

MemTest86 (bootável) / Multímetro digital (VDRAM) / Lupa 10x

### Execução da correção

#### Procedimento de correção (passo a passo)

DESKTOP:  
1. Desligar completamente e remover cabo AC.  
2. Segurar botão power 30 segundos (descarga capacitores).  
3. Remover todos os módulos DIMM.  
4. Limpar contatos dourados com borracha branca (isopropanol 99%).  
5. Limpar slots com ar comprimido.  
6. Inserir 1 módulo no slot A2 (ou slot primário conforme manual da placa).  
7. Ligar e verificar se POST completa.  
8. Se OK, adicionar módulos um a um.  
9. Se falhar em todos os slots com RAM sabidamente boa: falha na controladora de memória (CPU ou northbridge).  

NOTEBOOK:  
1. Remover bateria e AC.  
2. Acessar compartimento SO-DIMM.  
3. Mesmo procedimento de limpeza.  
4. Testar slot individual.

### Resultado esperado

#### Critério de validação

POST completa com 1 beep curto (AMI) ou silêncio + vídeo. MemTest86 sem erros em 4 passes completos. VDRAM estável em 1.2V (DDR4) / 1.1V (DDR5).

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

AMI BIOS Beep Code Reference — AMI Technical Documentation

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-02 — 2 ou 3 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `2 ou 3 Beeps Curtos`

### Identificação

#### Interpretação oficial

Base 64K Memory Failure — Falha nos primeiros 64KB de RAM

#### Componente afetado

RAM (Base Memory)

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Init (PEI)

### Diagnóstico

#### Causa raiz (documentação oficial)

Os primeiros 64KB de memória (Base Memory) não passam no teste de leitura/escrita. Esta região é crítica pois contém a IVT (Interrupt Vector Table) e a BDA (BIOS Data Area) em modo real.

#### Condições que geram o erro

1. Primeiro módulo DIMM defeituoso.  
2. Falha no canal primário de memória (Channel A).  
3. Controladora de memória com defeito.  
4. BIOS não consegue treinar a memória no timing correto.

#### Método de diagnóstico técnico

1. Testar com pente único no slot primário (geralmente Slot 1 / A1 ou A2).  
2. Reset CMOS (jumper CLR_CMOS por 10s com AC desconectado).  
3. Trocar módulo por known-good (mesmo spec: freq, CL, voltagem).  
4. Se falhar com múltiplos módulos bons: falha controladora (CPU).

#### Ferramentas oficiais

Teste Cruzado com RAM validada / POST Card (opcional)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain 30s.  
2. Remover todos os módulos.  
3. Inserir 1 módulo known-good no slot A1/A2.  
4. Reset CMOS via jumper (mover para posição CLR por 10s, retornar).  
5. Ligar sistema.  
6. Se POST OK: módulo original defeituoso.  
7. Se falhar: testar outro slot.  
8. Se falhar em todos os slots: controladora de memória (CPU) ou trilha na placa-mãe.

### Resultado esperado

#### Critério de validação

POST completa. MemTest86 sem erros. Sistema estável sob carga.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

AMI BIOS Beep Code Reference

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-03 — 4 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `4 Beeps Curtos`

### Identificação

#### Interpretação oficial

System Timer Failure — Falha no Timer do Sistema (8254/equivalente)

#### Componente afetado

Timer / Chipset (PCH/SIO)

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

Chipset Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O timer programável do sistema (historicamente o 8254 PIT, atualmente integrado ao PCH/SIO) não responde ou gera frequência incorreta. O cristal de 32.768 kHz que alimenta o RTC pode estar defeituoso.

#### Condições que geram o erro

1. Cristal de 32.768 kHz defeituoso.  
2. Bateria CR2032 descarregada (< 2.8V).  
3. Chip PCH/Southbridge com defeito.  
4. Trilha interrompida entre cristal e chip.

#### Método de diagnóstico técnico

1. Medir tensão da bateria CR2032 (deve ser ≥ 2.9V).  
2. Com osciloscópio: verificar sinal de 32.768 kHz nos pinos do cristal.  
3. Reset CMOS completo.  
4. Se persistir: falha no PCH — requer reballing BGA ou troca da placa.

#### Ferramentas oficiais

Osciloscópio (cristal 32kHz) / Multímetro (bateria CR2032)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Trocar bateria CR2032 por nova (verificar tensão antes: ≥ 3.0V).  
2. Reset CMOS via jumper (10s com AC desconectado).  
3. Se persistir:  

   DESKTOP: Falha no PCH/Chipset — placa condenada ou reparo BGA especializado.  
   SERVIDOR: Substituir system board.

### Resultado esperado

#### Critério de validação

RTC mantém data/hora após power off. POST completa sem erros de timer. Cristal oscila a 32.768 kHz ±20ppm.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

AMI BIOS Beep Code Reference / Intel PCH Datasheet

### Próximos passos

- Ficha da camada: [Camada 5: Chipset / Motherboard](../08-diagnostico-por-camada.md#camada-5--chipset--motherboard)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-04 — 5 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `5 Beeps Curtos`

### Identificação

#### Interpretação oficial

CPU Error — Processador não responde ou falha de instrução

#### Componente afetado

CPU (Processador)

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

CPU Init (SEC/PEI)

### Diagnóstico

#### Causa raiz (documentação oficial)

O processador não executa instruções corretamente ou não é detectado pela placa-mãe. Pode indicar incompatibilidade de microcode, dano físico nos pinos/pads, ou falha na alimentação VCore.

#### Condições que geram o erro

1. Pinos LGA do socket tortos ou contaminados.  
2. Alimentação EPS 12V (4+4 ou 8 pin) desconectada ou com defeito.  
3. CPU incompatível com a versão do BIOS.  
4. Pasta térmica excessiva vazou para o socket.  
5. VRM da placa-mãe com defeito (VCore ausente).

#### Método de diagnóstico técnico

1. Inspeção visual do socket LGA com lupa 10x (pinos tortos, debris).  
2. Medir tensão EPS 12V no conector (deve ser 12V ±5%).  
3. Medir VCore nos pontos de teste da placa (varia por modelo, ~0.8-1.4V).  
4. Verificar lista de CPUs suportadas no site do fabricante da placa.  
5. Testar CPU known-good compatível.

#### Ferramentas oficiais

Multímetro (VCore, EPS 12V) / Lupa 10x / Lista de compatibilidade CPU

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain.  
2. Remover cooler cuidadosamente (girar para soltar pasta).  
3. Limpar pasta térmica residual com isopropanol 99%.  
4. Inspecionar socket LGA — se pinos tortos: tentar alinhar com agulha (risco alto).  
5. Verificar conector EPS 12V (4+4 ou 8 pinos) firmemente conectado.  
6. Medir 12V no conector EPS com multímetro.  
7. Se CPU nova: verificar se BIOS suporta (flash via BIOS Flashback se disponível).  
8. Reaplicar pasta térmica (grão de arroz no centro).  
9. Reinstalar cooler com pressão uniforme.  

SERVIDOR: Verificar ambos sockets se dual-CPU. Testar CPU em socket alternativo.

### Resultado esperado

#### Critério de validação

POST completa. CPU reconhecida no BIOS com modelo e stepping corretos. VCore estável. Stress test (Prime95 / AIDA64) estável por 30 min.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

AMI BIOS Beep Code Reference / Intel LGA Socket Spec

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-05 — 6 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `6 Beeps Curtos`

### Identificação

#### Interpretação oficial

Gate A20 Error — Falha no controlador de teclado (KBC)

#### Componente afetado

KBC / Super I/O

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

KBC Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O Gate A20, controlado pelo KBC (Keyboard Controller), não alterna corretamente. Em sistemas legados, o KBC era responsável por habilitar a linha de endereço A20 para acesso a memória acima de 1MB. Em sistemas modernos, esta função está no Super I/O ou PCH.

#### Condições que geram o erro

1. Chip Super I/O com defeito ou oxidação.  
2. Teclado PS/2 causando curto no KBC.  
3. Firmware do KBC corrompido.  
4. Trilha interrompida entre Super I/O e PCH.

#### Método de diagnóstico técnico

1. Desconectar todos os teclados (PS/2 e USB).  
2. Limpar portas I/O traseiras com ar comprimido.  
3. Inspecionar chip Super I/O visualmente (oxidação, pinos com solda fria).  
4. Testar com teclado USB vs PS/2 para isolar.

#### Ferramentas oficiais

Teclado known-good (USB e PS/2) / Inspeção visual do Super I/O

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desconectar todos os periféricos de entrada.  
2. Limpar conectores I/O com isopropanol.  
3. Tentar POST sem teclado.  
4. Se POST OK sem teclado: teclado com defeito ou porta PS/2 com curto.  
5. Se persistir: falha no Super I/O — requer reparo em nível de componente ou troca da placa.

### Resultado esperado

#### Critério de validação

POST completa. Teclado funcional em BIOS Setup. Gate A20 reportado OK no log POST.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

AMI BIOS Beep Code Reference / Super I/O Datasheet

### Próximos passos

- Ficha da camada: [Camada 5: Chipset / Motherboard](../08-diagnostico-por-camada.md#camada-5--chipset--motherboard)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-06 — 7 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `7 Beeps Curtos`

### Identificação

#### Interpretação oficial

Processor Exception Interrupt Error — Erro de exceção da CPU

#### Componente afetado

CPU (Processador)

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

CPU Init

### Diagnóstico

#### Causa raiz (documentação oficial)

A CPU gerou uma exceção inesperada durante o POST. Pode ser causado por instabilidade de clock, VCore insuficiente, ou dano físico no die do processador.

#### Condições que geram o erro

1. Overclock instável (multiplicador ou BCLK muito alto).  
2. VCore abaixo do necessário para a frequência.  
3. CPU com defeito físico no die (degradação por calor/eletromigração).  
4. Instabilidade na alimentação VRM.

#### Método de diagnóstico técnico

1. Reset CMOS para defaults (eliminar OC).  
2. Se OC: reduzir multiplicador e aumentar VCore marginalmente.  
3. Verificar estabilidade VRM (capacitores inchados?).  
4. Teste cruzado com outra CPU.

#### Ferramentas oficiais

BIOS Setup (AI Tweaker / Extreme Tweaker) / Multímetro (VCore)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Reset CMOS para defaults de fábrica.  
2. Se OC ativo: carregar XMP/DOCP apenas, sem OC manual.  
3. Se persistir em defaults:  

   a. Verificar capacitores VRM visualmente (abaulados = defeito).  
   b. Medir VCore nos pontos de teste.  
   c. Teste cruzado com CPU known-good.  
4. Se falhar com CPU boa: VRM da placa com defeito.

### Resultado esperado

#### Critério de validação

POST completa em defaults. CPU estável em stress test (Prime95 Small FFTs, 30 min). Sem WHEA errors no Event Viewer.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

AMI BIOS Beep Code Reference

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-07 — 8 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `8 Beeps Curtos`

### Identificação

#### Interpretação oficial

Display Memory R/W Error — Falha na memória de vídeo (VRAM)

#### Componente afetado

GPU / VRAM

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

Video Init

### Diagnóstico

#### Causa raiz (documentação oficial)

Falha no teste de leitura/escrita da memória de vídeo. Em sistemas com GPU dedicada, indica defeito na VRAM da placa de vídeo. Em sistemas com iGPU, pode indicar falha na RAM do sistema alocada para gráficos.

#### Condições que geram o erro

1. VRAM da GPU com defeito (chips de memória soldados).  
2. GPU mal encaixada no slot PCIe.  
3. Slot PCIe com oxidação nos contatos.  
4. Em iGPU: RAM do sistema com defeito (memória compartilhada).

#### Método de diagnóstico técnico

1. Remover GPU e limpar contatos dourados com borracha branca.  
2. Limpar slot PCIe com ar comprimido.  
3. Testar outra GPU known-good.  
4. Se iGPU: testar RAM do sistema (pois iGPU usa RAM compartilhada).  
5. Verificar se há saída de vídeo pela iGPU (remover GPU dedicada).

#### Ferramentas oficiais

Borracha branca / Limpa Contato eletrônico / GPU known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain.  
2. Remover GPU dedicada.  
3. Limpar contatos PCIe da GPU com borracha branca + isopropanol.  
4. Limpar slot PCIe com ar comprimido.  
5. Reinserir GPU com pressão firme e uniforme.  
6. Verificar cabo de alimentação PCIe da fonte (6+2 pinos).  
7. Ligar e testar.  
8. Se persistir: testar outra GPU.  
9. Se outra GPU funciona: GPU original com VRAM defeituosa (condenação ou reparo BGA).  

Se iGPU: seguir procedimento de diagnóstico de RAM.

### Resultado esperado

#### Critério de validação

POST completa com vídeo funcional. Sem artefatos visuais. GPU-Z reporta VRAM corretamente. FurMark estável por 15 min.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

AMI BIOS Beep Code Reference

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-08 — 9 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `9 Beeps Curtos`

### Identificação

#### Interpretação oficial

ROM Checksum Error — BIOS Corrompida

#### Componente afetado

BIOS / EEPROM

#### Camada de diagnóstico

Camada 6: Firmware

#### Fase POST

BIOS Verify

### Diagnóstico

#### Causa raiz (documentação oficial)

O checksum da ROM do BIOS não confere com o valor esperado. O firmware armazenado na EEPROM/SPI Flash está corrompido. Pode ocorrer após falha de energia durante atualização, degradação da memória flash, ou ataque de malware.

#### Condições que geram o erro

1. Interrupção durante flash do BIOS.  
2. Degradação natural da EEPROM/SPI Flash.  
3. Bateria CR2032 descarregada causando corrupção de dados.  
4. Malware de BIOS (raro, mas documentado: Mebromi, LoJax).

#### Método de diagnóstico técnico

1. Trocar bateria CR2032.  
2. Tentar BIOS Recovery nativo (varia por fabricante).  
3. Se não há recovery: regravação externa via programadora.

#### Ferramentas oficiais

Programadora EPROM (CH341A) / Pendrive FAT32 / Bateria CR2032 nova

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Trocar bateria CR2032.  
2. Tentar BIOS Recovery:  

   ASUS: Renomear arquivo BIOS para modelo correto, colocar em pendrive FAT32, inserir na porta USB BIOS Flashback, segurar botão Flashback 3s.  
   GIGABYTE: Q-Flash Plus — pendrive FAT32 na porta designada, botão Q-Flash Plus.  
   MSI: Flash BIOS Button — procedimento similar.  
3. Se não há Recovery nativo:  

   a. Identificar chip BIOS (geralmente Winbond/MXIC SPI Flash 8-pin).  
   b. Remover chip (se em socket) ou usar clamp SOIC-8.  
   c. Conectar ao programadora CH341A.  
   d. Gravar firmware correto baixado do site do fabricante.  
   e. Reinstalar chip.  
4. Ligar e verificar POST.

### Resultado esperado

#### Critério de validação

POST completa. BIOS Setup acessível. Versão de firmware correta exibida. Data/hora mantidas após reboot.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

AMI BIOS Recovery Procedures / Fabricante da placa-mãe

### Próximos passos

- Ficha da camada: [Camada 6: Firmware](../08-diagnostico-por-camada.md#camada-6--firmware-biosuefi)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-09 — 10 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `10 Beeps Curtos`

### Identificação

#### Interpretação oficial

CMOS Shutdown Register R/W Error — Falha no registro de shutdown do CMOS

#### Componente afetado

CMOS / Super I/O

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

CMOS Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O registro de shutdown do CMOS (usado para controlar sequências de reinício e modos de operação) não pode ser lido ou escrito corretamente.

#### Condições que geram o erro

1. Chip CMOS/RTC com defeito (integrado ao PCH em sistemas modernos).  
2. Super I/O com falha parcial.  
3. Trilhas de comunicação entre CMOS e CPU/chipset interrompidas.  
4. Bateria CR2032 descarregada.

#### Método de diagnóstico técnico

1. Reset CMOS via jumper CLR_CMOS (10s com AC desconectado).  
2. Trocar bateria CR2032.  
3. Se chip BIOS removível: trocar.  
4. Verificar trilhas ao redor do Super I/O com multímetro (continuidade).

#### Ferramentas oficiais

Multímetro (continuidade de trilhas) / Bateria CR2032 nova

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain.  
2. Reset CMOS via jumper (mover para posição CLR por 10s, retornar).  
3. Trocar bateria CR2032.  
4. Se chip BIOS em socket DIP: trocar por chip gravado.  
5. Se persistir: falha no Super I/O ou PCH — reparo em nível de componente.

### Resultado esperado

#### Critério de validação

POST completa. CMOS mantém configurações após power off. Data/hora corretas.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

AMI BIOS Beep Code Reference

### Próximos passos

- Ficha da camada: [Camada 5: Chipset / Motherboard](../08-diagnostico-por-camada.md#camada-5--chipset--motherboard)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-10 — 11 Beeps Curtos

**Fabricante BIOS:** AMI (Legacy BIOS)  
**Fabricante / plataforma:** AMI Legacy — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro  
**Código:** `11 Beeps Curtos`

### Identificação

#### Interpretação oficial

Cache Memory Error — Falha na cache L1/L2/L3 da CPU

#### Componente afetado

CPU (Cache)

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

CPU Cache Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O teste de cache L1/L2/L3 falhou. Em CPUs modernas, a cache é integrada ao die — falha indica dano físico irreversível no processador. Pode ser causado por degradação térmica, eletromigração, ou defeito de fabricação.

#### Condições que geram o erro

1. Degradação térmica prolongada (operação acima de TjMax).  
2. Eletromigração por overclock extremo (VCore excessivo).  
3. Defeito de fabricação (stepping/revision com bug conhecido).  
4. Dano por ESD (descarga eletrostática).

#### Método de diagnóstico técnico

1. Reset CMOS para defaults.  
2. Não há reparo possível para cache integrada.  
3. Confirmar com teste cruzado: CPU defeituosa em outra placa = mesma falha.  
4. CPU boa na mesma placa = POST OK.

#### Ferramentas oficiais

N/A — Diagnóstico por exclusão. Condenação da CPU.

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Reset CMOS.  
2. Se persistir: a CPU tem dano interno irreversível.  
3. Teste cruzado:  

   a. CPU defeituosa em outra placa known-good → mesma falha = CPU condenada.  
   b. CPU known-good na placa suspeita → POST OK = confirma CPU defeituosa.  
4. Substituir CPU por modelo compatível.  

Nota: NÃO tentar overclock na CPU com falha de cache.

### Resultado esperado

#### Critério de validação

POST completa com CPU substituta. IntelBurnTest / Prime95 estável. Sem erros de cache reportados em HWiNFO64.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

AMI BIOS Beep Code Reference / Intel CPU Spec

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
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
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.3.0` |
