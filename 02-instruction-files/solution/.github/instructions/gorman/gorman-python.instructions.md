---
description: 'Gorman Manufacturing Python conventions for plant KPI tooling'
applyTo: '**/*.py'
---

# Gorman Python Conventions

These rules apply in addition to `.github/copilot-instructions.md`.

## Runtime

- Target Python 3.11+ and the standard library only. Don't add `requirements.txt`, `uv` or `pip` steps.
- Run code with `python3 -m <package.module>` from the repository root.

## Entry Points

```python
EXIT_SUCCESS = 0  # Run completed
EXIT_FAILURE = 1  # Data rejected or processing failed
EXIT_ERROR = 2    # Bad arguments or configuration


def main(argv: list[str] | None = None) -> int:
    ...


if __name__ == "__main__":
    sys.exit(main())
```

- Parse arguments with `argparse`. Never read `sys.argv` directly.
- Open files with `pathlib.Path` and `with` blocks, and always pass `encoding="utf-8"`.

## Style

- Use type hints on all public functions, and a one-line docstring that states units.
- Use `snake_case` for functions and variables and `UPPER_SNAKE_CASE` for constants.
- Use `logging.getLogger("gorman_oee")`. Log the record key (`plant/line/date/shift`) with every warning or error.

## Security

- Read credentials only from environment variables, for example `os.environ["GORMAN_MES_DSN"]`.
- Use `?` placeholders for every SQL statement.

## Tests

- Use `unittest` under `tests/`, with files named `test_*.py`.
- Give each bug fix a test that fails before the fix.
