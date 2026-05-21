import math
from typing import overload


@overload
def add(a: int, b: int) -> int: ...
@overload
def add(a: float, b: int) -> float: ...
@overload
def add(a: int, b: float) -> float: ...
@overload
def add(a: float, b: float) -> float: ...
def add(a: int | float, b: int | float) -> int | float:
    return a + b


@overload
def subtract(a: int, b: int) -> int: ...
@overload
def subtract(a: float, b: int) -> float: ...
@overload
def subtract(a: int, b: float) -> float: ...
@overload
def subtract(a: float, b: float) -> float: ...
def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


@overload
def multiply(a: int, b: int) -> int: ...
@overload
def multiply(a: float, b: int) -> float: ...
@overload
def multiply(a: int, b: float) -> float: ...
@overload
def multiply(a: float, b: float) -> float: ...
def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


def divide(a: int | float, b: int | float) -> float:
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("operands must be int or float, not bool")
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise ValueError(f"divisor must be a finite number, got {b!r}")
    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise ValueError(f"dividend must be a finite number, got {a!r}")
    if b == 0:
        raise ZeroDivisionError(f"division by zero: {a!r} / {b!r}")
    result = a / b
    if math.isinf(result):
        raise OverflowError(f"result overflows to infinity: {a!r} / {b!r}")
    return result
