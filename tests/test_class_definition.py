"""
    Class Definition.

    Classes are like a blueprint or a prototype that you can define to use to
    create objects. This defines a set of attributes that will characterize any
    object that is instantiated from this class.

    Objects are the instances of the class.
"""


def test_class_definition():

    # Class definition is done using 'class' keyword similar to 'def' in
    # functions.

    class complex_number():
        """ Example of the complex numbers class """
        real = 0
        imaginary = 0

        def get_real(self):
            # Return real part of a complx number.
            return self.real

        def get_imaginary(self):
            # Return imaginary part of a complex number.
            return self.imaginary

    assert complex_number.real == 0
    assert complex_number.imaginary == 0
    assert complex_number.__doc__ == " Example of the complex numbers class "

    complex_number_1 = complex_number()
    complex_number_1.real = 1
    complex_number_1.imaginary = 2

    assert complex_number_1.real == 1
    assert complex_number_1.imaginary == 2

    class complex_number_constructor():

        """ Example of Complex number with a constructor """

        def __init__(self, real_part, imaginary_part):
            """ Initiazles real and imaginary attributes of a complex_number
            object with real_part and imaginary_part """
            self.real = real_part
            self.imaginary = imaginary_part

        def get_real(self):
            """ Returns real part of a complex number"""
            return self.real

        def get_imaginary(self):
            """ Returns imaginary part of a complex number"""
            return self.imaginary

    complex_number_2 = complex_number_constructor(3, 2)
    assert complex_number_2.real == 3
    assert complex_number_2.imaginary == 2
