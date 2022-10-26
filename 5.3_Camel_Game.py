'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
totalMilesTraveled = 0
water = 3
thirst = 0
camelTiredness = 0
nativesTraveled = -15
nativesDistance = 15
milesTraveled = 0
desertDistance = random.randrange(150, 251)
dead = False
done = False

while not done:
    print("Welcome to Camel!")
    print()
    print("You have stolen a camel to make your way across the desert.")
    print("The natives want their camel back and are hunting you down!")
    print("Survive your desert trek and outrun the natives.")
    print()

    while not dead:
        if totalMilesTraveled >= 200:
            break
        oasis = random.randrange(1, 21)
        if oasis == 1:
            print("You found an oasis!")
            print("Your water has been refilled and your camel is happy.")
            print()
            water += 3
            thirst = 0
            camelTiredness = 0

        print("-----------------------------------------")
        print("A. Drink from canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Rest for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        userInput = input("What is your choice? ")
        print()
        # Allows the player to quit
        if userInput.lower() == "q":
            dead = True
            done = True
        # Status check
        elif userInput.lower() == "e":
            print("Drinks in canteen:", water)
            print("Miles traveled:", totalMilesTraveled)
            print("The natives are", nativesDistance, "miles behind you.")
            print()
        # Drink from canteen
        elif userInput.lower() == "a":
            if water > 0:
                water -= 1
                thirst = 0
                print("You drank some water.")
                print()
            else:
                print("You are out of water.")
                print()
        # Ahead moderate speed
        elif userInput.lower() == "b":
            milesTraveled = random.randrange(5, 13)
            print("You traveled", milesTraveled, "miles.")
            print()
            totalMilesTraveled += milesTraveled
            camelTiredness += 1
            thirst += 1
            nativesTraveled += random.randrange(7, 15)
            nativesDistance = totalMilesTraveled - nativesTraveled
        # Ahead full speed
        elif userInput.lower() == "c":
            milesTraveled = random.randrange(10, 21)
            print("You traveled", milesTraveled, "miles.")
            print()
            totalMilesTraveled += milesTraveled
            camelTiredness += random.randrange(1, 5)
            thirst += 1
            nativesTraveled += random.randrange(8, 19)
            nativesDistance = totalMilesTraveled - nativesTraveled
        # Rest for the night
        elif userInput.lower() == "d":
            print("Your camel is happy.")
            camelTiredness = 0
            nativesTraveled += random.randrange(7, 15)
            nativesDistance = totalMilesTraveled - nativesTraveled
        else:
            print("That is not an option.")
            print()
            continue

        # If the player dies of thirst the dead loop will break
        if thirst == 6:
            dead = True
        # You are thirsty
        elif thirst >= 4:
            print("You are thirsty.")
            print()
        # If the players camel dies the dead loop will break
        if camelTiredness == 8:
            dead = True
            break
        # Your camel is getting tired
        elif camelTiredness >= 5:
            print("Your camel is getting tired.")
            print()
        # If the natives catch up to the player the dead loop will break
        if nativesDistance <= 0:
            dead = True
            break
        # The natives are getting close
        elif nativesDistance < 15:
            print("The natives are getting close.")
            print()
        # You made it across the dessert
        if totalMilesTraveled >= desertDistance:
            dead = True
            break

    # You died of thirst GAME OVER
    if thirst == 6:
        print()
        print("You died of thirst!")
        print("GAME OVER")
        print()
        playAgain = input("Would you like to play again? (Y/N) ")
        # Lets player play again
        if playAgain.lower() == "y":
            totalMilesTraveled = 0
            water = 3
            thirst = 0
            camelTiredness = 0
            nativesTraveled = -15
            nativesDistance = 15
            milesTraveled = 0
            desertDistance = random.randrange(150, 251)
            dead = False
        else:
            done = True
    # Your camel is dead GAME OVER
    elif camelTiredness == 8:
        print()
        print("Your camel is dead.")
        print("GAME OVER")
        print()
        playAgain = input("Would you like to play again? (Y/N) ")
        # Lets player play again
        if playAgain.lower() == "y":
            totalMilesTraveled = 0
            water = 3
            thirst = 0
            camelTiredness = 0
            nativesTraveled = -15
            nativesDistance = 15
            milesTraveled = 0
            desertDistance = random.randrange(150, 251)
            dead = False
        else:
            done = True
    # The natives caught you
    elif nativesDistance <= 0:
        print()
        print("The natives caught up to you.")
        print("GAME OVER")
        print()
        playAgain = input("Would you like to play again? (Y/N) ")
        # Lets player play again
        if playAgain.lower() == "y":
            totalMilesTraveled = 0
            water = 3
            thirst = 0
            camelTiredness = 0
            nativesTraveled = -15
            nativesDistance = 15
            milesTraveled = 0
            desertDistance = random.randrange(150, 251)
            dead = False
        else:
            done = True
    # YOU WON
    elif totalMilesTraveled >= desertDistance:
        print()
        print("Congratulations! You made it across the desert!")
        print("YOU WIN")
        print()
        playAgain = input("Would you like to play again? (Y/N) ")
        # Allows player to play again
        if playAgain.lower() == "y":
            print()
            totalMilesTraveled = 0
            water = 3
            thirst = 0
            camelTiredness = 0
            nativesTraveled = -15
            nativesDistance = 15
            milesTraveled = 0
            desertDistance = random.randrange(150, 251)
            dead = False
        else:
            done = True
print()
print("Thanks for playing!")
