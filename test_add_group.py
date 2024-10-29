# -*- coding: utf-8 -*-
import unittest
from application import Application
from group import Group
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.fill_group_form( Group(name= "Group1",header= "header", footer= "footer"))
        app.submit_group_create()


def test_add_empty_group(app):
        app.login(username= "admin", password= "secret")
        app.fill_group_form(Group(name= "",header= "", footer= ""))
        app.submit_group_create()



