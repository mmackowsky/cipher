from abc import ABC, abstractmethod
from filehandler.filehandler import Buffer


class Rot(ABC):
    def __init__(self, text: str) -> None:
        self.text = text

    @abstractmethod
    def encrypt_decrypt(self) -> str:
        raise NotImplementedError

    @staticmethod
    def create_rot(text: str, rot_type: str):
        if rot_type == "rot13":
            return Rot13(text)
        elif rot_type == "rot47":
            return Rot47(text)


class Rot13(Rot):
    def __init__(self, text: str) -> None:
        super().__init__(text)

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
        Buffer().buffer.append([self.text, result])
        return result


class Rot47(Rot):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    def encrypt_decrypt(self) -> str:
        x = []
        for i in range(len(self.text)):
            j = ord(self.text[i])
            if 33 <= j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(self.text[i])
        Buffer().buffer.append([self.text, "".join(x)])
        return "".join(x)


rot13 = Rot13("abc")
rot47 = Rot47("abc")
print(rot13.encrypt_decrypt())
print(rot47.encrypt_decrypt())
print(Buffer().buffer)
