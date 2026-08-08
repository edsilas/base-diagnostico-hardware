<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → abas `TABELA_PRINCIPAL` e `INDICE_CENARIOS`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Cenário — Disco não reconhecido**

# Cenário — Disco não reconhecido

> Procedimento completo para o cenário Disco não reconhecido: pré-requisitos, diagnóstico, correção, resultado esperado e riscos.


**Aplica-se a:** Equipamentos que concluem o POST — falhas percebidas em uso

## Neste documento

- [Entrada rápida (registro do índice de cenários)](#entrada-rápida-registro-do-índice-de-cenários)
- [DN-01](#dn-01)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas de diagnóstico do cenário `Disco não reconhecido` conforme registrado na fonte. Cada ficha corresponde a um ID da tabela principal e reproduz integralmente seus campos.

## Escopo

IDs DN-01 — sintoma, causa raiz, método de diagnóstico, comandos, correção, validação, risco e fonte oficial.

## Fora do escopo

Outros cenários; catálogo de códigos POST; guias detalhados das ferramentas.

## Relação com outros documentos

- [Índice de cenários](00-indice-cenarios.md)
- [Fluxo de diagnóstico sistêmico](../07-fluxo-sistemico.md)
- [Correlações entre camadas](../12-correlacoes.md)
- [Validação final por componente](../13-validacao-final.md)

---

## Entrada rápida (registro do índice de cenários)

- **Cenário (fonte):** Disco não reconhecido
- **IDs relacionados:** DN-01
- **Camada primária:** 5 - Armazenamento
- **Primeiro teste:** Verificar cabos → Outra porta SATA → BIOS (AHCI) → Outro sistema
- **Ferramentas necessárias:** Cabos SATA known-good, Victoria

---

## DN-01

### Identificação

#### Sintoma observado

Disco não aparece na BIOS/UEFI nem no Gerenciador de Dispositivos.

#### Camada afetada

5 - Armazenamento

#### Componente suspeito

Disco HDD/SSD / Cabo SATA-Dados / Cabo SATA-Energia / Porta SATA/M.2

#### Condição de ocorrência

Disco recém-instalado ou disco existente que parou de ser detectado. Sem presença na BIOS.

### Pré-requisitos

#### Dependências

NL-01 (energia presente e estável)

#### Ordem de execução

10

#### Ferramentas oficiais

Victoria (se disco detectado parcialmente); Gerenciador de Discos (diskmgmt.msc); BIOS/UEFI Setup; Cabos SATA known-good

### Diagnóstico

#### Causa raiz

Falha de comunicação no barramento: cabo de dados ou energia desconectado/defeituoso, porta SATA/M.2 desativada na BIOS, controladora PCB do disco em curto (BSY state), ou disco em falha catastrófica. Ref: SATA-IO Specification Rev 3.5; NVMe Specification Rev 2.0.

#### Método de diagnóstico (passo a passo)

1. Verificar conexão física: cabo SATA dados + cabo SATA energia (ambos necessários).  
2. Substituir cabo de dados por known-good.  
3. Testar em outra porta SATA da placa-mãe.  
4. Verificar BIOS: SATA Configuration → modo deve ser AHCI (não IDE/RAID se não intencional).  
5. Para M.2 NVMe: verificar se o slot suporta NVMe (nem todos os M.2 suportam).  
6. Conectar disco em outro sistema known-good.  
7. SE disco detectado em outro sistema → porta/controladora da placa original defeituosa.  
8. SE disco não detectado em nenhum sistema → PCB ou motor em falha.

#### Comandos técnicos

diskmgmt.msc  
diskpart → list disk  
Get-PhysicalDisk (PowerShell)  
wmic diskdrive list brief

### Execução da correção

#### Procedimento de correção (detalhado)

1. Substituir cabo SATA dados.  
2. Substituir cabo SATA energia (testar outro conector da PSU).  
3. Testar em outra porta SATA.  
4. Para M.2: verificar especificação do slot (SATA vs NVMe) no manual da placa.  
5. SE disco com PCB queimada → substituir disco. Dados recuperáveis apenas via laboratório.  
6. SE porta da placa-mãe defeituosa → usar outra porta ou adicionar controladora PCIe SATA.

### Resultado esperado

#### Critério de validação técnica

Disco aparece na BIOS com modelo/capacidade corretos. Gerenciador de Discos exibe o disco. Victoria lê S.M.A.R.T. sem erros.

#### Evidência de sucesso

BIOS lista o disco. diskmgmt.msc mostra volume. S.M.A.R.T. status GOOD.

### Risco e impacto

#### Risco associado

Alto

#### Impacto no sistema

Dados inacessíveis. SO não boota se disco de sistema.

### Origem

#### Fonte oficial

SATA-IO Serial ATA Revision 3.5; NVM Express Specification Rev 2.0; Manual OEM da Placa-mãe (M.2 Compatibility Chart)

### Próximos passos

- Alcançado pelos nós [F10](../07-fluxo-sistemico.md#f10) do fluxo sistêmico
- Depende de [NL-01](nao-liga.md#nl-01) — execute-os antes
- Comando desta ficha na [referência consolidada de comandos](../19-comandos.md#dn-01--disco-não-aparece-na-biosuefi-nem-no-gerenciador-de-dispositivos)
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
| **Versão da documentação** | `doc-1.4.0` |
