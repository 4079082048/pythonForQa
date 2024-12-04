from datetime import datetime
from model.group import Group
from model.contact import Contact
from pony.orm import *
from pony.orm import db_session, select
from pony.orm.dbproviders import pymysql
from pymysql.converters import decoders

#Описали набор классов, связали их с таблицами в бд и теперь объекты извлекаются из БД на языке питон

class ORMFixture:
    db = Database() #стоим объект для привязки

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name =Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda:ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True) #вхождение в множество и связующая таблица


    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda :ORMFixture.ORMGroup,table="address_in_groups", column="group_id", reverse="contacts", lazy=True )#подгружаем данные только при обращении = lazy

    def __init__(self, host, name, user, password):
        self.db.bind('mysql',host=host, database=name, user=user, password=password) #сделали привязку , conv=decoders
        self.db.generate_mapping() #сопоставляются
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name= group.name, header= group.header, footer= group.footer)
        return list(map(convert, groups))

    @db_session #код в функции должен выполняться в рамках этой сессии
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname= contact.lastname, lastname= contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select (g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contatcs)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select (c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
