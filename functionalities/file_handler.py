import json
import os
from dataclasses import asdict
from typing import List

from functionalities.buffer import Text


class Filehandler:
    @staticmethod
    def get_file_name() -> str:
        file_name = input("Type file name: ")
        return file_name

    @staticmethod
    def make_file(buffer: List[Text]):
        file_name = Filehandler.get_file_name()
        with open(f"files/{file_name}.json", "w") as json_file:
            saved_data = []
            for values in buffer:
                buffer_dict = asdict(values)
                saved_data.append(buffer_dict)
            json.dump(saved_data, json_file, indent=4)

    @staticmethod
    def read_file() -> None:
        file_name = Filehandler.get_file_name()
        try:
            with open(f"files/{file_name}.json") as json_file:
                read_data = json.load(json_file)
                for count, value in enumerate(read_data, 1):
                    print(count, value)
        except json.decoder.JSONDecodeError:
            print("File is empty.")
        except FileNotFoundError:
            print("File do not exist\n")

    @staticmethod
    def add_new_data(buffer: List[Text]) -> None:
        file_name = Filehandler.get_file_name()
        try:
            with open(f"files/{file_name}.json") as json_file:
                data = json.load(json_file)

            for values in buffer:
                data_to_add = asdict(values)
                data.append(data_to_add)

            with open(f"files/{file_name}.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
        except FileNotFoundError:
            print("File do not exist\n")

    @staticmethod
    def remove_element() -> None:
        file_name = Filehandler.get_file_name()
        with open(f"files/{file_name}.json", "r") as json_file:
            data = json.load(json_file)

        while True:
            try:
                index = input("Which element you want to remove: ")
                del data[int(index) - 1]
                print("Element removed")
                break
            except json.decoder.JSONDecodeError:
                print("File is empty.")
                break
            except IndexError:
                print("Element do not exist on the list.")

        with open(f"files/{file_name}.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def remove_all_data() -> None:
        file_name = Filehandler.get_file_name()
        with open(f"files/{file_name}.json", "w") as json_file:
            json.dump("", json_file)
        print("Data removed.\n")

    @staticmethod
    def remove_file() -> None:
        file_name = Filehandler.get_file_name()
        while True:
            try:
                question = input(
                    f"Are you sure to delete {file_name} file? This will be irreversible. (Y/N): "
                )
                if question.lower() == "y":
                    os.remove(f"files/{file_name}.json")
                    print("File removed.\n")
                    break
                elif question.lower() == "n":
                    print("Operation stopped.")
                    break
                else:
                    print("Wrong data. Type Y or N")
            except FileNotFoundError:
                print("File do not exist.")
