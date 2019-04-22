from unittest import TestCase
from abstract_strings_coder import StringsCoder

from bpe_coder import BPECoder


class TestBPECoder(TestCase):

    def setUp(self):
        # YOUR CODE HERE
        # DO NOT TOUCH OTHER METHODS
        self.coder_tool = BPECoder()

    def test_encode(self):
        s_to_encode = "окно"

        assert isinstance(self.coder_tool.encode(s_to_encode), str)

    def test_encode_2(self):
        s_to_encode = "окно"

        res = self.coder_tool.encode(s_to_encode)
        print(res)

    def test_decode(self):
        s_to_decode = "aloa"

        assert isinstance(self.coder_tool.decode(s_to_decode), str)

    def test_decode_2(self):
        s_to_decode = "aloa"

        res = self.coder_tool.decode(s_to_decode)
        print(res)

    def test_encode_decode(self):
        s_to_encode = "моногамно"

        assert self.coder_tool.decode(self.coder_tool.encode(s_to_encode)) == s_to_encode

    def test_inheritance(self):
        assert isinstance(self.coder_tool, StringsCoder)
