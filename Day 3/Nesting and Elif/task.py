print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("your your age"))
    if(age >= 18):
        bill = 7
        print("your are adult")
    elif(age>= 12):
        bill = 5
        print("you are mid adult")
    else:
        bill = 7
        print("you are boy")
    photo = input("do you want to take a photo Y for Yes and N for no")
    if(photo == "Y"):
        bill = bill+3
    print(f"the total amout you have to pay is :$ {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
