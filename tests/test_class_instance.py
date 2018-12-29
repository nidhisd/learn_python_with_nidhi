"""
    Class Instance Objects.
"""


def test_class_instance():

    # we can declare the attribute reference for a class on the go while
    # we create the instance of the object.

    class dummy():
        """ This is dummmy sample of class. """

        pass

    dummy_instance = dummy()
    dummy_instance.temporary_attribute = 10

    assert dummy_instance.temporary_attribute == 10
    del dummy_instance.temporary_attribute
