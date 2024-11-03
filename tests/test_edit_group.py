from model.group import Group


def test_edit_group(app):
        app.contact.open_home_page()
        app.session.login(username="admin", password="secret")
        #app.group.fill_form(Group(name="Group1", header="header", footer="footer"))
        app.group.edit_group(Group(name="GroupNew", header="headerNew", footer="footerNew"))
        #app.group.submit_creation()
        app.session.logout()
