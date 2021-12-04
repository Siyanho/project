# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
        a1=np.zeros((self.size,self.size))
        a1[0]=8
        a1[1][1]=1
        a1[self.size-2][self.size-2]=2
        for i in range(self.size):
            a1[i][0]=8
            a1[i][self.size-1]=8
        a1[self.size-1]=8
        return a1
        
    def pi(self):
        print('There are '+str(self.PlayerNumber)+' players totally.')
        
        

#CLASS2    
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
    
#MAIN
import sys
m=int(input(' Enter the board size:'))
if m>3:
   print(' Board of size ('+str(m)+'x'+str(m)+') created with default locations:')
   board1=Board(m,2)
   b=board1.bd()
   print(b)
else:
   print('Create a game board of size m*m (m >3)!!!')
   sys.exit()
print('======================')
board1.pi()
print('======================')
print('Method is as following:')
board1.md()
    
player1=Player(m,2,1,1,1)
player2=Player(m,2,2,m-1,m-1)

x=1
t1=1
r1=1
p1=b[t1][r1]
t2=m-2
r2=m-2
p2=b[t2][r2]
while x==1:
    m1=input('Enter the move of player 1: ')
    if m1!='R' and m1!='L' and m1!='U' and m1!='D':
        print('ILLEGAL!!!Please enter R,L,U or D !')
        break
    if m1=='R':
        b[t1][r1]=4
        p1=b[t1][r1+1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1][r1+1]=1
            print(b)
        else:
            x=0
            print('The game is over!Player2 is the winner!')
            break
        r1+=1
    if m1=='L':
        b[t1][r1]=4
        p1=b[t1][r1-1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1][r1-1]=1
            print(b)
        else:
            x=0
            print('The game is over!Player2 is the winner!')
            break
        r1-=1
    if m1=='U':
        b[t1][r1]=4
        p1=b[t1-1][r1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1-1][r1]=1
            print(b)
        else:
            x=0
            print('The game is over!Player2 is the winner!')
            break
        t1-=1
    if m1=='D':
        b[t1][r1]=4
        p1=b[t1+1][r1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1+1][r1]=1
            print(b)
        else:
            x=0
            print('The game is over!Player2 is the winner!')
            break
        t1+=1
#上面第一部分循环的修改过了 还没有改变终止条件
    m2=input('Enter the move of player 2: ')
    if m2!='R' and m2!='L' and m2!='U' and m2!='D':
        print('ILLEGAL!!!Please enter R,L,U or D !')
    if m2=='R':
        b[t2][r2]=4
        p2=b[t2][r2+1]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2][r2+1]=2
            print(b)
        else:
            x=0
            print('The game is over!Player1 is the winner!')
            break
        r2+=1
    if m2=='L':
        b[t2][r2]=4
        p2=b[t2][r2-1]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2][r2-1]=2
            print(b)
        else:
            x=0
            print('The game is over!Player1 is the winner!')
            break
        r2-=1
    if m2=='U':
        b[t2][r2]=4
        p2=b[t2-1][r2]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2-1][r2]=2
            print(b)
        else:
            x=0
            print('The game is over!Player1 is the winner!')
            break
        t2-=1
    if m2=='D':
        b[t2][r2]=4
        p2=b[t2+1][r2]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2+1][r2]=2
            print(b)
        else:
            x=0
            print('The game is over!Player1 is the winner!')
            break
        t2+=1






    
# =============================================================================
#     def player1(self):
#         t=1
#         r=1
#         b=Board.bd(self.size)
#         p1=b[t][r]
#         if self.move1=='R':
#             b[t][r]=4
#             p1=b[t][r+1]
#             if p1!=8 and p1!=2 and p1!=4:
#                 b[t][r+1]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             r+=1
#         if self.move1=='L':
#             b[t][r]=4
#             p1=b[t][r-1]
#             if p1!=8 and p1!=2 and p1!=4:
#                 b[t][r-1]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             r-=1
#         if self.move1=='U':
#             b[t][r]=4
#             p1=b[t-1][r]
#             if p1!=8 and p1!=2 and p1!=4:
#                 b[t-1][r]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             t-=1
#         if self.move1=='D':
#             b[t][r]=4
#             p1=b[t+1][r]
#             if p1!=8 and p1!=2 and p1!=4:
#                 b[t+1][r]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             t+=1
#         
#     def player2(self):
#         t=1
#         r=1
#         b=Board.bd(self.size)
#         p2=b[t][r]
#         if self.move1=='R':
#             b[t][r]=4
#             p2=b[t][r+1]
#             if p2!=8 and p2!=1 and p2!=4:
#                 b[t][r+1]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             r+=1
#         if self.move1=='L':
#             b[t][r]=4
#             p2=b[t][r-1]
#             if p2!=8 and p2!=2 and p2!=4:
#                 b[t][r-1]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             r-=1
#         if self.move1=='U':
#             b[t][r]=4
#             p2=b[t-1][r]
#             if p2!=8 and p2!=1 and p2!=4:
#                 b[t-1][r]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             t-=1
#         if self.move1=='D':
#             b[t][r]=4
#             p2=b[t+1][r]
#             if p2!=8 and p2!=1 and p2!=4:
#                 b[t+1][r]=1
#                 print(b)
#             else:
#                 #break
#                 print('The game is over!')
#             t+=1
# =============================================================================
        
# =============================================================================
# m1=input('Enter the move of player 1: ')
# P1=Player(m,m1)
# print(P1.player1())
# 
# m2=input('Enter the move of player 2: ')
# P2=Player(m,m2)
# print(P2.player2())
# =============================================================================
            
        
