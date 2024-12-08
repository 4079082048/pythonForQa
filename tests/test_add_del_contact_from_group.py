import pytest
import random
from random import randrange
from tests.conftest import check_ui
from fixture.contact import Contact
from fixture.group import Group


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_to_group(app, orm, data_contacts, check_ui):
    if len(orm.contact.count()) == 0:
        app.contact.create(Contact(firstname="FisrtNameAny", lastname="LastNameAny"))
    if len(orm.get_group_list()) == 0:
        app.group.fill_group_form(Group(name = "GroupAny"))
    db_group_list = orm.get_group_list()
    random_index = random.randrange(len(db_group_list)) #Get random group index
    w_g_contacts = orm.get_contacts_not_in_group()
    no_g_contacts = orm.get_contacts_not_in_group()
    app.contact.add_contact_to_group(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
