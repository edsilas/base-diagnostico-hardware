---
title: Códigos do Gerenciador de Dispositivos (Windows)
description: Os 18 códigos de erro que o Windows exibe quando um dispositivo não é detectado, não inicia ou está com o driver defeituoso, com o procedimento de correção de cada um.
author: Edsilas
date: 2026-08-30
---

[Início](../README.md) › [Resolva](../README.md#resolva) › **Códigos do Gerenciador de Dispositivos**

# Códigos do Gerenciador de Dispositivos (Windows)

> Os 18 códigos que o Windows exibe quando um dispositivo não é detectado, não inicia ou está com o driver defeituoso — com o que cada um significa, como confirmar e como corrigir.

**Aplica-se a:** Equipamentos que concluem o POST e carregam o Windows, mas em que uma peça não aparece, aparece com aviso amarelo ou não funciona

## Neste documento

- [Contexto](#contexto)
- [Escopo](#escopo)
- [Fora do escopo](#fora-do-escopo)
- [Relação com outros documentos](#relação-com-outros-documentos)
- [Como ler este documento](#como-ler-este-documento)
- [Como chegar ao código](#como-chegar-ao-código)
- [Escala de risco deste documento](#escala-de-risco-deste-documento)
- [Catálogo de códigos](#catálogo-de-códigos)
- [Código 1 — Dispositivo sem driver instalado](#código-1--dispositivo-sem-driver-instalado)
- [Código 10 — O dispositivo não conseguiu iniciar](#código-10--o-dispositivo-não-conseguiu-iniciar)
- [Código 12 — Conflito de recursos entre dispositivos](#código-12--conflito-de-recursos-entre-dispositivos)
- [Código 14 — O dispositivo exige reinicialização](#código-14--o-dispositivo-exige-reinicialização)
- [Código 18 — É preciso reinstalar o driver](#código-18--é-preciso-reinstalar-o-driver)
- [Código 19 — Configuração no registro incompleta ou danificada](#código-19--configuração-no-registro-incompleta-ou-danificada)
- [Código 22 — Dispositivo desativado no Windows](#código-22--dispositivo-desativado-no-windows)
- [Código 24 — Dispositivo ausente, com defeito ou incompleto](#código-24--dispositivo-ausente-com-defeito-ou-incompleto)
- [Código 28 — Driver não instalado](#código-28--driver-não-instalado)
- [Código 29 — Dispositivo desativado no firmware (BIOS/UEFI)](#código-29--dispositivo-desativado-no-firmware-biosuefi)
- [Código 31 — O Windows não conseguiu carregar os drivers exigidos](#código-31--o-windows-não-conseguiu-carregar-os-drivers-exigidos)
- [Código 32 — O serviço do driver está desabilitado](#código-32--o-serviço-do-driver-está-desabilitado)
- [Código 37 — O Windows não conseguiu inicializar o driver](#código-37--o-windows-não-conseguiu-inicializar-o-driver)
- [Código 39 — Driver corrompido ou ausente](#código-39--driver-corrompido-ou-ausente)
- [Código 43 — O driver relatou falha do dispositivo](#código-43--o-driver-relatou-falha-do-dispositivo)
- [Código 45 — Dispositivo não conectado no momento](#código-45--dispositivo-não-conectado-no-momento)
- [Código 48 — Driver bloqueado por incompatibilidade conhecida](#código-48--driver-bloqueado-por-incompatibilidade-conhecida)
- [Código 52 — Assinatura digital do driver não pôde ser verificada](#código-52--assinatura-digital-do-driver-não-pôde-ser-verificada)
- [Próximos passos](#próximos-passos)

## Contexto

Quando o equipamento conclui o POST e carrega o Windows, o diagnóstico deixa de ser feito por bipe
ou LED e passa a ser feito pelo próprio sistema. O Gerenciador de Dispositivos marca com um aviso
amarelo toda peça que não subiu, e associa a ela um **código numérico** que diz por quê. Este
documento é o catálogo desses códigos, no mesmo formato das fichas de POST.

## Escopo

Os 18 códigos do Gerenciador de Dispositivos que correspondem a falha de hardware, de driver ou de
configuração de dispositivo: peça não detectada, peça com erro, driver ausente, driver incompatível,
driver corrompido, dispositivo desativado no Windows, dispositivo desativado no firmware, serviço
desabilitado, conflito de recursos e assinatura inválida.

## Fora do escopo

Os demais códigos definidos em `Cfg.h` que não descrevem uma condição acionável por quem faz o
reparo — falta de memória, dispositivo em remoção, dispositivo em uso por depurador, entre outros.
Também estão fora: códigos de POST (ver [Catálogo de códigos POST](09-codigos-post/00-indice-codigos.md)),
telas azuis (ver [BSOD](10-cenarios/bsod.md)) e diagnóstico de disco (ver [Victoria](14-ferramentas/victoria.md)).

## Relação com outros documentos

- [Fluxo de diagnóstico sistêmico](07-fluxo-sistemico.md) — onde este documento entra no atendimento
- [Diagnóstico por camada](08-diagnostico-por-camada.md) — o que testar quando o código apontar defeito físico
- [Catálogo de códigos POST](09-codigos-post/00-indice-codigos.md) — a etapa anterior, antes do Windows carregar
- [Cenários de falha](10-cenarios/00-indice-cenarios.md) — quando o sintoma não é um dispositivo específico
- [Segurança e boas práticas](15-seguranca-e-boas-praticas.md) — descarga de energia residual antes de reassentar peça

---

## Como ler este documento

Cada ficha tem seis partes, na ordem em que você precisa delas:

| Parte | O que traz |
| --- | --- |
| **Mensagem do Windows** | O texto exato exibido, em inglês. É o mesmo texto que o Windows em português exibe traduzido — use o **número do código** para se localizar, não a tradução |
| **O que significa** | A explicação da condição, em português |
| **O que verificar** | O que olhar antes de mexer em qualquer coisa |
| **Como corrigir** | Os passos, na ordem de execução |
| **Como confirmar** | O sinal objetivo de que funcionou |
| **Se continuar** | O que fazer quando a primeira tentativa não resolve, e quando parar |

> [!IMPORTANT]
> A mensagem está aqui em inglês. Este documento não publica uma tradução da string do Windows —
> transcrever errado o texto que o técnico vai procurar na tela seria pior que não transcrever. O
> identificador estável é o número: `(Code 43)` aparece igual em qualquer idioma.

## Como chegar ao código

Pelo Gerenciador de Dispositivos:

1. Pressione **Windows + R**, digite `devmgmt.msc` e confirme.
2. Procure os itens com aviso amarelo. Se não houver nenhum, abra **Exibir › Mostrar dispositivos ocultos**.
3. Clique duas vezes no item e leia a caixa **Status do dispositivo**. O código está no fim da mensagem, no formato `(Code NN)`.

Pela linha de comando, em um prompt **como administrador** — lista todos os dispositivos com problema
de uma vez:

```powershell
pnputil /enum-devices /problem
```

Para filtrar por um código específico:

```powershell
pnputil /enum-devices /problem 43
```

> [!NOTE]
> **Disponibilidade das opções do `pnputil`.** `/enum-devices` existe a
> partir do Windows 10 versão 1903; o filtro `/problem` também. `/enable-device`,
> `/disable-device`, `/restart-device`, `/remove-device` e `/scan-devices` existem a partir do
> Windows 10 versão 2004. Em versões anteriores, use o Gerenciador de Dispositivos.

## Escala de risco deste documento

Este documento declara a própria escala de risco, pelo **critério de reversibilidade da ação de
correção**:

| Nível | Significado |
| --- | --- |
| **Baixo** | A correção é reversível e não altera configuração do sistema fora do dispositivo |
| **Médio** | A correção mexe em firmware, em posicionamento físico de peça, ou depende de desligar o equipamento |
| **Alto** | A correção mexe em registro, em serviço do sistema ou em proteção de segurança, e pode impedir o Windows de iniciar se aplicada ao item errado |

---

## Catálogo de códigos

### Código 1 — Dispositivo sem driver instalado

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 1` |
| **Nome interno** | `CM_PROB_NOT_CONFIGURED` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "This device is not configured correctly. (Code 1)"
>
> "To Update the drivers for this device, click Update Driver. If that doesn't work, see your hardware documentation for more information."

**O que significa.** O Windows enxerga a peça, mas não encontrou nenhum driver para ela. A chave `ConfigFlags` do dispositivo não existe no registro — normalmente porque nenhum arquivo `.inf` compatível foi localizado.

**O que verificar**

1. Abra o Gerenciador de Dispositivos (`devmgmt.msc`) e localize o item com o aviso amarelo.
2. Confira em **Propriedades › Detalhes › IDs de Hardware** qual é a peça. Esse é o identificador que o fabricante usa para publicar o driver.

**Como corrigir**

1. No próprio dispositivo, use **Atualizar driver**.
2. Se o Windows não encontrar sozinho, baixe o driver no site do fabricante do equipamento (não de sites de driver genéricos) usando o ID de hardware anotado.
3. Instale e reinicie.

**Como confirmar.** O aviso amarelo desaparece e o dispositivo passa a aparecer com o nome real, não como *Dispositivo desconhecido*.

**Se continuar.** Se o código continuar depois de instalar o driver do fabricante, trate como **Código 28** — os dois casos são distintos: o 1 é *nenhuma tentativa de instalação*, o 28 é *tentou e não achou driver compatível*.

---

### Código 10 — O dispositivo não conseguiu iniciar

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 10` |
| **Nome interno** | `CM_PROB_FAILED_START` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "This device cannot start. (Code 10)"
>
> "Try upgrading the device drivers for this device."

**O que significa.** O driver está instalado, mas a peça recusou o comando de partida. Um dos drivers da pilha do dispositivo falhou o `IRP_MN_START_DEVICE`. Quando o driver publica um motivo próprio no registro (valor `FailReasonString`), o Windows mostra esse texto no lugar da mensagem genérica.

**O que verificar**

1. Leia a mensagem exibida: se ela for diferente do texto genérico acima, é o próprio fabricante explicando a causa — siga essa mensagem primeiro.
2. Verifique se a peça está bem encaixada e alimentada. Este código também aparece com contato ruim, não só com driver ruim.
3. Liste o problema pela linha de comando, como administrador: `pnputil /enum-devices /problem 10`

**Como corrigir**

1. Use **Atualizar driver** no dispositivo.
2. Se não resolver, desinstale o dispositivo e use **Ação › Verificar se há alterações de hardware** para reinstalá-lo.
3. Se a peça for removível (placa PCIe, módulo M.2, cabo de dados), desligue o equipamento, faça a descarga de energia residual, reassente a peça e ligue de novo.

**Como confirmar.** O dispositivo inicia sem aviso amarelo e `pnputil /enum-devices /problem 10` deixa de listá-lo.

**Se continuar.** O Código 10 não identifica sozinho qual driver da pilha falhou. Se persistir com driver novo e peça reassentada, trate como suspeita de defeito físico: vá para [Diagnóstico por camada](08-diagnostico-por-camada.md) e teste a peça em outro equipamento.

---

### Código 12 — Conflito de recursos entre dispositivos

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 12` |
| **Nome interno** | `CM_PROB_NORMAL_CONFLICT` |
| **Risco da correção** | Médio |

**Mensagem do Windows**:

> "This device cannot find enough free resources that it can use. (Code 12)"
>
> "If you want to use this device, you will need to disable one of the other devices on this system."

**O que significa.** Dois dispositivos receberam a mesma porta de E/S, a mesma interrupção ou o mesmo canal DMA. A atribuição pode ter vindo do BIOS, do sistema operacional ou da combinação dos dois. O código também aparece quando o BIOS simplesmente não alocou recursos suficientes para a peça.

**O que verificar**

1. Abra as propriedades do dispositivo e veja a aba **Recursos**: o Windows lista ali o conflito.
2. Anote qual é o outro dispositivo envolvido. O conflito sempre tem dois lados.

**Como corrigir**

1. Desative temporariamente o outro dispositivo do par para confirmar que o conflito é esse — o Gerenciador de Dispositivos é a ferramenta para localizar e resolver.
2. Se o equipamento tem placas de expansão, mova a placa para outro slot PCIe. Isso costuma mudar a atribuição de interrupção.
3. Atualize o firmware (BIOS/UEFI) pelo site do fabricante da placa-mãe. Tabela MPS inválida no BIOS é uma causa conhecida deste código.

**Como confirmar.** A aba **Recursos** deixa de reportar conflito e os dois dispositivos funcionam ao mesmo tempo.

**Se continuar.** Se o conflito voltar após atualizar o firmware, o limite é de plataforma, não de software: reduza o número de placas de expansão ou consulte o fabricante da placa-mãe sobre compartilhamento de recursos entre os slots.

---

### Código 14 — O dispositivo exige reinicialização

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 14` |
| **Nome interno** | `CM_PROB_NEED_RESTART` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "This device cannot work properly until you restart your computer. (Code 14)"
>
> "To restart your computer now, click Restart Computer."

**O que significa.** Uma operação de instalação ficou pendente e só se conclui no próximo boot. As causas comuns são: arquivo de driver que não pôde ser copiado e ficou na fila para o próximo boot, serviço que não pôde ser iniciado durante a instalação e problema ao reativar um dispositivo desativado.

**O que verificar**

1. Confirme que não há uma instalação de driver ou uma atualização do Windows em andamento.

**Como corrigir**

1. Reinicie o equipamento. É a única ação aplicável para este código.

**Como confirmar.** Depois do boot, o aviso amarelo some e o dispositivo funciona.

**Se continuar.** Se o Código 14 reaparecer a cada boot, a instalação não está se concluindo. Desinstale o driver, reinicie, e instale de novo a partir do pacote do fabricante.

---

### Código 18 — É preciso reinstalar o driver

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 18` |
| **Nome interno** | `CM_PROB_REINSTALL` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "Reinstall the drivers for this device. (Code 18)"

**O que significa.** O Windows determinou que o driver precisa ser instalado de novo. Este código é **frequentemente transitório**.

**O que verificar**

1. Antes de qualquer coisa, reinicie e verifique se o código persiste: boa parte dos casos se resolve sozinha.

**Como corrigir**

1. Reinstale pelo assistente: no Gerenciador de Dispositivos, clique com o botão direito no dispositivo e escolha **Atualizar driver**.
2. Se não resolver, o segundo procedimento é: **Desinstalar** o dispositivo e, no menu **Ação**, escolher **Verificar se há alterações de hardware** para reinstalá-lo.

**Como confirmar.** O dispositivo aparece sem aviso amarelo depois da reinstalação.

**Se continuar.** Se voltar depois de reinstalado, trate como driver defeituoso: obtenha o pacote diretamente do fabricante e veja o **Código 39**.

---

### Código 19 — Configuração no registro incompleta ou danificada

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 19` |
| **Nome interno** | `CM_PROB_REGISTRY` |
| **Risco da correção** | Alto |

**Mensagem do Windows**:

> "Windows cannot start this hardware device because its configuration information (in the registry) is incomplete or damaged. (Code 19)"

**O que significa.** As informações de configuração do dispositivo no registro do Windows estão inconsistentes. São três as origens possíveis: mais de um serviço definido para o mesmo dispositivo, falha ao abrir a chave do serviço, ou impossibilidade de obter o nome do driver a partir dessa chave.

> [!CAUTION]
> Procedimento de risco **Alto** nesta escala: ele altera registro, serviço do sistema ou proteção de segurança. Leia [Escala de risco deste documento](#escala-de-risco-deste-documento) e a seção *Se continuar* antes de executar.

**O que verificar**

1. Verifique se algum utilitário de limpeza de registro, otimizador ou antivírus foi executado pouco antes do problema aparecer. É o gatilho típico.

**Como corrigir**

1. Primeiro procedimento — desinstalar e reinstalar: no Gerenciador de Dispositivos, **Desinstalar** o dispositivo, depois **Ação › Verificar se há alterações de hardware**.
2. Segundo procedimento, se o primeiro não resolver: reiniciar em Modo de Segurança e escolher a opção **Última configuração válida**, revertendo o registro para o último estado que funcionou.

**Como confirmar.** O dispositivo inicia sem aviso amarelo e permanece assim após um novo boot.

**Se continuar.** Se os dois procedimentos falharem, o dano no registro é mais amplo que este dispositivo. Trate como recuperação do sistema, não como reparo de hardware.

---

### Código 22 — Dispositivo desativado no Windows

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 22` |
| **Nome interno** | `CM_PROB_DISABLED` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "This device is disabled. (Code 22)"

**O que significa.** A peça está fisicamente presente e com driver, mas alguém a desativou pelo Gerenciador de Dispositivos. A causa é sempre essa: o dispositivo foi desativado por quem operou o Gerenciador de Dispositivos.

**O que verificar**

1. Confirme no Gerenciador de Dispositivos que o ícone tem a seta para baixo, que indica item desativado — não o aviso amarelo de erro.

**Como corrigir**

1. Clique com o botão direito no dispositivo e escolha **Habilitar dispositivo**.
2. Pela linha de comando, como administrador: `pnputil /enable-device "<ID de instância>"` (disponível a partir do Windows 10, versão 2004).

**Como confirmar.** A seta some do ícone e o dispositivo volta a funcionar.

**Se continuar.** Se o dispositivo se desativar de novo sozinho, procure uma política de grupo ou um software de gerenciamento corporativo que esteja aplicando essa configuração. Não é falha de hardware.

---

### Código 24 — Dispositivo ausente, com defeito ou incompleto

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 24` |
| **Nome interno** | `CM_PROB_DEVICE_NOT_THERE` |
| **Risco da correção** | Médio |

**Mensagem do Windows**:

> "This device is not present, is not working properly, or does not have all its drivers installed. (Code 24)"

**O que significa.** O Windows tem um registro do dispositivo, mas não consegue confirmar que ele está presente e íntegro. **A causa pode ser hardware com defeito ou driver faltando**, e dispositivos preparados para remoção permanecem neste estado.

**O que verificar**

1. Verifique se a peça foi removida ou preparada para remoção (o caso de dispositivos que foram ejetados e não retirados).
2. Desligue o equipamento, retire da tomada, faça a descarga de energia residual conforme [Segurança e boas práticas](15-seguranca-e-boas-praticas.md) e reassente a peça e seus cabos.

**Como corrigir**

1. Reassente a peça e os cabos de dados e de energia.
2. Ligue e reinstale o driver a partir do pacote do fabricante.
3. Se a peça continuar ausente, teste-a em outro equipamento conhecidamente bom.

**Como confirmar.** O dispositivo aparece com o nome correto, sem aviso amarelo, e permanece assim após dois boots.

**Se continuar**

> [!IMPORTANT]
> O Código 24 **não distingue** peça com defeito de driver faltando — as duas possibilidades ficam em aberto, sem critério de desempate. Não conclua defeito físico sem antes ter testado a peça em outro equipamento. Se ela funcionar no outro, o problema está na porta, no cabo ou na placa-mãe de origem.

---

### Código 28 — Driver não instalado

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 28` |
| **Nome interno** | `CM_PROB_FAILED_INSTALL` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "The drivers for this device are not installed. (Code 28)"

**O que significa.** O Windows tentou instalar e não achou driver compatível. Os motivos internos mais comuns são: `STATUS_PNP_NO_COMPAT_DRIVERS` (nenhum driver compatível encontrado), dependência de pacote ausente e ausência de um driver de função associado no `.inf`. Há ainda um caso específico: o dispositivo funcionava antes de uma atualização do Windows e passou a mostrar Código 28 depois — porque o pacote do driver foi excluído da migração.

**O que verificar**

1. Anote o ID de hardware em **Propriedades › Detalhes › IDs de Hardware**.
2. Verifique se o problema começou logo depois de uma atualização de versão do Windows. Se sim, é o caso de migração descrito acima.

**Como corrigir**

1. A orientação é direta: obter o driver mais recente **no site do fabricante do dispositivo**.
2. Instale o pacote do fabricante e reinicie.
3. Se o pacote vier como `.inf` avulso, instale como administrador: `pnputil /add-driver <arquivo.inf> /install`

**Como confirmar.** O dispositivo passa a aparecer com o nome real e sem aviso amarelo.

**Se continuar.** Se o fabricante não publica driver para a sua versão do Windows, o limite é de compatibilidade, não de instalação. Confirme na página do produto quais versões são suportadas antes de concluir que a peça está com defeito.

---

### Código 29 — Dispositivo desativado no firmware (BIOS/UEFI)

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 29` |
| **Nome interno** | `CM_PROB_HARDWARE_DISABLED` |
| **Risco da correção** | Médio |

**Mensagem do Windows**:

> "This device is disabled because the firmware of the device did not give it the required resources. (Code 29)"

**O que significa.** O dispositivo está desligado no nível do firmware, antes do Windows. A resolução é objetiva: **habilitar o dispositivo no BIOS**.

**O que verificar**

1. Identifique qual é a peça. Os casos comuns são controladora SATA, áudio integrado, rede integrada, câmera, leitor de cartão e vídeo integrado.
2. Entre no BIOS/UEFI e localize a seção de dispositivos integrados ou periféricos.

**Como corrigir**

1. Habilite o dispositivo no BIOS/UEFI e salve.
2. Se você não encontrar a opção, consulte o manual da placa-mãe ou do equipamento — o nome do item varia por fabricante.

**Como confirmar.** Depois do boot, o dispositivo aparece no Gerenciador de Dispositivos sem o Código 29.

**Se continuar**

> [!CAUTION]
> Não restaure os padrões do BIOS para tentar resolver isso sem antes anotar as configurações atuais. Em equipamentos com inicialização segura, RAID ou criptografia de disco, restaurar padrões pode deixar o sistema sem iniciar. Veja [Segurança e boas práticas](15-seguranca-e-boas-praticas.md).

---

### Código 31 — O Windows não conseguiu carregar os drivers exigidos

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 31` |
| **Nome interno** | `CM_PROB_FAILED_ADD` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "This device is not working properly because Windows cannot load the drivers required for this device. (Code 31)"

**O que significa.** O driver de função do dispositivo retornou erro na rotina `AddDevice`, ou seja, ele foi carregado mas recusou assumir a peça. A ação indicada é atualizar o driver.

**O que verificar**

1. Verifique se o driver instalado é o da versão correta do Windows e da arquitetura correta (64 bits).

**Como corrigir**

1. Atualize o driver do dispositivo pelo pacote do fabricante.
2. Se o problema apareceu depois de uma atualização de driver, use **Propriedades › Driver › Reverter driver** para voltar à versão anterior.

**Como confirmar.** O dispositivo funciona e o aviso amarelo desaparece.

**Se continuar.** Se as duas versões de driver falharem igual, o defeito pode estar na peça. Teste em outro equipamento antes de trocar.

---

### Código 32 — O serviço do driver está desabilitado

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 32` |
| **Nome interno** | `CM_PROB_DISABLED_SERVICE` |
| **Risco da correção** | Alto |

**Mensagem do Windows**:

> "A driver (service) for this device has been disabled. An alternate driver may be providing this functionality. (Code 32)"

**O que significa.** O serviço que carrega este driver está com o tipo de inicialização definido como **Desabilitado** no registro. Outro driver pode estar fornecendo a mesma funcionalidade — ou seja, nem sempre há problema real a corrigir.

> [!CAUTION]
> Procedimento de risco **Alto** nesta escala: ele altera registro, serviço do sistema ou proteção de segurança. Leia [Escala de risco deste documento](#escala-de-risco-deste-documento) e a seção *Se continuar* antes de executar.

**O que verificar**

1. Confirme se a funcionalidade está realmente indisponível. Se a peça funciona por outro driver, o Código 32 é informativo.
2. Verifique se algum software de segurança ou otimização desabilitou o serviço.

**Como corrigir**

1. A orientação é condicional: **se o driver for realmente necessário, altere o tipo de inicialização** do serviço.
2. Reinstale o driver pelo pacote do fabricante — a instalação normalmente restaura o tipo de inicialização correto.

**Como confirmar.** A funcionalidade volta e o Código 32 não reaparece após um boot.

**Se continuar**

> [!WARNING]
> Não altere o tipo de inicialização de um serviço de driver sem saber qual é. Serviços de armazenamento definidos incorretamente impedem o Windows de iniciar. Prefira reinstalar o driver a editar o registro.

---

### Código 37 — O Windows não conseguiu inicializar o driver

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 37` |
| **Nome interno** | `CM_PROB_FAILED_DRIVER_ENTRY` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "Windows cannot initialize the device driver for this hardware. (Code 37)"

**O que significa.** O driver retornou falha na própria rotina de entrada (`DriverEntry`) — ele nem chegou a assumir o dispositivo. A resolução indicada é reinstalar ou obter um driver novo.

**O que verificar**

1. Verifique se o driver é compatível com a versão e a arquitetura do Windows instaladas.

**Como corrigir**

1. Desinstale o driver e instale a versão publicada pelo fabricante para a sua versão do Windows.
2. Reinicie após a instalação.

**Como confirmar.** O dispositivo inicia sem aviso amarelo.

**Se continuar.** Se persistir com o driver oficial mais recente, registre o caso junto ao fabricante do dispositivo: a falha está no driver, não na configuração.

---

### Código 39 — Driver corrompido ou ausente

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 39` |
| **Nome interno** | `CM_PROB_DRIVER_FAILED_LOAD` |
| **Risco da correção** | Médio |

**Mensagem do Windows**:

> "Windows cannot load the device driver for this hardware. The driver may be corrupted or missing. (Code 39)"

**O que significa.** O arquivo do driver não pôde ser carregado. As causas mais comuns são: driver que depende de outro binário ausente no sistema; driver que usa uma API não existente na versão do Windows em uso; driver incompatível com a **Integridade de código protegida por hipervisor (HVCI)** quando esse recurso está ativo; e falha de leitura do arquivo por corrupção ou erro de E/S.

**O que verificar**

1. Verifique se o recurso **Integridade de memória** (Segurança do Windows › Segurança do dispositivo › Isolamento do núcleo) está ativo. HVCI é causa direta deste código.
2. Verifique se o disco do sistema apresenta erros: falha de E/S no arquivo é uma das causas.

**Como corrigir**

1. Reinstale o driver a partir do pacote do fabricante, ou obtenha uma versão mais nova.
2. Se o driver for antigo e a Integridade de memória estiver ativa, procure a versão compatível com HVCI junto ao fabricante.

**Como confirmar.** O dispositivo carrega e permanece funcionando após um novo boot.

**Se continuar**

> [!CAUTION]
> Desativar a Integridade de memória faz o driver antigo carregar, mas **reduz a proteção do sistema**. É uma medida de contorno, não uma correção. Prefira o driver compatível. Se o disco estiver com erro de leitura, o Código 39 é sintoma: vá para [Disco não reconhecido](10-cenarios/disco-nao-reconhecido.md) e [Victoria](14-ferramentas/victoria.md).

---

### Código 43 — O driver relatou falha do dispositivo

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 43` |
| **Nome interno** | `CM_PROB_FAILED_POST_START` |
| **Risco da correção** | Médio |

**Mensagem do Windows**:

> "Windows has stopped this device because it has reported problems. (Code 43)"

**O que significa.** Um dos drivers que controlam a peça informou ao Windows que ela falhou. O mecanismo é este: a pilha do dispositivo respondeu `PNP_DEVICE_FAILED`. A resolução indicada é **desinstalar e reinstalar o dispositivo**.

**O que verificar**

1. Anote se o código aparece sempre ou de forma intermitente. O Código 43 intermitente em GPU e em dispositivos USB costuma acompanhar problema de alimentação ou de temperatura.
2. Verifique a alimentação da peça: no caso de placa de vídeo, os conectores PCIe auxiliares; no caso de USB, se o dispositivo é alimentado pela porta.

**Como corrigir**

1. Desinstale o dispositivo no Gerenciador de Dispositivos e use **Ação › Verificar se há alterações de hardware**.
2. Desligue, faça a descarga de energia residual e reassente a peça e seus cabos de alimentação.
3. Reinstale o driver do fabricante.

**Como confirmar.** O dispositivo funciona e o Código 43 não reaparece durante o tempo de observação previsto em [Validação final](13-validacao-final.md).

**Se continuar.** O Código 43 diz que o dispositivo **relatou** falha — não diz qual. Se voltar depois de driver novo e peça reassentada, trate como falha física da peça e siga [Diagnóstico por camada](08-diagnostico-por-camada.md). Em GPU, confira também [Superaquecimento](10-cenarios/superaquecimento.md) antes de condenar a placa.

---

### Código 45 — Dispositivo não conectado no momento

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 45` |
| **Nome interno** | `CM_PROB_PHANTOM` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "Currently, this hardware device is not connected to the computer. (Code 45)"
>
> "To fix this problem, reconnect this hardware device to the computer."

**O que significa.** É o registro de um dispositivo que já esteve conectado e agora não está. **Não há resolução a aplicar**, e este código só deve aparecer quando a variável de ambiente `DEVMGR_SHOW_NONPRESENT_DEVICES` está definida — isto é, quando o Gerenciador de Dispositivos foi configurado para mostrar dispositivos ausentes.

**O que verificar**

1. Confirme se o Gerenciador de Dispositivos está com **Exibir › Mostrar dispositivos ocultos** ativo. Se estiver, o Código 45 é esperado e não indica defeito.

**Como corrigir**

1. Se você precisa do dispositivo: reconecte-o, como diz a própria mensagem.
2. Se o dispositivo foi removido de propósito: não há o que corrigir. O registro pode permanecer.

**Como confirmar.** Ao reconectar, o dispositivo sai do estado 45 e passa a operar normalmente.

**Se continuar.** Se um dispositivo que **está** fisicamente conectado aparece com Código 45, o problema é de detecção da porta ou do cabo, não do dispositivo. Teste em outra porta e com outro cabo.

---

### Código 48 — Driver bloqueado por incompatibilidade conhecida

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 48` |
| **Nome interno** | `CM_PROB_DRIVER_BLOCKED` |
| **Risco da correção** | Baixo |

**Mensagem do Windows**:

> "The software for this device has been blocked from starting because it is known to have problems with Windows. Contact the hardware vendor for a new driver. (Code 48)"

**O que significa.** O Windows recusou carregar este driver porque ele consta da **base de proteção de drivers fornecida pelo Windows Update**. Há ainda um segundo caso: em equipamentos com **Segurança de Entrada Aprimorada**, o driver instalado foi considerado incompatível com os requisitos desse recurso e por isso o dispositivo foi impedido de iniciar.

**O que verificar**

1. Anote a versão do driver instalado em **Propriedades › Driver**. É a versão que está bloqueada.
2. Verifique se o equipamento usa Windows Hello com Segurança de Entrada Aprimorada — nesse caso o bloqueio pode ser desse mecanismo, não da base do Windows Update.

**Como corrigir**

1. A resolução é uma só: **obter um driver novo junto ao fabricante do hardware**.
2. Instale a versão mais recente publicada pelo fabricante e reinicie.

**Como confirmar.** O dispositivo inicia e o Código 48 não reaparece.

**Se continuar**

> [!WARNING]
> Não tente contornar o bloqueio instalando o driver antigo à força. O driver está na lista porque causa problemas conhecidos no Windows. Se o fabricante não publicou versão compatível, a peça está sem suporte para esta versão do Windows — essa é a conclusão, não um defeito de hardware.

---

### Código 52 — Assinatura digital do driver não pôde ser verificada

| Atributo | Valor |
| --- | --- |
| **Código** | `Code 52` |
| **Nome interno** | `CM_PROB_UNSIGNED_DRIVER` |
| **Risco da correção** | Alto |

**Mensagem do Windows**:

> "Windows cannot verify the digital signature for the drivers required for this device. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source. (Code 52)"

**O que significa.** Em Windows de 64 bits, o dispositivo não iniciou porque o driver não tem assinatura digital válida. O driver não está em conformidade com a política de assinatura de código em modo kernel, e **para o usuário final a única forma de evitar o erro é obter e instalar um driver assinado digitalmente**.

> [!CAUTION]
> Procedimento de risco **Alto** nesta escala: ele altera registro, serviço do sistema ou proteção de segurança. Leia [Escala de risco deste documento](#escala-de-risco-deste-documento) e a seção *Se continuar* antes de executar.

**O que verificar**

1. Verifique de onde veio o driver instalado. Drivers baixados de sites agregadores costumam ser a origem deste código.
2. Confirme a assinatura em **Propriedades › Driver › Detalhes do driver**.

**Como corrigir**

1. Desinstale o driver não assinado.
2. Instale o driver assinado publicado pelo fabricante do equipamento ou do componente.

**Como confirmar.** O dispositivo inicia sem o Código 52 e o driver aparece com fornecedor identificado.

**Se continuar**

> [!CAUTION]
> Existem formas de fazer o Windows carregar driver não assinado, mas elas são recurso de **desenvolvimento e teste**, não de produção. Usá-las em equipamento de cliente desliga uma proteção contra driver malicioso. Se não há driver assinado, a peça está sem suporte — trate como fim de vida útil, não como problema a contornar.

---

## Próximos passos

| Se você… | Vá para |
| --- | --- |
| concluiu que a peça está com defeito | [Diagnóstico por camada](08-diagnostico-por-camada.md) — o que testar em cada subsistema |
| ainda não chegou a carregar o Windows | [Catálogo de códigos POST](09-codigos-post/00-indice-codigos.md) |
| tem um sintoma, não um dispositivo específico | [Cenários de falha](10-cenarios/00-indice-cenarios.md) |
| aplicou a correção e precisa fechar o atendimento | [Validação final por componente](13-validacao-final.md) |

---

| Atributo | Valor |
| --- | --- |
| **Autoria** | Edsilas |
| **Versão da documentação** | `doc-3.0.0` |
