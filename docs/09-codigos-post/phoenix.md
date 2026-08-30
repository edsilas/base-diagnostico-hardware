<!-- Gerado a partir de `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST`. Não editar manualmente sem atualizar a fonte. -->

[Início](../../README.md) › [Resolva](../../README.md#resolva) › **Códigos POST — Lenovo (SmartBeep / beep binário)**

# Referência de Códigos de Erro POST: Lenovo (SmartBeep / Binário)

**Aplica-se a:** Equipamentos com BIOS `Proprietário Lenovo` (Linhas ThinkPad e ThinkCentre)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos de erro baseados em bipes da família Lenovo (SmartBeep / beep binário). Utilize o índice abaixo para navegar diretamente para a sequência identificada.

---

## Neste artigo

- [Melodia Variável: SmartBeep](#melodia-variável-smartbeep)
- [0110 (Binário): Falha no Chip de Segurança TPM](#0110-binário-falha-no-chip-de-segurança-tpm)
- [Consulte também](#consulte-também)

---

## Melodia Variável: SmartBeep

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Lenovo PC Diagnostics* (Código sonoro interpretável via app) |
| **Componente afetado** | Variável |
| **Fase / Camada** | Fase POST: Variável / Camada: Variável |
| **Criticidade** | Variável |

### Causas
Os Lenovo ThinkPads modernos usam o sistema SmartBeep: uma sequência melódica que pode ser decodificada pelo aplicativo *Lenovo PC Diagnostics* no smartphone. O aplicativo ouve o padrão sonoro e o traduz em um código de erro específico. 
* As condições que geram o erro são variáveis, dependendo inteiramente do código decodificado pelo app.

### Diagnóstico e Resolução
**Ferramentas oficiais:** App *Lenovo PC Diagnostics* (smartphone iOS/Android).
1. Acesse `https://support.lenovo.com/smartbeep`.
2. Baixe o aplicativo *Lenovo PC Diagnostics* e instale-o no seu smartphone.
3. Abra o aplicativo e selecione a opção **SmartBeep**.
4. Ligue o sistema ThinkPad/ThinkCentre e posicione o smartphone próximo ao *speaker* (alto-falante).
5. **Ação indispensável:** Em sintomas de tela preta acompanhada de bipes, se o bipe já ocorreu e não se repete sozinho, pressione a tecla **Fn** no computador para emitir o bipe novamente (com o aplicativo já em execução e o smartphone próximo). Sem isso, não há sinal para decodificar.
6. O aplicativo identificará o padrão e exibirá: o código de erro, o componente afetado e o procedimento sugerido.
7. Siga o procedimento indicado pelo aplicativo. Se não resolver, consulte o Lenovo PSREF e o HMM (*Hardware Maintenance Manual*) do equipamento.

### Validação
O aplicativo identifica o código e o procedimento resolve o erro. O equipamento completa o POST com sucesso e o *Lenovo Diagnostics* (tecla F10) é executado sem registrar falhas.

---

## 0110 (Binário): Falha no Chip de Segurança TPM

| Atributo | Detalhe |
| :--- | :--- |
| **Mensagem oficial** | *Security Chip (TPM) Error* — Falha no chip de segurança TPM |
| **Componente afetado** | TPM (Trusted Platform Module) |
| **Fase / Camada** | Fase POST: Security Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Alto |

### Causas
O chip TPM (*Trusted Platform Module*) não responde ou apresenta erro. Em ThinkPads, o TPM é usado para a criptografia do BitLocker, autenticação e funções de segurança empresarial.
* Firmware do TPM corrompido.
* TPM desabilitado incorretamente.
* Configuração do TPM perdida/resetada após uma atualização de BIOS.
* Chip TPM com defeito físico.

### Diagnóstico e Resolução
**Ferramentas oficiais:** BIOS Setup (F1) / Lenovo BIOS Update.
1. Acesse o BIOS Setup pressionando a tecla **F1** ao ligar a máquina, na tela de POST.
2. Navegue até o menu **Security** → **Security Chip** e verifique o estado do TPM.
3. Se a opção estiver disponível, selecione **Security Chip → Clear**. Salve as configurações e reinicie.
4. Se o problema persistir:
   * Atualize o BIOS para a versão mais recente disponível no site da Lenovo.
   * Após o término do update, repita a operação de *Clear* do TPM.
5. Se o TPM for diagnosticado como inoperante ("morto"): desabilite o *Security Chip* no BIOS (se possível). **ATENÇÃO:** Se o BitLocker estiver ativo, os dados podem ficar inacessíveis. Faça o backup da *recovery key* (chave de recuperação) ANTES de executar essa ação.
6. Se for um TPM discreto (não fTPM) com defeito físico, será necessário o reparo em nível de componente ou a troca da placa-mãe.

### Validação
O TPM é reconhecido adequadamente no BIOS. A criptografia BitLocker (se aplicável) está funcional. No Windows, a execução de `tpm.msc` reporta que o TPM está pronto para uso.

---

## Consulte também

Para aprofundamento técnico ou informações sobre o fluxo de atendimento, consulte os documentos relacionados:

* **[Índice de códigos POST](00-indice-codigos.md):** Catálogo completo.
* **[Ambiguidade de códigos](../11-ambiguidades.md):** Verifique divergências de sinais entre fabricantes.
* **[Diagnóstico por camada](../08-diagnostico-por-camada.md):** Metodologia de testes nos subsistemas de hardware.
* **[Fluxo de diagnóstico POST](../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.
* **[Validação final por componente](../13-validacao-final.md):** Testes recomendados para fechamento de atendimento com segurança.

---

| Metadados do Artigo | |
| :--- | :--- |
| **Fonte oficial** | Lenovo SmartBeep Documentation / Lenovo HMM / Lenovo BIOS Guide |
| **Fonte primária interna** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem |
| **Última verificação** | 2026-08-08 |
| **Autoria** | Edsilas |
| **Versão da doc.** | `doc-2.0.0` |
