from model.group import Group
from  fixture.application import Application


def test_edit_group_name(app):
        old_groups = app.group.get_group_list()
        if app.group.count_g() == 0:
                app.group.fill_group_form(Group(name="testCreatedToModify"))
        app.group.edit_first_group(Group(name="GroupNew"))
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        app.session.logout()


def test_edit_group_header(app):
        old_groups = app.group.get_group_list()
        if app.group.count_g() == 0:
                app.group.fill_group_form(Group(name="testCreatedToModify"))
        app.group.edit_first_group(Group(header="headerNew"))
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        app.session.logout()



