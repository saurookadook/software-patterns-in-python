.PHONY: install  ## Install the package, dependencies, and pre-commit for local development
install: .uv
    uv sync --frozen --group all --all-extras
    # uv pip install pre-commit
    uv run pre-commit install --install-hooks

.PHONY: clean  ## Clear local caches and build artifacts
clean:
    rm -rf `find . -name __pycache__`
    rm -f `find . -type f -name '*.py[co]'`
    rm -f `find . -type f -name '*~'`
    rm -f `find . -type f -name '.*~'`
    rm -rf .pytest_cache
    rm -rf .ruff_cache
    rm -f .coverage
    rm -f .coverage.*
    rm -rf build
    rm -rf dist
    rm -rf coverage.xml
