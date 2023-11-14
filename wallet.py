class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val + 20 # Bug here "+20"

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val
