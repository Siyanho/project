# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:05:40 2021

@author: admin
"""
# Part 1: Software Development
"""
First of all, I create four classes: board,player,computer,human.
The class computer and human are two children's classes,and player is the parent class of them.
"""
## Board

In board.py:
>class Board:
>   def __init__(self,size,PlayerNumber):
>        self.size=size
>        self.PlayerNumber=PlayerNumber
I gave the panel some properties:size, playernumber.
I also define some functions, md(),bd() and pi(),to describe the game description, define the panel size, and describe the rules.
