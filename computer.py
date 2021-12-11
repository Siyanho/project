# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:07:53 2021

@author: admin
"""
from player import Player
class Computer(Player):
    def __init__(self,size,PlayerNumber,PlayerID,positionRow,positionCol):
        super().__init__(size,PlayerNumber)
        self.PlayerID=PlayerID
        self.positionRow=positionRow
        self.positionRow=positionCol
        b=Board.bd()
        
            
        
