"""
    Dictionaries.

    @See: https://github.com/trekhleb/learn-python/blob/master/src/data_types/test_dictionaries.py

    - A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are
    written with curly brackets, and they have keys and values.
    
    Dictionaries are sometimes found in other languages as “associative memories” or “associative
    arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
    keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used
    as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
    either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since
    lists can be modified in place using index assignments, slice assignments, or methods like append()
    and extend().

    It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
    keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
    Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
    to the dictionary; this is also the way dictionaries are written on output.


"""

def test_dicts():

    dict_of_cars_models = {
        2010 : 'Hyundai',
        1991 : 'Porsche',
        2014 : 'Tesla'
    }

    assert isinstance(dict_of_cars_models, dict)

    assert dict_of_cars_models[2010] == 'Hyundai'
    assert dict_of_cars_models[1991] == 'Porsche'
    assert dict_of_cars_models[2014] == 'Tesla'

    # Existence using Keys:
    assert 2010 in dict_of_cars_models
    assert 2018 not in dict_of_cars_models

    #Chnaging value using keys:

    dict_of_cars_models[2010] = "Maruti"
    assert dict_of_cars_models[2010] == "Maruti"

    #Adding new key:value pair to dictionary:

    dict_of_cars_models[2011] = "Honda"
    assert len(dict_of_cars_models) == 4
    assert 2011 in dict_of_cars_models

    # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
    # in insertion order (if you want it sorted, just use sorted(d) instead).

    assert list(dict_of_cars_models) == [2010, 1991, 2014, 2011]
    assert sorted(dict_of_cars_models) == [1991, 2010, 2011, 2014]

    # Deleting key:value pair using del:
    del dict_of_cars_models[2011]
    assert 2011 not in dict_of_cars_models

    # Dict Comprehensions:
    dict_of_squares = { x: x ** 2 for x in range(10)}
    assert dict_of_squares == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

    dict_of_cubes = { x: x ** 3 for x in (1, 2, 3)}
    assert dict_of_cubes == {1: 1, 2: 8, 3: 27}

    # Dictionary for String keys:

    dict_of_string_keys = dict(Hyundai = 2010, Maruti = 2011, Tesla = 2014)
    assert dict_of_string_keys['Hyundai'] == 2010
    assert dict_of_string_keys['Maruti'] == 2011
    assert dict_of_string_keys['Tesla'] == 2014