class Contact:

    def __init__(self, firstname=None, lastname=None, company=None, address=None, mobile=None, nickname=None, title=None, id =None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.nickname = nickname
        self.title = title
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname