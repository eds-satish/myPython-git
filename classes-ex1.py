# -*- coding: utf-8 -*-
class FooClass(object):
    """ my very first class: FooClass """
    version = 0.1
    
    def __init__(self, nm='John Doe'):
        """ constructor """
        self.name = nm # class instance (data) attribute
        print('1. Created a class instance for', nm)
        print('I am printing: ', self.__doc__)
        print(__name__)
        
    def showname(self):
        """ display instance attribute and class name """
        print('2. Your name is: ', self.name)
        print('3. My name is: ', self.__class__.__name__)
        print(__name__)
    def showver(self):
        """ display class(static) attribute """
        print('4. Version is: ', self.version) # References FooClass.version
        print(__name__)
    def addMe2Me(self, x): #does not use self
        """ apply + operation to argument """
        return x + x
        
    
foo1 = FooClass() # Class instance is created and init fucntion called and executed
print(foo1.__class__) # __ double underscore are special names defined by the python interpreter
print(foo1.__dir__) # __*__ are the attributes that are available in the scope of (class or function or method)
print(foo1.__init__) # https://docs.python.org/3/reference/datamodel.html#specialnames

# Read the URL https://docs.python.org/3/reference/lexical_analysis.html 
# lexical analysis is very important


foo1.showname()
foo1.showver()
print('5. addMe2Me is: ', foo1.addMe2Me('xyz'))
print(__name__)
print(dir())
print(__builtins__)
print(__file__)


