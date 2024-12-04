import pymysql.cursors
from fixture.db import DbFixture

# было connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# создаем объект типа db
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
  contacts = db.get_contact_list() #получаем списко групп, сохраняем в переменную
  for contact in contacts:
        print(contact)#выводим список
  print(len(contacts)) #выводим длину списка
finally:
    db.destroy()

