# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="Sofia9", lastname="Zolotova", company="ailet", address="Tula", mobile="89096309913", nickname="swallow", title="mem")

    contact = Contact(firstname="Sofia", lastname="Zolotova", company="ailet", address="Tula", mobile="89096309913",
                      nickname="swallow", title="mm", homephone="3432423",workphone="000000", fax="4444", email= "s1@gmail.com", email3= "s3@gmail.com", email2= "s2@gmail.com", homepage= "www.itsasony.com" )
    app.open_home_page()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.contact.check_main_page()


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", lastname="", company="", address="", mobile="",nickname="", title="")
#    app.open_home_page()
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
#    app.contact.check_main_page()




