from address_book import AddressBook
from address import Address
from work_address import WorkAddress

class Controller:
    main_menu = ['\n1. Create new address book',
                 '\n2. Open address book',
                 '\n0. Exit - closes the program',
                 '\nChoose option: ']

    address_book_menu = ['\n1. List addresses',
                         '\n2. Add a new address',
                         '\n3. Remove an address',
                         '\n4. Search for an address',
                         '\n5. Save this address book',
                         '\n0. Back to main menu',
                         '\nChoose option: ']

    @staticmethod
    def show_menu():
        menu_option = input(''.join(Controller.main_menu))
        while menu_option != '0':
            if menu_option == '1':
                Controller.show_submenu(new_address_book=True)

            elif menu_option == "2":
                Controller.show_submenu(new_address_book=False)

            else:
                print('\nWrong input. Try again')
                break

            menu_option = input(''.join(Controller.main_menu))

        exit('\nGoodbye!')

    @staticmethod
    def show_submenu(new_address_book=False):
        addresses = Controller.open_address_book(new_address_book)
        submenu_option = input(''.join(Controller.address_book_menu))
        while submenu_option != '0':
            if submenu_option == '1':
                AddressBook.__str__(addresses)
                input('\nPlease enter to continue...')
            elif submenu_option == '2':
                Controller.add_address(addresses)
                input('\nPlease enter to continue...')
            elif submenu_option == '3':
                pass

            elif submenu_option == '4':
                pass

            elif submenu_option == '5':
                pass

            else:
                print('\nWrong input. Try again')
                break

            submenu_option = input(''.join(Controller.address_book_menu))

    def open_address_book(new_address_book):
        if new_address_book == False:
            list_name = input('Gimmie name of existing address_book: ')
        else:
            list_name = input('Gimmie name of new address book: ')
        addresses = AddressBook.create_from_csv(list_name, list_name + '.csv')
        return addresses

    def create_address(): #not finished
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        city = input('Enter city: ')
        street = input('Enter street: ')
        house_no = input('House number: ')
        company = input('Enter company or leave empty: ')
        return Address.get_full_address([name + ' ' + surname, city, street, house_no, company])

    def add_address(addresses): #not finished
        address = Controller.create_address()
        addresses.add_address(Address(*address))
