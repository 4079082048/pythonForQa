import re
from random import randrange
from fixture.orm import ORMFixture
from model.contact import Contact

def test_compare_ui_db_contacts(app, orm):
    #index = randrange(app.contact.count_contacts())
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    # Проверяем, что длины списков совпадают
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for id in range (app.contact.count_contacts()):
        contact_from_home_page=contacts_from_home_page[id]
        contact_from_db=contacts_from_db[id]
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)



def clear(s):
    return re.sub("[()-]", "", s) #что на что заменить

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))



#stitching of all emails from edit_page: get emails, filter and if its not None, filter not empty.
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))

