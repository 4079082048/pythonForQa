from generator.group import random_string
from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f =a #прочитали опции


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation  # + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#Contact(firstname="Sa", lastname="La", nickname="Ln", title="mm", company="ai", address="ad", homephone="312", mobilephone="2342342", workphone="5522", fax="23", email="d@a.com", email2="d2@a.com", email3="d3@a.com", homepage="www.a.com")
testdata = [Contact(firstname="", lastname="", nickname="", title="", company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="", email3="", homepage="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10),company=random_string("company", 10), address=random_string("address", 10), homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10), fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homephone", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)#склеивается путь в генератору, переход в корень проекта, относит путь к файлу параметра
#with open(file, "w") as out:
#    out.write(json.dumps(testdata, default=lambda  x: x.__dict__, indent=2)) #__dict__ хранит свойства из полей которые присваиваем в __init__

with open(file, "w") as f_out:
        jsonpickle.set_encoder_options("json", indent=2)
        f_out.write(jsonpickle.encode(testdata))