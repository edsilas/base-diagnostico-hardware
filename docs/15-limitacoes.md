<!-- Gerado a partir de Verificação direta sobre ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../README.md) › [Consulte a referência](../README.md#consulte-a-referência) › **Limitações conhecidas**

# Limitações conhecidas

> O que esta base não entrega, verificado item a item contra os arquivos de origem.


**Aplica-se a:** Avaliação de confiança antes de decidir com base neste material

## Neste documento

- [Para que serve esta página](#para-que-serve-esta-página)
- [O que exige atenção antes de decidir](#o-que-exige-atenção-antes-de-decidir)
- [Como ler cada limitação](#como-ler-cada-limitação)
- [1. Metadados do projeto ausentes](#1-metadados-do-projeto-ausentes)
- [2. Conflito de taxonomia entre as fontes](#2-conflito-de-taxonomia-entre-as-fontes)
- [3. Divergências de procedimento entre as fontes](#3-divergências-de-procedimento-entre-as-fontes)
- [4. Campos vazios na origem](#4-campos-vazios-na-origem)
- [5. Anomalias estruturais nas fontes](#5-anomalias-estruturais-nas-fontes)
- [6. Cobertura técnica ausente](#6-cobertura-técnica-ausente)
- [7. Limites de uso do material](#7-limites-de-uso-do-material)
- [8. Limite desta documentação](#8-limite-desta-documentação)
- [Quando consultar outro documento](#quando-consultar-outro-documento)
- [Próximos passos](#próximos-passos)

## Contexto

Registro honesto do que esta base **não** entrega. Cada item foi verificado contra os arquivos de origem; nenhum é suposição.

## Escopo

Lacunas de metadados, conflitos entre fontes, campos vazios, cobertura técnica ausente e limites de uso.

## Fora do escopo

Itens que exigem decisão do proprietário do projeto — esses estão em [references/pendencias.md](references/pendencias.md).

## Relação com outros documentos

- [Pendências](references/pendencias.md)
- [Taxonomia de camadas](03-taxonomia-camadas.md)
- [Fontes](references/fontes.md)
- [FAQ](16-faq.md)

---

## Para que serve esta página

Esta página lista **o que esta base não resolve**. Ela existe porque uma documentação técnica só é
confiável quando declara os próprios limites: saber onde o material é sólido é tão importante
quanto saber onde ele não é.

Leia antes de tomar uma decisão que dependa deste material — trocar uma peça, aprovar ou reprovar
um equipamento, padronizar um procedimento na oficina.

Nada aqui é opinião. Cada limitação foi verificada nos arquivos de origem, e cada uma indica o que
fazer quando você esbarrar nela.

## O que exige atenção antes de decidir

Quatro limitações podem mudar o resultado de um diagnóstico. Se você tem pouco tempo, leia estas.

| Limitação | Por que importa na prática | Detalhe |
| --- | --- | --- |
| **Camada 3 significa coisas diferentes** | *Memória* em um arquivo-fonte, *CPU* no outro. Usar o número errado leva a testar o subsistema errado | [Seção 2](#2-conflito-de-taxonomia-entre-as-fontes) |
| **Quatro procedimentos têm dois valores** | Tempo de descarga, composição do teste mínimo e dois limiares de temperatura divergem entre as fontes | [Seção 3](#3-divergências-de-procedimento-entre-as-fontes) |
| **A base não cobre tudo** | Sem ECC, servidores com BMC/IPMI, ARM, Apple Silicon nem reparo em nível de componente | [Seção 6](#6-cobertura-técnica-ausente) |
| **Alguns procedimentos apagam dados** | As etapas de escrita e zero-fill do guia Victoria são destrutivas | [Seção 7](#7-limites-de-uso-do-material) |

> [!IMPORTANT]
> Onde há divergência, **a documentação preserva as duas versões e não escolhe uma**. A escolha
> depende de uma decisão registrada em
> [pendências](references/pendencias.md). Não padronize um procedimento divergente sem consultá-la.

## Como ler cada limitação

Cada seção abaixo traz um **tipo** e um **estado**. Os dois respondem perguntas diferentes.

**Tipo — qual é a natureza do problema:**

| Tipo | Significado |
| --- | --- |
| Informação ausente | A fonte não fornece o dado |
| Conflito entre fontes | Existem versões diferentes da mesma informação |
| Divergência não resolvida | Há alternativas documentadas, sem evidência para escolher uma |
| Anomalia da fonte | A estrutura original é inconsistente |
| Cobertura ausente | O cenário ou a tecnologia não tem procedimento documentado |
| Limitação de uso | O material tem restrições práticas ou operacionais |
| Limitação da documentação | Esta base não realizou determinada validação |

**Estado — o que se sabe sobre a informação:**

| Estado | Significado |
| --- | --- |
| Confirmado | Encontrado e verificado diretamente na fonte |
| Não identificado | Não encontrado na fonte analisada |
| Conflitante | Fontes diferentes apresentam informações diferentes |
| Não verificado | Sem validação independente por esta documentação |
| Pendente | Depende de decisão ou investigação adicional |

---

## 1. Metadados do projeto ausentes

**Tipo:** Informação ausente · **Estado:** Confirmado

**Situação.** Os dois arquivos `.xlsx` não contêm `docProps/core.xml` — o registro interno onde o
Excel grava autor, título e datas de criação e revisão. Nenhuma aba supre esses campos.

| Informação | Nas planilhas | Situação atual |
| --- | --- | --- |
| Nome oficial do projeto | Não identificada | **Confirmado** fora da planilha — ver [P-01](references/pendencias.md#p-01--nome-oficial-do-projeto--fechada) |
| Autor / responsável técnico | Não identificada | **Confirmado** fora da planilha — `edsilas` |
| Licença de uso | Não identificada | **Confirmado** fora da planilha — MIT |
| Versão do conteúdo técnico | Não identificada | **Pendente** — ver [P-02](references/pendencias.md#p-02--versão-do-conteúdo-técnico) |
| Data de elaboração | Não identificada | **Não identificado** |

**Impacto.** A versão do conteúdo técnico é a que ainda pesa: sem ela, **um procedimento
desatualizado é indistinguível de um atualizado**. Os demais campos foram resolvidos por consulta
ao repositório oficial, informado pelo proprietário.

**Como proceder.** Nenhum campo foi preenchido por dedução. Ao citar autoria, licença ou nome,
use os valores confirmados — não os atribua às planilhas, que não os declaram.

## 2. Conflito de taxonomia entre as fontes

**Tipo:** Conflito entre fontes · **Estado:** Conflitante

**Situação.** Os dois arquivos numeram as camadas de diagnóstico de forma **incompatível**. O
exemplo mais direto: camada 3 é *Memória* em um e *CPU* no outro.

Há um segundo problema, de natureza diferente. O modelo de 10 camadas usado pelo arquivo de fluxo
**não possui tabela de definição** em nenhuma aba — foi reconstruído a partir das ocorrências
literais nas células.

| Camada | Onde aparece |
| --- | --- |
| 2 (*Firmware*), 8 (*Periféricos*), 10 (*Drivers*) | Apenas na aba `CORRELACOES` |
| 7 (*Placa-mãe*) | Apenas na aba `TABELA_PRINCIPAL` |

Nenhuma camada desse modelo tem ficha técnica equivalente à do
[documento 08](08-diagnostico-por-camada.md), que cobre apenas o outro modelo.

**Impacto.** Um número de camada lido fora de contexto leva ao subsistema errado. É a limitação de
maior alcance desta base, porque afeta todos os documentos que citam camadas.

**Como proceder.** Leia [03-taxonomia-camadas.md](03-taxonomia-camadas.md) antes de usar qualquer
número de camada — o documento explica como identificar de qual modelo o número veio pelo formato
em que está escrito. A falta da tabela de definição está registrada em
[P-04](references/pendencias.md#p-04--modelo-de-camadas-b-sem-tabela-de-definição).

## 3. Divergências de procedimento entre as fontes

**Tipo:** Divergência não resolvida · **Estado:** Conflitante

**Situação.** Quatro procedimentos aparecem com valores diferentes conforme o arquivo consultado.
Nenhuma divergência foi resolvida: **todas as versões estão preservadas** nos documentos
correspondentes.

| Tema | Uma fonte diz | A outra diz | Pendência |
| --- | --- | --- | --- |
| Duração do *power drain* — descarga dos capacitores | 30 s (`CODIGOS_DE_ERROS`, vários registros) | 10 s (`FLUXO_DIAGNOSTICO`, NL-01) | [P-05](references/pendencias.md#p-05--duração-do-power-drain) |
| Composição do *boot mínimo* — teste com o mínimo de peças | "CPU + 1 RAM + fonte"; "CPU+RAM+Vídeo apenas" (`CODIGOS_DE_ERROS`) | "CPU+Cooler+1RAM+PSU apenas" (`FLUXO_DIAGNOSTICO`, F02b) | [P-06](references/pendencias.md#p-06--composição-do-boot-mínimo) |
| Limiar térmico em repouso | ">60 °C em idle → problema térmico confirmado" (SA-01) | ">90 °C em idle → problema térmico" (COR-04) | [P-07](references/pendencias.md#p-07--limiar-térmico-em-idle) |
| Critério FAIL de temperatura | Linha *CPU*: Temp > 95 °C | Linha *Térmico*: Temp > 90 °C — **na mesma aba** `VALIDACAO_FINAL` | [P-08](references/pendencias.md#p-08--critério-fail-de-temperatura-na-validação-final) |

> [!NOTE]
> A linha do *boot mínimo* condensa **três** definições literais, não duas: a coluna da esquerda
> reúne duas variantes do mesmo arquivo. O texto integral das três está em
> [P-06](references/pendencias.md#p-06--composição-do-boot-mínimo).

**Impacto.** Cada divergência muda um resultado concreto. Um equipamento a 92 °C é aprovado por uma
linha da validação final e reprovado por outra. Uma descarga de 10 s pode não eliminar a tensão
residual que 30 s eliminaria.

**Como proceder.** Use a versão do documento que você está seguindo e registre qual foi. Antes de
padronizar qualquer um desses procedimentos na oficina, consulte a pendência correspondente na
tabela acima — a decisão não pode ser tomada apenas com base nas fontes analisadas.

## 4. Campos vazios na origem

**Tipo:** Informação ausente · **Estado:** Confirmado

**Situação.** Dois campos dos guias de ferramentas estão vazios em parte das etapas.

| Aba | Campo | Etapas sem preenchimento |
| --- | --- | --- |
| `REF_Victoria` | Atalho de Teclado | 6 de 9 |
| `REF_AIDA64` | Atalho de Teclado | 42 de 45 |
| `REF_AIDA64` | Alternativa Segura | 4 de 45 |
| `REF_MemTest86` | Atalho de Teclado | 7 de 10 |
| `REF_MemTest86` | Alternativa Segura | 5 de 10 |

As demais colunas das abas `Tabela Diagnóstico POST` e `TABELA_PRINCIPAL` estão **100 %
preenchidas**.

> [!NOTE]
> **O denominador de `REF_MemTest86` é ambíguo.** A aba tem onze linhas de conteúdo — as dez etapas
> mais o bloco de critérios descrito na [seção 5](#5-anomalias-estruturais-nas-fontes), cujos campos
> também estão vazios. A contagem acima usa as dez etapas, que é o recorte verificável em
> [memtest86.md](14-ferramentas/memtest86.md). Qual recorte a planilha considera continua por
> confirmar: [P-12](references/pendencias.md#p-12--campos-vazios-nos-guias-de-ferramentas).

**Impacto.** Baixo. É plausível que muitas etapas simplesmente não tenham atalho — mas a fonte
**não distingue "não existe" de "não preenchido"**.

**Como proceder.** Onde há vazio, o documento correspondente exibe
*"Informação não identificada na fonte analisada"* em vez de omitir a seção. Trate como lacuna
real: não preencha por analogia com outra etapa.

## 5. Anomalias estruturais nas fontes

**Tipo:** Anomalia da fonte · **Estado:** Confirmado

**Situação.** Quatro pontos em que a estrutura original foge do próprio padrão.

| Onde | O que acontece | Como está tratado aqui | Pendência |
| --- | --- | --- | --- |
| `REF_MemTest86`, última linha | Contém um bloco de critérios de decisão pós-teste ocupando a coluna `Nº da Etapa`. Não é uma etapa | Preservado como seção própria em [memtest86.md](14-ferramentas/memtest86.md) | [P-13](references/pendencias.md#p-13--bloco-de-critérios-do-memtest86-fora-da-estrutura) |
| `FLUXO_LOGICO`, nós F06 e F08 | Sem ID de cenário associado — campo preenchido com "—" | Reproduzido como está | [P-14](references/pendencias.md#p-14--nós-f06-e-f08-sem-cenário-associado) |
| `TABELA_PRINCIPAL`, ID FI-01 | Existe na tabela e no índice, mas **nenhum nó do fluxo sistêmico chega até ele** | A ficha exibe aviso e link para a pendência | [P-09](references/pendencias.md#p-09--fi-01-inalcançável-pelo-fluxo-sistêmico) |
| Códigos de POST | Não possuem identificador próprio na fonte | O rótulo `POST-NN` foi criado nesta documentação para permitir link estável, e vem sempre acompanhado do código literal | [P-16](references/pendencias.md#p-16--identificador-post-nn-criado-por-esta-documentação) |

**Impacto.** Baixo para o diagnóstico. Relevante para quem for alterar as planilhas: inserir uma
linha no meio da tabela de códigos **desloca todos os identificadores `POST-NN` seguintes**.

**Como proceder.** Ao citar um código de POST fora desta base, use o código literal — `1 Longo + 2
Curtos`, `B4` —, não o rótulo `POST-NN`.

## 6. Cobertura técnica ausente

**Tipo:** Cobertura ausente · **Estado:** Confirmado por leitura integral das fontes

**Situação.** Estes cenários e tecnologias **não têm procedimento documentado** nesta base.

| Não coberto | Observação |
| --- | --- |
| Reparo em nível de componente | A fonte cita "reparo em nível de componente (BGA, capacitor, etc.)" apenas como escalação final, sem detalhar |
| Lenovo SmartBeep | O registro traz "Variável" na maior parte dos campos e remete ao aplicativo Lenovo PC Diagnostics — ver [P-11](references/pendencias.md#p-11--lenovo-smartbeep-sem-procedimento) |
| Beep contínuo de teclado (AMI) | A aba de ambiguidades menciona que, em algumas versões AMI, beep contínuo indica tecla presa. Não há entrada no catálogo, que registra beep contínuo apenas para Award (memória) — ver [P-10](references/pendencias.md#p-10--beep-contínuo-de-teclado-ami-sem-ficha-no-catálogo) |
| Memória ECC, servidores com BMC/IPMI, plataformas ARM, Apple Silicon | O material Apple documentado cobre **Mac com processador Intel** |
| Notebooks, de forma sistemática | Aparecem apenas pontualmente, dentro de registros específicos (Dell LCD/eDP, Acer cabo flat, compartimento SO-DIMM) |
| Custo, tempo médio de reparo, disponibilidade de peças | Nenhum dado dessa natureza nas fontes |

**Impacto.** Fora dessas fronteiras, esta base não ajuda — e não sinaliza que não ajuda. Um técnico
diante de um servidor com ECC não encontrará aqui o procedimento correto.

**Como proceder.** Para o que está fora de cobertura, recorra à documentação do fabricante. Para os
três primeiros itens, há pendência aberta: a lacuna é reconhecida e pode vir a ser preenchida na
fonte.

## 7. Limites de uso do material

**Tipo:** Limitação de uso · **Estado:** Confirmado

| Limite | O que isso significa |
| --- | --- |
| **Não há instruções de segurança do trabalho** | Os procedimentos envolvem medição elétrica e abertura de equipamento. A fonte registra um nível de risco por procedimento — Crítico, Alto, Médio, Baixo — mas não traz orientação de segurança além das menções pontuais nos próprios registros |
| **Vários procedimentos apagam dados** | Em especial as etapas de escrita e zero-fill do guia [Victoria](14-ferramentas/victoria.md). A fonte alerta nos campos de risco de cada etapa |
| **Não substitui o manual do fabricante** | Vários registros remetem explicitamente a ele: pinagem de front panel, seção de Q-Code, QVL de memória, lista de CPUs suportadas |

**Impacto.** O risco é real e recai sobre o operador e sobre os dados do cliente. A ausência de
orientação de segurança **não significa que o procedimento seja seguro** — significa que a fonte
não trata do assunto.

**Como proceder.** Confira o nível de risco e os pré-requisitos da ficha antes de executar. Faça
cópia de segurança antes de qualquer etapa de escrita em disco. Tenha o manual da placa-mãe à mão.

## 8. Limite desta documentação

**Tipo:** Limitação da documentação · **Estado:** Não verificado

**Situação.** Esta base reflete **o conteúdo das duas planilhas na data de análise**. As
afirmações técnicas não foram conferidas contra a documentação oficial dos fabricantes citados,
embora a fonte declare basear-se nela e informe a referência em cada registro.

Houve duas conferências pontuais, de natureza estritamente bibliográfica:

| O que foi conferido | Resultado |
| --- | --- |
| A designação de parte das normas citadas | UEFI 2.10 e JEDEC JESD79-4/79-5 existem como citadas. A citação *ATX12V PSU Design Guide v2.53* nomeia um documento inexistente sob esse título — ver [P-15](references/pendencias.md#p-15--referências-externas-citadas-mas-não-verificadas) |
| Se a Lenovo publica a tabela de melodias do SmartBeep | Não publica; a decodificação é feita pelo aplicativo — ver [P-11](references/pendencias.md#p-11--lenovo-smartbeep-sem-procedimento) |

> [!IMPORTANT]
> Essas conferências apuraram **se o documento citado existe e como se chama** — não se a afirmação
> atribuída a ele está lá. **Nenhuma informação técnica desta base veio de documentação de
> fabricante**, e nenhuma foi incorporada às fichas. O inventário completo está em
> [references/fontes.md](references/fontes.md).

**Impacto.** Toda afirmação técnica desta base tem o valor da planilha de origem — nem mais, nem
menos. Se a planilha errou, a documentação reproduz o erro fielmente.

**Como proceder.** Para uma decisão de alto custo — descartar uma peça cara, definir um padrão de
oficina —, confronte o valor com a especificação do fabricante antes de agir.

## Quando consultar outro documento

| Se você… | Vá para | Por quê |
| --- | --- | --- |
| Encontrou um número de camada e não sabe o que ele significa | [Taxonomia de camadas](03-taxonomia-camadas.md) | Único lugar onde o conflito entre os dois modelos é explicado |
| Precisa decidir entre dois valores divergentes | [Pendências](references/pendencias.md) | Registra a divergência, o impacto e o que falta para resolvê-la |
| Quer saber de qual aba e coluna veio uma informação | [Matriz de rastreabilidade](references/matriz-rastreabilidade.md) | Mapeia informação → coluna de origem → documento → nível de confiança |
| Quer conferir quais fontes existem e qual o nível de confiança de cada uma | [Fontes](references/fontes.md) | Inventário das planilhas e das referências que elas citam |
| Tem uma dúvida pontual sobre como usar o material | [Perguntas frequentes](16-faq.md) | Respostas curtas derivadas do conteúdo documentado |
| Vai operar uma ferramenta citada aqui | [Victoria](14-ferramentas/victoria.md) · [MemTest86](14-ferramentas/memtest86.md) · [AIDA64](14-ferramentas/aida64-etapas-01-15.md) | Guias operacionais etapa a etapa |

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer o que exige decisão sua | [Pendências](references/pendencias.md) |
| quer entender o conflito de camadas | [Taxonomia de camadas](03-taxonomia-camadas.md) |
| quer conferir a origem de uma informação | [Fontes](references/fontes.md) |
| tem uma dúvida pontual sobre o uso da base | [Perguntas frequentes](16-faq.md) |
| quer saber o que a base **entrega** | [Visão geral](01-visao-geral.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Verificação direta sobre ambos os arquivos-fonte |
| **Status de confiança** | Confirmado — cada item verificado contra a origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
