""" Logical operators:

Logical operators are used in conditional statements. It helps combine two conditional statements.

"""

def logical_operators():

    number_1 = 10
    number_2 = 20

#And
    assert number_1 > 5 and number_2 < 30
    assert number_2 > 15 and number_2 < 30

#Or
    assert number_1 > 5 or number_2 < 15
    assert number_2 > 35 or number_2 < 30

#Not
    assert not number_1 == number_2
    assert number_2 != number_1


logical_operators()