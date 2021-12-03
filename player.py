#CLASS2
from board import Board
class Player(Board):
    def __init__(self,size,PlayerNumber,PlayerID,positionRow,positionCol):
        super().__init__(size,PlayerNumber)
        self.PlayerID=PlayerID
        self.positionRow=positionRow
        self.positionRow=positionCol
        
    def pid(self):
        return self.PlayerID
    
    def posR(self):
        return self.positionRow
    
    def posC(self):
        return self.positionCol
