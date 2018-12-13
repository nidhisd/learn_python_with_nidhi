"""
    IF statement.
    @see: https://docs.python.org/3/tutorial/controlflow.html
    
    There can be zero or more elif parts, and the else part is optional.    
    An if … elif … elif … sequence is a substitute for the switch or case statements found
    in other languages.

"""

def test_ifs():

    total_amount = 13
    message = ''

    if total_amount < 50:
        shipping_amount = 0.1 * total_amount
        total_amount += shipping_amount
        message = "Your total cost is $10"
    elif total_amount >= 50 and total_amount < 100:
        shipping_amount = 0.05 * total_amount
        total_amount += shipping_amount
        message = "Your total cost is $5"
    elif total_amount >= 100:
        message = "Congratulations! Shipping is free for you! Happy Shopping!"
    
    assert message == "Your total cost is $10"
        

