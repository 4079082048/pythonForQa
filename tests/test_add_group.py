# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation #+ " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
        Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
        for i in range(5)
]

#testdata = [
#        Group(name=name, header=header, footer=footer)
#        for name in ["", random_string("name", 10)] #пробегаем по двум значениям имени и возникают разные комбинации
#        for header in ["", random_string("header", 20)]
#        for footer in ["", random_string("footer", 20)]
#]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
        old_groups = app.group.get_group_list() #load old list
        app.group.fill_form(group)
        app.group.submit_creation()
        assert len(old_groups) + 1 == app.group.count_g() #assert two lists length
        new_groups = app.group.get_group_list()  # load new list IF only previous assert is ok
        old_groups.append(group)
        print("Old groups:", old_groups)
        print("New groups:", new_groups)
        print("Group being added:", group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)









