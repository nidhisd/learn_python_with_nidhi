"""
    @See: https://www.geeksforgeeks.org/tuples-in-python/

    Tuples.

    A Tuple is a collection of Python objects separated by commas. 
    In someways a tuple is similar to a list in terms of indexing, nested objects and repetition 
    but a tuple is immutable unlike lists which are mutable.

"""

def test_tuples():

    empty_tuple = ()
    assert empty_tuple == ()
    
    #tuplefying a list
    list = [1, 2, 3]
    tuple_from_list = tuple(list)
    assert tuple_from_list == (1, 2, 3)

    #Accessing elements of the tuples
    assert tuple_from_list[0] == 1

    #You cannot modify elements of the tuple. The statement below will error out as below:
    
    #tuple_from_list[0] = 4

    """
      Traceback (most recent call last):
        File "test_tuples.py", line 31, in <module>
          test_tuples()
        File "test_tuples.py", line 26, in test_tuples
          tuple_from_list[0] = 4
      TypeError: 'tuple' object does not support item assignment
    """

    #Slicing elements of a tuple
    assert tuple_from_list[0:2] == (1, 2)

    assert tuple_from_list[-1:] == (3,)

    #Comparing Tuples

    assert  ((3, 4, 5) < (6, 7, 3))
    assert  ((2, 3, 4) > (1, 2, 3))

    #Singleton-tuple

    singleton_tuple = 'Hi',
    assert len(singleton_tuple) == 1
    assert singleton_tuple == ('Hi',)

    #Packed-tuple

    packed_tuple = 12345, 23456, 'Hello!'

    first_is_number, second_is_number, third_is_string = packed_tuple
    assert first_is_number == 12345
    assert second_is_number == 23456
    assert third_is_string == 'Hello!'

    #Swapping using tuples
    first_is_number, second_is_number = second_is_number, first_is_number
    assert first_is_number == 23456
    assert second_is_number == 12345

