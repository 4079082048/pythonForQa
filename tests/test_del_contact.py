__author__ = 'Sofia'

from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="TestCount", lastname="TestCountZolotova"))
    app.contact.del_first_contact()



