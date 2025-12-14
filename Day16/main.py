# from random import randint
# print(randint(1,10))

# from turtle import Turtle , Screen
# # from turtle module i have imported Turtle , Screen class
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(200)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


#--------------------------------------------


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["pikachu","squirtle","charmander"])
table.add_column("Type",["Electric","Water","Fire"])

# table.align = "r"
# print(table.align)
print(table)


x = PrettyTable() 
x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"]) 
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386]) 
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769]) 
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
print(x)

