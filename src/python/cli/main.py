import argparse
from ialgebra.types import IConst
from ialgebra.operations import oplus
from ialgebra.printing import pretty


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")

    repl = sub.add_parser("repl", help="Minimal demo REPL-like output")

    args = p.parse_args()
    if args.cmd == "repl":
        expr = oplus(IConst.I, 0)
        print(pretty(expr))
        return

    p.print_help()


if __name__ == "__main__":
    main()
