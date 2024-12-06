import pytest
from data.contacts import testdata
from tests.conftest import check_ui


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_to_group(app, db, data_contacts, check_ui):
    contact = data_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_contact_to_group(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
