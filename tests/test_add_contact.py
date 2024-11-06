# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.open_home_page()
    #app.session.login(username= "admin", password= "secret")
    app.contact.create(Contact(firstname="Sofia", lastname="Zolotova", company="ailet", address="Tula", mobile="89096309913", nickname="swallow", title="mem"))
    app.contact.check_main_page()
    #app.session.logout()


def test_add_empty_contact(app):
    app.contact.open_home_page()
    #app.session.login(username= "admin", password= "secret")
    app.contact.create(Contact(firstname="", lastname="", company="", address="", mobile="", nickname="", title=""))
    app.contact.check_main_page()
    #app.session.logout()





