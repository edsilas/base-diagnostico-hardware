<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Liga sem vídeo**

# Cenário — Liga sem vídeo

> Procedimento completo para o cenário Liga sem vídeo: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.


**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [SV-01](#sv-01)
- [SV-02](#sv-02)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Liga sem vídeo` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs SV-01, SV-02 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Liga sem vídeo
- **IDs relacionados:** SV-01, SV-02
- **Camada primária:** 4 - Memória / 6-GPU
- **Primeiro teste:** Reencaixar RAM (1 módulo, slot primário) → Testar iGPU
- **Ferramentas necessárias:** Manual placa-mãe, GPU known-good

---

## SV-01

### Identificação

#### Sintoma observado

Sistema liga (ventoinhas giram, LEDs acendem) mas sem saída de vídeo. Monitor em standby.

#### Camada afetada

4 - Memória

#### Componente suspeito

Módulos DRAM / Slots DIMM

#### Condição de ocorrência

POST não completa. Beep codes indicam erro de memória (se speaker conectado). Debug LEDs em DRAM.

### Pré-requisitos

#### Dependências

NL-01, NL-02 (energia e placa-mãe validadas)

#### Ordem de execução

3

#### Ferramentas oficiais

MemTest86 (após obter vídeo); Borracha branca de vinil para contatos; Manual da placa-mãe (mapa de slots)

### Diagnóstico

#### Causa raiz

Falha na inicialização de memória (Memory Training failure): módulos mal encaixados, incompatíveis ou defeituosos. SPD não lido corretamente. Ref: JEDEC JESD79-5 (DDR5 SDRAM Standard); Intel Memory Reference Code (MRC) documentation.

#### Método de diagnóstico (passo a passo)

1. Desligar e desconectar AC.  
2. Remover todos os módulos de RAM.  
3. Reinstalar UM módulo no slot primário (geralmente A2 — verificar manual da placa-mãe).  
4. Ligar o sistema.  
5. SE vídeo volta → adicionar módulos um a um para isolar o defeituoso.  
6. SE sem vídeo com módulo known-good → suspeitar de slot ou CPU (IMC).  
7. Limpar contatos do módulo com borracha branca de vinil.

#### Comandos técnicos

N/A (teste físico). Pós-reparo: MemTest86 via boot USB

### Execução da correção

#### Procedimento de correção (detalhado)

1. Limpar contatos dourados do módulo com borracha branca (movimentos unidirecionais).  
2. Soprar slot DIMM com ar comprimido.  
3. Reinstalar módulo com pressão firme até travas encaixarem.  
4. SE módulo defeituoso identificado → substituir e iniciar RMA.  
5. SE slot defeituoso → testar em outro slot; se confirmado, placa-mãe com defeito.  
6. Redefinir BIOS para defaults (CMOS Clear) se XMP/DOCP causou falha de training.

### Resultado esperado

#### Critério de validação técnica

Sistema completa POST e exibe imagem no monitor. MemTest86 conclui 4 passes sem erros.

#### Evidência de sucesso

Debug LED da placa-mãe sai de DRAM e avança para VGA/Boot. Beep único curto (POST OK).

### Risco e impacto

#### Risco associado

Alto

#### Impacto no sistema

Sistema inoperante sem vídeo. Dados inacessíveis até resolução.

### Origem

#### Fonte oficial

JEDEC JESD79-4/5 (DDR4/DDR5 Standards); Intel MRC; Manual OEM da placa-mãe (Memory QVL)

### Próximos passos

- Alcançado pelos nós [F03](../07-fluxo-sistemico.md#f03), [F04](../07-fluxo-sistemico.md#f04) do fluxo sistêmico
- Depende de [NL-01](nao-liga.md#nl-01), [NL-02](nao-liga.md#nl-02) — execute-os antes
- É pré-requisito de [SV-02](liga-sem-video.md#sv-02), [TR-01](travamentos-freeze.md#tr-01), [SA-01](superaquecimento.md#sa-01)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#sv-01--sistema-liga-ventoinhas-giram-leds-acendem-mas-sem-saída-de-vídeo-monitor-em-standby)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---

## SV-02

### Identificação

#### Sintoma observado

Sistema liga sem vídeo. RAM validada. Debug LED estaciona em VGA.

#### Camada afetada

6 - GPU

#### Componente suspeito

GPU Dedicada / iGPU / Slot PCIe x16

#### Condição de ocorrência

Memória funcional confirmada. Debug LED indica falha de GPU/VGA. Sem sinal em nenhuma saída de vídeo.

### Pré-requisitos

#### Dependências

SV-01 (RAM validada)

#### Ordem de execução

4

#### Ferramentas oficiais

Ar comprimido (limpeza de slot PCIe); Sistema known-good para teste cruzado; Cabo de vídeo known-good (HDMI/DP)

### Diagnóstico

#### Causa raiz

GPU sem contato adequado no slot PCIe, alimentação auxiliar (6/8-pin) desconectada, GPU defeituosa, ou iGPU desativada na BIOS. Ref: PCI Express Base Specification Rev 5.0; OEM GPU User Guide.

#### Método de diagnóstico (passo a passo)

1. Desligar e desconectar AC.  
2. Remover GPU dedicada.  
3. Conectar monitor na saída de vídeo da placa-mãe (iGPU).  
4. SE vídeo volta → GPU dedicada ou slot defeituoso.  
5. Reinstalar GPU com pressão firme. Verificar cabos de alimentação auxiliar (6+2 pin).  
6. Testar GPU em outro slot PCIe ou em outro sistema known-good.  
7. SE iGPU também sem vídeo → suspeitar de CPU ou firmware.

#### Comandos técnicos

N/A (teste físico)

### Execução da correção

#### Procedimento de correção (detalhado)

1. Limpar contatos PCIe da GPU com ar comprimido.  
2. Reinstalar firmemente no slot x16 primário.  
3. Conectar todos os cabos de alimentação auxiliar.  
4. SE GPU defeituosa confirmada → substituir e iniciar RMA.  
5. SE slot defeituoso → usar slot x16 secundário (pode operar em x8).  
6. Atualizar BIOS se iGPU estava desativada incorretamente.

### Resultado esperado

#### Critério de validação técnica

POST completa, imagem exibida no monitor. GPU detectada no Device Manager sem erros.

#### Evidência de sucesso

Debug LED avança além de VGA. Driver de vídeo carrega sem código 43. Resolução nativa atingida.

### Risco e impacto

#### Risco associado

Médio

#### Impacto no sistema

Sistema sem saída visual. Inacessível para diagnóstico posterior via GUI.

### Origem

#### Fonte oficial

PCI Express Base Spec Rev 5.0; NVIDIA/AMD GPU User Guides; Manual OEM da placa-mãe

### Próximos passos

- Alcançado pelos nós [F05](../07-fluxo-sistemico.md#f05) do fluxo sistêmico
- Depende de [SV-01](liga-sem-video.md#sv-01) — execute-os antes
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#sv-02--sistema-liga-sem-vídeo-ram-validada-debug-led-estaciona-em-vga)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---


## Próximos passos

| Se você… | Vá para |
| --- | --- |
| o problema voltou depois da troca de peça | [Correlações entre camadas](../12-correlacoes.md) |
| aplicou a correção e precisa validar | [Validação final por componente](../13-validacao-final.md) |
| precisa operar AIDA64, MemTest86 ou Victoria | [Guias de ferramentas](../14-ferramentas/00-indice-ferramentas.md) |
| quer conferir onde este cenário entra no fluxo | [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.3.0` |
