#!/usr/bin/env python3
import unittest
from ciphers.caesar import caesar_encrypt


class TestCaesarMethods(unittest.TestCase):

    def test_caesar_encrypt_min_key(self):
        res = caesar_encrypt("abc", 1)
        self.assertEqual(res, "bcd", f"Expected 'bcd'. Got '{res}'.")

    def test_caesar_encrypt_zero_key(self):
        res = caesar_encrypt("abc", 0)
        self.assertEqual(res, "abc", f"Expected 'abc'. Got '{res}'.")

    def test_caesar_encrypt_neg_key(self):
        res = caesar_encrypt("abc", -1)
        self.assertEqual(res, "zab", f"Expected 'abc'. Got '{res}'")

    def test_caesar_encrypt_wrap_in_middle(self):
        res = caesar_encrypt("abc", 25)
        self.assertEqual(res, "zab", f"Expected 'zab'. Got '{res}'.")

    def test_caesar_encrypt_wrap_from_start(self):
        res = caesar_encrypt("abc", 30)
        self.assertEqual(res, "efg", f"Expected 'efg'. Got '{res}'.")

    def test_caesar_encrypt_with_space(self):
        res = caesar_encrypt("abc def", 1)
        self.assertEqual(res, "bcd efg", f"Expected 'bcd efg'. Got '{res}'.")


if __name__ == '__main__':
    unittest.main()