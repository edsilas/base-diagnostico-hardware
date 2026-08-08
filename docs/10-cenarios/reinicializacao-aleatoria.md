<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Reinicialização aleatória**

# Cenário — Reinicialização aleatória

> Procedimento completo para o cenário Reinicialização aleatória: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.


**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [RA-01](#ra-01)
- [RA-02](#ra-02)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Reinicialização aleatória` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs RA-01, RA-02 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Reinicialização aleatória
- **IDs relacionados:** RA-01, RA-02
- **Camada primária:** 1 - Energia / 4-Memória
- **Primeiro teste:** AIDA64 Voltage monitoring → MemTest86
- **Ferramentas necessárias:** AIDA64, MemTest86, Multímetro

---

## RA-01

### Identificação

#### Sintoma observado

Sistema reinicia sem aviso durante uso normal ou sob carga. Sem BSOD prévio.

#### Camada afetada

1 - Energia

#### Componente suspeito

PSU / VRM / Cabos de alimentação

#### Condição de ocorrência

Reinício ocorre sob carga (jogos, renderização) ou aleatoriamente. Event Viewer mostra Kernel-Power ID 41.

### Pré-requisitos

#### Dependências

Nenhuma (pode ser primeiro sintoma)

#### Ordem de execução

5

#### Ferramentas oficiais

AIDA64 Engineer (Stability Test + Voltage Monitoring); Event Viewer (eventvwr.msc); Multímetro digital; Testador de PSU

### Diagnóstico

#### Causa raiz

PSU não sustenta carga de pico: proteção OCP/OPP disparando, Vdrop excessivo na linha +12V, ou ripple acima da tolerância ATX (120mV p-p em +12V). Ref: ATX12V PSU Design Guide v2.53 §3.2.1 Transient Load Response.

#### Método de diagnóstico (passo a passo)

1. Abrir Event Viewer (eventvwr.msc) → System → filtrar por Kernel-Power ID 41.  
2. Executar AIDA64 Stability Test (Stress CPU + FPU + Cache + Memory).  
3. Monitorar aba Voltages durante o stress: +12V deve permanecer entre 11.4V e 12.6V.  
4. SE queda abrupta na linha +12V antes do reinício → PSU não sustenta carga.  
5. Medir com multímetro nos conectores Molex/SATA durante carga se sensor de software não for confiável.  
6. Verificar cabos de alimentação: conectores frouxos, pinos queimados.

#### Comandos técnicos

eventvwr.msc → System → Filter: Source=Kernel-Power, Event ID=41  
powercfg /energy /duration 60

### Execução da correção

#### Procedimento de correção (detalhado)

1. Substituir PSU por unidade de maior potência e certificação 80 Plus.  
2. Verificar e substituir cabos de alimentação com sinais de derretimento.  
3. SE VRM da placa-mãe (verificar com câmera térmica ou toque): SE > 100°C → adicionar dissipadores de VRM ou melhorar airflow.  
4. Retestar com AIDA64 Stability Test por mínimo 30 minutos.

### Resultado esperado

#### Critério de validação técnica

Sistema completa 30min de AIDA64 Stability Test sem reinício. +12V estável. Kernel-Power 41 não reaparece.

#### Evidência de sucesso

Gráfico de Voltages do AIDA64 estável. Event Viewer sem novos Kernel-Power 41 por 48h.

### Risco e impacto

#### Risco associado

Crítico

#### Impacto no sistema

Reinícios sob carga podem corromper sistema de arquivos e causar perda de dados. PSU instável pode danificar componentes.

### Origem

#### Fonte oficial

ATX12V PSU Design Guide v2.53 (Intel); Microsoft Docs: Kernel-Power Event ID 41; AIDA64 Documentation

### Próximos passos

- Alcançado pelos nós [F09](../07-fluxo-sistemico.md#f09) do fluxo sistêmico
- É pré-requisito de [RA-02](reinicializacao-aleatoria.md#ra-02), [BS-01](bsod.md#bs-01), [TR-01](travamentos-freeze.md#tr-01)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#ra-01--sistema-reinicia-sem-aviso-durante-uso-normal-ou-sob-carga-sem-bsod-prévio)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---

## RA-02

### Identificação

#### Sintoma observado

Reinicialização aleatória. PSU validada. Ocorre principalmente com carga em RAM.

#### Camada afetada

4 - Memória

#### Componente suspeito

Módulos DRAM / XMP Profile / IMC da CPU

#### Condição de ocorrência

Reinício durante operações intensivas de memória. PSU estável. Pode ou não gerar BSOD antes do reinício.

### Pré-requisitos

#### Dependências

RA-01 (PSU validada como estável)

#### Ordem de execução

6

#### Ferramentas oficiais

MemTest86 v10+ (USB bootável); BIOS/UEFI Setup; AIDA64 (Cache & Memory Benchmark)

### Diagnóstico

#### Causa raiz

Instabilidade de memória: XMP/DOCP instável, VDIMM insuficiente, binagem ruim do módulo, ou IMC (Integrated Memory Controller) da CPU não sustenta a frequência anunciada. Ref: JEDEC JESD79-4/5; Intel/AMD Memory Overclocking Guides.

#### Método de diagnóstico (passo a passo)

1. Executar MemTest86 (boot USB) com XMP ativo: 4 passes mínimos.  
2. SE erros detectados → desativar XMP na BIOS e retestar em frequência JEDEC padrão.  
3. SE erros persistem em JEDEC → módulo defeituoso. Isolar com teste individual (um pente por vez).  
4. SE erros apenas com XMP → aumentar VDIMM em +0.02V incrementais (máx 1.45V DDR4 / 1.40V DDR5).  
5. Verificar se RAM está na QVL (Qualified Vendor List) da placa-mãe.

#### Comandos técnicos

MemTest86 via boot USB (sem comandos Windows)  
Pós-validação Windows: sfc /scannow  
DISM /Online /Cleanup-Image /RestoreHealth

### Execução da correção

#### Procedimento de correção (detalhado)

1. Desativar XMP na BIOS como primeiro passo.  
2. Retestar em JEDEC base.  
3. SE erro persiste → teste individual de pentes.  
4. Identificar pente defeituoso → RMA ao fabricante.  
5. SE XMP instável mas JEDEC OK → ajustar VDIMM ou reduzir frequência manualmente.  
6. Verificar integridade do SO após resolver: sfc /scannow + DISM RestoreHealth.

### Resultado esperado

#### Critério de validação técnica

MemTest86 completa 4 passes com 0 erros na configuração final. Sistema estável por 48h.

#### Evidência de sucesso

Relatório HTML do MemTest86 com PASS verde. Event Viewer sem Kernel-Power 41. Sem BSODs.

### Risco e impacto

#### Risco associado

Alto

#### Impacto no sistema

Corrupção silenciosa de dados. BSODs intermitentes. Instabilidade progressiva do SO.

### Origem

#### Fonte oficial

MemTest86 User Guide (PassMark); JEDEC JESD79-4/5; Intel/AMD Memory OC Guides; Manual OEM (Memory QVL)

### Próximos passos

- Alcançado pelos nós [F09](../07-fluxo-sistemico.md#f09), [F13](../07-fluxo-sistemico.md#f13) do fluxo sistêmico
- Depende de [RA-01](reinicializacao-aleatoria.md#ra-01) — execute-os antes
- É pré-requisito de [BS-01](bsod.md#bs-01)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#ra-02--reinicialização-aleatória-psu-validada-ocorre-principalmente-com-carga-em-ram)
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
