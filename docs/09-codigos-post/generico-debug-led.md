---
title: "Referência de Códigos de Erro POST: Genérico (Debug LED)"
description: Este artigo fornece a referência completa de diagnóstico e resolução para os códigos visuais informados pelos 4 LEDs de status (CPU, DRAM, VGA, BOOT) presentes na maioria das placas-mãe modernas. Utilize o índice abaixo para navegar diretamente para o LED que permanece aceso estaticamente na placa.
author: Edsilas
date: 2026-08-25
---

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Genérico — Debug LED**

# Referência de Códigos de Erro POST: Genérico (Debug LED)

**Aplica-se a:** Equipamentos com BIOS `Genérico (Múltiplos)` (Placas-mãe modernas com *EZ Debug LED*: ASUS, GIGABYTE, MSI, ASRock, etc.)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos visuais informados pelos 4 LEDs de status (CPU, DRAM, VGA, BOOT) presentes na maioria das placas-mãe modernas. Utilize o índice abaixo para navegar diretamente para o LED que permanece aceso estaticamente na placa.

---

## Neste documento

- [POST-51 — LED CPU (Vermelho): Falha na CPU](#post-51--led-cpu-vermelho)
- [POST-52 — LED DRAM (Amarelo): Falha no Treinamento de Memória](#post-52--led-dram-amarelo)
- [POST-53 — LED VGA (Branco): GPU Não Detectada](#post-53--led-vga-branco)
- [POST-54 — LED BOOT (Verde): Dispositivo de Boot Não Encontrado](#post-54--led-boot-verde)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos ao fabricante de BIOS `Genérico (Múltiplos)`. Cada ficha reproduz integralmente os campos técnicos do código.

## Escopo

Os 4 códigos da família `Genérico (Múltiplos)`, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação e risco.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-51 — LED CPU (Vermelho)

**Falha na CPU**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *CPU Not Detected / Fail* (CPU não detectada ou com falha) |
| **Componente afetado** | CPU / VRM / EPS |
| **Fase / Camada** | SEC/PEI (CPU Init) / Camada 2: CPU |
| **Criticidade** | Crítico |

### Causas
O LED de diagnóstico travado na indicação da CPU aponta falha primária na inicialização do processador.
- Cabo EPS 8-pin (alimentação da CPU) desconectado da fonte ou da placa.
- Pinos do soquete LGA tortos.
- BIOS instalada não suporta a geração do processador instalado.
- Defeito elétrico/estrutural na CPU.
- Circuito regulador de tensão (VRM) da placa-mãe com avaria.

### Diagnóstico e Resolução
**Ferramentas:** Multímetro (EPS 12V), Lupa 10x, BIOS Flashback.
1. Verifique se o cabo de energia EPS 8-pin (ou 4+4) está firmemente conectado na placa-mãe e modularmente na fonte.
2. Utilize um multímetro para garantir que o cabo EPS está entregando 12V constantes. Se ausente, o cabo ou a fonte falharam.
3. Se as tensões estão OK, verifique a compatibilidade CPU-BIOS no site da fabricante da placa. Se a CPU for mais nova que a placa, utilize o recurso *BIOS Flashback* (ou *Q-Flash Plus*) para atualizar sem precisar dar vídeo.
4. Remova o dissipador e a CPU e inspecione o soquete com a lupa. Se houver pinos tortos, tente realinhar ou condene a placa.
5. Se nenhuma inspeção física ou atualização solucionar, realize o teste cruzado trocando a CPU.

### Validação
O LED vermelho correspondente à CPU apaga, e a sequência passa para o LED DRAM (que acenderá brevemente e apagará), finalizando o POST.

---

## POST-52 — LED DRAM (Amarelo)

**Falha no Treinamento de Memória**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Memory Training Fail* (Falha no treinamento de memória) |
| **Componente afetado** | RAM / Controladora |
| **Fase / Camada** | PEI (Memory Training) / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
O LED DRAM aceso indica que o sistema empacou ao tentar sincronizar e treinar as frequências/timings da memória.
- **Aviso para DDR5:** O treinamento normal pode demorar até 3 minutos ou mais na primeira vez (Não se trata de falha).
- Módulo de RAM mal encaixado nos *slots*.
- Povoamento incorreto dos *slots* (ex: ignorar a recomendação de preencher primeiro o `A2`).
- Módulos incompatíveis ou de velocidades conflitantes misturados.
- Cache de configurações antigas no CMOS que impedem o *boot* da nova memória.

### Diagnóstico e Resolução
**Ferramentas:** Cronômetro, QVL do fabricante da Placa, Módulo RAM de teste.
1. **Primeiro passo obrigatório (Especialmente AM5 / DDR5):** Ao ligar a máquina após instalar RAM nova ou resetar a BIOS, aguarde 3 minutos inteiros. O LED DRAM ficará aceso enquanto a placa realiza o treinamento.
2. Se após a espera o LED persistir, desligue e faça o *power drain*. 
3. Remova todos os módulos de memória e execute o Reset do CMOS (feche o *jumper* correspondente).
4. Insira apenas 1 pente no *slot* prioritário da placa (consulte o manual, geralmente `A2`). Ligue e aguarde novamente.
5. Se falhar, limpe os contatos e teste outro pente de memória de modelo homologado (QVL).
6. A falha recorrente com memórias funcionais aponta para avaria na controladora da memória (na CPU) ou dano aos *slots* da placa.

### Validação
O LED amarelo apaga, passando o bastão para o LED VGA e, sucessivamente, concluindo o POST. A memória será integralmente identificada no SO.

---

## POST-53 — LED VGA (Branco)

**GPU Não Detectada**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *VGA Not Detected* (GPU não detectada) |
| **Componente afetado** | GPU / Slot PCIe |
| **Fase / Camada** | DXE (Video Init) / Camada 4: Vídeo |
| **Criticidade** | Alto |

### Causas
O sistema ligou processador e memória, mas paralisou por não encontrar hardware para prover saída gráfica.
- Placa de vídeo (GPU) dedicada mal encaixada no barramento PCIe.
- Cabos auxiliares de energia da GPU (6+2 pinos) não conectados.
- **Peculiaridade de algumas placas:** O LED pode acender se o cabo do monitor estiver desconectado ou o monitor desligado, pois a BIOS não completa o *handshake* (comum em conexões DisplayPort).
- Cabo HDMI/DP avariado.
- Placa de vídeo danificada.

### Diagnóstico e Resolução
**Ferramentas:** Cabo de vídeo funcional, Monitor energizado, GPU de teste.
1. Assegure-se de que o monitor está LIGADO na tomada e selecionado exatamente na entrada de vídeo correta antes de acionar o *Power* do PC.
2. Substitua preventivamente o cabo DisplayPort ou HDMI.
3. Desligue, remova a placa de vídeo, limpe os contatos dourados, reinsira no *slot* e cheque com firmeza os cabos vindos da fonte.
4. Se o seu processador possuir gráficos integrados (iGPU), remova completamente a placa de vídeo dedicada e conecte o monitor diretamente nas portas traseiras da placa-mãe.
5. Se a iGPU der vídeo (LED branco apagar), efetue um teste cruzado colocando a placa dedicada suspeita em outro PC de bancada.

### Validação
O LED VGA branco apaga, o fabricante logomarca sobe na tela e o último LED pisca momentaneamente.

---

## POST-54 — LED BOOT (Verde)

**Dispositivo de Boot Não Encontrado**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Boot Device Missing* (Dispositivo de boot não encontrado) |
| **Componente afetado** | SSD / HDD / NVMe / Config BIOS |
| **Fase / Camada** | BDS (Boot Device Selection) / Camada 7: Periféricos Críticos |
| **Criticidade** | Médio |

### Causas
O POST de *hardware* já passou perfeitamente (Processador, RAM e GPU estão operacionais). A máquina travou porque não localizou nenhum arquivo de Sistema Operacional (`bootloader`) ou disco inicializável.
- SSD, NVMe ou HDD inoperante (queimado).
- Instalação do Windows/Linux gravemente corrompida (setor de boot apagado).
- Conflito de configuração: SO instalado em modo Legacy/CSM, mas BIOS atualizada e travada em modo puramente UEFI (ou vice-versa).
- Ordem de boot (`Boot Priority`) desconfigurada.
- SSD M.2 mal conectado ou com folga no parafuso; Cabo SATA solto.

### Diagnóstico e Resolução
**Ferramentas:** Pendrive Bootável (Linux Live / Win PE), Acesso ao BIOS Setup.
1. Reinicie e entre imediatamente no Setup da BIOS (`Del` ou `F2`).
2. Vá à aba de Armazenamento/Storage e verifique se o SSD/HDD é listado eletronicamente.
   - **Se o disco não aparecer:** Desligue. Remova, limpe e reinstale o M.2. Para SSDs SATA, substitua o cabo de dados e verifique o de energia.
3. Se o disco for listado, verifique a ordem de inicialização (Boot Order) e garanta que o Windows Boot Manager seja o primeiro.
4. Alterne o suporte CSM (*Compatibility Support Module*). Se o seu Windows é antigo (Legacy), ligue o CSM. Se for moderno (UEFI), desligue o CSM e ative o Secure Boot. Salve e reinicie.
5. Empaque persistente exige o uso de um Pendrive Bootável com ferramentas do Windows (`bootrec /rebuildbcd`) para reparar o setor de boot da unidade, ou sua eventual formatação e reinstalação.

### Validação
O LED BOOT (Geralmente Verde ou Amarelo-esverdeado) acende rapidamente para validar a partição e se apaga. A logomarca do sistema operacional de fato inicia o carregamento.

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou o código aqui | [Índice de códigos POST](00-indice-codigos.md) — catálogo completo |
| suspeita que o código tem outro significado | [Ambiguidade de códigos](../11-ambiguidades.md) |
| quer saber o que testar naquele subsistema | [Diagnóstico por camada](../08-diagnostico-por-camada.md) |
| aplicou a correção e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |

**Para aprofundar**

- **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
