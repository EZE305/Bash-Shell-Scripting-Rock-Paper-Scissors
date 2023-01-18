#!/usr/bin/env python3
import random
def rock_paper_scissors():
    while True:
        play = input("Wanna play some Rock, Paper, Scissors? (y/n)")
        choices = ["r", "p", "s"]
        comp_choice = random.choice(choices)
        if play == "y":
            player_choice = input("What do you choose? 'Rock','Paper' or 'Scissors'").lower()
            if player_choice.startswith == comp_choice:
                print("The computer chose {} and so did you". format(comp_choice))
                print("Izza Tie, go again?")
            elif player_choice == "rock" and comp_choice == "scissors":
                print("The computer chose {} and you chose Rock". format(comp_choice))
                print("You win! Rock beats scissors.")
            elif player_choice == "paper" and comp_choice == "rock":
                print("The computer chose {} and you chose Paper". format(comp_choice))
                print("You win! Paper beats rock.")
            elif player_choice == "scissors" and comp_choice == "paper":
                print("The computer chose {} and you chose Scissors". format(comp_choice))
                print("You win! Scissors beat paper.")
            else:
                print("You lose! {} beats {}.".format(comp_choice, player_choice))   
        elif play == "n":
            print("Sorry to see you go :(")
            break
        else:
            print("Not Valid command")
            continue
        
rock_paper_scissors()


