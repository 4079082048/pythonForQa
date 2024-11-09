# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
        app.contact.open_home_page()
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="TestCount2", lastname="TestCountZolotova2"))
        app.contact.edit_first_contact(Contact(firstname="Ivanna"))


def test_edit_contact_lastname(app):
        app.contact.open_home_page()
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="TestCount2", lastname="TestCountZolotova2"))
        app.contact.edit_first_contact(Contact(lastname="Gladisheva"))
