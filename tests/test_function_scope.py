
def test_function_scope():

    variable_scope = "Global"

    def test_local():
        variable_scope = "Local"
        nonlocal variable_scope
        return variable_scope
    
    def test_non_local():
        nonlocal variable_scope 
        variable_scope = "Non Local"
        return variable_scope
    
    def test_global():
        global variable_scope 
        variable_scope = "Global"
        return variable_scope
    
    print("Current scope : " + variable_scope)
    test_local()
    print("Current scope : " + variable_scope)
    test_non_local()
    print("Current scope : " + variable_scope)
    test_global()
    print("Current scope : " + variable_scope)

test_function_scope()
print(variable_scope)