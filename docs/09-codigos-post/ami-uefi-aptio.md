---
title: "Referência de Códigos de Erro POST: AMI UEFI / Aptio V"
description: Este artigo fornece a referência completa de diagnóstico e resolução para os códigos sonoros (bipes) de erro POST da família AMI UEFI e Aptio V. Utilize o índice abaixo para navegar diretamente para o código de erro apresentado pelo equipamento.
author: Edsilas
date: 2026-08-08
---

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — AMI UEFI / Aptio V**

# Referência de Códigos de Erro POST: AMI UEFI / Aptio V

**Aplica-se a:** Equipamentos com BIOS `AMI (UEFI/Aptio V)` (Desktops Modernos)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos sonoros (bipes) de erro POST da família AMI UEFI e Aptio V. Utilize o índice abaixo para navegar diretamente para o código de erro apresentado pelo equipamento.

---

## Neste documento

- [POST-11 — 1 Longo + 2 Curtos: Falha no Sistema de Vídeo (GPU)](#post-11--1-longo--2-curtos)
- [POST-12 — 1 Longo + 3 Curtos: Falha de Treinamento de Memória (RAM)](#post-12--1-longo--3-curtos)
- [Próximos passos](#próximos-passos)

## Contexto

Fichas completas dos códigos de POST atribuídos ao fabricante de BIOS `AMI (UEFI/Aptio V)`. Cada ficha reproduz integralmente os campos técnicos do código.

## Escopo

Os 2 códigos da família `AMI (UEFI/Aptio V)`, com interpretação, causa raiz, método de diagnóstico, procedimento de correção, critério de validação e risco.

## Fora do escopo

Códigos de outras famílias de BIOS; fluxos de decisão; cenários sistêmicos (pós-boot); guias de ferramentas.

## Relação com outros documentos

- [Índice de códigos POST](00-indice-codigos.md)
- [Fluxo de diagnóstico POST](../06-fluxo-post.md)
- [Camadas de diagnóstico](../08-diagnostico-por-camada.md)
- [Ambiguidade de códigos](../11-ambiguidades.md)

---

## POST-11 — 1 Longo + 2 Curtos

**Falha no Sistema de Vídeo (GPU)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Video System Failure* (GPU não detectada ou ROM Opcional falha) |
| **Componente afetado** | GPU / PCIe |
| **Fase / Camada** | DXE Video Init / Camada 4: Vídeo |
| **Criticidade** | Alto |

### Causas
O BIOS não consegue inicializar o adaptador gráfico. A GPU não é detectada no barramento PCIe, ou a *Option ROM* da placa de vídeo falha ao carregar. Em sistemas com GPU montada via *riser* (ex: cases compactos SFF ou mineração), pode indicar problema de compatibilidade com a geração do PCIe (Gen 3.0 / 4.0).
- GPU mal encaixada no slot PCIe.
- Cabo de alimentação PCIe (6+2 pinos) desconectado da fonte ou frouxo.
- Placa de vídeo sem fornecimento de energia suficiente (fonte subdimensionada).
- Cabo extensor/Riser PCIe com defeito ou incompatível.
- Conflito de configuração no BIOS (configurada para iGPU forçada, mas apenas GPU dedicada está instalada).

### Diagnóstico e Resolução
**Ferramentas:** GPU de teste, Fonte com potência adequada, Multímetro (12V PCIe).
1. Faça o *power drain* (desligue e drene a energia residual).
2. Verifique se o cabo de energia PCIe (6+2 pinos) está firmemente conectado à GPU.
3. Remova a placa de vídeo, limpe os contatos dourados, e faça o *reseat* (reinstalação firme) no slot.
4. **Se estiver usando Riser PCIe:** Remova o cabo extensor e conecte a placa de vídeo diretamente na placa-mãe. Se der vídeo, o problema é o riser ou a versão do barramento (configure para Gen 3.0 no BIOS temporariamente).
5. Se persistir, realize um teste cruzado com outra placa de vídeo. Se a substituta der vídeo, a original está com defeito.
6. Avalie realizar o Reset do CMOS para restaurar a seleção primária de display (*Primary Display*).

### Validação
O POST deve completar dando imagem no monitor. A GPU deve ser corretamente listada no BIOS e no Gerenciador de Dispositivos do sistema operacional, permanecendo estável sob carga (benchmark).

---

## POST-12 — 1 Longo + 3 Curtos

**Falha de Treinamento de Memória (RAM)**

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Conventional/Extended Memory Failure* (RAM mal encaixada/incompatível) |
| **Componente afetado** | RAM (Módulos DIMM) |
| **Fase / Camada** | Memory Training (PEI) / Camada 3: Memória |
| **Criticidade** | Alto |

### Causas
Falha crítica no processo de *memory training* (treinamento da memória) durante a fase PEI. A controladora da placa-mãe/CPU não consegue estabelecer sincronia e comunicação com os módulos DIMM. Este erro é cada vez mais frequente em plataformas DDR5, que exigem rotinas de treinamento mais longas.
- Módulo DIMM mal encaixado (a trava plástica não fechou ou fechou de forma irregular).
- Povoamento incorreto dos slots (ex: inserir no slot `A1` quando o manual exige `A2` como primário).
- Módulos misturados ou incompatíveis (diferentes frequências, *ranks* ou PMICs).
- Em DDR5: Defeito no PMIC (Power Management IC) interno do próprio pente de memória.
- Pressão excessiva no aperto do *cooler* da CPU, causando leve empenamento do *socket* LGA e isolando os pinos da memória.

### Diagnóstico e Resolução
**Ferramentas:** Manual da placa-mãe (QVL), Módulo de memória sabidamente bom.
1. Efetue um *power drain* completo.
2. Remova todos os módulos DIMM. Verifique se as travas estão sendo empurradas com firmeza até o fim de curso (o "clique" precisa ser limpo e uniforme).
3. Insira **apenas 1 módulo** no slot primário designado pelo manual (usualmente o slot `A2`).
4. Ligue o sistema. **Nota para DDR5:** Aguarde pacientemente. O primeiro boot de treinamento pode levar de 1 a 3 minutos sem exibir imagem no monitor.
5. Se o POST for bem-sucedido, adicione os demais módulos um a um.
6. Se falhar, teste outro módulo de memória listado na QVL da placa.
7. Se ainda falhar com um módulo compatível e funcional, afrouxe levemente os parafusos do *cooler* da CPU (cerca de 1/4 de volta) para aliviar a pressão no soquete.

### Validação
POST completado com sucesso e bipes normais. A RAM deve ser identificada com sua capacidade, frequência e *timings* corretos no BIOS. Teste em *MemTest86* limpo, sem erros.

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou o código aqui | [Índice de códigos POST](00-indice-codigos.md) — catálogo completo |
| suspeita que o código tem outro significado | [Ambiguidade de códigos](../11-ambiguidades.md) |
| quer saber o que testar naquele subsistema | [Diagnóstico por camada](../08-diagnostico-por-camada.md) |
| aplicou a correção e precisa fechar o atendimento | [Validação final por componente](../13-validacao-final.md) |

**Para aprofundar**

- **[Camada 3: Memória](../08-diagnostico-por-camada.md#camada-3--memória-ram) / [Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu):** Aprofunde-se no diagnóstico da camada correspondente.
- **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até este código partindo de um sintoma generalizado.
- **[Índices cruzados](../18-indices-cruzados.md):** Outros códigos do mesmo componente ou nível de risco.

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
