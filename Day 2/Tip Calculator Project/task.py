# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))


print("welcome to the tip calculator")
bill = float(input("enter your total bill amount? $"))
tip = int(input("enter your tip value 10 12 15  20"))
people = int(input("enter total number of people"))

totalamteachp = round(((bill * (1+tip/100)) / people),2)
print(f"your have to pay: ${totalamteachp} only")