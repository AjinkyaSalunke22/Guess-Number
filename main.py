import random



# Function to guess the random number generated by the computer
def guess_comp(maxrange):
    maxrange = int(input(("Enter the range of numbers from 1 to ? :\n"))) # Taking user input for range of guess.

    random_num = random.randint(1, maxrange) # Generating random number using random library.
    guess = 0 # Declaring the default guess as 0 so it will never be equal to the random number and it will continue the loop.
    
    # Loop runs untill guess is correct.
    while (guess != random_num):
        guess = int(input("Guess the number:\n")) # User is guessing the number.

        # Hints about the random number.
        if (guess < random_num):
            print("Sorry, the guessed number is lesser than the actual number. Please try again.")
        elif (guess > random_num):
            print("Sorry, the guessed number is greater than the actual number. Please try again.")

    # Declaring the number and the greetings.
    print(f"Hey!!!\nYou got it. You guessed it right, it was {random_num}.\n")



# Function to guess the users entered number by the computer,
def guess_user(maxrange):
    maxrange = int(input(("Enter the range of numbers from 1 to ? :\n"))) # Taking user input for range of guess.
    low = 1 # Lower value of range.
    high = maxrange # Greater value of range.
    feedback = '' # Dclaring feedback from user as empty string.
    
    # Loop runs until the feedback is as correct guess form the user.
    while (feedback != 'c'):
        # randomly guessing the number from the given range
        # checking if the low and high of the guess dosn't be same.
        if (low != high):
            guess = random.randint(low, high)
        elif (low == high):
            guess = low # it can be either low or high

        # Creating a feedback loop to guess and update the range of guess.
        feedback = input(f"Is the guessed number {guess} greater 'G', Lesser 'L' or Correct 'C'.\n").lower()
        if (feedback == 'g'):
            high = guess-1
        elif (feedback == 'l'):
            low = guess+1

    print("Yeah!!! Computer guessed it correct. The number is, ", guess, "\n")



# Creating a loop of 10 trials.
for i in range(1,5):
    if i % 2 == 0:
        print("*****************************************************************")
        print("Your Turn:- \n")
        guess_comp(0) # Calling the computer function.
    elif i % 2 != 0:
        print("*****************************************************************")
        print("Computer's Turn:- \n")
        guess_user(0) # Calling the user function