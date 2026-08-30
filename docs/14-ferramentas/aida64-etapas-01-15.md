---
title: Guia operacional — AIDA64 (etapas 01 a 15)
description: Etapas 1 a 15 do procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e auditoria.
author: Edsilas
date: 2026-08-08
---

[Início](../../README.md) › [Opere as ferramentas](../../README.md#opere-as-ferramentas) › **Guia operacional — AIDA64 (etapas 01 a 15)**

# Guia operacional — AIDA64 (etapas 01 a 15)

> [!NOTE]
> Etapas 1 a 15 do procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e auditoria.

**Aplica-se a:** Sistemas que carregam o Windows — sensores, stress test e relatórios

## Neste documento

- [Contexto](#contexto)
- [Escopo](#escopo)
- [Fora do escopo](#fora-do-escopo)
- [Relação com outros documentos](#relação-com-outros-documentos)
- [Etapas](#etapas)
- [Próximos passos](#próximos-passos)

## Contexto

Procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e auditoria. Esta parte cobre a faixa de etapas indicada no título.

## Escopo

As etapas 1 a 15 registradas na fonte, com todos os campos originais.

## Fora do escopo

Interpretação clínica dos resultados fora do que a fonte declara; procedimentos de outras ferramentas; critérios de validação por componente (ver documento 13).

## Relação com outros documentos

- [Índice de ferramentas](00-indice-ferramentas.md)
- [Validação final por componente](../13-validacao-final.md)
- [Índice de cenários](../10-cenarios/00-indice-cenarios.md)

---

> [!NOTE]
> Este guia foi dividido em três arquivos **apenas pela numeração das etapas de origem** (1–15, 16–30, 31–45). A divisão é organizacional; a fonte não define grupos.

## Etapas

| Nº | Fase do processo | Risco | Tempo estimado |
| --- | --- | --- | --- |
| [1](#etapa-1--inicialização-e-licenciamento) | Inicialização e Licenciamento | Baixo | 2 min |
| [2](#etapa-2--configuração-de-sensores-monitoring) | Configuração de Sensores (Monitoring) | Médio | 5 min |
| [3](#etapa-3--preparação-do-teste-de-estabilidade) | Preparação do Teste de Estabilidade | Baixo | 3 min |
| [4](#etapa-4--execução-do-stress-test-fase-térmica) | Execução do Stress Test (Fase Térmica) | Crítico | 10-30 min |
| [5](#etapa-5--análise-de-voltagens-e-estabilidade) | Análise de Voltagens e Estabilidade | Alto | Durante Etapa 04 |
| [6](#etapa-6--benchmark-de-memória-e-cache) | Benchmark de Memória e Cache | Médio | 5 min |
| [7](#etapa-7--benchmark-de-gpgpu-opcional) | Benchmark de GPGPU (Opcional) | Baixo | 3 min |
| [8](#etapa-8--geração-de-relatório-técnico-auditoria) | Geração de Relatório Técnico (Auditoria) | Baixo | 2 min |
| [9](#etapa-9--análise-comparativa-de-desempenho) | Análise Comparativa de Desempenho | Baixo | 5 min |
| [10](#etapa-10--configuração-de-sensorpanel-monitoramento-persistente) | Configuração de SensorPanel (Monitoramento Persistente) | Baixo | 15 min |
| [11](#etapa-11--configuração-de-alertas-automáticos) | Configuração de Alertas Automáticos | Médio | 5 min |
| [12](#etapa-12--encerramento-e-limpeza-do-ambiente) | Encerramento e Limpeza do Ambiente | Baixo | 1 min |
| [13](#etapa-13--diagnóstico-de-monitor-display) | Diagnóstico de Monitor (Display) | Médio (Saúde) | 5 min |
| [14](#etapa-14--benchmark-de-disco-performance) | Benchmark de Disco (Performance) | Alto | 10 min |
| [15](#etapa-15--análise-profunda-de-dram-spd) | Análise Profunda de DRAM (SPD) | Baixo | 2 min |

---

## Etapa 1 — Inicialização e Licenciamento

**Objetivo:** Garantir acesso total às funções de engenharia sem limitações de trial.
**Risco:** Baixo | **Tempo estimado:** 2 min

### Ação exata a executar

1. Executar `aida64.exe`.
2. Inserir chave de produto (Engineer) se não ativado.
3. Desativar atualizações automáticas durante diagnósticos.

**Caminho no software:** **Ajuda** > **Sobre** > **Digitar Chave do Produto**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Versão *Portable* (em Pen Drive). Idioma Português (Brasil).
- **Verificação antes de executar:** Verificar se a versão do AIDA64 é compatível com o chipset da placa-mãe (ex: Z790, X670) e SO.

> [!TIP]
> **Boas práticas:** Usar versão *Portable* para não sujar o registro do Windows do cliente.
> **Alternativa segura:** Usar HWiNFO64 apenas para leitura de sensores (não faz stress test/relatório igual).

### Solução de problemas

**Possíveis erros:**
1. Valores ocultos `[TRIAL VERSION]`.
2. Crash ao carregar "Scanning PCI".

**Causa técnica:**
1. Chave inválida ou software não registrado.
2. Conflito de driver de baixo nível (`Kernaldrv.sys`).

**Como identificar:**
1. O relatório exibe asteriscos em vez de dados.
2. Software fecha ou trava na tela de splash.

**Como corrigir:**
`SE` travamento na carga `ENTÃO`:
1. Criar atalho do executável.
2. Adicionar flag `/SAFE` no destino.
3. Executar novamente ignorando sensores instáveis.

**Validação pós-correção:** Verificar menu **Ajuda** > **Sobre**. Deve constar "Licensed to..." e não "Evaluation".

> [!WARNING]
> **Impacto se ignorado:** Dados críticos ocultados impedem diagnóstico preciso ou geração de relatório profissional.

### Checklist de confirmação
- [ ] Licença Ativa?
- [ ] Versão atualizada?
- [ ] Carregou sem travar?

---

## Etapa 2 — Configuração de Sensores (Monitoring)

**Objetivo:** Calibrar leitura térmica e voltagens antes de estressar o hardware.
**Risco:** Médio | **Tempo estimado:** 5 min

### Ação exata a executar

Habilitar e configurar o Painel OSD para monitoramento em tempo real fora da janela principal.

**Caminho no software:** **Arquivo** > **Preferências** > **Monitoramento de Hardware** > **OSD**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Check: Mostrar Painel OSD.
  - Itens: Temperaturas (CPU Package, GPU Hotspot), Vcore, +12V, Fan RPM.
- **Verificação antes de executar:** Confirmar se os sensores da placa-mãe (Super I/O) são detectados corretamente na aba **Computador** > **Sensores**.

> [!TIP]
> **Boas práticas:** Customizar as cores do OSD: Vermelho para Temp, Azul para Voltagem, Verde para Rotação.
> **Alternativa segura:** Usar a aba Sensor padrão se o OSD falhar.
> **Observações técnicas:** A leitura "CPU Diode" é mais precisa que "CPU Socket". Em GPUs modernas, monitorar "Hotspot" é vital.

### Solução de problemas

**Possíveis erros:**
1. Leituras absurdas (ex: 128°C ou -50°C).
2. Sensores ausentes.

**Causa técnica:**
1. Erro de interpretação do chip sensor ou deslocamento de TjMax.
2. SMBus bloqueado por outro software (ex: RGB Fusion, iCUE).

**Como identificar:**
Valores estáticos que não mudam ou valores fora da física possível.

**Como corrigir:**
`SE` conflito SMBus `ENTÃO`:
1. Fechar todo software de RGB/Controle de Fan.
2. Reiniciar AIDA64.
3. Ir em **Preferências** > **Estabilidade** > Ativar *Low-level PCI access*.

**Validação pós-correção:** Verificar se a temperatura oscila (sobe/desce) conforme uso leve do mouse.

> [!WARNING]
> **Impacto se ignorado:** Iniciar stress test sem leitura confiável pode queimar componentes por superaquecimento não detectado.

### Checklist de confirmação
- [ ] OSD Visível na tela?
- [ ] Temps flutuando?
- [ ] Softwares RGB fechados?

---

## Etapa 3 — Preparação do Teste de Estabilidade

**Objetivo:** Selecionar componentes específicos para isolar falhas (CPU vs RAM vs FPU).
**Risco:** Baixo | **Tempo estimado:** 3 min

### Ação exata a executar

Abrir a ferramenta de estabilidade e selecionar apenas os checkboxes pertinentes ao objetivo.

**Caminho no software:** **Ferramentas** > **Teste de Estabilidade do Sistema**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Para Máximo Calor: *Stress FPU* apenas.
  - Para RAM: *Stress System Memory* apenas.
  - Para Uso Geral: *Stress CPU* + *FPU* + *Cache* + *System Memory*.
- **Verificação antes de executar:** Fechar todos os apps em segundo plano. Garantir que o plano de energia do Windows está em "Alto Desempenho".

> [!TIP]
> **Boas práticas:** Nunca marcar *Stress Local Disks* junto com CPU/RAM, pois o lag do disco mascarará instabilidade do processador.
> **Alternativa segura:** Testar um componente por vez (Isolamento).
> **Observações técnicas:** Stress FPU usa instruções AVX/AVX-512, gerando calor extremo irrealista para uso diário, mas ideal para testar refrigeração.

### Solução de problemas

**Possíveis erros:**
1. Congelamento imediato ao abrir a janela.
2. Gráficos não plotam dados.

**Causa técnica:**
1. Driver de vídeo instável ou falta de memória virtual.
2. Erro na renderização do gráfico GDI+.

**Como identificar:**
Janela abre mas fica branca (Não Responde) ou linhas do gráfico não aparecem.

**Como corrigir:**
`SE` travar ao abrir `ENTÃO`: Atualizar driver de vídeo e aumentar arquivo de paginação do Windows.

**Validação pós-correção:** As abas "Temperatures", "Cooling Fans" e "Voltages" devem mostrar linhas vivas avançando para a direita.

> [!WARNING]
> **Impacto se ignorado:** Testar componentes errados (ex: Stress Disk em SSD) desgasta hardware sem necessidade.

### Checklist de confirmação
- [ ] Checkboxes corretos?
- [ ] Gráficos ativos?
- [ ] Botão Start visível?

---

## Etapa 4 — Execução do Stress Test (Fase Térmica)

**Objetivo:** Validar a eficiência do cooler/pasta térmica e curvas de ventoinha.
**Risco:** Crítico | **Tempo estimado:** 10-30 min

### Ação exata a executar

Clicar em **Start** e monitorar IMEDIATAMENTE a linha de "Throttling" e temperaturas.

**Caminho no software:** Janela **System Stability Test** > Botão **Start**

> [!NOTE]
> **Atalho de teclado:** Informação não identificada na fonte analisada.

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Monitorar aba **Statistics** (valores Min/Max/Avg) em tempo real.
- **Verificação antes de executar:** Ficar com a mão sobre o botão Stop ou atalho de emergência.

> [!TIP]
> **Boas práticas:** Limpar os logs anteriores (Clear) antes de iniciar para não misturar dados de idle com load.
> **Alternativa segura:** Parar se a temperatura ambiente estiver muito alta (>35°C) sem ar condicionado.
> **Observações técnicas:** O AIDA64 estressa o sistema de forma linear. Diferente do Prime95, é mais seguro, mas ainda letal para cooling defeituoso.

### Solução de problemas

**Possíveis erros:**
1. Superaquecimento instantâneo (>95°C em 2s).
2. Throttling (Estrangulamento) detectado.

**Causa técnica:**
1. Cooler mal encaixado ou bomba de Watercooler parada.
2. VRM da placa-mãe sobrecarregado ou CPU atingindo TJMax.

**Como identificar:**
Texto vermelho "CPU Throttling - Overheating Detected!" aparece no gráfico. Linha verde de throttling sobe.

**Como corrigir:**
`SE` Temp > 95°C ou Throttling > 5% `ENTÃO`:
1. Clicar **Stop** imediatamente.
2. Verificar montagem do cooler/pasta térmica.
3. Ajustar curva de fans na BIOS.

**Validação pós-correção:** O sistema deve estabilizar uma temperatura (ex: 80°C) e manter o clock sem baixar a frequência (Throttling 0%).

> [!CAUTION]
> **Impacto se ignorado:** Danos permanentes ao silício se proteções da placa-mãe falharem (raro, mas possível em hardware antigo).

### Checklist de confirmação
- [ ] Botão Start clicado?
- [ ] Olhos na Temp?
- [ ] Olhos no Throttling?
- [ ] Coolers aceleraram?

---

## Etapa 5 — Análise de Voltagens e Estabilidade

**Objetivo:** Verificar se a fonte de alimentação (PSU) suporta a carga máxima sem Vdrop (queda de tensão).
**Risco:** Alto | **Tempo estimado:** Durante Etapa 04

### Ação exata a executar

Durante o teste de stress (Etapa 04), alternar para a aba **Voltages** e observar a linha de +12V, +5V e Vcore.

**Caminho no software:** Janela **System Stability Test** > Aba **Voltages**

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Tolerância ATX: +/- 5%.
  - +12V deve ficar entre 11.4V e 12.6V.
  - Vcore deve ser estável (ex: sem cair de 1.2v para 0.8v bruscamente).
- **Verificação antes de executar:** Conhecer a voltagem nominal do processador (VID).

> [!TIP]
> **Boas práticas:** Não confiar cegamente em sensores de placas-mãe low-end.
> **Alternativa segura:** Usar testador de fonte físico.
> **Observações técnicas:** Monitoramento via software tem margem de erro. O ideal é usar multímetro, mas queda abrupta no gráfico é indicativo forte de falha.

### Solução de problemas

**Possíveis erros:**
1. Reinicialização súbita (Black screen).
2. Queda drástica na linha 12V.

**Causa técnica:**
1. Fonte desarmando por OCP (Over Current Protection).
2. Fonte de baixa qualidade ou capacitor de saída estufado.

**Como identificar:**
PC desliga e liga sozinho. Gráfico mostra linha 12V mergulhando antes do corte.

**Como corrigir:**
`SE` reinício espontâneo `ENTÃO`: Substituir Fonte de Alimentação (PSU) imediatamente. O sistema está instável eletricamente.

**Validação pós-correção:** Voltagens permanecem dentro da margem de 5% durante 100% de carga.

> [!WARNING]
> **Impacto se ignorado:** Fonte ruim sob estresse pode explodir ou queimar placa-mãe/GPU junto com ela.

### Checklist de confirmação
- [ ] Linha 12V estável?
- [ ] Sem reboot?
- [ ] Vcore constante?

---

## Etapa 6 — Benchmark de Memória e Cache

**Objetivo:** Validar performance e latência da RAM (XMP/EXPO) e Cache L1/L2/L3.
**Risco:** Médio | **Tempo estimado:** 5 min

### Ação exata a executar

Executar o benchmark completo de memória e latência.

**Caminho no software:** **Ferramentas** > **Benchmark de Cache e Memória**

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Clicar no botão **Start Benchmark** (centro).
- **Verificação antes de executar:** Fechar absolutamente tudo (Navegadores, Discord, Steam) para não contaminar a latência.

> [!TIP]
> **Boas práticas:** Salvar screenshot do resultado (Botão Save) para comparar antes e depois de overclock.
> **Alternativa segura:** Teste MemTest86 via boot para diagnóstico de erro de bit físico (AIDA mede performance, não integridade física profunda).

### Solução de problemas

**Possíveis erros:**
1. Tela azul (BSOD) durante o teste.
2. Resultados muito abaixo do esperado (Ex: Latência 100ns em DDR4).

**Causa técnica:**
1. Timing de memória instável ou XMP falho.
2. Memória em Single Channel ou slot incorreto.

**Como identificar:**
1. Código de erro BSOD: `MEMORY_MANAGEMENT`.
2. Largura de banda metade do esperado.

**Como corrigir:**
`SE` BSOD `ENTÃO`:
1. Entrar na BIOS.
2. Desativar XMP/DOCP.
3. Retestar em stock (JEDEC).

`SE` Single Channel `ENTÃO`: Verificar slots (A2/B2 geralmente).

**Validação pós-correção:** Resultado de "Latency" em ns deve ser condizente com a tecnologia (DDR4 ~60ns, DDR5 ~70-80ns).

> [!WARNING]
> **Impacto se ignorado:** Corrupção de dados silenciosa se a RAM estiver instável.

### Checklist de confirmação
- [ ] Apps fechados?
- [ ] Dual Channel confirmado?
- [ ] Sem BSOD?

---

## Etapa 7 — Benchmark de GPGPU (Opcional)

**Objetivo:** Testar capacidade de computação da Placa de Vídeo e Processador juntos.
**Risco:** Baixo | **Tempo estimado:** 3 min

### Ação exata a executar

Executar teste de carga computacional gráfica.

**Caminho no software:** **Ferramentas** > **Benchmark de GPGPU**

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Selecionar as GPUs corretas se houver multi-GPU.
- **Verificação antes de executar:** Instalar drivers de vídeo oficiais (Studio ou Game Ready) atualizados.

> [!TIP]
> **Boas práticas:** Comparar "Memory Read/Write" da GPU com especificações do fabricante.
> **Alternativa segura:** Furmark (mais agressivo, mas não mede computação).

### Solução de problemas

**Possíveis erros:**
1. Driver de vídeo para e recupera ("O driver parou de responder").
2. Artefatos na tela.

**Causa técnica:**
1. Instabilidade de clock/voltagem da GPU.
2. VRAM defeituosa ou superaquecimento da memória de vídeo.

**Como identificar:**
Tela pisca preta, AIDA64 trava, ou aparecem quadrados coloridos na tela.

**Como corrigir:**
`SE` driver resetar `ENTÃO`: Reduzir overclock da GPU (MSI Afterburner) ou verificar temperatura de Hotspot.

**Validação pós-correção:** Conclusão do teste com valores preenchidos em todas as células (Gflops, IOPS).

> [!WARNING]
> **Impacto se ignorado:** Apenas crash de driver, raramente danifica hardware se temperaturas estiverem controladas.

### Checklist de confirmação
- [ ] Driver atualizado?
- [ ] Sem artefatos visuais?
- [ ] Teste concluído?

---

## Etapa 8 — Geração de Relatório Técnico (Auditoria)

**Objetivo:** Documentar todo o hardware e software para entrega ao cliente ou inventário.
**Risco:** Baixo | **Tempo estimado:** 2 min

### Ação exata a executar

Criar um relatório completo em formato legível e universal.

**Caminho no software:** **Relatório** > **Assistente de Relatórios**

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Perfil: Todas as páginas ou Somente Hardware.
  - Formato: HTML (Melhor visualização) ou MHTML (Arquivo único com imagens).
- **Verificação antes de executar:** Definir nome do arquivo padronizado (`Cliente_Data_PC.html`).

> [!TIP]
> **Boas práticas:** Personalizar o cabeçalho do relatório com o logo da sua empresa em **Preferências** > **Relatório** > **Cabeçalho**.
> **Alternativa segura:** Print Screen das telas principais (amador, mas funcional).
> **Observações técnicas:** O relatório inclui chaves de licença de software (Windows/Office) na seção "Licenças". Cuidado ao compartilhar.

### Solução de problemas

**Possíveis erros:**
1. Relatório incompleto.
2. Travamento durante a geração ("DMI Query").

**Causa técnica:**
1. Permissões de usuário ou versão Trial.
2. DMI da BIOS corrompido.

**Como identificar:**
O arquivo final tem 2KB ou o software congela na barra de progresso.

**Como corrigir:**
`SE` travar no DMI `ENTÃO`: Ir em **Preferências** > **Estabilidade** > Desativar *DMI Support*.

**Validação pós-correção:** Abrir o HTML no navegador e verificar se o resumo (Sumário) contém CPU, Placa-mãe, RAM e Discos listados corretamente.

> [!WARNING]
> **Impacto se ignorado:** Falta de documentação profissional desvaloriza o serviço técnico.

### Checklist de confirmação
- [ ] Formato HTML?
- [ ] Todas as páginas?
- [ ] Logo da empresa incluso?
- [ ] Salvo em local seguro?

---

## Etapa 9 — Análise Comparativa de Desempenho

**Objetivo:** Validar se o hardware entrega a performance esperada para o modelo (Benchmark sintético).
**Risco:** Baixo | **Tempo estimado:** 5 min

### Ação exata a executar

Executar benchmarks de CPU (Queen, PhotoWorxx) e FPU (Julia, Mandel) e comparar no ranking.

**Caminho no software:** Menu Lateral **Benchmarks** > Duplo clique no teste desejado > Botão **Start**

> [!NOTE]
> **Atalho de teclado:** `F5` (Atualiza)

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Priorizar CPU Queen (Branch Prediction) e FPU Julia (Ponto Flutuante).
- **Verificação antes de executar:** Garantir que nenhum outro software pesado esteja rodando.

> [!TIP]
> **Boas práticas:** Clicar com botão direito na barra de resultados > **Results** para ver detalhes numéricos precisos.
> **Alternativa segura:** Usar Cinebench R23 (foca apenas em renderização, AIDA foca em instruções puras).
> **Observações técnicas:** CPU PhotoWorxx é sensível à velocidade da RAM. FPU Mandel usa instruções vetoriais pesadas.

### Solução de problemas

**Possíveis erros:**
1. Score muito abaixo da referência (ex: i9 pontuando como i5).
2. Sistema trava durante o cálculo.

**Causa técnica:**
1. Throttling térmico ou Power Limit (PL1/PL2) mal configurado na BIOS.
2. Instabilidade de AVX.

**Como identificar:**
O resultado aparece destacado em negrito muito abaixo de processadores similares na lista.

**Como corrigir:**
`SE` pontuação baixa `ENTÃO`:
1. Monitorar temperatura durante o teste.
2. Se temperatura OK, verificar na BIOS se "Intel SpeedStep" ou "AMD Cool'n'Quiet" estão limitando o clock.

**Validação pós-correção:** O resultado deve estar dentro de uma margem de erro de 5% dos modelos idênticos listados no banco de dados do AIDA64.

> [!WARNING]
> **Impacto se ignorado:** Entregar um PC montado que subutiliza o hardware pago pelo cliente (gargalo lógico).

### Checklist de confirmação
- [ ] Teste Queen executado?
- [ ] Teste Julia executado?
- [ ] Score condizente com modelo?

---

## Etapa 10 — Configuração de SensorPanel (Monitoramento Persistente)

**Objetivo:** Criar um painel visual personalizado para monitoramento contínuo pós-diagnóstico.
**Risco:** Baixo | **Tempo estimado:** 15 min

### Ação exata a executar

Habilitar e configurar o SensorPanel com métricas vitais para o usuário final.

**Caminho no software:** **Arquivo** > **Preferências** > **Monitoramento de Hardware** > **SensorPanel**

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Check: Exibir SensorPanel.
  - Check: Manter janelas sobrepostas.
  - Atualização: 1000ms.
- **Verificação antes de executar:** Verificar a resolução do monitor do cliente para não criar um painel gigante ou minúsculo.

> [!TIP]
> **Boas práticas:** Exportar o perfil do SensorPanel pronto (**Exportar**) para restaurar se o usuário desinstalar o software.
> **Alternativa segura:** Usar o Gadget de Sidebar (mais simples/antigo) se o SensorPanel for muito pesado.

### Solução de problemas

**Possíveis erros:**
1. Painel não aparece.
2. Gráficos/Medidores vazios.
3. Painel reseta posição ao reiniciar.

**Causa técnica:**
1. Serviço gráfico bloqueado ou posição X/Y fora da área de trabalho.
2. Sensor desconectado.
3. Falta de privilégios de escrita no arquivo `.INI` de configuração.

**Como identificar:**
1. Checkbox marcado mas nada na tela.
2. Medidores mostram "N/A".

**Como corrigir:**
`SE` não aparecer `ENTÃO`:
1. Clicar em **Posição Padrão** nas preferências.
`SE` não salvar posição `ENTÃO`: Executar AIDA64 como Administrador sempre.

**Validação pós-correção:** O painel deve persistir na área de trabalho e atualizar valores a cada segundo.

> [!WARNING]
> **Impacto se ignorado:** Perda de tempo configurando layout que não será salvo.

### Checklist de confirmação
- [ ] Painel visível?
- [ ] Posição travada?
- [ ] Backup do layout salvo?

---

## Etapa 11 — Configuração de Alertas Automáticos

**Objetivo:** Automatizar a segurança do hardware com gatilhos de evento (Temperatura/Voltagem).
**Risco:** Médio | **Tempo estimado:** 5 min

### Ação exata a executar

Definir regras de alerta para notificar ou desligar o PC em caso de falha crítica futura.

**Caminho no software:** **Arquivo** > **Preferências** > **Alertas**

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Trigger: Temperatura CPU > 85°C.
  - Ação: Exibir mensagem de alerta ou Desligar o sistema.
- **Verificação antes de executar:** Testar o sistema de som se escolher "Tocar som". Testar envio de e-mail se configurar SMTP.

> [!TIP]
> **Boas práticas:** Configurar envio de e-mail para o técnico responsável em caso de falha crítica (requer SMTP).
> **Alternativa segura:** Usar alertas da BIOS (nível de hardware), que são infalíveis mas menos flexíveis.

### Solução de problemas

**Possíveis erros:**
1. Alertas falsos contínuos.
2. Ação de desligamento executada durante trabalho não salvo.

**Causa técnica:**
1. Sensor com leitura errática (picos falsos de ms).
2. Limite definido muito próximo da temperatura de operação normal.

**Como identificar:**
Janelas de alerta pipocando sem motivo ou PC desligando "sozinho".

**Como corrigir:**
`SE` falsos positivos `ENTÃO`: Aumentar o intervalo de checagem ou elevar o limiar (Threshold) do gatilho em +5°C.

**Validação pós-correção:** Simular aquecimento (rodando Stress Test controlado) e verificar se o alerta dispara no momento exato.

> [!WARNING]
> **Impacto se ignorado:** Desligamento abrupto configurado incorretamente pode causar perda de dados do usuário.

### Checklist de confirmação
- [ ] Gatilho > 85°C definido?
- [ ] Ação de alerta escolhida?
- [ ] Teste de disparo realizado?

---

## Etapa 12 — Encerramento e Limpeza do Ambiente

**Objetivo:** Remover drivers de baixo nível e garantir que o sistema volte ao estado original.
**Risco:** Baixo | **Tempo estimado:** 1 min

### Ação exata a executar

1. Desativar SensorPanel/OSD.
2. Fechar o software completamente.
3. Remover driver temporário (se versão portable).

**Caminho no software:** **Arquivo** > **Sair**

> [!NOTE]
> **Atalho de teclado:** `Alt` + `F4`

### Configurações e Pré-requisitos

- **Configurações recomendadas:**
  - Se usar versão instalável: Não requer ação extra.
  - Se Portable: Verificar pasta temporária.
- **Verificação antes de executar:** Verificar se o processo `aida64.exe` sumiu do Gerenciador de Tarefas.

> [!TIP]
> **Boas práticas:** Nunca deixar versões antigas/vulneráveis do driver do AIDA64 no PC do cliente (risco de segurança CVE).
> **Alternativa segura:** Reiniciar o PC para garantir limpeza total da memória.

### Solução de problemas

**Possíveis erros:**
1. Processo preso em segundo plano.
2. Driver `kerneld.x64` bloqueado.

**Causa técnica:**
1. Conflito com softwares de monitoramento (MSI Afterburner/RivaTuner).
2. Windows segurando o handle do driver.

**Como identificar:**
Impossibilidade de deletar a pasta do AIDA64 Portable ("Arquivo em uso").

**Como corrigir:**
`SE` não fechar `ENTÃO`:
1. Pressione `Ctrl`+`Shift`+`Esc`.
2. Acesse a aba **Detalhes**.
3. Finalize `aida64.exe`.
4. Abrir CMD como Admin e digitar `sc stop aida64driver`.

**Validação pós-correção:** A pasta do AIDA64 pode ser movida ou deletada sem erros de permissão.

> [!WARNING]
> **Impacto se ignorado:** Deixar drivers de kernel desnecessários rodando pode causar instabilidade futura ou conflitos de anticheat em jogos.

### Checklist de confirmação
- [ ] Processo finalizado?
- [ ] Driver descarregado?
- [ ] Arquivos temporários limpos?

---

## Etapa 13 — Diagnóstico de Monitor (Display)

**Objetivo:** Validar calibração de cores, geometria e detectar Dead/Stuck Pixels no painel LCD/OLED.
**Risco:** Médio (Saúde) | **Tempo estimado:** 5 min

### Ação exata a executar

Executar a bateria de testes visuais de painel.

**Caminho no software:** **Ferramentas** > **Diagnóstico de Monitor**

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Selecionar: Solid Fill (todas as cores), Grid e Gradient. Modo: Auto Run.
- **Verificação antes de executar:** Limpar fisicamente a tela do monitor para não confundir poeira com pixels mortos.

> [!TIP]
> **Boas práticas:** Executar em ambiente escuro para identificar vazamento de luz (Backlight Bleed) no teste de tela preta.
> **Alternativa segura:** Usar site "Dead Pixel Test" (menos robusto, mas não requer software).

### Solução de problemas

**Possíveis erros:**
1. Epilepsia fotossensível (risco humano).
2. Monitor entra em standby durante o teste.

**Causa técnica:**
1. Padrões de cintilação rápida (Flickering).
2. Configuração de energia do Windows interrompe o vídeo.

**Como identificar:**
1. Usuário sente tontura.
2. Tela apaga no meio do gradiente.

**Como corrigir:**
`SE` mal-estar `ENTÃO`: Pressionar `Esc` imediatamente.
`SE` tela apagar `ENTÃO`: Mover o mouse ou desativar economia de energia antes.

**Validação pós-correção:** Verificar visualmente se todos os pixels acenderam nas cores R, G, B, Branco e Preto.

> [!WARNING]
> **Impacto se ignorado:** Entregar um monitor com Dead Pixel não detectado gera devolução imediata (RMA).

### Checklist de confirmação
- [ ] Tela limpa?
- [ ] Cores primárias OK?
- [ ] Gradientes suaves?

---

## Etapa 14 — Benchmark de Disco (Performance)

**Objetivo:** Medir a velocidade real de Leitura/Escrita (IOPS e MB/s) para validar SSDs/NVMe.
**Risco:** Alto | **Tempo estimado:** 10 min

### Ação exata a executar

Executar teste de desempenho de armazenamento (Diferente do teste de saúde do Victoria).

**Caminho no software:** **Ferramentas** > **Disk Benchmark**

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Opção: Linear Read (Padrão) ou Random Read. Block Size: Auto.
- **Verificação antes de executar:** **CRÍTICO:** Nunca selecionar "Write" em disco com dados.

> [!TIP]
> **Boas práticas:** Monitorar a temperatura do SSD via sensor durante o benchmark. NVMe quente perde 50% da performance.
> **Alternativa segura:** CrystalDiskMark (mais rápido e amigável, mas menos detalhado em curvas de latência).

### Solução de problemas

**Possíveis erros:**
1. Perda total de dados (se selecionar Write).
2. Resultado muito baixo (SSD SATA operando como IDE).

**Causa técnica:**
1. Ação destrutiva de sobrescrita.
2. Driver AHCI/NVMe ausente ou porta SATA incorreta (SATA2 vs SATA3).

**Como identificar:**
1. Aviso gigante "Data will be lost".
2. Gráfico linear abaixo de 500MB/s para SSD SATA.

**Como corrigir:**
`SE` velocidade baixa `ENTÃO`: Verificar BIOS (modo AHCI) e cabo.
`SE` selecionou Write sem querer `ENTÃO`: Cancelar no aviso de confirmação.

**Validação pós-correção:** O gráfico deve ser estável. Quedas bruscas indicam superaquecimento do controlador do SSD (Thermal Throttling).

> [!WARNING]
> **Impacto se ignorado:** Selecionar *Linear Write* destruirá a tabela de partição e arquivos sem chance de recuperação simples.

### Checklist de confirmação
- [ ] Modo READ selecionado?
- [ ] Disco correto?
- [ ] Temperatura monitorada?

---

## Etapa 15 — Análise Profunda de DRAM (SPD)

**Objetivo:** Verificar autenticidade dos pentes de memória e timings reais (JEDEC vs XMP).
**Risco:** Baixo | **Tempo estimado:** 2 min

### Ação exata a executar

Ler os dados brutos do chip SPD (Serial Presence Detect).

**Caminho no software:** **Placa Mãe** > **SPD**

### Configurações e Pré-requisitos

- **Configurações recomendadas:** Comparar Velocidade da Memória com Tensão do Módulo.
- **Verificação antes de executar:** Confirmar se a memória instalada é a que foi vendida (ex: 3200MHz vs 2133MHz).

> [!TIP]
> **Boas práticas:** Verificar a "Data de Fabricação" (Week/Year) para saber se o componente é novo ou estoque antigo (New Old Stock).
> **Alternativa segura:** CPU-Z (Aba SPD) - Leitura similar, interface mais simples.
> **Observações técnicas:** Fabricantes de RAM genérica muitas vezes não gravam o nome no SPD. AIDA64 mostrará "Module Name: A-DATA" ou similar se for genuína.

### Solução de problemas

**Possíveis erros:**
1. SPD vazio ou ilegível.
2. Incompatibilidade de timings (ex: CL16 rodando a CL22).

**Causa técnica:**
1. SMBus bloqueado ou memória falsificada (SPD apagado).
2. XMP desativado na BIOS.

**Como identificar:**
Linhas em branco ou valores genéricos "Unknown".

**Como corrigir:**
`SE` timings altos (lentos) `ENTÃO`:
1. Reiniciar.
2. Entrar na BIOS.
3. Ativar Profile XMP/DOCP.

**Validação pós-correção:** O campo "Active Mode" na aba Chipset deve igualar o "XMP Profile" da aba SPD.

> [!WARNING]
> **Impacto se ignorado:** Cliente pagou por memória rápida e está usando na velocidade mínima padrão (perda de performance de até 20%).

### Checklist de confirmação
- [ ] XMP Ativo?
- [ ] Voltagem correta (1.35v)?
- [ ] Fabricante identificado?

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
