from wallet import Wallet

def test_getbalance():
    obj = Wallet(0)
    obj.set_balance(20)
    assert obj.get_balance() == 20

def test_removebalance():
    obj = Wallet(50)
    obj.remove_balance(20)
    assert obj.get_balance() == 30

def test_setbalance():
    obj = Wallet(0)
    obj.set_balance(40)
    assert obj.get_balance() == 40

def test_increase_balance_by_1000():
    wallet = Wallet(500)  # saldo inicial cualquiera
    wallet.increase_balance_by_1000()
    assert wallet.balance == 1500
