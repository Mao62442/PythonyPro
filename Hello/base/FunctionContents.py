def addSum(a,b):
    """
    2つの数値を受け取り、その合計を返す関数
    :param a: 数値1
    :param b: 数値2
    :return: 合計
    """
    return a + b

print(addSum(1,2))
print(addSum(1.5,2.5))

# lambda関数
# lambda arguments: expression
# 関数名 = lambda 引数1,引数2... : 処理内容
addNum = lambda a,b: a + b
print(addNum(5,7))

numbersList = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbersList))
print(even_numbers)  # 输出：[2, 4, 6, 8]

numbersTuple = (1, 2, 3, 4, 5, 6, 7, 8)
even_numbers = tuple(filter(lambda x: x % 2 == 0, numbersTuple))
print(even_numbers)  # 输出：(2, 4, 6, 8)

numbersSet = {1, 2, 3, 4, 5, 6, 7, 8}
even_numbers = set(filter(lambda x: x % 2 != 0, numbersSet))
print(even_numbers)  # 输出：{1, 3, 5, 7}

numbersDict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
even_numbers = dict(filter(lambda x: x[0] % 2 != 0, numbersDict.items()))
print(even_numbers)  # 输出：{1: 'one', 3: 'three', 5: 'five', 7: 'seven'}