import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="mdb",
    auth_plugin='mysql_native_password'
)
print("資料庫連線成功")
cursor=con.cursor()
#用程式取得一筆資料
# cursor.execute("select * from product where id=2")
# data=cursor.fetchone()
# print(data)
# print(data[0],data[1])
#取得多筆資料
cursor.execute("select * from product")
data=cursor.fetchall()
print(data)
#逐一取得用row
for row in data:
    print(row[0],row[1]) 
#更新資料
# productName="American"
# productID=1
# cursor.execute("update product set name=%s where id=%s",(productName,productID))
con.commit()
con.close()