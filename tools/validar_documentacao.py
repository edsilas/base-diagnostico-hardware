#!/usr/bin/env python3
"""Validador da base de conhecimento.

Verifica, sem acesso à rede e sem dependências externas:

  1. links internos apontando para arquivos inexistentes;
  2. âncoras (`arquivo.md#secao`) que não correspondem a nenhum título;
  3. links absolutos para arquivos do próprio repositório;
  4. documentos sem os cabeçalhos de contexto obrigatórios;
  5. documentos sem rodapé de fonte;
  6. documentos órfãos (não referenciados por nenhum outro);
  7. documentos sem trilha de navegação de volta ao README;
  8. documentos sem a seção "Próximos passos";
  9. sumário "Neste documento" não preenchido;
 10. blocos ```mermaid``` desbalanceados;
 11. títulos de nível 2 duplicados no mesmo arquivo (âncora ambígua).

Uso:
    python tools/validar_documentacao.py            # a partir da raiz do repositório
    python tools/validar_documentacao.py --caminho .

Código de saída:
    0  nenhum erro (avisos não reprovam)
    1  pelo menos um erro
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

SECOES_OBRIGATORIAS = [
    "## Contexto",
    "## Escopo",
    "## Fora do escopo",
    "## Relação com outros documentos",
]
RODAPE_FONTE = "**Fonte primária deste documento**"
TRILHA = "[Início]("
PROXIMOS = "## Próximos passos"
SUMARIO_VAZIO = "<!-- SUMARIO -->"
SUMARIO_TITULO = "## Neste documento"
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
BLOCO_CODIGO = re.compile(r"```.*?```", re.S)

# Arquivos isentos das seções de contexto e do rodapé de fonte.
ISENTOS = {"README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md"}


def ancoras(caminho: str) -> set[str]:
    """Reproduz a regra de geração de âncoras do GitHub."""
    vistos: collections.Counter[str] = collections.Counter()
    saida: set[str] = set()
    with open(caminho, encoding="utf-8") as fh:
        dentro_de_codigo = False
        for linha in fh:
            if linha.lstrip().startswith("```"):
                dentro_de_codigo = not dentro_de_codigo
                continue
            if dentro_de_codigo:
                continue
            m = TITULO.match(linha)
            if not m:
                continue
            texto = m.group(2)
            texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)  # links
            # Remove marcação de ênfase. O underscore NÃO é removido: em GFM ele não
            # forma ênfase dentro de palavra (MEMORY_MANAGEMENT), e o GitHub o preserva
            # na âncora.
            texto = re.sub(r"[*`~]", "", texto)
            base = re.sub(r"[^\w\- ]", "", texto.strip().lower(), flags=re.UNICODE)
            base = base.replace(" ", "-")
            vistos[base] += 1
            saida.add(base if vistos[base] == 1 else f"{base}-{vistos[base] - 1}")
            saida.add(base)
    return saida


def coletar(raiz: str) -> list[str]:
    encontrados = []
    for dirpath, dirnames, filenames in os.walk(raiz):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", ".github"}]
        for nome in filenames:
            if nome.endswith(".md"):
                encontrados.append(os.path.join(dirpath, nome))
    return sorted(encontrados)


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida a base de conhecimento.")
    parser.add_argument("--caminho", default=".", help="raiz do repositório (padrão: .)")
    args = parser.parse_args()
    raiz = os.path.abspath(args.caminho)

    arquivos = coletar(raiz)
    if not arquivos:
        print(f"Nenhum arquivo .md encontrado em {raiz}", file=sys.stderr)
        return 1

    mapa_ancoras = {p: ancoras(p) for p in arquivos}
    erros: list[str] = []
    avisos: list[str] = []
    referenciados: set[str] = set()
    total_links = 0

    for caminho in arquivos:
        rel = os.path.relpath(caminho, raiz)
        base = os.path.dirname(caminho)
        texto = open(caminho, encoding="utf-8").read()
        texto_util = BLOCO_CODIGO.sub("", texto)

        for _, alvo in LINK.findall(texto_util):
            if alvo.startswith(("http://", "https://", "mailto:", "#")):
                if alvo.startswith("#"):
                    total_links += 1
                    if alvo[1:] not in mapa_ancoras[caminho]:
                        erros.append(f"âncora inexistente  {rel} -> {alvo}")
                continue
            total_links += 1
            if alvo.startswith("/"):
                erros.append(f"link absoluto       {rel} -> {alvo}")
                continue
            arquivo, _, anc = alvo.partition("#")
            destino = os.path.normpath(os.path.join(base, arquivo)) if arquivo else caminho
            if arquivo:
                referenciados.add(destino)
                if not os.path.exists(destino):
                    erros.append(f"arquivo inexistente {rel} -> {alvo}")
                    continue
            if anc:
                if destino not in mapa_ancoras:
                    erros.append(f"destino não-md      {rel} -> {alvo}")
                elif anc not in mapa_ancoras[destino]:
                    erros.append(f"âncora quebrada     {rel} -> {alvo}")

        nome = os.path.basename(caminho)
        if nome not in ISENTOS:
            for secao in SECOES_OBRIGATORIAS:
                if secao not in texto:
                    avisos.append(f"sem '{secao}'  {rel}")
            if RODAPE_FONTE not in texto:
                avisos.append(f"sem rodapé de fonte  {rel}")
            if TRILHA not in texto:
                avisos.append(f"sem trilha de navegação  {rel}")
            if PROXIMOS not in texto:
                avisos.append(f"sem 'Próximos passos'  {rel}")
            if SUMARIO_VAZIO in texto:
                erros.append(f"sumário não preenchido {rel}")
            elif SUMARIO_TITULO not in texto:
                avisos.append(f"sem sumário 'Neste documento'  {rel}")

        # blocos mermaid balanceados
        abertos = len(re.findall(r"^```mermaid\s*$", texto, re.M))
        fechas = len(re.findall(r"^```\s*$", texto, re.M))
        if abertos and fechas < abertos:
            erros.append(f"bloco mermaid aberto   {rel}")

        # títulos de nível 2 duplicados geram âncora ambígua
        h2 = [m.group(1).strip() for m in re.finditer(r"^##\s+(?!#)(.*)$", texto_util, re.M)]
        dup = [t for t, n in collections.Counter(h2).items() if n > 1]
        if dup:
            avisos.append(f"títulos H2 repetidos ({', '.join(dup[:3])})  {rel}")

    for caminho in arquivos:
        if caminho not in referenciados and os.path.basename(caminho) not in ISENTOS:
            avisos.append(f"órfão (não referenciado)  {os.path.relpath(caminho, raiz)}")

    print(f"Arquivos .md ............ {len(arquivos)}")
    print(f"Links verificados ....... {total_links}")
    print(f"Erros ................... {len(erros)}")
    print(f"Avisos .................. {len(avisos)}")

    if erros:
        print("\nERROS")
        for e in erros:
            print(f"  {e}")
    if avisos:
        print("\nAVISOS")
        for a in avisos:
            print(f"  {a}")

    if not erros and not avisos:
        print("\nDocumentação íntegra.")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
