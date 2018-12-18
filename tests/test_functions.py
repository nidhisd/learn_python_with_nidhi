def fibonacci_functions(number):

    fibonacci_list = []

    previous_number, current_number = 0, 1

    while(previous_number < number):

        fibonacci_list.append(previous_number)
        previous_number, current_number = current_number, previous_number + current_number
    
    return fibonacci_list

def test_fibonacci():

    fibonacci_function_clone = fibonacci_functions
    assert fibonacci_function_clone(10) == [0, 1, 1, 2, 3, 5, 8]

def test_functions_definitions():

    def greet(name):
        return 'Hello ' + name

    greet_someone = greet

    assert greet_someone('Gary') == "Hello Gary"

    def greet_again(name):
        def get_greet_message():
            return "Hi! "
        return get_greet_message() + name
    
    assert greet_again('Henry') == "Hi! Henry"

    #Functions can be passed as a parameter of other function.

    def person_name(func):
        other_person = 'Jack'
        return func(other_person)
    
    assert person_name(greet_again) == "Hi! Jack"