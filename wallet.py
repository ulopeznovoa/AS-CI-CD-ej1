class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        self.balance = self.balance - val

    def loteria(self):
        saldoAct = self.get_balance()
        saldoConLot = saldoAct + 1000
        set_balance(saldoConLot)
