import pytest

from ex_pipeline import add, divide, multiply, subtract


def test_add_integers() -> None:
    assert add(1, 2) == 3


def test_add_floats() -> None:
    assert add(1.5, 2.5) == pytest.approx(4.0)


def test_add_negative() -> None:
    assert add(-3, 5) == 2


def test_add_zero() -> None:
    assert add(0, 0) == 0


def test_subtract() -> None:
    assert subtract(10, 3) == 7


def test_subtract_negative_result() -> None:
    assert subtract(3, 10) == -7


def test_subtract_floats() -> None:
    assert subtract(1.5, 0.5) == pytest.approx(1.0)


def test_subtract_double_negative() -> None:
    assert subtract(-5, -3) == -2


def test_multiply() -> None:
    assert multiply(4, 5) == 20


def test_multiply_by_zero() -> None:
    assert multiply(99, 0) == 0


def test_multiply_negative() -> None:
    assert multiply(-3, 4) == -12


def test_multiply_floats() -> None:
    assert multiply(1.5, 2.0) == pytest.approx(3.0)


def test_divide() -> None:
    assert divide(10, 2) == pytest.approx(5.0)


def test_divide_float_result() -> None:
    assert divide(7, 2) == pytest.approx(3.5)


def test_divide_zero_numerator() -> None:
    assert divide(0, 5) == pytest.approx(0.0)


def test_divide_negative() -> None:
    assert divide(-9, 3) == pytest.approx(-3.0)


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(1, 0)


def test_divide_by_float_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(1, 0.0)


def test_divide_error_message_contains_operands() -> None:
    with pytest.raises(ZeroDivisionError, match=r"3 / 0"):
        divide(3, 0)


def test_divide_nan_divisor() -> None:
    with pytest.raises(ValueError, match="divisor must be a finite number"):
        divide(1.0, float("nan"))


def test_divide_inf_divisor() -> None:
    with pytest.raises(ValueError, match="divisor must be a finite number"):
        divide(1.0, float("inf"))


def test_divide_nan_dividend() -> None:
    with pytest.raises(ValueError, match="dividend must be a finite number"):
        divide(float("nan"), 1.0)


def test_divide_overflow() -> None:
    with pytest.raises(OverflowError, match="overflows to infinity"):
        divide(1e308, 1e-308)


def test_divide_bool_inputs() -> None:
    with pytest.raises(TypeError, match="bool"):
        divide(True, False)
