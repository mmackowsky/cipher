class Menu:
    MAIN_MENU = {
        "1": "ROT13/ROT47",
        "2": "Buffer options",
        "3": "File Handler options",
        "4": "Exit",
    }

    ROT_MENU = {"1.": "Encrypt", "2.": "Decrypt", "3.": "Return"}

    BUFFER_MENU = {"1.": "Show", "2.": "Remove element", "3.": "Return"}

    FILE_HANDLER_MENU = {
        "1.": "Make file",
        "2.": "Read file",
        "3.": "Add data to file",
        "4.": "Remove element from file",
        "5.": "Remove all elements from file",
        "6.": "Remove file",
        "7.": "Return",
    }

    @staticmethod
    def show_menu(menu) -> None:
        for key, value in menu.items():
            print(f"{key}: {value}")
