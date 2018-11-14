"""
    Membership operators: Membership operators tests for membership in a sequence, 
                          such as strings, lists, or tuples. 
    There are two membership operators as explained below:
    1. in : Evaluates to true if it finds a variable in the specified sequence and false otherwise.
    2. not in : Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
    
    @see: https://www.tutorialspoint.com/python/membership_operators_example.htm

"""

def membership_operators():

    x = 1
    y = 5
    z = [4, 5, 7, 9]

    #In operator
    assert y in z

    #Not in operator
    assert x not in z


membership_operators()
