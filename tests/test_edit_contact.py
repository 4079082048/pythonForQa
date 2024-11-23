# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
        # Get contacts list
        old_contacts = app.contact.get_contact_list()
        app.open_home_page()
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="TestCount2", lastname="TestCountZolotova2"))
        app.contact.edit_first_contact(Contact(firstname="Ivanna"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts)  == len(new_contacts)


def test_edit_contact_lastname(app):
        old_contacts = app.contact.get_contact_list()
        app.open_home_page()
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="TestCount2", lastname="TestCountZolotova2"))
        app.contact.edit_first_contact(Contact(lastname="Gladisheva"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)


