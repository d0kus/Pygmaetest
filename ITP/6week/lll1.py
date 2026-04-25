class BankAccount:
    owner =""
    balance = 0.0
    transaction_history =[]

    def __init__(self, owner, balance):
        self.owner = owner

        if balance > 0:
            self.balance = balance
        else:
            print('You cannot init negative amount, balance set to 0')

    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(('deposit', amount))
        else:
            print('You cannot deposit negative amount')

    def withdraw (self, amount):
        if amount > self.balance:
            print('You cannot withdraw more than the balance')
        elif amount < 0:
            print('You cannot withdraw negative amount')
        else:
            self.balance -= amount
            self.transaction_history.append(('withdraw', amount))

    def gethistory (self):
        return self.transaction_history

    def __str__(self):
        return f'Owner: {self.owner}, your balance: {self.balance}'


account1 = BankAccount('John', -300)
account1.deposit(600)
print(account1)
account1.withdraw(200)
print(account1)
print(account1.gethistory())




