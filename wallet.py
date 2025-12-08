class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val

    def increase_balance_by_1000(self):
        """Incrementa el saldo actual en 1000 unidades."""
        self.balance += 1000

