
"""CONTINUE statement

@see: https://docs.python.org/3/tutorial/controlflow.html

    The continue statement is borrowed from C, continues with the next iteration of the loop.
"""
def test_continue():

    even_numbers = []
    odd_numbers = []

    for number in range(0, 10):
        if number % 2 == 0:
            even_numbers.append(number)
            #Stops current loop iteration and go to the next iteration immediately.
            continue
        odd_numbers.append(number)
    
    assert even_numbers == [0, 2, 4, 6, 8]
    assert odd_numbers == [1, 3, 5, 7, 9]
