"""
    Lambda Expressions(Anonymous Function):

        - Anonymous function or lambda function is function that is defined 
          without a name.
        - It is defined using Lambda keyword unlike def keyword for normal 
        functions.
        - Syntax:
            ```lambda arguments: expression```
        - It can have any number of arguments but only one expression.
        - THe expression is evaluated and then returned.
        - Lambda functions are used along with built-in functions like 
        filter(), map() etc.

        example: list_l = [1, 4, 6, 7, 8, 3, 5]
                 newlist_l = list(filter(lambda x: x%2 == 0, list_l)

"""


def test_lambda_expression():

    def make_increment_func(delta):
        return(lambda n: n + delta)

    increment_func = make_increment_func(30)

    assert increment_func(0) == 30
    assert increment_func(1) == 31
    assert increment_func(2) == 32
    assert increment_func(3) == 33
