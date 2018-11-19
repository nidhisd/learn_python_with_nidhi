"""
    Strings:

"""
import pytest

def test_string_manipulation():

    #Declaring the string 
    x= "Hello World!, How are you?"

    #Finding the length 
    assert len(x) == 26

    #Splitting string with white space
    arr = x.split()
    assert arr == ['Hello', 'World!,', 'How', 'are', 'you?']

    #Counting the letter
    assert x.count('l') == 3

    #Replacing a letter
    assert arr[0].replace('H', 'J') == 'Jello'
    
    #Stripping white spaces
    assert x.strip() == "Hello World!, How are you?"

    #Lower casing the string
    assert x.lower() == "hello world!, how are you?"

    #Upper casing the string
    assert x.upper() == "HELLO WORLD!, HOW ARE YOU?"

    #Replacing a word
    assert x.replace("World!,", "World! Nidhi, ") == "Hello World! Nidhi,  How are you?"

    #Capitalizing the string - capitalizes first word of the string
    assert x.capitalize() == "Hello world!, how are you?"

    #Capitalize every word of the string
    assert x.title() == "Hello World!, How Are You?"

    #Find a word in given string - returns the position of the string where it was found
    assert x.find('are') == 18

    #If the string is decimal
    #print("1234".isdecimal())

    #Concatenate Using '+'
    assert 'Py' + 'Thon' == 'PyThon'

    #Repeatition using '*'
    assert 3 * 'Py' + 'Thon' == 'PyPyPyThon'

    #Indexing and Slicing: While indexing is
    # used to obtain individual characters, slicing allows you to obtain
    # substring:

    text = "Python"
    #Indexing
    assert text[0] == 'P'
    assert text[1] == 'y'
    assert text[2] == 't'
    assert text[3] == 'h'
    assert text[4] == 'o'
    assert text[5] == 'n'

    #Slicing

    # One way to remember how slices work is to think of the indices as
    # pointing between characters, with the left edge of the first character
    # numbered 0. Then the right edge of the last character of a string of n
    # characters has index n, for example:
    #
    # +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #  0   1   2   3   4   5   6
    # -6  -5  -4  -3  -2  -1

    assert text[:2] == 'Py' # Characters from start to position 2(excluding postition 2).
    assert text[3:] == 'hon'  # Characters from position 4 (including position 4) till the end.
    assert text[-2:] == 'on'  # Characters from position -2 (including position -2) till the end.

# Attempting to use an index that is too large will result in an error.
    with pytest.raises(Exception):
        character_not_found = text[10]
        assert not character_not_found
