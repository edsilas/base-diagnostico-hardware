<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — AMI UEFI / Aptio V**

# Códigos POST — AMI UEFI / Aptio V

> Fichas completas dos códigos de POST da família AMI UEFI / Aptio V, com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `AMI (UEFI/Aptio V)`

## Neste documento

- [POST-11 — 1 Longo + 2 Curtos](#post-11--1-longo--2-curtos)
- [POST-12 — 1 Longo + 3 Curtos](#post-12--1-longo--3-curtos)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `AMI (UEFI/Aptio V)`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 2 código(s) da família `AMI (UEFI/Aptio V)` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-11 — 1 Longo + 2 Curtos

**Fabricante BIOS:** AMI (UEFI/Aptio V)  
**Fabricante / plataforma:** AMI UEFI/Aptio — Desktop Moderno  
**Tipo de sinal:** Beep Sonoro  
**Código:** `1 Longo + 2 Curtos`

### Identificação

#### Interpretação oficial

Video System Failure — GPU não detectada ou ROM Opcional falha

#### Componente afetado

GPU / PCIe

#### Camada de diagnóstico

Camada 4: Vídeo

#### Fase POST

DXE Video Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O BIOS não consegue inicializar o adaptador gráfico. A GPU não é detectada no barramento PCIe, ou a Option ROM da GPU falha ao carregar. Em sistemas com GPU via riser (mineração, casos compactos), pode ser problema de compatibilidade PCIe Gen.

#### Condições que geram o erro

1. GPU mal encaixada no slot PCIe.  
2. Cabo de alimentação PCIe (6+2 pinos) desconectado.  
3. GPU sem energia suficiente (fonte subdimensionada).  
4. Riser PCIe com defeito ou incompatível.  
5. BIOS configurada para iGPU mas GPU dedicada instalada (ou vice-versa).

#### Método de diagnóstico técnico

1. Verificar cabo PCIe da fonte (6+2 pinos) firmemente conectado.  
2. Reseat GPU no slot.  
3. Se usar riser: testar diretamente no slot.  
4. Mudar PCIe Gen na BIOS para Gen 3.0 (compatibilidade).  
5. Teste cruzado com outra GPU.

#### Ferramentas oficiais

Teste GPU Cruzado / Fonte com potência adequada / Multímetro (12V PCIe)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain.  
2. Verificar cabo PCIe 6+2 pinos da fonte → GPU.  
3. Remover GPU, limpar contatos, reinserir.  
4. Se riser: remover e conectar GPU diretamente ao slot.  
5. Se persistir: testar outra GPU.  
6. Se outra GPU funciona: GPU original com defeito.  
7. Se nenhuma GPU funciona: slot PCIe ou configuração BIOS.  
8. Reset CMOS e verificar configuração Primary Display.

### Resultado esperado

#### Critério de validação

POST completa com vídeo. GPU reconhecida no BIOS e Device Manager. Benchmark gráfico estável.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

AMI Aptio V Status Codes / Fabricante da placa-mãe

### Próximos passos

- Ficha da camada: [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu)
- **Código ambíguo.** Confira o critério de diferenciação em [Ambiguidade de códigos](../11-ambiguidades.md#1-longo--2-curtos) antes de aplicar o procedimento.
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-12 — 1 Longo + 3 Curtos

**Fabricante BIOS:** AMI (UEFI/Aptio V)  
**Fabricante / plataforma:** AMI UEFI/Aptio — Desktop Moderno  
**Tipo de sinal:** Beep Sonoro  
**Código:** `1 Longo + 3 Curtos`

### Identificação

#### Interpretação oficial

Conventional/Extended Memory Failure — RAM mal encaixada ou incompatível

#### Componente afetado

RAM (Módulos DIMM)

#### Camada de diagnóstico

Camada 3: Memória

#### Fase POST

Memory Training (PEI)

### Diagnóstico

#### Causa raiz (documentação oficial)

Falha no treinamento de memória (memory training) durante a fase PEI. A controladora de memória não consegue estabelecer comunicação com os módulos DIMM. Muito comum com DDR5 que requer treinamento mais longo.

#### Condições que geram o erro

1. Módulo DIMM mal encaixado (trava não fechou completamente).  
2. Slot errado (ex: usar A1 quando manual pede A2 primeiro).  
3. Módulos incompatíveis (mix de ranks, frequências, fabricantes).  
4. DDR5: PMIC do módulo com defeito.  
5. Pressão excessiva do cooler empenando o socket.

#### Método de diagnóstico técnico

1. Verificar se travas do DIMM fecharam completamente.  
2. Consultar manual: usar slots corretos (geralmente A2 para single channel).  
3. Testar slots individualmente com 1 módulo.  
4. Verificar QVL (Qualified Vendor List) da placa-mãe.  
5. DDR5: aguardar até 3 min no primeiro boot (treinamento).

#### Ferramentas oficiais

Manual da placa-mãe (QVL) / Módulo known-good

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Desligar, remover AC, power drain.  
2. Remover todos os módulos DIMM.  
3. Pressionar travas com firmeza uniforme ao inserir.  
4. Inserir 1 módulo no slot A2 (ou conforme manual).  
5. Ligar — se DDR5, aguardar até 3 minutos.  
6. Se POST OK: adicionar módulos um a um.  
7. Se falhar: testar outro módulo known-good.  
8. Se falhar com módulo bom: verificar se cooler exerce pressão excessiva no IHS (afrouxar 1/4 de volta).

### Resultado esperado

#### Critério de validação

POST completa. RAM reconhecida com capacidade, frequência e timings corretos no BIOS. MemTest86 sem erros.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

AMI Aptio V Status Codes

### Próximos passos

- Ficha da camada: [Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram)
- **Código ambíguo.** Confira o critério de diferenciação em [Ambiguidade de códigos](../11-ambiguidades.md#1-longo--3-curtos) antes de aplicar o procedimento.
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
