---
title: Cenário — BSOD (Tela Azul)
description: Procedimento completo para o cenário BSOD (Tela Azul) - pré-requisitos, diagnóstico, correção, resultado esperado e riscos.
author: Edsilas
date: 2026-08-17
---

<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — BSOD (Tela Azul)**

# Cenário — BSOD (Tela Azul)

> [!NOTE]
> Procedimento completo para o cenário BSOD (Tela Azul): pré-requisitos, diagnóstico, correção, resultado esperado e riscos.

**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste artigo

- [Contexto](#contexto)
- [Escopo](#escopo)
- [Relação com outros documentos](#relação-com-outros-documentos)
- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [BS-01](#bs-01)
- [BS-02](#bs-02)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `BSOD (Tela Azul)` conforme registado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente os seus campos.

## Escopo

IDs BS-01, BS-02 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

**Fora do escopo:** Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistémico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** BSOD (Tela Azul)
- **IDs relacionados:** BS-01, BS-02
- **Camada primária:** 4 - Memória / 5 - Armazenamento
- **Primeiro teste:** WinDbg `!analyze -v` no minidump → `mdsched.exe` → Victoria SMART
- **Ferramentas necessárias:** WinDbg, BlueScreenView, MemTest86, Victoria

---

## BS-01

### Identificação

- **Sintoma observado:** BSOD com código `MEMORY_MANAGEMENT` (0x0000001A) ou `IRQL_NOT_LESS_OR_EQUAL` (0x0000000A).
- **Camada afetada:** 4 - Memória
- **Componente suspeito:** Módulos DRAM / Driver com vazamento de memória
- **Condição de ocorrência:** Ocorre durante uso normal ou sob carga de memória. Pode ser intermitente.

### Pré-requisitos

- **Dependências:** RA-01 (PSU), RA-02 (RAM)
- **Ordem de execução:** 7
- **Ferramentas oficiais:** WinDbg (Windows Debugging Tools); Windows Memory Diagnostic (`mdsched.exe`); MemTest86; BlueScreenView (NirSoft)

### Diagnóstico

**Causa raiz:** Célula de memória defeituosa a causar bit-flip, ou driver de kernel a aceder a endereço de memória inválido. Ref: *Microsoft Docs Bug Check 0x1A*; *Intel MRC Debug Guide*.

**Método de diagnóstico (passo a passo):**

1. Analisar minidump: `C:\Windows\Minidump\*.dmp` com WinDbg.
2. Comando WinDbg: `!analyze -v` para identificar driver faulting.
3. Executar Windows Memory Diagnostic (`mdsched.exe`) → reiniciar e testar.
4. `SE` `mdsched` detetar erros `ENTÃO`: confirmar com MemTest86 (4 passes).
5. `SE` nenhum erro de RAM `ENTÃO`: driver faulting identificado no minidump é o culpado.
6. Verificar integridade do SO: `sfc /scannow`.

**Comandos técnicos:**

```cmd
:: via Executar
mdsched.exe
```
```cmd
windbg -z C:\Windows\Minidump\MMDDYY-XXXXX.dmp
!analyze -v
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Execução da correção

**Procedimento de correção (detalhado):**

1. `SE` RAM defeituosa (MemTest com erros) `ENTÃO`: substituir módulo (ver RA-02).
2. `SE` driver faulting identificado `ENTÃO`: atualizar ou reverter driver.
3. `SE` driver de terceiros `ENTÃO`: desinstalar e testar estabilidade.
4. `SE` corrupção de SO `ENTÃO`: `sfc /scannow` + `DISM RestoreHealth`.
5. `SE` persistir `ENTÃO`: reinstalação limpa do Windows.

### Resultado esperado

- **Critério de validação técnica:** Sistema estável por 72h sem BSOD. Sem novas entradas de BugCheck no Event Viewer.
- **Evidência de sucesso:** Event Viewer → System: sem BugCheck. Reliability Monitor sem crashes. MemTest 4 passes limpo.

### Risco e impacto

- **Risco associado:** Alto
- **Impacto no sistema:** Perda de dados não salvos. Corrupção do sistema de ficheiros. Instabilidade progressiva.

> [!WARNING]
> **Risco alto:** Falhas de memória podem corromper ficheiros essenciais do sistema operativo.

### Origem

**Fonte oficial:** Microsoft Docs: Bug Check 0x1A MEMORY_MANAGEMENT; Microsoft Docs: Bug Check 0x0A IRQL_NOT_LESS_OR_EQUAL; WinDbg Documentation

### Próximos passos (BS-01)

- Alcançado pelos nós [F07](../07-fluxo-sistemico.md#f07) do fluxo sistémico
- Depende de [RA-01](reinicializacao-aleatoria.md#ra-01), [RA-02](reinicializacao-aleatoria.md#ra-02) — execute-os antes
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#bs-01--bsod-com-código-memory_management-0x0000001a-ou-irql_not_less_or_equal-0x0000000a)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---

## BS-02

### Identificação

- **Sintoma observado:** BSOD com código `KERNEL_DATA_INPAGE_ERROR` (0x0000007A) ou `NTFS_FILE_SYSTEM` (0x00000024).
- **Camada afetada:** 5 - Armazenamento
- **Componente suspeito:** HDD/SSD / Controladora SATA/NVMe
- **Condição de ocorrência:** Ocorre ao aceder a ficheiros, durante boot, ou sob I/O intenso. Disco pode apresentar ruídos (HDD).

### Pré-requisitos

- **Dependências:** NL-01 (energia estável para não corromper durante clone)
- **Ordem de execution:** 8
- **Ferramentas oficiais:** Victoria HDD/SSD (Scan + S.M.A.R.T.); CrystalDiskInfo; `chkdsk`; Event Viewer; Cabo SATA known-good

### Diagnóstico

**Causa raiz:** Setores defeituosos no disco a impedir a leitura de página do kernel. Controladora com falha. Cabo SATA defeituoso. Ref: *Microsoft Docs Bug Check 0x7A*; *Seagate/WD SMART Attribute Reference*.

**Método de diagnóstico (passo a passo):**

1. Verificar S.M.A.R.T. com Victoria ou CrystalDiskInfo.
2. Atributos críticos: ID 05 (Reallocated Sectors), C5 (Current Pending), C6 (Uncorrectable).
3. `SE` qualquer RAW > 0 `ENTÃO`: disco com degradação física.
4. Executar Victoria Scan (Read/Ignore) para mapear bad blocks.
5. Verificar cabo SATA: substituir por known-good.
6. Verificar porta SATA: testar noutra porta.
7. `chkdsk /r /f` na partição afetada (se SO acessível).

**Comandos técnicos:**

```cmd
chkdsk C: /r /f
wmic diskdrive get status,model,serialnumber
```
```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter
```

### Execução da correção

**Procedimento de correção (detalhado):**

1. BACKUP IMEDIATO de dados com `ddrescue` (Linux) ou Macrium Reflect.
2. `SE` poucos bad blocks `ENTÃO`: Victoria Remap (na faixa de LBA afetada).
3. `SE` muitos bad blocks ou S.M.A.R.T. BAD `ENTÃO`: substituir disco.
4. Após substituição: reinstalar SO ou restaurar imagem.
5. `SE` cabo defeituoso `ENTÃO`: substituir cabo SATA.
6. `SE` porta SATA defeituosa `ENTÃO`: usar outra porta.

### Resultado esperado

- **Critério de validação técnica:** Novo disco com S.M.A.R.T. GOOD. Victoria Scan sem blocos vermelhos/azuis. `chkdsk` sem erros.
- **Evidência de sucesso:** Victoria: 0 bad blocks. S.M.A.R.T.: ID 05=0, C5=0, C6=0. Event Viewer: sem erros de disco por 72h.

### Risco e impacto

- **Risco associado:** Crítico
- **Impacto no sistema:** Perda irreversível de dados. SO inbootável. Degradação progressiva do disco.

> [!CAUTION]
> **Risco crítico:** Realize imediatamente o backup dos dados se houver a suspeita de degradação física (S.M.A.R.T alert), pois a perda pode ser irreversível.

### Origem

**Fonte oficial:** Microsoft Docs: Bug Check 0x7A; Seagate Knowledge Base: SMART Attributes; Western Digital SMART Reference; Victoria HDD Documentation

### Próximos passos (BS-02)

- Alcançado pelos nós [F07](../07-fluxo-sistemico.md#f07), [F12](../07-fluxo-sistemico.md#f12) do fluxo sistémico
- Depende de [NL-01](nao-liga.md#nl-01) — execute-os antes
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#bs-02--bsod-com-código-kernel_data_inpage_error-0x0000007a-ou-ntfs_file_system-0x00000024)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---

## Próximos passos

| Se você… | Vá para |
| :--- | :--- |
| o problema voltou depois da troca de peça | [Correlações entre camadas](../12-correlacoes.md) |
| aplicou a correção e precisa validar | [Validação final por componente](../13-validacao-final.md) |
| precisa operar AIDA64, MemTest86 ou Victoria | [Guias de ferramentas](../14-ferramentas/00-indice-ferramentas.md) |
| quer conferir onde este cenário entra no fluxo | [Fluxo de diagnóstico sistémico](../07-fluxo-sistemico.md) |

---

| Atributo | Valor |
| :--- | :--- |
| **Fonte primária deste documento** | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-17 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
