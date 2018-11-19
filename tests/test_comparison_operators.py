""" Comparison operators

Comparison operators are used to compare two values
"""

def test_comparison_operators():

    #Equal-to

    number = 9
    assert number == 9

    #Not-Equal-to
    number = 4
    assert number != 2

    #Less-than-equal-to
    number = 3
    assert number <= 3
    assert number < 4
    assert number < 5

    #greater-than-equal-to
    assert number > 2
    assert number >= 3
    assert number > 1