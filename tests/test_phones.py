import re
from random import randrange

def test_phones_on_home_page(app):
    index = randrange(app.contact.count_contacts())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

#direct assert take info from  view_page and edit_page and compare it
def test_phones_on_contact_view_page(app):
    index = randrange(app.contact.count_contacts())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    #assert contact_from_home_page.fax == clear(contact_from_edit_page.fax)

def clear(s):
    return re.sub("[()-]", "", s) #что на что заменить

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))