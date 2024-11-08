# -*- coding: utf-8 -*-
from tests.conftest import fixture
from model.group import Group
from  fixture.application import Application


def test_add_group(app):
        app.group.fill_form(Group(name="Group1", header="header", footer="footer"))
        app.group.submit_creation()



def test_add_empty_group(app):
        app.group.fill_form(Group(name="", header="", footer=""))
        app.group.submit_creation()

pass


