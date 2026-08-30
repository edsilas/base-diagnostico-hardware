---
title: Índice da base de conhecimento
description: Mapa completo da documentação, na ordem lógica de uso, com uma linha por documento.
author: Edsilas
date: 2026-08-08
---

[Início](../README.md) › [Comece aqui](../README.md#comece-aqui) › **Índice da base de conhecimento**

# Índice da base de conhecimento

> Mapa completo da documentação, na ordem lógica de uso, com uma linha por documento.


**Aplica-se a:** Navegação — complementa o README com a lista exaustiva

## Neste documento

- [Mapa da documentação](#mapa-da-documentação)
- [Todos os documentos](#todos-os-documentos)
- [Conteúdo da base](#conteúdo-da-base)
- [Próximos passos](#próximos-passos)

## Contexto

Mapa completo da documentação, na ordem lógica de uso. Cada documento tem uma descrição de uma linha.

## Escopo

Listagem ordenada de todos os documentos, com finalidade e origem.

## Fora do escopo

Conteúdo técnico; detalhes de estrutura interna (ver documento 02).

## Relação com outros documentos

- [README](../README.md)
- [Visão geral](01-visao-geral.md)
- [Como utilizar](05-utilizacao.md)

---

> [!TIP]
> Para navegar **pelo sintoma**, use o [README](../README.md) — ele tem o fluxograma de entrada.
> Esta página lista **todos** os documentos, para quando você já sabe o que procura.

## Mapa da documentação

```mermaid
flowchart LR
    subgraph EN["Comece aqui"]
        A1["01 Visão geral"] --> A2["03 Taxonomia<br/>de camadas"] --> A3["04 Requisitos"] --> A4["05 Utilização"]
    end
    subgraph DI["Diagnostique"]
        B1["06 Fluxo POST"]
        B2["07 Fluxo sistêmico"]
        B3["08 Camadas"]
    end
    subgraph RE["Resolva"]
        C1["09 Códigos<br/>de POST"]
        C2["10 Cenários"]
        C3["11 Ambiguidades"]
        C4["12 Correlações"]
    end
    subgraph FE["Feche o atendimento"]
        D1["13 Validação final"]
    end
    subgraph FR["Opere as ferramentas"]
        E1["14 Victoria<br/>AIDA64<br/>MemTest86"]
    end
    subgraph RF["Consulte a referência"]
        F1["17 Glossário"]
        F2["18 Índices cruzados"]
        F3["19 Comandos"]
        F4["15 Segurança e<br/>boas práticas"]
        F5["16 FAQ"]
    end
    subgraph MA["Manutenção"]
        G1["02 Arquitetura"]
        G2["references/"]
    end

    EN --> DI
    B1 --> C1
    B1 --> C3
    B2 --> C2
    B3 --> C1
    C1 --> D1
    C2 --> D1
    C4 --> C2
    C2 --> E1
    D1 --> E1
    RE -.-> RF
    D1 -.-> MA
```

## Todos os documentos

Os grupos abaixo são os mesmos sete do [README](../README.md) e da trilha de navegação que abre
cada página. Se você chegou aqui por uma trilha — *Início › Resolva › …* —, o grupo **Resolva**
abaixo é exatamente o mesmo.

### Comece aqui

| Documento | Finalidade |
| --- | --- |
| [README](../README.md) | Porta de entrada: triagem por sintoma, o que há na base e para onde ir. |
| [00-indice.md](00-indice.md) | Este documento: uma linha por arquivo, para quem prefere o mapa ao fluxograma. |
| [01-visao-geral.md](01-visao-geral.md) | O que a base é, o que cobre, para quem, e onde ficam suas fronteiras. |
| [03-taxonomia-camadas.md](03-taxonomia-camadas.md) | Os dois modelos de camadas, um por escopo, e a regra de notação. **Leitura obrigatória.** |
| [04-requisitos-e-ferramentas.md](04-requisitos-e-ferramentas.md) | Inventário do instrumental exigido, por camada, por cenário e por componente. |
| [15-seguranca-e-boas-praticas.md](15-seguranca-e-boas-praticas.md) | Energia residual, ESD, medição energizada e procedimentos transversais canônicos. |
| [05-utilizacao.md](05-utilizacao.md) | Em que ordem ler e que regras seguir ao aplicar um procedimento. |

### Diagnostique

| Documento | Finalidade |
| --- | --- |
| [06-fluxo-post.md](06-fluxo-post.md) | As 7 etapas do fluxo de POST, da energia à identificação do código. |
| [07-fluxo-sistemico.md](07-fluxo-sistemico.md) | Os 17 nós do fluxo de ponta a ponta, do botão Power ao laudo. |
| [08-diagnostico-por-camada.md](08-diagnostico-por-camada.md) | O que testar em cada subsistema: componentes, testes primários, indicadores de falha. |

### Resolva

| Documento | Finalidade |
| --- | --- |
| [09-codigos-post/](09-codigos-post/00-indice-codigos.md) | Fichas dos 54 códigos de POST, agrupadas em 11 famílias de BIOS. |
| [10-cenarios/](10-cenarios/00-indice-cenarios.md) | Os 13 procedimentos de falha pós-boot, em 9 agrupamentos. |
| [11-ambiguidades.md](11-ambiguidades.md) | Os 5 sinais com mais de um significado, e o teste que desempata. |
| [12-correlacoes.md](12-correlacoes.md) | As 6 falhas que se manifestam em outro subsistema. |
| [20-dispositivos-windows.md](20-dispositivos-windows.md) | Os 18 códigos do Gerenciador de Dispositivos: peça não detectada, driver com problema, dispositivo desativado. **Fonte externa.** |

### Feche o atendimento

| Documento | Finalidade |
| --- | --- |
| [13-validacao-final.md](13-validacao-final.md) | Critério PASS, critério FAIL, tempo de observação e ação em caso de reprovação, para 10 componentes. |

### Opere as ferramentas

| Documento | Finalidade |
| --- | --- |
| [14-ferramentas/](14-ferramentas/00-indice-ferramentas.md) | Qual ferramenta usar para cada verificação, e o guia operacional de cada uma. |
| [14-ferramentas/victoria.md](14-ferramentas/victoria.md) | 9 etapas: S.M.A.R.T., varredura de superfície, remapeamento, relatório. |
| [14-ferramentas/memtest86.md](14-ferramentas/memtest86.md) | 10 etapas, mais os critérios de decisão sobre o destino dos módulos. |
| [14-ferramentas/aida64-etapas-01-15.md](14-ferramentas/aida64-etapas-01-15.md) | 45 etapas em três partes: [01–15](14-ferramentas/aida64-etapas-01-15.md) · [16–30](14-ferramentas/aida64-etapas-16-30.md) · [31–45](14-ferramentas/aida64-etapas-31-45.md). |

### Consulte a referência

| Documento | Finalidade |
| --- | --- |
| [18-indices-cruzados.md](18-indices-cruzados.md) | Os mesmos registros por componente, camada, risco, fase do POST, tipo de sinal e ferramenta. |
| [19-comandos.md](19-comandos.md) | Todos os comandos técnicos dos cenários, com contexto e risco. |
| [17-glossario.md](17-glossario.md) | 47 termos, com a definição usada na base e a expansão de cada sigla. |
| [16-faq.md](16-faq.md) | Dúvidas derivadas do conteúdo documentado. |
| [15-seguranca-e-boas-praticas.md](15-seguranca-e-boas-praticas.md) | Precauções de bancada e procedimentos transversais canônicos. |

### Manutenção

| Documento | Finalidade |
| --- | --- |
| [02-arquitetura.md](02-arquitetura.md) | Como o conhecimento está organizado e de qual aba cada documento saiu. |
| [references/changelog.md](references/changelog.md) | O que mudou em cada versão da documentação. |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Regras de conteúdo, padrão dos documentos e fluxo de alteração. |

> [!TIP]
> Procurando a **ordem de leitura** para quem está chegando agora? Ela fica em
> [05-utilizacao.md](05-utilizacao.md#ordem-de-leitura-para-quem-está-chegando-agora), com o
> diagrama da sequência.

## Conteúdo da base

| Métrica | Valor |
| --- | --- |
| Códigos de POST | 54 |
| Códigos do Gerenciador de Dispositivos | 18 |
| Cenários (IDs) | 13 |
| Cenários (agrupamentos) | 9 |
| Camadas do modelo POST | 7 |
| Camadas do modelo sistêmico | 10 (1–10) |
| Etapas do fluxo de POST | 7 |
| Nós do fluxo sistêmico | 17 |
| Casos de ambiguidade | 5 |
| Correlações | 6 |
| Componentes na validação final | 10 |
| Etapas de ferramentas | 64 |

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer entrar pelo sintoma | [README](../README.md) |
| vai alterar a documentação | [Como contribuir](../CONTRIBUTING.md) |


---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
