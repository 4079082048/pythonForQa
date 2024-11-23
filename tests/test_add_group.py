# -*- coding: utf-8 -*-
#from tokenize import group
from sys import maxsize
from model.group import Group


def test_add_group(app):
        old_groups = app.group.get_group_list()
        group = Group(name="Group1", header="header", footer="footer")
        app.group.submit_creation(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) +1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_group1(app):
#        old_groups = app.group.get_group_list()  # Ensure this is a method
#       group = Group(name="Group1", header="header", footer="footer")
#        app.group.submit_creation(group)  # Ensure this method works as expected
#        new_groups = app.group.get_group_list()  # Again, ensure this is a method
#        assert len(old_groups) + 1 == len(new_groups)
#        old_groups.append(group)  # Append the new group to the old list for comparison
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_add_empty_group(app):
#        old_groups = app.group.get_group_list()
#        app.group.fill_form(Group(name="", header="", footer=""))
#        app.group.submit_creation()
#        new_groups = app.group.get_group_list()
#        assert len(old_groups) +1 == len(new_groups)
#        old_groups.append(group)
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



