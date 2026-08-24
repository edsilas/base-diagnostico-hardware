<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Award BIOS**

# Referência de Códigos de Erro POST: Award BIOS

**Aplica-se a:** Equipamentos com BIOS `Award BIOS` (Desktops Legados)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos sonoros (bipes) de erro POST da família de BIOS Award. Utilize o índice abaixo para navegar diretamente para o código de erro apresentado pelo equipamento.

---

## Neste artigo

- [1 Bipe Longo + 2 Curtos: Falha no Adaptador Gráfico](#1-bipe-longo--2-curtos-falha-no-adaptador-gráfico)
- [1 Bipe Longo + 3 Curtos: Falha na VRAM da GPU](#1-bipe-longo--3-curtos-falha-na-vram-da-gpu)
- [Bipe Repetitivo (Sirene): Superaquecimento ou Tensão Irregular](#bipe-repetitivo-sirene-superaquecimento-ou-tensão-irregular)
- [Bipe Contínuo Longo: RAM Ausente ou Não Detectada](#bipe-contínuo-longo-ram-ausente-ou-não-detectada)
- [Consulte também](#consulte-também)

---

## 1 Bipe Longo + 2 Curtos: Falha no Adaptador Gráfico

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Video Adapter Error* (Falha no adaptador gráfico) |
| **Componente afetado** | GPU / Adaptador Gráfico |
| **Fase / Camada** | Video Init / Camada 4: Vídeo |
| **Criticidade** | Alto |

### Causas
O BIOS Award não consegue inicializar o adaptador de vídeo. Em sistemas legados Award, algumas placas exigiam carga resistiva no conector VGA para detectar a presença do monitor.
* GPU não detectada ou com defeito de hardware.
* Mau contato no slot AGP ou PCIe.
* Monitor não conectado ou desligado (aplicável a sistemas Award muito antigos).
* Cabos de vídeo (ex: VGA) com fios rompidos.

### Diagnóstico e Resolução
**Ferramentas:** GPU de teste (known-good), Cabo VGA/DVI funcional.
1. Desligue a máquina e remova a energia (AC).
2. Remova a placa de vídeo e limpe os contatos dourados com uma borracha branca. Limpe o slot (AGP/PCIe) com ar comprimido.
3. Reinserir a GPU certificando-se do encaixe correto.
4. Conecte firmemente o monitor à placa e assegure-se de que ele esteja ligado e selecionado na entrada correta.
5. Se for um sistema antigo com slot AGP, verifique os jumpers/chaves de voltagem AGP na placa-mãe (3.3V vs 1.5V).
6. Se o problema persistir, teste com outra placa de vídeo para confirmar a condenação da placa original.

### Validação
O POST deve completar, emitindo 1 bipe curto (sucesso), e apresentar vídeo estável no monitor.

---

## 1 Bipe Longo + 3 Curtos: Falha na VRAM da GPU

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Video Adapter Error / VRAM* (Falha na VRAM da GPU) |
| **Componente afetado** | GPU / VRAM |
| **Fase / Camada** | Video VRAM Test / Camada 4: Vídeo |
| **Criticidade** | Alto |

### Causas
Similar ao erro de inicialização gráfica (1L+2C), porém este código denota especificamente uma falha detectada durante o teste dos bancos de memória de vídeo (VRAM).
* Módulos de VRAM soldados na GPU com células inoperantes.
* Capacitores da GPU com defeito (estufados ou vazando).
* Trincas na solda BGA sob o processador gráfico ou sob os chips de memória (*cold solder joint*).
* Fornecimento de energia insuficiente para a placa de vídeo.

### Diagnóstico e Resolução
**Ferramentas:** Inspeção visual (Lupa), GPU de teste.
1. Execute a limpeza e o reposicionamento da GPU conforme descrito no código `1 Longo + 2 Curtos`.
2. Efetue uma minuciosa inspeção visual na placa de vídeo, especialmente buscando por capacitores eletrolíticos ou sólidos estufados.
3. Certifique-se de que o conector PCIe de força adicional (6 ou 8 pinos) está conectado, se o modelo exigir.
4. Verifique se a fonte de alimentação atende aos requisitos de potência da GPU.
5. Em caso de defeito físico (capacitores ou BGA), a GPU necessitará de reparo especializado ou substituição.

### Validação
POST com sucesso, sem distorções na imagem (artefatos). Testes de estresse como o *FurMark* não devem causar travamentos ou *flickering*.

---

## Bipe Repetitivo (Sirene): Superaquecimento ou Tensão Irregular

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *CPU Overheating / Voltage Out of Range* |
| **Componente afetado** | CPU / PSU (Fonte) / Cooler |
| **Fase / Camada** | Thermal/Voltage Monitor / Camadas 1 (Energia) e 2 (CPU) |
| **Criticidade** | Crítico |

### Causas
O monitoramento de hardware do BIOS detectou que a CPU ultrapassou o limiar de temperatura segura ou que as tensões da fonte estão foras da faixa de tolerância ATX. Este código soa como uma sirene de ambulância ou alarme constante e de duas frequências.
* Cooler (ventoinha) do processador travado ou desconectado do *header* `CPU_FAN`.
* Pasta térmica totalmente ressecada, impedindo a dissipação de calor.
* Fonte de alimentação entregando voltagem incorreta (ex: flutuações na linha de 12V ou 5V).
* Overclock agressivo com tensão excessiva (VCore).

### Diagnóstico e Resolução
**Ferramentas:** Termômetro IR, Multímetro, BIOS Hardware Monitor.
1. **Desligue imediatamente** o sistema para mitigar danos físicos à CPU.
2. Verifique visualmente se a ventoinha do *cooler* gira livremente e se o conector está devidamente plugado em `CPU_FAN`.
3. Remova o bloco do dissipador, limpe completamente os resíduos, e aplique nova pasta térmica (tamanho de um grão de ervilha/arroz) antes de reinstalar.
4. Caso o alarme permaneça após tratar a refrigeração, meça as tensões primárias nos chicotes da fonte com um multímetro:
   * **12V:** 11.4 a 12.6V
   * **5V:** 4.75 a 5.25V
   * **3.3V:** 3.14 a 3.47V
5. Se as medições estiverem fora destes limites, substitua imediatamente a fonte de alimentação. Se houver configuração de *overclock*, aplique o Reset do CMOS.

### Validação
Equipamento não emite mais o alarme. O monitoramento pelo BIOS (ou via software como HWiNFO64) deve acusar tensões estáveis e temperatura de CPU em *idle* inferior a 50°C.

---

## Bipe Contínuo Longo: RAM Ausente ou Não Detectada

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Memory Not Installed or Not Detected* |
| **Componente afetado** | RAM |
| **Fase / Camada** | Memory Detect / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
O equipamento não encontrou **nenhum** módulo de RAM acessível ou operante para iniciar o uso. O aviso sonoro é um longo bipe ininterrupto (sem pausas).
* Nenhum pente de memória foi colocado nos bancos.
* Todos os pentes inseridos estão mal encaixados.
* Falha no fornecimento de energia (VDRAM) causado por defeito nos circuitos reguladores de tensão (VRM) da memória na placa-mãe.
* Controladora de memória avariada ou pinos defeituosos no soquete.

### Diagnóstico e Resolução
**Ferramentas:** Multímetro, Módulo de RAM de teste.
1. Inspecione fisicamente os slots DIMM para confirmar a presença das memórias.
2. Remova os pentes, limpe os contatos (borracha/isopropanol) e remova poeira dos slots. Reencaixe garantindo o bloqueio seguro das travas nas extremidades.
3. Tente iniciar utilizando apenas 1 pente de memória sabidamente funcional no slot primário.
4. Se o problema se mantiver com o módulo validado, utilize o multímetro nos terminais de alimentação do slot DIMM para aferir se há fornecimento da VDRAM (Ex: `1.5V` para DDR3).
5. Se a tensão apontar 0V, o circuito (VRM de memória) está defeituoso. Se a tensão estiver correta mas nada for lido, o problema está nas rotas do processador ou placa (Condenação).

### Validação
Ao inicializar, a placa deverá soar o clássico bipe curto e único de sucesso do POST, carregando a configuração da BIOS sem interrupções e identificando a capacidade da memória correta.

---

## Consulte também

Para aprofundamento técnico ou informações sobre o fluxo de atendimento, consulte os documentos relacionados:

* **[Ambiguidade de códigos](../11-ambiguidades.md):** Alguns códigos de bipes são ambíguos a depender do fabricante de BIOS (ex: [1 Longo + 2 Curtos](../11-ambiguidades.md#1-longo--2-curtos), [1 Longo + 3 Curtos](../11-ambiguidades.md#1-longo--3-curtos)). Verifique a divergência de interpretações.
* **[Taxonomia de camadas](../03-taxonomia-camadas.md):** Para casos complexos onde falhas podem englobar mais de uma camada de diagnóstico (ex: CPU + Energia).
* **[Índice de códigos POST](00-indice-codigos.md):** Catálogo completo.
* **[Diagnóstico por camada](../08-diagnostico-por-camada.md):** Metodologia de testes nos subsistemas de hardware.
* **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.
* **[Validação final por componente](../13-validacao-final.md):** Testes para fechamento de atendimento.
* **[Índices cruzados](../18-indices-cruzados.md):** Outros códigos do mesmo componente ou nível de risco.

---

| Metadados do Artigo | |
| :--- | :--- |
| **Fonte oficial** | Award BIOS Beep Code Reference / ATX PSU Spec |
| **Fonte primária interna** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da doc.** | `doc-2.0.0` |
