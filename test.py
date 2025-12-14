from wallet import Wallet, increment_balance


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
    
def test_increment_balance():
    assert increment_balance(500) == 1500
