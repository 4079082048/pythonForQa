import pymysql.cursors

# было connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
connection = pymysql.connect(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # database operations go here
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall(): #метод вернет все что извлек в виде набора строк
        print(row)
finally:
    connection.close()
