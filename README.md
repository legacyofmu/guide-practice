# guide-practice

Simple arithmetic pipeline with full CI tooling.

## Functions

| Function | Signature | Description |
|---|---|---|
| `add` | `(a, b) -> int\|float` | Returns `a + b` |
| `subtract` | `(a, b) -> int\|float` | Returns `a - b` |
| `multiply` | `(a, b) -> int\|float` | Returns `a * b` |
| `divide` | `(a, b) -> float` | Returns `a / b`; see below for raised exceptions |

### `divide(a, b)` — 상세

```python
def divide(a: int | float, b: int | float) -> float
```

| 예외 | 조건 |
|---|---|
| `TypeError` | `a` 또는 `b`가 `bool` |
| `ValueError` | `a` 또는 `b`가 `nan` / `inf` |
| `ZeroDivisionError` | `b == 0` |
| `OverflowError` | 결과가 `inf` (예: `1e308 / 1e-308`) |

**사용 예시**

```python
from ex_pipeline import divide

# 정상
divide(10, 2)       # 5.0
divide(7, 2)        # 3.5
divide(-9, 3)       # -3.0
divide(0, 5)        # 0.0

# 예외 발생
divide(1, 0)                  # ZeroDivisionError: division by zero: 1 / 0
divide(1.0, float("nan"))     # ValueError: divisor must be a finite number, got nan
divide(1.0, float("inf"))     # ValueError: divisor must be a finite number, got inf
divide(float("nan"), 1.0)     # ValueError: dividend must be a finite number, got nan
divide(1e308, 1e-308)         # OverflowError: result overflows to infinity: 1e+308 / 1e-308
divide(True, 1)               # TypeError: operands must be int or float, not bool
```

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
