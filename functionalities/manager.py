from functionalities.rot import Rot
from functionalities.buffer import Text, Buffer
from functionalities.file_handler import Filehandler


class Menu:
    OPTIONS = {
        "1": "Encrypt",
        "2": "Decrypt",
        "3": "Buffer options",
        "4": "File Handler options",
        "5": "Return",
    }

    def show_menu(self) -> None:
        for key, value in self.OPTIONS.items():
            print(f"{key}: {value}")


class Manager:
    @staticmethod
    def file_handler_options():
        file_handler = Filehandler()
        while True:
            file_handler.show_file_handler_menu()
            user_command = input("Choose option: ")
            match user_command.split():
                case ["1"]:
                    file_handler.make_file()
                    print(f"File {file_handler.file_name} has been made.\n")
                case ["2"]:
                    file_handler.read_file()
                case ["3"]:
                    file_handler.add_data_to_file(Buffer.data)
                case ["4"]:
                    file_handler.remove_line()
                case ["5"]:
                    file_handler.remove_all()
                case ["6"]:
                    file_handler.remove_file()
                case ["7"]:
                    break
                case _:
                    print("Invalid option.")
            print(30 * "----")

    @staticmethod
    def buffer_options():
        buff = Buffer()
        while True:
            buff.show_buffer_menu()
            user_command = input("Choose option: ")
            match user_command.split():
                case ["1"]:
                    buff.show()
                case ["2"]:
                    buff.remove_element()
                case ["3"]:
                    break
                case _:
                    print("Invalid option.")
            print(30 * "----")

    @staticmethod
    def start():
        while True:
            while True:
                choose = input(
                    "Choose ROT (type rot13 or rot47), if you want exit, type: 'exit': "
                )
                if choose == "rot13" or choose == "rot47":
                    break
                elif choose == "exit":
                    exit()
                else:
                    print("Wrong data! Type 'rot13' or 'rot47'.\n")
            txt = input("Type text: ")
            rot = Rot.create_rot(text=txt, rot_type=choose)
            while True:
                print(rot)
                Menu().show_menu()
                menu_command = input("Choose option from MENU: ")
                match menu_command.split():
                    case ["1"]:
                        rot.encrypt_decrypt()
                        value = Text(
                            txt=txt,
                            result=rot.encrypt_decrypt().__repr__(),
                            rot_type=rot.__repr__(),
                            status="encrypted",
                        )
                        Buffer.add(value)
                        print("Data encrypted\n")
                    case ["2"]:
                        rot.encrypt_decrypt()
                        value = Text(
                            txt=txt,
                            result=rot.encrypt_decrypt().__repr__(),
                            rot_type=rot.__repr__(),
                            status="decrypted",
                        )
                        Buffer.add(value)
                        print("Data decrypted\n")
                    case ["3"]:
                        Manager.buffer_options()
                    case ["4"]:
                        Manager.file_handler_options()
                    case ["5"]:
                        break
                    case _:
                        print("Invalid option.")
                print(30 * "----")


Manager.start()
