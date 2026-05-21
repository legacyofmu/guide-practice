import pytest

from ex_pipeline import add, divide, multiply, subtract


def test_add_integers() -> None:
    assert add(1, 2) == 3


def test_add_floats() -> None:
    assert add(1.5, 2.5) == 4.0


def test_add_negative() -> None:
    assert add(-3, 5) == 2


def test_add_zero() -> None:
    assert add(0, 0) == 0


def test_subtract() -> None:
    assert subtract(10, 3) == 7


def test_subtract_negative_result() -> None:
    assert subtract(3, 10) == -7


def test_multiply() -> None:
    assert multiply(4, 5) == 20


def test_multiply_by_zero() -> None:
    assert multiply(99, 0) == 0


def test_divide() -> None:
    assert divide(10, 2) == 5.0


def test_divide_float_result() -> None:
    assert divide(7, 2) == pytest.approx(3.5)


def test_multiply_negative() -> None:
    assert multiply(-3, 4) == -12


def test_divide_negative() -> None:
    assert divide(-9, 3) == pytest.approx(-3.0)


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="division by zero"):
        divide(1, 0)
