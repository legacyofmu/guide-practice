# guide-practice

Simple arithmetic pipeline with full CI tooling.

## Functions

| Function | Signature | Description |
|---|---|---|
| `add` | `(a, b) -> int\|float` | Returns `a + b` |
| `subtract` | `(a, b) -> int\|float` | Returns `a - b` |
| `multiply` | `(a, b) -> int\|float` | Returns `a * b` |
| `divide` | `(a, b) -> float` | Returns `a / b`; raises `ValueError` on zero divisor |

## Development

```bash
# lint
.venv/bin/ruff check .

# type check
.venv/bin/mypy ex_pipeline.py test_pipeline.py

# test
.venv/bin/pytest -v
```

## CI

- **Pre-commit hook**: runs ruff + mypy + pytest before every commit.
- **GitHub Actions**: Claude posts an automated code review comment on every PR.
