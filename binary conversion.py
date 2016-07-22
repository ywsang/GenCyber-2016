# -*- coding: utf-8 -*-
"""
Yana Sang
GenCyber 2016
Conversions

"""
#Hexadecimal to Binary 



hexNum = input("Enter the hexadecimal digit that you want to convert : ")
print(bin(int(hexNum, 16)))

#inp = input("enter : ")
#print(inp)

def hex_to_bin (hexNum):
    print("Beginning conversion...")    
    table = "0123456789ABCDEF"    
    result = ""    
    i = 0
    while i <= (len(hexNum)-1):
        decimal = table.find(hexNum[i])   
        #beginning of conversion of decimal to binary
        binaryResult = ""
        quotient = decimal        
        while quotient > 0:
            binaryResult = str(quotient % 2) + binaryResult
            quotient = decimal//2
        #end of conversion of decimal to binary
        result = result + binaryResult
        i = i + 1        
    return result

inp = input("Enter the hexadecimal digit that you want to convert : ") 
hexNum = (int(hexNum, 16))
print(hexNum)

answer = hex_to_bin(hexNum)
print(answer)
#def ascii_to_hex(letter):
    