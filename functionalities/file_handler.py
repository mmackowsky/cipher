from buffer import Text, Buffer
import json
import os


class Filehandler:
    FILE_HANDLER_MENU = {
        "1.": "Make file",
        "2.": "Read file.",
        "3.": "Add data",
        "4.": "Remove line",
        "5.": "Remove all",
        "6.": "Remove file",
        "7.": "Return",
    }

    def __init__(self) -> None:
        self.file_name = input("Type file name: ")

    def show_file_handler_menu(self):
        for key, value in self.FILE_HANDLER_MENU.items():
            print(key, value)

    def make_file(self):
        with open(f"{self.file_name}.txt", "w+") as file:
            file.write("")

    def read_file(self) -> None:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                for count, line in enumerate(file.readlines()):
                    print(count, line)
        except FileNotFoundError:
            print("File do not exist\n")

    def add_data_to_file(self, buffer: list[str]) -> None:
        try:
            with open(f"{self.file_name}.txt", "a") as file:
                for line in buffer:
                    file.writelines(f"{str(line)}\n")
        except FileNotFoundError:
            print("File do not exist\n")

    def remove_line(self) -> None:
        self.read_file()
        line_to_remove = int(input("Type number of element which you want remove: "))
        with open(f"{self.file_name}.txt", "r") as file:
            lines = file.readlines()

        with open(f"{self.file_name}.txt", "w") as file:
            for i, line in enumerate(lines):
                if i != line_to_remove:
                    file.write(line)

    def remove_all(self) -> None:
        with open(f"{self.file_name}.txt", "w") as file:
            file.write("")

    def remove_file(self) -> None:
        while True:
            try:
                question = input(
                    f"Are you sure to delete {self.file_name} file? This will be irreversible. (Y/N): "
                )
                if question.lower() == "y":
                    os.remove(f"{self.file_name}.txt")
                    print("File removed.")
                    break
                elif question.lower() == "n":
                    print("Operation stopped.")
                    break
                else:
                    print("Wrong data. Type Y or N")
            except FileNotFoundError:
                print("File do not exist.")
