# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:20:21 2021

@author: admin
"""
from player import Player
class Human(Player):
    def __init__(self,size,PlayerNumber,PlayerID,positionRow,positionCol):
        super().__init__(size,PlayerNumber,PlayerID,positionRow,positionCol)

        
