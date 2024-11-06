from model.group import Group


def test_edit_group_name(app):
        app.group.open_group_page()
        #app.session.login(username="admin", password="secret")
        app.group.edit_first_group(Group(name="GroupNew"))
        #app.session.logout()


def test_edit_group_header(app):
        app.group.open_group_page()
        #app.session.login(username="admin", password="secret")
        app.group.edit_first_group(Group(header="headerNew"))
        #app.session.logout()