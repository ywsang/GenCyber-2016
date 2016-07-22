# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:38:08 2016

@author: student
"""

from random import randint

class Pokemon:
    #defining traits of a Pokemon object
   #constructor
    def __init__(self, oriName, oriType, oriHp, oriMoves):
        self.name = oriName        
        self.type = oriType
        self.hp = oriHp
        self.cp = randint(1, 100)
        self.moves = oriMoves
        
    #fight function
    def battle(self, myMove, opponent, oppMove):
        #make my move and announce it
        print(self.name + " used " + myMove + ".")
        #opponent health - my attack damage
        opponent.hp-=(self.moves[myMove]*self.cp)
        print(opponent.name + " now has " + str(opponent.hp) + " HP left.")
        #check if they are alive
        if opponent.hp <= 0:
            print(opponent.name + " DIED.")
            print(self.name + " WINS!!!")
            return
        #make their move
        print(opponent.name + " used " + oppMove + "!!")
        #my health - opponent's attack damage
        self.hp-=(opponent.moves[oppMove]*opponent.cp)
        print(self.name + " now has " + str(self.hp) + " HP left.")
        #check if I am alive
        if self.hp <= 0:
            print(self.name + " DIED.")
            print(opponent.name + " WINS!!")
            return
        print("DRAW.")
       
#making a Pokemon object; SELF does not go in as a parameter
eevee_moves = {"Swift": 10, "Dig": 20}
vee = Pokemon("Eevee", "normal", 50, eevee_moves)

squirtle_moves = {"Squirt": 40, "Water Gun": 100}
squirt = Pokemon("Squirtle", "water", 50, squirtle_moves)

#poli = Pokemon("Poliwag", "water", 75)
#chary = Pokemon("Charmander", "fire", 100)
#pip = Pokemon("Piplup", "water", 111)

print("Vee's CP:", str(vee.cp))
print("Squirt's CP:", str(squirt.cp))
vee.battle("Dig", squirt, "Squirt")



    