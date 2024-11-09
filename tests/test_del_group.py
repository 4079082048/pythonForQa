__author__ = 'Sofia'

from model.group import Group


def test_del_first_group(app):
    #app.group.open_group_page()
    if app.group.count_g() == 0:
        app.group.fill_group_form(Group(name = "test"))
    app.group.del_first_group()

