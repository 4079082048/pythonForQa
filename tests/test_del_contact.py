__author__ = 'Sofia'
from random import randrange
from model.contact import Contact


def test_del_some_contact(app):
    #If no contacts - create it
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="TestCount", lastname="TestCountZolotova"))
    #Get contacts list
    old_contacts = app.contact.get_contact_list()
    index =  randrange(len(old_contacts))
    #del first contact in the list
    app.contact.del_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    # get new contact list
    new_contacts = app.contact.get_contact_list()
    #del first contact in the old list
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts

def test_del_con_by_index(app):
    # предусловие если контактов нет - то создать
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Автандил"))
    # получаем список контактов
    old_con = app.contact.get_con_list()
    index = randrange(len(old_con))
    # метод удаления первого в списке контакта
    app.contact.del_con_by_index(index)
    # сравниваем старый список и счётчик контактов по количеству (в старом списке на 1 больше)
    assert len(old_con) - 1 == app.contact.count_con()
    # получаем новый список контактов
    new_con = app.contact.get_con_list()
    #прибиваем в старом списке первый по списку контакт
    old_con[index:index+1] = []


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


