intNum = 1
floatNum = 1.0
strNum = "Hello Hiroshima !!!"
existflag = True

listNum = [1, 2, 3, 4, 5]
listStr = ["Kouchi", "Hiroshima", "Fukuoka"]
listContainer = [1, 2, 3, 4, 5, "Hiroshima", "Okayama", True]

for item in listContainer:
    print(item)

def listNumLoop(listNum):
    for item in listNum:
        print(item)

def listNumLoop(listStr):
    for item in listStr:
        print(item)

print('---------------------')
listNumLoop(listNum)
listNum.append(6)
print('---------------------')
listNumLoop(listNum)
listNum.remove(2)
print('---------------------')
listNumLoop(listNum)

print('---------------------')
listNumLoop(listStr)
listStr.append("Okayama")
print('---------------------')
listNumLoop(listStr)
listStr.remove("Kouchi")
print('---------------------')
listNumLoop(listStr)

# 中身変更不可
tupleNum = (1, 2, 3, 4, 5)
tupleStr = ("Hello", "Hiroshima", "!!!")
tupleNum[0] = 10  # エラー]

dictCity = {1: "Hiroshima", 2: "Tokyo", 3: "Osaka"}
