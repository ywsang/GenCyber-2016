# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:20:55 2016

@author: student
"""
#for d in range (0,1380):
#    if ((13*d)%1380)==1:
#        print(d)
        
        
def RSA_encrypt(p, q, message):
    n = p*q
    print ("n =", n)
    t = (p-1)*(q-1)
    print ("t =", t)
    e = 13
    print ("e =", e)
    """    
    while e > 0:
        if (t%e != 0):
            e = e
            print ("e =", e)
            break
        e -= 1
    """
    for d in range (0,t):
        if ((e*d)%t)==1:
            d = d
            print ("d =",d)
            break
    #encrypted = ""
            
    lst = []
    for j in range (0, len(message)):
        m = ord(message[j])
        c = (m**e)%n
        #print (c)
        #toAdd = (c, " ")
        #encrypted += str(c)
        lst.append(c)
    #return encrypted
    print("c =", lst)
    
RSA_encrypt(47, 31, "food tastes good")
    
    