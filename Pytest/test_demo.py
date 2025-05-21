import pytest
from Pytest_app.demo import add, sub, div ,mul, dicount_season

@pytest.mark.skip("Skipping the test for some reason")
def test_add():
    assert add(10,20) == 30

def test_sub():
    assert sub(10,20) == -10

def test_div():
    assert div(20,10) == 2
    #Case for asserting exceptions
    with pytest.raises(ValueError):
        div(4,0)
@pytest.mark.skipif(dicount_season(),reason="skipping because discount season is on ")
def test_mul():
    assert mul(10,20) ==  200

