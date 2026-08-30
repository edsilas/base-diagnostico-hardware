---
title: "Referência de Códigos de Erro POST: HP (LED piscante)"
description: Este artigo fornece a referência completa de diagnóstico e resolução para os códigos de erro baseados em piscadas de LED (Caps Lock e Num Lock) presentes na BIOS proprietária da HP. O padrão de diagnóstico é lido pela sequência de piscadas longas seguidas de piscadas curtas. Utilize o índice abaixo para navegar diretamente para o código exibido pelo equipamento.
author: Edsilas
date: 2026-08-27
---

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — HP (LED piscante)**

# Referência de Códigos de Erro POST: HP (LED piscante)

**Aplica-se a:** Equipamentos com BIOS `Proprietário HP` (ProBook, EliteBook, ProDesk, EliteDesk, etc.)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos de erro baseados em piscadas de LED (Caps Lock e Num Lock) presentes na BIOS proprietária da HP. O padrão de diagnóstico é lido pela sequência de piscadas longas seguidas de piscadas curtas. Utilize o índice abaixo para navegar diretamente para o código exibido pelo equipamento.

---

## Neste documento

- [POST-38 — 2 Longos + 2 Curtos (2.2): Firmware BIOS Corrompido](#post-38--2-longos--2-curtos-22)
- [POST-39 — 3 Longos + 2 Curtos (3.2): Falha de Inicialização da Memória](#post-39--3-longos--2-curtos-32)
- [POST-40 — 3 Longos + 3 Curtos (3.3): Erro no Controlador Gráfico (GPU)](#post-40--3-longos--3-curtos-33)
- [POST-41 — 3 Longos + 4 Curtos (3.4): Falha de Alimentação (Energia)](#post-41--3-longos--4-curtos-34)
- [POST-42 — 4 Longos + 2 Curtos (4.2): Desligamento por Superaquecimento](#post-42--4-longos--2-curtos-42)
- [POST-43 — 5 Longos (5.0): Falha Geral da Placa-mãe](#post-43--5-longos-50)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos ao fabricante de BIOS `Proprietário HP`. Cada ficha reproduz integralmente os campos técnicos do código.

## Escopo

Os 6 códigos da família `Proprietário HP`, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação e risco.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-38 — 2 Longos + 2 Curtos (2.2)

**Firmware BIOS Corrompido**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *BIOS Corruption* (Firmware BIOS corrompido) |
| **Componente afetado** | BIOS / SPI Flash |
| **Fase / Camada** | BIOS Verify / Camada 6: Firmware |
| **Criticidade** | Crítico |

### Causas
O sistema detectou que o firmware da placa-mãe está danificado, impedindo o avanço lógico do POST.
- Interrupção/Falha de energia durante uma atualização de BIOS recente.
- Degradação natural ou falha física do chip SPI Flash.
- Possível ataque de firmware ou corrupção de sistema.

### Diagnóstico e Resolução
**Ferramentas:** Combinação `Win + B`, Pendrive (FAT32), HP BIOS Recovery.
1. **Recuperação Automática (Primária):** Com o PC desligado, mantenha pressionadas as teclas `Windows + B`. Pressione o botão *Power* por 1 segundo e solte, mas continue segurando `Win + B` por mais ~3 segundos.
2. A tela pode piscar ou ficar preta por alguns minutos antes do assistente de recuperação da HP iniciar automaticamente.
3. **Recuperação por Mídia:** Se o método acima não surtir efeito, em outro computador, baixe a versão correta da BIOS no `support.hp.com`. Extraia a ferramenta para criar um Pendrive de Recuperação e repita o processo `Win + B` com o pendrive inserido na máquina defeituosa.
4. Falha absoluta em todos os métodos lógicos pode requerer a regravação externa da EPROM via alicate/programadora (CH341A) ou a substituição da placa.

### Validação
A conclusão normal do POST, visualização da logomarca HP e a possibilidade de acessar o *Setup* (`F10`) verificando a versão atualizada e íntegra.

---

## POST-39 — 3 Longos + 2 Curtos (3.2)

**Falha de Inicialização da Memória**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Memory Initialization Failure* (Falha na inicialização da memória) |
| **Componente afetado** | RAM |
| **Fase / Camada** | Memory Init / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
A RAM não conseguiu ser reconhecida ou falhou nos testes iniciais, travando o sistema. Em notebooks corporativos da HP, isso ocorre com alta frequência por umidade e oxidação ambiental.
- Oxidação nos contatos dourados (memória ou *slot*).
- Módulo de RAM mal encaixado após manuseio.
- Incompatibilidade de barramento ou capacidade.
- Defeito estrutural do *slot* DIMM/SO-DIMM.

### Diagnóstico e Resolução
**Ferramentas:** Borracha branca, Álcool Isopropílico, Pincel Antiestático.
1. Remova a fonte de energia (e a bateria do notebook, se não for interna). Drene a carga residual pressionando o botão de ligar.
2. Extraia os módulos de RAM. Utilize a borracha branca esfregando suavemente os contatos do módulo, sempre em uma única direção.
3. Limpe o *slot* da placa-mãe com um pincel antiestático e um pouco de álcool isopropílico, garantindo a secagem completa.
4. Em notebooks, insira o pente a um ângulo de 30° e pressione para baixo até que os clipes de metal "cliquem" firmemente.
5. Em caso de falha persistente, alterne os pentes de memória e os *slots* para isolar se o defeito é no pente ou na placa-mãe.

### Validação
Os LEDs Caps/Num Lock param de piscar. O equipamento dá tela e a suíte *HP Diagnostics* (Memory Test) conclui sem alertas vermelhos.

---

## POST-40 — 3 Longos + 3 Curtos (3.3)

**Erro no Controlador Gráfico (GPU)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Graphics Controller Error* (Erro no controlador gráfico) |
| **Componente afetado** | GPU / iGPU |
| **Fase / Camada** | Video Init / Camada 4: Vídeo |
| **Criticidade** | Alto |

### Causas
Falha de *handshake* ou avaria crítica no subsistema que gera vídeo.
- Trincas ou solda fria na base BGA da GPU dedicada.
- Nas arquiteturas com gráfico integrado (UMA/iGPU), como a memória gráfica é compartilhada, o defeito pode estar no processador ou na memória RAM.
- Conflito interno de *driver* contido no firmware nativo.

### Diagnóstico e Resolução
**Ferramentas:** Monitor externo.
1. Conecte um monitor à saída lateral ou traseira do equipamento (HDMI, DP, VGA).
   - Se o externo apresentar imagem perfeitamente, o defeito restringe-se à tela original do computador ou ao cabo *flat/LVDS*.
   - Se não houver imagem nem externamente, a placa gráfica não está ativando.
2. Em equipamentos com vídeo integrado (Intel HD/UHD, AMD Radeon Graphics), realize um *Reset* do CMOS e aplique a rotina de teste de memórias RAM, que afetam diretamente o vídeo.
3. Se a máquina possui placa de vídeo dedicada e a RAM está hígida, o processador gráfico está danificado. Requer reparo especializado (substituição do *chip* / placa) em laboratório.

### Validação
Extinção do código intermitente. O painel interno acende exibindo caracteres e o ambiente pré-boot.

---

## POST-41 — 3 Longos + 4 Curtos (3.4)

**Falha de Alimentação (Energia)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Power Supply / System Board Voltage* (Falha de alimentação) |
| **Componente afetado** | PSU / DC-DC Converters |
| **Fase / Camada** | Power Sequencing / Camada 1: Energia |
| **Criticidade** | Crítico |

### Causas
O monitoramento elétrico acusou falta, subida abrupta ou queda em uma tensão crucial da placa-mãe.
- Conversores DC-DC ou capacitores primários entraram em curto.
- Carregador AC (*Power Adapter*) original com ruído elétrico ou defeito interno.
- Mau contato ou curto-circuito no *Jack DC* (conector de carga do notebook).

### Diagnóstico e Resolução
**Ferramentas:** Multímetro, Carregador AC extra confiável, Esquema Elétrico.
1. Comece eliminando a causa externa: conecte uma fonte/carregador HP sabidamente funcional, de mesma ponta (ex: ponta azul inteligente) e mesma voltagem/amperagem.
2. Inspecione visual e mecanicamente o conector de energia do computador (*Jack DC*). Veja se o pino central (Agulha) está torto ou quebrado. Observe se o LED de recepção de carga acende na lateral do PC.
3. Em *Desktops*, teste a fonte de alimentação de forma isolada ou utilize o botão de auto-teste da fonte. Se apresentar tensões instáveis, substitua-a.
4. Se carregador e *Jack* estão OK e o problema persiste em notebooks, trata-se de um problema complexo na placa-mãe exigindo solda de precisão baseada em esquema elétrico.

### Validação
Toda a arvore de voltagens sobe corretamente, não gerando alarmes para o *Embedded Controller*. O equipamento opera com estabilidade energética e carrega a bateria.

---

## POST-42 — 4 Longos + 2 Curtos (4.2)

**Desligamento por Superaquecimento**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Thermal Shutdown* (Desligamento por superaquecimento) |
| **Componente afetado** | CPU / Fan / Sistema térmico |
| **Fase / Camada** | Thermal Monitor / Camada 2: CPU / Camada 1: Energia |
| **Criticidade** | Médio |

### Causas
A proteção do hardware armou-se para prevenir danos derretendo silício após a placa não conseguir dissipar calor efetivamente.
- Ventilador (*Fan/Cooler*) obstruído por sujeira maciça, fios travando a hélice, ou motor inoperante.
- Interface térmica (pasta térmica, *pads*) profundamente ressecada.
- Dissipador de calor afrouxado por transporte mecânico brusco.
- Bloqueio severo das saídas de exaustão do gabinete/carcaça.

### Diagnóstico e Resolução
**Ferramentas:** Ar comprimido, Pasta Térmica (Ex: Prata/Cerâmica), Fonte de Bancada.
1. Acione o botão *Power* com a carcaça aberta e monitore o comportamento acústico e visual da ventoinha.
2. Se não girar: Confirme se o cabo do *Fan* está no *header* `CPU_FAN` da placa. Teste-o recebendo 5V (notebooks) ou 12V (desktops) em bancada. Se morto, compre uma peça de reposição.
3. Se girar normalmente: A falha é na transferência térmica. Remova o dissipador, efetue limpeza exaustiva com álcool isopropílico no *die* do processador e na chapa de cobre.
4. Aplique uma gota central de pasta térmica de alta condutividade e aperte os parafusos do dissipador cruzando-os em 'X'. Utilize ar comprimido na grade da carcaça.

### Validação
Os LEDs cessam as piscadas. POST segue sem acionar os "limites máximos" do ventilador. Monitoramento atesta temperas *Idle* inferiores a `50°C`.

---

## POST-43 — 5 Longos (5.0)

**Falha Geral da Placa-mãe**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *General System Board Failure* (Falha geral da placa-mãe) |
| **Componente afetado** | Placa-mãe / KBC / SIO |
| **Fase / Camada** | Board Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Crítico |

### Causas
Os controladores mestre (*Embedded Controller*, *Super I/O*, *KBC*) pararam de se comunicar adequadamente, ou um dano físico/elétrico no PCB interrompeu trilhas vitais do sistema. É uma falha terminal sem refinamento secundário.

### Diagnóstico e Resolução
1. Para exclusão de pane temporária (lixo elétrico ou *bug* persistente de estado), realize um *hard reset*:
   - Remova totalmente qualquer alimentação AC e Baterias Principais.
   - Remova a bateria *Moeda* (*Coin Cell CMOS*).
   - Mantenha o botão *Power* pressionado por 60 segundos contínuos.
   - Abandone a placa desenergizada por 30 minutos.
2. Após o tempo estipulado, remonte minimamente a estrutura e tente ligar.
3. Se o código 5.0 reaparecer, a placa-mãe está definitivamente avariada. Deve-se providenciar reparo de PCB por laboratório avançado ou substituir a placa (Em caso de parques corporativos com garantia HP válida, este é o momento de acioná-la para troca da *Motherboard*).

### Validação
Em caso de "ressurreição" pelo *reset*, a placa completa o POST. Nos demais cenários, aplica-se a substituição do ativo.

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou o código aqui | [Índice de códigos POST](00-indice-codigos.md) — catálogo completo |
| suspeita que o código tem outro significado | [Ambiguidade de códigos](../11-ambiguidades.md) |
| quer saber o que testar naquele subsistema | [Diagnóstico por camada](../08-diagnostico-por-camada.md) |
| aplicou a correção e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |

**Para aprofundar**

- **[Taxonomia de camadas](../03-taxonomia-camadas.md):** Entenda como o thermal monitor (Código 4.2) exige atenção em múltiplas camadas.
- **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
