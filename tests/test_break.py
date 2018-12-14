def test_break():

    number_to_search = 33

    number_to_iterate = 0

    for i in range(100):
        if i == number_to_search:
            break
        else:
            number_to_iterate += 1
    
    assert number_to_iterate == 33