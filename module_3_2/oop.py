class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма отрицательная")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: int):
        if amount > self.__balance:
            raise ValueError("Сумма превышает баланс")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return interest

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self._BankAccount__balance -= amount
        return self._BankAccount__balance


account = SavingsAccount("Kostya", 1000)
print(account.get_balance())
account.apply_interest()
print(account.apply_interest())
print(account.get_balance())

checking = CheckingAccount("Kos")
print(checking.get_balance())
checking.withdraw(150)
print(checking.get_balance())

