from rot import Rot, Rot13, Rot47
from abc import ABC, abstractmethod
import pytest


def test_create_rot13():
    rot = Rot.create_rot("abc", "rot13")

    assert isinstance(rot, Rot13)
    return rot


def test_create_rot47():
    rot = Rot.create_rot("abc", "rot47")

    assert isinstance(rot, Rot47)
    return rot


def test_rot13_encrypt_decrypt():
    rot13_encrypt = Rot13("abc")
    rot13_decrypt = Rot13("nop")

    assert rot13_encrypt.encrypt_decrypt() == "nop"
    assert rot13_decrypt.encrypt_decrypt() == "abc"


def test_rot47_encrypt_decrypt():
    rot47_encrypt = Rot47("abc")
    rot47_decrypt = Rot47("234")

    assert rot47_encrypt.encrypt_decrypt() == "234"
    assert rot47_decrypt.encrypt_decrypt() == "abc"


@pytest.mark.parametrize(
    "actual, expected", [("", ""), ("123", "123"), (";.,'[", ";.,'[")]
)
def test_rot13_should_return_correctly_not_alpha_values(actual, expected):
    rot13 = Rot13(actual)

    assert rot13.encrypt_decrypt() == expected
