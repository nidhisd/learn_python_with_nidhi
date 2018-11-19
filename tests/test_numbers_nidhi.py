"""
    @see: https://www.tutorialspoint.com/python/python_numbers.htm
    @see: https://www.w3schools.com/python/python_numbers.asp

    There are basically three numeric types in Python.
    1. int - Eg: x = 5
    2. long - Eg: y = 523432534546547657586786786867
    2. float - Eg: z = 2.87
    3. complex - Eg: w = 4 + 2i

"""

import math 

def test_numbers():

    x = 523
    assert type(x) is int

    #y = 523432534546547657586786786867
    #assert type(y) is long

    z = 4.6666666
    assert type(z) is float

    w = 5 + 2j
    assert type(w) is complex


def test_int():

    #There are several in-built mathematical functions around integers type.
    #Lets try few of them out.

    # cmp(x,y): Compares value of x and y.
    #           -1 ; if x < y
    #            1 ; if x > y
    #            0 ; if x = y
    # Note: cmp(a,b) does not work in Python 3.
    #assert cmp(3, 8) == -1
    #assert cmp(8, 3) == 1
    #assert cmp(3, 3) == 0

    # pow(x,y): x ** y
    
    assert pow(2,3) == 8    # 2 * 2 * 2

    # max(x1, x2, x3, x4, ...): returns largest number of the sequence .

    assert max(1, 2, 3, 4, 5) == 5

    # min(x1, x2, x3, x4, ...): returns smallest number of the sequence .

    assert min(1, 2, 3, 4, 5) == 1

    #sqrt(x) = returns square root of the number.

    assert math.sqrt(16) == 4
    # For many of the mathematical functions to execute we need to import math library in python.
    #Likewise, you can execute several inbuilt mathematical functions from the math library.
