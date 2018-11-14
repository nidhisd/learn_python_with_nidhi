"""Assignment operators

Assignment operators are used to assign values to variables
"""


def assignment_operator():
    """Assignment operator """

    # Assignment: =
    number = 5
    assert number == 5

    # Multiple Assignment
    number_1 , number_2 = 1, 2
    assert number_1 == 1
    assert number_2 == 2

    #Augmented operators
    number = 10
    number += 3
    assert number == 13

    number = 6
    number -= 3
    assert number == 3

    number = 5
    number %= 3
    assert number == 2

    number = 7
    number /= 2
    assert number == 3

    number = 9
    number //= 2
    assert number == 4

    number = 3
    number **= 3
    assert number == 27

    #Augmented bitwise operators

    #AND
    number = 10
    number &= 2
    assert number == 2

    #OR
    number = 5
    number |= 2
    assert number == 7

    #XOR
    number = 2
    number ^= 5
    assert number == 7

    #Right-Shift

    number = 10
    number >>= 2
    assert number == 2

    #Left-shift
    number = 3
    number <<= 4   # (5 * (2 ** 4))
    assert number == 48




assignment_operator()
