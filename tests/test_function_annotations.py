""" Function Annotations.

    see: @https://www.python.org/dev/peps/pep-3107/#fundamentals-of-function-annotations

    Function annotations are arbitrary python expressions that are associated
    with various part of functions. These expressions are evaluated at compile
    time and have no life in python’s runtime environment.
    Function annotations are completely optional metadata information about the
    types used by user-defined functions.

    Function annotations, both for parameters and return values.

    Parameter annotations are defined by a colon after the parameter name foll
    owed by an expression evaluating to the value of the annotation.

    Return annotations are defined by a literal ->, followed by an expression,
    between the parameter list and the colon denoting the end of the def statement.

"""


def thanksgiving(turkey: str, gifts: int = 3) -> str:
    """ Thanksgiving.

        This function has one positional argument 'turkey' and one keyword arg
        ument 'gifts' and the return value is annoted to str
    """
    message = "In Thanksgiving, i love eating " + turkey + "This year, I got "
    message += str(gifts) + "gifts from Grandma."
    return message


def test_function_annotations():
    """Function Annotations."""

    assert thanksgiving.__annotations__ == {'turkey': str,
                                            'gifts': int,
                                            'return': str}
