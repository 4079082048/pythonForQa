from model.group import Group
from  fixture.application import Application


def test_edit_group_name(app):
        app.group.edit_first_group(Group(name="GroupNew"))
        app.session.logout()


def test_edit_group_header(app):
        app.group.edit_first_group(Group(header="headerNew"))
        app.session.logout()