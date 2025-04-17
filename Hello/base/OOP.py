# OOP.py
class Animal:
    def talk(self):
        print("何かをしゃべる")

# Animal を継承して Dog を定義
class Dog(Animal):
    def speak(self):
        print("ワンワン！")

dog = Dog()
# 先ずは自分のクラスで該当メソッドを探して、見つからなければ継承元のクラスで探す
dog.talk()   # Animal の talk メソッドを呼び出す
dog.speak()  # Dog の speak メソッドを呼び出す

# 定義されていないメソッドを呼び出すとエラーになる
# dog.walk()  # AttributeError: 'Dog' object has no attribute 'walk'

class Base:
    def f1(self):
        print("before")
        self.f2()
        print("base.f1")
    def f2(self):
        print("base.f2")

class Foo(Base):
    def f2(self):
        print("foo.f2")

obj = Foo()
obj.f1()



class TCPServer:
    def f1(self):
        print("TCPServer")
    # pass

class ThreadingMixIn:
    def f1(self):
        print("ThreadingMixIn")

class MyServer(TCPServer, ThreadingMixIn):
    def run(self):
        print("before")
        self.f1()
        print("after")

obj = MyServer()
obj.run()

# 多態性
class Email(object):
    def send(self):
        print("Emailを送信")

class SMS(object):
    def send(self):
        print("SMSを送信")

def sendMsg(arg):
    arg.send()

email = Email()
sms = SMS()

sendMsg(email)
sendMsg(sms)