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

If user chooses 1, There is second while loop that loop until user chooses B. Program goes to weapon_menu function
and ask user to choose a weapon then return it to the main function. If the function returns B, then break second
while loop and back to top of the first while loop. Program continues if user chooses any weapon, then it goes to
comp_weapon function, which choose a weapon for computer randomly then return that result to the main function.
Finally, compare the weapons what user and computer chose, then return 0 when tie, 1 when user wins, and 2 when
computer wins. And increment the score of winner. If the result it a tie, no points are given to both player and
computer.

If user chooses 2, go to display_scores function which displays the current score. Then go back to the top of
while loop

If user chooses 3, displays final score of the games then quit the program.
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
        elif user_choice == "B":        #Return B to the main
            return "B"
        elif user_choice != "R" or "P" or "S" or "B":   #Go back to the top of this while loop
            print("Invalid input")
            continue


def find_winner(player, comp):  # Find winner and return 0 when tie,
                                # return 1 when player wins, and return 2 when comp wins
    if player == comp:
        print("Tie")
        return "0"
    elif (player == "R" and comp == "S") or (player == "P" and comp == "R") or (player == "S" and comp == "P"):
        print("You win")
        return "1"
    else:
        print("Computer wins")
        return "2"


def comp_weapon():  # Comp choose a weapon randomly
    random_comp = random.randint(1, 3)

    if random_comp == 1:
        print("Computer chose Rock")
        return "R"
    elif random_comp == 2:
        print("Computer chose Paper")
        return "P"
    elif random_comp == 3:
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

        if menu_num == "1":                 #Play the game
            while True:
                player = weapon_menu()      #What player chose
                if player == "B":
                    break
                comp = comp_weapon()        #What comp chose
                game_winner = find_winner(player, comp)     #Get return from find_winner func

                if game_winner == "0":      #Give 1 point to a winner. No points if its tie
                    continue
                elif game_winner == "1":
                    player_score += 1
                    continue
                elif game_winner == "2":
                    comp_score += 1
                    continue

        elif menu_num == "2":              #Display current score
            player = str(player_score)
            comp = str(comp_score)
            display_scores(player, comp)
            continue

        elif menu_num == "3":              # Print final score and quit the program
            print("Final Score: \nPlayer = " + str(player_score) + "\nComputer = "
                  + str(comp_score))
            return

        else:
            print("Invalid. Choose number between 1-3")
            continue

main()