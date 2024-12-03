__author__ = 'Sofia'

from random import randrange
from model.contact import Contact
import random


def test_del_some_contact(app):
    wd = app.wd
    #If no contacts - create it
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="TestCount", lastname="TestCountZolotova"))
    #Get contacts list
    old_contacts = app.contact.get_contact_list()
    index =  randrange(len(old_contacts))
    #del first contact in the list
    print(f"Количество контактов до удаления: {len(old_contacts)}")
    app.contact.del_contact_by_index(index)
    #app.contact.alert_accept()
    print(f"Количество контактов после удаления: {app.contact.count_contacts()}")
    #assert len(old_contacts) - 1 == app.contact.count_contacts()
    import time
    time.sleep(1)
    assert app.contact.count_contacts() == len(old_contacts) - 1
    new_contacts = app.contact.get_contact_list()
    #del first contact in the old list
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts


def test_del_some_contact_by_id(app, db):
    wd = app.wd
    #If no contacts - create it
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="TestCount", lastname="TestCountZolotova"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index =  randrange(len(old_contacts))
   # удаляем контакт по id
    app.contact.del_contact_by_id(contact.id)
    #сравниваем старый список и счетчики контактов
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    import time
    time.sleep(1)
    assert app.contact.count_contacts() == len(old_contacts) - 1
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


#def test_del_first_contact(app):
##    #If no contacts - create it
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="TestCount", lastname="TestCountZolotova"))
#    #Get contacts list
#    old_contacts = app.contact.get_contact_list()
#    #del first contact in the list
#    app.contact.del_first_contact()
#    # get new contact list
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == app.contact.count_contacts()
    #del first contact in the old list
#    old_contacts[0:1] = []
#    assert old_contacts == new_contacts


