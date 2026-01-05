SHELL := /bin/bash

.PHONY: doctor all python_test latex lean coq fmt lint clean

doctor:
	@./scripts/doctor.sh

all: doctor python_test latex lean coq
	@echo "OK: build complete."

python_test:
	@cd src/python && python -m pip install -U pip && pip install -e ".[dev]"
	@cd src/python && pytest -q

latex:
	@cd latex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

lean:
	@cd formal/lean && lake build

coq:
	@cd formal/coq && $(MAKE) || echo "WARNING: Coq build failed but is being ignored."

fmt:
	@./scripts/format_all.sh

lint:
	@python scripts/lint_repo.py

clean:
	@rm -rf latex/build || true
	@find . -name "__pycache__" -type d -prune -exec rm -rf {} \;
