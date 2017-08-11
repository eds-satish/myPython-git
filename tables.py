# -*- coding: utf-8 -*-

"""
def tables_function(num):
    print("Inside-1", dir())
    for n in range(1,myRange):
        print("Inside-2", dir())
        total = num * n
        print(num, '*', n, '=', total)
        print("Inside-3", dir())
        print("repeat loop")


print("Please enter a number: ")
myVal = input()
print("Please input the range: ")
myRange = int(input()) + 1
print("Outer-1", dir())
tables_function(int(myVal))

"""



def tables_function(myNum):
    for n in range(1,11):
        myTotal = myNum * n
        print(myNum, "*", n, "=", myTotal)
        
print("Enter a number: ")
myString = input()
tables_function(int(myString))
    