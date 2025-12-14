import random
import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(list):
    """take a list and send their scores back"""
    score = sum(list)
    if(score == 21 and len(list) == 2):
        return 0
    elif(score > 21 and 11 in list):
        list.remove(11)
        list.append(1)
        score -= 10
    return score

def compare(u_score, c_score):
    if(u_score == c_score):
        return ("Draw")
    elif(c_score == 0):
        return ("Lose, opponent has blackjack")
    elif(u_score == 0):
        return("YOU WIN, wins with balckjack")
    elif(u_score > 21):
        return("Lose, you went over ")
    elif(c_score > 21):
        return "You won, opponent went over"
    elif(u_score > c_score):
        return "You won , you have highest score"
    else:
        return "You lose :("

def play_game():
    print(art.logo)

    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if(user_score == 0 or computer_score == 0 or user_score > 21):
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if(user_should_deal == 'y'):
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and  computer_score <= 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand is {user_cards} and final score is {user_score}")
    print(f"computer final hand is {computer_cards} and final score is {computer_score}")
    print(compare(user_score,computer_score))


while(input("Do you want to play the game of balckjack? Type 'y' or 'n': ").lower() == 'y'):
        print("\n" * 20)
        play_game()



