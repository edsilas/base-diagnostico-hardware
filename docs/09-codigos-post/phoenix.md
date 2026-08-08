<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Phoenix BIOS**

# Códigos POST — Phoenix BIOS

> Fichas completas dos códigos de POST da família Phoenix BIOS, com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `Phoenix BIOS`

## Neste documento

- [POST-26 — 1-1-1-3](#post-26--1-1-1-3)
- [POST-27 — 1-2-2-3](#post-27--1-2-2-3)
- [POST-28 — 1-3-1-1](#post-28--1-3-1-1)
- [POST-29 — 1-3-4-1](#post-29--1-3-4-1)
- [POST-30 — 1-4-2-1](#post-30--1-4-2-1)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `Phoenix BIOS`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 5 código(s) da família `Phoenix BIOS` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-26 — 1-1-1-3

**Fabricante BIOS:** Phoenix BIOS  
**Fabricante / plataforma:** Phoenix — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro (Sequência)  
**Código:** `1-1-1-3`

### Identificação

#### Interpretação oficial

Verify Real Mode — CPU/MB falha ao entrar em modo real x86

#### Componente afetado

CPU / Placa-mãe

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

SEC Phase (Real Mode Init)

### Diagnóstico

#### Causa raiz (documentação oficial)

A CPU não consegue entrar em modo real (Real Mode), que é o primeiro modo de operação x86 após power-on. Indica falha fundamental na CPU ou na placa-mãe.

#### Condições que geram o erro

1. CPU morta (não executa nenhuma instrução).  
2. Placa-mãe com falha no barramento de CPU.  
3. VRM sem saída.  
4. Socket com dano massivo nos pinos.

#### Método de diagnóstico técnico

1. Verificar se há alguma atividade (fans, LEDs).  
2. Se fans giram mas nenhum outro sinal: CPU provavelmente morta.  
3. Teste cruzado de CPU (se disponível).  
4. Medir VCore.

#### Ferramentas oficiais

Multímetro (VCore) / CPU known-good / Condenação

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Medir VCore nos pontos de teste da placa.  
2. Se VCore = 0V: VRM defeituoso ou CPU em curto → testar CPU em outra placa.  
3. Se VCore presente mas código persiste: CPU morta → substituir.  
4. Se CPU known-good também falha: placa-mãe condenada.

### Resultado esperado

#### Critério de validação

POST completa. CPU em modo protegido. Sistema inicia normalmente.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Phoenix BIOS Technical Reference Manual

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-27 — 1-2-2-3

**Fabricante BIOS:** Phoenix BIOS  
**Fabricante / plataforma:** Phoenix — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro (Sequência)  
**Código:** `1-2-2-3`

### Identificação

#### Interpretação oficial

BIOS ROM Checksum — Falha de integridade do firmware

#### Componente afetado

BIOS / EEPROM

#### Camada de diagnóstico

Camada 6: Firmware

#### Fase POST

BIOS Verify

### Diagnóstico

#### Causa raiz (documentação oficial)

O checksum da ROM do BIOS não confere. Firmware corrompido na SPI Flash/EEPROM.

#### Condições que geram o erro

1. Flash corrompido por falha de energia durante update.  
2. Degradação da SPI Flash.  
3. Bateria morta causando perda de dados.

#### Método de diagnóstico técnico

1. Trocar bateria CR2032.  
2. Tentar BIOS Recovery (varia por fabricante).  
3. Regravação via programadora CH341A se necessário.

#### Ferramentas oficiais

Programadora EPROM (CH341A) / Bateria CR2032 / Pendrive FAT32

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Trocar bateria CR2032.  
2. Tentar BIOS Recovery nativo do fabricante.  
3. Se não há Recovery: regravar via CH341A (identificar chip, baixar firmware correto, gravar).  
4. Reinstalar e testar POST.

### Resultado esperado

#### Critério de validação

POST completa. BIOS Setup acessível. Firmware correto. Data/hora mantidas.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Phoenix BIOS Technical Reference Manual

### Próximos passos

- Ficha da camada: [Camada 6: Firmware](../08-diagnostico-por-camada.md#camada-6--firmware-biosuefi)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-28 — 1-3-1-1

**Fabricante BIOS:** Phoenix BIOS  
**Fabricante / plataforma:** Phoenix — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro (Sequência)  
**Código:** `1-3-1-1`

### Identificação

#### Interpretação oficial

DRAM Refresh Test — Falha no teste de refresh da DRAM

#### Componente afetado

RAM / Slots DIMM

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Init

### Diagnóstico

#### Causa raiz (documentação oficial)

Teste de refresh da DRAM falhou. Similar ao código AMI Legacy 1 beep curto.

#### Condições que geram o erro

1. Módulo DIMM com defeito.  
2. Slot DIMM com pinos tortos (dentro do conector).  
3. Controladora de memória com falha.

#### Método de diagnóstico técnico

1. Reseat RAM com atenção a pressão uniforme.  
2. Inspecionar slots DIMM internamente com lupa (pinos tortos dentro do conector plástico).  
3. Testar módulo known-good.  
4. Testar cada slot individualmente.

#### Ferramentas oficiais

Lupa 10x (inspecionar interior do slot DIMM) / RAM known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Remover todos os módulos.  
2. Inspecionar interior de cada slot DIMM com lupa e lanterna (pinos tortos, oxidação).  
3. Limpar contatos dos módulos.  
4. Inserir 1 módulo no slot primário.  
5. Testar cada slot.  
6. Se falhar em todos os slots: controladora de memória (CPU).

### Resultado esperado

#### Critério de validação

POST completa. RAM reconhecida. MemTest86 sem erros.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Phoenix BIOS Technical Reference Manual

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-29 — 1-3-4-1

**Fabricante BIOS:** Phoenix BIOS  
**Fabricante / plataforma:** Phoenix — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro (Sequência)  
**Código:** `1-3-4-1`

### Identificação

#### Interpretação oficial

RAM Failure on Address Line — Falha em linha de endereço da RAM

#### Componente afetado

RAM / Trilhas da Placa-mãe

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Address Test

### Diagnóstico

#### Causa raiz (documentação oficial)

Uma linha de endereço específica da RAM falhou no teste. Pode ser o módulo DIMM ou uma trilha rompida na placa-mãe entre a CPU e o slot DIMM.

#### Condições que geram o erro

1. Módulo DIMM com chip de memória defeituoso.  
2. Trilha rompida na placa-mãe (Address Bus).  
3. Solda fria no pino do slot DIMM.  
4. Controladora de memória com dano parcial.

#### Método de diagnóstico técnico

1. Trocar módulo por known-good.  
2. Se novo módulo falha no mesmo slot: teste de continuidade na trilha (requer esquema elétrico).  
3. Testar módulo original em outro slot/placa.

#### Ferramentas oficiais

Teste de Continuidade (multímetro) / Esquema elétrico da placa

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Trocar módulo DIMM por known-good.  
2. Se OK com novo módulo: módulo original defeituoso.  
3. Se falha persiste:  

   a. Testar outro slot.  
   b. Se falha muda de slot: slot com defeito (trilha rompida ou solda fria no conector).  
   c. Se falha em todos os slots: controladora de memória (CPU).

### Resultado esperado

#### Critério de validação

POST completa. MemTest86 sem erros de endereçamento. RAM com capacidade correta.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Phoenix BIOS Technical Reference Manual

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-30 — 1-4-2-1

**Fabricante BIOS:** Phoenix BIOS  
**Fabricante / plataforma:** Phoenix — Desktop / Servidor  
**Tipo de sinal:** Beep Sonoro (Sequência)  
**Código:** `1-4-2-1`

### Identificação

#### Interpretação oficial

CMOS Clock Test — Falha no clock RTC do CMOS

#### Componente afetado

CMOS / RTC / Cristal 32kHz

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

RTC Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O teste do Real Time Clock (RTC) falhou. O cristal de 32.768 kHz que alimenta o RTC está defeituoso ou a bateria CR2032 não fornece tensão suficiente.

#### Condições que geram o erro

1. Cristal de 32.768 kHz defeituoso.  
2. Bateria CR2032 abaixo de 2.8V.  
3. Circuito RTC do PCH/Southbridge com defeito.  
4. Solda fria no cristal.

#### Método de diagnóstico técnico

1. Medir bateria CR2032 (≥ 2.9V).  
2. Trocar bateria.  
3. Se persistir: verificar cristal com osciloscópio.  
4. Se cristal OK: falha no PCH/RTC.

#### Ferramentas oficiais

Osciloscópio (cristal 32.768 kHz) / Multímetro (bateria) / Cristal de reposição

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Trocar bateria CR2032 por nova (≥ 3.0V).  
2. Reset CMOS.  
3. Configurar data/hora no BIOS.  
4. Desligar, aguardar 10 min, ligar: data/hora devem estar corretas.  
5. Se data/hora perdem: cristal de 32.768 kHz defeituoso.  
6. Se tiver habilidade SMD: trocar cristal (componente ~R$0,50).  
7. Se não: placa condenada ou conviver com reset de data a cada boot.

### Resultado esperado

#### Critério de validação

RTC mantém data/hora após desligamento. Cristal oscila a 32.768 kHz (±20ppm).

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

Phoenix BIOS Technical Reference Manual

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
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.3.0` |
