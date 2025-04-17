# データリスト
numList = [1, 2, 3, 4, 5]
# 2で割り切れるものだけをリスト化
# [表达式 for 变量 in 列表 if 条件]
listComprehension = [num for num in numList if num % 2 == 0]
# リスト化したものを表示
print(listComprehension) # [2, 4]


# { key_expr: value_expr for value in collection if condition }
# Webサイトの辞書
websiteDic = {
    'google': 'www.google.com',
    'yahoo': 'www.yahoo.co.jp',
    'bing': 'www.bing.com',
    'baidu': 'www.baidu.com'
}
# 辞書の要素を取得する
websiteDicComprehension = {key: value for key, value in websiteDic.items() if key != 'baidu'}
print(websiteDicComprehension) # {'google': 'www.google.com', 'yahoo': 'www.yahoo.co.jp', 'bing': 'www.bing.com'}


# { expression for item in Sequence if conditional }
# 車の集合
carSet = {'BMW', 'Mercedes', 'Audi', 'Toyota', 'Honda'}
carSetComprehension = {car for car in carSet if car != 'Audi'}
print(carSetComprehension) # {'BMW', 'Mercedes', 'Toyota', 'Honda'}

# (expression for item in Sequence if conditional)
laptoptuple = ('MacBook', 'Dell', 'HP', 'Lenovo', 'Acer')
laptoptupleComprehension = (laptop for laptop in laptoptuple if laptop != 'HP')
print(tuple(laptoptupleComprehension)) # ('MacBook', 'Dell', 'Lenovo', 'Acer')