from module_3_2.oop import SavingsAccount


def test_savings_account():
    test_acc = SavingsAccount("Kostya")
    test_acc.deposit(500)
    test_acc.withdraw(100)
    assert test_acc.get_balance() > 0, "Отрицательный баланс"