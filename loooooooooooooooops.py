# -*- coding: utf-8 -*-
"""
Yana Sang
GenCyber 2016
Python: Intro to Loops
July 7, 2016

"""
import random 

#While Loops
"""
myInt = 465
while myInt > 400:
    myInt -= 5    
    print(myInt)
""" 

"""
GUESS THE NUMBER GAME
guess = int(input("Want to play a game? Guess the number! : "))
number = random.randint(0,100)
while (number != guess):
    if (guess > number):
        print("Sorry, your guess is too big.")
    else:
        print("Sorry, your guess is too small.")
    guess = int(input("Guess again! : "))
    
print("Congrats! You guessed the number! The number was", number)
"""
"""
GUESS THE PASSWORD GAME
Write a while loop that checks if a string (called password) 
is the same as the guessed password
The actual password should be 2 letters, ALL CAPS. 
You can set your own password in the program. 
The loop should let the guesser know if the password is wrong or not.
#START OF CODE
passGuess = input("Please enter the password : ")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = random.choice(letters)+random.choice(letters)
attempt = 5
while (passGuess != password and attempt > 0):
    print("Error! Incorrect password.")
    if (passGuess.find(password[0]) != -1 or passGuess.find(password[1]) != -1):
        print("One letter is correct.")
    else:
        print("No letters are correct.")
    print(attempt, "attempts left.")    
    passGuess = input("Try again : ")
    attempt = attempt - 1
if (attempt == 0):
    print ("FAILED to enter correct password in given attempts. Access DENIED.")
    print("The password was:", password)
else:
    print ("Password correct. Access granted.")
"""    
     
#FOR LOOPS
"""
EXAMPLES:
for i in range(1,11): #i is NOT previously designed 
    print(i)
string = "I got this feeling, inside my bones"
for char in string:
    print(char)
    
def ascii_to_eight_bit(letter):
    num = ord(letter)
    bitstring = ""
    for i in range(8):
        print(num)
        if(num%2 == 0):
            bitstring = '0'+bitstring
            print('0')
        else:
            bitstring = '1'+bitstring
            print('1')
        num = num // 2
    return bitstring
    
print(ascii_to_eight_bit('S'))
"""
#EXERCISES
"""
Write a function to check whether a password follows these rules:
-Must be at least 6 characters long
-Must contain at least one capital letter
-Must contain at least one lowercase letter
(Lots of conditionals)
Use FOR LOOPS!
Remember: 
for char in string --> will allow you to loop through each character in a string
len(string) gives you the length of the string
ASCII table capital/lowercase
"""

def valid_pass (givenPass):
    string = givenPass
    length = False
    capital = False
    lowercase = False
    if (len(givenPass) >= 6):
        length = True
    for char in string:
        if (ord(char) >=97 and ord(char)<=122):
            lowercase = True
        if (ord(char) >= 65 and ord(char)<=90):
            capital = True
    if (length and capital and lowercase):
        print("Password mee ts all requirements.")        
        return True
    else:
        print("Password does not meet all requirements.")
        if (not length):
            print("--> Password is not long enough.")
        if (not capital):
            print("--> Password does not have at least one capital letter.")
        if (not lowercase):
            print("--> Password does not have at least one lowercase letter.")
        return False
    
givenPass = input("Enter your password : ")
print(valid_pass(givenPass))
        

            
    
    
    
    
    
    
    
    