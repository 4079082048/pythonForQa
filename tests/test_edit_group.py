from model.group import Group


def test_edit_group(app):
        app.group.open_group_page()
        app.session.login(username="admin", password="secret")
        app.group.edit_group(Group(name="GroupNew", header="headerNew", footer="footerNew"))
        app.session.logout()
