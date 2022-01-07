#Part1 Siyan Huo bm21725@bristol.ac.uk
'''
The main code of the game.

There are 4 modes,please try each one.

Each time you make a selection, you should enter capital letters!

In normal computer mode, the computer may run itself into a dead end the first time, 
so you can try a few more times.

When running, please pay attention to the cursor position 
and do not type numbers or letters into the code!
'''

#MAIN
from board import Board
#from player import Player
from human import Human
from computer import Computer
import sys
#define the size of the board
m=int(input(' Enter the board size:'))
if m>3:
   print(' Board of size ('+str(m)+'x'+str(m)+') created with default locations:')
   board1=Board(m,2)
   b=board1.bd()
#size>3
else:
   print('Create a game board of size m*m (m >3)!!!')
   sys.exit()
print('======================')
board1.pi()
print('======================')
print('Method is as following:')
board1.md()

#Define the instances  
player1=Human(1,1,1)
player2=Human(2,m-1,m-1)
computer1=Computer(2,m-1,m-1)

#Define the initial positions
x=1
t1=1
r1=1
p1=b[t1][r1]
t2=m-2
r2=m-2
p2=b[t2][r2]

#Choose to play with people or computers
print('                               ')
print('===============================')
print('Please choose your opponent: Human or Computer?')
anwser2=input('please enter H or C (Capital letters):')
#if player chooses to play with a human
if anwser2=='H':
    #choose if wanna move simultaneously
    print('Do you wanna move simultaneously?')
    anwser1=input('please enter Y or N:')
    #Move asynchronously
    if anwser1=='N':
        while x==1:
            m1=input('Enter the move of player 1: ')
            if m1!='R' and m1!='L' and m1!='U' and m1!='D':
                print('Please enter R,L,U or D !')
            #If the player1 chooses to move right
            if m1=='R':
                #Update the status of the old position
                b[t1][r1]=4
                p1=b[t1][r1+1]
                #Check to see if the path has been traveled, or if it has collided with another player.
                #If you are not in the wrong place
                if p1!=8 and p1!=2 and p1!=4:
                    #update the status of the new position
                    b[t1][r1+1]=1
                    #Output the latest board
                    for v in range(m):
                        print(b[v])
                #If you hit a path you've already taken, or collide with another player, 
                #you jump out of the loop, announce winner, and the game is over
                else:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                r1+=1
            #When the player chooses to go in another direction, the code is much the same as above, with only a few details changed.
            if m1=='L':
                b[t1][r1]=4
                p1=b[t1][r1-1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1][r1-1]=1
                    for v in range(m):
                        print(b[v])
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
                    for v in range(m):
                        print(b[v])
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
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                t1+=1
        
            #Player 2 also has the same codes as Player 1.
            m2=input('Enter the move of player 2: ')
            if m2!='R' and m2!='L' and m2!='U' and m2!='D':
                print('Please enter R,L,U or D !')
            if m2=='R':
                b[t2][r2]=4
                p2=b[t2][r2+1]
                if p2!=8 and p2!=1 and p2!=4:
                    b[t2][r2+1]=2
                    for v in range(m):
                        print(b[v])
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
                    for v in range(m):
                        print(b[v])
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
                    for v in range(m):
                        print(b[v])
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
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                t2+=1
                
#move simultaneously
    if anwser1=='Y':
        while x==1:
             m1=input('Enter the move of player 1: ')
             m2=input('Enter the move of player 2: ')
             if (m1!='R' and m1!='L' and m1!='U' and m1!='D') or (m2!='R' and m2!='L' and m2!='U' and m2!='D'):
                print('Please enter R,L,U or D !')
    #1
    #In the first case, player1 and player2 both choose to go right
             if m1=='R' and m2=='R':
                b[t1][r1]=4
                p1=b[t1][r1+1]
                b[t2][r2]=4
                p2=b[t2][r2+1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1][r1+1]=1
                    b[t2][r2+1]=2
                    for v in range(m):
                        print(b[v])
                #Three possible game-ending scenarios:
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==t2 and (r1+1)==(r2+1):
                    x=0
                    print("Game ends in a tie!")
                    break
                r1+=1
                r2+=1
             if m1=='R' and m2=='L':
                b[t1][r1]=4
                p1=b[t1][r1+1]
                b[t2][r2]=4
                p2=b[t2][r2-1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                   b[t1][r1+1]=1
                   b[t2][r2-1]=2
                   for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==t2 and (r1+1)==(r2-1):
                    x=0
                    print("Game ends in a tie!")
                    break
                r1+=1
                r2-=1
             if m1=='R' and m2=='U':
                b[t1][r1]=4
                p1=b[t1][r1+1]
                b[t2][r2]=4
                p2=b[t2-1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                   b[t1][r1+1]=1
                   b[t2-1][r2]=2
                   for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==(t2-1) and (r1+1)==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                r1+=1
                t2-=1
             if m1=='R' and m2=='D':
                b[t1][r1]=4
                p1=b[t1][r1+1]
                b[t2][r2]=4
                p2=b[t2+1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                   b[t1][r1+1]=1
                   b[t2+1][r2]=2
                   for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==(t2+1) and (r1+1)==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                r1+=1
                t2+=1
    #2          
             if m1=='L' and m2=='R':
                b[t1][r1]=4
                p1=b[t1][r1-1]
                b[t2][r2]=4
                p2=b[t2][r2+1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1][r1-1]=1
                    b[t2][r2+1]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==t2 and (r1-1)==(r2+1):
                    x=0
                    print("Game ends in a tie!")
                    break
                r1-=1
                r2+=1
             if m1=='L' and m2=='L':
                b[t1][r1]=4
                p1=b[t1][r1-1]
                b[t2][r2]=4
                p2=b[t2][r2-1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1][r1-1]=1
                    b[t2][r2-1]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==t2 and (r1-1)==(r2-1):
                    x=0
                    print("Game ends in a tie!")
                    break
                r1-=1
                r2-=1
             if m1=='L' and m2=='U':
                b[t1][r1]=4
                p1=b[t1][r1-1]
                b[t2][r2]=4
                p2=b[t2-1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1][r1-1]=1
                    b[t2-1][r2]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==(t2-1) and (r1-1)==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                r1-=1
                t2-=1
             if m1=='L' and m2=='D':
                b[t1][r1]=4
                p1=b[t1][r1-1]
                b[t2][r2]=4
                p2=b[t2+1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1][r1-1]=1
                    b[t2+1][r2]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if t1==(t2+1) and (r1-1)==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                r1-=1
                t2+=1
    #3
             if m1=='U' and m2=='R':
                b[t1][r1]=4
                p1=b[t1-1][r1]
                b[t2][r2]=4
                p2=b[t2][r2+1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1-1][r1]=1
                    b[t2][r2+1]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1-1)==t2 and r1==(r2+1):
                    x=0
                    print("Game ends in a tie!")
                    break
                t1-=1
                r2+=1
             if m1=='U' and m2=='L':
                b[t1][r1]=4
                p1=b[t1-1][r1]
                b[t2][r2]=4
                p2=b[t2][r2-1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1-1][r1]=1
                    b[t2][r2-1]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1-1)==t2 and r1==(r2-1):
                    x=0
                    print("Game ends in a tie!")
                    break
                t1-=1
                r2-=1
             if m1=='U' and m2=='U':
                b[t1][r1]=4
                p1=b[t1-1][r1]
                b[t2][r2]=4
                p2=b[t2-1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1-1][r1]=1
                    b[t2-1][r2]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1-1)==(t2-1) and r1==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                t1-=1
                t2-=1
             if m1=='U' and m2=='D':
                b[t1][r1]=4
                p1=b[t1-1][r1]
                b[t2][r2]=4
                p2=b[t2+1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1-1][r1]=1
                    b[t2+1][r2]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1-1)==(t2+1) and r1==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                t1-=1
                t2+=1
    #4
             if m1=='D' and m2=='R':
                b[t1][r1]=4
                p1=b[t1+1][r1]
                b[t2][r2]=4
                p2=b[t2][r2+1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1+1][r1]=1
                    b[t2][r2+1]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1+1)==t2 and r1==(r2+1):
                    x=0
                    print("Game ends in a tie!")
                    break
                t1+=1
                r2+=1
             if m1=='D' and m2=='L':
                b[t1][r1]=4
                p1=b[t1+1][r1]
                b[t2][r2]=4
                p2=b[t2][r2-1]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1+1][r1]=1
                    b[t2][r2-1]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1+1)==t2 and r1==(r2-1):
                    x=0
                    print("Game ends in a tie!")
                    break
                t1+=1
                r2-=1
             if m1=='D' and m2=='U':
                b[t1][r1]=4
                p1=b[t1+1][r1]
                b[t2][r2]=4
                p2=b[t2-1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1+1][r1]=1
                    b[t2-1][r2]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1+1)==(t2-1) and r1==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                t1+=1
                t2-=1
             if m1=='D' and m2=='D':
                b[t1][r1]=4
                p1=b[t1+1][r1]
                b[t2][r2]=4
                p2=b[t2+1][r2]
                if p1!=8 and p1!=4 and p2!=8 and p2!=4 and p1!=2 and p2!=1 :
                    b[t1+1][r1]=1
                    b[t2+1][r2]=2
                    for v in range(m):
                        print(b[v])
                if p1==8 or p1==4:
                    x=0
                    print('The game is over!Player2 is the winner!')
                    break
                if p2==8 or p2==4:
                    x=0
                    print('The game is over!Player1 is the winner!')
                    break
                if (t1+1)==(t2+1) and r1==r2:
                    x=0
                    print("Game ends in a tie!")
                    break
                t1+=1
                t2+=1

#Play with computer
if anwser2=='C':
      print('===========================================')
      print('Please choose an Ordinary or Smart computer.') 
      answer3=input('please enter O or S(capital letters):')
#Normal computer
      if answer3=='O':
          while x==1:
            #Player1's  movement.
            m1=input('Enter the move of player 1: ')
            if m1!='R' and m1!='L' and m1!='U' and m1!='D':
                print('Please enter R,L,U or D !')
            if m1=='R':
                b[t1][r1]=4
                p1=b[t1][r1+1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1][r1+1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                r1+=1
            if m1=='L':
                b[t1][r1]=4
                p1=b[t1][r1-1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1][r1-1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                r1-=1
            if m1=='U':
                b[t1][r1]=4
                p1=b[t1-1][r1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1-1][r1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                t1-=1
            if m1=='D':
                b[t1][r1]=4
                p1=b[t1+1][r1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1+1][r1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                t1+=1
        #computer's movement
        #Call the mov () function in computer.py
            m2=computer1.mov()
            print('The computer choose:')
            print(m2)
            if m2=='R':
                b[t2][r2]=4
                p2=b[t2][r2+1]
                if p2!=8 and p2!=1 and p2!=4:
                    b[t2][r2+1]=2
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!You are the winner!')
                    break
                r2+=1
            if m2=='L':
                b[t2][r2]=4
                p2=b[t2][r2-1]
                if p2!=8 and p2!=1 and p2!=4:
                    b[t2][r2-1]=2
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!You are the winner!')
                    break
                r2-=1
            if m2=='U':
                b[t2][r2]=4
                p2=b[t2-1][r2]
                if p2!=8 and p2!=1 and p2!=4:
                    b[t2-1][r2]=2
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!You are the winner!')
                    break
                t2-=1
            if m2=='D':
                b[t2][r2]=4
                p2=b[t2+1][r2]
                if p2!=8 and p2!=1 and p2!=4:
                    b[t2+1][r2]=2
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!You are the winner!')
                    break
                t2+=1
#Samrt computer                
      if answer3=='S':
          while x==1:
            m1=input('Enter the move of player 1: ')
            if m1!='R' and m1!='L' and m1!='U' and m1!='D':
                print('Please enter R,L,U or D !')
            if m1=='R':
                b[t1][r1]=4
                p1=b[t1][r1+1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1][r1+1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                r1+=1
            if m1=='L':
                b[t1][r1]=4
                p1=b[t1][r1-1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1][r1-1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                r1-=1
            if m1=='U':
                b[t1][r1]=4
                p1=b[t1-1][r1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1-1][r1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                t1-=1
            if m1=='D':
                b[t1][r1]=4
                p1=b[t1+1][r1]
                if p1!=8 and p1!=2 and p1!=4:
                    b[t1+1][r1]=1
                    for v in range(m):
                        print(b[v])
                else:
                    x=0
                    print('The game is over!The computer is the winner!')
                    break
                t1+=1

#the movement of the smart computer            
#X2 =1 is used to control the computer's cycle.
#the computer chooses randomly until it finds a path to take; Or winding down a dead end automatically.            
            x2=1
            while x2==1:
                m2=computer1.mov()
                if m2=='R':
                   p2=b[t2][r2+1]
                   #if p2!=8 and p2!=1 and p2!=4:
                   if p2==0:
                       b[t2][r2]=4
                       x2=0
                       print('The computer choose:')
                       print(m2)
                       b[t2][r2+1]=2
                       for v in range(m):
                            print(b[v])
                       r2+=1
                   if (b[t2][r2+1]==8 or b[t2][r2+1]==1 or b[t2][r2+1]==4) and (b[t2+1][r2]==8 or b[t2+1][r2]==1 or b[t2+1][r2]==4) and (b[t2-1][r2]==8 or b[t2-1][r2]==1 or b[t2-1][r2]==4) and (b[t2][r2-1]==8 or b[t2][r2-1]==1 or b[t2][r2-1]==4):
                       x=0
                       x2=0
                       print('The game is over!You are the winner!')
                       break
                
                if m2=='L':
                   p2=b[t2][r2-1]
                   if p2!=8 and p2!=1 and p2!=4:
                       b[t2][r2]=4
                       x2=0
                       print('The computer choose:')
                       print(m2)
                       b[t2][r2-1]=2
                       for v in range(m):
                            print(b[v])
                       r2-=1
                   if (p2==8 or p2==1 or p2==4) and (b[t2+1][r2]==8 or b[t2+1][r2]==1 or b[t2+1][r2]==4) and (b[t2-1][r2]==8 or b[t2-1][r2]==1 or b[t2-1][r2]==4) and (b[t2][r2+1]==8 or b[t2][r2+1]==1 or b[t2][r2+1]==4):
                       x=0
                       x2=0
                       print('The game is over!You are the winner!')
                       break
                   
                if m2=='U':
                   p2=b[t2-1][r2]
                   if p2!=8 and p2!=1 and p2!=4:
                       b[t2][r2]=4
                       x2=0
                       print('The computer choose:')
                       print(m2)
                       b[t2-1][r2]=2
                       for v in range(m):
                            print(b[v])
                       t2-=1
 
                   if (p2==8 or p2==1 or p2==4) and (b[t2+1][r2]==8 or b[t2+1][r2]==1 or b[t2+1][r2]==4) and (b[t2][r2-1]==8 or b[t2][r2-1]==1 or b[t2][r2-1]==4) and (b[t2][r2+1]==8 or b[t2][r2+1]==1 or b[t2][r2+1]==4):
                        x=0
                        x2=0
                        print('The game is over!You are the winner!')
                        break
       
                if m2=='D':
                   p2=b[t2+1][r2]
                   if p2!=8 and p2!=1 and p2!=4:
                       b[t2][r2]=4
                       x2=0
                       print('The computer choose:')
                       print(m2)
                       b[t2+1][r2]=2
                       for v in range(m):
                             print(b[v])
                       t2+=1
                   if (p2==8 or p2==1 or p2==4) and (b[t2][r2-1]==8 or b[t2][r2-1]==1 or b[t2][r2-1]==4) and (b[t2-1][r2]==8 or b[t2-1][r2]==1 or b[t2-1][r2]==4) and (b[t2][r2+1]==8 or b[t2][r2+1]==1 or b[t2][r2+1]==4):
                       x=0
                       x2=0
                       print('The game is over!You are the winner!')
                       break
        

       


    
