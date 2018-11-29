
"""
    Sets.

    A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
    Set objects also support mathematical operations like union, intersection, difference, and 
    symmetric difference.   

"""

def test_sets():

    sets_of_cars = {'Hyundai', 'Tesla', 'Honda', 'Maruti'}

    assert isinstance(sets_of_cars, set)
    # We can also create sets using constructor set()
    #Notice the double round brackets below.

    set_of_fruits = set(("apple", "Banana", "Guava", "Strawberry"))

    assert isinstance(set_of_fruits, set)

def test_set_methods():

    set_of_fruits = set(("apple", "Banana", "Guava", "Strawberry"))
    
    # 1. To check if the item is in the set:
    assert "apple" in set_of_fruits

    assert "Hyundai" not in set_of_fruits

    # 2. To check the length of the set:

    assert len(set_of_fruits) == 4

    # 3. Removing an item from the set:

    set_of_fruits.remove("apple")
    assert "apple" not in set_of_fruits
    assert len(set_of_fruits) == 3

    # 4. Making set of letters from words

    first_word = "Abracadabracadabra"
    set_of_first_word = set(first_word)

    assert set_of_first_word == {'a', 'c', 'd', 'A', 'b', 'r'}
    
    second_word = "Giligialiglichhu"
    set_of_second_word = set(second_word)

    assert set_of_second_word == {'h', 'G', 'l', 'g', 'u', 'c', 'i', 'a'}

    # 5. Intersection operation:

    assert set_of_first_word & set_of_second_word == {'a', 'c'}

    # 6. Letters in first word but not in second:

    assert set_of_first_word - set_of_second_word == {'b', 'r', 'd', 'A'}

    # 7. Letters in first word or second word or both:
    assert set_of_first_word | set_of_second_word == {'r', 'i', 'l', 'b', 'A', 'c', 'u', 'a', 'g', 'd', 'h', 'G'}

    # 8. Letters in first or second word but not both:
    assert set_of_first_word ^ set_of_second_word == {'A', 'l', 'u', 'r', 'G', 'b', 'g', 'd', 'h', 'i'}

    # 9. Set Comprehensions:
    word = { char for char in "Apple" if char not in "Avacado"}
    assert word == {'p', 'e','l'}

    #Always remember order doesn't matter in sets so; {'a', 'b', 'c'} == {'b', 'a', 'c'}