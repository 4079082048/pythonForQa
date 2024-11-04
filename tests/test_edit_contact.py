# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
        app.contact.open_home_page()
        app.session.login(username="admin", password="secret")
        app.contact.edit_contact(Contact(firstname="Ivan", lastname="Petrov", company="Google", address="NY", mobile="3151020234", nickname="swallow", title="mem"))
        app.session.logout()