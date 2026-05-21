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
    if not b:
        raise ZeroDivisionError("division by zero")
    return a / b
