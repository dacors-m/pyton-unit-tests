from main import Calculator

def test_add_ok() -> None:
    cal = Calculator(number_a=5, number_b=5)

    res = cal.add()

    assert res == 10

def test_substract_ok() -> None:
    cal = Calculator(number_a=5, number_b=5)

    res = cal.substract()

    assert res == 0


