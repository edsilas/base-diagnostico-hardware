---
title: Cenário — Falhas intermitentes
description: Procedimento completo para o cenário Falhas intermitentes - pré-requisitos, diagnóstico, correção, resultado esperado e riscos.
author: Edsilas
date: 2026-08-18
---

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Falhas intermitentes**

# Cenário — Falhas intermitentes

> [!NOTE]
> Procedimento completo para o cenário Falhas intermitentes: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.

**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Contexto](#contexto)
- [Escopo](#escopo)
- [Fora do escopo](#fora-do-escopo)
- [Relação com outros documentos](#relação-com-outros-documentos)
- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [FI-01](#fi-01)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Falhas intermitentes` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs FI-01 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação e risco.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Falhas intermitentes
- **IDs relacionados:** FI-01
- **Camada primária:** 1 - Energia (mais comum)
- **Primeiro teste:** AIDA64 Log CSV contínuo (24h) → Analisar última linha antes da falha
- **Ferramentas necessárias:** AIDA64 (Log), UPS, Multímetro

---

## FI-01

### Identificação

- **Sintoma observado:** Falhas esporádicas sem padrão claro: freezes, BSODs variados, reinícios. Não reproduzível sob demanda.
- **Camada afetada:** 1 - Energia
- **Componente suspeito:** PSU / Contactos elétricos / Cabos internos
- **Condição de ocorrência:** Problema intermitente. Pode ocorrer a qualquer momento. Difícil reprodução.

### Pré-requisitos

- **Dependências:** Todas as camadas anteriores como diagnóstico diferencial
- **Ordem de execução:** 13
- **Ferramentas oficiais:** AIDA64 Engineer (Log CSV contínuo); Multímetro; UPS/No-break; Event Viewer

### Diagnóstico

**Causa raiz:** Mau contacto intermitente em conetor de energia (ATX 24-pin, CPU 8-pin, PCIe), micro-interrupções na rede elétrica sem UPS, ou capacitores de PSU em degradação inicial.

**Método de diagnóstico (passo a passo):**

1. Configurar AIDA64 Log Contínuo (CSV, intervalo 1s) com sensores: +12V, +5V, +3.3V, Vcore, CPU Temp, GPU Temp.
2. Deixar a executar por período prolongado (12-24h) cobrindo o horário típico das falhas.
3. Quando a falha ocorrer, analisar a última linha do CSV antes da interrupção.
4. `SE` última leitura mostra queda de voltagem `ENTÃO`: PSU ou contacto.
5. `SE` temperatura alta na última leitura `ENTÃO`: problema térmico.
6. Reconectar TODOS os cabos internos: ATX 24-pin, CPU 8-pin, PCIe, SATA dados e energia.
7. Verificar cada conetor por pinos escurecidos/derretidos.

**Comandos técnicos:**

```text
AIDA64: Preferências > Hardware Monitoring > Log > CSV, 1s interval
```
```cmd
:: Executar no Windows (Win + R)
eventvwr.msc
:: Em Event Viewer -> Windows Logs -> System -> procurar por Kernel-Power, WHEA-Logger
```
```cmd
powercfg /systempowerreport
```

### Execução da correção

**Procedimento de correção (detalhado):**

1. Reconectar todos os conectores internos de energia com firmeza.
2. Substituir cabos de energia suspeitos.
3. Instalar UPS/No-break para eliminar variável de rede elétrica.
4. `SE` logs indicam PSU `ENTÃO`: substituir PSU.
5. `SE` logs indicam temperatura `ENTÃO`: resolver térmico (SA-01).
6. `SE` problema persiste com PSU nova + UPS `ENTÃO`: avançar para diagnóstico de placa-mãe.

### Resultado esperado

- **Critério de validação técnica:** Sistema estável por 72h+ com AIDA64 Log ativo. Nenhuma interrupção registrada.
- **Evidência de sucesso:** CSV contínuo de 72h sem gaps. Event Viewer sem Kernel-Power 41. Reliability Monitor sem falhas.

### Risco e impacto

- **Risco associado:** Alto
- **Impacto no sistema:** Dificuldade de diagnóstico. Corrupção de dados silenciosa. Perda de produtividade do utilizador.

> [!WARNING]
> **Risco alto:** Falhas de energia intermitentes não diagnosticadas podem corromper silenciosamente o sistema de arquivos e danificar componentes sensíveis a longo prazo.

### Próximos passos (FI-01)

- **Como se chega aqui pelo fluxo:** a partir de [F08](../07-fluxo-sistemico.md#regra-de-entrada-do-cenário-fi-01), quando o sistema não opera estável mas F09, F09b e F09c não reproduzem a falha sob demanda. Entrada direta também pelo [índice de cenários](00-indice-cenarios.md)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#fi-01--falhas-esporádicas-sem-padrão-claro-freezes-bsods-variados-reinícios-não-reproduzível-sob-demanda)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| o problema voltou depois da troca de peça | [Correlações entre camadas](../12-correlacoes.md) |
| aplicou a correção e precisa validar | [Validação final por componente](../13-validacao-final.md) |
| precisa operar AIDA64, MemTest86 ou Victoria | [Guias de ferramentas](../14-ferramentas/00-indice-ferramentas.md) |
| quer conferir onde este cenário entra no fluxo | [Regra de entrada de FI-01](../07-fluxo-sistemico.md#regra-de-entrada-do-cenário-fi-01) |

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
