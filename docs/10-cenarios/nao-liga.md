<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Não liga**

# Cenário — Não liga

> Procedimento completo para o cenário Não liga: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.


**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [NL-01](#nl-01)
- [NL-02](#nl-02)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Não liga` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs NL-01, NL-02 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Não liga
- **IDs relacionados:** NL-01, NL-02
- **Camada primária:** 1 - Energia
- **Primeiro teste:** Teste paperclip da PSU → Multímetro nas tensões
- **Ferramentas necessárias:** Multímetro, Testador PSU, Chave de fenda

---

## NL-01

### Identificação

#### Sintoma observado

Equipamento não liga: sem LEDs, sem ventoinhas, sem sinal de vida.

#### Camada afetada

1 - Energia

#### Componente suspeito

PSU (Fonte de Alimentação)

#### Condição de ocorrência

Ao pressionar o botão Power. Nenhuma resposta elétrica detectada.

### Pré-requisitos

#### Dependências

Nenhuma (primeiro teste da cadeia)

#### Ordem de execução

1

#### Ferramentas oficiais

Multímetro digital (Fluke 115 ou equivalente); Testador de PSU dedicado (ex: Thermaltake Dr. Power II)

### Diagnóstico

#### Causa raiz

Falha na PSU: capacitores de saída degradados, fusível interno rompido, ou circuito de standby (+5VSB) inoperante. Ref: ATX12V Power Supply Design Guide v2.53, Intel §2.2 DC Output.

#### Método de diagnóstico (passo a passo)

1. Desconectar cabo AC e aguardar 30s.  
2. Medir tensão +5VSB no conector ATX 24 pinos (pino 9, fio roxo) com multímetro. Deve ser 5.0V ±5%.  
3. Realizar teste de paperclip: curto-circuitar PS_ON (pino 16, fio verde) ao COM (pino 17, fio preto).  
4. Medir +12V, +5V, +3.3V nos pinos correspondentes.  
5. SE todas as tensões ausentes → PSU defeituosa.  
6. SE +5VSB presente mas PSU não liga → verificar botão Power e front panel header.

#### Comandos técnicos

N/A (teste elétrico físico)

### Execução da correção

#### Procedimento de correção (detalhado)

1. Desligar e desconectar todos os cabos AC.  
2. Descarregar capacitores residuais (pressionar Power 10s com cabo desconectado).  
3. Substituir PSU por unidade known-good de potência equivalente ou superior.  
4. Reconectar ATX 24-pin e CPU 8/4-pin.  
5. Testar ligamento.  
6. SE funcionar → PSU original confirmada defeituosa.  
7. SE não funcionar → avançar para diagnóstico de placa-mãe (NL-02).

### Resultado esperado

#### Critério de validação técnica

Ventoinhas giram, LEDs acendem, POST inicia.

#### Evidência de sucesso

Multímetro registra +12V (11.4-12.6V), +5V (4.75-5.25V), +3.3V (3.14-3.47V) sob carga. Beep de POST audível.

### Risco e impacto

#### Risco associado

Crítico

#### Impacto no sistema

Sistema totalmente inoperante. Risco de dano em cadeia se PSU entregar tensão fora de especificação.

### Origem

#### Fonte oficial

Intel ATX12V PSU Design Guide v2.53; IEC 62368-1 (Segurança Elétrica)

### Próximos passos

- Alcançado pelos nós [F01](../07-fluxo-sistemico.md#f01), [F02](../07-fluxo-sistemico.md#f02) do fluxo sistêmico
- É pré-requisito de [NL-02](nao-liga.md#nl-02), [SV-01](liga-sem-video.md#sv-01), [BS-02](bsod.md#bs-02), [DN-01](disco-nao-reconhecido.md#dn-01), [SA-01](superaquecimento.md#sa-01)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#nl-01--equipamento-não-liga-sem-leds-sem-ventoinhas-sem-sinal-de-vida)
- Critérios de encerramento: [Validação final por componente](../13-validacao-final.md)

---

## NL-02

### Identificação

#### Sintoma observado

PSU funcional (teste paperclip OK), mas sistema não liga ao conectar na placa-mãe.

#### Camada afetada

7 - Placa-mãe

#### Componente suspeito

Placa-mãe / VRM / Front Panel Header

#### Condição de ocorrência

PSU validada como funcional isoladamente. Sistema não responde ao botão Power.

### Pré-requisitos

#### Dependências

NL-01 (PSU validada)

#### Ordem de execução

2

#### Ferramentas oficiais

Multímetro; Lupa/Lanterna para inspeção visual; Chave de fenda (para curto do PWR_SW)

### Diagnóstico

#### Causa raiz

Curto-circuito na placa-mãe (VRM em curto, capacitor estufado), front panel header desconectado ou botão Power defeituoso. Ref: OEM Hardware Maintenance Manual (seção Power-on Circuit).

#### Método de diagnóstico (passo a passo)

1. Desconectar todos os periféricos (GPU, RAM, drives, USB).  
2. Manter apenas CPU + cooler + ATX 24-pin + CPU 8-pin.  
3. Curto-circuitar pinos PWR_SW no front panel header com chave de fenda.  
4. SE liga → front panel ou botão defeituoso.  
5. SE não liga → inspecionar visualmente capacitores e VRM por inchaço, vazamento ou queima.  
6. Testar com PSU known-good se disponível.

#### Comandos técnicos

N/A (teste físico)

### Execução da correção

#### Procedimento de correção (detalhado)

1. SE front panel defeituoso → reconectar ou substituir cabo/botão.  
2. SE capacitores estufados → placa-mãe condenada, substituir.  
3. SE VRM em curto → placa-mãe condenada.  
4. Documentar evidências fotográficas do defeito.

### Resultado esperado

#### Critério de validação técnica

Sistema liga e inicia POST ao curto-circuitar PWR_SW ou reconectar front panel.

#### Evidência de sucesso

LEDs de diagnóstico da placa-mãe acendem. Ventoinhas giram. Beep de POST.

### Risco e impacto

#### Risco associado

Alto

#### Impacto no sistema

Sistema inoperante. Possível perda de placa-mãe.

### Origem

#### Fonte oficial

Manual de Manutenção OEM (Dell/HP/Lenovo); ASUS/Gigabyte/MSI Motherboard User Manual (Front Panel Header pinout)

### Próximos passos

- Alcançado pelos nós [F02b](../07-fluxo-sistemico.md#f02b) do fluxo sistêmico
- Depende de [NL-01](nao-liga.md#nl-01) — execute-os antes
- É pré-requisito de [SV-01](liga-sem-video.md#sv-01)
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#nl-02--psu-funcional-teste-paperclip-ok-mas-sistema-não-liga-ao-conectar-na-placa-mãe)
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
| **Última verificação contra a fonte** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
