""" Documentation String.

Here are some conventions about the content and formatting of documentation strings.
The first line should always be a short, concise summary of the object’s purpose. For brevity,
it should not explicitly state the object’s name or type, since these are available by other means
(except if the name happens to be a verb describing a function’s operation). This line should begin
with a capital letter and end with a period.

If there are more lines in the documentation string, the second line should be blank, visually
separating the summary from the rest of the description. The following lines should be one or more
paragraphs describing the object’s calling conventions, its side effects, etc.
"""


def documentation_only():
    """ Documentation.

        It doesn't really do anything but describe the code following it.
    """
    pass


def test_documentation_string():
    """ Test Documentation String. """

    assert documentation_only.__doc__ == """ Documentation.

        It doesn't really do anything but describe the code following it.
    """
