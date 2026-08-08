# Como contribuir e manter esta base

Este repositório é uma base de conhecimento derivada de planilhas. A regra que sustenta a
confiabilidade dele é simples e não negociável:

> **A planilha é a fonte da verdade. O Markdown é gerado.**

Editar diretamente um arquivo gerado em `docs/` funciona até a próxima regeração — quando a
alteração é silenciosamente perdida. Pior: enquanto ela existe, o conteúdo do repositório deixa de
corresponder à fonte, que é exatamente o que a rastreabilidade desta base promete evitar.

---

## Quais arquivos são gerados e quais não são

### Gerados — **não edite à mão**

Todos trazem, na primeira linha, um comentário HTML indicando a aba de origem.

| Arquivo | Aba de origem |
| --- | --- |
| `docs/06-fluxo-post.md` | `Fluxo de Diagnóstico` |
| `docs/07-fluxo-sistemico.md` | `FLUXO_LOGICO` |
| `docs/08-diagnostico-por-camada.md` | `Camadas de Diagnóstico` |
| `docs/09-codigos-post/*` | `Tabela Diagnóstico POST` |
| `docs/10-cenarios/*` | `TABELA_PRINCIPAL` + `INDICE_CENARIOS` |
| `docs/11-ambiguidades.md` | `Ambiguidade de Códigos` |
| `docs/12-correlacoes.md` | `CORRELACOES` |
| `docs/13-validacao-final.md` | `VALIDACAO_FINAL` |
| `docs/14-ferramentas/*` | `REF_Victoria`, `REF_AIDA64`, `REF_MemTest86` |
| `docs/18-indices-cruzados.md` | derivado das colunas de classificação |
| `docs/19-comandos.md` | coluna `Comandos Técnicos` |

### Redigidos — edite à vontade, com fonte

`README.md`, `docs/00-indice.md`, `01`, `02`, `03`, `04`, `05`, `15`, `16`, `17` e
`docs/references/*`.

Esses documentos organizam, explicam e sinalizam. Eles **também** são reconstruídos pelo gerador,
porque o texto deles vive dentro dos scripts em `tools/gerador/`. Para alterá-los de forma
duradoura, edite o script correspondente — não o `.md`.

| Documento | Script |
| --- | --- |
| `README.md`, `docs/00-indice.md` | `tools/gerador/gen5c_final.py` |
| `docs/01`, `02`, `05` | `tools/gerador/gen5b_entrada.py` |
| `docs/03`, `04` | `tools/gerador/gen5a_estrutura.py` |
| `docs/15`, `16` | `tools/gerador/gen5d_refs.py` |
| `docs/17` | `tools/gerador/gen5e_glossario.py` |
| `docs/references/fontes.md`, `matriz-rastreabilidade.md` | `tools/gerador/gen6_references.py` |
| `docs/references/pendencias.md`, `changelog.md` | `tools/gerador/gen7_pendencias.py` |

---

## Padrão estrutural dos documentos

Todo documento de `docs/` segue a mesma estrutura. O gerador a aplica automaticamente; ao editar um
script em `tools/gerador/`, mantenha-a.

| Elemento | Como é produzido | Obrigatório |
| --- | --- | --- |
| Comentário HTML com a aba de origem | primeira linha, escrito pelo gerador | documentos derivados |
| Trilha de navegação | `doc_header(..., secao=, nivel=)` | sim |
| Título e resumo de uma linha | `doc_header(..., resumo=)` | sim |
| **Aplica-se a** | `doc_header(..., aplica_se=)` | quando faz sentido |
| **Neste documento** | marcador `<!-- SUMARIO -->`, preenchido por `gen9_sumarios.py` | sim |
| Contexto, Escopo, Fora do escopo, Relação com outros documentos | `doc_header` | sim |
| Fluxograma | bloco ```` ```mermaid ```` escrito no gerador | quando o documento resolve uma decisão |
| **Próximos passos** | `doc_footer(..., proximos=[...])` | sim |
| Rodapé com fonte, confiança, autoria e versão | `doc_footer` | sim |

O parâmetro `secao` aceita: `comecar`, `diagnosticar`, `resolver`, `fechar`, `ferramentas`,
`referencia`, `manutencao`. Cada um aponta para uma seção do README — se você criar uma seção nova
lá, registre-a em `SECOES`, no `common.py`. O validador reprova âncoras inexistentes.

O parâmetro `nivel` é `0` para `docs/*.md` e `1` para `docs/<subpasta>/*.md`. Ele só ajusta a
quantidade de `../` na trilha.

### Avisos

Use os callouts do GitHub, com significado fixo. A função `aviso()` do `common.py` também os
produz.

| Callout | Quando usar |
| --- | --- |
| `> [!NOTE]` | Procedência, nível de confiança, observação de leitura |
| `> [!TIP]` | Atalho de navegação |
| `> [!IMPORTANT]` | Pré-requisito ou regra que muda o resultado |
| `> [!WARNING]` | Risco de erro de diagnóstico ou de perda de tempo |
| `> [!CAUTION]` | Risco elétrico, perda de dados ou dano a componente |

### Procedimentos

Fichas de código e de cenário agrupam os campos em fases, nesta ordem: **Identificação** →
**Pré-requisitos** → **Diagnóstico** → **Execução da correção** → **Resultado esperado** →
**Risco e impacto** → **Origem** → **Próximos passos**. Os nomes dos campos dentro de cada fase são
os da planilha e não devem ser alterados.

### Fluxogramas

- Escreva em Mermaid, dentro de bloco ```` ```mermaid ````. O GitHub renderiza nativamente.
- Use linguagem descritiva nos rótulos ("liga, mas a tela fica preta"), não jargão. O fluxograma
  precisa ser legível por quem não domina a terminologia.
- O diagrama **resume**; o conteúdo integral vem logo abaixo, sem cortes.
- Quando o diagrama condensar ou reorganizar o que a fonte declara, registre isso em um
  `> [!NOTE]` com o nível de confiança.
- O validador confere se os blocos estão balanceados, mas **não** renderiza. Confira visualmente no
  GitHub depois do push.

### Duplicação

Cada assunto tem um dono. A entrada por sintoma, por exemplo, vive no `README.md`; os demais
documentos remetem a ela. Antes de acrescentar uma tabela ou explicação, verifique se ela já existe
em outro documento — se existir, use um link.

## Regras de conteúdo

Estas regras existem porque a base é usada para decidir se um componente vai para o lixo ou para a
bancada. Um dado inventado aqui custa uma peça boa descartada — ou uma ruim devolvida ao cliente.

1. **Não invente.** Funcionalidade, comando, código de erro, tensão, limiar, tempo, compatibilidade,
   versão — nada entra sem estar na fonte.
2. **Lacuna se declara.** Campo sem informação vira
   *"Informação não identificada na fonte analisada"*, nunca uma dedução plausível.
3. **Conflito se registra, não se resolve por conta própria.** Se duas fontes divergem, documente as
   duas e abra uma pendência em `docs/references/pendencias.md`. A base já carrega quatro
   divergências assim.
4. **Inferência se marca.** Conclusão derivada leva o rótulo **Inferido** no ponto de uso.
5. **Versão se preserva.** `MemTest86 v10+`, `ATX12V v2.53`, `UEFI 2.10` — copie exatamente como
   está. Não atualize por conta própria.
6. **Nome técnico não se troca por sinônimo.** `Q-Code`, `Debug LED`, `power drain`, `boot mínimo`
   têm grafia estabelecida na base.
7. **Fonte externa não preenche lacuna da fonte primária.** Se a planilha não diz, a documentação
   não diz.

---

## Fluxo de alteração

### 1. Alterar conteúdo técnico

```bash
# edite HW_HARDWARE_CODIGOS_DE_ERROS.xlsx ou HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx
pip install openpyxl
python tools/gerar_documentacao.py --fontes ./fontes --saida .
python tools/validar_documentacao.py
```

### 2. Alterar texto explicativo

```bash
# edite o script correspondente em tools/gerador/
python tools/gerar_documentacao.py --fontes ./fontes --saida .
python tools/validar_documentacao.py
```

### 3. Conferir antes de commitar

```bash
git diff --stat            # a mudança atingiu só o que deveria?
python tools/validar_documentacao.py
```

O validador precisa terminar com **0 erros**. Ele verifica links internos, âncoras, cabeçalhos de
contexto e rodapés de fonte, sem acesso à rede e sem dependências externas. O mesmo comando roda
no CI a cada push que toque `docs/`.

### 4. Registrar

Toda alteração entra em `docs/references/changelog.md`, com versão, data, o que mudou e qual aba foi
afetada. Pendência resolvida é **marcada como fechada**, não apagada — o histórico da decisão vale
mais que a lista limpa.

Versionamento da documentação:

- **maior** (`2.0.0`) — arquivos renomeados, removidos ou reorganizados;
- **menor** (`1.1.0`) — conteúdo novo, pendência fechada, documento acrescentado;
- **correção** (`1.0.1`) — link, formatação ou erro de transcrição.

---

## Testar sem tocar no repositório

```bash
python tools/gerar_documentacao.py --fontes ./fontes --saida /tmp/teste
python tools/validar_documentacao.py --caminho /tmp/teste
diff -rq docs /tmp/teste/docs
```

Duas execuções com as mesmas planilhas produzem saída idêntica. Se o `diff` acusar diferença sem
que a fonte tenha mudado, há não-determinismo no gerador — isso é bug.

Para ver as etapas sem executar nada:

```bash
python tools/gerar_documentacao.py --listar
```

---

## Onde estão as pendências abertas

`docs/references/pendencias.md` lista o que precisa de decisão humana. As de maior impacto:

- **P-03** — os dois arquivos-fonte numeram as camadas de forma incompatível;
- **P-02** — o conteúdo técnico não é versionado;
- **P-17** — as planilhas de origem precisam ser versionadas no repositório para que a regeração
  seja auditável pelo histórico do Git.

Antes de abrir uma pendência nova, confira a seção *O que não ficou pendente*, no fim do mesmo
arquivo — ela registra o que já foi verificado.

---

## Autoria

**Edsilas** — autor e responsável pelo projeto ([`edsilas`](https://github.com/edsilas)).

Licença: MIT, conforme o arquivo
[`LICENSE`](https://github.com/edsilas/base-diagnostico-hardware/blob/main/LICENSE) do
repositório.
