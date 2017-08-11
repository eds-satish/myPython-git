# -*- coding: utf-8 -*-

"""
import random


print(dir())
r1 = random.randint(100, 1000)
print(r1)
"""

import random

num = random.randint(1,10)
print(num)

# Add your code here
guess = int(input('Guess a number between 1 and 10: '))
times = 1
# While loop will break out when the condition becomes TRUE. Please be careful with infinite loop
while guess != num:
    guess = int(input('Guess again: '))
    times = times + 1
    if times == 3:
        break
if guess == num:
    print('No. of times: ',times)
    print('You win!')     
else:
    print('You lose! The number was: ', num)

