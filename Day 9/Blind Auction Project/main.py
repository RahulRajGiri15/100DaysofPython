import art
print(art.logo)
# TODO-1: Ask the user for input
cust_inp = False
auction = {}
while(cust_inp != True):
    name = input("Enter your name \n")
    bid = int(input("Enter the amount you want to Bid in $: "))
    auction[name] = bid
    again = input("Is anyone else who want to Bid if yes type 'Yes' if not than type 'No' \n ").lower()
    if(again == "no"):
        cust_inp = True
        print("Okay than")
    else:
        print("\n" * 100)

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print("\n" * 100)
maxi = -1
name = ""
for key in auction:
    if(auction[key] > maxi):
        maxi = auction[key]
        name = key

print(f"The Highest Bid value is ${maxi} by {name}")



