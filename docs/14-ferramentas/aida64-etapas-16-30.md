<!-- Gerado a partir de `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → aba `REF_AIDA64`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Opere as ferramentas](../../README.md#opere-as-ferramentas) › **Guia operacional — AIDA64 (etapas 16 a 30)**

# Guia operacional — AIDA64 (etapas 16 a 30)

> Etapas 16 a 30 do procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e auditoria.


**Aplica-se a:** Sistemas que carregam o Windows — sensores, stress test e relatórios

## Neste documento

- [Etapas](#etapas)
- [Etapa 16 — Auditoria de ACPI (Debug de BIOS)](#etapa-16--auditoria-de-acpi-debug-de-bios)
- [Etapa 17 — Automação via Linha de Comando (CLI)](#etapa-17--automação-via-linha-de-comando-cli)
- [Etapa 18 — Backup e Exportação de Preferências](#etapa-18--backup-e-exportação-de-preferências)
- [Etapa 19 — Verificação de OpenCL e GPGPU (Compute)](#etapa-19--verificação-de-opencl-e-gpgpu-compute)
- [Etapa 20 — Validação Final e "Golden Sample"](#etapa-20--validação-final-e-golden-sample)
- [Etapa 21 — Diagnóstico de Bateria (Notebooks)](#etapa-21--diagnóstico-de-bateria-notebooks)
- [Etapa 22 — Auditoria de Segurança e TPM](#etapa-22--auditoria-de-segurança-e-tpm)
- [Etapa 23 — Monitoramento Remoto (RemoteSensor)](#etapa-23--monitoramento-remoto-remotesensor)
- [Etapa 24 — Auditoria de Instruções de CPU (CPUID)](#etapa-24--auditoria-de-instruções-de-cpu-cpuid)
- [Etapa 25 — Recuperação de Licenças de Software](#etapa-25--recuperação-de-licenças-de-software)
- [Etapa 26 — Integração em Ambiente WinPE](#etapa-26--integração-em-ambiente-winpe)
- [Etapa 27 — Limpeza e Reset Pós-Uso](#etapa-27--limpeza-e-reset-pós-uso)
- [Etapa 28 — Conclusão e Entrega Técnica](#etapa-28--conclusão-e-entrega-técnica)
- [Etapa 29 — Integração OSD em Jogos (RivaTuner)](#etapa-29--integração-osd-em-jogos-rivatuner)
- [Etapa 30 — Registro de Log Contínuo ("Black Box")](#etapa-30--registro-de-log-contínuo-black-box)
- [Próximos passos](#próximos-passos)

## Contexto

Procedimento de uso do AIDA64 para monitoramento, teste de estabilidade, benchmark e auditoria. Esta parte cobre a faixa de etapas indicada no título.

## Escopo

As etapas 16 a 30 registradas na fonte, com todos os campos originais.

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
| [16](#etapa-16--auditoria-de-acpi-debug-de-bios) | Auditoria de ACPI (Debug de BIOS) | Alto (Risco de Crash) | 5 min |
| [17](#etapa-17--automação-via-linha-de-comando-cli) | Automação via Linha de Comando (CLI) | Baixo | N/A (Instantâneo) |
| [18](#etapa-18--backup-e-exportação-de-preferências) | Backup e Exportação de Preferências | Baixo | 1 min |
| [19](#etapa-19--verificação-de-opencl-e-gpgpu-compute) | Verificação de OpenCL e GPGPU (Compute) | Médio | 3 min |
| [20](#etapa-20--validação-final-e-golden-sample) | Validação Final e "Golden Sample" | Baixo | 5 min |
| [21](#etapa-21--diagnóstico-de-bateria-notebooks) | Diagnóstico de Bateria (Notebooks) | Médio (Financeiro) | 2 min |
| [22](#etapa-22--auditoria-de-segurança-e-tpm) | Auditoria de Segurança e TPM | Alto | 3 min |
| [23](#etapa-23--monitoramento-remoto-remotesensor) | Monitoramento Remoto (RemoteSensor) | Baixo | 5 min |
| [24](#etapa-24--auditoria-de-instruções-de-cpu-cpuid) | Auditoria de Instruções de CPU (CPUID) | Médio | 2 min |
| [25](#etapa-25--recuperação-de-licenças-de-software) | Recuperação de Licenças de Software | Alto (Legal) | 1 min |
| [26](#etapa-26--integração-em-ambiente-winpe) | Integração em Ambiente WinPE | Baixo | 10 min |
| [27](#etapa-27--limpeza-e-reset-pós-uso) | Limpeza e Reset Pós-Uso | Baixo (Imagem Profissional) | 2 min |
| [28](#etapa-28--conclusão-e-entrega-técnica) | Conclusão e Entrega Técnica | Crítico (Reputação) | 10 min |
| [29](#etapa-29--integração-osd-em-jogos-rivatuner) | Integração OSD em Jogos (RivaTuner) | Baixo | 5 min |
| [30](#etapa-30--registro-de-log-contínuo-black-box) | Registro de Log Contínuo ("Black Box") | Médio | 5 min |

---

## Etapa 16 — Auditoria de ACPI (Debug de BIOS)

### Objetivo da etapa

Investigar tabelas de firmware para resolver incompatibilidades de hardware ou BSODs misteriosos

### Ação exata a executar

Acessar o navegador de tabelas ACPI (Advanced Configuration and Power Interface).

### Caminho no software

Menu Ferramentas > ACPI Browser

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Focar nas tabelas DSDT e SSDT.

### Verificação antes de executar

Requer conhecimento avançado de arquitetura de computadores.

### Possíveis erros

1. Travamento ao ler tabelas.  

2. Informação incompreensível.

### Causa técnica do erro

1. BIOS com bugs na implementação ACPI.  

2. Falta de driver de chipset atualizado.

### Como identificar o erro

Software para de responder ("Scanning ACPI").

### Como corrigir (passo a passo)

SE travar ENTÃO: Atualizar a BIOS da placa-mãe para a versão mais recente. Isso geralmente corrige tabelas ACPI corrompidas.

### Validação pós-correção

Acesso à árvore de dispositivos (Device Tree) sem erros.

### Risco

Alto (Risco de Crash)

### Impacto se ignorado

Ignorar erros de ACPI pode levar a falhas de suspensão/hibernação e telas azuis DRIVER_POWER_STATE_FAILURE.

### Tempo estimado

5 min

### Observações técnicas

Ferramenta essencial para Hackintosh ou para diagnosticar por que um dispositivo não "acorda" do sleep.

### Boas práticas

Salvar as tabelas ACPI (Save Table) para enviar ao suporte do fabricante da placa-mãe em caso de bugs.

### Alternativa segura

RW-Everything (Software dedicado de leitura de hardware, mais perigoso).

### Checklist de confirmação

- [ ] BIOS Atualizada?  
- [ ] Tabelas carregaram?  
- [ ] Erros de DSDT logados?

---

## Etapa 17 — Automação via Linha de Comando (CLI)

### Objetivo da etapa

Gerar relatórios em massa sem intervenção humana (Ideal para manutenção de parque)

### Ação exata a executar

Executar o AIDA64 via script .bat ou CMD com parâmetros de relatório silencioso.

### Caminho no software

CMD / PowerShell

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Comando: aida64.exe /R c:\\logs\\$HOSTNAME /HTML /SILENT /ALL

### Verificação antes de executar

Testar o comando em uma máquina piloto antes de implantar via GPO/Rede.

### Possíveis erros

1. Relatório não gerado.  

2. AIDA64 fica aberto na tela do usuário.

### Causa técnica do erro

1. Erro de permissão de escrita na pasta destino.  

2. Faltou o parâmetro /SILENT ou /VERYSILENT.

### Como identificar o erro

Nenhum arquivo aparece na pasta de destino ou janela abre interrompendo o usuário.

### Como corrigir (passo a passo)

SE erro de escrita ENTÃO: Apontar o caminho para %TEMP% ou garantir permissão de escrita na pasta de rede compartilhada.

### Validação pós-correção

Arquivo HTML completo gerado automaticamente no caminho especificado sem interação do usuário.

### Risco

Baixo

### Impacto se ignorado

Falha na automação obriga o técnico a ir de máquina em máquina manualmente.

### Tempo estimado

N/A (Instantâneo)

### Observações técnicas

O parâmetro /CSV é melhor para importar dados em Excel posteriormente. /HTML é melhor para leitura humana.

### Boas práticas

Usar variáveis de ambiente como %COMPUTERNAME% e %DATE% no nome do arquivo para organização automática.

### Alternativa segura

Scripts VBS (mais complexos, mas ocultam janelas de CMD).

### Checklist de confirmação

- [ ] Script testado?  
- [ ] Caminho com permissão?  
- [ ] Modo silencioso ativo?

---

## Etapa 18 — Backup e Exportação de Preferências

### Objetivo da etapa

Garantir que todas as configurações personalizadas (OSD, Relatórios, Alertas) sejam salvas

### Ação exata a executar

Exportar as configurações do registro ou arquivo INI para portabilidade.

### Caminho no software

Menu Arquivo > Preferências > Botão Exportar (Canto inferior)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Salvar como: aida64.ini (na mesma pasta do executável para versão Portable).

### Verificação antes de executar

Verificar se as configurações de e-mail (SMTP) e layout do SensorPanel estão inclusas.

### Possíveis erros

1. Perda de configuração ao mudar de PC.  

2. Arquivo corrompido.

### Causa técnica do erro

1. AIDA64 instalado vs Portable usam locais de armazenamento diferentes (Registro vs INI).

### Como identificar o erro

Ao abrir em outro PC, tudo volta ao padrão (idioma inglês, sem sensores).

### Como corrigir (passo a passo)

SE configurações não carregarem ENTÃO: Renomear o arquivo exportado para aida64.ini e colocar na raiz da pasta do programa.

### Validação pós-correção

Abrir o software em uma máquina limpa e ver se o SensorPanel carrega automaticamente.

### Risco

Baixo

### Impacto se ignorado

Perder horas de personalização de layout OSD/SensorPanel.

### Tempo estimado

1 min

### Observações técnicas

A versão Portable lê automaticamente o aida64.ini se estiver ao lado do .exe. Isso torna o pendrive de diagnóstico "Plug & Play".

### Boas práticas

Manter uma cópia do .ini na nuvem.

### Alternativa segura

Configurar manualmente (inviável profissionalmente).

### Checklist de confirmação

- [ ] Arquivo .INI gerado?  
- [ ] Testado em outro PC?  
- [ ] Layout preservado?

---

## Etapa 19 — Verificação de OpenCL e GPGPU (Compute)

### Objetivo da etapa

Validar se a placa de vídeo está sendo usada para cálculos além de gráficos (CUDA/OpenCL)

### Ação exata a executar

Executar teste de extensão GPGPU.

### Caminho no software

Menu Monitor > GPU ou Ferramentas > GPGPU

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Verificar suporte a: OpenCL, CUDA, DirectCompute, Vulkan.

### Verificação antes de executar

Instalar drivers específicos (ex: CUDA Toolkit) se for workstation de renderização.

### Possíveis erros

1. Dispositivos não listados.  

2. Versão OpenCL antiga.

### Causa técnica do erro

1. Driver "Standard" do Windows Update instalado em vez do driver "DCH" ou completo do fabricante.  

2. GPU legado.

### Como identificar o erro

Softwares de edição (Premiere/DaVinci) não ativam aceleração de hardware.

### Como corrigir (passo a passo)

SE falta suporte ENTÃO: Baixar driver direto da NVidia/AMD e selecionar "Instalação Limpa".

### Validação pós-correção

Checkboxes de tecnologias suportadas devem estar marcados na tela de resumo da GPU.

### Risco

Médio

### Impacto se ignorado

Perda massiva de desempenho em renderização de vídeo e IA se o Compute não estiver ativo.

### Tempo estimado

3 min

### Observações técnicas

Essencial para diagnosticar PCs de arquitetos e editores de vídeo. O AIDA lista exatamente quais extensões o driver expõe ao SO.

### Boas práticas

Não confiar apenas no Gerenciador de Tarefas do Windows.

### Alternativa segura

GPU-Z (mostra checkboxes similares na base da janela).

### Checklist de confirmação

- [ ] CUDA/OpenCL ativo?  
- [ ] Driver Studio instalado?  
- [ ] Versão do driver checada?

---

## Etapa 20 — Validação Final e "Golden Sample"

### Objetivo da etapa

Comparar a máquina auditada com um banco de dados de referência para controle de qualidade

### Ação exata a executar

Usar o banco de dados interno para comparar o PC atual com configurações de referência.

### Caminho no software

Menu Arquivo > Banco de Dados (Requer config prévia SQL/MDB)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Adicionar o relatório atual ao banco de dados Reports.

### Verificação antes de executar

Configurar um banco de dados local (Access/MDB) nas preferências para salvar histórico.

### Possíveis erros

1. Banco de dados bloqueado.  

2. Inconsistência de dados históricos.

### Causa técnica do erro

1. Arquivo .MDB em uso por outra instância.  

2. Mudança de versão do AIDA64 altera esquema do banco.

### Como identificar o erro

Erro SQL ao tentar adicionar relatório.

### Como corrigir (passo a passo)

SE erro de DB ENTÃO: Criar um novo arquivo de banco de dados vazio via menu Preferências.

### Validação pós-correção

Ter um histórico onde se pode provar "No dia X, a temperatura era Y".

### Risco

Baixo

### Impacto se ignorado

Sem histórico, não é possível provar degradação lenta (ex: pasta térmica secando ao longo de 1 ano).

### Tempo estimado

5 min

### Observações técnicas

Esta etapa transforma o técnico de "consertador" em "auditor". Permite gerar gráficos de evolução da saúde da máquina.

### Boas práticas

Fazer backup do arquivo .MDB mensalmente.

### Alternativa segura

Salvar PDFs em pastas organizadas (menos inteligente, mas funciona).

### Checklist de confirmação

- [ ] Relatório salvo no DB?  
- [ ] Comparativo acessível?  
- [ ] Backup do DB feito?

---

## Etapa 21 — Diagnóstico de Bateria (Notebooks)

### Objetivo da etapa

Verificar a saúde química da bateria e o nível real de desgaste (Wear Level)

### Ação exata a executar

Acessar dados do controlador de carga e comparar capacidade projetada vs. atual.

### Caminho no software

Menu Computador > Gerenciamento de Energia

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Observar campo Nível de Desgaste e Taxa de Carga/Descarga.

### Verificação antes de executar

Desconectar o carregador momentaneamente para testar a taxa de descarga (mW).

### Possíveis erros

1. Dados em branco.  

2. Desgaste reportado incorretamente (0% em bateria velha).

### Causa técnica do erro

1. Bateria genérica sem chip Smart Battery.  

2. Controlador descalibrado (memória de carga viciada).

### Como identificar o erro

Campos de capacidade exibem "Unknown" ou valores estáticos.

### Como corrigir (passo a passo)

SE desgaste suspeito ENTÃO: Realizar ciclo de calibração física (carregar 100% -> descarregar 0% -> carregar 100%) e retestar.

### Validação pós-correção

O valor de Capacidade de Carga Total deve ser atualizado após o ciclo.

### Risco

Médio (Financeiro)

### Impacto se ignorado

Comprar/Vender notebook usado com bateria "viciada" sem saber, gerando prejuízo.

### Tempo estimado

2 min

### Observações técnicas

O "Wear Level" é calculado pela diferença entre a capacidade de fábrica e a capacidade máxima atual. Acima de 40% indica troca iminente.

### Boas práticas

Usar este dado para negociar preço de notebooks usados.

### Alternativa segura

powercfg /batteryreport no CMD do Windows (Nativo).

### Checklist de confirmação

- [ ] Wear Level < 20%?  
- [ ] Taxa de descarga estável?  
- [ ] Status "Carregando" OK?

---

## Etapa 22 — Auditoria de Segurança e TPM

### Objetivo da etapa

Validar compatibilidade com Windows 11 e recursos de segurança de hardware (Virtualização/DEP)

### Ação exata a executar

Verificar status do TPM 2.0, Secure Boot e Proteção de Execução de Dados.

### Caminho no software

Menu Computador > Resumo (Seção Placa Mãe e Sistema Operacional)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Verificar linhas: TPM, Secure Boot, DEP, VBS.

### Verificação antes de executar

Acessar BIOS/UEFI previamente para garantir que fTPM ou PTT estejam habilitados.

### Possíveis erros

1. TPM não detectado.  

2. Secure Boot "Desativado" mesmo estando ativo na BIOS.

### Causa técnica do erro

1. BIOS em modo Legacy (CSM) ou chip desativado.  

2. Disco em MBR impedindo o boot seguro real.

### Como identificar o erro

Windows 11 recusa instalação ou BitLocker falha ao ativar.

### Como corrigir (passo a passo)

SE TPM ausente ENTÃO:  
1. Reiniciar.  
2. BIOS.  
3. Desativar CSM/Legacy.  
4. Ativar UEFI Only + Secure Boot.

### Validação pós-correção

As linhas no resumo devem mudar para "Ativo" ou "Suportado v2.0".

### Risco

Alto

### Impacto se ignorado

Falha em criptografia de disco (BitLocker) ou impossibilidade de upgrade de SO.

### Tempo estimado

3 min

### Observações técnicas

Secure Boot exige partição GPT. Se o disco for MBR, o AIDA64 acusará "Secure Boot: Não Suportado".

### Boas práticas

Gerar relatório específico desta tela para auditoria de conformidade em empresas.

### Alternativa segura

Ferramenta "PC Health Check" da Microsoft.

### Checklist de confirmação

- [ ] TPM 2.0 Ativo?  
- [ ] Secure Boot Ativo?  
- [ ] Virtualização (VT-x) Ativa?

---

## Etapa 23 — Monitoramento Remoto (RemoteSensor)

### Objetivo da etapa

Monitorar temperaturas e voltagens de um PC/Servidor através de outra máquina na rede

### Ação exata a executar

Configurar o AIDA64 como "Servidor" em uma máquina e "Cliente" em outra.

### Caminho no software

Arquivo > Preferências > Recursos de Hardware > RemoteSensor

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Porta padrão: 8080.  

Check: Habilitar RemoteSensor.

### Verificação antes de executar

Garantir que ambos os PCs estejam na mesma sub-rede e o Firewall do Windows permita a porta.

### Possíveis erros

1. "Connection Refused".  

2. Navegador não abre a página.

### Causa técnica do erro

1. Firewall bloqueando a porta TCP.  

2. IP da máquina mudou (DHCP dinâmico).

### Como identificar o erro

Erro de conexão no navegador da máquina cliente.

### Como corrigir (passo a passo)

SE bloqueado ENTÃO: Adicionar regra de entrada no Firewall do Windows para porta 8080 (TCP).

### Validação pós-correção

Acessar http://IP-do-PC:8080 no navegador/celular e ver os dados atualizando.

### Risco

Baixo

### Impacto se ignorado

Perda de visibilidade de servidores headless (sem monitor).

### Tempo estimado

5 min

### Observações técnicas

Transforma qualquer navegador (celular, tablet) em um painel de monitoramento sem instalar apps extras.

### Boas práticas

Fixar o IP da máquina monitorada no roteador para não perder o link.

### Alternativa segura

Usar o recurso "Alertas" por e-mail (passivo) em vez de monitoramento ativo.

### Checklist de confirmação

- [ ] Servidor Web ativo?  
- [ ] Porta liberada no Firewall?  
- [ ] Acesso via IP testado?

---

## Etapa 24 — Auditoria de Instruções de CPU (CPUID)

### Objetivo da etapa

Validar suporte a instruções críticas para softwares específicos (AVX-512, AES, SHA)

### Ação exata a executar

Verificar o painel detalhado de flags do processador.

### Caminho no software

Menu Placa Mãe > CPUID

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Analisar bloco Instruction Set Extensions.

### Verificação antes de executar

Saber quais instruções o software do cliente exige (ex: Photoshop 2024 exige SSE4.2).

### Possíveis erros

1. Instruções "cinzas" (desativadas).  

2. CPU reportando suporte errado.

### Causa técnica do erro

1. BIOS desatualizada ou microcódigo antigo desabilitando instruções por bugs (ex: Skylake bug).  

2. Virtualização ocultando flags.

### Como identificar o erro

Software de renderização/CAD trava com erro "Illegal Instruction".

### Como corrigir (passo a passo)

SE instrução crítica faltante ENTÃO: Atualizar BIOS (Microcode Update). Se persistir, a CPU é incompatível fisicamente.

### Validação pós-correção

A flag (ex: AVX2) deve estar marcada e ativa.

### Risco

Médio

### Impacto se ignorado

Crash de aplicações profissionais que dependem de aceleração de hardware específica.

### Tempo estimado

2 min

### Observações técnicas

Instrução AES-NI é vital para performance de criptografia (VPN/Bitlocker). AVX é vital para renderização.

### Boas práticas

Tirar print desta tela para provar obsolescência de hardware antigo para clientes.

### Alternativa segura

CPU-Z (Aba CPU).

### Checklist de confirmação

- [ ] AVX/AVX2 suportado?  
- [ ] AES-NI suportado?  
- [ ] Virtualização (VMX/SVM) ativa?

---

## Etapa 25 — Recuperação de Licenças de Software

### Objetivo da etapa

Resgatar chaves de ativação (Product Keys) antes de formatar a máquina

### Ação exata a executar

Listar e exportar as chaves de software detectadas no registro/BIOS.

### Caminho no software

Menu Programas > Licenças

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Salvar em arquivo texto seguro imediatamente.

### Verificação antes de executar

Verificar se a licença é OEM (gravada na BIOS) ou Retail (instalada no SO).

### Possíveis erros

1. Chave não aparece.  

2. Chave parcial (apenas últimos 5 dígitos).

### Causa técnica do erro

1. Licença digital vinculada à conta Microsoft (não tem chave fixa).  

2. Office 2019/365 moderno oculta a chave completa por segurança.

### Como identificar o erro

Campo "Chave do Produto" vazio ou com texto "Digital License".

### Como corrigir (passo a passo)

SE chave oculta ENTÃO: Usar script VBS específico ou ferramenta "ShowKeyPlus" para ler a tabela MSDM da ACPI.

### Validação pós-correção

Comparar a chave extraída com a etiqueta (se houver) ou validar no site da Microsoft.

### Risco

Alto (Legal)

### Impacto se ignorado

Formatar o PC do cliente e perder a licença original do Windows/Office gera prejuízo financeiro e processual.

### Tempo estimado

1 min

### Observações técnicas

Atenção: O AIDA64 pode não ler chaves de volume (MAK/KMS) corretamente.

### Boas práticas

Nunca incluir esta página em relatórios públicos. Dados sensíveis!

### Alternativa segura

ProduKey (NirSoft) - Específico para isso.

### Checklist de confirmação

- [ ] Chave Windows copiada?  
- [ ] Chave Office copiada?  
- [ ] Arquivo salvo externamente?

---

## Etapa 26 — Integração em Ambiente WinPE

### Objetivo da etapa

Preparar o AIDA64 para rodar via Pen Drive de boot (Manutenção Offline)

### Ação exata a executar

Copiar a pasta do programa para um drive USB inicializável.

### Caminho no software

Explorador de Arquivos (Manual)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Usar versão Portable (ZIP). Não requer instalação.

### Verificação antes de executar

Ter um pendrive com Ventoy, Sergei Strelec ou Hiren's BootCD preparado.

### Possíveis erros

1. Erro de DLL faltando ao abrir no WinPE.  

2. Driver não carrega.

### Causa técnica do erro

1. Ambiente WinPE muito antigo (ex: Win7 PE) incompatível com AIDA64 moderno.  

2. WinPE de 32 bits tentando rodar AIDA64 de 64 bits.

### Como identificar o erro

Mensagem "File not found" ou "Subsystem needed".

### Como corrigir (passo a passo)

SE erro de arquitetura ENTÃO: Ter ambas as versões (aida64.exe e aida64_x64.exe) na pasta. Executar a compatível com o boot.

### Validação pós-correção

O software abre e lê sensores mesmo sem o Windows principal estar rodando.

### Risco

Baixo

### Impacto se ignorado

Ficar sem ferramentas de diagnóstico quando o Windows do cliente não inicia (BSOD/Loop).

### Tempo estimado

10 min

### Observações técnicas

Rodar pelo WinPE elimina interferência de drivers e vírus do sistema operacional infectado. É o diagnóstico mais puro possível.

### Boas práticas

Criar uma pasta \\Tools\\AIDA64 na raiz do seu pendrive de técnico.

### Alternativa segura

HWiNFO Portable (Alternativa leve).

### Checklist de confirmação

- [ ] Pasta copiada para USB?  
- [ ] Testado em boot WinPE?  
- [ ] Drivers carregaram?

---

## Etapa 27 — Limpeza e Reset Pós-Uso

### Objetivo da etapa

Garantir que nenhuma configuração ou arquivo residual fique na máquina do cliente

### Ação exata a executar

Apagar logs, relatórios gerados e remover a pasta do software (se portable).

### Caminho no software

Gerenciador de Arquivos + AIDA64

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Shift + Del na pasta de logs/relatórios.

### Verificação antes de executar

Verificar se o driver kerneld.x64 foi liberado (ver Etapa 12).

### Possíveis erros

1. Arquivos de log esquecidos na Área de Trabalho.  

2. Atalhos quebrados no Menu Iniciar.

### Causa técnica do erro

1. Falha humana na organização.  

2. Instalação via .EXE (Installer) em vez de Portable.

### Como identificar o erro

Cliente liga perguntando "O que é esse arquivo HTML na minha tela?".

### Como corrigir (passo a passo)

SE instalou via .EXE ENTÃO: Usar Revo Uninstaller para remover sobras de registro.  

SE Portable ENTÃO: Apenas deletar a pasta.

### Validação pós-correção

A máquina deve estar idêntica a antes do serviço, exceto pelos problemas resolvidos.

### Risco

Baixo (Imagem Profissional)

### Impacto se ignorado

Deixar "lixo" digital passa impressão de amadorismo.

### Tempo estimado

2 min

### Observações técnicas

Se usou SensorPanel, certifique-se de desativá-lo antes de entregar, ou o cliente verá janelas estranhas flutuando.

### Boas práticas

Criar uma pasta C:\\Manutencao_Temp e trabalhar tudo lá dentro para facilitar a limpeza final.

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Logs deletados?  
- [ ] Pasta removida?  
- [ ] Lixeira esvaziada?

---

## Etapa 28 — Conclusão e Entrega Técnica

### Objetivo da etapa

Interpretar o conjunto de dados para dar o veredito final ao cliente

### Ação exata a executar

Correlacionar Temperaturas + Voltagens + Benchmarks + S.M.A.R.T. em um diagnóstico coeso.

### Caminho no software

N/A (Análise Intelectual)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Resumir: "Hardware Saudável", "Requer Manutenção Preventiva" ou "Hardware Condenado".

### Verificação antes de executar

Revisar todos os passos anteriores (Checklist 01-27).

### Possíveis erros

1. Diagnóstico inconclusivo.  

2. Falso positivo (culpar hardware por erro de software).

### Causa técnica do erro

1. Testes insuficientes ou tempo de stress curto.  

2. Ignorar conflitos de driver.

### Como identificar o erro

O problema retorna 2 dias após a entrega.

### Como corrigir (passo a passo)

SE inconclusivo ENTÃO: Rodar testes de longa duração (Overnight - 12h) de Memória e CPU.

### Validação pós-correção

Cliente recebe um laudo técnico (PDF/HTML) baseado em fatos numéricos, não "achismos".

### Risco

Crítico (Reputação)

### Impacto se ignorado

Diagnóstico errado = Retrabalho grátis e perda de confiança.

### Tempo estimado

10 min

### Observações técnicas

O AIDA64 é a ferramenta de coleta; o técnico é o cérebro. Um relatório cheio de gráficos vermelhos precisa de explicação humana simples.

### Boas práticas

Entregar o relatório impresso ou PDF junto com a Nota Fiscal. Valoriza o serviço.

### Alternativa segura

> Informação não identificada na fonte analisada.

### Checklist de confirmação

- [ ] Laudo coerente?  
- [ ] Solução proposta?  
- [ ] Cliente ciente?

---

## Etapa 29 — Integração OSD em Jogos (RivaTuner)

### Objetivo da etapa

Exibir métricas de hardware (FPS/Temp/Hz) dentro de jogos DirectX/Vulkan

### Ação exata a executar

Vincular o AIDA64 ao RivaTuner Statistics Server (RTSS) para sobreposição.

### Caminho no software

Arquivo > Preferências > Monitoramento de Hardware > OSD (Externo)

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Ativar suporte a RivaTuner ou External Applications.

### Verificação antes de executar

O software MSI Afterburner/RTSS deve estar instalado e rodando previamente.

### Possíveis erros

1. OSD não aparece no jogo.  

2. Conflito de overlay (Steam + AIDA + Discord).

### Causa técnica do erro

1. RTSS bloqueado pelo anticheat do jogo.  

2. API de injeção gráfica sobrecarregada.

### Como identificar o erro

Jogo abre, mas sem informações na tela ou jogo fecha sozinho (Crash to Desktop).

### Como corrigir (passo a passo)

SE não aparecer ENTÃO:  
1. Abrir RTSS.  
2. Adicionar o executável do jogo.  
3. Setar "Application Detection Level" para "High".

### Validação pós-correção

As métricas escolhidas no AIDA64 aparecem coloridas no canto da tela do jogo.

### Risco

Baixo

### Impacto se ignorado

Perda de dados diagnósticos durante carga real de jogos (que é diferente de stress test sintético).

### Tempo estimado

5 min

### Observações técnicas

O AIDA64 envia os dados para a memória compartilhada, e o RTSS lê e desenha. É a forma mais leve de monitorar sem Alt-Tab.

### Boas práticas

Não poluir a tela. Exibir apenas CPU Temp, GPU Temp e FPS.

### Alternativa segura

Xbox Game Bar (Win+G) - Menos detalhado.

### Checklist de confirmação

- [ ] RTSS Instalado?  
- [ ] Memória Compartilhada Ativa?  
- [ ] OSD visível no jogo?

---

## Etapa 30 — Registro de Log Contínuo ("Black Box")

### Objetivo da etapa

Diagnosticar desligamentos aleatórios gravando sensores até o milissegundo final

### Ação exata a executar

Configurar gravação de log de sensores em arquivo CSV ou HTML para análise post-mortem.

### Caminho no software

Arquivo > Preferências > Monitoramento de Hardware > Log

### Atalho de teclado

> Informação não identificada na fonte analisada.

### Configurações recomendadas

Formato: CSV.  

Intervalo: 1 seg (ou 5 seg para logs longos).  

Caminho: Pasta segura (não temporária).

### Verificação antes de executar

Garantir espaço em disco (logs de 24h podem ficar grandes).

### Possíveis erros

1. Arquivo de log corrompido no crash.  

2. Intervalo muito curto causa lag no sistema.

### Causa técnica do erro

1. O SO não conseguiu fechar o arquivo (flush) antes do corte de energia.  

2. I/O excessivo no disco.

### Como identificar o erro

O arquivo .CSV termina abruptamente ou está cheio de caracteres NUL.

### Como corrigir (passo a passo)

SE arquivo corrompido ENTÃO: Tentar abrir com Notepad++ (que ignora formatação rígida) para ver a última linha gravada.

### Validação pós-correção

Verificar se a última linha do log coincide com o horário do travamento relatado pelo cliente.

### Risco

Médio

### Impacto se ignorado

Sem log, é impossível saber se o PC desligou por superaquecimento ou falha de fonte.

### Tempo estimado

5 min

### Observações técnicas

Esta é a ferramenta definitiva para "O PC desliga sozinho quando eu jogo, mas não sempre". A última linha do CSV revela o culpado (ex: +12V caiu para 10V).

### Boas práticas

Configurar "Sempre anexar ao arquivo" para não sobrescrever logs antigos ao reiniciar.

### Alternativa segura

Visualizador de Eventos do Windows (Event Viewer) - Menos granular.

### Checklist de confirmação

- [ ] Log CSV ativo?  
- [ ] Intervalo definido?  
- [ ] Caminho de escrita seguro?

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
| **Última verificação contra a fonte** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
