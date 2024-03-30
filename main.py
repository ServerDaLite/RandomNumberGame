'''
ServerLite
03 / 29 / 2024 ~ 1:35 AM
Random number guessing game
'''

from random import randint
from os import system

number_of_tries = 5
minimum_guessing_number = 1
maximum_guessing_number = 10

# Picks a number from minimum number to the maximum number
def getRandomNumber(min_x: int, max_x: int) -> int:
    return randint(min_x, max_x)

# Clears the command prompt
def clearScreen() -> None:
    system("cls")

# Displays content for that round
def nextRound():
    clearScreen()
    print(" [ Guess the number ] ")
    print(f"Number of tries left: {number_of_tries}")
    return input("Enter a number: ")

# Display's some content when the answer is wrong
def answerWrong(user_input: int, random_number: int):
    print("That answer is not correct.")
    if random_number < user_input:
        print(f"The number you entered ({user_input}) is higher than the random number.")
    else:
        print(f"The number you entered ({user_input}) is lower than the random number.")
    input("Press \"Any Key\" to continue.")

# Display's some content when the answer is right
def answerRight(user_input: int):
    print(" [ Congragulations ] ")
    print(f"The number {user_input} is the random number!")
    print("Thank you for playing!")
    input("Press \"Any Key\" to continue.")

def isPlayingAgain():
    return input("Do you want to play again (y/n)?")

# The main function
def main():
    answer_right = False
    global number_of_tries
    global minimum_guessing_number
    global maximim_guessing_number
    random_number: int = getRandomNumber(minimum_guessing_number, maximum_guessing_number)
    
    while number_of_tries > 0:
        user_input = nextRound()
        
        clearScreen()
        if int(user_input) != random_number:
            number_of_tries -= 1
            answerWrong(int(user_input), int(random_number))
        else:
            answer_right = True
            answerRight(int(user_input))
            if isPlayingAgain():
                number_of_tries = 5
            else:
                break
    
    if not answer_right:
        


if __name__ == "__main__":
    main()