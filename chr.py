# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:01:52 2016

@author: student
"""
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = [84,89,65,75,83,73,68,72,77,69,81,84,65,72,83,76,83,72,77,69,81,84,65,72,83,76,83,72,68,89,79,65,78,83,72,70,85,65,89,83,78,86,76,83,73,65,66,83,74,68,85,69,65,78,83,75,70,72,65,77]
lstNumKey = []
for item in lst:
    lstNumKey.append(alphabet.find(chr(item)))
print(lstNumKey)

for item in lst:
    print(chr(item))

lstOrg = ["B","J","I","U","W","J","L","N","N","Y","J","M","S","H","F","O","A","J","D","L","B","O","G","D","P","J","S","O","S","G","G","C","P","J","J","R","P","L","Q","H","L","W","C","N","F","D","I","L","N","K"]
lstNum = []
for item in lstOrg:
    lstNum.append(alphabet.find(item))
print(lstNum)

finalNums = []
i=0
while i < 50:
    finalNums.append(lstNum[i]+26-lstNumKey[i])
    i+=1
print(finalNums)

finalMessage = []
for item in finalNums:
   #finalMessage.append(chr(item))
    while item > 25:
        item -= 26
    finalMessage.append(alphabet[item])
   #print(alphabet[item])
    
    
    
    
print(finalMessage)