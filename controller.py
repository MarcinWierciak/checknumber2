from address_book import AddressBook


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
                Controller.show_submenu()
            elif menu_option == "2":
                Controller.show_submenu()
            else:
                print('\nWrong input. Try again')
                break
            menu_option = input(''.join(Controller.main_menu))
        exit('\nGoodbye!')

    @staticmethod
    def show_submenu():
        submenu_option = input(''.join(Controller.address_book_menu))
        while submenu_option != '0':
            if submenu_option == '1':
                ab.__str__()
            elif submenu_option == '2':
                pass
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
