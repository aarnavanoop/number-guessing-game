import random

#Assign the random number to a variable
RandomNumber = str(random.randrange(0,11))

#Ask user to guess the number
UserGuess = input("Hi There! Please enter a number to guess what the correct one is: ")

#If number is wrong keep within the loop, asking them to guess again
while(UserGuess != RandomNumber):
    print("Oops! Wrong Number please guess again ")
    UserGuess = input("Please try again, what number could it be? ")

#If number is correct, congratulate them
print("Congrats you guessed the number! It was " + (RandomNumber))
