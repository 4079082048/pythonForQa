# -*- coding: utf-8 -*-
from fixture.application import Application
from contact import Contact
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username= "admin", password= "secret")
    app.create_contact(Contact(firstname= "Sofia", lastname= "Zolotova", company= "ailet", address= "Tula", mobile= "89096309913", nickname= "swallow", title= "mem"))
    app.check_main_page()
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username= "admin", password= "secret")
    app.create_contact(Contact(firstname= "", lastname= "", company= "", address= "", mobile= "", nickname= "", title= ""))
    app.check_main_page()
    app.session.logout()





