# # capacity (how much coffee can it hold)

# # amount (how much is it currently holding)

# # fill (to fill the cup to it's max capacity with coffee)

# # empty (to rid the cup of any existing coffee by drinking it all or pouring it out)

# # drink (to drink some amount of the coffee that is currently in the cup)


# class CoffeeCup():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.amount = 0

#     def __str__(self):
#         return f'This {self.capacity}oz covfefe cup is {self.amount}oz full.'

#     def fill(self):
#         self.amount = self.capacity

#     def drink(self, drink_amount):
#         self.amount -= drink_amount
#         if(self.amount <= 0):
#             self.amount = 0

#     def empty(self):
#         self.amount = 0 # pour one out for the homies

    

# gabes_cup = CoffeeCup(14)
# westons_cup = CoffeeCup(12)
# aprils_cup = CoffeeCup(14)
# zakariahs_cup = CoffeeCup(24)

# gabes_cup.fill()
# gabes_cup.empty()
# print(gabes_cup)




# ## # ## # ## # ## #
# DEFAULT PARAMETERS


import math # gotta import that math!

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    # def distance(self):
    #     return math.sqrt(self.x**2 + self.y**2) # x**2 to square it

    def distance(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return math.sqrt(dx**2 + dy**2)

    # attach ORIGIN after the Point class is defined
Point.ORIGIN = Point()


# p0 = Point()
# p1 = Point(2, 8)
# print(p1.distance())

p3 = Point(6, 13)
p4 = Point(1, 1)

# print(Point.ORIGIN)

p5 = Point(3, 4)
p6 = Point(3, 19)

print(p5.ORIGIN)

# Distance defaults to calculating how far away a Point is from ORIGIN
# p5.distance()

# print(p3.distance(p4))




# ## # ## # ## # ## #
# Create your own BankAccount class


#     # Upon creation, accounts should have a type (like savings, or checking).

#     # Upon creation, accounts should have a balance that can be set to a specific amount or default to 0.

#     # Each account should have access to a deposit method that adds a certain amount to the balance.

#     # Each account should have a withdraw method that subtracts a certain amount from the balance and returns that amount

#     # When an account is printed, it should show the current balance

# class BankAccount():
#     def __init__(self, acct_type, balance = 0, overdraft_fee = 0):
#         self.acct_type = acct_type
#         self.balance = balance
#         self.overdraft_fee = overdraft_fee

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount
#         if (self.balance < 0):
#             self.overdraft_fee += 20


#     def __str__(self):
#         return f'This {self.acct_type} has {self.balance} monies. Your overdraft fee is currently {self.overdraft_fee}'

# gabes_account = BankAccount('checking', 100)
# gabes_account.withdraw(150)
# # gabes_account.deposit(10)
# print(gabes_account)

