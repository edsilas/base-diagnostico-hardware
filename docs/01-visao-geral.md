<!-- Gerado a partir de Ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../README.md) › [Comece aqui](../README.md#comece-aqui) › **Visão geral**

# Visão geral

> O que esta base é, o que cobre, para quem foi escrita e o que ela deliberadamente não faz.


**Aplica-se a:** Primeira leitura de quem chega ao projeto

## Neste documento

- [Identidade oficial](#identidade-oficial)
- [O que é](#o-que-é)
- [O que as planilhas de origem declaram sobre si](#o-que-as-planilhas-de-origem-declaram-sobre-si)
- [Propósito](#propósito)
- [Conteúdo consolidado](#conteúdo-consolidado)
- [Público-alvo](#público-alvo)
- [O que esta base não faz](#o-que-esta-base-não-faz)
- [Próximos passos](#próximos-passos)

## Contexto

Primeiro documento a ler. Explica o que esta base de conhecimento é, o que ela cobre, para quem foi escrita e o que ela deliberadamente não faz.

## Escopo

Identidade do projeto, propósito, público, conteúdo consolidado e origem dos dados.

## Fora do escopo

Estrutura interna da documentação (ver documento 02); procedimentos técnicos; limitações detalhadas (ver documento 15).

## Relação com outros documentos

- [Arquitetura da documentação](02-arquitetura.md)
- [Como utilizar](05-utilizacao.md)
- [Limitações](15-limitacoes.md)
- [Fontes](references/fontes.md)

---

## Identidade oficial

| Item | Valor |
| --- | --- |
| Nome | Base de Diagnóstico de Hardware |
| Autor | Edsilas |
| Repositório | [`edsilas/base-diagnostico-hardware`](https://github.com/edsilas/base-diagnostico-hardware) |
| Descrição oficial | Base estruturada de conhecimento para diagnóstico de hardware, com fluxos, sintomas, códigos de erro, causas e procedimentos de análise e solução. |
| Licença | MIT |
| Proprietário do repositório | `edsilas` |
| Versão desta documentação | `doc-1.4.0` |

**Nível de confiança: Confirmado.** Todos os valores acima vêm do repositório informado pelo
proprietário e consultado em 2026-08-07. Ver [references/fontes.md](references/fontes.md).

## O que é

Base de conhecimento técnica para **diagnóstico de falhas de hardware em computadores**,
convertida a partir de duas planilhas de referência. Reúne, em um único corpo consultável:

- o catálogo de sinais de erro emitidos durante o POST (beeps, Q-Codes, LEDs de diagnóstico) e o
  procedimento associado a cada um;
- os cenários de falha observados após o boot (não liga, tela azul, reinício aleatório,
  superaquecimento, entre outros), com método de diagnóstico e correção;
- os fluxos de decisão que ligam sintoma a procedimento;
- os critérios objetivos de aprovação e reprovação usados para fechar o atendimento;
- os procedimentos operacionais completos de três ferramentas: Victoria, AIDA64 e MemTest86.

## O que as planilhas de origem declaram sobre si

| Item | Situação nas planilhas | Situação após consulta ao repositório |
| --- | --- | --- |
| Nome do projeto | Não declarado | **Confirmado** — ver identidade oficial acima |
| Autor / responsável | Não declarado | **Confirmado** — Edsilas |
| Licença | Não declarada | **Confirmado** — MIT |
| Versão do conteúdo técnico | Não declarada | **Ainda não declarada** — pendência P-02 |
| Idioma | Português (Brasil), com terminologia técnica em inglês preservada | Confirmado |

> Os arquivos `.xlsx` não contêm `docProps/core.xml`, o registro interno onde o Excel grava autor,
> título e datas. A identificação do projeto foi obtida do repositório, não das planilhas.
> A **versão do conteúdo técnico** continua sem declaração — ver
> [P-02 em references/pendencias.md](references/pendencias.md#p-02--versão-do-conteúdo-técnico).

## Propósito

A subtítulo declarado na primeira planilha define o nível pretendido:

> *"Referência Técnica Tier-3 — Baseado em documentação oficial AMI, Phoenix, Award, Dell, HP,
> Lenovo, Apple, ASUS, Gigabyte"*

O material assume um técnico capaz de operar multímetro, abrir equipamento, medir tensões em
conector ATX e interpretar S.M.A.R.T. Não é material de suporte ao usuário final.

## Conteúdo consolidado

| Conteúdo | Quantidade |
| --- | --- |
| Códigos de POST catalogados | 54 |
| Famílias de BIOS / fabricantes cobertos | 11 |
| Tipos de sinal distintos | 9 |
| Cenários de falha (IDs) | 13, agrupados em 9 cenários |
| Camadas de diagnóstico (modelo POST) | 7 |
| Etapas do fluxo de POST | 7 |
| Nós do fluxo sistêmico | 17 |
| Casos de ambiguidade documentados | 5 |
| Correlações em cascata entre camadas | 6 |
| Componentes com critério de validação final | 10 |
| Etapas operacionais de ferramentas | 64 |

### Distribuição dos códigos por família de BIOS

| Família (literal na fonte) | Códigos |
| --- | --- |
| AMI (Legacy BIOS) | 10 |
| AMI (Q-Code Hex) | 10 |
| Proprietário Dell | 7 |
| Proprietário HP | 6 |
| Phoenix BIOS | 5 |
| Award BIOS | 4 |
| Genérico (Múltiplos) | 4 |
| Apple (EFI) | 3 |
| AMI (UEFI/Aptio V) | 2 |
| Proprietário Lenovo | 2 |
| Proprietário Acer / Insyde | 1 |

### Distribuição por tipo de sinal

| Tipo de sinal | Códigos |
| --- | --- |
| Beep Sonoro | 17 |
| Hex Q-Code (Display) | 10 |
| LED Diagnóstico (Âmbar/Branco) | 7 |
| LED Piscante (Caps/Num Lock) | 6 |
| Beep Sonoro (Sequência) | 5 |
| LED de Diagnóstico (cor fixa) | 4 |
| Tom Sonoro | 3 |
| SmartBeep (Melodia) | 1 |
| Beep Sonoro (Binário) | 1 |

## Público-alvo

- Técnicos de manutenção de hardware em bancada.
- Equipes de suporte de nível 2 e 3 que precisam decidir entre reparo, troca de componente e RMA.
- Sistemas de IA que precisem consultar procedimentos de diagnóstico com rastreabilidade de origem.

## O que esta base não faz

- Não substitui o manual do fabricante da placa-mãe ou do equipamento.
- Não cobre reparo em nível de componente (BGA, retrabalho, rebobinamento) — a fonte apenas o
  cita como escalação possível, sem procedimento.
- Não emite recomendação comercial de peças ou fornecedores.
- Não versiona o próprio conteúdo técnico: não há como saber, pela planilha, se um procedimento
  foi revisado.

Ver [Limitações](15-limitacoes.md) para a lista completa e verificada.

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| vai usar a base num atendimento | [Como utilizar](05-utilizacao.md) |
| precisa entender os números de camada | [Taxonomia de camadas](03-taxonomia-camadas.md) |
| quer saber onde a base é frágil | [Limitações](15-limitacoes.md) |
| vai manter ou alterar a documentação | [Arquitetura da documentação](02-arquitetura.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Ambos os arquivos-fonte |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
