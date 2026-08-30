---
title: Guia operacional — Victoria (HDD/SSD)
description: Procedimento em 9 etapas para diagnosticar e reparar unidades de armazenamento, da preparação do ambiente à geração do relatório.
author: Edsilas
date: 2026-08-08
---

[Início](../../README.md) › [Opere as ferramentas](../../README.md#opere-as-ferramentas) › **Guia operacional — Victoria (HDD/SSD)**

# Guia operacional — Victoria (HDD/SSD)

> [!NOTE]
> Procedimento em 9 etapas para diagnosticar e reparar unidades de armazenamento, da preparação do ambiente à geração do relatório.

**Aplica-se a:** HDDs e SSDs — leitura de S.M.A.R.T., varredura de superfície e remapeamento

## Neste documento

- [Contexto](#contexto)
- [Escopo](#escopo)
- [Fora do escopo](#fora-do-escopo)
- [Relação com outros documentos](#relação-com-outros-documentos)
- [Etapas](#etapas)
- [Próximos passos](#próximos-passos)

## Contexto

Procedimento completo de uso do Victoria para diagnóstico de armazenamento, da preparação do ambiente à geração de relatório. Cada etapa registra também os erros possíveis, sua causa e a correção.

## Escopo

As 9 etapas do procedimento registradas na fonte, com todos os campos originais.

## Fora do escopo

Interpretação clínica dos resultados fora do que a fonte declara; procedimentos de outras ferramentas; critérios de validação por componente (ver documento 13).

## Relação com outros documentos

- [Índice de ferramentas](00-indice-ferramentas.md)
- [Validação final por componente](../13-validacao-final.md)
- [Índice de cenários](../10-cenarios/00-indice-cenarios.md)

---

## Etapas

| Nº | Fase do processo | Risco | Tempo estimado |
| --- | --- | --- | --- |
| [1](#etapa-1--preparação-do-ambiente) | Preparação do Ambiente | Crítico | 10 min |
| [2](#etapa-2--inicialização-do-software) | Inicialização do Software | Médio | 2 min |
| [3](#etapa-3--seleção-da-unidade-pass-api) | Seleção da Unidade (Pass API) | Alto | 1 min |
| [4](#etapa-4--análise-de-integridade-smart) | Análise de Integridade (S.M.A.R.T.) | Alto | 3 min |
| [5](#etapa-5--configuração-do-teste-de-superfície-diagnóstico) | Configuração do Teste de Superfície (Diagnóstico) | Crítico | 2 min |
| [6](#etapa-6--execução-da-varredura-scan) | Execução da Varredura (Scan) | Médio | 1h a 10h (depende do tamanho) |
| [7](#etapa-7--ação-de-reparo-lógico-remap) | Ação de Reparo Lógico (Remap) | Alto | Variável (1h+) |
| [8](#etapa-8--apagamento--sobrescrita-writeerase) | Apagamento / Sobrescrita (Write/Erase) | Crítico | 2h a 20h |
| [9](#etapa-9--validação-final-e-geração-de-relatórios) | Validação Final e Geração de Relatórios | Baixo | 5 min |

---

## Etapa 1 — Preparação do Ambiente

**Objetivo:** Garantir estabilidade de hardware/SO e isolamento da unidade.
**Risco:** Crítico | **Tempo estimado:** 10 min

### Ação exata a executar

1. Desativar suspensão/hibernação do Windows.
2. Fechar todos os programas em segundo plano.
3. Conectar o disco preferencialmente via SATA direto na placa-mãe.

**Caminho no software:** N/A (Ação no Sistema Operacional)

> [!NOTE]
> **Atalho de teclado:** `Win` + `R` > `powercfg.cpl`

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Energia: "Alto Desempenho".
  - Desligar HDDs: "Nunca".
  - Conexão: Porta SATA nativa (evitar adaptadores USB).
- **Verificação antes de executar:** Verificar se há no-break (UPS) ativo. Confirmar se os cabos SATA de dados e energia estão íntegros e firmes.

> [!TIP]
> **Boas práticas:** Isolar o disco executando o Victoria via ambiente WinPE (ex: Sergei Strelec) para evitar interferência do Windows Hospedeiro.
> **Alternativa segura:** Usar Live USB Linux (MHDD/HDAT2) se o Windows for instável.
> **Observações técnicas:** Conectar via USB insere latência do controlador ponte (SATA-to-USB), invalidando o tempo de resposta real dos blocos (ms) e impedindo comandos ATA diretos.

### Solução de problemas

**Possíveis erros:**
1. BSOD ou travamento durante o teste.
2. Desconexão repentina da unidade.

**Causa técnica:**
1. Conflito de I/O no barramento USB/SATA.
2. Queda de energia ou cabo frouxo.
3. SO tentou suspender a unidade em uso.

**Como identificar:**
1. Windows congela.
2. Disco some do Gerenciador de Discos.
3. Victoria reporta "Drive not ready".

**Como corrigir:**
`SE` erro de cabo `ENTÃO`:
1. Desligar PC.
2. Trocar cabo SATA/Energia.
3. Reiniciar.
`SE` erro de energia `ENTÃO`: Ligar em no-break.
`SE` erro de USB `ENTÃO`: Remover case e ligar via SATA.

**Validação pós-correção:** Reconectar unidade e verificar se a BIOS/UEFI reconhece o disco estavelmente sem quedas de comunicação.

> [!CAUTION]
> **Impacto se ignorado:** Corrupção irreversível do firmware do disco ou perda total de partições.

### Checklist de confirmação
- [ ] Energia configurada?
- [ ] Conexão direta SATA?
- [ ] Backup de dados críticos feito?

---

## Etapa 2 — Inicialização do Software

**Objetivo:** Carregar o Victoria com privilégios de baixo nível para acesso ao disco.
**Risco:** Médio | **Tempo estimado:** 2 min

### Ação exata a executar

Executar o executável com elevação de privilégios.

**Caminho no software:** Clique direito no ícone `Victoria.exe` > **Executar como administrador**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:** API Mode (Windows API) ativado por padrão. Nunca usar PIO Mode em Windows NT moderno.
- **Verificação antes de executar:** Verificar se a versão do Victoria é a mais recente compatível com a controladora (NVMe/SATA).

> [!TIP]
> **Boas práticas:** Sempre manter o log do Victoria ativado para auditoria posterior dos comandos enviados à controladora.
> **Alternativa segura:** Executar versão portátil a partir de um pendrive isolado.
> **Observações técnicas:** O Victoria requer acesso direto ao driver de armazenamento (`\\.\PhysicalDriveX`) contornando o sistema de arquivos lógico.

### Solução de problemas

**Possíveis erros:**
1. Erro "Privileged instruction".
2. Erro "PortTalk driver not loaded".

**Causa técnica:**
1. Falta de permissões de Administrador.
2. Incompatibilidade de arquitetura (32/64 bits) ou bloqueio de driver por Antivírus.

**Como identificar:**
Pop-up de erro vermelho no log inicial do programa informando acesso negado ao registrar drivers VCR.

**Como corrigir:**
`SE` sem privilégio `ENTÃO`: Fechar, clicar com botão direito e "Executar como Administrador".
`SE` bloqueio de AV `ENTÃO`: Adicionar exceção no Windows Defender/AV para a pasta do Victoria.

**Validação pós-correção:** Observar a aba "Log" inferior do Victoria. Deve conter a mensagem "Started for Admin" e enumerar os discos sem erros vermelhos.

> [!WARNING]
> **Impacto se ignorado:** Impossibilidade de ler o S.M.A.R.T. ou enviar comandos de reparo aos setores.

### Checklist de confirmação
- [ ] Executado como Admin?
- [ ] Antivírus não bloqueou?
- [ ] Aba Log sem erros iniciais?

---

## Etapa 3 — Seleção da Unidade (Pass API)

**Objetivo:** Isolar e focar o diagnóstico exclusivamente na unidade defeituosa/alvo.
**Risco:** Alto | **Tempo estimado:** 1 min

### Ação exata a executar

Selecionar a unidade correta no painel direito, verificando modelo e capacidade.

**Caminho no software:** Aba **Standard** > Painel Direito **Drive List**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Desmarcar Ignore OS a menos que seja um ambiente WinPE avançado. Confirmar checkbox "API" ativado.
- **Verificação antes de executar:** Verificar no Gerenciador de Discos (`diskmgmt.msc`) qual o número físico do disco (Disco 0, Disco 1) para cruzamento de dados.

> [!TIP]
> **Boas práticas:** Validar os 4 últimos dígitos do Serial Number do disco físico antes de prosseguir.
> **Alternativa segura:** Desconectar fisicamente todos os outros discos saudáveis para evitar erro humano.
> **Observações técnicas:** Em discos com falha de MFT/Tabela de partição, o Windows pode travar ao ler o disco, mas o Victoria (via API física) frequentemente consegue enxergá-lo.

### Solução de problemas

**Possíveis erros:**
1. Unidade errada selecionada.
2. Unidade não aparece na lista.

**Causa técnica:**
1. Desatenção do operador.
2. Firmware do disco corrompido (BSY state) ou falha catastrófica da controladora PCB.

**Como identificar:**
1. Capacidade incompatível exibida no painel esquerdo "Drive Info".
2. Lista vazia ou travada.

**Como corrigir:**
`SE` unidade errada `ENTÃO`: Clicar na unidade correta.
`SE` não aparece `ENTÃO`:
1. Clicar no botão Refresh (Ícone verde).
2. Verificar conexão física.
3. Checar Gerenciador de Dispositivos.

**Validação pós-correção:** Verificar painel esquerdo: Modelo Exato, Firmware, Serial Number, e LBA total devem corresponder perfeitamente à etiqueta do disco físico.

> [!WARNING]
> **Impacto se ignorado:** Selecionar o disco do SO e acidentalmente rodar "Erase", destruindo dados e sistema irrecuperavelmente.

### Checklist de confirmação
- [ ] Disco alvo é o correto?
- [ ] Serial Number bate?
- [ ] Status "Ready" verde exibido?

---

## Etapa 4 — Análise de Integridade (S.M.A.R.T.)

**Objetivo:** Avaliar a saúde física preexistente gravada na controladora do disco antes de estressá-lo.
**Risco:** Alto | **Tempo estimado:** 3 min

### Ação exata a executar

Solicitar leitura dos atributos S.M.A.R.T. e avaliar os valores RAW críticos.

**Caminho no software:** Aba **SMART** > Botão **Get SMART**

> [!NOTE]
> **Atalho de teclado:** `F9`

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Ativar Auto update (opcional).
- **Verificação antes de executar:** Certificar-se de que o disco não está em uso por outro processo (I/O).

> [!TIP]
> **Boas práticas:** Salvar a leitura S.M.A.R.T. em um arquivo de texto para criar um baseline de comparação após a tentativa de reparo.
> **Alternativa segura:** SE S.M.A.R.T. falhar totalmente, pular para clonagem de hardware.
> **Observações técnicas:** Focar nos IDs críticos: 05 (Reallocated Sectors), C5 (Current Pending Sectors), C6 (Uncorrectable Sectors). Valores RAW diferentes de 0 nestes IDs indicam degradação física.

### Solução de problemas

**Possíveis erros:**
1. "SMART return error".
2. Atributos invisíveis/bloqueados.
3. Status BAD imediato.

**Causa técnica:**
1. Controladora USB não repassa comandos ATA pass-through.
2. Firmware corrompido.
3. Disco em colapso mecânico iminente.

**Como identificar:**
1. Mensagem "Error reading SMART" no Log.
2. Tabela vazia.
3. Itens 05, C5, C6 em vermelho.

**Como corrigir:**
`SE` USB não lê `ENTÃO`: Ligar via SATA.
`SE` atributos vermelhos (Ex: 05 > 0) `ENTÃO`: Parar diagnóstico, risco de morte do disco. Iniciar backup de imagem raw (`ddrescue`) imediatamente.

**Validação pós-correção:** Verificar se a tabela exibe os IDs de 01 a C8. O status global superior deve mudar de cinza para "GOOD" ou "BAD".

> [!WARNING]
> **Impacto se ignorado:** Executar teste de superfície em um disco com falha mecânica severa (Head Crash) destruirá os pratos e os dados definitivamente.

### Checklist de confirmação
- [ ] Tabela S.M.A.R.T. gerada?
- [ ] ID 05 analisado?
- [ ] ID C5 analisado?
- [ ] Status geral interpretado?

---

## Etapa 5 — Configuração do Teste de Superfície (Diagnóstico)

**Objetivo:** Parametrizar a varredura lógica dos setores (LBA) sem alteração de dados.
**Risco:** Crítico | **Tempo estimado:** 2 min

### Ação exata a executar

Configurar os parâmetros de leitura não-destrutiva de ponta a ponta do disco.

**Caminho no software:** Aba **Test**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Ação: Read (Leitura).
  - Modo: Ignore (Apenas diagnóstico, não tenta consertar).
  - Block Size: 2048 (padrão).
  - Timeout: 1000 ms (1 seg) a 10000 ms.
- **Verificação antes de executar:** Confirmar de forma absoluta que a opção "Erase" e "Write" NÃO estão marcadas.

> [!TIP]
> **Boas práticas:** Executar um teste prévio de 1 minuto e pausar, apenas para verificar a resposta de velocidade do barramento.
> **Alternativa segura:** Usar o modo Verify em vez de Read em SSDs, pois testa a resposta da controladora sem transferir carga útil pelo barramento.
> **Observações técnicas:** A varredura por LBA começa em 0 (borda externa do prato, mais rápida) e vai até o LBA máximo (borda interna, mais lenta). A queda de velocidade ao longo do teste em HDDs mecânicos é normal física.

### Solução de problemas

**Possíveis erros:**
1. Timeout muito baixo gera falsos positivos.
2. Tamanho do bloco incompatível com o disco.

**Causa técnica:**
1. Discos antigos/lentos (5400 RPM) ou via USB podem exceder 1000ms naturalmente em áreas densas.

**Como identificar:**
Quantidade irreal de blocos laranja/vermelhos desde o início do teste, mesmo em disco novo.

**Como corrigir:**
`SE` falsos positivos ocorrendo `ENTÃO`: Aumentar o Timeout para 3000ms ou 5000ms no painel direito inferior.

**Validação pós-correção:** Iniciar o teste e verificar se a curva de leitura no gráfico é condizente com o throughput esperado (ex: 120MB/s em HDD, 500MB/s em SSD).

> [!CAUTION]
> **Impacto se ignorado:** Se configurado como "Write" nesta fase, todos os dados do disco começarão a ser sobrescritos com zeros (apagamento irreversível).

### Checklist de confirmação
- [ ] Opção "Read" marcada?
- [ ] Opção "Ignore" marcada?
- [ ] LBA Start é 0?

---

## Etapa 6 — Execução da Varredura (Scan)

**Objetivo:** Mapear a saúde de cada bloco (setor) em tempo de resposta (latência).
**Risco:** Médio | **Tempo estimado:** 1h a 10h (depende do tamanho)

### Ação exata a executar

Iniciar o escaneamento e monitorar ativamente a matriz térmica de cores.

**Caminho no software:** Aba **Test** > Botão **Scan**

> [!NOTE]
> **Atalho de teclado:** `F4`

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Ativar aba Grid para ver o mapa visual. Manter Grid size padrão.
- **Verificação antes de executar:** Garantir que o Windows não iniciará atualizações ou varreduras de antivírus simultâneas.

> [!TIP]
> **Boas práticas:** Não deixar o computador sozinho em varreduras de discos problemáticos. Monitorar os primeiros 10%.
> **Alternativa segura:** Interromper (Stop) aos primeiros 50 erros consecutivos para proteger a mecânica.
> **Observações técnicas:** A legenda de cores é vital:
> - Cinza claro (<25ms): Excelente.
> - Cinza escuro (<100ms): Bom.
> - Verde (<250ms): Aceitável.
> - Laranja (<1000ms): Lento/Degradando.
> - Vermelho (>1000ms): Crítico/Quase Bad Block.
> - Azul/X (Err): Bad Block confirmado.

### Solução de problemas

**Possíveis erros:**
1. Teste congela (hang).
2. Queda drástica de MB/s para 0.0.
3. Múltiplos blocos azuis (Err / UNC).

**Causa técnica:**
1. Cabeça de leitura presa/morta.
2. Setor físico destruído (Uncorrectable Error - UNC), causando timeout na controladora.

**Como identificar:**
1. Velocidade cai a 0.
2. Log exibe "Block XXXXXX Error: UNCR".
3. Ruídos de cliques metálicos no HDD.

**Como corrigir:**
`SE` blocos Err (Azul) aparecerem em massa OU velocidade zerar OU disco estalar `ENTÃO`: Clicar imediatamente em Stop. O disco tem dano físico mecânico (Head failure). Recuperação apenas em laboratório limpo (Cleanroom).

**Validação pós-correção:** Interromper o processo; se os cliques pararem e o disco responder no OS, isolar a unidade para envio a especialista.

> [!WARNING]
> **Impacto se ignorado:** Continuar varrendo um disco com dano mecânico riscará o prato magnético permanentemente, impedindo qualquer recuperação de dados forense.

### Checklist de confirmação
- [ ] Cores monitoradas?
- [ ] Nenhum ruído anormal?
- [ ] Velocidade constante?

---

## Etapa 7 — Ação de Reparo Lógico (Remap)

**Objetivo:** Forçar a controladora do disco a remapear os Bad Blocks (C5) para a área de reserva física.
**Risco:** Alto | **Tempo estimado:** Variável (1h+)

### Ação exata a executar

Caso o Scan diagnóstico localize setores Vermelhos/Azuis E o backup já tenha sido feito, reexecutar forçando correção.

**Caminho no software:** Aba **Test** > Selecionar ação **Remap** > Botão **Scan**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Ação: Read + Remap. Pode ser útil limitar o range de LBA (Start LBA e End LBA) apenas para a área defeituosa mapeada na Etapa 06 para economizar tempo.
- **Verificação antes de executar:** REGRA DE OURO: Confirmar que todos os dados importantes do disco já foram copiados. O Remap pode corromper arquivos onde o setor reside.

> [!TIP]
> **Boas práticas:** Direcionar o Remap apenas para as faixas (LBA) onde os erros foram encontrados na Etapa 06, inserindo os valores manualmente.
> **Alternativa segura:** Executar `chkdsk /R` do Windows como alternativa de nível de sistema de arquivos (menos profundo, mas mais amigável a dados).
> **Observações técnicas:** O Remap usa o comando ATA nativo para mover o endereço LBA defeituoso para a G-List (Growth Defect List). Quando a G-List lota, o HD não aceita mais Remaps.

### Solução de problemas

**Possíveis erros:**
1. Falha no Remap ("Remap Error").
2. Esgotamento da G-List (área de reserva cheia).

**Causa técnica:**
1. Setor tão danificado que a firmware não consegue ler o código ECC para remapear.
2. O disco já excedeu seu limite físico de setores reserva de fábrica.

**Como identificar:**
O Log mostrará repetidas mensagens: "Block XXXXXX Remap Error" após tentar corrigir um bloco azul.

**Como corrigir:**
`SE` Remap falha sistematicamente `ENTÃO`:
1. Tentar ação Refresh em vez de Remap para tentar reviver a carga magnética do setor.
2. Se falhar, o dano é físico puro e não há conserto via software.

**Validação pós-correção:** Executar um novo Scan (Modo Ignore) apenas na zona afetada (Start/End LBA). O bloco azul anterior deve agora aparecer como cinza claro, pois foi trocado fisicamente pelo firmware.

> [!WARNING]
> **Impacto se ignorado:** Tentar ler dados do setor corrompido continuará travando o SO (congelamentos do Windows Explorer, BSODs).

### Checklist de confirmação
- [ ] Backup garantido?
- [ ] LBA Start/End definidos?
- [ ] Ação REMAP selecionada?
- [ ] Log acompanhado?

---

## Etapa 8 — Apagamento / Sobrescrita (Write/Erase)

**Objetivo:** Destruir dados e forçar um reset magnético de setores relutantes (Zero-fill).
**Risco:** Crítico | **Tempo estimado:** 2h a 20h

### Ação exata a executar

Caso o Remap falhe, e o disco NÃO contenha dados úteis, aplicar zeros a todos os setores para obrigar o remapeamento brutal.

**Caminho no software:** Aba **Test** > Selecionar ação **Write** ou **Erase** > Botão **Scan**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Ação: Write (Zero fill completo). Usar Erase se quiser focar apenas nos setores detectados como ruins pelo timeout.
- **Verificação antes de executar:** ATENÇÃO CRÍTICA: Esta etapa apagará irrecuperavelmente a Tabela de Partição, MBR/GPT e TODOS os arquivos do disco.

> [!TIP]
> **Boas práticas:** Nunca usar em SSDs rotineiramente (desgasta os chips NAND inutilmente). Para SSDs, usar o utilitário do fabricante para "Secure Erase".
> **Alternativa segura:** Ao invés de usar Victoria para Write, usar o `diskpart > clean all`, que é nativo e menos suscetível a conflitos de VCR.
> **Observações técnicas:** O Write (Zero Fill) apaga os dados apagando a carga magnética anterior. Ele força o ECC da controladora a resetar o estado do setor. Muito útil para remover "Soft Bad Blocks" causados por queda de energia ou CRC lógico.

### Solução de problemas

**Possíveis erros:**
1. Acesso negado ("Access Denied").
2. Travamento I/O persistente.

**Causa técnica:**
1. O Windows está bloqueando a gravação crua porque o disco tem partições ativas montadas.
2. Controladora eletrônica em colapso completo.

**Como identificar:**
1. Log exibe "Error writing block... Access Denied".
2. Victoria exibe pop-up exigindo desligamento do MBR.

**Como corrigir:**
`SE` Access Denied `ENTÃO`:
1. Ir na aba Standard.
2. Botão MBR OFF (ou limpar partição no diskpart).
3. Voltar e repetir Write. (Requer ambiente WinPE na maioria dos casos para não travar o Windows).

**Validação pós-correção:** Recriar a tabela de partição (`diskmgmt.msc`), formatar e rodar um último Scan (Read/Ignore). O disco deve estar sem "Pending Sectors" (C5 = 0 no S.M.A.R.T.).

> [!CAUTION]
> **Impacto se ignorado:** Sobrescrever o disco errado resultará em perda total e permanente de dados.

### Checklist de confirmação
- [ ] ZERO dados importantes na unidade?
- [ ] Confirmou letra/serial?
- [ ] Função Write selecionada?

---

## Etapa 9 — Validação Final e Geração de Relatórios

**Objetivo:** Documentar o estado final, cruzar dados S.M.A.R.T e definir o futuro da unidade.
**Risco:** Baixo | **Tempo estimado:** 5 min

### Ação exata a executar

1. Salvar o log de eventos.
2. Re-ler o S.M.A.R.T. para confirmar alterações.
3. Tomar decisão lógica de uso.

**Caminho no software:** Aba **SMART** > **Get SMART** | Abaixo: Botão direito no log > **Save to file**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Formato de log: `.txt`.
- **Verificação antes de executar:** Checar se a varredura (Scan) chegou ao LBA final 100% (borda inferior da tela) sem ser cancelada manualmente.

> [!TIP]
> **Boas práticas:** Exportar logs com o Serial Number do HD no nome do arquivo (ex: `Log_WD10EZEX_WD-WCC3F1234.txt`).
> **Alternativa segura:** Tirar print screen das abas SMART e Test com a tecla `PrtScn` caso o salvamento falhe.
> **Observações técnicas:** Lógica de decisão pós-procedimento:
> - S.M.A.R.T = GOOD e Erros = 0 -> Uso normal.
> - 05 (Reallocated) aumentou muito, mas estável -> Usar apenas para backup secundário/arquivos não críticos.
> - Erros persistirem -> Sucata/Lixo eletrônico.

### Solução de problemas

**Possíveis erros:**
Discrepância de S.M.A.R.T. (Status não atualiza imediatamente).

**Causa técnica:**
O disco pode precisar de um ciclo de energia (Power Cycle) para o firmware recalcular as tabelas P-List/G-List e atualizar os atributos.

**Como identificar:**
S.M.A.R.T. ainda exibe C5 alto mesmo após dezenas de remapeamentos bem-sucedidos.

**Como corrigir:**
`SE` atributos não atualizaram `ENTÃO`:
1. Desligar computador.
2. Ligar novamente (Cold Boot).
3. Abrir Victoria e ler S.M.A.R.T. novamente.

**Validação pós-correção:** Comparar S.M.A.R.T. Inicial (Etapa 4) com o Final. SE C5 (Pending) converteu para 05 (Reallocated) E novos scans não geram erros, o reparo lógico teve sucesso.

> [!WARNING]
> **Impacto se ignorado:** Não salvar log impossibilita comprovar a saúde do HD para clientes (se for o caso) ou prever a taxa de degradação futura.

### Checklist de confirmação
- [ ] Log salvo em arquivo?
- [ ] SMART final comparado?
- [ ] Decisão de descarte ou reuso tomada?

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| terminou o teste e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |
| quer o procedimento do sintoma que motivou o teste | [Índice de cenários](../10-cenarios/00-indice-cenarios.md) |
| precisa de outra ferramenta | [Índice de ferramentas](00-indice-ferramentas.md) |

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
