# -*- coding: utf-8 -*-
from model.contact import Contact
#import random
#import string

#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation
#    return prefix + "".join([random.choice(symbols)
#                             for i in range(random.randrange(maxlen))])

#testdata = ([Contact(firstname="", lastname="", nickname="", title="", company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="", email3="", homepage="")] +
#            [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10), homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10), fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homepage", 10),)
#                                                     for i in range(5)])
from model.contact import Contact

testdata = [
        Contact(firstname="Sa", lastname="La", nickname="Ln", title="mm", company="ai", address="ad", homephone
        ="312", mobilephone="2342342", workphone="5522", fax="23", email="d@a.com", email2="d2@a.com", email3="d3@a.com", homepage="www.a.com"),
        Contact(firstname="Sb", lastname="Lb", nickname="Lm", title="nn", company="ia", address="da", homephone="123", mobilephone="432423", workphone="2255", fax="523", email="dr@a.com", email2="de@a.com", email3="dw@a.com", homepage="www.b.com")
]