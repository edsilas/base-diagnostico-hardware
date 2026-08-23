<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — AMI Q-Code Hex**

# Referência de Códigos de Erro POST: AMI Q-Code Hex

**Aplica-se a:** Equipamentos com BIOS `AMI (Q-Code Hex)` (Ex: Placas-mãe ASUS e GIGABYTE Desktop)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos hexadecimais de erro POST (Q-Code display) da família AMI. Utilize o índice abaixo para navegar diretamente para o código exibido no display da placa-mãe.

---

## Neste artigo

- [Código 00 / D0: Erro de Inicialização da CPU](#código-00--d0-erro-de-inicialização-da-cpu)
- [Código 50 a 55: Erro de Inicialização de Memória](#código-50-a-55-erro-de-inicialização-de-memória)
- [Código 63 a 67: Falha na Fase DXE da CPU (VCore/VRM)](#código-63-a-67-falha-na-fase-dxe-da-cpu-vcorevrm)
- [Código 99 / 9A / 9C: Problema em Periféricos USB/PCIe](#código-99--9a--9c-problema-em-periféricos-usbpcie)
- [Código A0 a A2: Falha na Inicialização de Armazenamento](#código-a0-a-a2-falha-na-inicialização-de-armazenamento)
- [Código B4: Erro de Hot Plug USB (Curto/Dano)](#código-b4-erro-de-hot-plug-usb-curtodano)
- [Código D6 / D7: GPU Não Detectada](#código-d6--d7-gpu-não-detectada)
- [Código FE: Travamento Pré-POST (Curto/Estrutural)](#código-fe-travamento-pré-post-curtoestrutural)
- [Código FF: Boot Normal ou Falha Crítica](#código-ff-boot-normal-ou-falha-crítica)
- [Código 7F: Aguardando Ação do Usuário](#código-7f-aguardando-ação-do-usuário)
- [Consulte também](#consulte-também)

---

## Código 00 / D0: Erro de Inicialização da CPU

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *CPU Initialization Error* (Microcode não encontrado ou CPU não responde) |
| **Componente afetado** | CPU |
| **Fase / Camada** | SEC Phase (CPU Init) / Camada 2: CPU |
| **Criticidade** | Crítico |

### Causas
A CPU não é inicializada. O BIOS não encontra microcode compatível para a revisão (*stepping*) do processador, ou a CPU fisicamente não responde. Na prática, `00` indica que o POST sequer iniciou.
* CPU não suportada pela versão atual do BIOS.
* Pinos do socket LGA tortos ou danificados.
* Conector EPS 8-pin (alimentação da CPU) desconectado.
* VRM da placa-mãe com defeito.
* CPU fisicamente danificada.

### Diagnóstico e Resolução
**Ferramentas:** Multímetro (12V EPS, VCore), Lupa 10x, BIOS Flashback.
1. Verifique a lista de compatibilidade de CPU e BIOS no site do fabricante.
2. Se a CPU exigir BIOS mais recente: atualize-a via USB BIOS Flashback / Q-Flash Plus, recurso que não exige que a CPU seja reconhecida.
3. Inspecione o socket LGA com uma lupa. Se houver pinos tortos, tente realinhá-los cuidadosamente ou condene a placa.
4. Confirme a conexão firme do EPS 8-pin e meça a tensão de 12V.
5. Se tudo estiver OK, realize um teste cruzado com outra CPU.

### Validação
Q-Code avança para além de `00` / `D0`. A CPU é reconhecida e o POST completa adequadamente.

---

## Código 50 a 55: Erro de Inicialização de Memória

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Memory Initialization Error* (RAM não detectada ou treinamento falhou) |
| **Componente afetado** | RAM / Controladora de Memória |
| **Fase / Camada** | PEI (Memory Training) / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
Ocorre erro (sendo o `55` o mais comum) durante o treinamento inicial da RAM. Nenhum módulo DIMM é detectado ou falhou na validação de timmings.
* Nenhum módulo DIMM instalado ou instalados em slots incorretos.
* Contatos da CPU sujos (controladora de memória integrada).
* Cooler com pressão excessiva, empenando os pinos de contato do socket.
* Módulo de memória incompatível (fora da QVL).

### Diagnóstico e Resolução
**Ferramentas:** Isopropanol 99%, Lupa 10x, Escova antiestática, Lista QVL.
1. Faça o *power drain* (remova AC e drene energia).
2. Remova o cooler da CPU. Limpe os contatos LGA inferiores do processador com isopropanol 99% e escova macia.
3. Inspecione o socket buscando detritos ou pinos tortos.
4. Reinstale a CPU e o cooler **sem aplicar força excessiva**.
5. Insira 1 único módulo DIMM sabidamente bom no slot primário (geralmente `A2`).
6. Faça um Reset de CMOS, ligue a máquina e aguarde o tempo de treinamento (em plataformas DDR5, pode levar até 3 minutos).

### Validação
Q-Code avança além de `55`. RAM reconhecida com capacidade e velocidade corretas. MemTest86 sem falhas.

---

## Código 63 a 67: Falha na Fase DXE da CPU (VCore/VRM)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *CPU DXE Initialization Started* (Travamento indica falha VCore/VRM) |
| **Componente afetado** | CPU / VRM |
| **Fase / Camada** | DXE Phase / Camada 2: CPU |
| **Criticidade** | Alto |

### Causas
A fase DXE iniciou, mas travou. A CPU começou a executar rotinas avançadas, mas encontrou instabilidade geralmente ligada a alimentação.
* Capacitores do VRM defeituosos (inchados, vazando).
* VCore instável ou insuficiente entregue à CPU.
* CPU com defeito estrutural parcial.
* BIOS corrompida na região de execução.

### Diagnóstico e Resolução
**Ferramentas:** Multímetro (VCore), Inspeção visual.
1. Execute Reset do CMOS para as configurações padrão.
2. Inspecione o VRM visualmente (capacitores inchados/vazando ou MOSFETs com marcas de queimado). Se sim, a placa está condenada ou requer reparo SMD.
3. Meça o VCore sob carga simulada (tipicamente 0.8-1.4V).
4. Efetue o teste cruzado com outra CPU.
5. Se a CPU boa funcionar, o processador original está defeituoso. Se travar igualmente, há falha de VRM/PCH na placa-mãe.

### Validação
Q-Code passa de `67` e avança no POST. O sistema fica estável em carga alta (stress tests).

---

## Código 99 / 9A / 9C: Problema em Periféricos USB/PCIe

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Super IO Initialization / USB Detect* (Problema em periféricos) |
| **Componente afetado** | Super I/O / USB / PCIe |
| **Fase / Camada** | DXE I/O Init / Camada 7: Periféricos Críticos |
| **Criticidade** | Médio |

### Causas
Travamento na detecção e inicialização via Super I/O. Indica conflito ou curto em dispositivo conectado externamente ou via headers internos.
* Dispositivo USB defeituoso ou em curto.
* Front Panel (USB/Audio) do gabinete com conector danificado.
* Placa de expansão PCIe causando conflito.
* Chip Super I/O com avaria.

### Diagnóstico e Resolução
1. Desconecte TODOS os periféricos USB (traseiros e frontais).
2. Desconecte os headers internos da placa-mãe (`F_USB1`, `F_USB2`, `F_AUDIO`, etc.).
3. Tente realizar o boot mínimo (Apenas CPU, RAM, Vídeo e Fonte).
4. Se o POST completar, reconecte os *headers* e portas um a um para isolar o causador do curto/conflito.
5. Se travar mesmo com boot mínimo e sem cabos, o chip Super I/O está comprometido.

### Validação
Q-Code avança de `9C`. Todos os dispositivos USB são alocados sem travar a inicialização.

---

## Código A0 a A2: Falha na Inicialização de Armazenamento

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *IDE/SATA Initialization* (Travamento por disco/SSD) |
| **Componente afetado** | SATA / M.2 / NVMe |
| **Fase / Camada** | DXE Storage Init / Camada 7: Periféricos Críticos |
| **Criticidade** | Médio |

### Causas
Bios tentando enumerar e iniciar controladores IDE/SATA/NVMe falhou.
* SSD/HDD com firmware travado (estado *busy/hung*).
* Cabo SATA defeituoso ou conector danificado.
* SSD M.2 mal encaixado nos contatos do slot.
* Fonte falhando na tensão SATA.

### Diagnóstico e Resolução
**Ferramentas:** Teste SMART, Cabos SATA de reposição.
1. Remova a comunicação de TODOS os discos (SATA e NVMe).
2. Ligue a máquina. Se o POST avançar sem discos, reconecte-os um a um.
3. Se um disco específico causar o travamento, substitua o cabo SATA.
4. Em unidades M.2: remova, limpe com isopropanol, reinsira firmemente e parafuse o espaçador adequadamente.
5. Em caso de defeito físico no SSD, confira a saúde utilizando *CrystalDiskInfo* em outro equipamento.

### Validação
O Q-Code passa rapidamente pelas fases A0-A2, reconhece os discos de inicialização, e o boot do SO procede corretamente.

---

## Código B4: Erro de Hot Plug USB (Curto/Dano)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *USB Hot Plug Error* (USB em curto ou porta danificada) |
| **Componente afetado** | USB |
| **Fase / Camada** | DXE USB Init / Camada 7: Periféricos Críticos |
| **Criticidade** | Médio |

### Causas
O sistema detectou um curto-circuito em um dispositivo USB hot-plug inserido ou as linhas de dados da própria porta estão mecanicamente rompidas/curto-circuitadas.

### Diagnóstico e Resolução
1. Desconecte todos os dispositivos USB.
2. Utilize uma lanterna e inspecione minuciosamente os contatos internos das portas USB (traseiras e as vinculadas ao painel frontal). Procure por "línguas" plásticas quebradas ou pinos amassados se tocando.
3. Desconecte *headers* frontais.
4. Ligue a placa. Se bootar normalmente, uma das portas isoladas apresenta curto permanente (deve ser desabilitada via software ou reparada fisicamente).

### Validação
POST completa sem travamentos. Dispositivos USB funcionam sem desconexões aleatórias no SO.

---

## Código D6 / D7: GPU Não Detectada

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *No Console Output Devices Found* (GPU não detectada p/ vídeo) |
| **Componente afetado** | GPU / Saída de Vídeo |
| **Fase / Camada** | DXE Console Init / Camada 4: Vídeo |
| **Criticidade** | Alto |

### Causas
O BIOS concluiu que não há nenhum dispositivo para renderizar o console de saída. A placa de vídeo simplesmente não apareceu no barramento PCIe.
* GPU não inserida completamente no slot PCIe.
* GPU com vBIOS corrompida (ou *switch* dual BIOS na posição intermediária/defeituosa).
* Defeito na trilha/slot PCIe.
* GPU demasiadamente legada que não suporta inicialização UEFI (GOP driver ausente).

### Diagnóstico e Resolução
1. Efetue um *power drain* no sistema. Remova a GPU.
2. Limpe os contatos dourados da GPU e limpe o slot PCIe com ar comprimido/limpa contato.
3. Se a placa de vídeo tiver uma chave seletora (*Silent/OC Switch*), assegure-se de que ela está firme em um dos lados.
4. Conecte o monitor diretamente à placa de vídeo (teste variar a saída HDMI/DisplayPort).
5. Se persistir, e a placa-mãe possuir outro slot PCIe x16 (mesmo que elétrico x4/x8), teste-a no slot inferior.
6. Avalie o Reset do CMOS. Caso não resolva, isole o problema realizando um teste cruzado com uma GPU de confiança.

### Validação
Vídeo devidamente exibido, placa reconhecida. Q-Code avança do bloco D.

---

## Código FE: Travamento Pré-POST (Curto/Estrutural)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Reserved / Pre-POST Hang* (Travamento antes do POST iniciar) |
| **Componente afetado** | Placa-mãe (Estrutural) |
| **Fase / Camada** | Pre-SEC / Camada 5: Chipset / Motherboard |
| **Criticidade** | Crítico |

### Causas
Código reservado que, no mundo real das assistências, denota que o sistema *freezou* nos primeiros ciclos de energia.
* Curto-circuito grave no PCH/Chipset, trilhas internas ou malha do VRM.
* Fonte de alimentação sem capacidade de fornecer os trilhos primários de corrente.

### Diagnóstico e Resolução
1. Desconecte discos, periféricos, placa de vídeo, ventoinhas (exceto cooler CPU) e deixe 1 módulo de RAM.
2. Com o cabo ATX de 24 pinos no lugar, meça a linha `5VSB` (Fio roxo, pino 9). Ela precisa entregar ~5V.
3. Ligue o equipamento e verifique os trilhos dinâmicos (12V, 5V e 3.3V). Se a fonte não segura tensão, teste uma fonte sabidamente boa.
4. Se o problema se mantiver com tensões ideais: Realize a inspeção olfativa (marcas de queimado).
5. A ausência de defeito cosmético aliada a um código FE fixo indica condenação do PCB (em desktops) ou da *System Board* (em servidores).

### Validação
Se for apenas fonte, a inicialização ocorre sem sustos. Se houver falha de PCB, apenas a troca garante a volta das operações.

---

## Código FF: Boot Normal ou Falha Crítica

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Recovery/Boot* (A depender do timing) |
| **Componente afetado** | Variável |
| **Fase / Camada** | Variável / Camadas 6 (Firmware) ou 2 (CPU) |
| **Criticidade** | Variável |

### Causas
O Q-Code `FF` tem dualidade de comportamento, dependendo do **momento** em que ele é exibido:
1. **Se fixo IMEDIATAMENTE ao ligar:** Falha dramática. VRM/CPU mortos, ou BIOS vazia/corrompida.
2. **Se parar em FF no FINAL (após piscar outros números):** O BIOS entregou o controle ao Sistema Operacional. É o fluxo de boot normal.

### Diagnóstico e Resolução
**Código Ambíguo:** Confira a seção [Ambiguidade de códigos](../11-ambiguidades.md#q-code-ff) para aprofundamento.
1. Se exibido de imediato, e em caráter fixo, adote as práticas do código `FE` e execute uma atualização do BIOS via botão Flashback para regravar a partição corrompida.
2. Se apareceu após `A0` ou similar, não há defeito no POST. Caso você não veja imagem, o problema é restrito ao cabo, monitor ou driver de SO.

### Validação
Passagem bem sucedida para o Windows/Linux (se final) ou diagnóstico elétrico fechado.

---

## Código 7F: Aguardando Ação do Usuário

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Check User Input (Waiting)* (Sistema pausado aguardando input) |
| **Componente afetado** | Teclado / BIOS Setup |
| **Fase / Camada** | BDS (Boot Device Selection) / Camada 7: Periféricos Críticos |
| **Criticidade** | Baixo |

### Causas
Não é propriamente um erro; o fluxo natural de boot foi interrompido (exibindo usualmente uma mensagem na tela) e aguarda confirmação, comumente o pressionar de `F1` para prosseguir, ou `Del/F2` para entrar no SETUP. Isso ocorre porque o CMOS detectou uma mudança física de hardware, overclocking mal-sucedido ou configurações zeradas (bateria morta).

### Diagnóstico e Resolução
1. Conecte um teclado USB devidamente funcional (ou PS/2, se aplicável e o USB for bloqueado).
2. Verifique o monitor; caso haja indicação (`Press F1 to run SETUP`), realize a ação.
3. Se falhas de overclock geraram o gatilho, a BIOS forçou o retorno para padrão. Entre no menu, ajuste os perfis, acione `F10` para Salvar e Sair.
4. Substitua a Bateria CR2032 se a placa apresentar este código consistentemente após cortes de energia elétrica.

### Validação
Q-Code prossegue o boot; códigos vinculados à passagem de sistema operacional se iniciam e o SO entra em funcionamento.

---

## Consulte também

Para aprofundamento técnico ou informações sobre o fluxo de atendimento, consulte os documentos relacionados:

* **[Índice de códigos POST](00-indice-codigos.md):** Catálogo completo.
* **[Ambiguidade de códigos](../11-ambiguidades.md):** Verifique divergências de sinais entre fabricantes.
* **[Diagnóstico por camada](../08-diagnostico-por-camada.md):** Metodologia de testes nos subsistemas de hardware.
* **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.
* **[Validação final por componente](../13-validacao-final.md):** Testes para fechamento de atendimento.

---

| Metadados do Artigo | |
| :--- | :--- |
| **Fonte oficial** | ASUS Q-Code Reference / GIGABYTE Debug Code List / AMI |
| **Fonte primária interna** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da doc.** | `doc-2.0.0` |
