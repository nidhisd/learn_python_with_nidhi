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



