# Part 1: Software Development
"""
Created on Mon Dec 27 21:05:40 2021

@author: Siyan Huo bm21725@bristol.ac.uk
"""
There are 4 modes,please try each one.
Each time you make a selection, you should enter capital letters!
In normal computer mode(input 'O'), the computer may run itself into a dead end the first time, so you can try a few more times.
When running, please pay attention to the cursor position and do not type numbers or letters into the code!

## board.py

In board.py:

    '''python
    class Board:
       def __init__(self,size,PlayerNumber):
           self.size=size
           self.PlayerNumber=PlayerNumber
    '''

I gave the panel some properties:size, playernumber.
I also define some functions, md(),bd() and pi(),to describe the game description, define the panel size, and describe the rules.
Here is the codes for generate the board:

    '''python
    def bd(self):
            a1=[] #Define an empty list
            for i in range(self.size):
                a1.append([])
                for j in range(self.size):
                        a1[i].append(0) # Generates nested lists in empty lists
            a1[1][1]=1 #Player 1 is represented by the number 1
            a1[self.size-2][self.size-2]=2 #Player 2 is represented by the number 2
            for k in range(self.size):
                a1[k][0]=8
                a1[k][self.size-1]=8 
            for f in range(self.size):
                a1[0][f]=8
                a1[self.size-1][f]=8 #Build a wall, representing the wall with the number 8
            for g in range(self.size): #For aesthetics, traverse the list to print
                print(a1[g])
            return a1 #return the board
    '''

**NOTE**:In order to be beautiful and reduce the complexity of the algorithm, the number 8 is used to represent the wall, and the number 4 is used to represent the road being walked. Because if you use the symbol '#' to represent the wall, the output is hard to align.

## player.py , computer.py , human.py
The class computer and human are two children's classes,and player is the parent class of them.
In this class I define the player's ID and initial position.

    '''python
    >class Player():
         def __init__(self,PlayerID,positionRow,positionCol):
            #super().__init__(size,PlayerNumber)
            self.PlayerID=PlayerID
            self.positionRow=positionRow
            self.positionRow=positionCol
    '''

The Computer and Human classes inherit directly from Player, so the attributes do the same.
In particular, in the Computer class, I added a function that randomly moves the computer.

    '''python
    from player import Player
    import random
    class Computer(Player):
        def __init__(self,PlayerID,positionRow,positionCol):
            super().__init__(PlayerID,positionRow,positionCol)    
        def mov(self):
            move_list=['R','L','U','D']
            moved=random.choice(move_list) #Select one at random from the list
            return moved
    '''
 ## main.py

**The main.py section is the most important part of my algorithm, and the largest, with nearly 800 lines of code, so I'll just pick out the important parts and details.**

First, import the required libraries and classes:

     '''python
    from board import Board
    #from player import Player
    from human import Human

    from computer import Computer
    import sys
    '''
Give the player the right to define the board's size:

    '''python
    #define the size of the board
    m=int(input(' Enter the board size:'))
    if m>3:
       print(' Board of size ('+str(m)+'x'+str(m)+') created with default locations:')
       #Define an instance
       board1=Board(m,2)
       #Call the bd() function in Board
       b=board1.bd()
       
    #If the size defined by the player is less than 3, it will alert the player and automatically close the application
    else:
       print('Create a game board of size m*m (m >3)!!!')
       sys.exit()
    print('======================')
    #Print game instructions
    board1.pi() 
    print('======================')
    print('Method is as following:')
    board1.md()
    '''
Creating player Instances:

    '''python
    player1=Human(1,1,1)
    player2=Human(2,m-1,m-1)
    computer1=Computer(2,m-1,m-1)
    '''
The idea of mode selection is: first, let the player choose whether to play with people or computers; If he/she chooses to play with people, let he/she choose whether to move asynchronously or simultaneously; If he/she chooses to play with a computer, let he/she choose to play with a regular computer or a smart one.

I'll write the explanations of details in the following codes:

### 1.Player1 and Player2 move asynchronously:

    '''python
    print('Please choose your opponent: Human or Computer?')
    anwser2=input('please enter H or C (Capital letters):')
    #if player chooses to play with a human
    if anwser2=='H': 
        print('Do you wanna move simultaneously?')
        anwser1=input('please enter Y or N:')
        #Move asynchronously
        if anwser1=='N':
            #Here x=1 is used to control the players' loop below
            while x==1:
                m1=input('Enter the move of player 1: ')
                # must input capital letters
                if m1!='R' and m1!='L' and m1!='U' and m1!='D':
                    print('Please enter R,L,U or D !')
                #If the player1 chooses to move right
                if m1=='R':
                    b[t1][r1]=4 #The path traveled becomes the number 4
                    #Check to see if the path has been traveled, or if it has collided with another player.
                    p1=b[t1][r1+1] 
                    if p1!=8 and p1!=2 and p1!=4:
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
     #Player 2 also has the same codes as Player 1.
    '''
### 2.Player1 and Player2 move in synchronously:

    '''python
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
     #There are 16 possible combinations, all of which are similar to the code above.
    '''
    
### 3.Normal computer mode:

    '''python
    if anwser2=='C':
          print('Please choose an Ordinary or Smart computer.') 
          answer3=input('please enter O or S(capital letters):')
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
               #The other three cases have much the same code
     
               #computer's movement
                m2=computer1.mov() #Call the mov () function in computer.py
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
                  #The other three cases have much the same code
    '''

### 4.Smart computer module:

Player 1's movement is the same as before:

    '''python
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
    '''
        
Here are the codes for the smart computer's movement:

    '''python
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
                       #If the computer hits a dead end, the game ends and player1 wins
                       if (b[t2][r2+1]==8 or b[t2][r2+1]==1 or b[t2][r2+1]==4) and (b[t2+1][r2]==8 or b[t2+1][r2]==1 or b[t2+1][r2]==4) and (b[t2-1][r2]==8 or b[t2-1][r2]==1 or b[t2-1][r2]==4) and (b[t2][r2-1]==8 or b[t2][r2-1]==1 or b[t2][r2-1]==4):
                           x=0
                           x2=0
                           print('The game is over!You are the winner!')
                           break
                       #The other three cases have much the same code
    '''
