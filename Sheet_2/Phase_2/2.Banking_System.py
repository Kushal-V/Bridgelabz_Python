class Account:

    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("InSufficientFundsError.")
        self.__balance -= amount
    
a = Account(1000)
print(a.balance)
a.deposit(500)
print(a.balance)
a.withdraw(200)
print(a.balance)