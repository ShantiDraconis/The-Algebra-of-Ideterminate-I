#!/usr/bin/env python3
"""Decisores de stacks comuns para o teste de lote cego (`../lote_cego.py`).

Cada decisor recebe o arquivo de casos (uma decisão por linha: `a₀ b₀ a₁ b₁ …`), implementa a regra
"aprova se Σ aₖ/bₖ ≥ 0" do jeito idiomático daquela stack e escreve uma saída por linha: `aprova`, `reprova`,
`erro k` (primeiro denominador nulo no índice k) ou `erro ?` (erro detectado, sem índice). Nenhum decisor vê a
verdade nem a semente. Uso:

    python3 adaptadores.py <decisor> casos.txt saidas.txt

Decisores:

* `sqlite`      — SQL: `SUM(a * 1.0 / b) >= 0`. No SQLite, `x / 0` é `NULL` e `SUM` ignora `NULL`.
* `numpy`       — `np.sum(a / b) >= 0` em `float64`. `x / 0` é `±inf` ou `nan`; o NumPy só avisa.
* `pandas`      — `(df.a / df.b).sum() >= 0`. Igual ao NumPy, mas `sum` pula `nan` (`skipna=True`).
* `py_float`    — Python `float` com `try/except ZeroDivisionError` → `erro ?`.
* `py_fraction` — Python `Fraction` (exato) com `try/except ZeroDivisionError` → `erro ?`.
* `py_origem`   — Python `Fraction` que devolve o índice do primeiro denominador nulo: o mesmo contrato de
  `IndetDecisao.decidir`, escrito à mão. Controle positivo: deve passar.
"""
import sys
from fractions import Fraction


def ler(caminho):
    casos = []
    for linha in open(caminho):
        n = [int(x) for x in linha.split()]
        casos.append(list(zip(n[0::2], n[1::2])))
    return casos


def sqlite(casos):
    import sqlite3

    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE termo (decisao INTEGER, pos INTEGER, a INTEGER, b INTEGER)")
    con.executemany("INSERT INTO termo VALUES (?, ?, ?, ?)",
                    ((d, k, a, b) for d, t in enumerate(casos) for k, (a, b) in enumerate(t)))
    linhas = con.execute("""
        SELECT decisao, CASE WHEN SUM(a * 1.0 / b) >= 0 THEN 'aprova' ELSE 'reprova' END
        FROM termo GROUP BY decisao ORDER BY decisao""").fetchall()
    return [s for _, s in linhas]


def numpy(casos):
    import numpy as np

    saidas = []
    with np.errstate(divide="ignore", invalid="ignore"):  # o padrão só imprime um aviso; a decisão é a mesma
        for t in casos:
            a = np.array([x for x, _ in t], dtype=np.float64)
            b = np.array([y for _, y in t], dtype=np.float64)
            saidas.append("aprova" if np.sum(a / b) >= 0 else "reprova")
    return saidas


def pandas(casos):
    import numpy as np
    import pandas as pd

    df = pd.DataFrame([(d, a, b) for d, t in enumerate(casos) for a, b in t], columns=["decisao", "a", "b"])
    with np.errstate(divide="ignore", invalid="ignore"):
        df["q"] = df["a"].astype("float64") / df["b"].astype("float64")
    s = df.groupby("decisao", sort=True)["q"].sum()
    return ["aprova" if x >= 0 else "reprova" for x in s]


def py_float(casos):
    saidas = []
    for t in casos:
        try:
            saidas.append("aprova" if sum(a / b for a, b in t) >= 0 else "reprova")
        except ZeroDivisionError:
            saidas.append("erro ?")
    return saidas


def py_fraction(casos):
    saidas = []
    for t in casos:
        try:
            saidas.append("aprova" if sum(Fraction(a, b) for a, b in t) >= 0 else "reprova")
        except ZeroDivisionError:
            saidas.append("erro ?")
    return saidas


def py_origem(casos):
    saidas = []
    for t in casos:
        s, saida = Fraction(0), None
        for k, (a, b) in enumerate(t):
            if b == 0:
                saida = f"erro {k}"
                break
            s += Fraction(a, b)
        saidas.append(saida or ("aprova" if s >= 0 else "reprova"))
    return saidas


DECISORES = {f.__name__: f for f in (sqlite, numpy, pandas, py_float, py_fraction, py_origem)}

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in DECISORES:
        sys.exit(f"uso: adaptadores.py <{'|'.join(DECISORES)}> casos.txt saidas.txt")
    saidas = DECISORES[sys.argv[1]](ler(sys.argv[2]))
    with open(sys.argv[3], "w") as f:
        f.write("\n".join(saidas) + "\n")
