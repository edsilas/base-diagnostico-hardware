<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Acer / Insyde**

# Erro de POST: 1 Longo + 2 Curtos (Acer / Insyde)

**Aplica-se a:** Equipamentos com BIOS Proprietário Acer / Insyde (Acer Aspire, Nitro, Predator)

Este artigo fornece detalhes de diagnóstico e resolução para o código de erro POST **1 Longo + 2 Curtos** da família de BIOS proprietária Acer / Insyde. 

---

## Visão geral do erro

| Atributo | Detalhe |
| :--- | :--- |
| **Código** | `1 Longo + 2 Curtos` |
| **Tipo de sinal** | Beep Sonoro |
| **Mensagem oficial** | *Video Interface Error* (Erro na interface de vídeo) |
| **Fase POST** | Video Init |
| **Componente afetado** | GPU / Cabo Flat (LVDS/eDP) |
| **Camada de diagnóstico**| Camada 4: Vídeo |
| **Criticidade** | Alta |

---

## Causas

O sistema emite 1 bipe longo seguido de 2 bipes curtos ao ligar. Este comportamento indica uma falha na interface de vídeo. Em notebooks Acer, este problema é frequentemente causado por um cabo flat LVDS/eDP rompido na região da dobradiça (ponto de maior estresse mecânico).

As condições que geram este erro incluem:

* Cabo flat LVDS/eDP desconectado ou rompido.
* Defeito no chip gráfico (GPU).
* Defeito no painel LCD (tela).
* Mau contato no conector da placa-mãe.

---

## Diagnóstico

Antes de iniciar o reparo físico da máquina, isole o componente que está falhando utilizando ferramentas básicas de bancada.

**Ferramentas necessárias:** Monitor externo (com cabo HDMI ou VGA) e Multímetro (para teste de continuidade).

**Etapas de isolamento:**
1. Conecte o monitor externo à porta de vídeo do notebook.
2. Ligue o computador e aguarde o processamento do vídeo.
3. Analise o resultado para determinar o plano de ação:
   * **Se houver imagem no monitor externo:** A falha está restrita ao cabo flat ou à tela LCD.
   * **Se não houver imagem no monitor externo:** A falha está na GPU ou na placa-mãe.

---

## Resolução

Siga os procedimentos abaixo com base no resultado obtido na fase de diagnóstico.

### Cenário A: O problema está no cabo ou na tela
Se o equipamento apresentou vídeo no monitor externo, o reparo consiste em verificar a via de comunicação com o painel nativo:

1. Remova a moldura da tela soltando os clipes plásticos com cuidado.
2. Inspecione visualmente o cabo flat, especialmente na área que sofre flexão pela dobradiça.
3. Verifique e reconecte as extremidades do cabo flat no painel LCD e na placa-mãe.
4. Execute um teste de continuidade no cabo flat com o multímetro.
5. **Se o cabo estiver rompido:** Substitua o cabo flat por uma peça específica do mesmo modelo.
6. **Se o cabo estiver intacto:** O painel LCD está com defeito. Substitua a tela.

### Cenário B: O problema está na GPU ou Placa-mãe
Se o equipamento não apresentou vídeo no monitor externo, o componente primário de vídeo falhou:

1. Encaminhe o equipamento para reparo BGA profissional ou proceda com a substituição completa da placa-mãe.

---

## Validação

Após aplicar a correção física, ligue o equipamento para validar o reparo. O sistema deve atender aos seguintes critérios:

* Imagem estável e nítida na tela interna e no monitor externo.
* Ausência de *flickering* (cintilação).
* Ausência de artefatos gráficos.

---

## Consulte também

Para aprofundamento técnico ou informações sobre o fluxo de atendimento, consulte os documentos relacionados:

* **[Ambiguidade de códigos](../11-ambiguidades.md#1-longo--2-curtos):** Este código é ambíguo. Verifique o critério de diferenciação antes de aplicar o procedimento.
* **[Camada 4: Vídeo](../08-diagnostico-por-camada.md#camada-4--vídeo-gpuigpu):** Aprofunde-se no diagnóstico da camada correspondente.
* **[Índice de códigos POST](00-indice-codigos.md):** Catálogo completo caso não tenha encontrado o código esperado.
* **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até este código partindo de um sintoma generalizado.
* **[Diagnóstico por camada](../08-diagnostico-por-camada.md):** Metodologia de testes nos subsistemas de hardware.
* **[Validação final por componente](../13-validacao-final.md):** Testes recomendados para fechar o atendimento com segurança.
* **[Índices cruzados](../18-indices-cruzados.md):** Outros códigos do mesmo componente ou nível de risco.

---

| Metadados do Artigo | |
| :--- | :--- |
| **Fonte oficial** | Acer Service Manual / Insyde BIOS Reference |
| **Fonte primária interna** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da doc.** | `doc-2.0.0` |
