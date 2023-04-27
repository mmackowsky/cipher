from dataclasses import dataclass
from typing import List


@dataclass
class Text:
    txt: str
    result: str
    rot_type: str
    status: str

    def __str__(self):
        return f"Text: {self.txt}, result: {self.result}, ROT: {self.rot_type}. Status: {self.status}"

    def __repr__(self):
        return f"Text(text={self.txt}, result={self.result}, rot_type={self.rot_type}, status={self.status})"


class Buffer:
    data: List[Text] = []

    @staticmethod
    def add(value: Text) -> None:
        Buffer.data.append(value)

    def show(self) -> None:
        if not self.data:
            print("Buffer is empty.")
        for count, element in enumerate(self.data, start=1):
            print(count, element)

    def remove_element(self) -> None:
        while True:
            try:
                element_to_remove = (
                    int(input("Type number of element you want to remove: ")) - 1
                )
                del self.data[element_to_remove]
                break
            except (ValueError, IndexError):
                print("Element do not exist on list")
                back = input("If you want back just type 'back', else press ENTER: ")
                if back == "back":
                    break
                continue
