<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `REF_AIDA64`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Opere as ferramentas](../../README.md#opere-as-ferramentas) › **Guia operacional — AIDA64 (etapas 31 a 45)**

# Guia operacional — AIDA64 (etapas 31 a 45)

> Etapas 31 a 45 do procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e auditoria.


**Aplica-se a:** Sistemas que carregam o Windows — sensores, stress test e relatórios

## Neste documento

- [Etapas](#etapas)
- [Etapa 31 — Calibração de Sensores (Offset)](#etapa-31--calibração-de-sensores-offset)
- [Etapa 32 — Identificação de Hardware Desconhecido](#etapa-32--identificação-de-hardware-desconhecido)
- [Etapa 33 — Monitoramento de No-Break (UPS)](#etapa-33--monitoramento-de-no-break-ups)
- [Etapa 34 — Integração com Displays LCD (Logitech/Razer)](#etapa-34--integração-com-displays-lcd-logitechrazer)
- [Etapa 35 — Exportação para Memória Compartilhada (Modding)](#etapa-35--exportação-para-memória-compartilhada-modding)
- [Etapa 36 — Backup de Drivers Instalados](#etapa-36--backup-de-drivers-instalados)
- [Etapa 37 — Diagnóstico de Link de Rede (PHY)](#etapa-37--diagnóstico-de-link-de-rede-phy)
- [Etapa 38 — Verificação de Tempo de Atividade (Uptime)](#etapa-38--verificação-de-tempo-de-atividade-uptime)
- [Etapa 39 — Auditoria de Softwares Instalados](#etapa-39--auditoria-de-softwares-instalados)
- [Etapa 40 — Gerenciador de Auditoria (Audit Manager)](#etapa-40--gerenciador-de-auditoria-audit-manager)
- [Etapa 41 — Solução de Conflito com Anti-Cheat](#etapa-41--solução-de-conflito-com-anti-cheat)
- [Etapa 42 — Auditoria de Segurança do Windows](#etapa-42--auditoria-de-segurança-do-windows)
- [Etapa 43 — Criação de "Master Report" (Entrega)](#etapa-43--criação-de-master-report-entrega)
- [Etapa 44 — Limpeza de Registro do AIDA64](#etapa-44--limpeza-de-registro-do-aida64)
- [Etapa 45 — Checklist Final de Encerramento (SOP)](#etapa-45--checklist-final-de-encerramento-sop)
- [Próximos passos](#próximos-passos)

## Contexto

Procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e auditoria. Esta parte cobre a faixa de etapas indicada no título.

## Escopo

As etapas 31 a 45 registradas na fonte, com todos os campos originais.

## Fora do escopo

Interpretação clínica dos resultados fora do que a fonte declara; procedimentos de outras ferramentas; critérios de validação por componente (ver documento 13).

## Relação com outros documentos

- [Índice de ferramentas](00-indice-ferramentas.md)
- [Validação final por componente](../13-validacao-final.md)
- [Índice de cenários](../10-cenarios/00-indice-cenarios.md)

---

> Este guia foi dividido em três arquivos **apenas pela numeração das etapas de origem** (1–15, 16–30, 31–45). A divisão é organizacional; a fonte não define grupos.

## Etapas

| Nº | Fase do processo | Risco | Tempo estimado |
| --- | --- | --- | --- |
| [31](#etapa-31--calibração-de-sensores-offset) | Calibração de Sensores (Offset) | Crítico | 10 min |
| [32](#etapa-32--identificação-de-hardware-desconhecido) | Identificação de Hardware Desconhecido | Baixo | 2 min |
| [33](#etapa-33--monitoramento-de-no-break-ups) | Monitoramento de No-Break (UPS) | Alto (Servidor) | 3 min |
| [34](#etapa-34--integração-com-displays-lcd-logitechrazer) | Integração com Displays LCD (Logitech/Razer) | Baixo (Cosmético) | 10 min |
| [35](#etapa-35--exportação-para-memória-compartilhada-modding) | Exportação para Memória Compartilhada (Modding) | Baixo | 15 min |
| [36](#etapa-36--backup-de-drivers-instalados) | Backup de Drivers Instalados | Médio | 3 min |
| [37](#etapa-37--diagnóstico-de-link-de-rede-phy) | Diagnóstico de Link de Rede (PHY) | Médio | 2 min |
| [38](#etapa-38--verificação-de-tempo-de-atividade-uptime) | Verificação de Tempo de Atividade (Uptime) | Baixo | 1 min |
| [39](#etapa-39--auditoria-de-softwares-instalados) | Auditoria de Softwares Instalados | Médio | 3 min |
| [40](#etapa-40--gerenciador-de-auditoria-audit-manager) | Gerenciador de Auditoria (Audit Manager) | Alto (Segurança) | 5 min |
| [41](#etapa-41--solução-de-conflito-com-anti-cheat) | Solução de Conflito com Anti-Cheat | Alto | 2 min |
| [42](#etapa-42--auditoria-de-segurança-do-windows) | Auditoria de Segurança do Windows | Crítico | 1 min |
| [43](#etapa-43--criação-de-master-report-entrega) | Criação de "Master Report" (Entrega) | Baixo | 5 min |
| [44](#etapa-44--limpeza-de-registro-do-aida64) | Limpeza de Registro do AIDA64 | Alto | 3 min |
| [45](#etapa-45--checklist-final-de-encerramento-sop) | Checklist Final de Encerramento (SOP) | Médio | 5 min |

---

## Etapa 31 — Calibração de Sensores (Offset)

### Objetivo da etapa

Corrigir leituras erradas de sensores da placa-mãe (ex: Temp ambiente vs Real)

### Ação exata a executar

Ajustar manualmente o deslocamento (Offset) ou multiplicador dos sensores.

### Caminho no software

Arquivo > Preferências > Monitoramento de Hardware > Correção

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Usar apenas se tiver um termômetro físico (infravermelho/laser) para referência.

### Verificação antes de executar

Comparar leitura da BIOS com a leitura do AIDA64. Se diferir, ajustar.

### Possíveis erros

1. Leitura mascarada.  

2. Superaquecimento real ignorado.

### Causa técnica do erro

1. Aplicar offset negativo (-20°C) incorretamente faz o PC ferver sem alertar.  

2. Confundir Fahrenheit com Celsius.

### Como identificar o erro

AIDA mostra 40°C, mas o dissipador está intocável de quente (>80°C).

### Como corrigir (passo a passo)

SE dúvida ENTÃO: Clicar em "Restaurar Padrões". Nunca chutar valores de calibração.

### Validação pós-correção

A temperatura exibida no software deve bater com a temperatura medida no termômetro IR (+/- 2°C).

### Risco

Crítico

### Impacto se ignorado

Mascarar um problema térmico real via software pode levar à queima do componente a longo prazo.

### Tempo estimado

10 min

### Observações técnicas

Placas-mãe antigas frequentemente reportam sensores "Aux" com valores absurdos (127°C ou -50°C). Estes são pinos desconectados e devem ser ocultados, não calibrados.

### Boas práticas

Ocultar sensores "fantasmas" na aba de visibilidade em vez de tentar calibrá-los.

### Alternativa segura

N/A - Confiar na BIOS.

### Checklist de confirmação

- [ ] Termômetro físico usado?  
- [ ] Offset aplicado com razão?  
- [ ] Sensores fantasmas ocultos?

---

## Etapa 32 — Identificação de Hardware Desconhecido

### Objetivo da etapa

Encontrar drivers para dispositivos listados como "Dispositivo Desconhecido" no Windows

### Ação exata a executar

Usar o banco de dados de Hardware ID (PCI/USB/ACPI) para identificar o fabricante.

### Caminho no software

Menu Dispositivos > Dispositivos do Windows > Unknown

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Clicar no dispositivo e olhar o painel inferior (Propriedades do Dispositivo).

### Verificação antes de executar

Ter conexão com a internet para buscar o driver posteriormente.

### Possíveis erros

1. ID genérico.  

2. Dispositivo não listado.

### Causa técnica do erro

1. Periférico USB sem handshake (defeituoso).  

2. Driver de chipset não instalado, ocultando o barramento inteiro.

### Como identificar o erro

O campo "Hardware ID" mostra apenas USB\\UNKNOWN.

### Como corrigir (passo a passo)

SE ID desconhecido ENTÃO: Copiar a string VEN_xxxx&DEV_xxxx. Colocar no Google ou site "PCI Lookup".

### Validação pós-correção

O AIDA64 deve mostrar o nome do fabricante (ex: "Realtek", "Intel") na descrição do dispositivo, facilitando o download.

### Risco

Baixo

### Impacto se ignorado

Entregar PC com "triângulos amarelos" no Gerenciador de Dispositivos.

### Tempo estimado

2 min

### Observações técnicas

O AIDA64 possui um banco de dados interno de Vendor IDs muito superior ao do Windows Update.

### Boas práticas

Copiar o ID do Hardware diretamente para a área de transferência com botão direito.

### Alternativa segura

DriverPack Solution (Cuidado com adwares).

### Checklist de confirmação

- [ ] Dispositivo identificado?  
- [ ] Driver baixado?  
- [ ] Gerenciador limpo?

---

## Etapa 33 — Monitoramento de No-Break (UPS)

### Objetivo da etapa

Verificar carga, voltagem de entrada/saída e saúde da bateria do UPS via USB

### Ação exata a executar

Acessar dados de energia externa (se o No-break tiver porta USB/Serial).

### Caminho no software

Menu Computador > Gerenciamento de Energia

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Requer cabo USB conectado entre UPS e PC.

### Verificação antes de executar

Instalar driver do fabricante do No-break (APC, SMS, Eaton) se não for plug-and-play.

### Possíveis erros

1. UPS não detectado.  

2. Leitura de carga errada.

### Causa técnica do erro

1. Cabo de dados desconectado ou serviço do Windows (Battery) conflitando.  

2. Bateria do UPS viciada.

### Como identificar o erro

Linha "Bateria" ausente ou mostrando "Carregando" infinitamente.

### Como corrigir (passo a passo)

SE não detectar ENTÃO: Verificar se o serviço "HID UPS Battery" do Windows está rodando (services.msc).

### Validação pós-correção

Tensão de Entrada deve mostrar ~115V/220V e Saída estável. Carga da bateria deve ser >90%.

### Risco

Alto (Servidor)

### Impacto se ignorado

Se o UPS falhar silenciosamente, o servidor desligará no primeiro pico de luz, corrompendo banco de dados.

### Tempo estimado

3 min

### Observações técnicas

Essencial para servidores. O AIDA64 pode disparar o alerta de "Voltagem Baixa" configurado na Etapa 11 se a energia cair.

### Boas práticas

Testar o "Self-Test" do UPS via software proprietário, usar AIDA apenas para leitura passiva.

### Alternativa segura

Software nativo do fabricante (PowerChute).

### Checklist de confirmação

- [ ] Cabo USB conectado?  
- [ ] Carga da bateria visível?  
- [ ] Tensão de entrada monitorada?

---

## Etapa 34 — Integração com Displays LCD (Logitech/Razer)

### Objetivo da etapa

Enviar dados para teclados com tela (G15/G19) ou displays dedicados

### Ação exata a executar

Configurar o layout para telas LCD monocromáticas ou coloridas integradas a periféricos.

### Caminho no software

Arquivo > Preferências > Hardware Monitoring > LCD

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Selecionar o modelo exato do teclado/display.

### Verificação antes de executar

Ter o software do fabricante (Logitech G Hub / Razer Synapse) rodando.

### Possíveis erros

1. Tela do teclado preta.  

2. Layout desconfigurado (texto cortado).

### Causa técnica do erro

1. Applet do AIDA64 não autorizado no software do teclado.  

2. Resolução do LCD incorreta.

### Como identificar o erro

AIDA64 aparece na lista de apps do teclado, mas não mostra dados.

### Como corrigir (passo a passo)

SE tela preta ENTÃO: Abrir Logitech G Hub > Applets > Ativar AIDA64. Pressionar botão de troca de app no teclado.

### Validação pós-correção

As informações aparecem fisicamente no teclado, permitindo monitorar temps em tela cheia no monitor principal.

### Risco

Baixo (Cosmético)

### Impacto se ignorado

Recurso "Gamer" premium não utilizado.

### Tempo estimado

10 min

### Observações técnicas

Para usuários avançados, pode-se usar um tablet velho como segundo monitor via "RemoteSensor" (Etapa 23) ou app "Odyssey".

### Boas práticas

Usar fontes grandes para facilitar leitura rápida.

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Display detectado?  
- [ ] Applet autorizado?  
- [ ] Dados legíveis?

---

## Etapa 35 — Exportação para Memória Compartilhada (Modding)

### Objetivo da etapa

Alimentar softwares de personalização de Desktop (Rainmeter/Samurize) com dados reais

### Ação exata a executar

Habilitar a escrita em Shared Memory para skins de terceiros.

### Caminho no software

Arquivo > Preferências > Hardware Monitoring > External Applications

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Check: Enable Shared Memory.

### Verificação antes de executar

Saber mapear as variáveis (ex: SCPUUTI = CPU Utilization) no software destino.

### Possíveis erros

1. Rainmeter mostra "0" ou nada.  

2. Alto uso de CPU pelo AIDA64.

### Causa técnica do erro

1. Mapeamento de nomes de variáveis incorreto na skin do Rainmeter.  

2. Taxa de atualização muito agressiva (<100ms).

### Como identificar o erro

Skin do desktop estática.

### Como corrigir (passo a passo)

SE dados zerados ENTÃO: Verificar a lista de "Registry/Shared Memory Labels" no AIDA e corrigir o .ini do Rainmeter.

### Validação pós-correção

O widget no desktop reage instantaneamente ao uso do computador.

### Risco

Baixo

### Impacto se ignorado

Apenas visual.

### Tempo estimado

15 min

### Observações técnicas

Permite criar desktops futuristas para clientes "Gamers/Modders". O AIDA64 atua como o motor (backend) e o Rainmeter como a interface (frontend).

### Boas práticas

Manter taxa de atualização em 1000ms para não consumir ciclos de CPU desnecessários.

### Alternativa segura

HWiNFO Shared Memory (Requer licença Pro para uso contínuo recente).

### Checklist de confirmação

- [ ] Shared Memory ativo?  
- [ ] Labels verificados?  
- [ ] Skin reagindo?

---

## Etapa 36 — Backup de Drivers Instalados

### Objetivo da etapa

Extrair uma lista ou os próprios arquivos de drivers funcionais para formatação futura

### Ação exata a executar

Listar todos os drivers de sistema e periféricos detectados.

### Caminho no software

Menu Computador > Sistema Operacional > Drivers de Sistema

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Clicar com botão direito > Copiar tudo.

### Verificação antes de executar

O objetivo não é fazer backup dos arquivos (o AIDA não faz isso bem), mas sim inventariar as versões.

### Possíveis erros

1. Confiar que a lista contém o instalador.  

2. Não anotar a versão exata.

### Causa técnica do erro

1. O AIDA lista o driver carregado na RAM, não o instalador .exe.  

2. Windows Update substitui drivers funcionais por genéricos.

### Como identificar o erro

Após formatar, o driver novo causa tela azul e não se sabe qual era o antigo funcional.

### Como corrigir (passo a passo)

SE driver crítico (ex: Placa de captura antiga) ENTÃO: Usar "DISM /Export-Driver" no CMD, usando o AIDA apenas para identificar qual é o crucial.

### Validação pós-correção

Ter uma lista impressa das versões (ex: Nvidia v531.29) que funcionavam perfeitamente.

### Risco

Médio

### Impacto se ignorado

Perder compatibilidade com hardware legado após formatação.

### Tempo estimado

3 min

### Observações técnicas

O AIDA64 é ferramenta de Informação. Para Extração de drivers, use o comando do PowerShell: Export-WindowsDriver -Online -Destination "D:\\BackupDrivers".

### Boas práticas

Usar a lista do AIDA para baixar previamente os drivers no site do fabricante antes de formatar.

### Alternativa segura

Double Driver (Software antigo mas funcional para backup).

### Checklist de confirmação

- [ ] Lista de versões salva?  
- [ ] DISM executado para extração?  
- [ ] Drivers críticos identificados?

---

## Etapa 37 — Diagnóstico de Link de Rede (PHY)

### Objetivo da etapa

Verificar se a placa de rede está negociando a velocidade correta (1Gbps vs 100Mbps) com o roteador

### Ação exata a executar

Acessar status da conexão física e verificar a velocidade negociada.

### Caminho no software

Menu Rede > Rede do Windows

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Verificar campo Velocidade da Conexão e Endereço MAC.

### Verificação antes de executar

Confirmar se o cabo é CAT5e ou superior e se o switch/roteador é Gigabit.

### Possíveis erros

1. Link travado em 100Mbps.  

2. Wi-Fi com sinal fraco (-80dBm).

### Causa técnica do erro

1. Cabo crimpado errado (apenas 2 pares) ou porta do roteador em modo "Eco".  

2. Interferência ou distância.

### Como identificar o erro

Velocidade de internet lenta, mas provedor entrega banda correta.

### Como corrigir (passo a passo)

SE 100Mbps em placa Gigabit ENTÃO: Trocar o cabo de rede imediatamente. SE Wi-Fi fraco ENTÃO: Mudar canal no roteador.

### Validação pós-correção

O campo deve mostrar "1000 Mbps" (Gigabit) ou velocidade Wi-Fi real (ex: 866 Mbps).

### Risco

Médio

### Impacto se ignorado

Diagnosticar erroneamente lentidão de internet como culpa do provedor, quando é o cabeamento local.

### Tempo estimado

2 min

### Observações técnicas

O AIDA64 lê a camada física (PHY). Se o driver estiver genérico, pode não mostrar detalhes avançados.

### Boas práticas

Cruzar essa informação com um teste de velocidade (Speedtest).

### Alternativa segura

ncpa.cpl (Status da placa no Windows).

### Checklist de confirmação

- [ ] Negociação Gigabit?  
- [ ] MAC Address confere?  
- [ ] Wi-Fi Signal > -65dBm?

---

## Etapa 38 — Verificação de Tempo de Atividade (Uptime)

### Objetivo da etapa

Descobrir se o usuário realmente reiniciou o PC ou apenas desligou e ligou (Fast Boot)

### Ação exata a executar

Verificar o contador de tempo de atividade real do kernel.

### Caminho no software

Menu Sistema Operacional > Tempo de Atividade

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Analisar: Tempo de Atividade do Sistema vs Tempo de Atividade Atual.

### Verificação antes de executar

Lembrar que o "Desligar" do Windows 10/11 é uma hibernação híbrida e não zera o contador.

### Possíveis erros

1. Uptime de 30+ dias reportado.  

2. Lentidão acumulada.

### Causa técnica do erro

1. O usuário clica em "Desligar", mas o kernel nunca reinicia devido ao "Fast Startup".  

2. Vazamento de memória (Memory Leak) acumulado.

### Como identificar o erro

O PC está lento e o cliente jura que "desligou ontem".

### Como corrigir (passo a passo)

SE Uptime > 7 dias e PC lento ENTÃO: Segurar Shift e clicar em Desligar (Força Full Shutdown) ou usar Reiniciar.

### Validação pós-correção

Contador deve zerar para "0 dias, 0 horas, X minutos".

### Risco

Baixo

### Impacto se ignorado

Diagnóstico falho de lentidão causada apenas por falta de reboot real.

### Tempo estimado

1 min

### Observações técnicas

Esta é a ferramenta nº 1 para desmentir usuários que dizem "Já reiniciei 3 vezes" (quando só desligaram o monitor ou suspenderam).

### Boas práticas

Desativar a "Inicialização Rápida" no Painel de Controle de Energia se causar problemas frequentes.

### Alternativa segura

Gerenciador de Tarefas > Desempenho > CPU (Tempo de Atividade).

### Checklist de confirmação

- [ ] Uptime verificado?  
- [ ] Reinício real confirmado?  
- [ ] Fast Boot explicado?

---

## Etapa 39 — Auditoria de Softwares Instalados

### Objetivo da etapa

Listar todos os programas para backup ou identificar Bloatware/Malware oculto

### Ação exata a executar

Gerar lista completa de aplicações instaladas via registro e Windows Store.

### Caminho no software

Menu Programas > Programas Instalados

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Ordenar por Data da Instalação para ver o que foi colocado recentemente.

### Verificação antes de executar

Perguntar ao cliente quais softwares são vitais antes de sugerir remoção.

### Possíveis erros

1. Lista incompleta (Portable apps).  

2. Softwares fantasmas (desinstalados mas registro sujo).

### Causa técnica do erro

1. Softwares que não escrevem em Uninstall no registro não aparecem.  

2. Restos de chaves de registro.

### Como identificar o erro

Programas que não aparecem no Painel de Controle mas estão na lista do AIDA.

### Como corrigir (passo a passo)

SE software suspeito ENTÃO: Google no nome do executável. SE confirmado inútil, usar Revo Uninstaller.

### Validação pós-correção

Lista limpa contendo apenas softwares úteis e drivers.

### Risco

Médio

### Impacto se ignorado

Deixar softwares espiões ou trials expirados consumindo recursos.

### Tempo estimado

3 min

### Observações técnicas

Útil para criar uma "Lista de Reinstalação" antes de formatar a máquina do cliente.

### Boas práticas

Exportar esta lista para TXT e salvar no backup do cliente (Softwares_Antigos.txt).

### Alternativa segura

appwiz.cpl (Não lista Apps da Loja Windows tão bem).

### Checklist de confirmação

- [ ] Bloatware identificado?  
- [ ] Lista exportada?  
- [ ] Softwares críticos notados?

---

## Etapa 40 — Gerenciador de Auditoria (Audit Manager)

### Objetivo da etapa

Rastrear mudanças de hardware/software entre duas datas (O que mudou?)

### Ação exata a executar

Comparar dois relatórios AIDA64 gerados em momentos diferentes para ver diferenças.

### Caminho no software

Menu Ferramentas > Gerenciador de Auditoria

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Carregar Relatório_Antigo.csv e Relatório_Novo.csv.

### Verificação antes de executar

Requer que um relatório anterior tenha sido salvo e guardado (Etapa 08/20).

### Possíveis erros

1. Relatórios incompatíveis.  

2. Falso positivo de mudança (ex: Temperatura).

### Causa técnica do erro

1. Formatos diferentes (HTML vs CSV) ou versões de AIDA muito distantes.  

2. Sensores variam naturalmente.

### Como identificar o erro

O software aponta "Mudança" em voltagem ou RPM de fan.

### Como corrigir (passo a passo)

Filtrar/Ignorar sensores na comparação. Focar em: Memória Total, Disco Rígido, Adaptador de Vídeo.

### Validação pós-correção

Detectar se um pente de memória foi removido ou uma GPU trocada.

### Risco

Alto (Segurança)

### Impacto se ignorado

Detectar furto de componentes em empresas ou mudanças não autorizadas pelo usuário.

### Tempo estimado

5 min

### Observações técnicas

Ferramenta administrativa poderosa para TI Corporativa. Permite provar que o usuário instalou software proibido entre a visita A e B.

### Boas práticas

Usar relatórios CSV para esta função (são mais fáceis de parsear).

### Alternativa segura

Comparação manual de olho (falível).

### Checklist de confirmação

- [ ] Relatório base existe?  
- [ ] Mudanças detectadas?  
- [ ] Furto/Alteração descartado?

---

## Etapa 41 — Solução de Conflito com Anti-Cheat

### Objetivo da etapa

Evitar que o driver kerneld.x64 cause banimento ou crash em jogos (Valorant/CS2)

### Ação exata a executar

Desativar recursos de baixo nível antes de entregar o PC ao cliente gamer.

### Caminho no software

Arquivo > Preferências > Estabilidade

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Check (Desativar): Kernel Driver (se não for usar sensores) ou apenas garantir que o AIDA esteja FECHADO.

### Verificação antes de executar

Perguntar se o cliente joga Valorant, FaceIT ou usa softwares bancários (Warsaw).

### Possíveis erros

1. Jogo não abre (Erro VAN 1067).  

2. Tela azul PAGE_FAULT_IN_NONPAGED_AREA.

### Causa técnica do erro

1. O Anti-Cheat detecta o driver do AIDA64 como ferramenta de hacking (leitura de memória).  

2. Conflito de acesso ao barramento SMBus.

### Como identificar o erro

Mensagem de erro do Riot Vanguard ao iniciar o PC.

### Como corrigir (passo a passo)

SE cliente gamer ENTÃO: Não configurar AIDA64 para iniciar com o Windows. Ensinar a fechar completamente após o uso.

### Validação pós-correção

O jogo abre normalmente sem alertas de segurança.

### Risco

Alto

### Impacto se ignorado

Cliente ser banido de jogo online por "Uso de software de terceiros" (Falso positivo).

### Tempo estimado

2 min

### Observações técnicas

O driver do AIDA64 acessa hardware diretamente. Anti-cheats modernos odeiam isso.

### Boas práticas

Configurar o AIDA64 para não carregar o driver na inicialização em PCs domésticos.

### Alternativa segura

Usar visualizadores de sensor nativos da GPU (GeForce Experience) para jogos.

### Checklist de confirmação

- [ ] Anti-Cheat detectado?  
- [ ] AIDA removido do Startup?  
- [ ] Cliente alertado?

---

## Etapa 42 — Auditoria de Segurança do Windows

### Objetivo da etapa

Verificar status real do Antivírus, Firewall e UAC via WMI

### Ação exata a executar

Acessar o centro de segurança via API para confirmar proteção ativa.

### Caminho no software

Menu Sistema Operacional > Sistema Operacional (Seção Segurança)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Verificar Antivírus, Firewall e Controle de Conta de Usuário (UAC).

### Verificação antes de executar

Não confiar apenas no ícone da bandeja do sistema (que pode ser falsificado por malware).

### Possíveis erros

1. Antivírus reportado como "Desativado" mas está ativo.  

2. UAC desativado.

### Causa técnica do erro

1. Delay na atualização do WMI do Windows.  

2. Usuário desativou UAC para instalar crack.

### Como identificar o erro

Campo de segurança em cinza ou vermelho.

### Como corrigir (passo a passo)

SE desativado ENTÃO: Ir no Painel de Segurança do Windows e reativar. Se falhar, possível infecção por Malware que matou o Defender.

### Validação pós-correção

Status "Ativo e Atualizado".

### Risco

Crítico

### Impacto se ignorado

Entregar PC vulnerável a ransomware.

### Tempo estimado

1 min

### Observações técnicas

O AIDA64 lê o repositório WMI root\\SecurityCenter2. Se o malware corromper isso, o AIDA reportará erro.

### Boas práticas

UAC deve estar sempre no nível padrão ou máximo. Nunca desligado.

### Alternativa segura

Comando wmic /namespace:\\\\root\\servicemodel path antivirusproduct get displayName.

### Checklist de confirmação

- [ ] AV Ativo?  
- [ ] Firewall Ativo?  
- [ ] UAC Nível 2+?

---

## Etapa 43 — Criação de "Master Report" (Entrega)

### Objetivo da etapa

Gerar o documento final consolidado que atesta a saúde da máquina

### Ação exata a executar

Compilar todas as páginas relevantes em um único PDF/HTML limpo.

### Caminho no software

Relatório > Assistente > Páginas Personalizadas

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Selecionar: Resumo, Sensor, S.M.A.R.T., Overclock, Licenças (Ocultas ou Visíveis dependendo do destino).

### Verificação antes de executar

Remover seções irrelevantes (ex: Debug, Direct X Database) para não criar um PDF de 200 páginas.

### Possíveis erros

1. Relatório muito grande (50MB+).  

2. Dados sensíveis expostos.

### Causa técnica do erro

1. Incluir "Logs de Eventos" ou "Arquivos DLL" no relatório.  

2. Não filtrar a seção de Licenças/Rede.

### Como identificar o erro

Cliente reclama que não consegue ler ou enviar o arquivo por e-mail.

### Como corrigir (passo a passo)

Selecionar apenas as categorias "Hardware Check" e "Benchmark" no assistente.

### Validação pós-correção

Arquivo final leve (<2MB), legível e profissional.

### Risco

Baixo

### Impacto se ignorado

Profissionalismo.

### Tempo estimado

5 min

### Observações técnicas

Este é o "Laudo Médico" do computador. Pode ser usado judicialmente em casos de garantia negada.

### Boas práticas

Adicionar um comentário no topo do relatório (campo Comentários nas Preferências) com o número da OS.

### Alternativa segura

Print Screen colado no Word (Amador).

### Checklist de confirmação

- [ ] Seções filtradas?  
- [ ] Dados sensíveis ocultos?  
- [ ] Salvo com nome da OS?

---

## Etapa 44 — Limpeza de Registro do AIDA64

### Objetivo da etapa

Remover chaves de configuração do registro do Windows ao desinstalar (Cleanup)

### Ação exata a executar

Apagar a chave HKEY_CURRENT_USER\\Software\\FinalWire\\AIDA64.

### Caminho no software

regedit.exe

### Atalho de teclado

Win + R > regedit

### Configurações recomendadas

Cuidado Extremo: Fazer backup do registro antes.

### Verificação antes de executar

Apenas necessário se o software foi instalado (não Portable) e apresentou bugs que reinstalação não resolve.

### Possíveis erros

1. Apagar chave errada.  

2. Corromper perfil de usuário.

### Causa técnica do erro

1. Erro humano.  

2. Manipulação indevida do regedit.

### Como identificar o erro

Windows não salva mais preferências ou AIDA não abre.

### Como corrigir (passo a passo)

SE erro ENTÃO: Restaurar backup do registro.

### Validação pós-correção

O AIDA64 abre como se fosse a primeira vez (Zero KM).

### Risco

Alto

### Impacto se ignorado

Danificar o registro do Windows é fatal para a estabilidade do SO.

### Tempo estimado

3 min

### Observações técnicas

O AIDA64 é muito limpo, mas configurações de OSD/SensorPanel ficam no registro. Se corromperem, só apagando a chave para resetar.

### Boas práticas

Só fazer isso se o AIDA64 estiver travando na inicialização ("Reset de Fábrica").

### Alternativa segura

Desinstalar via Revo Uninstaller (Modo Avançado).

### Checklist de confirmação

- [ ] Backup do Reg feito?  
- [ ] Chave correta localizada?  
- [ ] Reset confirmado?

---

## Etapa 45 — Checklist Final de Encerramento (SOP)

### Objetivo da etapa

Garantir que o técnico seguiu o fluxo lógico e não esqueceu nenhuma etapa crítica

### Ação exata a executar

Revisão mental ou física de todo o procedimento antes de liberar a máquina.

### Caminho no software

N/A (Procedural)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Validar: Backup > Hardware > Stress > Software > Limpeza > Relatório.

### Verificação antes de executar

Não ter pressa na entrega.

### Possíveis erros

1. Esquecer pen drive conectado.  

2. Deixar stress test rodando em background.  

3. Esquecer de reativar o Sleep Mode (Etapa 01).

### Causa técnica do erro

1. Distração.  

2. Falta de checklist físico.

### Como identificar o erro

Cliente liga dizendo "O PC não desliga a tela nunca mais" (Pois alteramos na Etapa 01).

### Como corrigir (passo a passo)

Reverter alterações de energia feitas na Etapa 01 (Restaurar plano "Equilibrado").

### Validação pós-correção

Máquina pronta, limpa, otimizada e documentada.

### Risco

Médio

### Impacto se ignorado

Pequenos esquecimentos geram chamados de retorno (Recall) desnecessários.

### Tempo estimado

5 min

### Observações técnicas

A diferença entre um "formatador" e um Engenheiro de TI está neste checklist final.

### Boas práticas

Colocar um adesivo de "Testado com AIDA64" ou selo de garantia na máquina (físico).

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Plano de Energia restaurado?  
- [ ] Pen drive removido?  
- [ ] Relatório entregue?

---


## Próximos passos

| Se você… | Vá para |
| --- | --- |
| terminou o teste e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |
| quer o procedimento do sintoma que motivou o teste | [Índice de cenários](../10-cenarios/00-indice-cenarios.md) |
| precisa de outra ferramenta | [Índice de ferramentas](00-indice-ferramentas.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `REF_AIDA64` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.3.0` |
