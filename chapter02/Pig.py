# this is a program for a dice game called pig, developed by Ryan Kinney, Will Sabin, Chris A

import random

point = 0
p1s = 0
p2s = 0
win = 25
play = "1"

def main():
    global total, point, p1s, p2s, win, player_1, player_2, play
    welcome()
    get_player_names()
    while p1s < win and play == "1":
        scoreboard()
        print("It is", player_1,"'s turn")
        roll_dice()



def welcome():

   print('''
     _____ _____ _____
    |  __ \_   _/ ____|
    | |__) || || |  __
    |  ___/ | || | |_ |
    | |    _| || |__| |
    |_|   |_____\_____|     
   
Welcome to Pig! You need 100 points to win.                                                          
   ''')


def roll_dice():
    global point
    input("Press Enter to roll the dice...")  #not doing anything with the input, we're just using it to pause the game

    die1 = random.randrange(1, 7)

    point = die1

    print()
    print(" +---+")
    print(" |", point, "|")
    print(" +---+")
    print()


    if point == 1:
       point = 0
       p1s = p1s + point
       print("You busted")
       play = "2"
    else:
       p1s = p1s + point
       print("You have", p1s,"points")
       if p1s != win and p2s < win:
           play = input("Press Enter to roll again, Type h to pass: ")
           if input == "":
           else:
               play = 2

        return point
def play_turn():
    global 
    while p2s < win and play == "2":
    print("It is", player_2,"'s turn")
    roll_dice()
    if point == 1:
        point = 0
        p2s = p2s + point
        print("You busted")
        play = "1"
    else:
        p2s = p2s + point
        print("You have", p2s ,"points")
        if p2s != win:
            play = input("Press Enter to play again, Type h to pass: ")
            if input == "":
                roll_dice()
            else:
                play = 1




def get_player_names():
   global player_1
   global player_2

   player_1 = input("Enter the name of player 1: ")
   player_2 = input("Enter the name of player 2: ")


def scoreboard():
   global p1s, p2s, player_1, player_2
   print("")
   print("Score Board")
   print("-----------")
   print(player_1, "=", p1s)
   print(player_2, "=", p2s)
   print("")


def winner():
   global p1s, p2s, player_1, player_2, win
   if p1s >= win:
       print("")
       print("Congrats", player_1, "You win" )
   if p2s >= win:
       print("Congrats", player_2, "You win" )

main()

