<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Dell (LED de diagnóstico)**

# Códigos POST — Dell (LED de diagnóstico)

> Fichas completas dos códigos de POST da família Dell (LED de diagnóstico), com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `Proprietário Dell`

## Neste documento

- [POST-31 — 2 Âmbar + 1 Branco](#post-31--2-âmbar--1-branco)
- [POST-32 — 2 Âmbar + 2 Branco](#post-32--2-âmbar--2-branco)
- [POST-33 — 2 Âmbar + 3 Branco](#post-33--2-âmbar--3-branco)
- [POST-34 — 2 Âmbar + 7 Branco](#post-34--2-âmbar--7-branco)
- [POST-35 — 3 Âmbar + 1 Branco](#post-35--3-âmbar--1-branco)
- [POST-36 — 3 Âmbar + 3 Branco](#post-36--3-âmbar--3-branco)
- [POST-37 — 3 Âmbar + 5 Branco](#post-37--3-âmbar--5-branco)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `Proprietário Dell`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 7 código(s) da família `Proprietário Dell` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-31 — 2 Âmbar + 1 Branco

**Fabricante BIOS:** Proprietário Dell  
**Fabricante / plataforma:** Dell — OptiPlex / XPS / Latitude  
**Tipo de sinal:** LED Diagnóstico (Âmbar/Branco)  
**Código:** `2 Âmbar + 1 Branco`

### Identificação

#### Interpretação oficial

CPU Failure — Processador não detectado ou com falha

#### Componente afetado

CPU

#### Camada de diagnóstico

Camada 2: CPU

#### Fase POST

CPU Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O sistema Dell não detectou a CPU ou a CPU falhou durante a inicialização. O padrão LED Dell usa combinações de LEDs âmbar (erro) e branco (contagem).

#### Condições que geram o erro

1. CPU não encaixada corretamente no socket.  
2. Pinos do socket LGA tortos.  
3. CPU incompatível.  
4. Falha elétrica da CPU.

#### Método de diagnóstico técnico

1. Reseat do socket (remover e reinstalar CPU).  
2. Inspecionar pinos do socket.  
3. Verificar compatibilidade CPU.  
4. Teste cruzado de CPU.

#### Ferramentas oficiais

Dell SupportAssist Diagnostics / Lupa para socket

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC.  
2. Abrir sistema (Dell: geralmente trava lateral sem parafusos).  
3. Remover heatsink (girar para soltar pasta).  
4. Levantar alavanca do socket, remover CPU.  
5. Inspecionar pinos LGA com lupa.  
6. Se pinos OK: reinstalar CPU alinhando triângulo.  
7. Fechar alavanca, reaplicar pasta, reinstalar heatsink.  
8. Se persistir: CPU com defeito → substituir por modelo listado na service manual Dell.

### Resultado esperado

#### Critério de validação

LED de diagnóstico apaga. POST completa. Dell Diagnostics (F12 → Diagnostics) passa sem erros.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Dell OptiPlex Service Manual / Dell LED Diagnostic Codes

### Próximos passos

- Ficha da camada: [Camada 2: CPU](../08-diagnostico-por-camada.md#camada-2--cpu-processador)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-32 — 2 Âmbar + 2 Branco

**Fabricante BIOS:** Proprietário Dell  
**Fabricante / plataforma:** Dell — OptiPlex / XPS / Latitude  
**Tipo de sinal:** LED Diagnóstico (Âmbar/Branco)  
**Código:** `2 Âmbar + 2 Branco`

### Identificação

#### Interpretação oficial

System Board / PSU / Cabling — Falha placa-mãe, fonte ou cabeamento

#### Componente afetado

Placa-mãe / PSU

#### Camada de diagnóstico

Camada 1: Energia / Camada 5: Chipset

#### Fase POST

Power/Board Init

### Diagnóstico

#### Causa raiz (documentação oficial)

Erro genérico indicando problema na placa-mãe, fonte de alimentação, ou cabeamento interno. Dell recomenda teste BIST da PSU como primeiro passo.

#### Condições que geram o erro

1. Fonte de alimentação com defeito.  
2. Cabo de alimentação interno mal conectado.  
3. Placa-mãe com curto.  
4. Periférico causando curto (GPU, M.2, etc.).

#### Método de diagnóstico técnico

1. Teste BIST da fonte Dell (botão na traseira da PSU — LED verde = OK).  
2. Desconectar todos periféricos.  
3. Reset CMOS.  
4. Boot mínimo.

#### Ferramentas oficiais

Botão BIST da PSU Dell / Multímetro

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Teste BIST da PSU Dell:  

   a. Desconectar cabo AC.  
   b. Pressionar e segurar botão BIST na traseira da fonte.  
   c. Conectar cabo AC mantendo botão pressionado.  
   d. LED verde = fonte OK. Sem LED = fonte com defeito.  
2. Se fonte OK:  

   a. Desconectar TODOS os periféricos (GPU, discos, headers).  
   b. Reset CMOS (jumper na placa Dell, conforme service manual).  
   c. Ligar com mínimo (CPU + RAM + fonte).  
   d. Se POST OK: reconectar periféricos um a um.  
3. Se fonte defeituosa: substituir por modelo Dell compatível.

### Resultado esperado

#### Critério de validação

LED de diagnóstico apaga. POST completa. Dell Diagnostics sem erros. Sistema estável.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Dell OptiPlex Service Manual

### Próximos passos

- Camada declarada: `Camada 1: Energia / Camada 5: Chipset` — valor composto ou variável; ver [Taxonomia de camadas](../03-taxonomia-camadas.md)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-33 — 2 Âmbar + 3 Branco

**Fabricante BIOS:** Proprietário Dell  
**Fabricante / plataforma:** Dell — OptiPlex / XPS / Latitude  
**Tipo de sinal:** LED Diagnóstico (Âmbar/Branco)  
**Código:** `2 Âmbar + 3 Branco`

### Identificação

#### Interpretação oficial

Memory / RAM Failure — Falha de memória RAM

#### Componente afetado

RAM

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Detect/Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O sistema Dell não consegue detectar ou inicializar a memória RAM.

#### Condições que geram o erro

1. Módulos DIMM mal encaixados.  
2. Módulos incompatíveis (verificar specs Dell).  
3. Slots DIMM com defeito.  
4. Se RAM ok em teste cruzado: falha na placa-mãe.

#### Método de diagnóstico técnico

1. Testar 1 pente por vez em cada slot.  
2. Usar módulo known-good (specs Dell).  
3. Se persistir com RAM boa: falha na placa-mãe.

#### Ferramentas oficiais

Memória validada (compatível Dell) / Dell SupportAssist

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC.  
2. Remover todos os módulos.  
3. Limpar contatos.  
4. Inserir 1 módulo no slot primário (conforme service manual Dell — geralmente slot 1 mais próximo da CPU).  
5. Ligar.  
6. Se OK: adicionar módulos.  
7. Se falhar: trocar por módulo known-good compatível Dell.  
8. Se falhar com módulo bom: slot ou placa com defeito.

### Resultado esperado

#### Critério de validação

LED apaga. RAM reconhecida. Dell Diagnostics Memory Test sem erros.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Dell Service Manual / Dell LED Codes

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-34 — 2 Âmbar + 7 Branco

**Fabricante BIOS:** Proprietário Dell  
**Fabricante / plataforma:** Dell — OptiPlex / XPS / Latitude / AIO  
**Tipo de sinal:** LED Diagnóstico (Âmbar/Branco)  
**Código:** `2 Âmbar + 7 Branco`

### Identificação

#### Interpretação oficial

LCD Failure (Notebook) / GPU Failure — Falha na tela ou GPU

#### Componente afetado

LCD / GPU / Cabo eDP

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

Video/LCD Init

### Diagnóstico

#### Causa raiz (documentação oficial)

Em notebooks/AIO Dell: falha na tela LCD ou no cabo flat (LVDS/eDP). Em desktops: falha na GPU.

#### Condições que geram o erro

1. Cabo flat LCD (LVDS/eDP) desconectado ou rompido.  
2. Tela LCD com defeito.  
3. GPU com defeito (desktop).  
4. Conector do cabo na placa com mau contato.

#### Método de diagnóstico técnico

1. Dell BIST de tela: segurar tecla 'D' + Power (tela deve exibir cores sólidas).  
2. Conectar monitor externo (se imagem no externo: problema na tela/cabo).  
3. Reconectar cabo flat.  
4. Testar com outra tela.

#### Ferramentas oficiais

Teste BIST Tela Dell (D + Power) / Monitor Externo

### Execução da correção

#### Procedimento de correção (passo a passo)

NOTEBOOK:  
1. BIST de tela: segurar 'D' + pressionar Power.  

   — Se tela exibe cores sólidas: tela OK, problema pode ser GPU/driver.  
   — Se tela preta: cabo flat ou tela com defeito.  
2. Conectar monitor externo:  

   — Se externo funciona: cabo flat LVDS/eDP rompido ou tela LCD com defeito.  
   — Se externo também sem imagem: GPU/placa com defeito.  
3. Se cabo flat: abrir moldura da tela, verificar conexão do cabo eDP na placa e no painel.  

DESKTOP: Seguir procedimento de GPU (reseat, teste cruzado).

### Resultado esperado

#### Critério de validação

BIST de tela mostra cores sólidas. Imagem estável. Dell Diagnostics Display Test OK.

### Risco e origem

#### Risco / criticidade

Médio

#### Fonte oficial

Dell Service Manual / Dell LCD Diagnostics

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-35 — 3 Âmbar + 1 Branco

**Fabricante BIOS:** Proprietário Dell  
**Fabricante / plataforma:** Dell — OptiPlex / XPS  
**Tipo de sinal:** LED Diagnóstico (Âmbar/Branco)  
**Código:** `3 Âmbar + 1 Branco`

### Identificação

#### Interpretação oficial

CMOS Battery Failure — Bateria CMOS esgotada

#### Componente afetado

Bateria CR2032

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

CMOS Init

### Diagnóstico

#### Causa raiz (documentação oficial)

A bateria CR2032 do CMOS está com tensão abaixo do limiar mínimo. Sistema pode perder data/hora e configurações do BIOS a cada desligamento.

#### Condições que geram o erro

1. Bateria CR2032 com tensão < 2.8V.  
2. Suporte da bateria com mau contato (oxidação).

#### Método de diagnóstico técnico

1. Medir tensão da bateria (deve ser ≥ 2.9V).  
2. Verificar contato no suporte (lâminas oxidadas?).

#### Ferramentas oficiais

Multímetro (medir 3V na bateria) / Bateria CR2032 nova

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC.  
2. Localizar bateria CR2032 na placa-mãe.  
3. Remover bateria (puxar trava do suporte).  
4. Medir tensão: < 2.8V = trocar.  
5. Inserir bateria nova (+ para cima).  
6. Limpar contatos do suporte com isopropanol se oxidados.  
7. Ligar, entrar no BIOS Setup (F2), configurar data/hora.  
8. Salvar e reiniciar.

### Resultado esperado

#### Critério de validação

LED apaga. Data/hora mantidas após desligamento prolongado. BIOS mantém configurações.

### Risco e origem

#### Risco / criticidade

Baixo

#### Fonte oficial

Dell Service Manual

### Próximos passos

- Ficha da camada: [Camada 5: Chipset / Motherboard](../08-diagnostico-por-camada.md#camada-5--chipset--motherboard)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-36 — 3 Âmbar + 3 Branco

**Fabricante BIOS:** Proprietário Dell  
**Fabricante / plataforma:** Dell — OptiPlex / XPS  
**Tipo de sinal:** LED Diagnóstico (Âmbar/Branco)  
**Código:** `3 Âmbar + 3 Branco`

### Identificação

#### Interpretação oficial

BIOS Recovery Image Not Found — Imagem de recuperação não encontrada

#### Componente afetado

BIOS / Firmware

#### Camada de diagnóstico

Camada 6: Firmware

#### Fase POST

BIOS Recovery

### Diagnóstico

#### Causa raiz (documentação oficial)

O sistema Dell entrou em modo de BIOS Recovery mas não encontrou a imagem de recuperação no pendrive ou internamente.

#### Condições que geram o erro

1. BIOS corrompida e recovery não encontra arquivo.  
2. Pendrive sem o arquivo correto.  
3. Formato do pendrive incorreto (deve ser FAT32).  
4. Arquivo com nome incorreto.

#### Método de diagnóstico técnico

1. Baixar BIOS recovery do suporte Dell.  
2. Renomear para BIOS_IMG.rcv (ou conforme modelo).  
3. Colocar na raiz de pendrive FAT32.  
4. Executar recovery (Ctrl+Esc ao ligar).

#### Ferramentas oficiais

Pendrive FAT32 / Arquivo BIOS recovery Dell / Outro PC

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Em outro PC: baixar BIOS mais recente do site support.dell.com (buscar por Service Tag).  
2. Extrair o arquivo .exe (Dell BIOS geralmente é auto-extraível).  
3. Renomear o arquivo .bin/.rom para BIOS_IMG.rcv (verificar no manual o nome exato para o modelo).  
4. Copiar para raiz de pendrive FAT32 (≤ 16GB recomendado).  
5. No sistema Dell:  

   a. Inserir pendrive na porta USB.  
   b. Desligado, segurar Ctrl + Esc.  
   c. Pressionar botão Power mantendo Ctrl+Esc.  
   d. Soltar após ~5s — processo de recovery inicia (LEDs piscam, pode demorar 2-5 min).  
6. NÃO desligar durante o processo.  
7. Sistema reinicia automaticamente.

### Resultado esperado

#### Critério de validação

POST completa. BIOS Setup acessível (F2). Versão de BIOS atualizada. Sistema estável.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Dell BIOS Recovery Guide / Dell Support

### Próximos passos

- Ficha da camada: [Camada 6: Firmware](../08-diagnostico-por-camada.md#camada-6--firmware-biosuefi)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-37 — 3 Âmbar + 5 Branco

**Fabricante BIOS:** Proprietário Dell  
**Fabricante / plataforma:** Dell — OptiPlex / XPS  
**Tipo de sinal:** LED Diagnóstico (Âmbar/Branco)  
**Código:** `3 Âmbar + 5 Branco`

### Identificação

#### Interpretação oficial

Power Rail Failure (EC/SIO) — Falha em trilha de alimentação secundária

#### Componente afetado

VRM / Power Rails / EC

#### Camada de diagnóstico

Camada 1: Energia

#### Fase POST

Power Sequencing

### Diagnóstico

#### Causa raiz (documentação oficial)

Uma das trilhas de alimentação secundárias (3.3V, 5V, ou outra rail gerenciada pelo Embedded Controller/SIO) está em curto ou ausente.

#### Condições que geram o erro

1. Curto-circuito em uma das rails secundárias (3.3V, 5V, 1.05V, etc.).  
2. Capacitor em curto na placa.  
3. Componente em curto (USB, M.2, etc.) puxando rail para baixo.  
4. Embedded Controller (EC) com defeito.

#### Método de diagnóstico técnico

1. Medir todas as tensões nos pontos de teste.  
2. Desconectar todos periféricos.  
3. Verificar se há componentes visivelmente queimados.  
4. Injeção de tensão controlada (bancada avançada).

#### Ferramentas oficiais

Multímetro / Fonte de bancada (injeção de tensão) / Câmera térmica (opcional)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desconectar TUDO (periféricos, discos, GPU).  
2. Medir standby 5VSB no conector de alimentação.  
3. Se 5VSB ausente: verificar fonte.  
4. Se 5VSB presente: ligar e medir 12V, 5V, 3.3V.  
5. Rail ausente ou muito baixo: curto na placa.  
6. Desconectar headers um a um medindo a rail.  
7. Se rail volta com header desconectado: componente no header em curto.  
8. Se rail ausente mesmo sem nada: placa em curto interno.  

Este tipo de falha geralmente requer reparo em bancada especializada ou troca da placa-mãe.

### Resultado esperado

#### Critério de validação

Todas as rails dentro de spec. POST completa. Sistema estável sob carga.

### Risco e origem

#### Risco / criticidade

Crítico

#### Fonte oficial

Dell Service Manual / Dell Power Supply Specs

### Próximos passos

- Ficha da camada: [Camada 1: Energia](../08-diagnostico-por-camada.md#camada-1--energia-psuvrm)
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
