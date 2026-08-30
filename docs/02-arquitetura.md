---
title: Arquitetura da documentação
description: Como o conhecimento foi organizado, o que cada documento carrega e quais convenções todos seguem.
author: Edsilas
date: 2026-08-08
---

[Início](../README.md) › [Manutenção](../README.md#manutenção) › **Arquitetura da documentação**

# Arquitetura da documentação

> Como o conhecimento foi organizado, o que cada documento carrega e quais convenções todos seguem.


**Aplica-se a:** Manutenção da base e auditoria de origem

## Neste documento

- [Os dois eixos do material](#os-dois-eixos-do-material)
- [Princípio de responsabilidade única](#princípio-de-responsabilidade-única)
- [Convenções adotadas](#convenções-adotadas)
- [Versionamento do conteúdo](#versionamento-do-conteúdo)
- [Como manter](#como-manter)
- [Próximos passos](#próximos-passos)

## Contexto

Explica como o conhecimento foi organizado: quais eixos existem e o que cada documento carrega. É o mapa para quem vai manter a base.

## Escopo

Eixos de organização, princípio de responsabilidade única por documento e convenções adotadas.

## Fora do escopo

Conteúdo técnico em si; procedimentos; navegação por tarefa (ver documento 05).

## Relação com outros documentos

- [Índice da documentação](00-indice.md)
- [Visão geral](01-visao-geral.md)

---

## Os dois eixos do material

O material se organiza em dois eixos que **se encontram no momento do boot**:

**Eixo 1 — pré-boot (POST).** O equipamento ainda não entregou controle ao sistema operacional. O
único canal de informação é o sinal que o firmware emite: beep, código hexadecimal em display,
LED de diagnóstico.

**Eixo 2 — pós-boot (sistêmico).** O equipamento liga e carrega o sistema, mas falha em uso: trava,
reinicia, exibe tela azul, superaquece. O canal de informação passa a ser software: logs, S.M.A.R.T.,
sensores, stress test.

```mermaid
flowchart TD
    P(["Botão Power"]) --> E1

    subgraph E1["EIXO 1 — POST (pré-boot)"]
        direction LR
        A1["06 Fluxo de POST"] --> A2["09 Códigos de POST"]
        A2 --> A3["08 Camadas"]
        A2 --> A4["11 Ambiguidades"]
    end

    E1 -->|"POST concluído"| E2

    subgraph E2["EIXO 2 — sistêmico (pós-boot)"]
        direction LR
        B1["07 Fluxo sistêmico"] --> B2["10 Cenários"]
        B2 --> B3["12 Correlações"]
        B2 --> B4["14 Ferramentas"]
    end

    E2 -->|"correção aplicada"| E3["13 Validação final<br/>fecha o atendimento"]
    E3 --> Z(["Laudo"])
```

> [!NOTE]
> O diagrama acima é uma **representação organizacional** desta documentação. Nível: **Inferido**,
> derivado da leitura dos fluxos
> (Etapa 1→7 no eixo 1; F01→F14 no eixo 2).

## Princípio de responsabilidade única

Cada documento tem um dono de assunto. Informação não é duplicada entre documentos: quando um
documento precisa de conteúdo de outro, ele **referencia** em vez de copiar.

| Documento | Responsabilidade exclusiva |
| --- | --- |
| `01-visao-geral.md` | O que o projeto é e o que não é |
| `02-arquitetura.md` | Como a documentação está organizada |
| `03-taxonomia-camadas.md` | Significado dos números de camada e o conflito entre os dois modelos |
| `04-requisitos-e-ferramentas.md` | Instrumental necessário |
| `05-utilizacao.md` | Por onde entrar conforme a situação |
| `06-fluxo-post.md` | Sequência de decisão antes do boot |
| `07-fluxo-sistemico.md` | Sequência de decisão de ponta a ponta |
| `08-diagnostico-por-camada.md` | O que testar em cada subsistema (modelo POST) |
| `09-codigos-post/` | Ficha de cada código de erro |
| `10-cenarios/` | Ficha de cada cenário de falha |
| `11-ambiguidades.md` | Códigos com mais de um significado |
| `12-correlacoes.md` | Falha em uma camada que aparece como sintoma em outra |
| `13-validacao-final.md` | Critérios de aprovação e reprovação pós-reparo |
| `14-ferramentas/` | Operação passo a passo de Victoria, AIDA64 e MemTest86 |
| `15-seguranca-e-boas-praticas.md` | Precauções de bancada e procedimentos transversais canônicos |
| `16-faq.md` | Perguntas derivadas do conteúdo documentado |
| `17-glossario.md` | Termos técnicos usados no material |
| `references/` | Histórico de versões |

## Convenções adotadas

**Fidelidade do texto técnico.** Os documentos das pastas `09-codigos-post/`, `10-cenarios/` e
`14-ferramentas/`, mais os documentos 06, 07, 08, 11, 12, 13, 18, 19 e 20, trazem os campos
técnicos **sem reescrita**: nada foi resumido, adaptado ou dito com outras palavras. Isso elimina a
possibilidade de paráfrase acidental.

**Referências cruzadas.** As ligações entre documentos — código → ficha da camada, camada →
códigos atribuídos, cenário → nós do fluxo que o alcançam, cenário → dependências — seguem as
classificações registradas em cada ficha e mudam junto com elas.

**Diagramas.** Os fluxogramas em Mermaid nos documentos 06 e 07 reproduzem a topologia do
encadeamento. Os rótulos foram condensados para caber no diagrama; o texto integral está sempre
logo abaixo, sem cortes.

**Identificadores.** Os IDs de cenário (`NL-01`, `SV-02`, …), de nó de fluxo (`F01`…`F14`) e de
correlação (`COR-01`…`COR-06`) são os da classificação original e foram preservados. O
identificador de código de POST (`POST-01`…`POST-54`) foi criado nesta documentação, seguindo a
ordem das fichas, para permitir link estável. Está sempre acompanhado do código literal.

**Camadas.** O número de camada é sempre reproduzido no formato original, porque o formato
identifica qual dos dois modelos está em uso. Ver [03-taxonomia-camadas.md](03-taxonomia-camadas.md).

**Divergências.** Quando dois pontos da base traziam valores diferentes para o mesmo
procedimento, um valor foi adotado e passou a valer em toda a base, com o critério explicado no
ponto de uso.

**Lacunas.** Informação ausente gera, no documento, a marcação explícita
*"Informação não identificada"*. Nenhuma lacuna foi preenchida por dedução.

**Links.** Todos os links entre documentos são relativos.

## Versionamento do conteúdo

O versionamento vale para o artefato publicado:

| Elemento | Como é versionado |
| --- | --- |
| **Conjunto publicado** | Um único número, `doc-X.Y.Z`, no rodapé de todos os documentos. Ele cobre estrutura **e** conteúdo técnico |
| **Data de revisão** | Campo `date` no front matter de cada documento |
| **Histórico** | [references/changelog.md](references/changelog.md), com o que mudou em cada versão |

Escala:

- **maior** (`2.0.0`) — mudança estrutural: arquivo renomeado, removido ou reorganizado;
- **menor** (`2.1.0`) — conteúdo novo ou documento acrescentado;
- **correção** (`2.0.1`) — link, formatação ou erro de digitação.

> [!IMPORTANT]
> Ao trocar a versão, atualize o rodapé de **todos** os documentos e a tabela de identidade em
> [01-visao-geral.md](01-visao-geral.md#identidade-oficial).

## Como manter

1. Valor técnico não muda sem necessidade comprovada, e toda mudança entra no changelog.
2. Os documentos de organização (README, 00, 01, 02, 03, 04, 05, 15, 16, 17 e `references/`) podem
   ser editados diretamente, desde que nenhuma afirmação nova entre sem base. A separação completa
   está em
   [CONTRIBUTING.md](../CONTRIBUTING.md#quais-arquivos-carregam-valor-técnico).
4. Toda mudança deve ser registrada em [references/changelog.md](references/changelog.md).
5. Divergência nova entre fontes se resolve contra documento oficial e se incorpora ao ponto de
   uso — a base não mantém lista paralela de itens em aberto.

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| vai alterar conteúdo técnico | [Como contribuir](../CONTRIBUTING.md) |
| quer ver o histórico de mudanças | [Changelog](references/changelog.md) |


---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
