
class Address:

    def __init__(self, person, city, street, house_no):
        self.person = person
        self.city = city
        self.street = street
        self.house_no = house_no

    def get_full_address(self):
        return '{}, {}, {} {}'.format(self.person, self.city, self.street, self.house_no)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __gt__(self, other):
        return self.get_full_address() > other.get_full_address()

    def __ge__(self, other):
        return self.get_full_address() >= other.get_full_address()

    def __lt__(self, other):
        return self.get_full_address() < other.get_full_address()

    def __le__(self, other):
        return self.get_full_address() <= other.get_full_address()

    def __eq__(self, other):
        return self.get_full_address() == other.get_full_address()

    def __ne__(self, other):
        return self.get_full_address() != other.get_full_address()
