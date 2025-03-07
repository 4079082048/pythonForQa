from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f =a #прочитали опции


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation  # + " "*10
    return prefix + "".join([random.choice(symbols)
                             for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [Group(name=random_string("=name=", 10), header=random_string("=header=", 10), footer=random_string("=footer=", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)#склеивается путь в генератору, переход в корень проекта, относит путь к файлу параметра
#with open(file, "w") as out:
#    out.write(json.dumps(testdata, default=lambda  x: x.__dict__, indent=2)) #__dict__ хранит свойства из полей которые присваиваем в __init__

with open(file, "w") as f_out:
        jsonpickle.set_encoder_options("json", indent=2)
        f_out.write(jsonpickle.encode(testdata))