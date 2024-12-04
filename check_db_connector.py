import pymysql.cursors
from fixture.orm import ORMFixture #from fixture.db import DbFixture

# было connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# создаем объект типа db
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#try:
#  l = db.get_group_list() #получаем списко групп, сохраняем в переменную
#  for item in l:
#        print(item)#выводим список
#  print(len(l)) #выводим длину списка
#finally:
#    pass

try:
  l = db.get_contact_list() #получаем списко групп, сохраняем в переменную
  for item in l:
        print(item)#выводим список
  print(len(l)) #выводим длину списка
finally:
    pass




