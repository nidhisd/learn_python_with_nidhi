"""
    Class Variable and Instance Variable.

        Class variables are the variables or attributes shared by all the instances
        of the class, whereas Instance variable is only shared by the particular
        object instance.
"""


def test_class_and_instance_variable():

    class Dog():
        """ Dog class Blue print"""

        kind = "German Shepherd"  # Class variable shared by all instances.

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

    Kosta = Dog('Kosta')
    Vruno = Dog('Vruno')

    assert Kosta.kind == "German Shepherd"
    assert Vruno.kind == "German Shepherd"

    class DogWithSharedTricks():
        """ Dog class with tricks class attribute """
        kind = 'German Shepherd'
        tricks = []

        def __init__(self, name):
            self.name = name
        
        def add_tricks(self, trick):
            self.tricks.append(trick)
        
    class DogWithTricks:
        """Dog class Instance attribute example"""

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.
            self.tricks = []  # creates a new empty list for each dog

        def add_trick(self, trick):
            self.tricks.append(trick)

    Kosta = DogWithTricks('Kosta')
    Vrunoa = DogWithTricks('vrunoa')

    Kosta.add_trick('roll over')
    Vrunoa.add_trick('play dead')

    assert Kosta.tricks == ['roll over']
    assert Vrunoa.tricks == ['play dead']
