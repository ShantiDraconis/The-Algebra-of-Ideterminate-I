# The Algebra of the Indeterminate

## Repository Bootstrap

This repository includes a comprehensive bootstrap script to create the full project structure.

### Usage

To create a new project structure:

```bash
# Option 1: Create in a new subdirectory
chmod +x bootstrap_repo.sh
./bootstrap_repo.sh my-project-name

# Option 2: Generate in current directory (must be empty or you accept merges)
./bootstrap_repo.sh .
```

### What the script creates

The `bootstrap_repo.sh` script generates a complete repository structure including:

- **Docker setup**: Dockerfile and docker-compose.yml for containerized development
- **Source code**: Python package, JavaScript playground, and formal verification (Lean/Coq)
- **Documentation**: Theory docs, tutorials, and governance materials
- **Testing infrastructure**: pytest setup for Python, jest for JavaScript
- **CI/CD**: GitHub Actions workflows
- **Issue templates**: Bug reports, feature requests, and theoretical questions
- **Development tools**: Makefile, linters, formatters
- **Buyer hub**: Materials for book purchasers including errata and examples
- **Notebooks**: Jupyter notebooks for interactive exploration

### Quick Start After Bootstrap

```bash
cd your-project-directory

# Using Docker (recommended)
docker compose up -d
docker compose exec app bash
make doctor
make all

# Or local installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e src/python/
make test
```

### Project Structure

See the generated `README.md` in the bootstrapped project for detailed structure documentation.