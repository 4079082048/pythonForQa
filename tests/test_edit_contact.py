# -*- coding: utf-8 -*-
from sys import maxsize
from model.contact import Contact


def test_edit_contact_firstname(app):
        old_contacts = app.contact.get_contact_list()
        #if app.contact.count() == 0:
        #        app.contact.create(Contact(firstname="TestCount2", lastname="TestCountZolotova2"))
        app.contact.edit_first_contact(Contact(firstname="Ivanna"))
        new_contacts = app.contact.get_contact_list() # Call the method
        assert len(old_contacts)  == len(new_contacts) # Check that the number of contacts is unchanged
        old_contacts[0].firstname = "Ivanna" # Update the first contact's firstname in old_contacts to match the edit
      #  def id_or_max(gr):
      #          if gr.id:
      #                  return int(gr.id)
      #          else:
      #                  return maxsize
      #  assert sorted(old_contacts, key=id_or_max) == sorted(new_contacts, key=id_or_max) # Check that the contact list matches after editing
        app.session.logout()



def test_edit_contact_lastname(app):
        app.open_home_page()
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="TestCount2", lastname="TestCountZolotova2"))
        app.contact.edit_first_contact(Contact(lastname="Gladisheva"))


