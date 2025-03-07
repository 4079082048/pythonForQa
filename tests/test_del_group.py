__author__ = 'Sofia'

from operator import index
from tokenize import group

from model.group import Group
from random import randrange, random  # generate the figure from 0 to any
import random

def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.fill_group_form(Group(name = "test000"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.del_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_del_first_group(app):
#    if app.group.count_g() == 0:
#        app.group.fill_group_form(Group(name = "test"))
#    old_groups = app.group.get_group_list()
#    app.group.del_first_group()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 1 == len(new_groups)
#    #del first(zero) number group
#    old_groups[0:1] = []
#    assert old_groups == new_groups