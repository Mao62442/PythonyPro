numSet = {1, 2, 3, 4, 5}
numUniqueSet = {1, 2, 2, 3, 3, 4, 4, 5}

print(numSet) # {1, 2, 3, 4, 5}
# 重複データは削除される
print(numUniqueSet) # {1, 2, 3, 4, 5}

numSetA = {1, 2, 3, 4}
numSetB = {3, 4, 5, 6}

print(numSetA | numSetB) # 和集合 {1, 2, 3, 4, 5, 6}
print(numSetA & numSetB) # 交差集合 {3, 4}
print(numSetA - numSetB) # 差集合 {1, 2}
print(numSetB - numSetA) # 差集合 {5, 6}
print(numSetA ^ numSetB) # 対称差（共通していない要素） {1, 2, 5, 6}