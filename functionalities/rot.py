from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Union


class Rot(ABC):
    def __init__(self, text: str) -> None:
        self.text = text

    @abstractmethod
    def encrypt_decrypt(self) -> None:
        raise NotImplementedError

    @staticmethod
    def create_rot(text: str, rot_type: str) -> Union[Rot13, Rot47]:
        if rot_type == "rot13":
            return Rot13(text)
        elif rot_type == "rot47":
            return Rot47(text)


class Rot13(Rot):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    def __str__(self):
        return "Rot13"

    def encrypt_decrypt(self) -> str:
        result = ""
        for char in self.text:
            if char.isalpha():
                new_pos = ord(char.lower()) + 13
                if new_pos > ord("z"):
                    new_pos -= 26
                result += chr(new_pos).upper() if char.isupper() else chr(new_pos)
            else:
                result += char
        return result


class Rot47(Rot):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    def __str__(self):
        return "Rot47"

    def encrypt_decrypt(self) -> str:
        result = []
        for i in range(len(self.text)):
            j = ord(self.text[i])
            if 33 <= j <= 126:
                result.append(chr(33 + ((j + 14) % 94)))
            else:
                result.append(self.text[i])
        return "".join(result)
