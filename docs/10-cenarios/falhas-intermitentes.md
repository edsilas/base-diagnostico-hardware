<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Falhas intermitentes**

# Cenário — Falhas intermitentes

> Procedimento completo para o cenário Falhas intermitentes: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.


**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [FI-01](#fi-01)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Falhas intermitentes` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs FI-01 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

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

#### Sintoma observado

Falhas esporádicas sem padrão claro: freezes, BSODs variados, reinícios. Não reproduzível sob demanda.

#### Camada afetada

1 - Energia

#### Componente suspeito

PSU / Contatos elétricos / Cabos internos

#### Condição de ocorrência

Problema intermitente. Pode ocorrer a qualquer momento. Difícil reprodução.

### Pré-requisitos

#### Dependências

Todas as camadas anteriores como diagnóstico diferencial

#### Ordem de execução

13

#### Ferramentas oficiais

AIDA64 Engineer (Log CSV contínuo); Multímetro; UPS/No-break; Event Viewer

### Diagnóstico

#### Causa raiz

Mau contato intermitente em conector de energia (ATX 24-pin, CPU 8-pin, PCIe), micro-interrupções na rede elétrica sem UPS, ou capacitores de PSU em degradação inicial. Ref: ATX12V PSU Design Guide (Transient Response); IPC-A-610 (Acceptability of Electronic Assemblies).

#### Método de diagnóstico (passo a passo)

1. Configurar AIDA64 Log Contínuo (CSV, intervalo 1s) com sensores: +12V, +5V, +3.3V, Vcore, CPU Temp, GPU Temp.  
2. Deixar rodando por período prolongado (12-24h) cobrindo o horário típico das falhas.  
3. Quando a falha ocorrer, analisar a última linha do CSV antes da interrupção.  
4. SE última leitura mostra queda de voltagem → PSU ou contato.  
5. SE temperatura alta na última leitura → problema térmico.  
6. Reconectar TODOS os cabos internos: ATX 24-pin, CPU 8-pin, PCIe, SATA dados e energia.  
7. Verificar cada conector por pinos escurecidos/derretidos.

#### Comandos técnicos

AIDA64: Preferências > Hardware Monitoring > Log > CSV, 1s interval  
eventvwr.msc → System → Kernel-Power, WHEA-Logger  
powercfg /systempowerreport

### Execução da correção

#### Procedimento de correção (detalhado)

1. Reconectar todos os conectores internos de energia com firmeza.  
2. Substituir cabos de energia suspeitos.  
3. Instalar UPS/No-break para eliminar variável de rede elétrica.  
4. SE logs indicam PSU → substituir PSU.  
5. SE logs indicam temperatura → resolver térmico (SA-01).  
6. SE problema persiste com PSU nova + UPS → avançar para diagnóstico de placa-mãe.

### Resultado esperado

#### Critério de validação técnica

Sistema estável por 72h+ com AIDA64 Log ativo. Nenhuma interrupção registrada.

#### Evidência de sucesso

CSV contínuo de 72h sem gaps. Event Viewer sem Kernel-Power 41. Reliability Monitor sem falhas.

### Risco e impacto

#### Risco associado

Alto

#### Impacto no sistema

Dificuldade de diagnóstico. Corrupção de dados silenciosa. Perda de produtividade do usuário.

### Origem

#### Fonte oficial

ATX12V PSU Design Guide v2.53 (Transient Response); Microsoft Docs: Kernel-Power 41; AIDA64 Sensor Logging Documentation

### Próximos passos

- **Nenhum nó do fluxo sistêmico conduz a este cenário.** Entrada apenas pelo [índice de cenários](00-indice-cenarios.md). Ver [P-09 em pendências](../references/pendencias.md)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#fi-01--falhas-esporádicas-sem-padrão-claro-freezes-bsods-variados-reinícios-não-reproduzível-sob-demanda)
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
