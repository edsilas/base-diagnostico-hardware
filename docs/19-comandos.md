<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL`, coluna `Comandos Técnicos`. Não editar manualmente sem atualizar a fonte. -->

[Início](../README.md) › [Consulte a referência](../README.md#consulte-a-referência) › **Referência de comandos técnicos**

# Referência de comandos técnicos

> Todos os comandos declarados nos cenários, reunidos com camada, risco e link para a ficha completa.


**Aplica-se a:** Consulta rápida durante a execução de um procedimento

## Neste documento

- [Comandos por cenário](#comandos-por-cenário)
- [Comandos que aparecem em mais de um cenário](#comandos-que-aparecem-em-mais-de-um-cenário)
- [Próximos passos](#próximos-passos)

## Contexto

Todos os comandos declarados na coluna `Comandos Técnicos` dos cenários, reunidos em um só lugar. Serve para consulta rápida durante o atendimento, sem abrir cada ficha.

## Escopo

Comandos por cenário, transcritos literalmente, com o contexto de uso e o link para a ficha completa.

## Fora do escopo

Comandos citados dentro de outros campos (método de diagnóstico, correção) — esses permanecem nas fichas; procedimentos de interface gráfica das ferramentas (ver `14-ferramentas/`).

## Relação com outros documentos

- [Índice de cenários](10-cenarios/00-indice-cenarios.md) — fichas completas
- [Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)
- [Validação final por componente](13-validacao-final.md)

---

> [!CAUTION]
> Os comandos abaixo são transcrição literal da fonte e vários **alteram o sistema**:
> `chkdsk /r /f` e `sfc /scannow`, por exemplo, modificam disco e arquivos de sistema. Consulte a
> ficha do cenário antes de executar — ela traz pré-requisitos, risco declarado e critério de
> validação.

> [!NOTE]
> Onde a fonte registra `N/A`, o diagnóstico é físico (medição elétrica, inspeção, substituição) e
> não há comando a executar.

## Comandos por cenário

### [NL-01](10-cenarios/nao-liga.md#nl-01) — Equipamento não liga: sem LEDs, sem ventoinhas, sem sinal de vida.

**Camada declarada:** 1 - Energia · **Risco:** Crítico

Sem comando: N/A (teste elétrico físico)

---

### [NL-02](10-cenarios/nao-liga.md#nl-02) — PSU funcional (teste paperclip OK), mas sistema não liga ao conectar na placa-mãe.

**Camada declarada:** 7 - Placa-mãe · **Risco:** Alto

Sem comando: N/A (teste físico)

---

### [SV-01](10-cenarios/liga-sem-video.md#sv-01) — Sistema liga (ventoinhas giram, LEDs acendem) mas sem saída de vídeo. Monitor em standby.

**Camada declarada:** 4 - Memória · **Risco:** Alto

Sem comando: N/A (teste físico). Pós-reparo: MemTest86 via boot USB

---

### [SV-02](10-cenarios/liga-sem-video.md#sv-02) — Sistema liga sem vídeo. RAM validada. Debug LED estaciona em VGA.

**Camada declarada:** 6 - GPU · **Risco:** Médio

Sem comando: N/A (teste físico)

---

### [RA-01](10-cenarios/reinicializacao-aleatoria.md#ra-01) — Sistema reinicia sem aviso durante uso normal ou sob carga. Sem BSOD prévio.

**Camada declarada:** 1 - Energia · **Risco:** Crítico

```text
eventvwr.msc → System → Filter: Source=Kernel-Power, Event ID=41
powercfg /energy /duration 60
```

---

### [RA-02](10-cenarios/reinicializacao-aleatoria.md#ra-02) — Reinicialização aleatória. PSU validada. Ocorre principalmente com carga em RAM.

**Camada declarada:** 4 - Memória · **Risco:** Alto

```text
MemTest86 via boot USB (sem comandos Windows)
Pós-validação Windows: sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

---

### [BS-01](10-cenarios/bsod.md#bs-01) — BSOD com código MEMORY_MANAGEMENT (0x0000001A) ou IRQL_NOT_LESS_OR_EQUAL (0x0000000A).

**Camada declarada:** 4 - Memória · **Risco:** Alto

```text
mdsched.exe (via Executar)
windbg -z C:\Windows\Minidump\MMDDYY-XXXXX.dmp
!analyze -v
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

---

### [BS-02](10-cenarios/bsod.md#bs-02) — BSOD com código KERNEL_DATA_INPAGE_ERROR (0x0000007A) ou NTFS_FILE_SYSTEM (0x00000024).

**Camada declarada:** 5 - Armazenamento · **Risco:** Crítico

```text
chkdsk C: /r /f
wmic diskdrive get status,model,serialnumber
Get-PhysicalDisk | Get-StorageReliabilityCounter (PowerShell)
```

---

### [TR-01](10-cenarios/travamentos-freeze.md#tr-01) — Sistema congela completamente (freeze). Mouse e teclado não respondem. Sem BSOD.

**Camada declarada:** 3 - CPU · **Risco:** Crítico

```text
AIDA64: Stress FPU (isola geração de calor máximo)
Event Viewer: eventvwr.msc → System → filtrar WHEA-Logger
```

---

### [DN-01](10-cenarios/disco-nao-reconhecido.md#dn-01) — Disco não aparece na BIOS/UEFI nem no Gerenciador de Dispositivos.

**Camada declarada:** 5 - Armazenamento · **Risco:** Alto

```text
diskmgmt.msc
diskpart → list disk
Get-PhysicalDisk (PowerShell)
wmic diskdrive list brief
```

---

### [SA-01](10-cenarios/superaquecimento.md#sa-01) — CPU operando acima de 90°C em idle ou atingindo TjMax (100-105°C) rapidamente sob carga.

**Camada declarada:** 3 - CPU · **Risco:** Crítico

```text
AIDA64: Menu Computador > Sensores
AIDA64: Ferramentas > Teste de Estabilidade > Stress FPU
```

---

### [AU-01](10-cenarios/alto-uso-cpu-gpu.md#au-01) — CPU em 100% de uso constante sem carga aparente do usuário. Sistema lento.

**Camada declarada:** 9 - SO · **Risco:** Médio

```text
tasklist /svc /fi "STATUS eq running"
wmic process where "PercentProcessorTime > 50" get name,processid
Get-Process | Sort-Object CPU -Descending | Select -First 10
Windows Defender: MpCmdRun.exe -Scan -ScanType 2
```

---

### [FI-01](10-cenarios/falhas-intermitentes.md#fi-01) — Falhas esporádicas sem padrão claro: freezes, BSODs variados, reinícios. Não reproduzível sob demanda.

**Camada declarada:** 1 - Energia · **Risco:** Alto

```text
AIDA64: Preferências > Hardware Monitoring > Log > CSV, 1s interval
eventvwr.msc → System → Kernel-Power, WHEA-Logger
powercfg /systempowerreport
```

---

## Comandos que aparecem em mais de um cenário

Agrupamento por ocorrência do nome do executável ou utilitário no texto acima.

| Comando / utilitário | Cenários |
| --- | --- |
| `eventvwr.msc` | [RA-01](10-cenarios/reinicializacao-aleatoria.md#ra-01), [TR-01](10-cenarios/travamentos-freeze.md#tr-01), [FI-01](10-cenarios/falhas-intermitentes.md#fi-01) |
| `mdsched.exe` | [BS-01](10-cenarios/bsod.md#bs-01) |
| `chkdsk` | [BS-02](10-cenarios/bsod.md#bs-02) |
| `sfc /scannow` | [RA-02](10-cenarios/reinicializacao-aleatoria.md#ra-02), [BS-01](10-cenarios/bsod.md#bs-01) |
| `DISM` | [RA-02](10-cenarios/reinicializacao-aleatoria.md#ra-02), [BS-01](10-cenarios/bsod.md#bs-01) |
| `diskmgmt.msc` | [DN-01](10-cenarios/disco-nao-reconhecido.md#dn-01) |
| `wmic` | [BS-02](10-cenarios/bsod.md#bs-02), [DN-01](10-cenarios/disco-nao-reconhecido.md#dn-01), [AU-01](10-cenarios/alto-uso-cpu-gpu.md#au-01) |
| PowerShell (`Get-*`) | [BS-02](10-cenarios/bsod.md#bs-02), [DN-01](10-cenarios/disco-nao-reconhecido.md#dn-01), [AU-01](10-cenarios/alto-uso-cpu-gpu.md#au-01) |
| WinDbg (`!analyze -v`) | [BS-01](10-cenarios/bsod.md#bs-01) |
| `tasklist` | [AU-01](10-cenarios/alto-uso-cpu-gpu.md#au-01) |
| MemTest86 (boot USB) | [SV-01](10-cenarios/liga-sem-video.md#sv-01), [RA-02](10-cenarios/reinicializacao-aleatoria.md#ra-02) |
| AIDA64 | [TR-01](10-cenarios/travamentos-freeze.md#tr-01), [SA-01](10-cenarios/superaquecimento.md#sa-01), [FI-01](10-cenarios/falhas-intermitentes.md#fi-01) |

> A tabela acima é montada por correspondência de texto sobre a mesma coluna transcrita acima.
> Nível de confiança: **Confirmado** (os comandos) / **Inferido** (o agrupamento).

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| precisa do procedimento completo do cenário | [Índice de cenários](10-cenarios/00-indice-cenarios.md) |
| o comando é de uma ferramenta com guia próprio | [Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md) |
| executou e precisa validar | [Validação final por componente](13-validacao-final.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL`, coluna `Comandos Técnicos` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.3.0` |
