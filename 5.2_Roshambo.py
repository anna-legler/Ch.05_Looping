'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import random
done = False
while not done:
    computer = random.randrange(1, 4)
    print("Welcome to Rock Paper Scissors!!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    player = float(input("Pick Rock Paper or Scissors: "))
    print()
    if player == 1:
        if computer == 1:
            print("You and the computer both chose rock. It's a tie!")
        elif computer == 2:
            print("You chose rock and the computer chose paper. You lost!")
        else:
            print("You chose rock and the computer chose scissors. You won!")
    elif player == 2:
        if computer == 1:
            print("You chose paper and the computer chose rock. You won!")
        elif computer == 2:
            print("You and the computer both chose paper. It's a tie!")
        else:
            print("You chose paper and the computer chose scissors. You lost!")
    elif player == 3:
        if computer == 1:
            print("You chose scissors and the computer chose rock. You lost!")
        elif computer == 2:
            print("You chose scissors and the computer chose paper. You won!")
        else:
            print("You and the computer both chose scissors. It's a tie!")
    else:
        done = True
    print()
print("Thanks for playing!")












