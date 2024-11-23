__author__ = 'Sofia'

from model.contact import Contact

def test_del_first_contact(app):
    #If no contacts - create it
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="TestCount", lastname="TestCountZolotova"))
    #Get contacts list
    old_contacts = app.contact.get_contact_list()
    #del first contact in the list
    app.contact.del_first_contact()
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    #get new contact list
    new_contacts = app.contact.get_contact_list()
    #del first contact in the old list
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


