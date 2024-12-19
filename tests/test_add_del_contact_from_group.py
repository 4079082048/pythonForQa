from tokenize import group

import pytest
import random
from random import randrange
from tests.conftest import check_ui
from fixture.contact import Contact
from fixture.group import Group



def test_add_contact_to_group(app, orm):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="FisrtNameAny", lastname="LastNameAny"))
    if app.group.count_g() == 0:
        app.group.create(Group(name = "GroupAny"))

    db_group_list = orm.get_group_list() #Get groups list from db
    random_g_id = random.randrange(len(db_group_list)) #Get random group index
    group = db_group_list[random_g_id]

    no_g_contacts = orm.get_contacts_not_in_group(group) #Get contacts without group from DB
    if no_g_contacts == []:
        app.contact.create(Contact(firstname="FisrtNameEmpty"))
        no_g_contacts = orm.get_contacts_not_in_group(group)
    random_id = random.randrange(len(no_g_contacts)) #Get random index in randrange
    r_contact = no_g_contacts[random_id] #Get random contact from index
    contacts_in_group_b = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(r_contact.id, group.id)
    contacts_in_group_a = orm.get_contacts_in_group(group)
    contacts_in_group_b.append(r_contact) #before contacts + new one
    assert sorted(contacts_in_group_a, key=Group.id_or_max) == sorted(contacts_in_group_b, key=Group.id_or_max)


def test_del_contact_from_group(app, orm):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="DelFisrtNameAny", lastname="DelLastNameAny"))
    if app.group.count_g() == 0:
        app.group.create(Group(name="DelGroupAny"))

    db_group_list = orm.get_group_list()  # Get groups list from db
    if not db_group_list:
        pytest.fail("No groups found in the database.")
    random_g_id = random.randrange(len(db_group_list))  # Get random group index
    group = db_group_list[random_g_id]

    db_contact_list = orm.get_contacts_in_group(group)  # Get contacts in group from DB
    if db_contact_list == []:
        db_contact_list = orm.get_con_list()
        contact_id = randrange(len(db_contact_list))
        contact = db_contact_list[contact_id]
        app.contact.add_contact_to_group(contact.id, group.id)
        db_contact_list = orm.get_contact_list(group)
    contact_id = randrange(len(db_contact_list))
    contact = db_contact_list[contact_id]
    contacts_in_group_before = orm.get_contacts_not_in_group(group)
    app.contact.del_contact_from_group(contact.id, group.id)
    contacts_in_group_after = orm.get_contacts_in_group(group)
    contacts_in_group_after.append(contact)
    assert sorted(contacts_in_group_after, key=Group.id_or_max) == sorted(contacts_in_group_before, key=Group.id_or_max)



