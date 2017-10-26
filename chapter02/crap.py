# craps.py
#
# This program simulates the dice game craps. The user starts with $100 and is allowed to bet on the roll of two
# six-sided dice:
#
#  - A roll of 7 or 11 on the opening throw results in a win
#  - A roll of 2, 3, or 12 on the opening throw results in a loss
#  - A roll of anything else means the user has to re-roll the dice until that same number is rolled (a win) or a 7 is
#    rolled (a loss)
#
# A win pays whatever amount was bet. A loss takes the amount bet. The user can continue to play until he/she is out of
# money.
#
# by Mr. Ciccolo

import random


def main():
    display_welcome()
    global winnings, bet
    winnings = 100
    bet = 0

    play_again = True
    while play_again:
        bet = place_bet()

        total = roll_dice()
        if total == 7 or total == 11:
            print("You win!")
            winnings = winnings + bet
            print("You now have $", winnings, sep="")
        elif total == 2 or total == 3 or total == 12:
            print("You lose!")
            winnings = winnings - bet
            print("You now have $", winnings, sep="")
        else:
            re_roll(total)

        print() # Blank line for spacing
        if winnings < 5:
            print("You don't have enough money to play again, better luck next time.")
            play_again = False
        else:
            play_again = (input("Press enter to play another round or type 'N' to quit ") == "")
            clear_screen()


def clear_screen():
    for i in range(20):
        print()


def display_welcome():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                              $")
    print("$ Welcome to the Computer Science Craps Table! $")
    print("$                                              $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()

def place_bet():
    raw_bet = eval(input("You have $%s. What would you like to bet? ($5-$%s)" % (winnings, winnings)))

    #here we need to validate raw_bet
    if raw_bet < 5:
        print("The minimum is $5 so that's what we will use.")
        raw_bet = 5
    elif raw_bet > winnings:
        print("The maximum bet is your", winnings, "that is what we will use.")
        raw_bet = winnings

    return raw_bet


def roll_dice():
    input("Press Enter to roll the dice...") # We don't do anything with the input, we're just using it to pause the game

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    total = die1 + die2

    print()
    print(" +---+   +---+")
    print(" |", die1, "| + |", die2, "| =", total)
    print(" +---+   +---+")
    print()

    return total


def re_roll(point):
    global winnings, bet

    print("You have to keep rolling until you get another", point)
    print() # Blank line for spacing

    total = roll_dice()
    while total != point and total != 7:
        total = roll_dice()

    if total == point:
        print("You win!")
        winnings = winnings + bet
        print("You now have $", winnings, sep="")
    else:
        print("You lose!")
        winnings = winnings - bet
        print("You now have $", winnings, sep="")


main()
