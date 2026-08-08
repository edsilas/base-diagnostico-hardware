<!-- Gerado a partir de Ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../README.md) › [Consulte a referência](../README.md#consulte-a-referência) › **Perguntas frequentes**

# Perguntas frequentes

> Dúvidas derivadas de ambiguidade, armadilha ou decisão explicitamente registrada nas fontes, com link para o documento que trata cada assunto.


**Aplica-se a:** Consulta rápida durante o atendimento

## Neste documento

- [Sobre navegação](#sobre-navegação)
- [Sobre interpretação de códigos](#sobre-interpretação-de-códigos)
- [Sobre decisão de procedimento](#sobre-decisão-de-procedimento)
- [Sobre encerramento do atendimento](#sobre-encerramento-do-atendimento)
- [Sobre procedimentos de bancada](#sobre-procedimentos-de-bancada)
- [Sobre a própria base](#sobre-a-própria-base)
- [Próximos passos](#próximos-passos)

## Contexto

Perguntas derivadas exclusivamente de conteúdo já documentado. Cada resposta remete ao documento que trata o assunto em profundidade.

## Escopo

Dúvidas de navegação, de interpretação de código e de decisão de procedimento que a fonte responde.

## Fora do escopo

Fronteiras de cobertura da base, que estão em
[01-visao-geral.md](01-visao-geral.md#fronteiras-de-cobertura).

## Relação com outros documentos

- [Como utilizar](05-utilizacao.md)
- [Segurança e boas práticas](15-seguranca-e-boas-praticas.md)
- [Glossário](17-glossario.md)

---

> Nenhuma pergunta abaixo foi criada para aumentar o volume da documentação. Todas derivam de
> ambiguidade, armadilha ou decisão explicitamente registrada nas fontes.

## Sobre navegação

### Por onde começo se o equipamento não dá sinal nenhum?

Pela Etapa 1 do [fluxo de POST](06-fluxo-post.md), que verifica energia antes de qualquer outra
coisa, e pela ficha do cenário [Não liga](10-cenarios/nao-liga.md).

### Qual a diferença entre o fluxo de POST e o fluxo sistêmico?

O [fluxo de POST](06-fluxo-post.md) atua enquanto o firmware ainda tem o controle, e sua saída é a
identificação de um código de erro. O [fluxo sistêmico](07-fluxo-sistemico.md) vai do botão Power
até a validação final, cobrindo também o comportamento depois que o sistema operacional carrega.
Eles se sobrepõem na faixa inicial.

### O número da camada significa a mesma coisa em toda a documentação?

Não. Existem dois modelos com numerações diferentes, um por arquivo-fonte. *Camada 3* é *Memória*
em um e *CPU* no outro. Ver [03-taxonomia-camadas.md](03-taxonomia-camadas.md).

## Sobre interpretação de códigos

### O mesmo beep aparece com dois significados. Como decidir?

Identificando primeiro o fabricante do BIOS. O caso "1 Longo + 2 Curtos", por exemplo, é falha de
vídeo em AMI e Award, mas erro de interface de vídeo (cabo flat) em Acer/Insyde. Os cinco casos
registrados e os critérios de diferenciação estão em [11-ambiguidades.md](11-ambiguidades.md).

### O Q-Code mostra FF. É falha ou é normal?

Depende de **quando** o FF aparece. Se surge imediatamente ao ligar e fica fixo, é tratado como
falha grave. Se aparece ao final de uma progressão de códigos, indica que o controle passou ao
sistema. O critério completo e o teste para distinguir estão em
[11-ambiguidades.md](11-ambiguidades.md).

### O código que observei não está no catálogo. E agora?

O fluxo de POST prevê essa situação nas Etapas 4 e 5: anotar o padrão exatamente como observado e
consultar a documentação do fabricante da placa-mãe. Ver [06-fluxo-post.md](06-fluxo-post.md).

### Por que os códigos têm um identificador `POST-NN` que não vejo em lugar nenhum?

Porque a fonte não numera os códigos. O `POST-NN` foi criado nesta documentação apenas para
permitir link estável entre documentos, e sempre aparece junto do código literal. Ver
[02-arquitetura.md](02-arquitetura.md).

## Sobre decisão de procedimento

### Troquei a memória e o problema continua. O que verificar?

As [correlações em cascata](12-correlacoes.md) tratam exatamente disso. COR-01 registra que
instabilidade de fonte provoca bit-flips na memória e corrupção no disco — trocar RAM não resolve,
e o problema retorna com componentes novos.

### Formatei o Windows e os erros voltaram. Por quê?

COR-02 registra esse caso: memória defeituosa corrompe dados durante a gravação, e o sistema
corrompido é sintoma, não causa. A recomendação da fonte é executar MemTest86 antes de reformatar.

### O sistema fica lento e desliga sozinho. É a fonte?

Pode ser térmico. COR-04 registra que uma CPU em throttling contínuo produz lentidão que parece
problema de software, e que a proteção térmica causa desligamento abrupto idêntico a falha de
fonte. A fonte recomenda monitorar temperatura antes de diagnosticar lentidão.

### Quando um componente está condenado?

O critério registrado no fluxo de POST é o teste cruzado: componente que falha em dois sistemas
está condenado; componente que funciona em outro sistema aponta a placa-mãe como culpada. Ver
Etapa 7 em [06-fluxo-post.md](06-fluxo-post.md).

### Quantas passagens de MemTest86 são necessárias?

Os critérios de decisão pós-teste registrados na fonte usam **4 passes** como referência, e
detalham o destino do módulo conforme a quantidade e o padrão de erros. Ver
[memtest86.md](14-ferramentas/memtest86.md).

## Sobre encerramento do atendimento

### Como sei que o reparo está concluído?

Pelo [documento 13](13-validacao-final.md), que define, para cada um dos 10 componentes, o teste
pós-correção, o critério PASS, o critério FAIL e o tempo de observação exigido.

### O que fazer se a validação reprovar?

Cada linha do documento 13 traz o campo *Ação se FAIL* com o encaminhamento previsto.

## Sobre procedimentos de bancada

### Quanto tempo devo segurar o botão Power para descarregar a energia residual?

**30 segundos**, com o cabo AC removido. Dell publica 15–20 s e HP publica cerca de 15 s; 30 s
satisfaz e supera todos os mínimos publicados, e segurar por mais tempo não causa dano. O
procedimento completo está em
[Segurança e boas práticas](15-seguranca-e-boas-praticas.md#procedimento-canônico-de-power-drain).

### O boot mínimo leva vídeo ou não?

Depende de como você vai ler o resultado. Se a placa tem Debug LED, Q-Code ou speaker, use o
**boot mínimo absoluto** (CPU + cooler + 1 RAM + PSU). Se não tem nenhum desses, a tela é o único
canal de resposta e você precisa do **boot mínimo com vídeo**. O cooler é obrigatório nos dois
casos. Ver
[Boot mínimo](15-seguranca-e-boas-praticas.md#boot-mínimo-as-duas-composições-canônicas).

### A CPU pode ficar a 92 °C? Uma tabela aprova e outra reprova.

As duas estão certas, porque avaliam coisas diferentes: 95 °C é o critério da **CPU como peça**, e
90 °C é o critério do **subsistema de refrigeração**. A 92 °C o processador não está defeituoso,
mas a refrigeração não dá conta dele — e o equipamento não deve ser liberado. Ver
[Como ler os dois limiares](13-validacao-final.md#como-ler-os-dois-limiares-de-temperatura).

### Como chego ao cenário de falhas intermitentes pelo fluxo?

A partir de **F08**, quando o sistema não opera estável mas F09, F09b e F09c não conseguem
reproduzir a falha durante a observação. Por definição, um sintoma intermitente não responde a
teste pontual. Ver
[Regra de entrada de FI-01](07-fluxo-sistemico.md#regra-de-entrada-do-cenário-fi-01).

## Sobre a própria base

### Posso confiar que nada foi inventado?

Os documentos técnicos foram **gerados programaticamente** a partir das células das planilhas, sem
redação intermediária. Onde a origem é omissa, o texto registra a lacuna. A rastreabilidade está em
[references/matriz-rastreabilidade.md](references/matriz-rastreabilidade.md).

### Qual é a versão e quem é o autor deste material?

O autor é **Edsilas**, e a licença é **MIT** — ambos confirmados por consulta ao repositório
oficial. A versão publicada é a que aparece no rodapé de cada documento (`doc-2.0.0`) e, desde essa
versão, ela cobre estrutura **e** conteúdo técnico. As planilhas de origem não trazem campo próprio
de versão; o estado delas fica fixado pelos hashes SHA-256 registrados em
[fontes](references/fontes.md#nível-1--fontes-primárias). A convenção completa está em
[Arquitetura da documentação](02-arquitetura.md#versionamento-do-conteúdo).

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou sua dúvida aqui | [Índice da documentação](00-indice.md) |
| quer entrar pelo sintoma | [README](../README.md) |
| não reconheceu um termo | [Glossário](17-glossario.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Ambos os arquivos-fonte |
| **Status de confiança** | Confirmado (respostas) — perguntas derivadas do conteúdo |
| **Última verificação contra a fonte** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-2.0.0` |
