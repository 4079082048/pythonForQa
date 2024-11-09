from model.group import Group
from  fixture.application import Application


def test_edit_group_name(app):
        if app.group.count() == 0:
                app.group.fill_group_form(Group(name="testCreatedToModify"))
        app.group.edit_first_group(Group(name="GroupNew"))
        app.session.logout()


def test_edit_group_header(app):
        if app.group.count() == 0:
                app.group.fill_group_form(Group(name="testCreatedToModify"))
        app.group.edit_first_group(Group(header="headerNew"))
        app.session.logout()



