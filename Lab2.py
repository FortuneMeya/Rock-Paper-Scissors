'''
Rock Paper Scissors Game

September 3rd, 2024

Fortune Meya
Yusuke Homma

In the main function, set player score and computer score as zero, and set blank string to substitute the result
of find_winner function later. Then start while loop that loop until 3 in main menu is selected. And come back to top
of the loop when user chose any other choices.

On the top of while loop, print main menu and ask uer to select number between 1-3 and displays invalid if
any other numbers or letters are chosen.

If user chose 1, There is second while loop that loop until user chooses B. Program goes to weapon_menu function
and ask user to choose a weapon then return it to the main function. If the function returns B, then break second
while loop and back to top of the first while loop. Program continues if user chooses any weapon, then it goes to
comp_weapon function, which choose a weapon for computer randomly then return that result to the main function.
Finally, compare the weapons what user and

'''

import random

def weapon_menu():  # User choose a weapon and return the weapon chosen.
    while True:
        print("Choose your weapon:")
        user_choice = str(input("R. Rock\nP. Paper\nS. Scissors\nB. Back\n"))

        if user_choice == "R":
            print("You chose Rock")
            return "R"
        elif user_choice == "P":
            print("You chose Paper")
            return "P"
        elif user_choice == "S":
            print("You chose Scissors")
            return "S"
        elif user_choice == "B":
            return "B"
        elif user_choice != "R" or "P" or "S" or "B":
            print("Invalid input")
            continue


def find_winner(player, comp):  # Find winner and return 0 when tie,
                                # return 1 when player wins, and return 2 when comp wins

    if player == "R" and comp == "R":  # User chose Rock
        print("Tie")
        return "0"
    elif player == "R" and comp == "P":
        print("Computer wins")
        return "2"
    elif player == "R" and comp == "S":
        print("You win")
        return "1"

    if player == "P" and comp == "R":  # User chose Paper
        print("You win")
        return "1"
    elif player == "P" and comp == "P":
        print("Tie")
        return "0"
    elif player == "P" and comp == "S":
        print("Computer wins")
        return "2"

    if player == "S" and comp == "R":  # User chose Scissors
        print("Computer wins")
        return "2"
    elif player == "S" and comp == "P":
        print("You win")
        return "1"
    elif player == "S" and comp == "S":
        print("Tie")
        return "0"


def comp_weapon():  # Comp choose a weapon randomly
    random_comp = random.choice(["R", "P", "S"])

    if random_comp == "R":
        print("Computer chose Rock")
        return "R"
    elif random_comp == "P":
        print("Computer chose Paper")
        return "P"
    elif random_comp == "S":
        print("Computer chose Scissors")
        return "S"


def display_scores(player, comp):  # Print how much player and comp won the game
    print("Player = " + player + "\nComputer = " + comp)


def main():
    player_score = 0    # How much player wins
    comp_score = 0      # How much computer wins
    game_winner = ""    # Substitute return from find_winner

    while True:
        print("RPS Menu: \n1. Play game \n2. Show score \n3. Quit")  # Displays menu

        menu_num = str(input())

        if menu_num == "1":
            while True:
                player = weapon_menu()
                if player == "B":
                    break
                comp = comp_weapon()
                game_winner = find_winner(player, comp)

                if game_winner == "0":
                    continue
                elif game_winner == "1":
                    player_score += 1
                    continue
                elif game_winner == "2":
                    comp_score += 1
                    continue

        elif menu_num == "2":
            player = str(player_score)
            comp = str(comp_score)
            display_scores(player, comp)
            continue

        elif menu_num == "3":
            print("Final Score: \nPlayer = " + str(player_score) + "\nComputer = " + str(
                comp_score))  # Print final score and quit the program
            return

        else:
            print("Choose number between 1-3")
            continue

main()


