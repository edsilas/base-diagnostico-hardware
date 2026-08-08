<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Award BIOS**

# Códigos POST — Award BIOS

> Fichas completas dos códigos de POST da família Award BIOS, com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `Award BIOS`

## Neste documento

- [POST-22 — 1 Longo + 2 Curtos](#post-22--1-longo--2-curtos)
- [POST-23 — 1 Longo + 3 Curtos](#post-23--1-longo--3-curtos)
- [POST-24 — Repetitivo (Sirene contínua)](#post-24--repetitivo-sirene-contínua)
- [POST-25 — Contínuo Longo (ininterrupto)](#post-25--contínuo-longo-ininterrupto)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `Award BIOS`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 4 código(s) da família `Award BIOS` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-22 — 1 Longo + 2 Curtos

**Fabricante BIOS:** Award BIOS  
**Fabricante / plataforma:** Award — Desktop Legado  
**Tipo de sinal:** Beep Sonoro  
**Código:** `1 Longo + 2 Curtos`

### Identificação

#### Interpretação oficial

Video Adapter Error — Falha no adaptador gráfico

#### Componente afetado

GPU / Adaptador Gráfico

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

Video Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O BIOS Award não consegue inicializar o adaptador de vídeo. Em sistemas legados Award, algumas placas exigiam carga resistiva no conector VGA para detectar monitor.

#### Condições que geram o erro

1. GPU não detectada ou com defeito.  
2. Slot AGP/PCIe com mau contato.  
3. Monitor não conectado (Award antigo pode exigir presença de monitor).  
4. Cabos de vídeo defeituosos.

#### Método de diagnóstico técnico

1. Remover e limpar GPU.  
2. Verificar se monitor está conectado e ligado.  
3. Em sistemas AGP: verificar chave de voltagem AGP.  
4. Teste cruzado GPU.

#### Ferramentas oficiais

GPU known-good / Cabo VGA/DVI known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC.  
2. Remover GPU, limpar contatos com borracha branca.  
3. Limpar slot com ar comprimido.  
4. Reinserir GPU.  
5. Conectar monitor e verificar que está ligado.  
6. Ligar sistema.  
7. Se persistir: testar outra GPU.  
8. Em sistemas muito antigos (AGP): verificar compatibilidade de voltagem AGP.

### Resultado esperado

#### Critério de validação

POST completa com vídeo. Imagem estável no monitor.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Award BIOS Beep Code Reference

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- **Código ambíguo.** Confira o critério de diferenciação em [Ambiguidade de códigos](../11-ambiguidades.md#1-longo--2-curtos) antes de aplicar o procedimento.
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-23 — 1 Longo + 3 Curtos

**Fabricante BIOS:** Award BIOS  
**Fabricante / plataforma:** Award — Desktop Legado  
**Tipo de sinal:** Beep Sonoro  
**Código:** `1 Longo + 3 Curtos`

### Identificação

#### Interpretação oficial

Video Adapter Error / VRAM — Falha na VRAM da GPU

#### Componente afetado

GPU / VRAM

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

Video VRAM Test

### Diagnóstico

#### Causa raiz (documentação oficial)

Similar ao anterior, mas especificamente indica falha no teste de memória de vídeo (VRAM). Pode indicar chips de memória da GPU com defeito.

#### Condições que geram o erro

1. VRAM da GPU com defeito.  
2. Capacitores da GPU com defeito (inchados).  
3. GPU com solda BGA fraturada (cold solder joint).  
4. Alimentação insuficiente para GPU.

#### Método de diagnóstico técnico

1. Mesmo procedimento do erro anterior.  
2. Inspecionar capacitores da GPU (inchados?).  
3. Verificar alimentação PCIe (6/8 pinos).  
4. Teste cruzado GPU.

#### Ferramentas oficiais

Inspeção visual GPU / GPU known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Seguir procedimento do código anterior (1L+2C).  
2. Adicionalmente: inspecionar capacitores da GPU com lupa.  
3. Verificar fonte — potência suficiente para GPU?  
4. Se GPU com capacitores inchados: condenação ou reparo especializado.

### Resultado esperado

#### Critério de validação

POST completa com vídeo. Sem artefatos visuais. FurMark estável.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Award BIOS Beep Code Reference

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- **Código ambíguo.** Confira o critério de diferenciação em [Ambiguidade de códigos](../11-ambiguidades.md#1-longo--3-curtos) antes de aplicar o procedimento.
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-24 — Repetitivo (Sirene contínua)

**Fabricante BIOS:** Award BIOS  
**Fabricante / plataforma:** Award — Desktop Legado  
**Tipo de sinal:** Beep Sonoro  
**Código:** `Repetitivo (Sirene contínua)`

### Identificação

#### Interpretação oficial

CPU Overheating / Voltage Out of Range — Superaquecimento ou tensão fora de faixa

#### Componente afetado

CPU / PSU / Cooler

#### Camada de diagnóstico

Camada 1: Energia / Camada 2: CPU

#### Fase POST

Thermal/Voltage Monitor

### Diagnóstico

#### Causa raiz (documentação oficial)

O BIOS detectou temperatura da CPU acima do limiar de segurança ou tensão fora da faixa especificada. O padrão de sirene é distinto e repetitivo, não deve ser confundido com beeps discretos.

#### Condições que geram o erro

1. Cooler da CPU desconectado ou não funcionando.  
2. Pasta térmica seca/ausente.  
3. Fluxo de ar do gabinete obstruído.  
4. Fonte de alimentação entregando voltagem incorreta.  
5. Overclock com VCore excessivo.

#### Método de diagnóstico técnico

1. Verificar imediatamente se cooler está girando.  
2. Medir temperatura com termômetro IR no heatsink.  
3. Medir tensões da fonte (12V, 5V, 3.3V) com multímetro.  
4. Verificar BIOS Hardware Monitor.

#### Ferramentas oficiais

Termômetro IR / Multímetro (tensões da fonte) / BIOS Hardware Monitor

### Execução da correção

#### Procedimento de correção (passo a passo)

1. DESLIGAR IMEDIATAMENTE para evitar dano à CPU.  
2. Verificar se cooler está conectado ao header CPU_FAN.  
3. Verificar se fan gira livremente (debris?).  
4. Remover cooler, limpar pasta térmica antiga.  
5. Reaplicar pasta térmica (grão de arroz no centro do IHS).  
6. Reinstalar cooler com pressão uniforme.  
7. Medir tensões da fonte:  

   12V: 11.4-12.6V  
   5V: 4.75-5.25V  
   3.3V: 3.14-3.47V  
8. Se tensões fora de spec: trocar fonte.  
9. Se OC: reverter para defaults.

### Resultado esperado

#### Critério de validação

POST sem alarme. BIOS Hardware Monitor mostra temperaturas normais (idle < 50°C). Tensões dentro de spec ATX. Stress test estável (30 min).

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Award BIOS Reference / ATX PSU Specification

### Próximos passos

- Camada declarada: `Camada 1: Energia / Camada 2: CPU` — valor composto ou variável; ver [Taxonomia de camadas](../03-taxonomia-camadas.md)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-25 — Contínuo Longo (ininterrupto)

**Fabricante BIOS:** Award BIOS  
**Fabricante / plataforma:** Award — Desktop Legado  
**Tipo de sinal:** Beep Sonoro  
**Código:** `Contínuo Longo (ininterrupto)`

### Identificação

#### Interpretação oficial

Memory Not Installed or Not Detected — RAM ausente ou não reconhecida

#### Componente afetado

RAM

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Detect

### Diagnóstico

#### Causa raiz (documentação oficial)

Beep contínuo e ininterrupto indica que nenhum módulo de memória foi detectado. O BIOS não encontrou RAM funcional em nenhum slot.

#### Condições que geram o erro

1. Nenhum módulo DIMM instalado.  
2. Todos os módulos mal encaixados.  
3. Tensão VDRAM ausente (VRM de memória com defeito).  
4. Todos os slots com defeito.  
5. Incompatibilidade total de memória.

#### Método de diagnóstico técnico

1. Verificar se há módulos instalados.  
2. Remover e reinstalar com pressão firme.  
3. Limpar contatos.  
4. Medir VDRAM nos pinos de alimentação do slot.  
5. Testar módulo known-good.

#### Ferramentas oficiais

Multímetro (VDRAM no slot DIMM) / Módulo known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Verificar se módulos estão fisicamente presentes.  
2. Remover todos, limpar contatos com borracha branca + isopropanol.  
3. Limpar slots com ar comprimido.  
4. Inserir 1 módulo no slot primário.  
5. Ligar sistema.  
6. Se beep persiste: medir VDRAM no slot (DDR3: 1.5V, DDR4: 1.2V).  
7. Se VDRAM = 0V: VRM de memória com defeito → placa condenada.  
8. Se VDRAM OK mas nenhum módulo funciona: controladora de memória (CPU) com defeito.

### Resultado esperado

#### Critério de validação

POST completa com beep de sucesso (1 curto). RAM reconhecida com capacidade correta.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Award BIOS Reference

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
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
