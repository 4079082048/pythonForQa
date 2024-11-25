from random import randrange

# compare contacts address from home_page and edit_page
def test_address_on_homepage(app):
    index = randrange(app.contact.count_contacts())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address

