import random
import art

print("Welcome to Numbering guess")


def findnum(number,chosen_no):
    while(number >= 0):
        if (number == 0):
            print("you have run out of guesses, You lose.")
            print(f"The number was: {chosen_no}")
            break
        print(f"you have {number} attempts remining to guess the number.")
        x = int(input("Make a guess: "))
        if(x == chosen_no):
            print(f"You Got it! The answer was {chosen_no}")
        elif(x < chosen_no):
            print("To low\nGuess again")

        elif(x > chosen_no):
            print("To high\nGuess again")

        number -= 1








game_play = True

while(game_play != False):
    print(art.logo)

    print("I am thinking of a number between 1 and 100")

    chosen_num = random.randint(1,100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


    if(difficulty == 'easy'):
        findnum(10,chosen_num)
    elif(difficulty == 'hard'):
        findnum(5,chosen_num)

    again = input("Do you want to play agian: 'y' or 'n': ").lower()

    if(again == 'n'):
        game_play = False

    else:
        print("\n"*20)