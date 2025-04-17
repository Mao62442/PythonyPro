# クラスを利用したインターフェースの実装
from abc import ABC, abstractmethod

# 抽象クラス
class Laptop(ABC):
    @abstractmethod
    def read(self, brand):
        pass

# 抽象クラスを継承して具体クラスを定義
class MacBook(Laptop):
    def read(self, brand):
        print('MacBook:', brand)

class Windows(Laptop):
    def read(self, brand):
        print('Windows:', brand)

macbook = MacBook()
dell = Windows()
macbook.read('Apple')
dell.read('Dell')