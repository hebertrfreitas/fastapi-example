# AGENTS.md

> This file is managed by **agents-md-governance**. The corporate rules block is synced
> automatically from the corporate standard on every pull request and must not be edited
> here: changes to it will be overwritten. Add project-specific instructions to the
> *Project-specific rules* section. **When rules conflict, corporate rules take precedence.**

<!-- agents-md-governance:corporate:begin template=python version=1.0.0 sha=1a73aa84ceaa -->
## Corporate rules — Python

### Environment and dependencies
- Target Python 3.12+. Manage dependencies with `uv` and declare them in `pyproject.toml`; never add a new `requirements.txt`.
- Pin direct dependencies with a lower bound and commit the lock file.
- Do not add a new third-party dependency when the standard library or an existing dependency already solves the problem.

### Code style
- Format with `ruff format` and lint with `ruff check`; code must pass both before a change is considered done.
- Add type hints to every public function and method; the code must pass `mypy --strict` in modules that already use it.
- Prefer `pathlib` over `os.path`, f-strings over `%`/`format`, and `dataclasses` or `pydantic` models over loose dicts.

### Testing
- Write tests with `pytest`. Every bug fix comes with a regression test; every new public function has at least one test.
- Tests must not call real external services (LLMs, databases, HTTP APIs); use fakes or mocks.
- Run `uv run pytest` and make sure it passes before finishing a task.

### Security
- Never hard-code secrets, tokens or credentials; read them from environment variables or the corporate secret manager.
- Never log personal data (PII) or secrets. Use the `logging` module, never `print`, in application code.
- Use parameterized queries; never build SQL with string concatenation.

### Working agreement for agents
- Keep changes small and focused on the requested task; do not refactor unrelated code.
- Explain any change to public APIs, database schemas or CI configuration in the PR description.
<!-- agents-md-governance:corporate:end -->

## Project-specific rules

<!-- agents-md-governance:project:begin -->
<!-- agents-md-governance:project:end -->
