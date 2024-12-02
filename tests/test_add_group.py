# -*- coding: utf-8 -*-
from model.group import Group
from data.groups import testdata
from fixture.application import Application


def test_add_group(app, db, json_groups): #загружать тест данные из пакета data
        group = json_groups #переменная group получает значение в качестве параметра
        old_groups = db.get_group_list() #load old list
        app.group.create(group)
        #assert len(old_groups) + 1 == app.group.count_g() #assert two lists length
        new_groups = db.get_group_list()  # load new list IF only previous assert is ok
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



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








