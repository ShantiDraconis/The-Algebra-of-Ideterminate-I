#!/usr/bin/env python3
"""Teste de lote cego para o decisor de `IndetDecisao` (sem humano entre a geração e a conferência).

1. `gera`: sorteia as decisões com uma semente do sistema operacional (ninguém escolhe os números) e injeta
   denominadores nulos numa fração delas. Escreve dois arquivos: os casos (sem a verdade) e a verdade (com a
   semente, para reproduzir depois).
2. O decisor (`LoteCego.lean`) lê só os casos e escreve uma saída por caso: `aprova`, `reprova` ou `erro k`.
3. `confere`: compara as saídas com a verdade. A decisão certa dos casos sem erro é calculada aqui, em Python, com
   `fractions.Fraction`: um oráculo independente do Lean.

O teste só vale se também reprovar decisores errados: o CI roda os controles negativos `A` (divisão total) e `F`
(ponto flutuante) e exige que eles falhem.
"""
import argparse
import json
import random
import secrets
import sys
from fractions import Fraction


def gera(a):
    semente = a.semente if a.semente is not None else secrets.randbits(64)
    rng = random.Random(semente)
    casos, verdade = [], []
    for _ in range(a.decisoes):
        if rng.random() < a.nulas:
            # trios a/10 + c/10 − (a+c)/10: a soma exata é 0 (aprova), o ponto flutuante costuma errar o sinal
            termos = []
            for _ in range(a.termos // 3):
                x, y = rng.randint(-10, 10), rng.randint(-10, 10)
                termos += [(x, 10), (y, 10), (-(x + y), 10)]
        else:
            termos = [(rng.randint(-10, 10), rng.randint(1, 10)) for _ in range(a.termos)]
        erro = None
        if rng.random() < a.erro:
            n = len(termos)

            def posicao():
                u = rng.random()
                return 0 if u < 0.1 else n - 1 if u < 0.2 else rng.randrange(n)

            k1 = posicao()
            termos[k1] = (termos[k1][0], 0)
            erro = k1
            if rng.random() < 0.5:
                k2 = posicao()
                termos[k2] = (termos[k2][0], 0)
                erro = min(k1, k2)
        casos.append(termos)
        if erro is not None:
            verdade.append({"erro": erro})
        else:
            s = sum(Fraction(x, y) for x, y in termos)
            verdade.append({"decisao": "aprova" if s >= 0 else "reprova", "soma_zero": s == 0})
    with open(a.casos, "w") as f:
        for t in casos:
            f.write(" ".join(f"{x} {y}" for x, y in t) + "\n")
    with open(a.verdade, "w") as f:
        json.dump({"semente": semente, "decisoes": a.decisoes, "termos": a.termos, "verdade": verdade}, f)
    print(f"{a.decisoes} decisões geradas; a semente e a verdade ficam em {a.verdade}")


def confere(a):
    v = json.load(open(a.verdade))
    saidas = open(a.saidas).read().splitlines()
    verdade = v["verdade"]
    if len(saidas) != len(verdade):
        sys.exit(f"{len(saidas)} saídas para {len(verdade)} decisões")
    c = {k: 0 for k in ("com_erro", "sem_erro", "soma_zero", "aprovou_certo", "reprovou_certo", "decidiu_errado",
                        "decidiu_errado_soma_zero", "aprovou_em_silencio", "reprovou_em_silencio", "detectou",
                        "localizou", "alarme_falso", "saida_invalida")}
    for t, s in zip(verdade, saidas):
        if s not in ("aprova", "reprova") and not s.startswith("erro "):
            c["saida_invalida"] += 1
            continue
        if "erro" in t:
            c["com_erro"] += 1
            if s == "aprova":
                c["aprovou_em_silencio"] += 1
            elif s == "reprova":
                c["reprovou_em_silencio"] += 1
            else:
                c["detectou"] += 1
                if s == f"erro {t['erro']}":
                    c["localizou"] += 1
        else:
            c["sem_erro"] += 1
            c["soma_zero"] += t["soma_zero"]
            if s.startswith("erro"):
                c["alarme_falso"] += 1
            elif s == t["decisao"]:
                c["aprovou_certo" if s == "aprova" else "reprovou_certo"] += 1
            else:
                c["decidiu_errado"] += 1
                c["decidiu_errado_soma_zero"] += t["soma_zero"]
    assert c["com_erro"] > 0 and c["soma_zero"] > 0, "lote sem caso de erro ou sem soma exatamente zero"
    passou = (c["saida_invalida"] == 0 and c["aprovou_em_silencio"] == 0 and c["reprovou_em_silencio"] == 0
              and c["localizou"] == c["com_erro"] and c["alarme_falso"] == 0 and c["decidiu_errado"] == 0)
    print(json.dumps({"saidas": a.saidas, "semente": v["semente"], "passou": passou, **c}, ensure_ascii=False))
    if passou != (a.espera == "passa"):
        sys.exit(f"esperado: {a.espera}; obtido: {'passa' if passou else 'falha'}")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = p.add_subparsers(dest="cmd", required=True)
    g = s.add_parser("gera")
    g.add_argument("casos")
    g.add_argument("verdade")
    g.add_argument("--decisoes", type=int, default=10000)
    g.add_argument("--termos", type=int, default=99)
    g.add_argument("--erro", type=float, default=0.05, help="fração das decisões com denominador nulo")
    g.add_argument("--nulas", type=float, default=0.01, help="fração das decisões com soma exatamente 0")
    g.add_argument("--semente", type=int, default=None, help="omitida: sorteada pelo sistema operacional")
    k = s.add_parser("confere")
    k.add_argument("verdade")
    k.add_argument("saidas")
    k.add_argument("--espera", choices=("passa", "falha"), default="passa")
    a = p.parse_args()
    gera(a) if a.cmd == "gera" else confere(a)


if __name__ == "__main__":
    main()
