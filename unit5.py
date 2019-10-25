# by Xander Eagle
# October 25, 2019
# this program has the user try to guess a number out of 100 in the lowest number of guesses

import random

# this main function allows the user to guess the number amd responds accordingly
# it tracks the amount of times they have guessed using while loops and if statements


def main():

    while True:
        play_again = input("Do you want to play a game? y/n:  ")
        if play_again == "y":
            print("Lets play!")
        else:
            break
        answer = (random.randint(1, 101))
        guess_number = 0
        while True:
            guess = int(input("What number am I thinking of? It's between 1 and 100. Your answer: "))
            guess_number = guess_number + 1
            if guess > answer:
                print("Too high.")
            elif guess < answer:
                print("Too low.")
            else:
                print("Correct!")
                print("It took you ", guess_number, "guesses to get the number right.")
                break


main()
