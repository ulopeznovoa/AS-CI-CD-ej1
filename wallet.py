class Wallet:
    def __init__(self, balance):
        self.balance = balance
        print("self.balance")

    def set_balance(self, val):
        self.balance = self.balance + val
        print("self.balance")

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val
