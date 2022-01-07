#Part1 Siyan Huo bm21725@bristol.ac.uk
'''
define the Player class
'''

#CLASS2
class Player():
    #Defining basic properties
    def __init__(self,PlayerID,positionRow,positionCol):
        self.PlayerID=PlayerID
        self.positionRow=positionRow
        self.positionRow=positionCol
    
    #Give some basic information about the player
    def pid(self):
        return self.PlayerID
    
    def posR(self):
        return self.positionRow
    
    def posC(self):
        return self.positionCol
