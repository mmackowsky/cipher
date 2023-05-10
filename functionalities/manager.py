from functionalities.buffer import Buffer, Text
from functionalities.file_handler import Filehandler
from functionalities.menu import Menu
from functionalities.rot import Rot


class Manager:
    @staticmethod
    def get_rot_type():
        while True:
            choose = input("Choose ROT (type rot13 or rot47): ")
            if choose in ["rot13", "rot47"]:
                return choose
            print("Wrong data! Type 'rot13' or 'rot47'.\n")

    @staticmethod
    def process_text(txt, rot_type, status):
        rot = Rot.create_rot(text=txt, rot_type=rot_type)
        rot.encrypt_decrypt()
        value = Text(
            txt=txt,
            result=rot.encrypt_decrypt().__repr__(),
            rot_type=rot.__str__(),
            status=status,
        )
        Buffer.add(value)

    @staticmethod
    def encrypt_text():
        choose = Manager.get_rot_type()
        txt = input("Type text: ")
        Manager.process_text(txt, choose, "encrypted")

    @staticmethod
    def decrypt_text():
        choose = Manager.get_rot_type()
        txt = input("Type text: ")
        Manager.process_text(txt, choose, "decrypted")

    @staticmethod
    def rots_options():
        while True:
            Menu.show_menu(Menu.ROT_MENU)
            user_command = input("Choose: ")
            match user_command:
                case "1":
                    Manager.encrypt_text()
                case "2":
                    Manager.decrypt_text()
                case "3":
                    break
                case _:
                    print("Option does not exist.")

    @staticmethod
    def file_handler_options() -> None:
        file_handler = Filehandler()
        while True:
            Menu.show_menu(Menu.FILE_HANDLER_MENU)
            user_command = input("Choose option: ")
            match user_command:
                case "1":
                    file_handler.make_file(Buffer.data)
                    print(f"File {file_handler.get_file_name()} has been made.\n")
                case "2":
                    file_handler.read_file()
                case "3":
                    file_handler.add_new_data(Buffer.data)
                case "4":
                    file_handler.remove_element()
                case "5":
                    file_handler.remove_all_data()
                case "6":
                    file_handler.remove_file()
                case "7":
                    break
                case _:
                    print("Wrong option.")
            print(30 * "----")

    @staticmethod
    def buffer_options() -> None:
        buff = Buffer()
        while True:
            Menu.show_menu(Menu.BUFFER_MENU)
            user_command = input("Choose option: ")
            match user_command:
                case "1":
                    buff.show()
                case "2":
                    buff.remove_element()
                case "3":
                    break
                case _:
                    print("Invalid option.")
            print(30 * "----")

    @staticmethod
    def start() -> None:
        print("Welcome in CIPHER.")
        while True:
            Menu.show_menu(Menu.MAIN_MENU)
            menu_command = input("Choose option from MENU: ")
            match menu_command:
                case "1":
                    Manager.rots_options()
                case "2":
                    Manager.buffer_options()
                case "3":
                    Manager.file_handler_options()
                case "4":
                    print("See you soon!")
                    exit()
                case _:
                    print("Invalid option.")
            print(30 * "----")
