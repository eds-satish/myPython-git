# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/faq/programming.html?highlight=object%20write#how-do-i-write-a-function-with-output-parameters-call-by-reference
"""

class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)

def func4(args):
    args.a = 'new-value'        # args is a mutable callByRef
    args.b = args.b + 1         # change object in-place

args = callByRef(a='old-value', b=99)
print(args.a, args.b)
func4(args)
print(args.a, args.b)


"""

https://docs.python.org/3/faq/programming.html?highlight=object%20write#why-are-default-values-shared-between-objects

How can I find the methods or attributes of an object? 
For an instance x of a user-defined class, dir(x) returns an alphabetized list 
of the names containing the instance attributes and methods and attributes 
defined by its class.

How can i find the type of an object ? Use type(x) returns the type

"""
print(dir(args))   # notice the attributes (actual arguements) a, b
print(type(args))  # see the type is calss callByRef

# an object has ITV - identity, type, value