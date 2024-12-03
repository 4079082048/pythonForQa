# -*- coding: utf-8 -*-
from operator import index
from random import randrange
from model.contact import Contact


def test_edit_contact_firstname(app):
        # Get contacts list
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="Sofia", lastname="Zolotova", company="ailet", address="Tula", mobilephone="89096309913",nickname="swallow", title="mem")
        app.open_home_page()
        if app.contact.count() == 0:
                app.contact.create(contact)
        index = randrange(len(old_contacts))
        contact.id = old_contacts[index].id
        app.contact.edit_contact_by_index(index, contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts)  == len(new_contacts)
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_contact_by_id(app, db):
        old_contacts = db.get_contact_list()
        app.open_home_page()
        index = randrange(len(old_contacts))
        contact = Contact(firstname="Sofia", lastname="Zolotova", company="ailet", address="Tula", mobile="89096309913",
                          nickname="swallow", title="mem")
        contact.id = old_contacts[index].id
        app.contact.edit_contact_by_id(contact.id, contact)
        assert len(old_contacts) == app.contact.count_contacts()
        new_contacts = db.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_edit_contact_lastname(app):
#        old_contacts = app.contact.get_contact_list()
#        app.open_home_page()
#        if app.contact.count() == 0:
#                app.contact.create(Contact(firstname="TestCount2", lastname="TestCountZolotova2"))
#        app.contact.edit_first_contact(Contact(lastname="Gladisheva"))
#        new_contacts = app.contact.get_contact_list()
#        assert len(old_contacts) == len(new_contacts)


