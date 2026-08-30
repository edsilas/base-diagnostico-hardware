---
title: Cenário — Alto uso CPU/GPU
description: Procedimento completo para o cenário Alto uso CPU/GPU - pré-requisitos, diagnóstico, correção, resultado esperado e riscos.
author: Edsilas
date: 2026-08-08
---

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Alto uso CPU/GPU**

# Cenário — Alto uso CPU/GPU

> [!NOTE]
> Procedimento completo para o cenário Alto uso CPU/GPU: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.

**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Contexto](#contexto)
- [Escopo](#escopo)
- [Fora do escopo](#fora-do-escopo)
- [Relação com outros documentos](#relação-com-outros-documentos)
- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [AU-01](#au-01)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Alto uso CPU/GPU` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs AU-01 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação e risco.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Alto uso CPU/GPU
- **IDs relacionados:** AU-01
- **Camada primária:** 9 - SO
- **Primeiro teste:** Gerenciador de Tarefas → Process Explorer → Verificar malware
- **Ferramentas necessárias:** Process Explorer, Windows Defender Offline

---

## AU-01

### Identificação

- **Sintoma observado:** CPU em 100% de uso constante sem carga aparente do utilizador. Sistema lento.
- **Camada afetada:** 9 - SO
- **Componente suspeito:** Processos do SO / Malware / Windows Update
- **Condição de ocorrência:** Gerenciador de Tarefas mostra processo a consumir CPU excessivamente. Pode ser `svchost`, `WmiPrvSE`, antimalware, ou processo desconhecido.

### Pré-requisitos

- **Dependências:** TR-01 (descartar superaquecimento como causa de lentidão)
- **Ordem de execução:** 12
- **Ferramentas oficiais:** Gerenciador de Tarefas; Process Explorer (Sysinternals); Resource Monitor (`resmon.exe`); Windows Defender Offline Scan

### Diagnóstico

**Causa raiz:** Windows Update em download/instalação, Windows Search indexando, driver com polling excessivo, ou malware (cryptominer).

**Método de diagnóstico (passo a passo):**

1. `Ctrl`+`Shift`+`Esc` → Gerenciador de Tarefas → Aba Detalhes → Ordenar por CPU.
2. Identificar o processo consumidor.
3. `SE` `svchost.exe` `ENTÃO`: clicar com botão direito → Ir para Serviço(s) → identificar o serviço.
4. `SE` `WmiPrvSE.exe` `ENTÃO`: investigar provider WMI com `wbemtest.exe`.
5. `SE` processo desconhecido `ENTÃO`: verificar assinatura digital (Propriedades → Assinaturas Digitais).
6. `SE` sem assinatura ou caminho suspeito `ENTÃO`: possível malware.

**Comandos técnicos:**

```cmd
tasklist /svc /fi "STATUS eq running"
wmic process where "PercentProcessorTime > 50" get name,processid
```
```powershell
Get-Process | Sort-Object CPU -Descending | Select -First 10
```
```cmd
:: Windows Defender:
MpCmdRun.exe -Scan -ScanType 2
```

### Execução da correção

**Procedimento de correção (detalhado):**

1. `SE` Windows Update `ENTÃO`: aguardar conclusão ou reiniciar serviço: `net stop wuauserv` → `net start wuauserv`.
2. `SE` Windows Search `ENTÃO`: Reconstruir índice: Painel de Controlo → Opções de Indexação → Avançado → Recriar.
3. `SE` malware `ENTÃO`: scan offline com Windows Defender: Settings → Update & Security → Recovery → Advanced Startup.
4. `SE` driver `ENTÃO`: atualizar ou reverter via Device Manager.
5. Verificar integridade: `sfc /scannow`.

### Resultado esperado

- **Critério de validação técnica:** CPU em idle < 5% de uso. Processo ofensor eliminado ou corrigido. Sistema responsivo.
- **Evidência de sucesso:** Gerenciador de Tarefas: CPU idle < 5%. Process Explorer sem processos anómalos. Performance restaurada.

### Risco e impacto

- **Risco associado:** Médio
- **Impacto no sistema:** Degradação de performance. Consumo energético elevado. `SE` malware: risco de roubo de dados.

> [!WARNING]
> **Risco médio:** Atenção para não interromper processos críticos do sistema que possam causar tela azul ou corrupção do Windows.

### Próximos passos (AU-01)

- Alcançado pelos nós [F09c](../07-fluxo-sistemico.md#f09c) do fluxo sistêmico
- Depende de [TR-01](travamentos-freeze.md#tr-01) — execute-os antes
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#au-01--cpu-em-100-de-uso-constante-sem-carga-aparente-do-usuário-sistema-lento)
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

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
