#!/usr/bin/env python3
import unittest
from ..ciphers.vigenere import encrypt


class TestVigenereMethods(unittest.TestCase):

    def test_vigenere_encrypt_key_length_less(self):
        res = encrypt("abc", "yz")
        self.assertEqual(res, "yaa", f"Expected 'yaa'. Got '{res}'.")
        res_strip = encrypt("abc", "yz", strip_frmt=True)
        self.assertEqual(res_strip, "YAA", f"Expected 'YAA'. Got '{res_strip}'.")

    def test_vigenere_encrypt_key_mixed_case(self):
        res = encrypt("abc", "Yz")
        self.assertEqual(res, "yaa", f"Expected 'yaa'. Got '{res}'.")
        res_strip = encrypt("abc", "Yz", strip_frmt=True)
        self.assertEqual(res_strip, "YAA", f"Expected 'YAA'. Got '{res_strip}'.")

    def test_vigenere_encrypt_key_length_equal(self):
        res = encrypt("abc", "xyz")
        self.assertEqual(res, "xzb", f"Expected 'xzb'. Got '{res}'.")
        res_strip = encrypt("abc", "xyz", strip_frmt=True)
        self.assertEqual(res_strip, "XZB", f"Expected 'XZB'. Got '{res_strip}'.")

    def test_vigenere_encrypt_key_length_more(self):
        res = encrypt("abc", "wxyz")
        self.assertEqual(res, "wya", f"Expected 'wya'. Got '{res}'.")
        res_strip = encrypt("abc", "wxyz", strip_frmt=True)
        self.assertEqual(res_strip, "WYA", f"Expected 'WYA'. Got '{res_strip}'.")

    def test_vigenere_encrypt_pt_contains_spaces(self):
        res = encrypt("abc efg", "key")
        self.assertEqual(res, "kfa oje", f"Expected 'kfa oje'. Got '{res}'.")
        res_strip = encrypt("abc efg", "key", strip_frmt=True)
        self.assertEqual(res_strip, "KFAOJE", f"Expected 'KFAOJE'. Got '{res_strip}'.")

    def test_vigenere_encrypt_pt_contains_symbols(self):
        res = encrypt("abcefg.", "key")
        self.assertEqual(res, "kfaoje.", f"Expected 'kfaoje.'. Got '{res}'.")
        res_strip = encrypt("abc efg.", "key", strip_frmt=True)
        self.assertEqual(res_strip, "KFAOJE", f"Expected 'KFAOJE'. Got '{res_strip}'.")

    def test_vigenere_encrypt_pt_contains_spaces_and_symbols(self):
        res = encrypt("abc efg.", "key")
        self.assertEqual(res, "kfa oje.", f"Expected 'kfa oje.'. Got '{res}'.")
        res_strip = encrypt("abc efg.", "key", strip_frmt=True)
        self.assertEqual(res_strip, "KFAOJE", f"Expected 'KFAOJE'. Got '{res_strip}'.")

    def test_vigenere_encrypt_pt_mixed_case(self):
        res = encrypt("Abc", "key")
        self.assertEqual(res, "Kfa", f"Expected 'Kfa'. Got '{res}'.")
        res_strip = encrypt("Abc", "key", strip_frmt=True)
        self.assertEqual(res_strip, "KFA", f"Expected 'KFA'. Got '{res_strip}'.")
