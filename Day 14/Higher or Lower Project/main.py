import random
import art
import  game_data

print(art.logo)

game_play = True
score = 0
user1 = random.choice(game_data.data)

while(game_play != False):

    user2 = random.choice(game_data.data)
    if(user1 == user2):
        user2 = random.choice(game_data.data)

    print(f"Compare A: {user1['name']}, a {user1['description']}, form {user1['country']}")
    print(art.vs)
    print(f"Against B: {user2['name']}, a {user2['description']}, form {user2['country']}")
    ans = input("who has more followers? Type 'A' or 'B': ").lower()
    if(ans == 'b' and user1['follower_count'] <= user2['follower_count']):
        user1 = user2
        score += 1
        print(f"You are right: your current sore is: {score}")
    elif(ans == 'a' and user1['follower_count'] > user2['follower_count']):
        score += 1
        print(f"You are right: your current sore is: {score}")
    else:
        print(f"Wrong , Game over , Your final score was {score}")
        again = input("Do you wish to paly agian, 'y' and 'n' ").lower()
        if(again == 'n'):
            game_play = False
        else:
            print("\n"*20)
            print(art.logo)
            user1 = random.choice(game_data.data)










