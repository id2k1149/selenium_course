def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

# launch test - >
#  pytest -v --tb=line lesson3_step8_pytest.py
