# ComputeTool.pyをインポート
import ComputeTool
from ComputeTool import resultSub
import requests

a = 5
b = 2

# print("足し算:", a + b)
# print("引き算:", a - b)
# print("掛け算:", a * b)
# print("割り算1:", a / b)
# print("割り算2:", a // b)
# print("割り算3:", a % b)
# print("べき乗:", a ** b)

print("モジュールで足し算:", ComputeTool.resultAdd(a, b))
print("モジュールで引き算:", ComputeTool.resultSub(a, b))

response = requests.get("https://www.google.com")
print("Googleのレスポンス:", response.status_code)