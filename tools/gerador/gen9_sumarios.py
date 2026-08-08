"""Preenche o sumário "Neste documento" de cada arquivo gerado.

Roda como última etapa da geração. Lê os títulos de nível 2 de cada `.md`, ignora os
que fazem parte do próprio cabeçalho padrão, e substitui o marcador `<!-- SUMARIO -->`
por uma lista de links. Reproduz a regra de âncora do GitHub, a mesma usada pelo
validador.

Se o arquivo não tiver o marcador, é deixado intacto.
"""
import os, re, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PROJ_NOME  # noqa: F401  (garante que o módulo comum carrega)

RAIZ = os.environ.get("BDH_SAIDA", ".").rstrip("/")
MARCADOR = "<!-- SUMARIO -->"

# Seções do cabeçalho padrão: não entram no sumário do próprio documento.
IGNORAR = {
    "Neste documento", "Contexto", "Escopo", "Fora do escopo",
    "Relação com outros documentos",
}

TITULO = re.compile(r"^##\s+(?!#)(.*?)\s*$")


def ancora(texto):
    texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)
    texto = re.sub(r"[*`~]", "", texto)
    base = re.sub(r"[^\w\- ]", "", texto.strip().lower(), flags=re.UNICODE)
    return base.replace(" ", "-")


def limpar(texto):
    """Texto do item de sumário: sem marcação de link, com ênfase preservada."""
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto).strip()


def processar(caminho):
    linhas = open(caminho, encoding="utf-8").read().split("\n")
    if MARCADOR not in "\n".join(linhas):
        return False

    titulos, vistos, dentro_codigo = [], collections.Counter(), False
    for l in linhas:
        if l.lstrip().startswith("```"):
            dentro_codigo = not dentro_codigo
            continue
        if dentro_codigo:
            continue
        m = TITULO.match(l)
        if not m:
            continue
        bruto = m.group(1)
        if limpar(bruto) in IGNORAR:
            continue
        a = ancora(bruto)
        vistos[a] += 1
        final = a if vistos[a] == 1 else f"{a}-{vistos[a] - 1}"
        titulos.append((limpar(bruto), final))

    if titulos:
        sumario = "\n".join(f"- [{t}](#{a})" for t, a in titulos)
    else:
        sumario = "_Documento sem seções adicionais._"

    saida = "\n".join(linhas).replace(MARCADOR, sumario)
    open(caminho, "w", encoding="utf-8").write(saida)
    return True


def main():
    n = 0
    for dp, dn, fn in os.walk(RAIZ):
        if ".git" in dp or "tools" in dp:
            continue
        for f in fn:
            if f.endswith(".md") and processar(os.path.join(dp, f)):
                n += 1
    print(f"sumários preenchidos: {n}")


if __name__ == "__main__":
    main()
