from buffer import Text, Buffer
import json


class Filehandler:
    @staticmethod
    def add_data_to_file(buffer):
        file_name = input("Type file name: ")
        with open(f"{file_name}.txt", "w+") as file:
            for line in buffer:
                file.writelines(f"{str(line)}\n")

    @staticmethod
    def read_file():
        try:
            file_name = input("Type file to read: ")
            with open(f"{file_name}.txt", "r") as file:
                file.readlines()
        except FileNotFoundError:
            print("File do not exist\n")
