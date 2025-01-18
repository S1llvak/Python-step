class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Додано {amount} до рахунку. Новий баланс: {self.balance}.")
        else:
            print("Сума депозиту повинна бути позитивною.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Знято {amount} з рахунку. Новий баланс: {self.balance}.")
            else:
                print("Недостатньо коштів на рахунку.")
        else:
            print("Сума зняття повинна бути позитивною.")

if __name__ == "__main__":
    account = BankAccount("123456789", 1000)

    account.deposit(500)

    account.withdraw(300)

    account.withdraw(1500)

    print(f"Кінцевий баланс рахунку: {account.balance}.")