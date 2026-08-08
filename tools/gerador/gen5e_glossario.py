import os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = os.environ.get("BDH_SAIDA", ".").rstrip("/") + "/docs"
cod = read(F_COD)
flu = read(F_FLU)

# =========================================================================
# 17 — Glossário
# =========================================================================
TERMOS = [
    ("5VSB (standby 5 V)",
     "Tensão de standby presente no conector ATX de 24 pinos com o cabo AC conectado, mesmo com o "
     "equipamento desligado. A fonte localiza a medição no pino 9, fio roxo, e define 5,0 V ±5% como "
     "valor esperado. Sua ausência é o primeiro indicador de fonte morta ou cabo AC com problema.",
     "Confirmado", "08-diagnostico-por-camada.md, 10-cenarios/nao-liga.md"),
    ("BDS (Boot Device Selection)",
     "Fase do POST em que o firmware seleciona o dispositivo de boot. Expansão fornecida pela "
     "própria fonte no campo `FASE POST`.", "Confirmado", "09-codigos-post/"),
    ("BIST",
     "Teste embutido citado como primeiro passo recomendado pela Dell para verificar a fonte. A "
     "fonte também registra um BIST de tela acionado por 'D' + Power. A expansão da sigla não é "
     "fornecida.", "Confirmado (uso) / Não confirmado (expansão)", "09-codigos-post/dell.md"),
    ("Boot mínimo (minimal boot)",
     "Configuração reduzida para isolar a falha. **A composição diverge entre as fontes**: "
     "'CPU + 1 RAM + fonte', 'CPU + RAM + Vídeo apenas' e 'CPU + Cooler + 1 RAM + PSU apenas'.",
     "Necessita validação", "06-fluxo-post.md, 07-fluxo-sistemico.md"),
    ("Camada",
     "Agrupamento de subsistemas usado para localizar a origem de uma falha. **Existem dois modelos "
     "de numeração incompatíveis** entre os arquivos-fonte.",
     "Necessita validação", "03-taxonomia-camadas.md"),
    ("CH341A",
     "Programadora de EPROM citada para regravação física do chip de BIOS, usada com clamp SOIC-8 e "
     "software de gravação (a fonte cita flashrom e AsProgrammer).",
     "Confirmado", "08-diagnostico-por-camada.md"),
    ("Debug LED",
     "LEDs de diagnóstico presentes em placas-mãe, que a fonte descreve seguindo a sequência "
     "CPU → DRAM → VGA → BOOT. O LED em que a sequência trava indica a camada com problema.",
     "Confirmado", "06-fluxo-post.md, 09-codigos-post/generico-debug-led.md"),
    ("DDU (Display Driver Uninstaller)",
     "Utilitário citado para remoção completa de driver de vídeo em Modo de Segurança, antes de "
     "instalar driver limpo. Expansão fornecida pela fonte.",
     "Confirmado", "12-correlacoes.md"),
    ("IMC (Integrated Memory Controller)",
     "Controladora de memória integrada à CPU. A fonte a aponta como suspeita quando módulos "
     "*known-good* falham em todos os slots. Expansão fornecida pela fonte.",
     "Confirmado", "12-correlacoes.md, 10-cenarios/"),
    ("Kernel-Power 41",
     "Evento do Visualizador de Eventos do Windows usado pela fonte como evidência de reinício sem "
     "desligamento limpo. O critério PASS de fonte exige zero ocorrências.",
     "Confirmado", "13-validacao-final.md, 10-cenarios/reinicializacao-aleatoria.md"),
    ("Known-good",
     "Componente comprovadamente funcional, usado como referência em teste cruzado. A fonte exige "
     "que o substituto tenha a mesma especificação (frequência, CL, tensão).",
     "Confirmado", "06-fluxo-post.md, 09-codigos-post/"),
    ("PCH (Platform Controller Hub)",
     "Chipset da placa-mãe. Expansão fornecida pela fonte na descrição da camada de chipset.",
     "Confirmado", "08-diagnostico-por-camada.md"),
    ("Pass (MemTest86)",
     "Ciclo completo da bateria de testes. A fonte registra que a bateria padrão executa 13 "
     "algoritmos e que o critério de aprovação é zero erro em **4 passes**.",
     "Confirmado (critério) / Inferido (equivalência 1 pass = 1 bateria completa)",
     "14-ferramentas/memtest86.md"),
    ("Power drain",
     "Descarga dos capacitores residuais antes de manipular componentes. **A duração diverge entre "
     "as fontes**: 30 s em um arquivo, 10 s no outro.",
     "Necessita validação", "09-codigos-post/, 10-cenarios/nao-liga.md"),
    ("PROCHOT",
     "Proteção térmica que, segundo a fonte, em caso extremo provoca desligamento abrupto "
     "indistinguível de falha de fonte.", "Confirmado", "12-correlacoes.md"),
    ("Q-Code",
     "Código hexadecimal de dois dígitos exibido em display na placa-mãe. A fonte distingue código "
     "**fixo** (travamento — consultar a ficha) de código **progredindo** (POST em andamento).",
     "Confirmado", "06-fluxo-post.md, 09-codigos-post/ami-q-code.md"),
    ("QVL (Qualified Vendor List)",
     "Lista de módulos de memória homologados pelo fabricante da placa-mãe. Expansão fornecida pela "
     "fonte.", "Confirmado", "08-diagnostico-por-camada.md"),
    ("Remap",
     "Ação que força a controladora do disco a remapear blocos defeituosos para a área de reserva. "
     "A fonte a associa ao atributo S.M.A.R.T. C5.",
     "Confirmado", "14-ferramentas/victoria.md"),
    ("Reseat",
     "Reencaixe do componente no slot, com pressão uniforme. Aparece como primeiro procedimento em "
     "falhas de memória e de vídeo.", "Confirmado", "08-diagnostico-por-camada.md"),
    ("Ripple",
     "Ondulação residual na saída da fonte. A fonte define tolerância de 120 mV pico a pico na linha "
     "+12 V e indica osciloscópio para a medição.",
     "Confirmado", "08-diagnostico-por-camada.md"),
    ("S.M.A.R.T. — IDs 05, C5 e C6",
     "Atributos críticos de saúde do disco. A fonte os identifica como ID 05 (*Reallocated "
     "Sectors*), C5 (*Current Pending*) e C6 (*Uncorrectable*), e exige valor zero nos três como "
     "critério de aprovação.",
     "Confirmado", "13-validacao-final.md, 07-fluxo-sistemico.md, 10-cenarios/bsod.md"),
    ("ACPI (Advanced Configuration and Power Interface)",
     "Conjunto de tabelas de firmware que descrevem o hardware ao sistema operacional. A fonte "
     "registra que erros de ACPI levam a falhas de suspensão/hibernação e à tela azul "
     "DRIVER_POWER_STATE_FAILURE, e que atualizar a BIOS costuma corrigir tabelas corrompidas.",
     "Confirmado", "14-ferramentas/aida64-etapas-16-30.md, 12-correlacoes.md"),
    ("BDA (BIOS Data Area) e IVT (Interrupt Vector Table)",
     "Estruturas alojadas nos primeiros 64 KB de memória. A fonte explica que essa região é crítica "
     "justamente por contê-las, o que torna sua falha impeditiva do POST.",
     "Confirmado", "09-codigos-post/ami-legacy.md"),
    ("DXE (Driver Execution Environment)",
     "Fase do POST em que os drivers do firmware são executados. A fonte registra que travamento "
     "nessa fase indica que a CPU começou a executar mas não concluiu. Expansão fornecida pela "
     "fonte.", "Confirmado", "09-codigos-post/ami-q-code.md"),
    ("G-List (Growth Defect List)",
     "Área de reserva do disco para onde o comando de Remap move endereços LBA defeituosos. A fonte "
     "registra que, quando a G-List lota, o disco deixa de aceitar novos remapeamentos.",
     "Confirmado", "14-ferramentas/victoria.md"),
    ("GOP (Graphics Output Protocol)",
     "Protocolo de saída de vídeo em ambiente UEFI. A fonte o cita como causa de tela preta ao "
     "tentar iniciar o MemTest86 em placas incompatíveis.",
     "Confirmado", "14-ferramentas/memtest86.md"),
    ("HMM (Hardware Maintenance Manual)",
     "Manual de manutenção do fabricante. A fonte o indica, junto ao Lenovo PSREF, como consulta "
     "final quando o procedimento documentado não resolve.",
     "Confirmado", "09-codigos-post/lenovo.md"),
    ("KBC (Keyboard Controller)",
     "Controlador de teclado. A fonte registra que ele comanda o Gate A20 e que, em sistemas "
     "legados, era responsável por habilitar a linha de endereço correspondente — daí falhas de "
     "teclado bloquearem o POST.",
     "Confirmado", "09-codigos-post/ami-legacy.md"),
    ("ME (Management Engine)",
     "Firmware listado pela fonte entre os componentes da camada de firmware, ao lado do SPI Flash, "
     "da EEPROM, da NVRAM do CMOS, das Option ROMs e dos patches de microcode.",
     "Confirmado", "08-diagnostico-por-camada.md"),
    ("OCP (Over Current Protection) e OPP",
     "Proteções da fonte de alimentação. A fonte registra o disparo de OCP/OPP como causa de a PSU "
     "não sustentar carga de pico, e o desarme por OCP como erro possível durante stress test. "
     "A expansão de OPP não é fornecida.",
     "Confirmado (OCP) / Não confirmado (expansão de OPP)",
     "10-cenarios/reinicializacao-aleatoria.md, 14-ferramentas/aida64-etapas-01-15.md"),
    ("Row Hammer",
     "Falha em que o acesso repetido a uma linha de memória faz a carga elétrica vazar para a linha "
     "vizinha e inverter um bit. A fonte a verifica pelo Teste 13 do MemTest86 e registra que "
     "módulos DDR3/DDR4 antigos costumam não ter proteção.",
     "Confirmado", "14-ferramentas/memtest86.md"),
    ("SmartBeep",
     "Sinal sonoro em forma de melodia usado por equipamentos Lenovo, interpretável pelo aplicativo "
     "Lenovo PC Diagnostics.", "Confirmado", "09-codigos-post/lenovo.md"),
    ("SPD (Serial Presence Detect)",
     "Chip do módulo de memória que guarda as temporizações. A fonte o cita como origem de "
     "incompatibilidade com a controladora e indica o AIDA64 para ler seus dados brutos. Expansão "
     "fornecida pela fonte.",
     "Confirmado", "09-codigos-post/, 14-ferramentas/aida64-etapas-01-15.md"),
    ("TPM (Trusted Platform Module)",
     "Chip de segurança. A fonte registra seu uso em ThinkPads para criptografia BitLocker e "
     "autenticação, lista as causas de falha (firmware corrompido, desabilitação incorreta, defeito "
     "físico, reset após atualização de BIOS) e define o critério de validação: TPM reconhecido no "
     "BIOS e `tpm.msc` reportando o chip pronto.",
     "Confirmado", "09-codigos-post/lenovo.md, 14-ferramentas/aida64-etapas-16-30.md"),
    ("TDR (Timeout Detection and Recovery)",
     "Mecanismo cujo disparo reinicia o driver de vídeo, podendo gerar tela azul. A fonte o usa como "
     "indicador de problema de driver, não de hardware. Expansão fornecida pela fonte.",
     "Confirmado", "12-correlacoes.md"),
    ("Teste cruzado",
     "Instalação do componente suspeito em outro sistema. A fonte define o critério de decisão: "
     "falha em dois sistemas condena o componente; funcionamento em outro sistema condena a "
     "placa-mãe.", "Confirmado", "06-fluxo-post.md"),
    ("Teste paperclip",
     "Acionamento da fonte fora da placa-mãe, curto-circuitando PS_ON (pino 16, fio verde) ao COM "
     "(pino 17, fio preto) do conector de 24 pinos.",
     "Confirmado", "10-cenarios/nao-liga.md"),
    ("TjMax",
     "Temperatura máxima de junção do processador. A fonte cita a faixa 100–105 °C ao descrever o "
     "sintoma de superaquecimento.", "Confirmado", "10-cenarios/superaquecimento.md"),
    ("Vdrop / voltage droop",
     "Queda de tensão sob carga. A fonte a associa à proteção OCP/OPP da fonte e ao VRM que não "
     "sustenta a carga da CPU.", "Confirmado", "10-cenarios/, 12-correlacoes.md"),
    ("Wear Level",
     "Indicador de desgaste de SSD lido via S.M.A.R.T. O critério FAIL registrado é acima de 90 %; "
     "o indicador de sucesso é abaixo de 80 %.", "Confirmado", "13-validacao-final.md"),
    ("WinDbg (Windows Debugging Tools)",
     "Depurador usado pela fonte para analisar o minidump gerado por uma tela azul. O comando "
     "registrado é `!analyze -v`, para identificar o driver em falha. Expansão fornecida pela "
     "fonte.", "Confirmado", "10-cenarios/bsod.md, 19-comandos.md"),
    ("WinPE",
     "Ambiente de execução independente do Windows instalado, recomendado pela fonte para rodar o "
     "Victoria sem interferência do sistema hospedeiro (a fonte cita Sergei Strelec como exemplo).",
     "Confirmado", "14-ferramentas/victoria.md"),
    ("XMP / EXPO / DOCP",
     "Perfis de desempenho de memória. A fonte exige que o perfil esteja ativo durante o teste com "
     "MemTest86, para não mascarar instabilidade. As expansões das siglas não são fornecidas.",
     "Confirmado (uso) / Não confirmado (expansão)", "14-ferramentas/memtest86.md"),
]

t = doc_header(
    "Glossário",
    "Ambos os arquivos-fonte",
    "Termos técnicos efetivamente usados no material, definidos a partir do que as fontes dizem "
    "sobre eles. Termos que a fonte usa sem definir estão marcados como tal.",
    "Definição, nível de confiança e documento onde o termo é aplicado.",
    "Termos genéricos de informática sem relação com os procedimentos documentados; expansões de "
    "siglas que a fonte não fornece.",
    [
        "[Índice da documentação](00-indice.md)",
        "[Taxonomia de camadas](03-taxonomia-camadas.md)",
        "[Limitações](15-limitacoes.md)",
    ],
    secao="referencia", nivel=0,
    resumo="43 termos técnicos usados no material, definidos pelo que as fontes dizem sobre eles.",
    aplica_se="Leitura de qualquer documento desta base",
)

t += """> **Critério de inclusão.** Só entram termos que aparecem nas fontes e cuja definição pode ser
> sustentada pelo que elas dizem. Onde a fonte usa a sigla sem expandi-la, isso está registrado no
> nível de confiança em vez de completado por conhecimento externo.

"""
for termo, definicao, conf, onde in TERMOS:
    t += f"## {termo}\n\n{definicao}\n\n"
    t += f"**Nível de confiança:** {conf}  \n**Aplicado em:** {onde}\n\n---\n\n"

t += """## Siglas de fase do POST

A fonte usa `SEC`, `PEI`, `DXE` e `BDS` no campo `FASE POST`, sempre nesta ordem de execução.

| Sigla | Expansão | Situação na fonte |
| --- | --- | --- |
| SEC | — | Usada sem expansão |
| PEI | — | Usada sem expansão; aparece sempre qualificada (`PEI (Memory Training)`, `SEC/PEI (CPU Init)`) |
| DXE | Driver Execution Environment | **Expandida pela fonte** |
| BDS | Boot Device Selection | **Expandida pela fonte** |

**Nível de confiança:** Confirmado (uso das quatro e expansão de DXE e BDS) / Não confirmado
(expansão de SEC e PEI).

## Termos usados sem definição na fonte

Registrados aqui para que a ausência fique explícita, em vez de ser preenchida por conhecimento
externo:

| Termo | Como a fonte o usa |
| --- | --- |
| BIST | Teste embutido; a fonte descreve dois usos (botão na traseira da PSU Dell e teste de tela com `D` + Power), sem expandir a sigla |
| XMP / EXPO / DOCP | Perfis de desempenho de memória; a fonte os trata como equivalentes entre fabricantes, sem expandir |
| SEC, PEI | Fases do POST; ver tabela acima |
| OPP | Proteção da PSU citada ao lado da OCP |
| QVL | Expandida (*Qualified Vendor List*), mas a fonte não descreve como obtê-la além de "site do fabricante" |
| PSREF | Citado como base de consulta Lenovo, sem expansão |
"""
t += doc_footer("Ambos os arquivos-fonte",
                conf="Confirmado para os termos definidos pela fonte; lacunas sinalizadas por termo",
                proximos=[
                    ("o termo era um número de camada",
                     "[Taxonomia de camadas](03-taxonomia-camadas.md)"),
                    ("o termo era uma ferramenta",
                     "[Guias de ferramentas](14-ferramentas/00-indice-ferramentas.md)"),
                    ("o termo não está aqui", "[Limitações](15-limitacoes.md)"),
                ])
open(f"{OUT}/17-glossario.md", "w").write(t)
print("17 gerado")
