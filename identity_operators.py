"""
    Identity Operators:  -  Identity Operators are used to determine whether a value is of a certain class or type.
                         -  They are usually used to determine the type of data a certain variable contains.
                         For Example;  >> x = 5 
                                       >> type(x) is int
"""

def identity_operators():

        #Is operator:
        # Returns true if both variables are the same object.
         
         x = 5
         assert type(x) is int
        
         x = ["Star", "light"]
         y = ["Star", "light"]
         z = x

         assert z is x
         # In above example, x and z are the same object, they also share the same memory location.
         
         #Is Not Operator
         # Returns true if both variables are not the same object.
         # For Example: x and y  are not same objects even if they have same content.

         assert x is not y
         # In above example, x and y are having same values but they are not same objects. 
         # They do not share same memory location.
         
         assert x == y
         # In above example, we can see how 'is' and '==' are different operators. 
         # '==' compares the value of the objects and 'is' compares object at memory level too.


identity_operators()

