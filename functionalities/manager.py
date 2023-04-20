from functionalities.rot import Rot
from functionalities.buffer import Text, Buffer
from functionalities.file_handler import Filehandler


class Menu:
    OPTIONS = {
        "1": "Encrypt",
        "2": "Decrypt",
        "3": "Show actual data.",
        "4": "Save to file",
        "5": "Read file.",
        "6": "Return",
    }

    def show_menu(self) -> None:
        for key, value in self.OPTIONS.items():
            print(f"{key}: {value}")


class Manager:
    @staticmethod
    def start():
        print("Welcome in Cipher.\n")
        while True:
            while True:
                choose = input(
                    "Choose ROT (type rot13 or rot47):\nIf you want exit, type: 'exit'."
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
                            txt=txt, rot_type=rot.__repr__(), status="encrypted"
                        )
                        Buffer.add(value)
                        print("Data encrypted\n")
                    case ["2"]:
                        rot.encrypt_decrypt()
                        value = Text(
                            txt=txt, rot_type=rot.__repr__(), status="decrypted"
                        )
                        Buffer.add(value)
                        print("Data decrypted\n")
                    case ["3"]:
                        Buffer().show()
                    case ["4"]:
                        Filehandler.add_data_to_file(Buffer.data)
                    case ["5"]:
                        Filehandler.read_file()
                    case ["6"]:
                        break
