import random

def main():
    while True:
        play_again = input("Do you want to play a game? y/n:  ")
        if play_again == "y":
            print("lets play!")
        else:
            break
        answer = (random.randint(1, 101))
        guess = input("What number do you think it is?")



main()
