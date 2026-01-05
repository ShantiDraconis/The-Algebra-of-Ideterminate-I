# The Algebra of the Indeterminate — Buyer Hub & Formalization Repository

This repository is the **expanded technical companion** to the book:

**"The Algebra of the Indeterminate: Ultra Advanced Theory Starting from I = 0/0"**  
Author: Tiago Fagliari (ORCID: 0009-0006-6874-3910)

## What this repo is
- A **reproducible, auditable** implementation and formalization of the book's framework.
- A **buyer hub**: issues, discussions, errata, replication reports, and extensions.
- A **Copilot-first engineering spec**: the repository is structured so GitHub Copilot can implement
  modules in a controlled, test-driven way.

## Quick start (recommended)
### Option A — Docker (most reliable)
```bash
docker compose up -d
docker compose exec app bash
make doctor
make all
```

### Option B — Local (advanced)
```bash
./scripts/bootstrap.sh
make doctor
make all
```

## Outputs produced by `make all`

- `latex/build/main.pdf` (expanded technical manuscript)
- Python package build + tests
- Lean / Coq compilation (skeleton + incremental proofs)
- Reproducibility report notebook exports (optional)

## Repository map

See `docs/repo_map.md`.

## Buyer Pack

If you came from the book:

- Start here: `docs/buyer_pack.md` (coming soon in Phase 4)
- How to verify release authenticity: `hub/buyers/how_to_verify_release.md` (coming soon in Phase 8)
- Where to ask questions: `hub/DISCUSSIONS_GUIDE.md` (coming soon in Phase 8)

## Core Modules

- Python reference implementation: `src/python/ialgebra/`
- Formalization (Lean): `formal/lean/IAlgebra/`
- Formalization (Coq): `formal/coq/`
- Expanded LaTeX manuscript: `latex/`

## License

See LICENSE. If you need a commercial or dual license arrangement, open an issue with label `licensing`.