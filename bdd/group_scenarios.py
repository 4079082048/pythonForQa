from pytest_bdd import scenario
from pytest_bdd import given, when, then, parsers
from .group_steps import *

@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass

@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass