<!-- Gerado a partir de Ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../README.md) › [Comece aqui](../README.md#comece-aqui) › **Como utilizar esta base**

# Como utilizar esta base

> Roteiro de entrada: por onde começar conforme o sintoma, em que ordem ler e quais regras seguir ao aplicar os procedimentos.


**Aplica-se a:** Uso da base durante um atendimento

## Neste documento

- [Antes de qualquer coisa](#antes-de-qualquer-coisa)
- [Entrada por sintoma](#entrada-por-sintoma)
- [Ordem de leitura para quem está chegando agora](#ordem-de-leitura-para-quem-está-chegando-agora)
- [Regras de uso do material](#regras-de-uso-do-material)
- [Uso por sistemas de IA](#uso-por-sistemas-de-ia)
- [Próximos passos](#próximos-passos)

## Contexto

Roteiro de entrada. Diz por onde começar conforme o que está acontecendo com o equipamento e em que ordem percorrer os documentos.

## Escopo

Pontos de entrada por situação, ordem de leitura recomendada e regras de uso do material.

## Fora do escopo

Conteúdo técnico dos procedimentos; organização interna da documentação (ver documento 02).

## Relação com outros documentos

- [Índice da documentação](00-indice.md)
- [Fluxo de diagnóstico POST](06-fluxo-post.md)
- [Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md)
- [Índice de cenários](10-cenarios/00-indice-cenarios.md)

---

## Antes de qualquer coisa

Leia [Taxonomia de camadas](03-taxonomia-camadas.md). Os dois arquivos-fonte numeram as camadas
de forma diferente, e usar o número errado leva a testar o subsistema errado.

## Entrada por sintoma

> [!TIP]
> A entrada por sintoma fica no [README](../README.md#por-onde-começar), que é o ponto de entrada
> da base: lá estão o fluxograma de triagem e a tabela completa de situação → documento.
> Esta página trata do **como usar** o material: em que ordem ler, que regras seguir e como um
> agente de IA deve consultá-lo.

## Ordem de leitura para quem está chegando agora

```mermaid
flowchart TD
    A["01 Visão geral<br/>o que é este material"] --> B["03 Taxonomia de camadas<br/>o conflito de numeração"]
    B --> C["04 Requisitos<br/>o que precisa estar na bancada"]
    C --> D{"O equipamento<br/>carrega o sistema?"}
    D -->|"Não"| E["06 Fluxo de POST<br/>a decisão antes do boot"]
    D -->|"Sim"| F["07 Fluxo sistêmico<br/>a decisão de ponta a ponta"]
    E --> G["08 Camadas<br/>o que testar em cada subsistema"]
    F --> G
    G --> H["09 e 10<br/>as fichas, sob demanda"]
    H --> I["13 Validação final<br/>como fechar"]
    I --> J["15 Limitações<br/>onde não confiar"]
```

> [!IMPORTANT]
> A etapa **03 Taxonomia de camadas** não é opcional. Ela é o único ponto da base em que o
> conflito entre os dois modelos de numeração é explicado, e todo número de camada que você
> encontrar depois depende dela.

## Regras de uso do material

1. **Não pule a camada de energia.** Os dois fluxos começam por ela, e a correlação
   [COR-01](12-correlacoes.md#cor-01) registra que instabilidade de fonte se manifesta como falha de
   memória, de disco e de sistema operacional.
2. **Anote o sinal exatamente como observado.** A Etapa 3 do fluxo de POST exige registrar número
   de beeps, duração (curto/longo) e pausas. Sem isso, a consulta ao catálogo não converge.
3. **Identifique o fabricante do BIOS antes de interpretar um beep.** O mesmo padrão sonoro tem
   significados diferentes entre AMI, Award e Acer/Insyde.
4. **Não conclua o atendimento sem validar.** O documento 13 traz critério PASS e FAIL por
   componente, com tempo de observação.
5. **Onde a documentação disser "Informação não identificada na fonte analisada", trate como
   lacuna real** — não como algo que possa ser preenchido por analogia com outro registro.

## Uso por sistemas de IA

Cada documento é autocontido: traz contexto, escopo, fora de escopo, relação com outros documentos
e a aba de origem no rodapé. Um agente pode carregar apenas o documento relevante sem perder a
noção de onde ele se encaixa. Os documentos gerados trazem, na primeira linha, um comentário HTML
com a aba de origem.

Para rastrear qualquer afirmação até a célula de origem, use
[references/matriz-rastreabilidade.md](references/matriz-rastreabilidade.md).

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| o equipamento não carrega o sistema | [Fluxo de diagnóstico POST](06-fluxo-post.md) |
| o equipamento carrega e falha em uso | [Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md) |
| quer a lista completa de documentos | [Índice da documentação](00-indice.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Ambos os arquivos-fonte |
| **Status de confiança** | Inferido (roteiro de navegação) sobre conteúdo Confirmado |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
