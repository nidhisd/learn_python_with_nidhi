"""
    Default Argument Values.

    We can assign default values to one or more arguments of a function. This makes it
    more simpler to call a function with lesser arguments.

"""

def test_default_arguments():

    def power_of(number, power = 2):
        return number ** power
    
    assert power_of(4) == 16  # Here, the second argument is missing. So, it took the default value.
    # We can also override the second argument by using the following function calls.
    assert power_of(3, 3) == 27
