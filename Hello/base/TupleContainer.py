# 丸括弧の対を使い、空のタプルを表す:()
tupleNull = ()
# カンマを使い、単要素のタプルを表す: a, または (a,)
tupleSingle = (1,)
# 項目をカンマで区切る: a, b, c または (a, b, c)
tupleNum = (1, 2, 3, 4, 5)
# 組み込みのtuple()を使う: tuple()またはtuple(iterable)
tupleBuiltIn = tuple([1, 2, 3, 4, 5])

# タプルの要素を取得する
print(tupleNum[0],tupleNum[1])

# タプルの要素を変更する

# 要素の値を直接に変更することはできない
# tupleNum[0] = 10 # TypeError: 'tuple' object does not support item assignment
tupleNewNum = tupleNum + (6,)
print(tupleNewNum)

# タプルの要素を削除することはできない
# del tupleNum[0] # TypeError: 'tuple' object doesn't support item deletion

# タプルの関数
tupleCity = ('Tokyo', 'Osaka', 'Nagoya', 'Kyoto', 'Fukuoka', 'Sapporo', 'Hiroshima', 'Sendai', 'Kobe', 'Yokohama')
# インデックスによって値を取得する
print(tupleCity[0])  # 'Tokyo'
print(tupleCity[-1]) # 'Yokohama'
# タプルの長さを取得する
print(len(tupleCity))
# タプルに要素が含まれているかを確認する
print('Tokyo' in tupleCity)
# タプルの最大値と最小値を取得する
print(max(tupleCity)) # 'Yokohama'
print(min(tupleCity)) # 'Fukuoka'