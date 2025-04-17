numSet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# for i in numSet:
#     print(i)
# else:
    # for文が正常に終了した場合に実行される
    # print(', ')

count = 0
for i in numSet:
    if i == 10:
        # for文を終了する
        break
    else:
        count += 1
        print(count)
        continue