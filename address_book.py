import csv

from address import Address
from work_address import WorkAddress


class AddressBook:

    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        if isinstance(address, Address):
            self.addresses.append(address)
        else:
            raise TypeError

    def find(self, search_phrase):
        self.sort()
        results = []
        for address in self.addresses:
            address_attributes = [address.person, address.city, address.street, address.house_no]
            if isinstance(address, WorkAddress):
                address_attributes.append(address.company)
            if search_phrase.upper() in " ".join(address_attributes).upper():
                results.append(address)
        return results

    def sort(self):
        for i in range(1,len(self.addresses)):
            j = i
            temp = self.addresses[j]
            while j > 0 and temp < self.addresses[j-1]:
                self.addresses[j] = self.addresses[j-1]
                j=j-1
            self.addresses[j] = temp

    @staticmethod
    def create_from_csv(list_name, csv_path):
        address_book = AddressBook(list_name)
        list_of_addresses = []
        with open(csv_path, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                list_of_addresses.append(row)
        for address in list_of_addresses:
            if address[-1] == "":
                address_book.addresses.append(Address(*address[:-1]))
            else:
                address_book.addresses.append(WorkAddress(*address))
        return address_book

    def save_to_csv(self):
        with open(self.name + ".csv", "w") as f:
            f.write("person,city,street,house_no,company\n")
            for address in self.addresses:
                address_data = [address.person, address.city, address.street, address.house_no]
                if isinstance(address, WorkAddress):
                    address_data.append(address.company)
                else:
                    address_data.append("")
                f.write(",".join(address_data)+"\n")

    def __str__(self):
        for address in self.addresses:
            if isinstance(address, WorkAddress):
                print(WorkAddress.get_full_address(address))
            else:
                print(Address.get_full_address(address))
