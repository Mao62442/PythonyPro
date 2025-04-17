var1 = 'Hello '
var2 = 'Hiroshima !'
var3 = '返事しない! '

# 文字列結合
print(var1 + var2)

# 文字列重複出力
print(var3 * 3)

# 文字列長さ
print(var1.__len__())
print(len(var1))

# 文字列の切り出し
print(var1[2:5])

# 文字列の検索
print('H' in var1)
print('H' not in var1)