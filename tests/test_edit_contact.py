# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
        app.contact.open_home_page()
        #app.session.login(username="admin", password="secret")
        app.contact.edit_first_contact(Contact(firstname="Ivanna"))
        #app.session.logout()


def test_edit_contact_lastname(app):
        app.contact.open_home_page()
        #app.session.login(username="admin", password="secret")
        app.contact.edit_first_contact(Contact(lastname="Gladisheva"))
        app.session.logout()