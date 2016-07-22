# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 12:53:59 2016

@author: student
"""

def hex_to_base64(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binaryString = ""    
    #lst = []
    converted = ""    
    for i in range (0, len(message)):
        #print (i)        
        binValue = bin(int(message[i], 16))
        #print(binValue)
        numsLength = (len(str(binValue)))-2
        for k in range (0,8-numsLength):
            binaryString += str(0)
        for l in range (0, numsLength):
            binaryString += (str(binValue)[l+2])
    #print(lst)
    print(binaryString)
    j = 0 
    individualString = binaryString[0,6]
    decValue = int(individualString, 2)
    print(decValue)
    """
    if (int(binary)%6 == 0):
        while j< 6:
            decValue = int(binary[j, j+6], 2)
            print(decValue)
            j+=6
    """  
        
        #j+=6

hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")