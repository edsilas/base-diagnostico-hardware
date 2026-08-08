#!/usr/bin/env python3
"""Regera a documentação da Base de Diagnóstico de Hardware a partir das planilhas.

A fonte da verdade são os dois arquivos `.xlsx`. Este script os lê e reconstrói os
documentos derivados em `docs/`, transcrevendo o conteúdo das células sem redação
intermediária — é o que garante que nenhuma paráfrase acidental entre na base.

Requisito:
    pip install openpyxl

Uso:
    python tools/gerar_documentacao.py                        # fontes em ./fontes, saída em .
    python tools/gerar_documentacao.py --fontes ~/planilhas   # outra origem
    python tools/gerar_documentacao.py --saida /tmp/teste     # gerar sem tocar no repositório
    python tools/gerar_documentacao.py --listar               # só mostra o que seria gerado

Arquivos esperados em `--fontes`:
    HW_HARDWARE_CODIGOS_DE_ERROS.xlsx
    HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx

Depois de gerar, valide:
    python tools/validar_documentacao.py

Autoria: Edsilas.
"""
from __future__ import annotations

import argparse
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
GERADOR = os.path.join(AQUI, "gerador")

FONTES_ESPERADAS = [
    "HW_HARDWARE_CODIGOS_DE_ERROS.xlsx",
    "HW_HARDWARE_FLUXO_DIAGNOSTICO.xlsx",
]

# Ordem importa: os índices e as referências dependem do que veio antes.
ETAPAS = [
    ("gen1_codigos.py", "Catálogo de códigos de POST — docs/09-codigos-post/"),
    ("gen2_cenarios.py", "Fichas de cenário — docs/10-cenarios/"),
    ("gen3_fluxos.py", "Fluxos, camadas, ambiguidades, correlações e validação"),
    ("gen4_ferramentas.py", "Guias de ferramentas — docs/14-ferramentas/"),
    ("gen5a_estrutura.py", "Taxonomia de camadas e requisitos"),
    ("gen5b_entrada.py", "Visão geral, arquitetura e utilização"),
    ("gen5c_final.py", "README e índice geral"),
    ("gen5d_refs.py", "Limitações e FAQ"),
    ("gen5e_glossario.py", "Glossário"),
    ("gen8_indices.py", "Índices cruzados e referência de comandos"),
    ("gen6_references.py", "Fontes e matriz de rastreabilidade"),
    ("gen7_pendencias.py", "Pendências e changelog"),
    ("gen9_sumarios.py", "Sumários 'Neste documento'"),
]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--fontes", default="./fontes",
                   help="diretório com as planilhas (padrão: ./fontes)")
    p.add_argument("--saida", default=".",
                   help="raiz onde docs/ e README.md serão escritos (padrão: .)")
    p.add_argument("--listar", action="store_true",
                   help="apenas listar as etapas, sem gerar")
    args = p.parse_args()

    if args.listar:
        print("Etapas de geração, nesta ordem:\n")
        for i, (mod, desc) in enumerate(ETAPAS, 1):
            print(f"  {i:2}. {mod:24} {desc}")
        return 0

    fontes = os.path.abspath(args.fontes)
    saida = os.path.abspath(args.saida)

    faltando = [f for f in FONTES_ESPERADAS if not os.path.isfile(os.path.join(fontes, f))]
    if faltando:
        print(f"ERRO: planilha(s) não encontrada(s) em {fontes}:", file=sys.stderr)
        for f in faltando:
            print(f"  - {f}", file=sys.stderr)
        print("\nUse --fontes para apontar o diretório correto.", file=sys.stderr)
        return 1

    try:
        import openpyxl  # noqa: F401
    except ImportError:
        print("ERRO: openpyxl não instalado.  pip install openpyxl", file=sys.stderr)
        return 1

    os.environ["BDH_FONTES"] = fontes
    os.environ["BDH_SAIDA"] = saida
    sys.path.insert(0, GERADOR)
    os.makedirs(os.path.join(saida, "docs"), exist_ok=True)

    print(f"Fontes ... {fontes}")
    print(f"Saída .... {saida}\n")

    for i, (mod, desc) in enumerate(ETAPAS, 1):
        caminho = os.path.join(GERADOR, mod)
        if not os.path.isfile(caminho):
            print(f"ERRO: módulo ausente: {caminho}", file=sys.stderr)
            return 1
        print(f"[{i:2}/{len(ETAPAS)}] {desc}")
        try:
            runpy.run_path(caminho, run_name="__main__")
        except Exception as exc:  # noqa: BLE001
            print(f"\nERRO na etapa {mod}: {exc}", file=sys.stderr)
            return 1

    print("\nDocumentação regerada.")
    print("Próximo passo:  python tools/validar_documentacao.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
