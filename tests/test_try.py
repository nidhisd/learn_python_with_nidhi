

def test_try():

    exception_occured = False

    # The try block will generate an error, because variable below is not defined:
    try:
        print(variable_that_does_not_exist)
    except NameError:
        exception_occured = True
    assert exception_occured

    #Try with error message:

    try:
        print(variable_that_is_not_defined)
    except NameError:
        exception_message = "Exception has occured!"
    
    assert exception_message == "Exception has occured!"

    # You can use the else keyword to define a block of code to be executed
    # if no errors were raised.

    message = ''

    try:
        message += 'Success.'
    except NameError:
        message += 'Something went wrong.'
    else:
        message += 'Nothing went wrong.'

    assert message == 'Success.Nothing went wrong.'

    #Try with Finally:
    message = ''

    try:
        message += 'Success.'
    except NameError:
        message += 'Something went wrong.'
    else:
        message += 'Nothing went wrong.'
    finally:
        message += 'Nothing went wrong.'




    