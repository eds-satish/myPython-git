# -*- coding: utf-8 -*-
"""
This is my first python exercise
"""

def func3(args):
    args['a'] = 'new-value'     # args is a mutable dictionary
    args['b'] = args['b'] + 1   # change it in-place

args = {'a': 'old-value', 'b': 99}
func3(args)
print(args['a'], args['b'])

"""
How can I find the methods or attributes of an object? 
For an instance x of a user-defined class, dir(x) returns an alphabetized list 
of the names containing the instance attributes and methods and attributes 
defined by its class.

How can i find the type of an object ? Use type(x) returns the type

"""

print(dir(args))  #
print(type(args))
print(dir(func3))