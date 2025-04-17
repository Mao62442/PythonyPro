try:
    result = 10 / 0
    print("Result:", result)
except Exception as e:
    # エラーが発生した場合の処理
    print("An error occurred:", e)
else:
    # エラーが発生しなかった場合の処理
    print("No errors occurred.")
finally:
    # 必ず実行される処理
    print("Execution completed.")