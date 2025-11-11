from wallet import Wallet
from bank import incrementar_saldo_1000 

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

def test_incrementar_saldo_1000():
    assert incrementar_saldo_1000(0) == 1000
    assert incrementar_saldo_1000(500) == 1500
