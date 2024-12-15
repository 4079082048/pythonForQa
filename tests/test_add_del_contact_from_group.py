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
    app.contact.add_contact_to_group(r_contact.id, group.id)

def test_del_contact_from_group(app, orm):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="DelFisrtNameAny", lastname="DelLastNameAny"))
    if app.group.count_g() == 0:
        app.group.create(Group(name="DelGroupAny"))

    db_group_list = orm.get_group_list()  # Get groups list from db
    random_g_id = random.randrange(len(db_group_list))  # Get random group index
    group = db_group_list[random_g_id]

    w_g_contacts = orm.get_contacts_in_group(group)  # Get contacts without group from DB
    if w_g_contacts == []: #If there are no contacts in the group add contact to group
            w_g_contacts = orm.get_contact_list()
            contact_id = randrange(len(w_g_contacts))
            contact = w_g_contacts[contact_id]
            app.contact.add_contact_to_group(contact.id, group.id)
            w_g_contacts = orm.get_contacts_in_group(group)
    random_id = random.randrange(len(w_g_contacts))  # Get random index in randrange
    r_contact = w_g_contacts[random_id]  # Get random contact from index

    app.contact.del_contact_from_group(r_contact.id, group.id)
