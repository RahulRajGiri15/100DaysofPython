letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
ranwordpass = ""
for i in range(0, nr_letters,1):
    x = random.choice(letters)
    ranwordpass += x
for i in range(0, nr_symbols,1):
    x = random.choice(symbols)
    ranwordpass += x
for i in range(0, nr_numbers,1):
    x = random.choice(numbers)
    ranwordpass += x

print(f"random easy password is:\n {ranwordpass}")


strong = []
for i in range(0,len(ranwordpass),1):
    strong.append(ranwordpass[i])

strpass = ""
random.shuffle(strong)
for i in range (0,len(strong)):
    strpass += strong[i];

# print(strpass)

print(f"strong password is \n {strpass}")