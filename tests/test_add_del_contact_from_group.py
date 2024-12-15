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
    if not db_group_list:
        pytest.fail("No groups found in the database.")

    random_g_id = random.randrange(len(db_group_list))  # Get random group index
    group = db_group_list[random_g_id]

    g_contacts = orm.get_contacts_in_group(group)  # Get contacts in group from DB
    if not g_contacts:  # Check if there are no contacts in the group
        all_contacts = orm.get_contact_list()
        if not all_contacts:  # If there are no contacts at all
            app.contact.create(Contact(firstname="NewContactForGroup"))
            all_contacts = orm.get_contact_list()

        contact_id = random.choice(all_contacts).id  # Get a random contact ID
        app.contact.add_contact_to_group(contact_id, group.id)  # Add contact to group
        g_contacts = orm.get_contacts_in_group(group)  # Refresh the list of contacts in the group

    # Ensure we have contacts in the group before trying to delete one
    if g_contacts:
        contact_to_delete = random.choice(g_contacts)  # Choose a random contact to delete
        app.contact.del_contact_from_group(contact_to_delete.id, group.id)

        # Refresh the contacts in the group after deletion
        g_contacts_after_deletion = orm.get_contacts_in_group(group)
        assert contact_to_delete not in g_contacts_after_deletion, "Contact was not deleted from the group."


