class User:
    def __init__ (self, name):
        self.name = name
        self.strength = 10
        self.account = BankAccout(100)
class BankAccout:
    def __init__ (self, money):
        self.money = money
    def deposit(self, ammount):
        self.money += ammount
    def withdraw(self, ammount):
        if self.money - ammount > 0:
            self.money -= ammount
bob = User("Fred")
print(bob.account.money)
bob.account.deposit(100)
print(bob.account.money)
