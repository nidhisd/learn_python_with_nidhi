""" 
    Variable Scope.

    @see: https://www.datacamp.com/community/tutorials/scope-of-variables-python

    Python keeps track of all the variable mappings with namespaces. These are containers 
    for mapping names of variables to objects. You can think of them as dictionaries, 
    containing name:object mappings. This allows access to objects by names you choose 
    to assign to them.

    For Example:
        i = 5
        j = i
        i = 3
    The namespace for the above code would look like; 
    {i:3, j:5}.


    Global Variable: If you define a variable at the top of your script, it will 
    be a global variable. This means that it is accessible from anywhere in your 
    script, including from within a function. 

    But, if the same variable is declared again in the nested function/inner function, the system will 
    use the locally declared instance of the variable unless we direct the system to use the global/non-local 
    instance rather than local. We can do so by using keywords 'global' and 'non-local'.

    Global keyword:
    With global, you're telling Python to use the globally defined variable instead of locally defining it. 
    To use it, simply type global, followed by the variable name.


    """





def test_function_scope_1():

    x = 'a'

    def outer():

        x = 'b'

        def inner():
            """
            With the nonlocal keyword below, you're telling python that the x in the inner() function 
            should actually refer to the x defined in the outer() function, which is one level higher
            """
            nonlocal x
            x = 'c'
            assert x == 'c'
        
        inner()
        assert x == 'c'

    
    outer()
    assert x == 'a'

name = 'Robert'

def test_global():

    def change_name(new_name):
    #The global keyword below will search for globally declared instance of variable 'name'
    
        global name
        name = new_name

    assert name == 'Robert'
    change_name('Henry')
    assert name == 'Henry'

assert name == 'Robert'

