# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.open_home_page()
    app.contact.create(Contact(firstname="Sofia", lastname="Zolotova", company="ailet", address="Tula", mobile="89096309913", nickname="swallow", title="mem"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    app.contact.check_main_page()


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.open_home_page()
    app.contact.create(Contact(firstname="", lastname="", company="", address="", mobile="", nickname="", title=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    app.contact.check_main_page()




