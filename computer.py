#Part1 Siyan Huo bm21725@bristol.ac.uk
"""
Created on Sat Dec 11 14:07:53 2021

define the Computer class
a subclass of the Player class

@author: Siyan Huo
"""
from player import Player
import random
class Computer(Player):
    def __init__(self,PlayerID,positionRow,positionCol):
        #Inherit player properties
        super().__init__(PlayerID,positionRow,positionCol)
        
    #Define the movement of the computer   
    def mov(self):
        move_list=['R','L','U','D']
        #Select one at random from the list
        moved=random.choice(move_list)
        #retunr the movement of the computer
        return moved


        
            
        
