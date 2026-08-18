---
title: "Cenário — Travamentos (Freeze)"
description: "Procedimento completo para o cenário Travamentos (Freeze) - pré-requisitos, diagnóstico, correção, resultado esperado e riscos."
author: "Edsilas"
date: "2026-08-18"
---

<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Travamentos (Freeze)**

# Cenário — Travamentos (Freeze)

> [!NOTE]
> Procedimento completo para o cenário Travamentos (Freeze): pré-requisitos, diagnóstico, correção, resultado esperado e riscos.

**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas durante o uso.

## Neste artigo

- [Contexto](#contexto)
- [Escopo](#escopo)
- [Relação com outros documentos](#relação-com-outros-documentos)
- [Entrada rápida](#entrada-rápida)
- [TR-01](#tr-01)
- [Próximos passos](#próximos-passos)

## Contexto

Ficha de diagnóstico do cenário `Travamentos (Freeze)` conforme registado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz os respectivos campos técnicos.

## Escopo

ID `TR-01` — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

**Fora do escopo:** outros cenários, catálogo de códigos POST e guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistémico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida

| Atributo | Valor |
| :--- | :--- |
| **Cenário** | Travamentos (Freeze) |
| **ID relacionado** | TR-01 |
| **Camada primária** | 3 - CPU |
| **Primeiro teste** | AIDA64 Stability Test + OSD |
| **Monitoramento** | Temperatura + Throttling |
| **Ferramentas necessárias** | AIDA64, pasta térmica, álcool isopropílico 99% |

---

## TR-01

### Identificação

- **Sintoma observado:** Sistema congela completamente (freeze). Mouse e teclado não respondem. Sem BSOD.
- **Camada afetada:** 3 - CPU
- **Componente suspeito:** CPU / Thermal Throttling / VRM
- **Condição de ocorrência:** Ocorre sob carga ou após período de uso. Pode estar associado a superaquecimento.

### Pré-requisitos

- **Dependências:** RA-01 (PSU estável), SV-01/02 (vídeo funcional para monitoramento)
- **Ordem de execução:** 9
- **Ferramentas oficiais:** AIDA64 Engineer; pasta térmica (ex.: Noctua NT-H1, Arctic MX-6); álcool isopropílico 99%; câmera térmica (opcional)

### Diagnóstico

**Causa raiz:** CPU atingindo TjMax e apresentando throttling extremo, ou VRM da placa-mãe incapaz de sustentar a carga, provocando *voltage droop* e possível travamento.

**Referências:** *Intel Datasheet Volume 1 — Thermal Specifications*; *AMD Processor Programming Reference*.

**Método de diagnóstico:**

1. Instalar o AIDA64.
2. Configurar o OSD com `CPU Package Temp` e `Throttling Indicator`.
3. Executar o **AIDA64 Stability Test** com **Stress FPU**.
4. Monitorar continuamente a temperatura e o throttling.
5. Se a temperatura ultrapassar `95 °C` ou o `Throttling` for superior a `0%`, considerar indício de problema térmico.
6. Se a temperatura ultrapassar `100 °C`, interromper imediatamente o teste.
7. Verificar a montagem do cooler e a pressão uniforme nos pontos de fixação.
8. Inspecionar a pasta térmica.
9. Se necessário, remover o cooler, limpar com álcool isopropílico 99% e reaplicar pasta térmica.
10. Se a temperatura permanecer normal e o freeze persistir, investigar firmware, BIOS e VRM.

### Comandos técnicos

```text
AIDA64
Stability Test → Stress FPU

Visualizador de Eventos
eventvwr.msc

Windows Logs → System
Filtro: WHEA-Logger
```

### Execução da correção

1. Desligar o equipamento e desconectar a alimentação AC.
2. Remover o cooler da CPU.
3. Remover completamente a pasta térmica antiga.
4. Limpar a CPU e a base do cooler com álcool isopropílico 99%.
5. Aplicar nova pasta térmica.
6. Reinstalar o cooler garantindo pressão uniforme.
7. Se for utilizado watercooler, verificar o funcionamento da bomba.
8. Verificar filtros de poeira e fluxo de ar do gabinete.
9. Executar novamente o **AIDA64 Stability Test por 30 minutos**.

### Resultado esperado

- **Critério de validação técnica:** AIDA64 Stability Test executado por 30 minutos sem throttling.
- **Temperatura:** CPU Package Temp abaixo de `85 °C` sob carga máxima.
- **Throttling:** `0%`.
- **Estabilidade:** nenhum novo freeze durante o teste.
- **Evidência de sucesso:** temperatura estabilizada, throttling em `0%` e frequência de clock mantida dentro do comportamento esperado.

### Risco e impacto

| Atributo | Classificação |
| :--- | :--- |
| **Risco associado** | Crítico |
| **Impacto no sistema** | Degradação acelerada do silício, aumento da frequência dos freezes e possibilidade de dano permanente à CPU |

> [!CAUTION]
> Interrompa imediatamente o teste de estresse caso a temperatura atinja o limite definido para o diagnóstico. Não mantenha o equipamento sob carga térmica excessiva durante a investigação.

### Origem

**Fontes técnicas:**

- Intel 13th/14th Gen Datasheet — Thermal Design
- AMD Ryzen Processor Technical Reference
- AIDA64 Documentation

### Próximos passos (TR-01)

- Alcançado pelo nó [F09b](../07-fluxo-sistemico.md#f09b) do fluxo sistémico
- Depende de [SV-01](liga-sem-video.md#sv-01) e [RA-01](reinicializacao-aleatoria.md#ra-01) — execute-os antes
- É pré-requisito de [AU-01](alto-uso-cpu-gpu.md#au-01)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#tr-01--sistema-congela-completamente-freeze-mouse-e-teclado-não-respondem-sem-bsod)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---

## Próximos passos

| Se você... | Vá para |
| :--- | :--- |
| O problema voltou depois da troca de peça | [Correlações entre camadas](../12-correlacoes.md) |
| Aplicou a correção e precisa validar | [Validação final por componente](../13-validacao-final.md) |
| Precisa operar AIDA64, MemTest86 ou Victoria | [Guias de ferramentas](../14-ferramentas/00-indice-ferramentas.md) |
| Quer conferir onde este cenário entra no fluxo | [Fluxo de diagnóstico sistémico](../07-fluxo-sistemico.md) |

---

| Atributo | Valor |
| :--- | :--- |
| **Fonte primária deste documento** | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-18 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
