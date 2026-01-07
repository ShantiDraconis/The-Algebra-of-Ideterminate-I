import argparse
from ialgebra.types import IConst
from ialgebra.operations import oplus
from ialgebra.printing import pretty


def main() -> None:
    """CLI entry point for the ialgebra package.
    
    Provides subcommands for interacting with the indeterminate algebra system.
    
    Subcommands:
        repl: Minimal demo REPL-like output showing basic operation usage
    """
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("repl", help="Minimal demo REPL-like output")

    args = p.parse_args()
    if args.cmd == "repl":
        expr = oplus(IConst.I, 0)
        print(pretty(expr))
        return

    p.print_help()


if __name__ == "__main__":
    main()
