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
- [Sobre a própria base](#sobre-a-própria-base)
- [Próximos passos](#próximos-passos)

## Contexto

Perguntas derivadas exclusivamente de conteúdo já documentado. Cada resposta remete ao documento que trata o assunto em profundidade.

## Escopo

Dúvidas de navegação, de interpretação de código e de decisão de procedimento que a fonte responde.

## Fora do escopo

Dúvidas não cobertas pelas fontes — essas estão em [15-limitacoes.md](15-limitacoes.md).

## Relação com outros documentos

- [Como utilizar](05-utilizacao.md)
- [Limitações](15-limitacoes.md)
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

## Sobre a própria base

### Posso confiar que nada foi inventado?

Os documentos técnicos foram **gerados programaticamente** a partir das células das planilhas, sem
redação intermediária. Onde a origem é omissa, o texto registra a lacuna. A rastreabilidade está em
[references/matriz-rastreabilidade.md](references/matriz-rastreabilidade.md).

### Qual é a versão e quem é o autor deste material?

Informação não identificada na fonte analisada. Os arquivos não contêm metadados de autoria ou
versão. Ver [15-limitacoes.md](15-limitacoes.md).

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| não encontrou sua dúvida aqui | [Limitações](15-limitacoes.md) |
| quer entrar pelo sintoma | [README](../README.md) |
| não reconheceu um termo | [Glossário](17-glossario.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Ambos os arquivos-fonte |
| **Status de confiança** | Confirmado (respostas) — perguntas derivadas do conteúdo |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
