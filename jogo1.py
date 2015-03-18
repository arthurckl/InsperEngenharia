# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:17:13 2015

@author: Arthur
"""

import random
a = 0    #pontos do computador
b = 0    #pontos do usuário
A = ["rock","paper", "scissors", "lizard", "spock"]

print ("Welcome!Let´s start! rock wins scissors, scissors  wins paper and paper wins rock. Spock wins rock and scissors, lizard wins spock and paper, spock looses paper and lizard, lizard looses rock and scissors")
     
computer_choice = random.choice(A)

while a!= 3 or b!=3:
    user_choice = str(input("Choose between rock, paper, scissors, lizard and spock: "))
    
    computer_choice = random.choice(A)
    if a == 2 and b == 1:
        a = a - 2 
        b = b -1 
    elif a == 1 and b == 2:
        a = a - 1 
        b = b - 2 
    elif a == 1 and b == 1:
        a = a - 1
        b = b - 1
    elif a == 3 and b == 0:
        print ("I won the game,play again") 
    elif a==0 and b == 3:
        print ("You won the game!!Play again")
    elif user_choice == "rock" and computer_choice == "rock":
        print ("It's a draw") 
    elif user_choice == "scissors" and computer_choice == "scissors":
        print ("It's a draw")
    elif user_choice == "paper" and computer_choice == "paper":
        print ("It's a draw")
    elif user_choice == "spock" and computer_choice == "spock":
        print ("It's a draw")
        
    elif user_choice== "lizard" and computer_choice == "lizard":
        print ("It's a draw")  
    elif user_choice == "rock" and computer_choice == "paper":
        print ("I won")  
        a += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print ("You won")
        b += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print ("You won")
        b += 1
    elif user_choice == "paper" and computer_choice == "scissors":
        print ("I won")
        a += 1
    elif user_choice == "lizard" and computer_choice == "paper":
        print ("You won")
        b += 1
    elif user_choice == "paper" and computer_choice == "lizard":
        print ("I won")
        a += 1
    elif user_choice == "spock" and computer_choice == "paper":
        print ("I won")
        a += 1
    elif user_choice == "paper" and computer_choice == "spock":
        print ("You won")  
        b += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print ("You won") 
        b += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print ("I won")
        a += 1
    elif user_choice == "scissors" and computer_choice == "spock":
        print ("I won")
        a += 1
    elif user_choice == "spock" and computer_choice == "scissors":
        print ("You won") 
        b += 1
    elif user_choice == "scissors" and computer_choice == "lizard":
        print ("You won")
        b += 1
    elif user_choice == "lizard" and computer_choice == "scissors":
        print ("I won")
        a += 1
    elif user_choice == "rock" and computer_choice == "spock":
        print ("I won")
        a += 1
    elif user_choice == "spock" and computer_choice == "rock":
        print ("You won")
        b += 1
    elif user_choice == "rock" and computer_choice == "lizard":
        print ("You won")
        b += 1
    elif user_choice == "lizard" and computer_choice == "rock":
        print ("I won")  
        a +=1
    elif user_choice == "lizard" and computer_choice == "spock":
        print ("You won")
        b += 1
    elif user_choice == "spock" and computer_choice == "lizard":
        print ("I won")
        a += 1
    else:
        print ("try again")
        