# -*- coding: utf-8 -*-
import pytest

from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
        Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20)),
        Group(name="", header="", footer="")
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
        pass
        #old_groups = app.group.get_group_list() #load old list
        #app.group.fill_form(group)
        #app.group.submit_creation()
        #assert len(old_groups) + 1 == app.group.count_g() #assert two lists length
        #new_groups = app.group.get_group_list()  # load new list IF only previous assert is ok
        #old_groups.append(group)
        #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)








