from model.contact import Contact
from model.group import Group
from timeit import timeit


def test_group_list(app, db): #через фикстуры app получим список из ui,а через db - из базы
    ui_list = app.group.get_group_list()
    #print(timeit(lambda: app.group.get_group_list(), number = 1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list= map(clean, db.get_group_list())
    #print(timeit(lambda : map(clean, db.get_group_list()),  number=1000))
    #assert False
    assert sorted(ui_list, key = Group.id_or_max) == sorted(db_list, key = Group.id_or_max)


def test_contact_list(app, db): #через фикстуры app получим список из ui,а через db - из базы
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname.strip(), firstname=contact.firstname.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key = Contact.id_or_max) == sorted(db_list, key = Contact.id_or_max)