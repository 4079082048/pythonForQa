from operator import index
from random import randrange
from tokenize import group

from model.group import Group
from random import randrange
from  fixture.application import Application


def test_edit_group_name(app):
        if app.group.count_g() == 0:
                app.group.fill_group_form(Group(name="testCreatedToModify"))
        old_groups = app.group.get_group_list()
        group = Group(name="!Name", header="HeaderNew", footer="NewFooter")
        index = randrange(len(old_groups))
        group.id = old_groups[index].id #remember id of the group
        app.group.edit_group_by_index(index, group)
        assert len(old_groups) ==  app.group.count_g()
        new_groups = app.group.get_group_list()
        old_groups[index] = group
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



