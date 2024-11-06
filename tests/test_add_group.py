# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
        app.contact.open_home_page()
        #app.session.login(username="admin", password="secret")
        app.group.fill_form(Group(name="Group1", header="header", footer="footer"))
        app.group.submit_creation()
        #app.session.logout()


def test_add_empty_group(app):
        app.contact.open_home_page()
        #app.session.login(username= "admin", password= "secret")
        app.group.fill_form(Group(name="", header="", footer=""))
        app.group.submit_creation()
        #app.session.logout()



