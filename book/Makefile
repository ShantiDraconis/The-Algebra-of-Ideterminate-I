# Makefile for The Algebra of the Indeterminate - Book

.PHONY: all clean book pdf view help

# LaTeX compiler
LATEX = pdflatex
BIBTEX = biber
MAIN = main
BUILD_DIR = build
OUTPUT = $(BUILD_DIR)/$(MAIN).pdf

# Default target
all: book

# Build the complete book
book: $(OUTPUT)

$(OUTPUT): main.tex references.bib parts/**/*.tex
	@echo "Building the book..."
	@mkdir -p $(BUILD_DIR)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN).tex
	$(BIBTEX) $(BUILD_DIR)/$(MAIN)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN).tex
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN).tex
	@echo "Book built successfully: $(OUTPUT)"

# Quick build (no bibliography update)
quick: main.tex
	@echo "Quick build..."
	@mkdir -p $(BUILD_DIR)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN).tex

# View the PDF
view: $(OUTPUT)
	@echo "Opening PDF..."
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(OUTPUT); \
	elif command -v open > /dev/null; then \
		open $(OUTPUT); \
	else \
		echo "Please open $(OUTPUT) manually"; \
	fi

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@rm -rf $(BUILD_DIR)
	@rm -f *.aux *.log *.out *.toc *.bbl *.blg *.bcf *.run.xml *.lof *.lot
	@echo "Clean complete."

# Deep clean including output PDF
distclean: clean
	@echo "Removing all generated files..."
	@rm -f $(MAIN).pdf

# Check for missing chapters
check:
	@echo "Checking for missing chapter files..."
	@grep -o 'include{[^}]*}' main.tex | sed 's/include{\(.*\)}/\1.tex/' | while read f; do \
		if [ ! -f "$$f" ]; then \
			echo "Missing: $$f"; \
		fi; \
	done
	@echo "Check complete."

# Create template for a new chapter
# Usage: make chapter PART=part1 NUM=05 NAME=new_chapter
chapter:
	@if [ -z "$(PART)" ] || [ -z "$(NUM)" ] || [ -z "$(NAME)" ]; then \
		echo "Usage: make chapter PART=partX NUM=NN NAME=chapter_name"; \
		exit 1; \
	fi
	@echo "Creating chapter $(NUM) in $(PART)..."
	@mkdir -p parts/$(PART)
	@echo "\\chapter{[Chapter Title]}" > parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\label{ch:$(NAME)}" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\section{Introduction}" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "[Content to be added]" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\section{Main Results}" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "[Theorems and proofs]" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\section{Examples}" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "[Examples and applications]" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\section{Exercises}" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\begin{enumerate}" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\item [Exercise 1]" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "\\end{enumerate}" >> parts/$(PART)/chapter$(NUM)_$(NAME).tex
	@echo "Chapter template created: parts/$(PART)/chapter$(NUM)_$(NAME).tex"

# Statistics
stats:
	@echo "=== Book Statistics ==="
	@echo "Total .tex files: $$(find . -name '*.tex' | wc -l)"
	@echo "Total lines of LaTeX: $$(find . -name '*.tex' -exec wc -l {} + | tail -1 | awk '{print $$1}')"
	@if [ -f $(OUTPUT) ]; then \
		echo "PDF pages: $$(pdfinfo $(OUTPUT) 2>/dev/null | grep Pages | awk '{print $$2}')"; \
	fi

# Help
help:
	@echo "Makefile for The Algebra of the Indeterminate"
	@echo ""
	@echo "Targets:"
	@echo "  all        - Build the complete book (default)"
	@echo "  book       - Build the complete book"
	@echo "  quick      - Quick build without bibliography"
	@echo "  view       - Open the PDF"
	@echo "  clean      - Remove build artifacts"
	@echo "  distclean  - Remove all generated files"
	@echo "  check      - Check for missing chapter files"
	@echo "  chapter    - Create new chapter template"
	@echo "  stats      - Show book statistics"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make book"
	@echo "  make chapter PART=part1 NUM=17 NAME=new_axiom"
	@echo "  make stats"
