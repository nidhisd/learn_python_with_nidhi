import pytest;

def car(name, mileage=120, speed=500, type='electric'):

        # The above definition says that the function 'car' has one re
        # quired argument and three optional argument.

        message = 'The ' + name + ' is amazingly smooth, which'
        message += ' gives mileage of ' + str(mileage) + ' km per hour.'
        message += ' It can possibly go to maximum speed of '
        message += str(speed) + ' km per hour.' + ' This is first '
        message += type + ' car in the market.'

        return message


def test_keyword_argument():

    message = (
        "The Tesla is amazingly smooth, which gives mileage of 120"
        " km per hour. It can possibly go to maximum speed of 500 km per hour."
        " This is first electric car in the market."
         )

    # One positional argument is necessary. Otherwise it will throw TypeError: 
    # car() missing 1 required positional argument
    assert car('Tesla') == message

    message = (
        "The Porsche is amazingly smooth, which gives mileage of 120"
        " km per hour. It can possibly go to maximum speed of 800 km per hour."
        " This is first electric car in the market."
         )
    
    # Two keyword arguments.
    assert car(name='Porsche', speed=800) == message
    
    message = (
        "The Mercedes is amazingly smooth, which gives mileage of 800"
        " km per hour. It can possibly go to maximum speed of 500 km per hour."
        " This is first electric car in the market."
         )
    assert car('Mercedes', 800) == message

    # In a function call, keyword arguments must follow positional arguments.
    # All the keyword arguments passed must match one of the arguments
    # accepted by the function.

    assert car('Mercedes', 800, speed=500) == message

    # No argument may receive a value more than once.

    def function_with_one_parameter(number):
        return(number)
    with pytest.raises(Exception):
        function_with_one_parameter(0, number=0)

    # When a final formal parameter of the form **name is present, it receives
    # a dictionary containing all keyword arguments except for those correspon
    # ding to a formal parameter.This may be combined with a formal parameter 
    # of the form *name which receives a tuple containing the positional argum
    # ents beyond the formal parameter list. (*name must occur before **name.)

    def test_function(first_paramater, *arguments, **keywords):
                assert first_paramater == 'First'
                assert arguments == ('second', 'third')
                assert keywords == {
                              'fourth': '4',
                              'fifth': '5'
                                }

    test_function('First', 'second', 'third', fourth='4', fifth='5')
