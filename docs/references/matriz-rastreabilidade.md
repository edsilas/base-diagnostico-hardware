<!-- Gerado a partir de Ambos os arquivos-fonte. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Manutenção e rastreabilidade](../../README.md#manutenção-e-rastreabilidade) › **Matriz de rastreabilidade**

# Matriz de rastreabilidade

> Caminho de ida e volta entre qualquer informação da documentação e a coluna de origem na planilha.


**Aplica-se a:** Auditoria da base e verificação de nível de confiança

## Neste documento

- [Como ler](#como-ler)
- [Documentos gerados a partir de dados](#documentos-gerados-a-partir-de-dados)
- [Documentos redigidos manualmente](#documentos-redigidos-manualmente)
- [Contagens verificáveis](#contagens-verificáveis)
- [Próximos passos](#próximos-passos)

## Contexto

Permite ir de qualquer informação da documentação até a célula de origem, e vice-versa. É o instrumento de auditoria da base.

## Escopo

Mapeamento informação → aba de origem → documento → nível de confiança, no nível de coluna/campo.

## Fora do escopo

O conteúdo em si; a análise de conflitos, que está em [pendencias.md](pendencias.md).

## Relação com outros documentos

- [Fontes](fontes.md)
- [Pendências](pendencias.md)
- [Índice da documentação](../00-indice.md)

---

## Como ler

Cada linha descreve **um grupo de informação**, identificado pela coluna de origem na planilha.
O nível de confiança segue a convenção definida em [00-indice.md](../00-indice.md).

## Documentos gerados a partir de dados

| Informação | Fonte (arquivo → aba → coluna) | Documento | Confiança |
| --- | --- | --- | --- |
| Família de BIOS de cada código | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `FABRICANTE BIOS` | `09-codigos-post/*` | Confirmado |
| Plataforma de aplicação do código | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `FABRICANTE / PLATAFORMA` | `09-codigos-post/*` | Confirmado |
| Natureza do sinal (beep, hex, LED, tom) | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `TIPO DE SINAL` | `09-codigos-post/*` | Confirmado |
| Valor literal do código | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `CÓDIGO` | `09-codigos-post/*` | Confirmado |
| Significado declarado do código | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `INTERPRETAÇÃO OFICIAL` | `09-codigos-post/*` | Confirmado |
| Componente indicado pelo código | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `COMPONENTE AFETADO` | `09-codigos-post/*` | Confirmado |
| Camada (modelo A) do código | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `CAMADA DE DIAGNÓSTICO` | `09-codigos-post/*` | Confirmado |
| Fase do POST em que o código ocorre | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `FASE POST` | `09-codigos-post/*` | Confirmado |
| Causa raiz declarada | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `CAUSA RAIZ (Documentação Oficial)` | `09-codigos-post/*` | Confirmado |
| Condições que produzem o erro | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `CONDIÇÕES QUE GERAM O ERRO` | `09-codigos-post/*` | Confirmado |
| Procedimento de diagnóstico | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `MÉTODO DE DIAGNÓSTICO TÉCNICO` | `09-codigos-post/*` | Confirmado |
| Ferramentas exigidas pelo código | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `FERRAMENTAS OFICIAIS` | `09-codigos-post/*` | Confirmado |
| Procedimento de correção | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `PROCEDIMENTO DE CORREÇÃO (Passo a Passo)` | `09-codigos-post/*` | Confirmado |
| Critério de validação do reparo | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `CRITÉRIO DE VALIDAÇÃO` | `09-codigos-post/*` | Confirmado |
| Classificação de risco | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `RISCO / CRITICIDADE` | `09-codigos-post/*` | Confirmado |
| Referência declarada pela fonte | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `FONTE OFICIAL` | `09-codigos-post/*` | Não confirmado |
| Identificador POST-NN | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Tabela Diagnóstico POST` → `(ordem das linhas)` | `09-codigos-post/*` | **Inferido (organizacional)** |
| Número da etapa do fluxo de POST | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Fluxo de Diagnóstico` → `ETAPA` | `06-fluxo-post.md` | Confirmado |
| Pergunta de decisão da etapa | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Fluxo de Diagnóstico` → `CONDIÇÃO / PERGUNTA` | `06-fluxo-post.md` | Confirmado |
| Ramo afirmativo | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Fluxo de Diagnóstico` → `AÇÃO SE SIM` | `06-fluxo-post.md` | Confirmado |
| Ramo negativo | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Fluxo de Diagnóstico` → `AÇÃO SE NÃO` | `06-fluxo-post.md` | Confirmado |
| Encadeamento entre etapas | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Fluxo de Diagnóstico` → `PRÓXIMA ETAPA` | `06-fluxo-post.md` | Confirmado |
| Observações da etapa | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Fluxo de Diagnóstico` → `OBSERVAÇÕES` | `06-fluxo-post.md` | Confirmado |
| Número da camada (modelo A) | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Camadas de Diagnóstico` → `CAMADA` | `08-diagnostico-por-camada.md`, `03-taxonomia-camadas.md` | Confirmado |
| Nome da camada | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Camadas de Diagnóstico` → `NOME` | `08-diagnostico-por-camada.md`, `03-taxonomia-camadas.md` | Confirmado |
| Componentes da camada | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Camadas de Diagnóstico` → `COMPONENTES` | `08-diagnostico-por-camada.md` | Confirmado |
| Sintomas típicos da camada | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Camadas de Diagnóstico` → `SINTOMAS TÍPICOS` | `08-diagnostico-por-camada.md` | Confirmado |
| Testes primários da camada | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Camadas de Diagnóstico` → `TESTES PRIMÁRIOS` | `08-diagnostico-por-camada.md` | Confirmado |
| Ferramentas da camada | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Camadas de Diagnóstico` → `FERRAMENTAS` | `08-diagnostico-por-camada.md`, `04-requisitos-e-ferramentas.md` | Confirmado |
| Indicadores de falha da camada | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Camadas de Diagnóstico` → `INDICADORES DE FALHA` | `08-diagnostico-por-camada.md` | Confirmado |
| Sinal com mais de um significado | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Ambiguidade de Códigos` → `CÓDIGO AMBÍGUO` | `11-ambiguidades.md` | Confirmado |
| Significados concorrentes por fabricante | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Ambiguidade de Códigos` → `FABRICANTE 1/2/3 e SIGNIFICADO 1/2/3` | `11-ambiguidades.md` | Confirmado |
| Como distinguir os significados | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Ambiguidade de Códigos` → `CRITÉRIO DE DIFERENCIAÇÃO` | `11-ambiguidades.md` | Confirmado |
| Teste de desempate | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → `Ambiguidade de Códigos` → `TESTE PARA IDENTIFICAR CAUSA` | `11-ambiguidades.md` | Confirmado |
| Identificador do cenário | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `ID` | `10-cenarios/*` | Confirmado |
| Sintoma relatado | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Sintoma Observado` | `10-cenarios/*` | Confirmado |
| Camada (modelo B) do cenário | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Camada Afetada` | `10-cenarios/*` | Confirmado |
| Componente suspeito | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Componente Suspeito` | `10-cenarios/*` | Confirmado |
| Condição em que o sintoma aparece | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Condição de Ocorrência` | `10-cenarios/*` | Confirmado |
| Causa raiz declarada | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Causa Raiz` | `10-cenarios/*` | Confirmado |
| Procedimento de diagnóstico | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Método de Diagnóstico (Passo a Passo)` | `10-cenarios/*` | Confirmado |
| Ferramentas exigidas | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Ferramentas Oficiais` | `10-cenarios/*` | Confirmado |
| Comandos a executar | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Comandos Técnicos` | `10-cenarios/*` | Confirmado |
| Procedimento de correção | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Procedimento de Correção (Detalhado)` | `10-cenarios/*` | Confirmado |
| Prioridade de execução | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Ordem de Execução` | `10-cenarios/*` | Confirmado |
| Pré-requisitos entre cenários | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Dependências` | `10-cenarios/*` | Confirmado |
| Critério de validação | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Critério de Validação Técnica` | `10-cenarios/*` | Confirmado |
| Evidência mensurável de sucesso | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Evidência de Sucesso` | `10-cenarios/*` | Confirmado |
| Classificação de risco | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Risco Associado` | `10-cenarios/*` | Confirmado |
| Impacto da falha | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Impacto no Sistema` | `10-cenarios/*` | Confirmado |
| Referência declarada pela fonte | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `TABELA_PRINCIPAL` → `Fonte Oficial` | `10-cenarios/*` | Não confirmado |
| Identificador do nó de decisão | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `FLUXO_LOGICO` → `Nó` | `07-fluxo-sistemico.md` | Confirmado |
| Pergunta do nó | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `FLUXO_LOGICO` → `Condição / Pergunta` | `07-fluxo-sistemico.md` | Confirmado |
| Ramos do nó | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `FLUXO_LOGICO` → `SE Verdadeiro → / SE Falso →` | `07-fluxo-sistemico.md` | Confirmado |
| Ação a executar no nó | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `FLUXO_LOGICO` → `Ação` | `07-fluxo-sistemico.md` | Confirmado |
| Ferramentas do nó | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `FLUXO_LOGICO` → `Ferramentas` | `07-fluxo-sistemico.md` | Confirmado |
| Cenário associado ao nó | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `FLUXO_LOGICO` → `Referência (ID)` | `07-fluxo-sistemico.md` | Confirmado |
| Identificador da correlação | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `ID` | `12-correlacoes.md` | Confirmado |
| Camadas envolvidas (modelo B) | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `Falha Primária (Camada) / Efeito Cascata (Camada)` | `12-correlacoes.md` | Confirmado |
| Como a falha se propaga | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `Mecanismo de Propagação` | `12-correlacoes.md` | Confirmado |
| Sintoma percebido | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `Sintoma Resultante` | `12-correlacoes.md` | Confirmado |
| Ordem de teste recomendada | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `Diagnóstico Diferencial` | `12-correlacoes.md` | Confirmado |
| Erro frequente de diagnóstico | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `Armadilha Comum` | `12-correlacoes.md` | Confirmado |
| Critério de desempate | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `Como Distinguir` | `12-correlacoes.md` | Confirmado |
| Referência declarada pela fonte | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `CORRELACOES` → `Fonte` | `12-correlacoes.md` | Não confirmado |
| Componente validado | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `VALIDACAO_FINAL` → `Componente` | `13-validacao-final.md` | Confirmado |
| Teste a executar após o reparo | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `VALIDACAO_FINAL` → `Teste Pós-Correção` | `13-validacao-final.md` | Confirmado |
| Ferramenta do teste | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `VALIDACAO_FINAL` → `Ferramenta de Validação` | `13-validacao-final.md`, `04-requisitos-e-ferramentas.md` | Confirmado |
| Indicador observável | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `VALIDACAO_FINAL` → `Indicador de Sucesso` | `13-validacao-final.md` | Confirmado |
| Duração exigida | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `VALIDACAO_FINAL` → `Tempo de Observação` | `13-validacao-final.md` | Confirmado |
| Limiares de aprovação e reprovação | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `VALIDACAO_FINAL` → `Critério PASS / Critério FAIL` | `13-validacao-final.md` | Confirmado |
| Encaminhamento em caso de reprovação | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `VALIDACAO_FINAL` → `Ação se FAIL` | `13-validacao-final.md` | Confirmado |
| Nome do cenário | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `INDICE_CENARIOS` → `Cenário` | `10-cenarios/00-indice-cenarios.md` | Confirmado |
| Agrupamento dos IDs por cenário | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `INDICE_CENARIOS` → `IDs Relacionados` | `10-cenarios/00-indice-cenarios.md` | Confirmado |
| Camada de entrada (modelo B) | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `INDICE_CENARIOS` → `Camada Primária` | `10-cenarios/00-indice-cenarios.md` | Confirmado |
| Teste inicial recomendado | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `INDICE_CENARIOS` → `Primeiro Teste` | `10-cenarios/00-indice-cenarios.md` | Confirmado |
| Ferramentas do cenário | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `INDICE_CENARIOS` → `Ferramentas Necessárias` | `10-cenarios/00-indice-cenarios.md`, `04-requisitos-e-ferramentas.md` | Confirmado |
| Etapas operacionais (20 campos: objetivo, ação, caminho, atalho, configurações, verificação prévia, erros, causa, identificação, correção, validação, risco, impacto, tempo, observações, boas práticas, alternativa, checklist) | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `REF_Victoria` → `(todas as colunas)` | `14-ferramentas/victoria.md` | Confirmado |
| Etapas operacionais (20 campos: objetivo, ação, caminho, atalho, configurações, verificação prévia, erros, causa, identificação, correção, validação, risco, impacto, tempo, observações, boas práticas, alternativa, checklist) | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `REF_AIDA64` → `(todas as colunas)` | `14-ferramentas/aida64-etapas-*.md` | Confirmado |
| Etapas operacionais (20 campos: objetivo, ação, caminho, atalho, configurações, verificação prévia, erros, causa, identificação, correção, validação, risco, impacto, tempo, observações, boas práticas, alternativa, checklist) | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `REF_MemTest86` → `(todas as colunas)` | `14-ferramentas/memtest86.md` | Confirmado |
| Critérios de decisão pós-teste | `HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx` → `REF_MemTest86` → `última linha, coluna `Nº da Etapa`` | `14-ferramentas/memtest86.md` | Confirmado |

## Documentos redigidos manualmente

Estes documentos não transcrevem células: organizam, explicam e sinalizam. Cada afirmação técnica
que contêm remete a um documento gerado.

| Documento | Natureza | Confiança |
| --- | --- | --- |
| `README.md` | Apresentação e navegação | Confirmado |
| `00-indice.md` | Mapa da documentação | Confirmado (estrutura) |
| `01-visao-geral.md` | Descrição do projeto e contagens | Confirmado (contagens e identificação) / Necessita validação (versão do conteúdo técnico) |
| `02-arquitetura.md` | Organização e mapa de origem | Confirmado (mapa) / Inferido (diagrama de eixos) |
| `03-taxonomia-camadas.md` | Registro de conflito entre modelos | Confirmado (modelo A) / Necessita validação (modelo B) |
| `04-requisitos-e-ferramentas.md` | Agregação de colunas de ferramentas | Confirmado |
| `05-utilizacao.md` | Roteiro de navegação | Inferido sobre conteúdo Confirmado |
| `15-limitacoes.md` | Lacunas e divergências verificadas | Confirmado |
| `16-faq.md` | Perguntas derivadas do conteúdo | Confirmado (respostas) |
| `17-glossario.md` | Termos com definição da fonte | Confirmado / sinalizado por termo |
| `references/*` | Rastreabilidade e auditoria | Confirmado |

## Contagens verificáveis

| Métrica | Valor |
| --- | --- |
| Códigos de POST | 54 |
| Cenários (IDs) | 13 |
| Cenários (agrupamentos) | 9 |
| Camadas modelo A | 7 |
| Camadas modelo B observadas | 10 números distintos (1–10) |
| Etapas do fluxo de POST | 7 |
| Nós do fluxo sistêmico | 17 |
| Casos de ambiguidade | 5 |
| Correlações | 6 |
| Componentes na validação final | 10 |
| Etapas de ferramentas | 64 |
| Referências externas citadas pelas fontes | 56 (não verificadas) |
| Fontes externas consultadas por esta documentação | 1 (repositório oficial) |

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| quer os arquivos de origem e seus hashes | [Fontes](fontes.md) |
| encontrou uma informação sem confirmação | [Pendências](pendencias.md) |
| vai alterar a documentação | [Como contribuir](../../CONTRIBUTING.md) |


---

| | |
| --- | --- |
| **Fonte primária deste documento** | Ambos os arquivos-fonte |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação contra a fonte** | 2026-08-07 |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-1.4.0` |
