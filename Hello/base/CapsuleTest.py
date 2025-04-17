class BankAccount:
    def __init__(self, owner, balance):
        # public
        self.owner = owner
        # protected（慣習的）
        self._account_type = "普通"
        # private
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "残高不足"

    def get_balance(self):
        return self.__balance

acc = BankAccount("田中", 1000)
print(acc.owner)           # OK（public）
print(acc._account_type)   # 一応アクセスできる（protected）
# print(acc.__balance)     # エラー：アクセスできない

print(acc.get_balance())   # メソッド経由で取得