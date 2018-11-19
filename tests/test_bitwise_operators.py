""" Bitwise Operators manipulates a number on bit level. 
It is mostly used to do low-level programming on Embedded systems """

def test_bitwise_operators():

    """
     
     1. AND ( & ) operator: Sets bit to 1 if both bits are 1
        5 = 0b0101
        3 = 0b0011
     
        5 & 3 = 0b0001 = 1
     """
    assert 5 & 3 == 1

    """
     2. OR ( | ) operator: Sets bit to 1 if either bit is 1.
        5 = 0b0101
        3 = 0b0011

        5 | 3 = 0b0111 = 7
     """
    assert 5 | 3 == 7

    """
     3. NOT ( ~ ) operator: Inverts all the bits.

        5 = 0b0101
       
        ~ 5 = 0b1010 = -6
    """
    assert ~5 == -6

    """
     4. XOR ( ^ ) operator: Sets each bit to 1 iff only one of the two bits is 1.
        5  = 0b0101
        15 = 0b1111
     
        5 ^ 15 = 0b1010 = 10
     """
    assert 5 ^ 15 == 10
    
    """
     5. Signed right shift ( >> ) operator: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost
        5  = 0b0101
     
        5 >> 1 = 0b0010 = 2
        5 >> 2 = 0b0001 = 1
     """
    assert 5 >> 1 == 2
    assert 5 >> 2 == 1

    """
     6. Zero fill left shift ( << ) operator: Shift left by pushing zeros in from the right and let the zero leftmost bits fall off and pad with zeroes at the right.
        5  = 0b0101
        10  = 0b1010
        5 << 1 = 0b1010 = 10
        10 << 3 = 0b1010000 = 80
     """
    assert 5 << 1 == 10
    assert 10 << 3 == 80