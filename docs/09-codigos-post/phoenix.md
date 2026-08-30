[Início](https://www.google.com/search?q=../../README.md) › [Resolva](https://www.google.com/search?q=../../README.md%23resolva) › **Códigos POST — Lenovo (SmartBeep / Beep binário)**

# Referência de Códigos de Erro POST: Lenovo (SmartBeep / Binário)

**Aplica-se a:** Equipamentos com BIOS `Proprietário Lenovo` (Linhas ThinkPad e ThinkCentre)

Este artigo fornece a referência completa de diagnóstico e resolução para os códigos de erro baseados em bipes da família Lenovo (SmartBeep / beep binário). Utilize o índice abaixo para navegar diretamente para a sequência identificada.

---

## Neste artigo

* [Melodia Variável: SmartBeep (Lenovo PC Diagnostics)](https://www.google.com/search?q=%23melodia-vari%C3%A1vel-smartbeep-lenovo-pc-diagnostics)
* [0110 (Binário): Falha no Chip de Segurança TPM](https://www.google.com/search?q=%230110-bin%C3%A1rio-falha-no-chip-de-seguran%C3%A7a-tpm)
* [Consulte também](https://www.google.com/search?q=%23consulte-tamb%C3%A9m)

---

## Melodia Variável: SmartBeep (Lenovo PC Diagnostics)

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Lenovo PC Diagnostics* (Código sonoro interpretável via aplicativo) |
| **Componente afetado** | Variável |
| **Fase / Camada** | Fase POST: Variável / Camada: Variável |
| **Criticidade** | Variável |

### Causas

Os modelos ThinkPad modernos (a partir da 7ª geração de processadores Intel Core e modelos posteriores de 2018 em diante) utilizam a tecnologia proprietária *SmartBeep*. Quando ocorre uma falha com tela preta, o sistema emite um sinal sonoro em formato de melodia codificada que representa o erro de hardware.

* As condições que geram o erro variam de acordo com o subsistema afetado, dependendo inteiramente da decodificação realizada pelo aplicativo oficial de suporte.

### Diagnóstico e Resolução

**Ferramentas oficiais:** Aplicativo móvel *Lenovo PC Diagnostics* (compatível com smartphones e tablets baseados em Android e iOS).

1. Acesse o portal de suporte oficial em `https://support.lenovo.com/smartbeep` ou utilize o leitor de QR Code disponibilizado nos manuais da marca.
2. Baixe e instale o aplicativo **Lenovo PC Diagnostics** em seu dispositivo móvel.
3. Abra o aplicativo e selecione a opção de decodificação por áudio (*SmartBeep*).
4. Posicione o smartphone próximo ao alto-falante (*speaker*) do equipamento ThinkPad ou ThinkCentre afetado.
5. **Ação indispensável:** Caso o ciclo de bipes já tenha ocorrido e o computador permaneça em tela preta sem repetir o som automaticamente, pressione a tecla **Fn** no teclado do computador para forçar a reemissão da melodia enquanto o aplicativo estiver escutando.
6. O aplicativo processará o espectro acústico, decodificará o sinal sonoro e exibirá na tela o código de erro específico, o componente de hardware afetado e as diretrizes de solução.
7. Siga estritamente o procedimento recomendado pela ferramenta ou consulte o respectivo Manual de Manutenção de Hardware (*HMM - Hardware Maintenance Manual*) do modelo do equipamento.

### Validação

O aplicativo reconhece a melodia com precisão e o procedimento corretivo soluciona a falha. O sistema completo executa o POST com êxito e o utilitário integrado de diagnóstico (*Lenovo Diagnostics* acionado via tecla F10) conclui as verificações sem registrar anomalias.

---

## 0110 (Binário): Falha no Chip de Segurança TPM

| Atributo | Detalhe |
| --- | --- |
| **Mensagem oficial** | *Security Chip (TPM) Error* — Falha no chip de segurança TPM |
| **Componente afetado** | TPM (Trusted Platform Module) |
| **Fase / Camada** | Fase POST: Security Init / Camada 5: Chipset / Motherboard |
| **Criticidade** | Alto |

### Causas

O subsistema do chip de segurança *Trusted Platform Module* (TPM) falhou ao inicializar ou deixou de responder durante a rotina de POST. Nos notebooks ThinkPad, o TPM desempenha papéis cruciais para a integridade do sistema, sendo amplamente utilizado para criptografia de dados via BitLocker, recursos de autenticação e políticas corporativas de segurança.

* Corrupção lógica nos dados ou no firmware residente do TPM.
* Desativação incorreta ou desalinhamento das flags de segurança no firmware da placa.
* Perda ou corrupção de parâmetros na NVRAM após a execução de uma atualização de BIOS (*BIOS Update*).
* Avaria física direta no componente discreto do TPM ou falha de comunicação com o PCH/Chipset.

### Diagnóstico e Resolução

**Ferramentas oficiais:** Utilitário BIOS Setup (acessado pela tecla **F1**) e pacotes oficiais de atualização de BIOS da Lenovo.

1. Ligue o equipamento e pressione repetidamente a tecla **F1** durante a exibição da tela inicial de POST para entrar no utilitário de configuração do BIOS.
2. Navegue até a aba ou seção de **Security** e localize a opção **Security Chip** para inspecionar o status atual de funcionamento do módulo.
3. Caso a opção esteja acessível, selecione o comando para limpar os registros do componente (**Security Chip → Clear**), salve as alterações e reinicie o sistema.
4. Se o erro persistir após a limpeza lógica:
* Realize a atualização do firmware do BIOS para a versão mais recente disponibilizada pelo canal oficial de suporte da Lenovo para o modelo específico.
* Concluído o processo de atualização, retorne ao BIOS e repita a operação de limpeza do TPM (*Clear*).


5. Em cenários onde o chip TPM seja diagnosticado como inoperante definitivo ("morto"), tente desabilitar o *Security Chip* diretamente no BIOS (caso o perfil da placa permita). **ATENÇÃO CRÍTICA:** Se a unidade possuir partições protegidas por criptografia BitLocker ativa, desabilitar ou limpar o TPM sem a devida precaução tornará os dados inacessíveis; assegure-se de realizar o backup prévio da chave de recuperação (*recovery key*) antes de prosseguir com esta etapa.
6. Tratando-se de falha física em um chip TPM discreto, o cenário exige intervenção avançada de laboratório para reparo em nível de componente ou a substituição integral da placa-mãe (*system board*).

### Validação

O módulo TPM passa a ser detectado corretamente pelo firmware no painel do BIOS, e os recursos de criptografia (como o BitLocker) operam sem restrições. No ambiente do sistema operacional Windows, a execução do console de gerenciamento por meio do comando `tpm.msc` deve retornar o status informando que o chip está pronto para uso.

---

## Consulte também

Para aprofundamento técnico ou informações sobre o fluxo de atendimento, consulte os documentos relacionados:

* **[Índice de códigos POST](https://www.google.com/search?q=00-indice-codigos.md):** Catálogo completo.
* **[Ambiguidade de códigos](https://www.google.com/search?q=../11-ambiguidades.md):** Verifique divergências de sinais entre fabricantes.
* **[Diagnóstico por camada](https://www.google.com/search?q=../08-diagnostico-por-camada.md):** Metodologia de testes nos subsistemas de hardware.
* **[Fluxo de diagnóstico POST](https://www.google.com/search?q=../06-fluxo-post.md):** Como chegar até o código partindo de um sintoma generalizado.
* **[Validação final por componente](https://www.google.com/search?q=../13-validacao-final.md):** Testes recomendados para fechamento de atendimento com segurança.

---

| Metadados do Artigo |  |
| --- | --- |
| **Fonte oficial** | Documentação Oficial Lenovo SmartBeep / Manuais HMM / Guias de BIOS Lenovo |
| **Fonte primária interna** | `HW_HARDWARE_CODIGOS_DE_ERROS.xlsx` → aba `Tabela Diagnóstico POST` |
| **Status de confiança** | Confirmado — transcrito das células de origem e validado com documentação técnica de suporte |
| **Última verificação** | 2026-08-29 |
| **Autoria** | Edsilas |
| **Versão da doc.** | `doc-2.0.0` |
