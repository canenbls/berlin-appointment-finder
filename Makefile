.PHONY: test

# Type-check code
check:
	uv run mypy --check-untyped-defs .

# Lint and check formatting (no fixes)
lint:
	uv run ruff check .
	uv run ruff format --check .

# Fix linting and formatting issues
format:
	uv run ruff check --fix .
	uv run ruff format .

# Run tests
test:
	uv run pytest .

# Clean project directory
clean:
	rm -rf .venv/ .mypy_cache/ .ruff_cache/ .pytest_cache/ .coverage* __pycache__/

