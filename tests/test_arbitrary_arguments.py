"""
    Arbitrary Arguments.
    Sometimes, we do not know in advance the number of arguments that will
    be passed into a function.Python allows us to handle this kind of situ
    ation through function calls with arbitrary number of arguments.

    In the function definition we use an asterisk (*) before the parameter 
    name to denote this kind of argument.
"""


def greet(*names):
    # names is a tuple with arguments
    greeting_message = "Hi"
    greet_list = []
    # Unpacking the names argument in the below line of code.
    for name in names:
        greet_list.append(greeting_message + " " + name)
    assert greet_list == ['Hi Tom', 'Hi David', 'Hi Emily']


greet("Tom", "David", "Emily")
