#CLASS1
import numpy as np
class Board:
    def __init__(self,size,PlayerNumber):
        self.size=size
        self.PlayerNumber=PlayerNumber
    
    def md(self):
        print('Hello! Welcome!')
        print('The number 8 represents the wall,')
        print('the numbers 1 and 2 represent the two players, ')
        print('the number 0 represents the place that can be walked,')
        print('and the number 4 represents the place that cannot be walked because it has already been walked.')
        print('=======How to manage it?==========')
        print('The two players are moving in turns on a grid board that is surrounded by walls.  ')
        print('A player can move in four directions (up, down, left, right). ')
        print('NOTE:Enter uppercase letters U,D,L, and R.')
        print('As a player moves, it leaves a trail on the spaces it has traversed, which acts as a wall.')
        print('The game ends if at least one player crashes into the wall, another player or previously visited cell. ')
        print('The player who survives the longest win.  ')
        
    def bd(self):
        a1=[]
        for i in range(self.size):
            a1.append([])
            for j in range(self.size):
                    a1[i].append(0)  
        a1[1][1]=1
        a1[self.size-2][self.size-2]=2
        for k in range(self.size):
            a1[k][0]=8
            a1[k][self.size-1]=8
        for f in range(self.size):
            a1[0][f]=8
            a1[self.size-1][f]=8
        for g in range(self.size):
            print(a1[g])
        return a1
        
    def pi(self):
        print('There are '+str(self.PlayerNumber)+' players totally.')
