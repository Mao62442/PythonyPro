from pathlib import Path

file_path = Path("C:/Pro/PyPro/Hello/fileobject/temp.txt")

# 1. ファイルに書き込む（上書きモード "w"）
with open(file_path, "w", encoding="utf-8") as f:
    f.write("こんにちは、Python！\n")
    f.write("これはテキストファイルのテストです。\n")
    f.close()

print("✅ファイルに書き込みました✅")

# 2. ファイルを読み込む（読み込みモード "r"）
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    f.close()

# 3. 内容を表示する
print("\n📄ファイルの内容:")
print("----------------------------")
print(content)
print("----------------------------")