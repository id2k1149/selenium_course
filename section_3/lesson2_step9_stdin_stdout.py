def test_substring(full_string, substring):
    assert str(substring) in str(full_string), f"expected '{substring}' to be substring of '{full_string}'"


x1 = 'fulltext'
x2 = 'some_value'
test_substring(x1, x2)
