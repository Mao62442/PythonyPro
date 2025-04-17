# mysqlのモジュールをインポート
import mysql.connector

# mysql.connectorを使用してMySQLに接続する
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    auth_plugin="mysql_native_password",
    database="daichigiken"
)

# コミット用の関数を定義
def queryCommit(queryObj):
    queryObj.execute("commit")

# カーソルを作成
query = mysql_connection.cursor()

# query.execute("insert into daichigiken.employee values (3, '二藤宏嵩', '男', '2025/04/10 16:05:00','2025/04/10 16:05:00')")
# 更新用Sqlの実行
query.execute("update daichigiken.employee set age = 25 where id in (1,2,3)")
# コミットメソッドを実行
queryCommit(query)
# 検索用Sqlの実行
query.execute("select * from daichigiken.employee")

# 結果を取得して表示
for row in query.fetchall():
    print(row)