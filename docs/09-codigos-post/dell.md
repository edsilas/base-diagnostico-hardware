---
title: "Referência de Códigos de Erro POST: Dell (LED de diagnóstico)"
description: Este artigo fornece a referência completa de diagnóstico e resolução para os códigos de erro baseados em piscadas de LED (Âmbar e Branco) presentes na BIOS proprietária da Dell. Utilize o índice abaixo para navegar diretamente para o código exibido pelo equipamento.
author: Edsilas
date: 2026-08-08
---

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Dell (LED de diagnóstico)**

# Referência de Códigos de Erro POST: Dell (LED de diagnóstico)

**Aplica-se a:** Equipamentos com BIOS `Proprietário Dell` (OptiPlex, XPS, Latitude, AIO)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos de erro baseados em piscadas de LED (Âmbar e Branco) presentes na BIOS proprietária da Dell. Utilize o índice abaixo para navegar diretamente para o código exibido pelo equipamento.

---

## Neste documento

- [POST-31 — 2 Âmbar + 1 Branco: Falha no Processador (CPU)](#post-31--2-âmbar--1-branco)
- [POST-32 — 2 Âmbar + 2 Branco: Falha Geral (Placa-mãe/Fonte/Cabos)](#post-32--2-âmbar--2-branco)
- [POST-33 — 2 Âmbar + 3 Branco: Falha de Memória (RAM)](#post-33--2-âmbar--3-branco)
- [POST-34 — 2 Âmbar + 7 Branco: Falha de Tela (LCD) ou GPU](#post-34--2-âmbar--7-branco)
- [POST-35 — 3 Âmbar + 1 Branco: Falha na Bateria CMOS](#post-35--3-âmbar--1-branco)
- [POST-36 — 3 Âmbar + 3 Branco: Imagem de Recuperação BIOS Ausente](#post-36--3-âmbar--3-branco)
- [POST-37 — 3 Âmbar + 5 Branco: Falha em Trilha de Alimentação (Power Rail)](#post-37--3-âmbar--5-branco)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos ao fabricante de BIOS `Proprietário Dell`. Cada ficha reproduz integralmente os campos técnicos do código.

## Escopo

Os 7 códigos da família `Proprietário Dell`, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação e risco.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-31 — 2 Âmbar + 1 Branco

**Falha no Processador (CPU)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *CPU Failure* (Processador não detectado ou com falha) |
| **Componente afetado** | CPU |
| **Fase / Camada** | CPU Init / Camada 2: CPU |
| **Criticidade** | Crítico |

### Causas
O sistema não detectou a CPU ou o processador falhou na inicialização.
- CPU não encaixada corretamente no soquete.
- Pinos do soquete LGA tortos.
- CPU fisicamente incompatível com a placa-mãe.
- Falha elétrica no *die* do processador.

### Diagnóstico e Resolução
**Ferramentas:** Lupa, CPU de teste.
1. Efetue um *power drain* (remova a energia e sangre capacitores).
2. Abra o equipamento, remova o dissipador (girando para quebrar o selo da pasta) e retire a CPU.
3. Inspecione o soquete com a lupa em busca de pinos tortos.
4. Se íntegro, limpe e reinstale a CPU, aplicando nova pasta térmica.
5. Se o erro persistir, o processador está avariado. Substitua por um modelo idêntico ou validado no *Service Manual*.

### Validação
O LED apaga, permitindo o POST. O sistema conclui o `Dell Diagnostics` (`F12`) sem erros relativos a CPU.

---

## POST-32 — 2 Âmbar + 2 Branco

**Falha Geral (Placa-mãe/Fonte/Cabos)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *System Board / PSU / Cabling* (Falha placa-mãe, fonte ou cabeamento) |
| **Componente afetado** | Placa-mãe / PSU |
| **Fase / Camada** | Power/Board Init / Camadas 1 (Energia) e 5 (Chipset) |
| **Criticidade** | Crítico |

### Causas
Erro generalizado apontando problemas de inicialização elétrica, comumente relacionado à fonte, cabos soltos ou curto na placa.
- Fonte de alimentação avariada.
- Cabo principal mal encaixado na placa.
- Curto estrutural na placa-mãe ou em periféricos (GPU, M.2).

### Diagnóstico e Resolução
**Ferramentas:** Botão BIST da PSU Dell, Multímetro.
1. Desconecte o cabo AC.
2. Acione o botão de teste de BIST (traseira da fonte Dell). Mantenha pressionado e conecte o cabo AC.
3. Se o LED verde ascender, a fonte está funcional. Sem LED, a fonte tem defeito.
4. Se a fonte passar no teste: remova os periféricos e cabos sobressalentes.
5. Execute um Reset no CMOS via *jumper* e teste o boot em estado mínimo.
6. Se funcionar, adicione um periférico de cada vez até recriar o defeito.

### Validação
Extinção do código LED, boot completo do sistema operacional. Estabilidade sob a carga do *Dell Diagnostics*.

---

## POST-33 — 2 Âmbar + 3 Branco

**Falha de Memória (RAM)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Memory / RAM Failure* (Falha de memória RAM) |
| **Componente afetado** | RAM |
| **Fase / Camada** | Memory Detect/Init / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
O sistema não consegue inicializar a memória RAM.
- Módulos soltos ou não "clicados" totalmente.
- Módulos de memória de marca não-homologada ou especificações diferentes das aceitas pela Dell.
- Defeito nos conectores (DIMM slots).

### Diagnóstico e Resolução
**Ferramentas:** Módulo RAM compatível.
1. Retire a força e drene a energia.
2. Retire todos os módulos e passe uma borracha nos contatos.
3. Popule apenas o primeiro slot designado no manual (geralmente o slot `1`).
4. Ligue a máquina. Se houver falha, insira a RAM de teste.
5. Se falhar mesmo com módulo validado, a placa (slot ou *Memory Controller* interno) possui problema estrutural.

### Validação
Nenhum LED de alerta. Conclusão livre de erros na etapa de *Memory Test* do `Dell Diagnostics`.

---

## POST-34 — 2 Âmbar + 7 Branco

**Falha de Tela (LCD) ou GPU**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *LCD Failure (Notebook) / GPU Failure* (Falha na tela ou GPU) |
| **Componente afetado** | LCD / GPU / Cabo eDP |
| **Fase / Camada** | Video/LCD Init / Camada 4: Vídeo |
| **Criticidade** | Médio |

### Causas
Problemas na malha de exibição de vídeo (comum em Latitude, XPS e OptiPlex AIO).
- Cabo Flat (LVDS/eDP) da tela rasgado ou frouxo.
- O próprio painel de cristal líquido quebrou as vias internas.
- Defeito da placa de vídeo dedicada (Desktops).

### Diagnóstico e Resolução
**Ferramentas:** Teste BIST de tela (D + Power), Monitor Externo.
1. **Em Notebooks/AIO:** Com a máquina desligada, mantenha pressionada a tecla `D` e pressione `Power`.
2. Se a tela apresentar o ciclo de cores sólidas, o painel está fisicamente perfeito (problema é na GPU ou *drivers*).
3. Conecte um monitor externo via HDMI. Se tiver imagem, o cabo da tela interna pode estar rompido.
4. Efetue a abertura da moldura e reconecte o cabo do *display*.
5. **Em Desktops (Torre):** Proceda com a reinstalação e limpeza da GPU no slot PCIe ou efetue teste cruzado.

### Validação
Display sem cintilações e operando perfeitamente. Ferramenta de *Display Test* da BIOS com veredito "OK".

---

## POST-35 — 3 Âmbar + 1 Branco

**Falha na Bateria CMOS**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *CMOS Battery Failure* (Bateria CMOS esgotada) |
| **Componente afetado** | Bateria CR2032 |
| **Fase / Camada** | CMOS Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Baixo |

### Causas
A célula tipo moeda CR2032 que retém dados voláteis perdeu sua tensão nominal, forçando zeramento dos parâmetros e desconfigurando horários a cada inicialização sem AC.

### Diagnóstico e Resolução
1. Remova a célula da placa mãe.
2. Utilize multímetro e afira a tensão; menos de `2.8V` requer substituição.
3. Se houver tensão (ex `3.0V`), o defeito pode ser por oxidação nos terminais do "berço" da bateria. Limpe-os com álcool isopropílico.
4. Após substituição, entre no Setup (`F2`), aplique configurações corretas de data e armazenamento e salve.

### Validação
Ao desconectar totalmente da energia e esperar um período, o equipamento deve religar ostentando o horário correto da configuração.

---

## POST-36 — 3 Âmbar + 3 Branco

**Imagem de Recuperação BIOS Ausente**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *BIOS Recovery Image Not Found* |
| **Componente afetado** | BIOS / Firmware |
| **Fase / Camada** | BIOS Recovery / Camada 6: Firmware |
| **Criticidade** | Alto |

### Causas
A proteção do sistema tentou puxar o ambiente de reescrita (Recovery) em resposta a uma corrupção interna da ROM, porém falhou em encontrar a mídia com a imagem apropriada.
- Flash de recuperação inexistente.
- Pendrive no formato não suportado ou corrompido.
- Arquivo da BIOS mal nomeado.

### Diagnóstico e Resolução
**Ferramentas:** Outro PC, Pendrive (≤ 16GB, formatado em FAT32).
1. No PC funcional, utilize a etiqueta *Service Tag* no `support.dell.com` e obtenha o `.exe` contendo o BIOS do modelo.
2. Renomeie o arquivo extraído ou principal para `BIOS_IMG.rcv` (Confira o manual, em alguns casos o nome diverge).
3. Transfira para a raiz do pendrive FAT32.
4. Retorne à Dell afetada, com ela desligada, insira o pendrive e pressione `Ctrl + Esc` + `Power`. Solte o *Power* após ~5 segundos, segurando as teclas.
5. O console de recuperação subirá. Prossiga com a instalação. **Aviso:** Não interfira no fornecimento elétrico do sistema, mesmo que demore até 5 minutos.

### Validação
Ciclo encerrado. Boot completo e acesso viabilizado ao menu *Setup*.

---

## POST-37 — 3 Âmbar + 5 Branco

**Falha em Trilha de Alimentação (Power Rail)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Power Rail Failure (EC/SIO)* |
| **Componente afetado** | VRM / Power Rails / EC |
| **Fase / Camada** | Power Sequencing / Camada 1: Energia |
| **Criticidade** | Crítico |

### Causas
Interrupção ou curto no barramento gerenciado pelo Controlador Embarcado (*Embedded Controller* / SIO). Tensões como 3.3V, 5V ou similares essenciais para *handshake* não estão de pé.
- Capacitor SMD entrou em curto puxando a *rail* ao terra.
- O próprio SIO ou PCH superaqueceu e "morreu".
- Dispositivo problemático operando na malha elétrica.

### Diagnóstico e Resolução
**Ferramentas Avançadas:** Fonte de Bancada (Injeção de corrente), Câmera Térmica, Multímetro.
1. Extraia o maquinário de todos periféricos possíveis e meça, na entrada da placa (em *standby*), a via de `5VSB`.
2. Dando *Power-on*, meça os polos dinâmicos. A *rail* que entregar 0V é a defeituosa.
3. Se ao desligar um determinado flat/cabo de áudio/USB frontal a voltagem ressurgir, troque/conserte aquela subplaca.
4. Caso a voltagem falhe sem periféricos, há curto puro no PCB, implicando na troca absoluta da placa-mãe para o usuário final, ou injeção direcionada de corrente por especialista.

### Validação
Todas as linhas vitais estão nos limites de especificação; o processamento do POST prossegue sem alarmes visuais.

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou o código aqui | [Índice de códigos POST](00-indice-codigos.md) — catálogo completo |
| suspeita que o código tem outro significado | [Ambiguidade de códigos](../11-ambiguidades.md) |
| quer saber o que testar naquele subsistema | [Diagnóstico por camada](../08-diagnostico-por-camada.md) |
| aplicou a correção e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |

**Para aprofundar**

- **[Taxonomia de camadas](../03-taxonomia-camadas.md):** Entenda como uma falha interliga Energia e Chipset.
- **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.
- **[Índices cruzados](../18-indices-cruzados.md):** Outros códigos do mesmo componente ou nível de risco.

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
