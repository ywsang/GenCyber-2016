# -*- coding: utf-8 -*-
"""
Yana Sang
GenCyber 2016
July 8, 2016
Caesar Cipher

"""
def caesar_cipher_encrypt (original, shift):
    encoded = ""
    for char in original:
        newNum = 0        
        num = ord(char)
        if (num >= 65 and num <=90):        
            if num == 32:
                newNum = 32
            elif (num+shift)>90:
                newNum = (num+shift)-26
            else:
                newNum = num+shift
            encoded = encoded+chr(newNum)
        else :
            if num == 32:
                newNum = 32
            elif (num+shift)>122:
                newNum = (num+shift)-26
            else:
                newNum = num+shift
            encoded = encoded+chr(newNum)
    return encoded
    
original = input("Enter your phrase : ")
shift = int(input("Enter the shift : "))
print(caesar_cipher_encrypt(original, shift))

def caesar_cipher_decrypt (message):
    decoded = ""    
    i = 1
    while (i<=26):        
        for char in message:
            newNum = 0
            num = ord(char)
            if (num >= 65 and num <= 90):            
                if num == 32:
                    newNum = 32
                elif (num-i)<65:
                    newNum = (num-i)+26
                else: 
                    newNum = num-i
                decoded = decoded+chr(newNum)
            else :
                if num == 32:
                    newNum = 32
                elif (num-i)<97:
                    newNum = (num-i)+26
                else: 
                    newNum = num-i
                decoded = decoded+chr(newNum)
        decoded = decoded + '\n'
        i += 1
    return decoded
    
orig = input("Enter the encoded message : ")
print(caesar_cipher_decrypt(orig))
                
