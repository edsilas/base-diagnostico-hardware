<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Travamentos (Freeze)**

# Cenário — Travamentos (Freeze)

> Procedimento completo para o cenário Travamentos (Freeze): pré-requisitos, diagnóstico, correção, resultado esperado e riscos.


**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [TR-01](#tr-01)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Travamentos (Freeze)` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs TR-01 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Travamentos (Freeze)
- **IDs relacionados:** TR-01
- **Camada primária:** 3 - CPU
- **Primeiro teste:** AIDA64 Stability Test + OSD (temperatura + throttling)
- **Ferramentas necessárias:** AIDA64, Pasta térmica, Álcool isopropílico

---

## TR-01

### Identificação

#### Sintoma observado

Sistema congela completamente (freeze). Mouse e teclado não respondem. Sem BSOD.

#### Camada afetada

3 - CPU

#### Componente suspeito

CPU / Thermal Throttling / VRM

#### Condição de ocorrência

Ocorre sob carga ou após período de uso. Pode estar associado a superaquecimento.

### Pré-requisitos

#### Dependências

RA-01 (PSU estável), SV-01/02 (vídeo funcional para monitorar)

#### Ordem de execução

9

#### Ferramentas oficiais

AIDA64 Engineer (Stability Test + OSD); Pasta térmica (ex: Noctua NT-H1, Arctic MX-6); Álcool isopropílico 99%; Câmera térmica (opcional)

### Diagnóstico

#### Causa raiz

CPU atingindo TjMax e throttling extremo, ou VRM da placa-mãe não sustentando carga, causando voltage droop fatal. Ref: Intel Datasheet Volume 1 (Thermal Specifications); AMD Processor Programming Reference.

#### Método de diagnóstico (passo a passo)

1. Instalar AIDA64 e configurar OSD com CPU Package Temp e Throttling indicator.  
2. Executar AIDA64 Stability Test (Stress FPU).  
3. Monitorar temperatura: SE > 95°C ou Throttling > 0% → problema térmico.  
4. Parar teste imediatamente se Temp > 100°C.  
5. Verificar montagem do cooler: pressão uniforme nos 4 pontos.  
6. Verificar pasta térmica: remover cooler, limpar com álcool isopropílico 99%, reaplicar pasta de qualidade.  
7. SE temperatura OK mas freeze persiste → suspeitar de firmware/BIOS.

#### Comandos técnicos

AIDA64: Stress FPU (isola geração de calor máximo)  
Event Viewer: eventvwr.msc → System → filtrar WHEA-Logger

### Execução da correção

#### Procedimento de correção (detalhado)

1. Desligar e desconectar AC.  
2. Remover cooler da CPU.  
3. Limpar pasta térmica antiga com álcool isopropílico e pano sem fiapos.  
4. Reaplicar pasta térmica (método do ponto central ou X).  
5. Reinstalar cooler com pressão uniforme.  
6. SE watercooler: verificar bomba (vibração/som).  
7. Retestar com AIDA64 Stability Test 30min.

### Resultado esperado

#### Critério de validação técnica

AIDA64 Stability Test 30min sem throttling. CPU Package Temp estabiliza abaixo de 85°C sob carga máxima.

#### Evidência de sucesso

Gráfico AIDA64: temperatura estabilizada. Throttling = 0%. Frequência de clock mantida em boost.

### Risco e impacto

#### Risco associado

Crítico

#### Impacto no sistema

Degradação acelerada do silício. Freezes progressivamente mais frequentes. Possível dano permanente à CPU.

### Origem

#### Fonte oficial

Intel 13th/14th Gen Datasheet Vol.1 (Thermal Design); AMD Ryzen Processor Technical Reference; AIDA64 Documentation

### Próximos passos

- Alcançado pelos nós [F09b](../07-fluxo-sistemico.md#f09b) do fluxo sistêmico
- Depende de [SV-01](liga-sem-video.md#sv-01), [RA-01](reinicializacao-aleatoria.md#ra-01) — execute-os antes
- É pré-requisito de [AU-01](alto-uso-cpu-gpu.md#au-01)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#tr-01--sistema-congela-completamente-freeze-mouse-e-teclado-não-respondem-sem-bsod)
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
