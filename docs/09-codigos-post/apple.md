<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Apple EFI (Mac Intel)**

# Códigos POST — Apple EFI (Mac Intel)

> Fichas completas dos códigos de POST da família Apple EFI (Mac Intel), com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `Apple (EFI)`

## Neste documento

- [POST-46 — 1 Tom repetido a cada 5 segundos](#post-46--1-tom-repetido-a-cada-5-segundos)
- [POST-47 — 3 Tons repetidos a cada 5 segundos](#post-47--3-tons-repetidos-a-cada-5-segundos)
- [POST-48 — 3 Longos + 3 Curtos + 3 Longos (SOS)](#post-48--3-longos--3-curtos--3-longos-sos)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `Apple (EFI)`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 3 código(s) da família `Apple (EFI)` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-46 — 1 Tom repetido a cada 5 segundos

**Fabricante BIOS:** Apple (EFI)  
**Fabricante / plataforma:** Apple — Mac Intel (iMac, MacBook, Mac Pro, Mac Mini)  
**Tipo de sinal:** Tom Sonoro  
**Código:** `1 Tom repetido a cada 5 segundos`

### Identificação

#### Interpretação oficial

No RAM Installed — Nenhuma memória RAM instalada

#### Componente afetado

RAM

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Detect

### Diagnóstico

#### Causa raiz (documentação oficial)

O firmware EFI do Mac não detectou nenhum módulo de RAM instalado.

#### Condições que geram o erro

1. Nenhum módulo RAM instalado.  
2. Módulos mal encaixados.  
3. RAM incompatível (DDR3L vs DDR3 — Mac requer DDR3L 1.35V em muitos modelos).  
4. Slot com defeito.

#### Método de diagnóstico técnico

1. Verificar se RAM está instalada.  
2. Verificar compatibilidade (DDR3L vs DDR3, frequência, etc.).  
3. Reseat módulos.  
4. Testar com RAM compatível Apple.

#### Ferramentas oficiais

Especificações Apple (support.apple.com) / RAM compatível

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar Mac completamente.  
2. Para iMac: usar ferramenta para abrir compartimento RAM (modelo específico).  
3. Para MacBook (modelos com RAM removível): remover tampa inferior.  
4. Remover módulos, verificar spec (DDR3L 1.35V, não DDR3 1.5V em muitos modelos).  
5. Limpar contatos com borracha branca.  
6. Reinserir módulos firmemente.  
7. Ligar.  
8. Se persistir com RAM compatível confirmada: slot ou controladora com defeito.

### Resultado esperado

#### Critério de validação

Tom para de soar. Mac inicia normalmente. 'Sobre Este Mac' mostra RAM com capacidade e frequência corretas.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Apple Support - Mac Startup Tones

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-47 — 3 Tons repetidos a cada 5 segundos

**Fabricante BIOS:** Apple (EFI)  
**Fabricante / plataforma:** Apple — Mac Intel  
**Tipo de sinal:** Tom Sonoro  
**Código:** `3 Tons repetidos a cada 5 segundos`

### Identificação

#### Interpretação oficial

RAM Integrity Failed — RAM não passou no teste de integridade

#### Componente afetado

RAM

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Test

### Diagnóstico

#### Causa raiz (documentação oficial)

A RAM foi detectada mas falhou no teste de integridade. Módulo com defeito ou incompatível.

#### Condições que geram o erro

1. Módulo RAM com defeito (células mortas).  
2. RAM incompatível (especificação errada).  
3. Mix de módulos incompatíveis entre si.  
4. Controladora de memória com falha parcial.

#### Método de diagnóstico técnico

1. Testar módulos individuais.  
2. Verificar compatibilidade no site Apple.  
3. Reset NVRAM.  
4. Testar com RAM known-good Apple-compatible.

#### Ferramentas oficiais

Reset NVRAM (Option+Cmd+P+R) / RAM compatível Apple

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Reset NVRAM: desligar, ligar e imediatamente segurar Option+Cmd+P+R por ~20s (até ouvir segundo tom de inicialização ou logo Apple aparecer 2x).  
2. Desligar.  
3. Remover todos os módulos exceto um.  
4. Ligar e testar.  
5. Se OK: adicionar módulos um a um para identificar defeituoso.  
6. Se falhar com 1 módulo: testar outro módulo known-good.  
7. Garantir que módulos são da mesma spec (marca, freq, CL, voltagem).

### Resultado esperado

#### Critério de validação

Mac inicia. 'Sobre Este Mac' mostra RAM correta. Apple Diagnostics (D ao ligar) sem erros de memória.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Apple Support - Mac Startup Tones

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-48 — 3 Longos + 3 Curtos + 3 Longos (SOS)

**Fabricante BIOS:** Apple (EFI)  
**Fabricante / plataforma:** Apple — Mac Intel (modelos com T2 ou Intel)  
**Tipo de sinal:** Tom Sonoro  
**Código:** `3 Longos + 3 Curtos + 3 Longos (SOS)`

### Identificação

#### Interpretação oficial

EFI ROM Corrupted — Firmware EFI corrompido (padrão SOS em Morse)

#### Componente afetado

EFI / Firmware

#### Camada de diagnóstico

Camada 6: Firmware

#### Fase POST

EFI Verify

### Diagnóstico

#### Causa raiz (documentação oficial)

O firmware EFI está corrompido. O padrão sonoro é SOS em código Morse (···−−−···). Em Macs com chip T2 ou Apple Silicon, a restauração requer outro Mac e Apple Configurator 2.

#### Condições que geram o erro

1. Falha durante atualização de firmware.  
2. Corrupção da SPI Flash.  
3. Degradação de firmware.  
4. Em Macs T2: chip T2 com firmware corrompido.

#### Método de diagnóstico técnico

1. Firmware Restoration via CD/USB (Macs mais antigos).  
2. Modo DFU + Apple Configurator 2 (Macs com T2).  
3. Requer outro Mac funcional para restauração.

#### Ferramentas oficiais

Outro Mac + Cabo USB-C / Apple Configurator 2 / Internet

### Execução da correção

#### Procedimento de correção (passo a passo)

Macs sem T2 (antigos):  
1. Baixar firmware restoration tool do Apple Support.  
2. Criar pendrive bootável.  
3. Iniciar Mac com pendrive e seguir instruções.  

Macs com T2:  
1. Em OUTRO Mac: instalar Apple Configurator 2 (App Store).  
2. Conectar Mac defeituoso ao Mac host via cabo USB-C (porta específica — consultar Apple docs).  
3. No Mac defeituoso: DFU Mode:  

   — Desligar.  
   — Segurar botão Power por 3s.  
   — Sem soltar Power, adicionar Shift direito + Option esquerdo + Control esquerdo por 10s.  
   — Soltar todas as teclas.  
4. No Mac host: Apple Configurator 2 → Actions → Revive/Restore.  
5. Aguardar restauração completa (pode demorar 15-30 min).

### Resultado esperado

#### Critério de validação

Mac inicia normalmente. Sem tom SOS. Apple Diagnostics sem erros. Firmware version correta em 'Sobre Este Mac' → System Report.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Apple Support - Restore Firmware / Apple Configurator 2 Guide

### Próximos passos

- Ficha da camada: [Camada 6: Firmware](../08-diagnostico-por-camada.md#camada-6--firmware-biosuefi)
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
| **Versão da documentação** | `doc-1.4.0` |
