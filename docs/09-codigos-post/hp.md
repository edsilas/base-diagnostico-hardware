<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — HP (LED piscante)**

# Códigos POST — HP (LED piscante)

> Fichas completas dos códigos de POST da família HP (LED piscante), com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `Proprietário HP`

## Neste documento

- [POST-38 — 2 Longos + 2 Curtos (2.2)](#post-38--2-longos--2-curtos-22)
- [POST-39 — 3 Longos + 2 Curtos (3.2)](#post-39--3-longos--2-curtos-32)
- [POST-40 — 3 Longos + 3 Curtos (3.3)](#post-40--3-longos--3-curtos-33)
- [POST-41 — 3 Longos + 4 Curtos (3.4)](#post-41--3-longos--4-curtos-34)
- [POST-42 — 4 Longos + 2 Curtos (4.2)](#post-42--4-longos--2-curtos-42)
- [POST-43 — 5 Longos (5.0)](#post-43--5-longos-50)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `Proprietário HP`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 6 código(s) da família `Proprietário HP` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-38 — 2 Longos + 2 Curtos (2.2)

**Fabricante BIOS:** Proprietário HP  
**Fabricante / plataforma:** HP — ProBook / EliteBook / ProDesk / EliteDesk  
**Tipo de sinal:** LED Piscante (Caps/Num Lock)  
**Código:** `2 Longos + 2 Curtos (2.2)`

### Identificação

#### Interpretação oficial

BIOS Corruption — Firmware BIOS corrompido

#### Componente afetado

BIOS / SPI Flash

#### Camada de diagnóstico

Camada 6: Firmware

#### Fase POST

BIOS Verify

### Diagnóstico

#### Causa raiz (documentação oficial)

O HP detectou que o firmware BIOS está corrompido. HP usa padrão de LEDs Caps Lock e Num Lock para diagnóstico (Longos.Curtos).

#### Condições que geram o erro

1. BIOS corrompida por update falho.  
2. Degradação da SPI Flash.  
3. Ataque de firmware.  
4. Falha de energia durante atualização.

#### Método de diagnóstico técnico

1. Tentar HP BIOS Recovery: Win + B ao ligar.  
2. Pendrive com HP Diagnostics.  
3. Se recovery falha: regravação externa.

#### Ferramentas oficiais

Combinação de teclas Win+B / Pendrive FAT32 / HP BIOS Recovery

### Execução da correção

#### Procedimento de correção (passo a passo)

1. HP BIOS Recovery (método primário):  

   a. Desligar completamente.  
   b. Segurar Win + B.  
   c. Pressionar e soltar Power mantendo Win+B.  
   d. Aguardar ~3s, soltar teclas.  
   e. Tela pode piscar ou ficar preta por 2-3 min.  
   f. Processo de recovery automático inicia.  
2. Se não funcionar:  

   a. Baixar BIOS do support.hp.com.  
   b. Extrair e copiar para pendrive FAT32.  
   c. Inserir pendrive e repetir Win+B.  
3. Se tudo falhar: regravação via CH341A.

### Resultado esperado

#### Critério de validação

POST completa. BIOS Setup (F10) acessível. Versão de BIOS correta.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

HP BIOS Recovery Guide / HP LED Flash Codes

### Próximos passos

- Ficha da camada: [Camada 6: Firmware](../08-diagnostico-por-camada.md#camada-6--firmware-biosuefi)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-39 — 3 Longos + 2 Curtos (3.2)

**Fabricante BIOS:** Proprietário HP  
**Fabricante / plataforma:** HP — ProBook / EliteBook / ProDesk / EliteDesk  
**Tipo de sinal:** LED Piscante (Caps/Num Lock)  
**Código:** `3 Longos + 2 Curtos (3.2)`

### Identificação

#### Interpretação oficial

Memory Initialization Failure — Falha na inicialização da memória

#### Componente afetado

RAM

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Init

### Diagnóstico

#### Causa raiz (documentação oficial)

A RAM não pode ser inicializada. Em notebooks HP, frequentemente causado por oxidação no slot SO-DIMM.

#### Condições que geram o erro

1. Módulo SO-DIMM/DIMM mal encaixado.  
2. Oxidação nos contatos (comum em ambientes úmidos).  
3. Módulo incompatível.  
4. Slot com defeito.

#### Método de diagnóstico técnico

1. Reseat RAM.  
2. Limpar contatos com borracha branca.  
3. Testar slot individual.  
4. Se notebook: verificar oxidação no slot SO-DIMM.

#### Ferramentas oficiais

Borracha branca / Isopropanol / RAM compatível HP

### Execução da correção

#### Procedimento de correção (passo a passo)

NOTEBOOK HP:  
1. Remover bateria e AC.  
2. Remover tampa inferior (parafusos + clipes).  
3. Soltar módulos SO-DIMM (puxar travas laterais).  
4. Limpar contatos dourados com borracha branca (movimentos em uma direção).  
5. Limpar slot com escova antiestática e isopropanol.  
6. Inserir módulo a 30°, pressionar até travas clicarem.  
7. Remontar e testar.  

DESKTOP HP:  
1. Remover painel lateral.  
2. Remover todos os DIMM, limpar, reinserir.  
3. Testar slot individual.

### Resultado esperado

#### Critério de validação

LEDs param de piscar. POST completa. Memória reconhecida. HP Diagnostics Memory Test OK.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

HP LED Flash Codes / HP Service Manual

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-40 — 3 Longos + 3 Curtos (3.3)

**Fabricante BIOS:** Proprietário HP  
**Fabricante / plataforma:** HP — ProBook / EliteBook / ProDesk / EliteDesk  
**Tipo de sinal:** LED Piscante (Caps/Num Lock)  
**Código:** `3 Longos + 3 Curtos (3.3)`

### Identificação

#### Interpretação oficial

Graphics Controller Error — Erro no controlador gráfico

#### Componente afetado

GPU / iGPU

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

Video Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O controlador gráfico (dedicado ou integrado) falhou na inicialização.

#### Condições que geram o erro

1. GPU dedicada com defeito (BGA com solda fria).  
2. Se UMA (APU/iGPU): pode indicar falha na CPU ou RAM (memória compartilhada).  
3. Driver de vídeo no firmware com conflito.

#### Método de diagnóstico técnico

1. Se GPU dedicada: reflow é diagnóstico arriscado.  
2. Se iGPU/UMA: problema pode ser CPU ou RAM.  
3. Testar saída de vídeo externa.  
4. Reset CMOS.

#### Ferramentas oficiais

Soprador térmico (diagnóstico arriscado para BGA) / Monitor externo

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Conectar monitor externo:  

   — Se externo funciona: tela ou cabo com defeito.  
   — Se externo sem imagem: GPU/placa com defeito.  
2. Se GPU dedicada (notebook): solda BGA fraturada — reparo profissional ou troca da placa.  
3. Se iGPU:  

   a. Testar RAM (iGPU usa memória compartilhada).  
   b. Reset CMOS.  
   c. Se persistir: falha na CPU (GPU integrada no die).  
4. Desktop com GPU dedicada: trocar GPU.

### Resultado esperado

#### Critério de validação

LEDs param. Vídeo funcional. HP Diagnostics Video Test OK.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

HP LED Flash Codes

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-41 — 3 Longos + 4 Curtos (3.4)

**Fabricante BIOS:** Proprietário HP  
**Fabricante / plataforma:** HP — ProBook / EliteBook / ProDesk / EliteDesk  
**Tipo de sinal:** LED Piscante (Caps/Num Lock)  
**Código:** `3 Longos + 4 Curtos (3.4)`

### Identificação

#### Interpretação oficial

Power Supply / System Board Voltage — Falha de alimentação

#### Componente afetado

PSU / DC-DC Converters

#### Camada de diagnóstico

Camada 1: Energia

#### Fase POST

Power Sequencing

### Diagnóstico

#### Causa raiz (documentação oficial)

Falha interna de alimentação. Os conversores DC-DC da placa não estão entregando tensões corretas.

#### Condições que geram o erro

1. Conversores DC-DC (buck/boost) com defeito.  
2. Capacitores em curto.  
3. Fonte externa (AC adapter) com defeito (notebook).  
4. Jack DC com mau contato (notebook).

#### Método de diagnóstico técnico

1. Testar com outro AC adapter HP compatível.  
2. Medir tensões nos pontos de teste.  
3. Verificar jack DC (notebook).  
4. Requer esquema elétrico para diagnóstico avançado.

#### Ferramentas oficiais

Esquema elétrico da placa / Multímetro / AC Adapter known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

NOTEBOOK:  
1. Testar com outro AC adapter HP compatível (mesma voltagem/potência).  
2. Verificar jack DC: movimentar conector e observar LED de carga.  
3. Se LED de carga não acende: jack ou circuito de carga com defeito.  
4. Requer reparo em nível de componente.  

DESKTOP:  
1. Testar PSU BIST (se disponível).  
2. Medir tensões com multímetro.  
3. Se tensões fora de spec: trocar fonte.  
4. Se tensões OK: placa-mãe com DC-DC converter defeituoso.

### Resultado esperado

#### Critério de validação

LEDs param. Tensões corretas. Sistema estável. HP Diagnostics sem erros.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

HP LED Flash Codes / HP Power Supply Specs

### Próximos passos

- Ficha da camada: [Camada 1: Energia](../08-diagnostico-por-camada.md#camada-1--energia-psuvrm)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-42 — 4 Longos + 2 Curtos (4.2)

**Fabricante BIOS:** Proprietário HP  
**Fabricante / plataforma:** HP — ProBook / EliteBook / ProDesk / EliteDesk  
**Tipo de sinal:** LED Piscante (Caps/Num Lock)  
**Código:** `4 Longos + 2 Curtos (4.2)`

### Identificação

#### Interpretação oficial

Thermal Shutdown — Desligamento por superaquecimento

#### Componente afetado

CPU / Fan / Sistema térmico

#### Camada de diagnóstico

Camada 2: CPU / Camada 1: Energia

#### Fase POST

Thermal Monitor

### Diagnóstico

#### Causa raiz (documentação oficial)

O sistema desligou ou falhou no POST por temperatura excessiva da CPU.

#### Condições que geram o erro

1. Fan da CPU parado (poeira, motor queimado).  
2. Pasta térmica seca.  
3. Heatsink desconectado ou mal assentado.  
4. Fluxo de ar bloqueado (notebook: ventilação obstruída).

#### Método de diagnóstico técnico

1. Verificar se fan gira ao ligar.  
2. Limpar poeira com ar comprimido.  
3. Verificar sinal tacômetro (header CPU_FAN).  
4. Trocar pasta térmica.

#### Ferramentas oficiais

Fonte de bancada (testar fan isolado) / Ar comprimido / Pasta térmica

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Verificar se fan da CPU gira ao ligar.  
2. Se não gira:  

   a. Verificar conexão no header CPU_FAN.  
   b. Testar fan com fonte de bancada (12V para desktop, 5V para notebook).  
   c. Se fan não gira isolado: substituir fan.  
3. Se fan gira:  

   a. Limpar heatsink com ar comprimido.  
   b. Remover heatsink, limpar pasta antiga.  
   c. Reaplicar pasta térmica.  
   d. Reinstalar heatsink.  
4. NOTEBOOK: desmontar, limpar todo o sistema de refrigeração, trocar pasta.

### Resultado esperado

#### Critério de validação

LEDs param. POST completa. Temperatura idle < 50°C. Fan silencioso e funcional.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

HP LED Flash Codes / HP Thermal Design Guide

### Próximos passos

- Camada declarada: `Camada 2: CPU / Camada 1: Energia` — valor composto ou variável; ver [Taxonomia de camadas](../03-taxonomia-camadas.md)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-43 — 5 Longos (5.0)

**Fabricante BIOS:** Proprietário HP  
**Fabricante / plataforma:** HP — ProBook / EliteBook / ProDesk / EliteDesk  
**Tipo de sinal:** LED Piscante (Caps/Num Lock)  
**Código:** `5 Longos (5.0)`

### Identificação

#### Interpretação oficial

General System Board Failure — Falha geral da placa-mãe

#### Componente afetado

Placa-mãe / KBC / SIO

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

Board Init

### Diagnóstico

#### Causa raiz (documentação oficial)

Falha genérica da placa-mãe. Geralmente indica falha no Embedded Controller (EC), KBC, ou Super I/O — componentes fundamentais que controlam a sequência de power-on.

#### Condições que geram o erro

1. Embedded Controller (EC) com firmware corrompido.  
2. Super I/O chip com defeito.  
3. KBC não responde.  
4. Falha estrutural na placa (trilha, via, etc.).

#### Método de diagnóstico técnico

1. Reset CMOS.  
2. Desconectar bateria CMOS por 30 min.  
3. Se notebook: desconectar bateria interna e manter power pressionado 60s.  
4. Se persistir: placa condenada.

#### Ferramentas oficiais

N/A — Condenação da placa-mãe na maioria dos casos

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Reset CMOS completo:  

   a. Remover AC/bateria.  
   b. Remover bateria CMOS.  
   c. Segurar power 60 segundos.  
   d. Aguardar 30 minutos.  
   e. Reinstalar bateria CMOS.  
   f. Conectar AC e ligar.  
2. Se persistir: placa-mãe condenada.  
3. Em ambiente corporativo: acionar garantia HP ou substituir placa-mãe.

### Resultado esperado

#### Critério de validação

Se resolvido: POST completa. Se condenação: N/A — substituir placa.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

HP LED Flash Codes

### Próximos passos

- Ficha da camada: [Camada 5: Chipset / Motherboard](../08-diagnostico-por-camada.md#camada-5--chipset--motherboard)
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
