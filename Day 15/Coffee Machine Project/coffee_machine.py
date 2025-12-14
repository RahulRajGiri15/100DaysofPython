MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit_money = 0

def report():
    '''prints the available reousces'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

    print(f"Money: ${profit_money}")

def checkrequirements(reso,coff,total_money):
    '''this function checks if the resources are sufficient enough'''
    if(coff == "espresso"):
        if(resources['water'] >= 50 and resources['coffee'] >= 18 and total_money >= 1.50):
            resources['water'] -= 50
            resources['coffee'] -= 18
            return True
        else:
            return False
    elif (coff == "latte"):
        if (resources['water'] >= 200 and resources['coffee'] >= 24 and resources['milk'] >=150 and total_money >= 2.50):
            resources['water'] -= 200
            resources['coffee'] -= 24
            resources['milk'] -= 150
            return True
        else:
            return False
    elif (coff == "cappuccino"):
        if (resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >=100 and total_money >= 3.00):
            resources['water'] -= 250
            resources['coffee'] -= 24
            resources['milk'] -= 100
            return True
        else:
            return False
    return False

def lackreso(ingred, cst, moneypaid):
    '''this function print the missing resource'''
    if(cst > moneypaid):
        print(f"Not enough money, lacking money ${cst-moneypaid}")
    else:
        for item in ingred:
            if(ingred[item] >= resources[item]):
                print(f"sorry not enough {item}")
                break

machine_on = True

def finaldisplay(cafe,totmoney):
    ''''this is function which just display the output'''
    global profit_money
    change = totmoney - MENU[cafe]['cost']
    profit_money += MENU[cafe]["cost"]
    print(f"Here is the ${round(change ,2)} in change")
    print(f"Here is you Cofee {cafe} ☕:)")


while(machine_on != False):
    coffe = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if(coffe == 'report'):
        report()
        continue
    if(coffe == "off"):
        machine_on = False
        break
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_money = (quarters*0.01)+(dimes*0.10)+(nickles*0.05)+(pennies*0.25)

    if(checkrequirements(resources,coffe,total_money) == True):

            finaldisplay(coffe,total_money)
    else:
        drink = MENU[coffe]
        lackreso(drink["ingredients"],drink["cost"],total_money)

        # print("sorry there is not enough resources")

