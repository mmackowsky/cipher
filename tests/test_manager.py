import unittest
from unittest.mock import patch

from functionalities.buffer import Buffer, Text
from functionalities.manager import Manager
from functionalities.rot import Rot


class TestManager(unittest.TestCase):
    def test_get_rot_type(self):
        with patch("builtins.input", return_value="rot13"):
            rot_type = Manager.get_rot_type()
            self.assertEqual(rot_type, "rot13")

        with patch("builtins.input", return_value="rot47"):
            rot_type = Manager.get_rot_type()
            self.assertEqual(rot_type, "rot47")

        with patch("builtins.input", side_effect=["random_input", "rot13"]):
            rot_type = Manager.get_rot_type()
            self.assertEqual(rot_type, "rot13")

    def test_process_text(self):
        with patch.object(Rot, "encrypt_decrypt", return_value="encrypted_text"):
            Manager.process_text("text", "rot13", "status")
            expected_text = Text(
                txt="text", result="'grkg'", rot_type="Rot13", status="status"
            )
            self.assertEqual(Buffer.data[0].__dict__, expected_text.__dict__)

        with patch.object(Rot, "encrypt_decrypt", return_value="encrypted_text"):
            Manager.process_text("text", "rot47", "status")
            expected_text = Text(
                txt="text", result="'E6IE'", rot_type="Rot47", status="status"
            )
            self.assertEqual(Buffer.data[1].__dict__, expected_text.__dict__)
