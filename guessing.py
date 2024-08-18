import random

#create a function to check if the input is a valid integer
def check_if_digit(guess):
    while True:
        try:
            guess = int(guess)
            if guess >= 0:
                return guess
            else:
                guess = input("Please enter a valid positive integer: ")
        except ValueError:
            guess = input("Please enter a valid number: ")


#create a function to check if the user's guess is correct
def is_correct(num1, num2):
    while True:
        if num1 == num2:
            print("Congrats you guessed the number correctly! It was: " + str(random))
            break
        else:
            num1 = input("Wrong number! Please enter a new guess: ")
            num1 = check_if_digit(num1)

def main():
    #ask the user for a guess and assign that to a variable
    user_guess = input("What number am i? : ")

    #check if the user input is an integer
    user_guess = check_if_digit(user_guess)

    #assign the random number to be within the range of the user's number
    random_number = random.randint(1,100)

    is_correct(user_guess,random_number)
 

main()




