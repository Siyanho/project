#MAIN
from board import Board
from player import Player
m=int(input(' Enter the board size:'))
print(' Board of size ('+str(m)+'x'+str(m)+') created with default locations:')
board1=Board(m,2)
b=board1.bd()
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
    if m1!='R' or m1!='L' or m1!='U' or m1!='D':
        print('Please enter R,L,U or D !')
    if m1=='R':
        b[t1][r1]=4
        p1=b[t1][r1+1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1][r1+1]=1
            print(b)
        else:
            x=0
            print('The game is over!')
        r1+=1
    if m1=='L':
        b[t1][r1]=4
        p1=b[t1][r1-1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1][r1-1]=1
            print(b)
        else:
            x=0
            print('The game is over!')
        r1-=1
    if m1=='U':
        b[t1][r1]=4
        p1=b[t1-1][r1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1-1][r1]=1
            print(b)
        else:
            x=0
            print('The game is over!')
        t1-=1
    if m1=='D':
        b[t1][r1]=4
        p1=b[t1+1][r1]
        if p1!=8 and p1!=2 and p1!=4:
            b[t1+1][r1]=1
            print(b)
        else:
            x=0
            print('The game is over!')
        t1+=1

    m2=input('Enter the move of player 2: ')
    if m2!='R' or m2!='L' or m2!='U' or m2!='D':
        print('Please enter R,L,U or D !')
    if m2=='R':
        b[t2][r2]=4
        p2=b[t2][r2+1]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2][r2+1]=2
            print(b)
        else:
            x=0
            print('The game is over!')
        r2+=1
    if m2=='L':
        b[t2][r2]=4
        p2=b[t2][r2-1]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2][r2-1]=2
            print(b)
        else:
            x=0
            print('The game is over!')
        r2-=1
    if m2=='U':
        b[t2][r2]=4
        p2=b[t2-1][r2]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2-1][r2]=2
            print(b)
        else:
            x=0
            print('The game is over!')
        t2-=1
    if m2=='D':
        b[t2][r2]=4
        p2=b[t2+1][r2]
        if p2!=8 and p2!=1 and p2!=4:
            b[t2+1][r2]=2
            print(b)
        else:
            x=0
            print('The game is over!')
        t2+=1
