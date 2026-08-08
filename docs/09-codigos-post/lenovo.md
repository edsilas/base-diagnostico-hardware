<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Lenovo (SmartBeep / beep binário)**

# Códigos POST — Lenovo (SmartBeep / beep binário)

> Fichas completas dos códigos de POST da família Lenovo (SmartBeep / beep binário), com causa raiz, diagnóstico, correção e critério de validação.


**Aplica-se a:** Equipamentos com BIOS `Proprietário Lenovo`

## Neste documento

- [POST-44 — Melodia variável](#post-44--melodia-variável)
- [POST-45 — 0110 (Binário)](#post-45--0110-binário)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos, na fonte, ao fabricante de BIOS `Proprietário Lenovo`. Cada ficha reproduz integralmente os campos registrados na planilha de origem.

## Escopo

Os 2 código(s) da família `Proprietário Lenovo` presentes na fonte, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação, risco e fonte oficial.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-44 — Melodia variável

**Fabricante BIOS:** Proprietário Lenovo  
**Fabricante / plataforma:** Lenovo — ThinkPad / ThinkCentre  
**Tipo de sinal:** SmartBeep (Melodia)  
**Código:** `Melodia variável`

### Identificação

#### Interpretação oficial

Lenovo PC Diagnostics — Código sonoro interpretável via app

#### Componente afetado

Variável

#### Camada de diagnóstico

Variável

#### Fase POST

Variável

### Diagnóstico

#### Causa raiz (documentação oficial)

Lenovo ThinkPads modernos usam o sistema SmartBeep: uma sequência melódica que pode ser decodificada pelo app 'Lenovo PC Diagnostics' no smartphone. O app ouve o padrão sonoro e traduz em código de erro específico.

#### Condições que geram o erro

Variável — depende do código decodificado pelo app.

#### Método de diagnóstico técnico

1. Instalar app 'Lenovo PC Diagnostics' no smartphone (iOS/Android).  
2. Aproximar o smartphone do sistema ao ligar.  
3. O app captura a melodia e exibe o código de erro com descrição.  
4. Seguir procedimento específico do código identificado.

#### Ferramentas oficiais

App 'Lenovo PC Diagnostics' (smartphone iOS/Android)

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Baixar e instalar 'Lenovo PC Diagnostics' no smartphone.  
2. Abrir o app e selecionar 'SmartBeep'.  
3. Ligar o sistema ThinkPad/ThinkCentre.  
4. Posicionar o smartphone próximo ao speaker.  
5. O app identifica o padrão e exibe:  

   — Código de erro.  
   — Componente afetado.  
   — Procedimento sugerido.  
6. Seguir procedimento indicado pelo app.  
7. Se não resolver: consultar Lenovo PSREF e HMM (Hardware Maintenance Manual).

### Resultado esperado

#### Critério de validação

App identifica código e procedimento resolve o erro. POST completa. Lenovo Diagnostics (F10) sem erros.

### Risco e origem

#### Risco / criticidade

Variável

#### Fonte oficial

Lenovo SmartBeep Documentation / Lenovo HMM

### Próximos passos

- Camada declarada: `Variável` — valor composto ou variável; ver [Taxonomia de camadas](../03-taxonomia-camadas.md)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## POST-45 — 0110 (Binário)

**Fabricante BIOS:** Proprietário Lenovo  
**Fabricante / plataforma:** Lenovo — ThinkPad  
**Tipo de sinal:** Beep Sonoro (Binário)  
**Código:** `0110 (Binário)`

### Identificação

#### Interpretação oficial

Security Chip (TPM) Error — Falha no chip de segurança TPM

#### Componente afetado

TPM (Trusted Platform Module)

#### Camada de diagnóstico

Camada 5: Chipset / Motherboard

#### Fase POST

Security Init

### Diagnóstico

#### Causa raiz (documentação oficial)

O chip TPM (Trusted Platform Module) não responde ou apresenta erro. Em ThinkPads, o TPM é usado para criptografia BitLocker, autenticação, e funções de segurança empresarial.

#### Condições que geram o erro

1. Firmware do TPM corrompido.  
2. TPM desabilitado incorretamente.  
3. Chip TPM com defeito físico.  
4. Após atualização de BIOS que resetou configuração TPM.

#### Método de diagnóstico técnico

1. Acessar BIOS Setup (F1 na tela de POST).  
2. Navegar até Security → Security Chip.  
3. Verificar estado do TPM.  
4. Tentar Clear Security Chip.  
5. Se TPM discreto (não fTPM): chip pode estar defeituoso.

#### Ferramentas oficiais

BIOS Setup (F1) / Lenovo BIOS Update

### Execução da correção

#### Procedimento de correção (passo a passo)

1. Acessar BIOS (F1 ao ligar).  
2. Navegar: Security → Security Chip.  
3. Se opção disponível: Security Chip → Clear.  
4. Salvar e reiniciar.  
5. Se persistir:  

   a. Atualizar BIOS para versão mais recente (site Lenovo).  
   b. Após update: repetir clear do TPM.  
6. Se TPM morto:  

   a. Desabilitar Security Chip no BIOS (se possível).  
   b. ATENÇÃO: BitLocker ativo = dados podem ficar inacessíveis. Fazer backup da recovery key ANTES.  
7. Se chip discreto com defeito: reparo em nível de componente ou troca da placa.

### Resultado esperado

#### Critério de validação

TPM reconhecido no BIOS. BitLocker funcional (se aplicável). tpm.msc no Windows reporta TPM pronto.

### Risco e origem

#### Risco / criticidade

Alto

#### Fonte oficial

Lenovo ThinkPad HMM / Lenovo BIOS Guide

### Próximos passos

- Ficha da camada: [Camada 5: Chipset / Motherboard](../08-diagnostico-por-camada.md#camada-5--chipset--motherboard)
- Outros códigos do mesmo componente ou risco: [Índices cruzados](../18-indices-cruzados.md)
- Como chegar até este código: [Fluxo de diagnóstico POST](../06-fluxo-post.md)

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou o código aqui | [Índice de códigos POST](00-indice-codigos.md) — catálogo completo |
| suspeita que o código tem outro significado | [Ambiguidade de códigos](../11-ambiguidades.md) |
| quer saber o que testar naquele subsistema | [Diagnóstico por camada](../08-diagnostico-por-camada.md) |
| aplicou a correção e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
