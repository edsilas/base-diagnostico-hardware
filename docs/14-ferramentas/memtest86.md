<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `REF_MemTest86`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Opere as ferramentas](../../README.md#opere-as-ferramentas) › **Guia operacional — MemTest86**

# Guia operacional — MemTest86

> Procedimento em 10 etapas para testar memória fora do sistema operacional, com os critérios de decisão sobre o destino dos módulos.


**Aplica-se a:** Módulos DIMM e SO-DIMM — teste em ambiente bootável, com XMP ativo

## Neste documento

- [Etapas](#etapas)
- [Etapa 1 — Criação da Mídia Bootável](#etapa-1--criação-da-mídia-bootável)
- [Etapa 2 — Configuração de BIOS/UEFI](#etapa-2--configuração-de-biosuefi)
- [Etapa 3 — Seleção de Processamento (SMP)](#etapa-3--seleção-de-processamento-smp)
- [Etapa 4 — Execução da Bateria Padrão (Pass 1)](#etapa-4--execução-da-bateria-padrão-pass-1)
- [Etapa 5 — Teste de Row Hammer (Teste 13)](#etapa-5--teste-de-row-hammer-teste-13)
- [Etapa 6 — Interpretação de Endereços de Erro](#etapa-6--interpretação-de-endereços-de-erro)
- [Etapa 7 — Isolamento Físico (Swapping)](#etapa-7--isolamento-físico-swapping)
- [Etapa 8 — Teste de Sobrecarga XMP (Overclock)](#etapa-8--teste-de-sobrecarga-xmp-overclock)
- [Etapa 9 — Geração de Relatório HTML (Prova Técnica)](#etapa-9--geração-de-relatório-html-prova-técnica)
- [Etapa 10 — Encerramento e Restauração de Boot](#etapa-10--encerramento-e-restauração-de-boot)
- [Critérios de decisão pós-MemTest86](#critérios-de-decisão-pós-memtest86)
- [Próximos passos](#próximos-passos)

## Contexto

Procedimento completo de teste de memória com MemTest86, da criação da mídia bootável à restauração do boot, incluindo os critérios de decisão sobre o destino dos módulos testados.

## Escopo

As 10 etapas do procedimento registradas na fonte, mais o bloco de critérios de decisão pós-teste presente na última linha da aba.

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
| [1](#etapa-1--criação-da-mídia-bootável) | Criação da Mídia Bootável | Baixo | 5 min |
| [2](#etapa-2--configuração-de-biosuefi) | Configuração de BIOS/UEFI | Médio | 2 min |
| [3](#etapa-3--seleção-de-processamento-smp) | Seleção de Processamento (SMP) | Baixo | 1 min |
| [4](#etapa-4--execução-da-bateria-padrão-pass-1) | Execução da Bateria Padrão (Pass 1) | Crítico | 30m - 2h |
| [5](#etapa-5--teste-de-row-hammer-teste-13) | Teste de Row Hammer (Teste 13) | Médio | 1h+ |
| [6](#etapa-6--interpretação-de-endereços-de-erro) | Interpretação de Endereços de Erro | Alto | 5 min |
| [7](#etapa-7--isolamento-físico-swapping) | Isolamento Físico (Swapping) | Crítico | 15 min/pente |
| [8](#etapa-8--teste-de-sobrecarga-xmp-overclock) | Teste de Sobrecarga XMP (Overclock) | Médio | 4h+ (Madrugada) |
| [9](#etapa-9--geração-de-relatório-html-prova-técnica) | Geração de Relatório HTML (Prova Técnica) | Baixo | 1 min |
| [10](#etapa-10--encerramento-e-restauração-de-boot) | Encerramento e Restauração de Boot | Alto | 2 min |

---

## Etapa 1 — Criação da Mídia Bootável

### Objetivo da etapa

Criar um ambiente de execução isolado do Windows para acesso direto ao hardware

### Ação exata a executar

1. Baixar o MemTest86 USB Image.  
2. Executar imageUSB.exe.  
3. Gravar no Pen Drive.

### Caminho no software

Windows > imageUSB.exe

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Selecionar "Write image to USB drive".  

Zeroar MBR: Sim.

### Verificação antes de executar

O Pen Drive será formatado. Salvar dados antes.

### Possíveis erros

1. Erro de escrita ("Write Error").  
2. Pen Drive não boota depois.

### Causa técnica do erro

1. Pen Drive falso ou corrompido.  
2. Partição GPT não criada corretamente pelo imageUSB.

### Como identificar o erro

1. Barra vermelha no imageUSB.  
2. BIOS não reconhece o dispositivo como "UEFI: USB".

### Como corrigir (passo a passo)

SE falha na escrita ENTÃO:  
1. Trocar Pen Drive.  
2. Tentar porta USB 2.0 (mais estável para criação de mídia).

### Validação pós-correção

O Pen Drive deve aparecer no Explorer com nome "EFI" e conter pasta /EFI/BOOT.

### Risco

Baixo

### Impacto se ignorado

Sem a mídia correta, impossível rodar o teste fora do SO.

### Tempo estimado

5 min

### Observações técnicas

O MemTest86 v10+ requer UEFI. Para PCs antigos (Legacy BIOS), deve-se usar a versão v4.3.7 (que vem junto no pacote, mas é limitada).

> [!IMPORTANT]
> **A v4 deixou de acompanhar o pacote.** Segundo o histórico de versões do desenvolvedor, o
> MemTest86 v4 (BIOS) foi retirado das imagens de boot: as versões atuais são **exclusivamente
> UEFI**, e o pacote não é mais de boot duplo. Para máquinas com BIOS legado, a v4 precisa ser
> baixada à parte, na área de versões antigas do site do PassMark. Se o equipamento não oferece
> boot UEFI, baixar apenas o pacote atual deixa você sem ferramenta.
>
> Verificado na documentação do desenvolvedor — ver
> [Fontes](../references/fontes.md#verificações-independentes-realizadas).

### Boas práticas

Usar Pen Drive de baixa capacidade (4GB/8GB) é suficiente e formata mais rápido.

### Alternativa segura

Ventoy (Multiboot), mas imageUSB nativo é mais garantido.

### Checklist de confirmação

- [ ] ImageUSB executado?  
- [ ] Partição EFI criada?  
- [ ] Pen Drive reconhecido?

---

## Etapa 2 — Configuração de BIOS/UEFI

### Objetivo da etapa

Permitir que o código não-assinado (ou assinado por terceiros) execute antes do Kernel do Windows

### Ação exata a executar

1. Entrar na BIOS.  
2. Desativar Fast Boot.  
3. Ajustar ordem de Boot.

### Caminho no software

BIOS > Boot Menu

### Atalho de teclado

Del ou F2

### Configurações recomendadas

Secure Boot: Disabled (recomendado para evitar bloqueio de chaves antigas).  

Boot Mode: UEFI Only.

### Verificação antes de executar

Confirmar se o perfil XMP/DOCP da memória está ATIVADO para testar na velocidade real de uso.

### Possíveis erros

1. Tela preta ao tentar bootar.  
2. Boot direto para o Windows ignorando USB.

### Causa técnica do erro

1. Incompatibilidade de vídeo GOP (Graphics Output Protocol).  
2. Prioridade de Boot incorreta.

### Como identificar o erro

O PC ignora o pen drive ou trava no logo da placa-mãe.

### Como corrigir (passo a passo)

SE pular o USB ENTÃO: Usar "Boot Override" (F8/F11/F12) e selecionar a partição "UEFI: [Nome do Pen Drive]".

### Validação pós-correção

A tela inicial azul do MemTest86 deve carregar com um timer de 10 segundos.

### Risco

Médio

### Impacto se ignorado

Testar RAM sem XMP ativo é inútil, pois esconde instabilidade de voltagem/frequência.

### Tempo estimado

2 min

### Observações técnicas

O Secure Boot da Microsoft às vezes revoga assinaturas de ferramentas de diagnóstico. Desativar temporariamente é o padrão ouro.

### Boas práticas

Testar primeiro em Stock (JEDEC), depois ativar XMP se passar.

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Secure Boot OFF?  
- [ ] XMP Ativo?  
- [ ] Boot Override USB?

---

## Etapa 3 — Seleção de Processamento (SMP)

### Objetivo da etapa

Definir se o teste usará todos os núcleos da CPU (Rápido) ou um só (Compatível)

### Ação exata a executar

Na tela inicial, configurar o modo de CPU antes do início automático.

### Caminho no software

Menu Principal > Config > CPU Selection

### Atalho de teclado

C

### Configurações recomendadas

Padrão: Parallel (All CPUs).  

Se travar: Single CPU.

### Verificação antes de executar

Verificar se o processador é estável termicamente (o teste Parallel esquenta muito).

### Possíveis erros

1. Travamento (Freeze) imediato no Teste 1.  
2. Reboot aleatório.

### Causa técnica do erro

1. BIOS antiga com implementação SMP bugada.  
2. Fonte de alimentação não aguenta carga de CPU + RAM simultânea.

### Como identificar o erro

O contador de tempo no canto superior direito para de rodar.

### Como corrigir (passo a passo)

SE travar no Parallel ENTÃO:  
1. Reiniciar.  
2. Entrar em Config.  
3. Selecionar Single CPU. (O teste será 4x mais lento, mas estável).

### Validação pós-correção

O teste deve iniciar e as barras de progresso devem se mover.

### Risco

Baixo

### Impacto se ignorado

Travamentos de SMP mascaram o erro real da memória.

### Tempo estimado

1 min

### Observações técnicas

O modo Parallel estressa o controlador de memória (IMC) dentro da CPU, testando também a comunicação CPU<->RAM.

### Boas práticas

Monitorar a temperatura da CPU na tela do MemTest86. Se passar de 90°C, abortar.

### Alternativa segura

Modo Round Robin (Alterna CPUs).

### Checklist de confirmação

- [ ] Modo Parallel selecionado?  
- [ ] Temperatura monitorada?  
- [ ] Timer rodando?

---

## Etapa 4 — Execução da Bateria Padrão (Pass 1)

### Objetivo da etapa

Rodar os 13 algoritmos padrão para detectar 95% dos erros comuns

> [!NOTE]
> **Conferência com a documentação do desenvolvedor.** O manual do MemTest86 (PassMark) descreve a
> bateria padrão como os testes **0 a 13 — quatorze testes**, e não treze. A numeração começa em
> zero, o que explica a diferença: o último teste é o de número 13, o
> [*Hammer Test*](#etapa-5--teste-de-row-hammer-teste-13). Nada muda na execução — a etapa continua
> sendo deixar o Pass 1 completar —, mas a contagem correta é quatorze.

### Ação exata a executar

Deixar o teste rodar automaticamente até completar 100% do "Pass 1".

### Caminho no software

N/A (Automático)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Não mexer no mouse/teclado durante a execução.

### Verificação antes de executar

Confirmar que o número de pentes e tamanho total (ex: 16GB) está correto no topo da tela.

### Possíveis erros

1. Erros vermelhos aparecendo na lista inferior.  
2. Tela corrompida (artefatos).

### Causa técnica do erro

1. Célula de memória defeituosa (bit flip).  
2. Memória de vídeo compartilhada (iGPU) usando RAM corrompida.

### Como identificar o erro

Linhas vermelhas com "Error" incrementando o contador.

### Como corrigir (passo a passo)

SE aparecer 1 erro que seja ENTÃO: O pente está condenado. Não existe "conserto" de software para RAM física. Abortar e ir para Etapa 07.

### Validação pós-correção

O indicador "Pass" deve mudar de 0 para 1 sem erros.

### Risco

Crítico

### Impacto se ignorado

Um único bit errado pode corromper o registro do Windows ou arquivos do sistema silenciosamente.

### Tempo estimado

30m - 2h

### Observações técnicas

Testes críticos: Teste 6 (Block Move) e Teste 8 (Random Number). São os que mais pegam falhas.

### Boas práticas

Se o tempo for curto, rodar apenas Teste 6 e 8 manualmente (Menu Test Selection).

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Total RAM correto?  
- [ ] Pass % avançando?  
- [ ] Zero erros vermelhos?

---

## Etapa 5 — Teste de Row Hammer (Teste 13)

### Objetivo da etapa

Verificar vulnerabilidade a interferência eletromagnética entre células vizinhas

### Ação exata a executar

Garantir que o Teste 13 (Hammer Test) seja executado e não pulado.

### Caminho no software

Test Selection > Test 13

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Executar isoladamente se houver suspeita de instabilidade apenas em carga pesada.

### Verificação antes de executar

Esse teste demora muito em módulos de 32GB+.

### Possíveis erros

1. Erros massivos apenas no Teste 13.  
2. PC reinicia.

### Causa técnica do erro

1. Módulos de RAM sem proteção contra Row Hammer (comum em DDR3/DDR4 antigas).  
2. Refresh Rate da RAM configurado errado na BIOS.

### Como identificar o erro

O log mostra "Hammer Test" com milhares de erros, mas outros testes zerados.

### Como corrigir (passo a passo)

SE erro no Hammer ENTÃO: Atualizar BIOS (geralmente melhora o algoritmo de Refresh) ou trocar por memória de marca premium.

### Validação pós-correção

Passar no Teste 13 garante que a RAM é robusta para servidores e cargas intensas.

### Risco

Médio

### Impacto se ignorado

Vulnerabilidade de segurança e corrupção de dados em bancos de dados de alta frequência.

### Tempo estimado

1h+

### Observações técnicas

O "Row Hammer" consiste em acessar uma linha de memória repetidamente para ver se a carga elétrica "vaza" para a linha vizinha, mudando um bit (0 virar 1).

### Boas práticas

Em DDR5, o ECC on-die mitiga isso, mas não elimina.

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Teste 13 concluído?  
- [ ] Note 1: "Vulnerable"?  
- [ ] Note 2: Erros reais?

---

## Etapa 6 — Interpretação de Endereços de Erro

### Objetivo da etapa

Entender se o erro é em um slot específico ou aleatório

### Ação exata a executar

Analisar a coluna Address e Bits (Máscara de erro) nas linhas vermelhas.

### Caminho no software

Painel Inferior Error List

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Anotar o endereço mais baixo (ex: 4096MB) e o mais alto com erro.

### Verificação antes de executar

Ter o esquema da placa-mãe (qual slot é o #1, #2).

### Possíveis erros

1. Erros em endereços aleatórios em todo o range.  
2. Erros sempre no mesmo bit (ex: 0x00000004).

### Causa técnica do erro

1. Problema de voltagem (VDIMM) ou Controlador de Memória (CPU).  
2. Problema físico em um chip de memória específico do pente.

### Como identificar o erro

Coluna "Bits" mostra sempre o mesmo padrão hexadecimal.

### Como corrigir (passo a passo)

SE erros em todo lugar ENTÃO: Suspeitar de Placa-mãe ou CPU. SE erros localizados ENTÃO: Suspeitar do pente de memória.

### Validação pós-correção

Diagnóstico diferencial para não trocar a peça errada.

### Risco

Alto

### Impacto se ignorado

Trocar a memória quando o defeito é na placa-mãe (slot sujo/solda fria).

### Tempo estimado

5 min

### Observações técnicas

Se o erro ocorre logo no início (0MB - 1024MB), geralmente o sistema nem boota. Erros altos (>8GB) aparecem só quando o PC está cheio.

### Boas práticas

Tirar foto da tela com o celular para análise posterior dos endereços hexadecimais.

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Endereços anotados?  
- [ ] Padrão de bits identificado?  
- [ ] Faixa de MB definida?

---

## Etapa 7 — Isolamento Físico (Swapping)

### Objetivo da etapa

Identificar qual pente de memória é o culpado em sistemas com múltiplos pentes

### Ação exata a executar

1. Desligar PC.  
2. Remover todos os pentes exceto o do Slot A2.  
3. Retestar.

### Caminho no software

Hardware Físico

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Testar um pente por vez no mesmo slot primário.

### Verificação antes de executar

Descarregar estática do corpo (tocar no gabinete) antes de tocar na RAM.

### Possíveis erros

1. PC não liga com um pente específico.  
2. Todos os pentes dão erro no Slot A2.

### Causa técnica do erro

1. Pente morto.  
2. Slot da placa-mãe defeituoso (pinos tortos no socket da CPU).

### Como identificar o erro

O erro persiste mesmo trocando a memória.

### Como corrigir (passo a passo)

SE erro em todos os pentes no Slot A2 ENTÃO: Testar no Slot B2. SE persistir, limpar contatos ou re-assentar a CPU (socket torto).

### Validação pós-correção

Encontrar o "Pente Assassino" e removê-lo do kit.

### Risco

Crítico

### Impacto se ignorado

Usar um kit Dual Channel onde um lado está podre causará BSODs aleatórias.

### Tempo estimado

15 min/pente

### Observações técnicas

Sempre testar um pente de cada vez para validação de RMA (Garantia). O fabricante exige saber qual stick falhou.

### Boas práticas

Marcar os pentes com fita crepe (#1, #2) para não misturar.

### Alternativa segura

Borracha branca escolar nos contatos (cuidado com resíduos).

### Checklist de confirmação

- [ ] Teste individual feito?  
- [ ] Slot validado?  
- [ ] Pente ruim marcado?

---

## Etapa 8 — Teste de Sobrecarga XMP (Overclock)

### Objetivo da etapa

Validar se a memória suporta a velocidade anunciada na etiqueta

### Ação exata a executar

Ativar perfil XMP/EXPO na BIOS e rodar 4 Passes completos.

### Caminho no software

BIOS > AI Tweaker / OC

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

XMP Profile 1 (Frequência Máxima).

### Verificação antes de executar

Verificar se a voltagem (1.35v ou 1.4v) foi aplicada corretamente pela BIOS.

### Possíveis erros

1. Erros apenas com XMP ativo.  
2. Sistema não boota (Training fail).

### Causa técnica do erro

1. O chip de memória é ruim de binagem (silicon lottery) ou a placa-mãe não aguenta a frequência.  
2. Controlador de memória da CPU fraco.

### Como identificar o erro

MemTest passa limpo em Stock (2133/4800) mas enche de erros em XMP (3200/6000).

### Como corrigir (passo a passo)

SE erro no XMP ENTÃO: Aumentar voltagem VDIMM em +0.02v OU reduzir frequência manualmente (ex: de 3200 para 3000).

### Validação pós-correção

Sistema estável em alta performance.

### Risco

Médio

### Impacto se ignorado

Vender PC Gamer que trava em jogos pesados porque o XMP é instável.

### Tempo estimado

4h+ (Madrugada)

### Observações técnicas

"XMP é Overclock". Não é garantido que funcione em qualquer CPU. O MemTest86 é o juiz final se o OC é estável.

### Boas práticas

Rodar teste "Overnight" (deixar a noite toda) para validar estabilidade térmica do XMP.

### Alternativa segura

Usar frequências JEDEC padrão (perda de FPS).

### Checklist de confirmação

- [ ] XMP Ativado?  
- [ ] Voltagem conferida?  
- [ ] 4 Passes sem erro?

---

## Etapa 9 — Geração de Relatório HTML (Prova Técnica)

### Objetivo da etapa

Documentar o teste para garantia ou cliente (Fundamental para RMA)

### Ação exata a executar

Ao fim do teste, salvar o relatório na partição do Pen Drive.

### Caminho no software

Botão Save Report ao finalizar

### Atalho de teclado

S

### Configurações recomendadas

Formato: HTML.

### Verificação antes de executar

O MemTest86 Free grava na partição EFI do pen drive. O Pro grava logs detalhados.

### Possíveis erros

1. Arquivo não salvo.  
2. Pen Drive em modo somente leitura.

### Causa técnica do erro

1. Esquecimento do técnico.  
2. Falha no sistema de arquivos FAT32.

### Como identificar o erro

Ao plugar no Windows, a pasta EFI/BOOT não tem o arquivo .html.

### Como corrigir (passo a passo)

SE falha ao salvar ENTÃO: Tirar foto legível da tela mostrando "Pass: 4, Errors: 0".

### Validação pós-correção

Arquivo MemTest86-Report.html visível no navegador.

### Risco

Baixo

### Impacto se ignorado

Sem prova, o fabricante da memória pode recusar a troca em garantia.

### Tempo estimado

1 min

### Observações técnicas

O relatório contém o Serial Number dos pentes (SPD Data), provando que aquele pente específico foi testado.

### Boas práticas

Salvar o relatório com o nome do cliente.

### Alternativa segura

Foto da tela (válida, mas menos profissional).

### Checklist de confirmação

- [ ] Relatório salvo?  
- [ ] Serial Number confere?  
- [ ] Resultado "PASS" verde?

---

## Etapa 10 — Encerramento e Restauração de Boot

### Objetivo da etapa

Devolver o PC ao estado bootável normal do Windows

### Ação exata a executar

1. Remover Pen Drive.  
2. Entrar na BIOS.  
3. Reativar Fast Boot/Secure Boot (Opcional).

### Caminho no software

BIOS > Boot

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Secure Boot: Enabled.  

Boot Option #1: Windows Boot Manager.

### Verificação antes de executar

Verificar se o Windows carrega normalmente após o teste.

### Possíveis erros

1. Windows entra em reparo automático.  
2. BitLocker pede chave de recuperação.

### Causa técnica do erro

1. Mudança de configuração SATA/NVMe (raro mexer nisso para MemTest).  
2. Alteração do Secure Boot ou TPM triggerou proteção.

### Como identificar o erro

Tela azul de BitLocker.

### Como corrigir (passo a passo)

SE BitLocker pedir chave ENTÃO: Inserir a chave salva (Etapa 25 do AIDA64) ou reverter configurações de BIOS exatamente como estavam.

### Validação pós-correção

Windows Desktop carrega sem erros.

### Risco

Alto

### Impacto se ignorado

Cliente ficar trancado fora dos dados por BitLocker.

### Tempo estimado

2 min

### Observações técnicas

Alterações na configuração de memória (tamanho) podem fazer o Windows demorar mais no primeiro boot ("Memory Training"). Avisar o cliente.

### Boas práticas

Deixar o XMP ativo se passou no teste.

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Pen Drive removido?  
- [ ] Windows iniciou?  
- [ ] BitLocker OK?

---

## Critérios de decisão pós-MemTest86

> Este bloco ocupa, na planilha de origem, a última linha da aba, na coluna `Nº da Etapa`. **Não é uma etapa do procedimento** — é um critério de decisão. Título literal na fonte: **Critérios de Decisão Pós-MemTest86**. Reproduzido integralmente abaixo.

0 Erros após 4 Passes: Memória 100% Saudável. Pode vender/usar.  
1 a 10 Erros (Aleatórios): Memória instável. Tentar limpar contatos, aumentar levemente a voltagem (DDR4 1.35v -> 1.36v) ou reduzir clock. Retestar. Se persistir = Lixo.  
Milhares de Erros (Sequenciais/Bit Stuck): Chip de memória morto. Lixo imediato. Não serve nem para escritório.  
Erros apenas no Teste 13 (Hammer): Vulnerável. Uso aceitável para PC doméstico simples (web/office), inaceitável para Servidor, Workstation ou Gamer Hardcore.

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| terminou o teste e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |
| quer o procedimento do sintoma que motivou o teste | [Índice de cenários](../10-cenarios/00-indice-cenarios.md) |
| precisa de outra ferramenta | [Índice de ferramentas](00-indice-ferramentas.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `REF_MemTest86` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
