
"""
@see: https://www.tutorialspoint.com/python3/python_lists.htm

The list is the most versatile datatype available in Python, which can be writ
ten as a list of comma-separated values (items) between square brackets.
Important thing about a list is that the items in a list need not be of the
same type.

Example:

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

"""


def test_lists():

    # Accessing values from the list

    list1 = ['apples', 'oranges', 'banana', 2018, 2019]
    list2 = [1, 2, 3, 4, 5, 6, 7, 7, 7]

    assert list1[0:3] == ['apples', 'oranges', 'banana']
    assert list1[3:] == [2018, 2019]

    # Adding objects to the lists:

    list1.append(2020)
    assert list1[5] == 2020

    # Finding length of the lists:

    assert len(list1) == 6

    # Maximum value: Returns item from the list with max value.
    # Note: max(list1) will not work because it is a composite
    # list with objects of int and str.

    assert max(list2) == 7

    # Minimum value: Returns item from the list with min value.
    # Note: min(list1) will not work because it is a composite
    # s list with objects of int and str.

    assert min(list2) == 1

    # Counting object in a list:
    # Returns count of how many times an obj occurs in list

    assert list1.count('apples') == 1
    assert list2.count(7) == 3

    # Removing object from the list:
    assert list1.remove(2018) is None
 
    # Inserting object in the list at an offset:
    assert list1.insert(2, 2018) is None
    assert list1 == ['apples', 'oranges', 2018, 'banana', 2019, 2020]
    
    # Nesting of lists:
    # It is possible to nest lists (create lists containing other lists),
    # for example:

    list_of_cars = ['Audi', 'Tesla', 'Hyundai']
    year_of_model = [2018, 2012, 2013]
    mixed_list = [list_of_cars, year_of_model] 

    assert mixed_list == [['Audi', 'Tesla', 'Hyundai'], [2018, 2012, 2013]]


def test_list_methods():

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # 1. list.append(x)
    #       Add an item to the end of the list.
    #       Equivalent to a[len(a):] = [x].
    fruits.append('grapes')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'grapes']

    # 2. list.remove(x)
    #       Removes an item from the list.
    #       It raises a ValueError if there is no such item.

    fruits.remove('grapes')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # 3. list.insert(i, x)
    #       Inserts an item at before ith index element in the list.
    #       Example: a.insert(0, x) will insert x in front of the list a

    fruits.insert(0, 'grapes')
    assert fruits == ['grapes', 'orange', 'apple', 'pear', 'banana', 'kiwi',
                      'apple']


def test_list_comprehensions():

    """
    List Comprehensions.
        List comprehensions provide a concise way to create lists. Common
        applications are to make new lists where each element is the result
        of some operations applied to each member of another sequence or
        iterable, or to create a subsequence of those elements that satisfy
        a certain condition.
        A list comprehension consists of brackets containing an expression
        followed by a for clause,then zero or more for or if clauses. The
        result will be a new list resulting from evaluating the expression
        in the context of the for and if clauses which follow it.
    """

    squares = []

    for numbers in range(10):
        squares.append(numbers ** 2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    squares = [x ** 2 for x in range(5, 10)]

    assert squares == [25, 36, 49, 64, 81]

    # This list comprehension combines the elements of two lists if they are 
    # not equal.
    combination = [(x, y) for x in [1, 2, 3] for y in [3, 4, 3] if x != y]   
    assert combination == [(1, 3), (1, 4), (1, 3), (2, 3), (2, 4), (2, 3), 
                           (3, 4)]

    # Another equivalent code snippet for the combinations above can be 
    #  written as below:

    combination = []

    for first in [1, 2, 3]:
        for second in [3, 4, 3]:
            if first != second:
                combination.append((first, second))
    assert combination == [(1, 3), (1, 4), (1, 3), (2, 3), (2, 4), (2, 3), 
                           (3, 4)]

    # As you can see the above list contains few duplicates, we can remove
    #  the duplicates using sets. A set contains an unordered collection of
    #  unique and immutable objects.
    combination = list(set(combination))
    assert combination == [(1, 3), (1, 4), (2, 3), (3, 4), (2, 4)]

    # Lets see some more examples:

    vector = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

    # Doubling the vector
    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -6, -4, -2, 0, 2, 4, 6, 8]

    # Filtering +ves

    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 1, 2, 3, 4]

    # Applying a function to all the element in the vector
    absolute_vector = [abs(x) for x in vector]
    assert absolute_vector == [4, 3, 2, 1, 0, 1, 2, 3, 4]

    # Calling a method on each element
    fruits = ['  banana', '  loganberry ', 'passion fruit  ']
    clean_fruits = [x.strip() for x in fruits]
    assert clean_fruits == ['banana', 'loganberry', 'passion fruit']

    # Here I am creating a tuple:
    squaring = [(x, x ** 2) for x in range(10)]
    assert squaring == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25),
                        (6, 36), (7, 49), (8, 64), (9, 81)]

    # Flattening a list using two for's
    vector = [[1, 2, 3], [4, 5, 6]]
    flattened_vector = [num for elem in vector for num in elem]
    assert flattened_vector == [1, 2, 3, 4, 5, 6]

    # Finding Transpose of Matrix above
    transpose_vector = [[row[i] for row in vector] for i in range(3)]
    assert transpose_vector == [[1, 4], [2, 5], [3, 6]]
