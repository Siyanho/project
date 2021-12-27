#MAIN
from board import Board
#from player import Player
from human import Human
#define the size of the board
from computer import Computer
import sys
m=int(input(' Enter the board size:'))
if m>3:
   print(' Board of size ('+str(m)+'x'+str(m)+') created with default locations:')
   board1=Board(m,2)
   b=board1.bd()

else:
   print('Create a game board of size m*m (m >3)!!!')
   sys.exit()
print('======================')
board1.pi()
print('======================')
print('Method is as following:')
board1.md()
    
player1=Human(m,2,1,1,1)
player2=Human(m,2,2,m-1,m-1)
computer1=Computer(m,2,2,m-1,m-1)

x=1
t1=1
r1=1
p1=b[t1][r1]
t2=m-2
r2=m-2
p2=b[t2][r2]

#choose if wanna move simultaneously
print('                               ')
print('===============================')
print('Please choose your opponent: Human or Computer?')
anwser2=input('please enter H or C (Capital letters):')
if anwser2=='H':
    print('Do you wanna move simultaneously?')
    anwser1=input('please enter Y or N:')
    #Move asynchronously
    if anwser1=='N':
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
                    print('The game is over!Player2 is the winner!')
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


if anwser2=='C':
      print('Please choose an Ordinary or Smart computer.') 
      answer3=input('please enter O or S(capital letters):')
      if answer3=='O':
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
#samrt computer                
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
            
            
            if b[t2][r2+1]==8 and b[t2][r2+1]==1 and b[t2][r2+1]==4 and b[t2+1][r2]==8 and b[t2+1][r2]==1 and b[t2+1][r2]==4 and b[t2-1][r2]==8 and b[t2-1][r2]==1 and b[t2-1][r2]==4 and b[t2][r2-1]==8 and b[t2][r2-1]==1 and b[t2][r2-1]==4:
                   x=0
                   print('The game is over!You are the winner!')
                   break
            
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
                       x2=1
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
        

       


    
