# Part1 Siyan Huo bm21725@bristol.ac.uk
"""
define the Human class
a subclass of the Player class
"""
from player import Player
class Human(Player):
    def __init__(self,PlayerID,positionRow,positionCol):
        #Inherit player properties
        super().__init__(PlayerID,positionRow,positionCol)

        
