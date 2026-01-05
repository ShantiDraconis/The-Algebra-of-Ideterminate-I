# I-Theory Requirements

## Python

```bash
pip install numpy
```

## Lean 4

Install Lean 4 from: https://leanprover.github.io/lean4/doc/setup.html

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
```

## Coq

Install Coq 8.16 or later:

```bash
# Ubuntu/Debian
sudo apt-get install coq

# macOS
brew install coq

# Or via opam
opam install coq
```

## Isabelle

Download from: https://isabelle.in.tum.de/

## Agda

Install Agda 2.6.3 or later:

```bash
# Via cabal
cabal update
cabal install Agda

# Or via stack
stack install Agda
```

Install Agda standard library:

```bash
mkdir -p ~/.agda
cd ~/.agda
git clone https://github.com/agda/agda-stdlib.git
```
