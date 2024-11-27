# -*- coding: utf-8 -*-
from tokenize import group

from model.group import Group
import pytest
from data.groups import constant as testdata


#testdata = [
#        Group(name=name, header=header, footer=footer)
#        for name in ["", random_string("name", 10)] #пробегаем по двум значениям имени и возникают разные комбинации
#        for header in ["", random_string("header", 20)]
#        for footer in ["", random_string("footer", 20)]
#]


#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#def test_add_group(app, group):
#        old_groups = app.group.get_group_list() #load old list
#        app.group.fill_form(group)
#        app.group.submit_creation()
#        assert len(old_groups) + 1 == app.group.count_g() #assert two lists length
#        new_groups = app.group.get_group_list()  # load new list IF only previous assert is ok
#        old_groups.append(group)
#        print("Old groups:", old_groups)
#        print("New groups:", new_groups)
#        print("Group being added:", group)
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_group(app, data_groups): #загружать тест данные из пакета data
        group = data_groups
        old_groups = app.group.get_group_list() #load old list
        app.group.fill_form(group)
        app.group.submit_creation()
        assert len(old_groups) + 1 == app.group.count_g() #assert two lists length
        new_groups = app.group.get_group_list()  # load new list IF only previous assert is ok
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)








