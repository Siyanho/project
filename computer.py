# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:07:53 2021

@author: admin
"""
from player import Player
import random
class Computer(Player):
    def __init__(self,size,PlayerNumber,PlayerID,positionRow,positionCol):
        super().__init__(size,PlayerNumber,PlayerID,positionRow,positionCol)
        
        
    def mov(self):
        move_list=['R','L','U','D']
        moved=random.choice(move_list)
        return moved

# =============================================================================
# computer1=Computer(5,2,2,4,4)       
# m2=computer1.mov()
# print(m2)
# =============================================================================
        
            
        
