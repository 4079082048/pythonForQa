__author__ = 'Sofia'



def test_del_first_group(app):
    app.contact.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.del_first_group()
    app.session.logout()