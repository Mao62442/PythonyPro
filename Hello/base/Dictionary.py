# 空マッピングデータ作成
emptyDic = {}

# 空マッピングデータ作成
studentDic = {
    # 名前
    'name': 'Taro',
    # 年齢
    'age': 20,
    # 住所
    'address': 'Tokyo',
}

# マッピングデータの全要素を取得する
print(studentDic) # {'name': 'Taro', 'age': 20, 'address': 'Tokyo'}
# 年齢を取得する
print(studentDic['age']) # 20

# Keyが重複している場合、最後の値が優先される
catDic = {
    # 名前
    'name': '花子',
    # 年齢
    'age': 20,
    # 住所
    'address': 'Tokyo',
    # 名前(重複)
    'name': '雫',
}
print(catDic['name']) #'雫'

# Keyがリストの場合、エラーになる
# listDic = {
#     # 名前
#     ['Name']: '雫',
#     # 年齢
#     'age': 20,
#     # 住所
#     'address': 'Tokyo',
# }
# print(listDic['Name']) # TypeError: unhashable type: 'list'

animalDic = {
    'cat': {'name': '雫', 'age': 3, 'address': 'China'},
    'dog': {'name': 'モモコ', 'age': 5, 'address': 'China'},
    'bird': {'name': 'DeathBird', 'age': 2, 'address': 'China'}
}

for key in animalDic:
    print(key) # cat dog bird
    print(animalDic[key]) # {'name': '雫', 'age': 3, 'address': 'China'}
    print(animalDic[key]['name']) # 雫 モモコ DeathBird