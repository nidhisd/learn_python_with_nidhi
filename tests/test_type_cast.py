"""
    Type Casting.

        There may be times when you want to specify a type on to a variable. This can be done with casting.
        Python is an object-orientated language, and as such it uses classes to define data types,
        including its primitive types.
        
        Casting in python is therefore done using constructor functions:
        - int() - constructs an integer number from an integer literal, a float literal (by rounding down
        to the previous whole number) literal, or a string literal (providing the string represents a
        whole number)
        - float() - constructs a float number from an integer literal, a float literal or a string literal
        (providing the string represents a float or an integer)
        - str() - constructs a string from a wide variety of data types, including strings, integer
        literals and float literals.

"""

def test_type_cast():

    #Type Casting to integer;
    assert int(1) == 1
    assert int(1.2) == 1
    assert int(1.9) == 1

    #Type Casting to float;
    assert float(1) == 1.0
    assert float(2.8) == 2.8
    assert float("3") == 3.0
    assert float("4.2") == 4.2

    #TYpe casting to String;
    assert str("s1") == 's1'
    assert str(2) == '2'
    assert str(3.0) == '3.0'