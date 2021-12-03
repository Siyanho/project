# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:01:40 2021

@author: admin
"""

#num_list = [ [0] * 5 for i in range(2)]
#print(num_list)


#import numpy
#num_list = numpy.zeros((5,5))
#num_list[0]='#'
#num_list[:,0]='#'
#print(num_list)


# =============================================================================
# m=5
# print('#'*m)
# i=1
# while i<=m-2:
#     print('#'+' '*(m-2)+'#')
#     i+=1
# print('#'*m)
#       
# def bd(n):
#     print('#'*n)
#     i=1
#     while i<=n-2:
#         print('#'+' '*(n-2)+'#')
#         i+=1
#     print('#'*n)
#           
# n=int(input(' Enter the board size'))
# bd(n)
# 
# def bd(size):
#         print('#'*(size*2+3))
#         print('#'+'1'+'|'+' |'*(size-1)+' #')
#         i=1
#         while i<=(size-1):
#             print('#'+' |'*size+' #')
#             i+=1
#         print('#'+' |'*(size-1)+' |2#')
#         print('#'*(size*2+3))
#           
# m=int(input(' Enter the board size'))
# bd(m)

import numpy as np
import pandas as pd

def bd(size):
    a1=np.zeros((size,size))
    a1[0]=8
    a1[1][1]=1
    a1[size-2][size-2]=2
    for i in range(size):
        a1[i][0]=8
        a1[i][size-1]=8
    a1[size-1]=8
    return a1

m=int(input(' Enter the board size:'))
print(' Board of size ('+str(m)+'x'+str(m)+') created with default locations')
print(bd(m))

def player1(size,move1):
    t=1
    r=1
    b=bd(size)
    p1=b[t][r]
    if move1=='R':
        b[t][r]=4
        p1=b[t][r+1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t][r+1]=1
            print(b)
        else:
            #break
            print('The game is over!')
        r+=1
    if move1=='L':
        b[t][r]=4
        p1=b[t][r-1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t][r-1]=1
            print(b)
        else:
            #break
            print('The game is over!')
        r-=1
    if move1=='U':
        b[t][r]=4
        p1=b[t-1][r]
        if p1!=8 and p1!=2 and p1!=4:
            b[t-1][r]=1
            print(b)
        else:
            #break
            print('The game is over!')
        t-=1
    if move1=='D':
        b[t][r]=4
        p1=b[t+1][r]
        if p1!=8 and p1!=2 and p1!=4:
            b[t+1][r]=1
            print(b)
        else:
            #break
            print('The game is over!')
        t+=1
    
            
            
m1=input('Enter the move of player 1: ')
player1(m,m1)
            
class Board:
    def __init__(self,size):
        self.size=size
        
    def bd(self):
        a1=np.zeros((self.size,self.size))
        a1[0]=8
        a1[1][1]=1
        a1[self.size-2][self.size-2]=2
        for i in range(self.size):
            a1[i][0]=8
            a1[i][self.size-1]=8
        a1[self.size-1]=8
        print(a1)
          
m=int(input(' Enter the board size:'))
print(' Board of size ('+str(m)+'x'+str(m)+') created with default locations:')
board1=Board(m)
board1.bd()
            
        


