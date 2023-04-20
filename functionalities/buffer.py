from dataclasses import dataclass
from functionalities.rot import Rot, Rot13, Rot47
from typing import Optional


@dataclass
class Text:
    txt: str
    rot_type: str
    status: str

    def __repr__(self):
        return f"[text={self.txt}, rot_type={self.rot_type}, status={self.status}]"


class Buffer:
    data = []

    @staticmethod
    def add(value: Text):
        Buffer.data.append(value)

    def show(self):
        for count, element in enumerate(self.data):
            print(count, element)

    def remove_element(self):
        while True:
            try:
                element_to_remove = int(
                    input("Type number of element you want to remove: ")
                )
                self.data.remove(element_to_remove)
                break
            except ValueError:
                print("Element do not exist on list")
                back = input("If you want back just type 'back', else press ENTER: ")
                if back == "back":
                    break
                else:
                    continue
