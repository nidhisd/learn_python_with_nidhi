

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