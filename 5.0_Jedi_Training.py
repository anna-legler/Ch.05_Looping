  # Sign your name: Anna Legler
import random
'''
 1. Make the following program work.
   '''
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total += x
# print("The total is:", total)


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(2, 101, 2):
#     print(i)


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# countdown = 10
# while countdown >= 0:
#     print(countdown)
#     countdown -= 1
# print("BLAST OFF!!")


'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# print(random.randrange(1, 11))


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
totalPos = 0
totalNeg = 0
totalZero = 0
for i in range(7):
    num = int(input("Type a number "))
    total += num
    if num > 0:
        totalPos += 1
    elif num < 0:
        totalNeg += 1
    else:
        totalZero += 1
print("The total is", total)
print("You typed", totalPos, "Positive numbers,", totalNeg, "negative numbers, and", totalZero, "zeros.")
