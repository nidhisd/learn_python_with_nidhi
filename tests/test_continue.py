def test_continue():

    even_numbers = []
    odd_numbers = []

    for number in range(0, 10):
        if number % 2 == 0:
            even_numbers.append(number)
            continue
        odd_numbers.append(number)
    
    assert even_numbers == [0, 2, 4, 6, 8]
    assert odd_numbers == [1, 3, 5, 7, 9]
