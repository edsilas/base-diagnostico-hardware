<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Phoenix BIOS**

# Referência de Códigos de Erro POST: Phoenix BIOS

**Aplica-se a:** Equipamentos com `Phoenix BIOS` (Desktops e Servidores clássicos e corporativos)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos de erro baseados em bipes sonoros presentes nas placas com Phoenix BIOS. O padrão de diagnóstico da Phoenix é caracterizado por bipes agrupados em sequências (ex: 1 bipe, pausa, 2 bipes, pausa, etc.). Utilize o índice abaixo para navegar diretamente para a sequência identificada.

---

## Neste artigo

- [1-1-1-3: Falha de Modo Real (CPU/MB)](#1-1-1-3-falha-de-modo-real-cpumb)
- [1-2-2-3: Falha de Integridade do Firmware (ROM)](#1-2-2-3-falha-de-integridade-do-firmware-rom)
- [1-3-1-1: Falha no Teste de Refresh da RAM](#1-3-1-1-falha-no-teste-de-refresh-da-ram)
- [1-3-4-1: Falha em Linha de Endereço da RAM](#1-3-4-1-falha-em-linha-de-endereço-da-ram)
- [1-4-2-1: Falha no Clock RTC do CMOS](#1-4-2-1-falha-no-clock-rtc-do-cmos)
- [Consulte também](#consulte-também)

---

## 1-1-1-3: Falha de Modo Real (CPU/MB)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Verify Real Mode* (CPU/MB falha ao entrar em modo real x86) |
| **Componente afetado** | CPU / Placa-mãe |
| **Fase / Camada** | SEC Phase (Real Mode Init) / Camada 2: CPU |
| **Criticidade** | Crítico |

### Causas
A CPU não consegue iniciar o modo real (*Real Mode*), primeiro modo de operação arquitetural x86 após o acionamento de energia. Indica falha crítica primária.
* Processador morto ou em curto (não executa nenhuma instrução).
* Falha grave no barramento de comunicação da CPU na placa-mãe.
* Circuito regulador de tensão (VRM) da placa sem saída de energia.
* Danos severos nos pinos do *socket* da placa-mãe.

### Diagnóstico e Resolução
**Ferramentas:** Multímetro (Leitura de VCore), CPU de Teste Homologada.
1. Ligue o equipamento e verifique se há sinais de vida secundários (ventoinhas girando, LEDs). Se as ventoinhas giram, mas o erro surge, a CPU não está operando.
2. Com o multímetro, afira a tensão VCore nos pontos de teste ou indutores do VRM próximos ao processador.
   * Se o `VCore = 0V`, o VRM está defeituoso ou a CPU apresenta um curto-circuito grave desarmando a fonte.
   * Se a tensão VCore estiver presente e correta, a probabilidade é que a CPU esteja inoperante.
3. Teste o processador defeituoso em outra placa ou utilize uma CPU funcional (*known-good*) na placa em bancada.
4. Se o erro 1-1-1-3 continuar com uma CPU sabidamente boa, a placa-mãe deve ser condenada.

### Validação
O equipamento passa no POST, a CPU avança do modo real para o modo protegido e o carregamento do Sistema Operacional é iniciado.

---

## 1-2-2-3: Falha de Integridade do Firmware (ROM)

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *BIOS ROM Checksum* (Falha de integridade do firmware) |
| **Componente afetado** | BIOS / EEPROM |
| **Fase / Camada** | BIOS Verify / Camada 6: Firmware |
| **Criticidade** | Crítico |

### Causas
A validação criptográfica (Checksum) do arquivo de BIOS falhou, o que significa que o código necessário para ligar a máquina está ilegível ou incompleto.
* Desligamento repentino ou falha elétrica durante uma atualização de BIOS.
* Chip SPI Flash/EEPROM degradado por tempo de vida útil ou pico elétrico.
* Bateria CR2032 esgotada, gerando lixo na memória e corrupção das configurações.

### Diagnóstico e Resolução
**Ferramentas:** Bateria CR2032 Nova, Pendrive FAT32, Programadora EPROM (CH341A).
1. Substitua preventivamente a bateria CR2032 por uma nova.
2. Tente acionar o recurso de *BIOS Recovery* (Recuperação nativa). O método de ativação varia dependendo da fabricante final da placa (ex: apertar combinações de teclas específicas usando um pendrive com o arquivo ROM extraído).
3. Caso a placa não suporte ou não reaja à recuperação via USB, será necessário utilizar uma programadora externa (como a CH341A). Identifique o chip BIOS, baixe o firmware confiável e proceda com a regravação via hardware.

### Validação
Os bipes cessam, o POST completa sem erros. É possível acessar o *Setup* da BIOS, salvar configurações e confirmar que a data/hora permanecem inalteradas após o desligamento.

---

## 1-3-1-1: Falha no Teste de Refresh da RAM

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *DRAM Refresh Test* (Falha no teste de refresh da DRAM) |
| **Componente afetado** | RAM / Slots DIMM |
| **Fase / Camada** | Memory Init / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
As memórias dinâmicas necessitam de um ciclo de *refresh* elétrico contínuo para não perderem dados. A placa acusou falha nesse circuito.
* O próprio pente de memória (Módulo DIMM) está avariado.
* Pinos amassados ou oxidados no interior do *slot* DIMM da placa-mãe.
* Controladora de memória (interna à CPU) apresentando instabilidade.

### Diagnóstico e Resolução
**Ferramentas:** Lupa de Bancada (10x), RAM de Teste Homologada.
1. Desligue, remova todos os pentes de memória e reinsira-os (ação de *Reseat*), garantindo que a pressão seja firme e uniforme em ambas as extremidades.
2. Utilize uma lupa de 10x acoplada com lanterna para inspecionar rigorosamente o interior do plástico dos *slots* DIMM. Procure por pinos abaixados, cruzados ou poeira incrustada.
3. Teste o equipamento com apenas 1 pente de memória *known-good* inserido estritamente no *slot* primário designado pelo manual da placa.
4. Avance testando o pente funcional em cada *slot* individual. Se todos os *slots* falharem e o processador integrar a controladora de memória (padrão atual), a falha pode estar na CPU ou em suas trilhas de comunicação.

### Validação
Extinção dos bipes e POST bem-sucedido. Recomenda-se rodar o *MemTest86* por pelo menos 1 ciclo (*pass*) sem registrar erros.

---

## 1-3-4-1: Falha em Linha de Endereço da RAM

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *RAM Failure on Address Line* (Falha em linha de endereço da RAM) |
| **Componente afetado** | RAM / Trilhas da Placa-mãe |
| **Fase / Camada** | Memory Address Test / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
Erro de hardware altamente específico em que a controladora consegue energizar a RAM, mas não consegue endereçar/localizar um bloco específico de memória (Address Bus).
* *Chip* lógico individual de memória (CI preto no pente) defeituoso.
* Trilha microscópica rompida na placa-mãe no percurso entre a CPU e o *slot* DIMM.
* Microfissuras ou solda fria nas soldagens inferiores do *slot* DIMM na placa.
* Controladora de memória (CPU) parcialmente queimada.

### Diagnóstico e Resolução
**Ferramentas:** Módulo RAM Funcional, Multímetro (Continuidade), Esquema Elétrico.
1. O passo inicial isola o componente mais barato: remova o pente suspeito e coloque um que se saiba estar perfeito.
2. Se o computador ligar bem, descarte a RAM original, pois a mesma está avariada.
3. Se a falha persistir mesmo com a memória boa:
   * Mude a memória para o *slot* secundário. Se no secundário funcionar, o *slot* primário possui trilha rompida ou solda fria profunda na placa-mãe.
   * Se falhar identicamente em todos os *slots*, há um dano no barramento da controladora de memória contida na CPU.
4. Um reparo de trilha exige esquema elétrico para o teste de continuidade (Técnica avançada).

### Validação
POST limpo. O sistema identifica integralmente a capacidade total instalada, e ferramentas de estresse lógico como o *MemTest86* não acusam anomalias de endereçamento.

---

## 1-4-2-1: Falha no Clock RTC do CMOS

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *CMOS Clock Test* (Falha no clock RTC do CMOS) |
| **Componente afetado** | CMOS / RTC / Cristal 32kHz |
| **Fase / Camada** | RTC Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Médio |

### Causas
O relógio de tempo real da placa (RTC), fundamental para a criptografia e agendamento de eventos do sistema, parou de funcionar.
* Bateria do CMOS (CR2032) entregando voltagem insuficiente (inferior a 2.8V).
* Cristal oscilador SMD de 32.768 kHz inoperante ou com solda fria.
* Circuito interno de RTC no Chipset (PCH/Southbridge) queimado.

### Diagnóstico e Resolução
**Ferramentas:** Multímetro, Osciloscópio, Bateria CR2032 Nova, Componente Cristal SMD (opcional).
1. Aferir a tensão da bateria tipo moeda atual e, se estiver abaixo de 3.0V, substituí-la por uma nova.
2. Realize o reset completo (*Clear CMOS*), ligue a máquina e configure a data e a hora atualizadas dentro do *Setup*. Salve e saia.
3. Desligue a máquina da tomada, aguarde cerca de 10 minutos e torne a ligá-la. Verifique se o erro retorna e a hora foi zerada.
4. Se o problema for persistente com bateria nova: O cristal oscilador de 32.768 kHz falhou.
   * Laboratórios equipados utilizam osciloscópio para validar a oscilação nos pinos do componente.
   * Havendo experiência em microsolda (SMD), o cristal pode ser substituído (componente de baixíssimo custo). Sem isso, a placa deverá ser condenada ou o usuário terá que aceitar a inconveniência do relógio perdendo sincronismo a cada *reboot*.

### Validação
Relógio e datas mantidos intactos mesmo com o computador desconectado da tomada. Cristal comprovadamente oscilando com frequência estável em 32.768 kHz (tolerância ±20ppm).

---

## Consulte também

Para aprofundamento técnico ou informações sobre o fluxo de atendimento, consulte os documentos relacionados:

* **[Índice de códigos POST](00-indice-codigos.md):** Catálogo completo.
* **[Ambiguidade de códigos](../11-ambiguidades.md):** Verifique divergências de sinais entre fabricantes.
* **[Diagnóstico por camada](../08-diagnostico-por-camada.md):** Metodologia de testes nos subsistemas de hardware.
* **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.
* **[Validação final por componente](../13-validacao-final.md):** Testes recomendados para fechamento de atendimento com segurança.

---

| Metadados do Artigo | |
| :--- | :--- |
| **Fonte oficial** | Phoenix BIOS Technical Reference Manual |
| **Fonte primária interna** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da doc.** | `doc-2.0.0` |
