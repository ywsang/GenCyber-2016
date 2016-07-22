# -*- coding: utf-8 -*-
"""
Conditionals Practice

"""

def odd_or_even (num):
    if (num%2==0):
        print("even")
    else :
        print("odd")
        
def big_or_small (num):
    if (num>100):
        print("big")
    else:
        print("small")
        
def oddeven_bigsmall (num):
    if (num%2==0 and num>100):
        print("big & even")
    elif(num%2==0):
        print("small & even")
    elif(num%2!=0 and num>100):
        print("big & odd")
    else:
        print("small & odd")

num = int(input("Enter any integer : "))
print("This number is:")
odd_or_even(num)
print("This number is:")
big_or_small(num)
print("Therefore this number is:")
oddeven_bigsmall(num)

     
    

