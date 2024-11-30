# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

testdata = [
        Group(name="name1", header="header1", footer="footer1"),
        Group(name="name2", header="header2", footer="footer2")
]

#constant = [
#        Group(name="name3", header="header3", footer="footer4"),
#        Group(name="name5", header="header5", footer="footer5")
#]

#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation  # + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
#    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
#    for i in range(5)
#]