from sys import maxsize
class Contact:

    def __init__(self, firstname=None, lastname=None, company=None, address=None, mobile=None, nickname=None, title=None, id = None, homephone = None, mobilephone = None, workphone = None, secondaryphone = None, fax = None, all_phones_from_home_page = None, email = None, email2 = None, email3 = None, homepage = None, all_emails_from_home_page = None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.nickname = nickname
        self.title = title
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

        # return max id or max value
    def id_or_max(self):
            if self.id:
                return int(self.id)
            else:
                return maxsize