<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Superaquecimento**

# Cenário — Superaquecimento

> Procedimento completo para o cenário Superaquecimento: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.


**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [SA-01](#sa-01)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Superaquecimento` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs SA-01 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Superaquecimento
- **IDs relacionados:** SA-01
- **Camada primária:** 3 - CPU
- **Primeiro teste:** AIDA64 Sensores (idle) → Stability Test FPU (2min)
- **Ferramentas necessárias:** AIDA64, Pasta térmica, Termômetro IR

---

## SA-01

### Identificação

#### Sintoma observado

CPU operando acima de 90°C em idle ou atingindo TjMax (100-105°C) rapidamente sob carga.

#### Camada afetada

3 - CPU

#### Componente suspeito

Cooler / Pasta Térmica / Ventilação do Gabinete

#### Condição de ocorrência

Temperatura ambiente normal (<30°C). Verificável via AIDA64 Sensor Panel ou BIOS.

### Pré-requisitos

#### Dependências

NL-01 (energia), SV-01/02 (vídeo para monitorar)

#### Ordem de execução

11

#### Ferramentas oficiais

AIDA64 Engineer; Termômetro infravermelho (opcional); Pasta térmica nova; Álcool isopropílico 99%

### Diagnóstico

#### Causa raiz

Pasta térmica seca/ausente, cooler mal encaixado (pressão desigual nos pinos/parafusos), bomba de AIO inoperante, ou fluxo de ar do gabinete obstruído. Ref: Intel Thermal Design Guide; AMD Thermal Solution Design Guide.

#### Método de diagnóstico (passo a passo)

1. AIDA64 → Computador → Sensores: verificar CPU Package Temp em idle.  
2. SE > 60°C em idle → problema térmico confirmado.  
3. Executar AIDA64 Stability Test (Stress FPU) por 2 minutos.  
4. SE > 95°C em 2 minutos → parar imediatamente.  
5. Verificar se ventoinhas do cooler estão girando.  
6. Verificar se bomba de AIO vibra (encostar dedo no bloco d'água).  
7. Remover cooler e inspecionar pasta térmica (cobertura, secagem).

#### Comandos técnicos

AIDA64: Menu Computador > Sensores  
AIDA64: Ferramentas > Teste de Estabilidade > Stress FPU

### Execução da correção

#### Procedimento de correção (detalhado)

1. Desligar e desconectar AC.  
2. Remover cooler.  
3. Limpar pasta térmica antiga (CPU e base do cooler) com álcool isopropílico 99%.  
4. Aplicar nova pasta térmica.  
5. Reinstalar cooler garantindo pressão uniforme.  
6. Limpar filtros de poeira do gabinete.  
7. Verificar fluxo de ar: intake frontal → exhaust traseiro/superior.  
8. Retestar com AIDA64 Stability Test.

### Resultado esperado

#### Critério de validação técnica

CPU Package Temp < 45°C em idle. < 85°C sob carga FPU máxima por 30 min. Throttling = 0%.

#### Evidência de sucesso

AIDA64 Statistics: Temp Max < 85°C. Gráfico de temperatura estabilizado. Clock mantido.

### Risco e impacto

#### Risco associado

Crítico

#### Impacto no sistema

Degradação do silício. Throttling reduz performance. Possível dano permanente em hardware antigo sem proteção térmica.

### Origem

#### Fonte oficial

Intel Thermal Design Guide (TDP/TjMax); AMD Ryzen Thermal Solution Design Guide; Noctua Application Notes

### Próximos passos

- Alcançado pelos nós [F11](../07-fluxo-sistemico.md#f11) do fluxo sistêmico
- Depende de [NL-01](nao-liga.md#nl-01), [SV-01](liga-sem-video.md#sv-01) — execute-os antes
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#sa-01--cpu-operando-acima-de-90c-em-idle-ou-atingindo-tjmax-100-105c-rapidamente-sob-carga)
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
