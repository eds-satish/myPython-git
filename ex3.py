# -*- coding: utf-8 -*-

#printing tables
"""
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
"""

def funct_multi(x, y):
    ans = x * y
    print(ans)

def funct_tables(n):
    for an1 in range(1,11):
        an2 = n * an1
        print(n, 'x', an1, '=', an2)
        
"""       
    ans1 = x * c1
    ans2 = x * c2
    ans3 = x * c3
    ans4 = x * c4
    ans5 = x * c5
"""

funct_multi(2, 3)
funct_tables(10)

print('==========================')
"""
100
1%100 = 1
2%100 = 2
3%100 = 3

1000 profit 
1% mean 1/100 = 0.01
1% * n ? = 1000
n = 1000 / 0.01
2%? = 1000
3%? = 1000
100% of n = 1000
out1 = given/(1/100)
out2 = given/(2/100)

"""

def funct_percent(given):
    for ito in range(1,101,10):
        out1 = given/(ito/100)
        #print(ito, '%',  'profit margin of Rs.', given, '=', 'sell', out1)
        print('EARN Rs. ', given, 'at', ito, '% margin', '=', 'sell', out1)

funct_percent(100000)

"""
sales is 100000 then break them into profits at each percent
100000 then 1%100000 = 1/100 * 100000

1/100 * 100000 = 
2/100 * 100000 = 
3/100 * 100000 =

out1 = 1/100 * given
out2 = 2/100 * given

"""
   
print('====================')
     
def funct_sales(given2):
    for ito2 in range(0,101,10):
        out2 = (ito2/100) * given2
        print('Monthly sales of', given2, 'with profit margin of', ito2, '% is =', out2)

funct_sales(100000)

'''
help me choose the function to run
'''
print('which function you want to run:')

'''
funct_multi
funct_tables
funct_percent
funct_sales
'''


