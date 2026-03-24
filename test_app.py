# test_app.py
import pytest
import app  

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0

def test_subtract():
    assert app.sub(5, 3) == 2
    assert app.sub(0, 5) == -5
    assert app.sub(-3, -2) == -1

def test_multiply():
    assert app.mul(4, 3) == 12
    assert app.mul(-2, 3) == -6
    assert app.mul(0, 100) == 0

def test_divide():
    assert app.div(10, 2) == 5
    assert app.div(-9, 3) == -3

    assert app.div(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        app.div(5, 0)
    assert "Cannot divide by zero" in str(exc_info.value)
