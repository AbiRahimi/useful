import hashlib
import unittest


class ToHash(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def set_parameters(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_arg_value(self):
        string = str()
        for arg in self.args:
            string += str(arg) + '_'

        for key in self.kwargs:
            string += str(key) + ':' + str(self.kwargs.get(key)) + '_'

        return string

    def get_hash_code(self):
        string = self._get_arg_value()
        return hashlib.sha256(string.encode('utf-8')).hexdigest()


class TestCase(unittest.TestCase):
    def test_to_hash(self):
        h0 = '6a770e6502742656553eef6f4ed1355e93f36db5e7546a54a78c4ff9d122a08a'
        h1 = ToHash('Signalman', User='AbiRQK', val=1.05).get_hash_code()
        self.assertEqual(h0, h1)


if __name__ == '__main__':
    unittest.main()
