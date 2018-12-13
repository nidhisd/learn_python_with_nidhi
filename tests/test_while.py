def test_while():

    """ 
    count = 0
    while (count <= 9):
        print("The count is ", count + 1) 
        count += 1 
        
    """
    
    number = 2
    power, result = 5,1

    while (power > 0):
        result *= number
        power -= 1
    
    assert result == 32



test_while()