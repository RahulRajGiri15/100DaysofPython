rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

x = int(input("enter 0 for rock 1 for paper 2 for sissor\n"))
if(x == 0):print(rock)
elif(x == 1):print(paper)
elif(x == 2):print(scissors)


import random
y = random.randint(0,2)
print("Other player choose\n")
if(y == 0):print(f"Rock \n{rock}")
elif(y == 1):print(f"paper \n {paper}")
elif(y == 2):print(f"scissors \n {scissors}")


if(x == y):print("Draw - try again")
elif(x == 0 and y == 2):print("you win")
elif(x == 1 and y == 2): print(f"you win")
else:print("You LOST the Game")
