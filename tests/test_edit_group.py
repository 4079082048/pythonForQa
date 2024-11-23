from tokenize import group

from model.group import Group
from  fixture.application import Application


def test_edit_group_name(app):
        old_groups = app.group.get_group_list()
        group = Group(name="testCreatedToModify")
        group.id = old_groups[0].id #remember id of the group
        #if app.group.count_g() == 0:
        #        app.group.fill_group_form(group)
        app.group.edit_first_group(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        app.session.logout()


#def test_edit_group_header(app):
#        old_groups = app.group.get_group_list()
#        if app.group.count_g() == 0:
#                app.group.fill_group_form(Group(name="testCreatedToModify"))
#        app.group.edit_first_group(Group(header="headerNew"))
#        new_groups = app.group.get_group_list()
#        assert len(old_groups) == len(new_groups)
#        app.session.logout()



