<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Genérico — Debug LED**

# Códigos POST — Genérico — Debug LED

> Fichas completas dos códigos de POST da família Genérico — Debug LED, com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `Genérico (Múltiplos)`

## Neste documento

- [POST-51 — LED CPU (Vermelho)](#post-51--led-cpu-vermelho)
- [POST-52 — LED DRAM (Amarelo)](#post-52--led-dram-amarelo)
- [POST-53 — LED VGA (Branco)](#post-53--led-vga-branco)
- [POST-54 — LED BOOT (Verde)](#post-54--led-boot-verde)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `Genérico (Múltiplos)`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 4 código(s) da família `Genérico (Múltiplos)` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-51 — LED CPU (Vermelho)

**Fabricante BIOS:** Genérico (Múltiplos)  
**Fabricante / plataforma:** GERAL — Placas com Debug LED (ASUS, GIGABYTE, MSI, ASRock)  
**Tipo de sinal:** LED de Diagnóstico (cor fixa)  
**Código:** `LED CPU (Vermelho)`

### Identificação

#### Interpretação oficial

CPU Not Detected / Fail — CPU não detectada ou com falha

#### Componente afetado

CPU / VRM / EPS

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

SEC/PEI (CPU Init)

### Diagnóstico

#### Causa raiz (documentação oficial)

O LED de diagnóstico da placa-mãe indica falha na inicialização da CPU. Presente na maioria das placas modernas (ASUS, GIGABYTE, MSI, ASRock) com 4 LEDs: CPU, DRAM, VGA, BOOT.

#### Condições que geram o erro

1. Cabo EPS 8-pin (CPU power) desconectado.  
2. Pinos do socket LGA tortos.  
3. BIOS não suporta a CPU instalada (requer atualização).  
4. CPU com defeito.  
5. VRM com defeito.

#### Método de diagnóstico técnico

1. Verificar conector EPS 8-pin.  
2. Medir 12V no conector EPS.  
3. Inspecionar socket com lupa.  
4. Verificar compatibilidade CPU-BIOS.  
5. Se CPU nova: BIOS Flashback.

#### Ferramentas oficiais

Multímetro (EPS 12V) / Lupa 10x / BIOS Flashback

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Verificar cabo EPS 8-pin (4+4) firmemente conectado na placa E na fonte.  
2. Medir 12V no conector com multímetro.  
3. Se 12V OK:  

   a. Verificar compatibilidade CPU-BIOS no site do fabricante.  
   b. Se CPU requer BIOS update: usar BIOS Flashback/Q-Flash Plus.  
   c. Inspecionar socket com lupa (pinos tortos = realinhar ou condenar placa).  
4. Se 12V ausente: fonte ou cabo com defeito.  
5. Se tudo OK: teste cruzado CPU.

### Resultado esperado

#### Critério de validação

LED CPU apaga. Próximo LED (DRAM) acende brevemente e passa. POST completa.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Manual da placa-mãe do fabricante

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-52 — LED DRAM (Amarelo)

**Fabricante BIOS:** Genérico (Múltiplos)  
**Fabricante / plataforma:** GERAL — Placas com Debug LED  
**Tipo de sinal:** LED de Diagnóstico (cor fixa)  
**Código:** `LED DRAM (Amarelo)`

### Identificação

#### Interpretação oficial

Memory Training Fail — Falha no treinamento de memória

#### Componente afetado

RAM / Controladora

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

PEI (Memory Training)

### Diagnóstico

#### Causa raiz (documentação oficial)

O LED DRAM indica falha ou demora no treinamento de memória. IMPORTANTE: DDR5 pode demorar até 3 minutos no primeiro boot ou após mudança de configuração — aguardar antes de diagnosticar.

#### Condições que geram o erro

1. DDR5: treinamento normal pode demorar até 3 min (NÃO é erro).  
2. Módulo mal encaixado.  
3. Módulo em slot errado.  
4. Módulo incompatível.  
5. Reset CMOS necessário após mudança de RAM.

#### Método de diagnóstico técnico

1. PRIMEIRO: aguardar 3 minutos completos (especialmente DDR5).  
2. Se após 3 min LED persiste: reseat RAM.  
3. Reset CMOS.  
4. Verificar QVL.  
5. Testar slot individual.

#### Ferramentas oficiais

Cronômetro (aguardar 3 min) / QVL do fabricante / RAM known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Ao instalar RAM nova (especialmente DDR5): AGUARDAR ATÉ 3 MINUTOS. LED DRAM aceso durante treinamento é NORMAL.  
2. Se após 3 min LED persiste:  

   a. Desligar, remover AC, power drain.  
   b. Remover todos os módulos.  
   c. Reset CMOS via jumper.  
   d. Inserir 1 módulo no slot A2 (ou conforme manual).  
   e. Ligar e aguardar 3 min novamente.  
3. Se persistir: testar outro módulo.  
4. Se nenhum módulo funciona: controladora de memória (CPU) ou placa.

### Resultado esperado

#### Critério de validação

LED DRAM apaga. LED avança para VGA e depois BOOT. POST completa. RAM reconhecida.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Manual da placa-mãe / DDR5 JEDEC Specification

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-53 — LED VGA (Branco)

**Fabricante BIOS:** Genérico (Múltiplos)  
**Fabricante / plataforma:** GERAL — Placas com Debug LED  
**Tipo de sinal:** LED de Diagnóstico (cor fixa)  
**Código:** `LED VGA (Branco)`

### Identificação

#### Interpretação oficial

VGA Not Detected — GPU não detectada

#### Componente afetado

GPU / Slot PCIe

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

DXE (Video Init)

### Diagnóstico

#### Causa raiz (documentação oficial)

O LED VGA indica que nenhuma GPU foi detectada ou inicializada. Em algumas placas, o LED pode acender se o monitor não estiver conectado ou ligado (handshake HDMI/DP requerido).

#### Condições que geram o erro

1. GPU mal encaixada no slot PCIe.  
2. Cabo de alimentação PCIe desconectado.  
3. Monitor desligado (algumas placas requerem handshake ativo).  
4. Cabo de vídeo defeituoso.  
5. GPU com defeito.

#### Método de diagnóstico técnico

1. Reseat GPU.  
2. Verificar cabo PCIe power.  
3. Verificar se monitor está ligado e no input correto.  
4. Testar outro cabo de vídeo.  
5. Teste cruzado GPU.

#### Ferramentas oficiais

Cabo HDMI/DP known-good / Monitor ligado / GPU known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Verificar se monitor está LIGADO e no input correto (HDMI, DP, etc.).  
2. Trocar cabo de vídeo.  
3. Desligar, remover GPU, limpar contatos, reinserir.  
4. Verificar cabo PCIe power (6+2 pinos) da fonte.  
5. Se iGPU disponível: remover GPU dedicada e testar pela saída da placa-mãe.  
6. Se nenhuma saída funciona: testar outra GPU.  
7. Se outra GPU funciona: GPU original com defeito.

### Resultado esperado

#### Critério de validação

LED VGA apaga. Imagem no monitor. POST completa.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Manual da placa-mãe do fabricante

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-54 — LED BOOT (Verde)

**Fabricante BIOS:** Genérico (Múltiplos)  
**Fabricante / plataforma:** GERAL — Placas com Debug LED  
**Tipo de sinal:** LED de Diagnóstico (cor fixa)  
**Código:** `LED BOOT (Verde)`

### Identificação

#### Interpretação oficial

Boot Device Missing — Dispositivo de boot não encontrado

#### Componente afetado

SSD / HDD / NVMe / Config BIOS

#### Camada de diagnóstico

Camada 7: Periféricos Críticos

#### Fase POST

BDS (Boot Device Selection)

### Diagnóstico

#### Causa raiz (documentação oficial)

O LED BOOT indica que o BIOS completou o POST com sucesso mas não encontrou dispositivo de boot válido. Tecnicamente NÃO é uma falha de hardware POST — o hardware está funcional.

#### Condições que geram o erro

1. SSD/HDD com defeito ou morto.  
2. Windows/Linux corrompido (BSOD/kernel panic imediato).  
3. Modo UEFI/CSM incorreto no BIOS.  
4. Boot order incorreto.  
5. M.2 mal encaixado.  
6. Cabo SATA desconectado.

#### Método de diagnóstico técnico

1. Entrar no BIOS (Del/F2) e verificar se disco é detectado.  
2. Verificar Boot Order.  
3. Verificar modo UEFI vs CSM/Legacy.  
4. Verificar cabo SATA / encaixe M.2.  
5. Testar com pendrive bootável.

#### Ferramentas oficiais

Pendrive bootável (Linux Live / Windows PE) / BIOS Setup

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Entrar no BIOS Setup (Del ou F2).  
2. Verificar se SSD/HDD aparece na lista de dispositivos.  
3. Se não aparece:  

   a. Verificar cabo SATA (trocar cabo).  
   b. Verificar encaixe M.2 (remover, limpar, reinserir, parafusar).  
   c. Testar disco em outro sistema.  
   d. Se disco não é detectado em nenhum sistema: disco morto.  
4. Se aparece mas não dá boot:  

   a. Verificar Boot Order (disco deve ser primeiro).  
   b. Verificar modo: se Windows instalado em UEFI, BIOS deve estar em UEFI (não CSM).  
   c. Testar boot por pendrive para acessar disco e verificar partições.  
5. Se Windows corrompido: bootrec /rebuildbcd via Windows Recovery.

### Resultado esperado

#### Critério de validação

LED BOOT apaga. OS carrega normalmente. Disco reconhecido no BIOS. SMART OK.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

Manual da placa-mãe / Microsoft Boot Recovery Guide

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
