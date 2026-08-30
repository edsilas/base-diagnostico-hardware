---
title: "Referência de Códigos de Erro POST: Apple EFI (Mac Intel)"
description: Este artigo fornece a referência completa de diagnóstico e resolução para os códigos sonoros (tons de erro) da interface de firmware extensível (EFI) da Apple em equipamentos com processadores Intel. Utilize o índice abaixo para navegar diretamente para o código de erro apresentado pelo equipamento.
author: Edsilas
date: 2026-08-08
---

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Apple EFI (Mac Intel)**

# Referência de Códigos de Erro POST: Apple EFI (Mac Intel)

**Aplica-se a:** Equipamentos com BIOS `Apple (EFI)` (Família Mac Intel: iMac, MacBook, Mac Pro, Mac Mini)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos sonoros (tons de erro) da interface de firmware extensível (EFI) da Apple em equipamentos com processadores Intel. Utilize o índice abaixo para navegar diretamente para o código de erro apresentado pelo equipamento.

---

## Neste documento

- [POST-46 — 1 Tom repetido a cada 5 segundos: RAM Não Instalada](#post-46--1-tom-repetido-a-cada-5-segundos)
- [POST-47 — 3 Tons repetidos a cada 5 segundos: Falha de Integridade da RAM](#post-47--3-tons-repetidos-a-cada-5-segundos)
- [POST-48 — 3 Longos + 3 Curtos + 3 Longos (SOS): Firmware Corrompido](#post-48--3-longos--3-curtos--3-longos-sos)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos ao fabricante de BIOS `Apple (EFI)`. Cada ficha reproduz integralmente os campos técnicos do código.

## Escopo

Os 3 códigos da família `Apple (EFI)`, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação e risco.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-46 — 1 Tom repetido a cada 5 segundos

**RAM Não Instalada**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *No RAM Installed* (Nenhuma memória RAM instalada) |
| **Componente afetado** | RAM |
| **Fase / Camada** | Memory Detect / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
O firmware EFI do Mac não conseguiu detectar nenhum módulo de memória RAM presente no barramento.
- Nenhum módulo RAM fisicamente instalado.
- Módulos mal encaixados nos conectores.
- RAM incompatível (Ex: Uso de memória DDR3 de 1.5V em vez de DDR3L de 1.35V exigida por diversos modelos de Mac).
- Slot de memória com defeito.

### Diagnóstico e Resolução
**Ferramentas:** Especificações da Apple (support.apple.com), Módulos de RAM compatíveis.
1. Desligue o Mac completamente e desconecte o cabo de força.
2. Acesse o compartimento de RAM:
   - **iMac:** Utilize a ferramenta adequada ou o botão no compartimento traseiro (depende do ano/modelo).
   - **MacBook (modelos não soldados):** Remova os parafusos da tampa inferior.
3. Remova os módulos e verifique as especificações. Confirme se as voltagens (DDR3 vs DDR3L) e frequências batem com a exigência exata do modelo.
4. Limpe os contatos dos módulos com uma borracha branca e remova resíduos.
5. Reinserir os módulos firmemente (assegure-se de ouvir/sentir o clique das travas laterais).
6. Se o erro persistir com RAM sabidamente compatível e boa, há falha no slot ou na controladora da placa lógica.

### Validação
O tom sonoro cessa. O Mac inicia a tela com o logotipo da Apple e carrega o macOS. No menu Apple () > "Sobre Este Mac", a RAM é exibida com a capacidade e a frequência corretas.

---

## POST-47 — 3 Tons repetidos a cada 5 segundos

**Falha de Integridade da RAM**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *RAM Integrity Failed* (RAM não passou no teste de integridade) |
| **Componente afetado** | RAM |
| **Fase / Camada** | Memory Test / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
A memória RAM foi detectada (ou seja, existe fisicamente e envia pulsos), mas falhou no teste de leitura/escrita de integridade exigido pela Apple EFI.
- Módulo com defeito físico (células inoperantes).
- RAM incompatível, forçando frequências ou temporizações erradas.
- Uso misto de módulos incompatíveis entre si (marcas ou *timings* variados).
- Controladora de memória com falha parcial.

### Diagnóstico e Resolução
**Ferramentas:** Módulo de RAM compatível (known-good).
1. Efetue a redefinição (Reset) da NVRAM: Desligue o Mac, ligue e imediatamente segure as teclas `Option + Command + P + R` por cerca de 20 segundos (até ouvir o segundo som de inicialização ou o logo da Apple aparecer e sumir pela segunda vez).
2. Se persistir, desligue o equipamento e remova todos os módulos de memória, exceto um.
3. Ligue e teste. Se funcionar sem tons de erro, adicione os demais módulos, um de cada vez, até identificar o pente defeituoso.
4. Caso o teste falhe já no primeiro módulo, substitua-o por um sobressalente sabidamente compatível.
5. Em configurações com múltiplos módulos, certifique-se de preencher sempre com módulos de especificações idênticas (marca, frequência, CL, voltagem).

### Validação
O Mac inicia normalmente. A ferramenta de Diagnóstico da Apple (iniciada ao segurar a tecla `D` durante o boot) reporta que não há problemas de hardware (Código `ADP000`).

---

## POST-48 — 3 Longos + 3 Curtos + 3 Longos (SOS)

**Firmware Corrompido**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *EFI ROM Corrupted* (Firmware EFI corrompido) |
| **Componente afetado** | EFI / Firmware |
| **Fase / Camada** | EFI Verify / Camada 6: Firmware |
| **Criticidade** | Crítico |

### Causas
O padrão sonoro universal de SOS em código Morse (···−−−···) indica que o firmware EFI central está gravemente corrompido e o Mac acionou a rotina de recuperação.
- Interrupção de energia durante uma atualização do macOS/Firmware.
- Corrupção física do chip SPI Flash.
- Degradação geral do firmware.
- Em Macs equipados com o chip de segurança Apple T2: O bridgeOS ou o firmware do chip T2 encontram-se corrompidos.

### Diagnóstico e Resolução
**Ferramentas:** Outro computador Mac (Mac Host), Cabo USB-C compatível (Charge/Data), Aplicativo Apple Configurator 2, Acesso à internet.

**Procedimento para Macs Antigos (Sem chip T2):**
1. Baixe a ferramenta *Firmware Restoration* na página de Suporte da Apple.
2. Crie um CD/Pendrive inicializável com a imagem, inicie o Mac segurando `Option` e aplique a recuperação do firmware.

**Procedimento para Macs Modernos Intel (Com chip T2):**
1. Em OUTRO Mac em perfeito funcionamento, instale o aplicativo **Apple Configurator 2** a partir da Mac App Store.
2. Conecte o cabo USB-C à porta designada para recuperação no Mac defeituoso (normalmente a primeira porta USB-C da esquerda/inferior, *consulte a documentação técnica específica do modelo*). Conecte a outra extremidade no Mac host.
3. Coloque o Mac defeituoso em **Modo DFU**:
   - Desligue o equipamento (segure o botão Power se necessário).
   - Segure o botão Power e adicione as seguintes teclas simultaneamente por cerca de 10 segundos: `Shift (Direito) + Option (Esquerdo) + Control (Esquerdo)`.
   - Solte todas as teclas após os 10 segundos. O Mac parecerá estar desligado.
4. No Mac host, o Apple Configurator 2 deverá exibir a silhueta de um dispositivo com os dizeres "DFU".
5. No aplicativo, clique em `Actions` (Ações) > `Advanced` (Avançado) > `Revive Device` (Reanimar) ou `Restore` (Restaurar) - Nota: *Restore apagará os dados do disco*.
6. Aguarde o download do BridgeOS e a reescrita do firmware (isso pode levar de 15 a 30 minutos). O Mac será reiniciado com o logotipo da Apple e uma barra de progresso.

### Validação
O ciclo de SOS sonoro deixa de ocorrer e o Mac completa o carregamento. A ferramenta Apple Diagnostics (`D`) passa sem erros. A versão correta da Boot ROM / T2 Firmware consta no Relatório do Sistema.

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
