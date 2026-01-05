.PHONY: help build test clean install lint docs

help:
	@echo "Available commands:"
	@echo "  make build     - Build all components (Python, Lean, LaTeX)"
	@echo "  make test      - Run all tests"
	@echo "  make install   - Install Python package"
	@echo "  make clean     - Clean build artifacts"
	@echo "  make lint      - Run linters and formatters"
	@echo "  make docs      - Build documentation"

build: build-python build-lean build-latex

build-python:
	@echo "Building Python package..."
	pip install -e .

build-lean:
	@echo "Building Lean project..."
	cd lean && lake build

build-latex:
	@echo "Building LaTeX documents..."
	cd docs && make

test: test-python test-lean

test-python:
	@echo "Running Python tests..."
	pytest tests/

test-lean:
	@echo "Running Lean tests..."
	cd lean && lake test

lint:
	@echo "Running Python linters..."
	ruff check ialgebra/ tests/
	mypy ialgebra/

clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	cd lean && lake clean || true
	cd docs && make clean || true

install:
	pip install -e .

docs:
	@echo "Building documentation..."
	cd docs && make html
