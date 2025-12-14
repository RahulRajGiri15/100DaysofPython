def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1 / n2
def mod(n1,n2):
    return n1 % n2

cal_final = True
res = 0
conti = False
while(cal_final == True):
    if(conti == True):
        x1 = res
    elif(conti == False):
        x1 = int(input("What's the first input? "))
    sign = {
        "+" : add,
        "-": sub,
        "*": mul,
        "/": div,
        "%": mod
    }
    for sg in sign:
        print(sg)
    xsg = input("Pick up an operation: ")
    x2 = int(input("What's the next number? "))
    # for key in sign:
    #     if(key == xsg):
    #         res = sign[key](x1,x2)

    #OR--another way of this is

    res = sign[xsg](x1,x2)


    print(f"{x1} {xsg} {x2} = {res}")

    again = input(f"Type 'Y' to calculating with {res}, or type 'n' to start a new calculation: ").lower()

    if(again == "y"):
        conti = True
    elif(again == "n"):
        res = 0
    else:
        print("wrong input")



