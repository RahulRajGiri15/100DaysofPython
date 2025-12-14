from typing import final

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

totalm = 0
if(size == "S"):
    totalm += 15
    if(pepperoni == "Y"):
        totalm += 2
    if(extra_cheese == "Y"):
        totalm += 1
elif(size == "M"):
    totalm += 20
    if(pepperoni == "Y"):
        totalm += 3
    if(extra_cheese == "Y"):
        totalm += 1

elif(size == "L"):
    totalm += 25
    if(pepperoni == "Y"):
        totalm += 3
    if(extra_cheese == "Y"):
        totalm += 1

print(f"your final bill is: ${totalm}")