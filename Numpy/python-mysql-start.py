import mysql.connector
con =mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    port=3306,
    database="mdb",
    auth_plugin='mysql_native_password'
)
print("資料庫連線成功")
#建立cursor物件 用來對資料庫下SQL指令
#將變數帶入到SQL指令裡面
productID=6
productName="Green red tea"
cursor=con.cursor()
cursor.execute("INSERT INTO PRODUCT(id,Name) VALUES(%s,%s)",(productID,productName)) #sql語法是''一個點而已
con.commit() #確定執行
con.close()



# import pymysql
# # import charts
# db_settings = {
#     "host": "127.0.0.1",
#     "port": 3306,
#     "user": "root",
#     "password": "12345678",
#     "db": "mdb",
#     "charset": "utf8"
# }
# try:
#     # 建立Connection物件
#     conn = pymysql.connect(**db_settings)
# except Exception as ex:
#     print(ex)