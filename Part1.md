# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:05:40 2021

@author: admin
"""
# Part 1: Software Development

## Board

In board.py:
>class Board:
>   def __init__(self,size,PlayerNumber):
>        self.size=size
>        self.PlayerNumber=PlayerNumber

I gave the panel some properties:size, playernumber.
I also define some functions, md(),bd() and pi(),to describe the game description, define the panel size, and describe the rules.
Here is the codes for generate the board:
>def bd(self):
        a1=[] #Define an empty list
        for i in range(self.size):
            a1.append([])
            for j in range(self.size):
                    a1[i].append(0) # Generates nested lists in empty lists
        a1[1][1]=1 #Player 1 is represented by the number 1
        a1[self.size-2][self.size-2]=2 #Player 2 is represented by the number 2
        for k in range(self.size):
            a1[k][0]=8
            a1[k][self.size-1]=8 
        for f in range(self.size):
            a1[0][f]=8
            a1[self.size-1][f]=8 #Build a wall, representing the wall with the number 8
        for g in range(self.size): #For aesthetics, traverse the list to print
            print(a1[g])
        return a1 #return the board

==In order to be beautiful and reduce the complexity of the algorithm, the number 8 is used to represent the wall, and the number 4 is used to represent the road being walked. Because if you use the symbol # to represent the wall, the output is hard to align.==

## Player, computer, human
The class computer and human are two children's classes,and player is the parent class of them.
In this class I define the player's ID and initial position.
>>class Player():
     def __init__(self,PlayerID,positionRow,positionCol):
        #super().__init__(size,PlayerNumber)
        self.PlayerID=PlayerID
        self.positionRow=positionRow
        self.positionRow=positionCol

The Computer and Human classes inherit directly from Player, so the attributes do the same.
In particular, in the Computer class, I added a function that randomly moves the computer.
>from player import Player
import random
class Computer(Player):
    def __init__(self,PlayerID,positionRow,positionCol):
        super().__init__(PlayerID,positionRow,positionCol)    
>    def mov(self):
        move_list=['R','L','U','D']
        moved=random.choice(move_list) #Select one at random from the list
        return moved
        
        
        
