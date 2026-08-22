<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — AMI BIOS Legacy**

# Referência de Códigos de Erro POST: AMI BIOS Legacy

**Aplica-se a:** Equipamentos com BIOS `AMI (Legacy BIOS)` (Desktops e Servidores)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos sonoros (bipes) de erro POST da família AMI BIOS Legacy. Utilize o índice abaixo para navegar diretamente para o código de erro apresentado pelo equipamento.

---

## Neste artigo

- [1 Bipe Curto: Falha de Refresh da DRAM](#1-bipe-curto-falha-de-refresh-da-dram)
- [2 ou 3 Bipes Curtos: Falha na Memória Base (64KB)](#2-ou-3-bipes-curtos-falha-na-memória-base-64kb)
- [4 Bipes Curtos: Falha no Timer do Sistema](#4-bipes-curtos-falha-no-timer-do-sistema)
- [5 Bipes Curtos: Erro de Processador (CPU)](#5-bipes-curtos-erro-de-processador-cpu)
- [6 Bipes Curtos: Erro no Gate A20 (KBC)](#6-bipes-curtos-erro-no-gate-a20-kbc)
- [7 Bipes Curtos: Erro de Exceção da CPU](#7-bipes-curtos-erro-de-exceção-da-cpu)
- [8 Bipes Curtos: Falha na Memória de Vídeo (VRAM)](#8-bipes-curtos-falha-na-memória-de-vídeo-vram)
- [9 Bipes Curtos: Erro de Checksum da ROM (BIOS)](#9-bipes-curtos-erro-de-checksum-da-rom-bios)
- [10 Bipes Curtos: Falha no Registro de Shutdown do CMOS](#10-bipes-curtos-falha-no-registro-de-shutdown-do-cmos)
- [11 Bipes Curtos: Falha na Memória Cache (CPU)](#11-bipes-curtos-falha-na-memória-cache-cpu)
- [Consulte também](#consulte-também)

---

## 1 Bipe Curto: Falha de Refresh da DRAM

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *DRAM Refresh Failure* (Falha no circuito de refresh da DRAM) |
| **Componente afetado** | RAM (Módulos DIMM) |
| **Fase / Camada** | Memory Init (PEI) / Camada 3: Memória |
| **Criticidade** | Alta |

### Causas
O circuito de refresh da DRAM não responde. O timer de refresh (controladora de memória integrada à CPU ou northbridge) não consegue atualizar os capacitores das células DRAM dentro do intervalo especificado (tipicamente 64ms). Condições comuns incluem:
* Módulo DIMM com defeito físico (célula morta).
* Slot DIMM com oxidação ou pino torto.
* Tensão VDRAM fora de especificação (ex: DDR4: 1.2V ±5%).
* Incompatibilidade de timing SPD vs controladora.

### Diagnóstico
**Ferramentas:** MemTest86 (bootável), Multímetro digital (VDRAM), Lupa 10x.
1. Efetue um *power drain* completo (desligue, remova o cabo AC, segure o power por 30s).
2. Inspecione visualmente os slots DIMM com lupa buscando pinos tortos ou oxidação.
3. Meça a VDRAM no slot com multímetro (pinos de alimentação do DIMM).
4. Teste cada módulo individualmente em cada slot para isolar falha de slot vs. módulo.
5. Verifique o SPD com CPU-Z (ou equivalente) caso o POST seja parcial.

### Resolução
**Desktops:**
1. Execute o *power drain* (30s).
2. Remova todos os módulos DIMM.
3. Limpe os contatos dourados com borracha branca e isopropanol 99%. Limpe os slots com ar comprimido.
4. Insira 1 módulo no slot A2 (ou primário, conforme manual).
5. Ligue o sistema. Se o POST completar, adicione os demais módulos um a um.
6. Se falhar em todos os slots com RAM sabidamente boa, há falha na controladora de memória (CPU ou northbridge).

**Notebooks:** Remova a bateria e o cabo AC, acesse o compartimento SO-DIMM e siga o mesmo procedimento de limpeza e teste individual.

### Validação
* O POST deve completar com 1 bipe curto (padrão de sucesso AMI) ou silêncio seguido de vídeo.
* MemTest86 sem erros em 4 passes completos. VDRAM estável (ex: 1.2V para DDR4 / 1.1V para DDR5).

---

## 2 ou 3 Bipes Curtos: Falha na Memória Base (64KB)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Base 64K Memory Failure* (Falha nos primeiros 64KB de RAM) |
| **Componente afetado** | RAM (Base Memory) |
| **Fase / Camada** | Memory Init (PEI) / Camada 3: Memória |
| **Criticidade** | Alta |

### Causas
Os primeiros 64KB de memória não passam no teste de leitura/escrita. Região crítica que contém a IVT e a BDA em modo real.
* Primeiro módulo DIMM defeituoso.
* Falha no canal primário de memória (Channel A).
* Controladora de memória com defeito.
* BIOS não consegue treinar a memória no timing correto.

### Diagnóstico e Resolução
**Ferramentas:** Teste Cruzado com RAM validada, POST Card (opcional).
1. Execute o *power drain* (30s) e remova todos os módulos.
2. Insira 1 módulo sabidamente bom no slot primário (A1/A2).
3. Faça o Reset do CMOS (jumper CLR_CMOS por 10s com AC desconectado).
4. Ligue o sistema. Se o POST funcionar, o módulo original estava defeituoso.
5. Se falhar, teste em outro slot. Se falhar em todos com memória boa, o defeito está na controladora (CPU) ou trilha da placa-mãe.

### Validação
POST completa com sucesso. MemTest86 sem erros. Estabilidade do sistema sob carga.

---

## 4 Bipes Curtos: Falha no Timer do Sistema

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *System Timer Failure* (Falha no Timer do Sistema) |
| **Componente afetado** | Timer / Chipset (PCH/SIO) |
| **Fase / Camada** | Chipset Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Crítico |

### Causas
O timer programável (8254 PIT ou integrado ao PCH/SIO) não responde ou gera frequência incorreta.
* Cristal de 32.768 kHz defeituoso.
* Bateria CR2032 descarregada (< 2.8V).
* Chip PCH/Southbridge com defeito ou trilha interrompida.

### Diagnóstico e Resolução
**Ferramentas:** Osciloscópio (cristal 32kHz), Multímetro (bateria).
1. Meça a tensão da bateria CR2032. Se estiver abaixo de 3.0V, substitua-a.
2. Com um osciloscópio, verifique o sinal de 32.768 kHz nos pinos do cristal.
3. Execute o Reset do CMOS via jumper (10s).
4. Se o erro persistir: Em desktops, indica falha no PCH (requer reparo BGA ou troca da placa). Em servidores, substitua a *system board*.

### Validação
O RTC mantém data/hora após o desligamento. O POST completa sem erros. O cristal oscila a 32.768 kHz ±20ppm.

---

## 5 Bipes Curtos: Erro de Processador (CPU)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *CPU Error* (Processador não responde ou falha de instrução) |
| **Componente afetado** | CPU (Processador) |
| **Fase / Camada** | CPU Init (SEC/PEI) / Camada 2: CPU |
| **Criticidade** | Crítico |

### Causas
O processador não executa instruções ou não é detectado.
* Pinos LGA tortos ou contaminados.
* Alimentação EPS 12V (4+4 ou 8 pin) desconectada/defeituosa.
* CPU incompatível com a versão do BIOS ou pasta térmica vazada no socket.
* VRM da placa-mãe com defeito (VCore ausente).

### Diagnóstico e Resolução
**Ferramentas:** Multímetro (VCore, EPS), Lupa 10x.
1. Remova o cooler (gire para soltar) e limpe a pasta com isopropanol 99%.
2. Inspecione o socket LGA com a lupa. Se houver pinos tortos, tente alinhar com agulha (alto risco).
3. Verifique se o conector EPS 12V está firme e meça a tensão (deve ser 12V ±5%).
4. Se a CPU for nova, confirme a compatibilidade do BIOS e atualize via Flashback, se possível.
5. Reinstale a CPU, aplique nova pasta e teste. Para dual-CPU em servidores, teste isoladamente.

### Validação
POST completa. CPU reconhecida corretamente no BIOS (modelo e *stepping*). VCore estável e *stress test* (Prime95/AIDA64) estável por 30 minutos.

---

## 6 Bipes Curtos: Erro no Gate A20 (KBC)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Gate A20 Error* (Falha no controlador de teclado - KBC) |
| **Componente afetado** | KBC / Super I/O |
| **Fase / Camada** | KBC Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Médio |

### Causas
O Gate A20 não alterna corretamente (gerenciado pelo Super I/O ou PCH em sistemas modernos).
* Chip Super I/O com defeito/oxidação.
* Teclado PS/2 em curto.
* Firmware corrompido ou trilha interrompida.

### Diagnóstico e Resolução
1. Desconecte todos os teclados (PS/2 e USB).
2. Limpe os conectores I/O traseiros com isopropanol e ar comprimido.
3. Tente ligar o equipamento sem teclado conectado.
4. Se o POST passar: o teclado original ou a porta PS/2 estão em curto.
5. Se persistir: Falha no Super I/O. Requer reparo em nível de componente ou troca da placa.

### Validação
POST completa. Teclado funcional dentro do BIOS Setup. 

---

## 7 Bipes Curtos: Erro de Exceção da CPU

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Processor Exception Interrupt Error* (Erro de exceção da CPU) |
| **Componente afetado** | CPU (Processador) |
| **Fase / Camada** | CPU Init / Camada 2: CPU |
| **Criticidade** | Crítico |

### Causas
A CPU gerou uma exceção inesperada durante o POST.
* Overclock instável.
* VCore insuficiente.
* Dano físico no *die* do processador (degradação).
* Instabilidade na alimentação VRM.

### Diagnóstico e Resolução
1. Faça o Reset do CMOS para restaurar os padrões de fábrica (remove *overclock*).
2. Se persistir nos padrões de fábrica, inspecione os capacitores do VRM em busca de abaulamento (sinal de defeito).
3. Meça o VCore nos pontos de teste.
4. Efetue um teste cruzado com uma CPU sabidamente boa. Se a placa falhar com uma CPU boa, o defeito está no VRM da placa.

### Validação
POST completa em *defaults*. CPU estável em *stress test* (Prime95 Small FFTs) por 30 minutos. Sem erros WHEA.

---

## 8 Bipes Curtos: Falha na Memória de Vídeo (VRAM)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Display Memory R/W Error* (Falha na memória de vídeo) |
| **Componente afetado** | GPU / VRAM |
| **Fase / Camada** | Video Init / Camada 4: Vídeo |
| **Criticidade** | Alta |

### Causas
Falha na leitura/escrita da memória de vídeo.
* VRAM da GPU dedicada com defeito.
* GPU mal encaixada ou slot PCIe oxidado.
* Em iGPU: RAM do sistema com defeito (memória compartilhada).

### Diagnóstico e Resolução
1. Remova a GPU dedicada e limpe os contatos com borracha branca e isopropanol. Limpe o slot PCIe com ar comprimido.
2. Reinserir com pressão firme e verifique a alimentação PCIe (6+2 pinos).
3. Se persistir, teste com outra GPU. Se a placa substituta funcionar, a GPU original requer reparo BGA ou substituição.
4. **Nota para iGPU:** Se não houver GPU dedicada, o problema reflete na memória RAM do sistema. Siga o diagnóstico de RAM.

### Validação
Vídeo funcional no POST. Sem artefatos visuais. GPU-Z reconhecendo a VRAM corretamente e FurMark estável por 15 min.

---

## 9 Bipes Curtos: Erro de Checksum da ROM (BIOS)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *ROM Checksum Error* (BIOS Corrompida) |
| **Componente afetado** | BIOS / EEPROM |
| **Fase / Camada** | BIOS Verify / Camada 6: Firmware |
| **Criticidade** | Crítico |

### Causas
O firmware armazenado na flash EEPROM/SPI está corrompido (falha de energia durante update, degradação do chip, bateria CR2032 morta).

### Diagnóstico e Resolução
1. Substitua a bateria CR2032.
2. Tente métodos de *BIOS Recovery* nativos:
   * **ASUS:** Pendrive FAT32 na porta USB Flashback, segure o botão Flashback por 3s.
   * **GIGABYTE/MSI:** Utilize o botão Q-Flash Plus / Flash BIOS com pendrive formatado.
3. Se não houver recuperação nativa: Remova o chip (ou use alicate SOIC-8) e regrave o firmware usando uma programadora EEPROM (ex: CH341A) com o arquivo oficial.

### Validação
Acesso restaurado ao BIOS Setup. Versão correta de firmware exibida e data/hora mantidas após reboot.

---

## 10 Bipes Curtos: Falha no Registro de Shutdown do CMOS

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *CMOS Shutdown Register R/W Error* |
| **Componente afetado** | CMOS / Super I/O |
| **Fase / Camada** | CMOS Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Médio |

### Causas
Falha de leitura/escrita no registro de shutdown do CMOS (usado para controlar sequências de reinício). Pode ser defeito no chip CMOS, Super I/O ou bateria descarregada.

### Diagnóstico e Resolução
1. Faça o *power drain* completo.
2. Execute o Reset do CMOS via jumper CLR_CMOS (10s).
3. Substitua a bateria CR2032.
4. Se a BIOS for do tipo soquete DIP, substitua por um chip regravado.
5. Se persistir, o problema está no Super I/O ou PCH, exigindo reparo em nível de componente.

### Validação
O CMOS deve reter as configurações e a data/hora após a remoção da alimentação primária.

---

## 11 Bipes Curtos: Falha na Memória Cache (CPU)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Cache Memory Error* (Falha na cache L1/L2/L3 da CPU) |
| **Componente afetado** | CPU (Cache) |
| **Fase / Camada** | CPU Cache Init / Camada 2: CPU |
| **Criticidade** | Crítico |

### Causas
Falha estrutural irreversível no processador. A cache integrada sofreu degradação térmica, dano por *overclock* extremo (eletromigração) ou descarga eletrostática (ESD).

### Diagnóstico e Resolução
**Não há reparo possível para cache integrada danificada.**
1. Execute o Reset do CMOS para restaurar as frequências e tensões padrão.
2. Se persistir, confirme o diagnóstico cruzando as peças:
   * Teste a CPU em uma placa-mãe boa (O erro acompanhará a CPU).
3. Substitua o processador por um modelo compatível.
4. *Aviso:* Não tente realizar *overclock* em uma CPU apresentando falhas de cache.

### Validação
POST completa com a CPU substituta. Testes de estresse (IntelBurnTest/Prime95) estáveis, sem erros relatados no HWiNFO64.

---

## Consulte também

Para aprofundamento técnico ou informações sobre o fluxo de atendimento, consulte os documentos relacionados:

* **[Índice de códigos POST](00-indice-codigos.md):** Catálogo completo.
* **[Ambiguidade de códigos](../11-ambiguidades.md):** Verifique divergências de sinais entre fabricantes.
* **[Diagnóstico por camada](../08-diagnostico-por-camada.md):** Metodologia de testes nos subsistemas de hardware.
* **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.
* **[Validação final por componente](../13-validacao-final.md):** Testes para fechamento de atendimento.

---

| Metadados do Artigo | |
| :--- | :--- |
| **Fonte oficial** | AMI BIOS Beep Code Reference / Technical Documentation |
| **Fonte primária interna** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da doc.** | `doc-2.0.0` |
