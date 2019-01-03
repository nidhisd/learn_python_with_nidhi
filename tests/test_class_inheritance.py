"""
Inheritance.

Inheritance is one of the principles of object-oriented programming. Since classes may share a lot
of the same code, inheritance allows a derived class to reuse the same code and modify accordingly
"""


class Person:
    """Base class example"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Returns person's name"""
        return self.name


# The syntax for a derived class definition looks like this.

class Employee(Person):
    """Example of the derived class   """

    def __init__(self, name, staff_id):
        Person.__init__(self, name)
        # You may also use super() here in order to avoid explicit using of parent class name:
        # >>> super().__init__(name)
        self.staff_id = staff_id

    def get_full_id(self):
        """Get full employee id"""
        return self.get_name() + ', ' + self.staff_id


def test_inheritance():
    """Inheritance."""
    
    person = Person('Henry')
    employee = Employee('Joseph', 'J23')

    assert person.get_name() == 'Henry'
    assert employee.get_name() == 'Joseph'
    assert employee.get_full_id() == 'Joseph, A23'

    assert isinstance(employee, Employee)
    assert not isinstance(person, Employee)

    assert isinstance(person, Person)
    assert isinstance(employee, Person)

    assert issubclass(Employee, Person)
    assert not issubclass(Person, Employee)