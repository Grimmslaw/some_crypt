import re
from ..util.functional import shift_with_wrap, keygen


def __encrypt_str(plaintext: str, keyword: str) -> str:
    ciphertext = ""

    _pt_stripped = (re.sub(r'[^a-zA-Z0-9]', "", plaintext)).upper()
    autokey = keyword.upper() + _pt_stripped

    keytext = keygen(autokey)
    for _pt_char in plaintext:
        if 65 <= ord(_pt_char) <= 90:
            # uppercase block
            _key_char_ord = ord(next(keytext))
            ciphertext += shift_with_wrap(_pt_char, (_key_char_ord % 65))
        elif 97 <= ord(_pt_char) <= 122:
            # lowercase block
            _key_char_ord = ord(next(keytext))
            ciphertext += shift_with_wrap(_pt_char.upper(), (_key_char_ord % 65)).lower()
        else:
            # any other block
            ciphertext += _pt_char

    return ciphertext


def __encrypt_strip_frmt(plaintext: str, keyword: str) -> str:
    ciphertext = ""

    plaintext = (re.sub(r'[^a-zA-Z0-9]', "", plaintext)).upper()
    autokey = keyword.upper() + plaintext

    keytext = keygen(autokey)
    for _pt_char in plaintext:
        _key_char_ord = ord(next(keytext))
        ciphertext += shift_with_wrap(_pt_char, (_key_char_ord % 65))

    return ciphertext


def encrypt(plaintext: str, keyword: str, strip_frmt=False) -> str:
    if strip_frmt:
        return __encrypt_strip_frmt(plaintext, keyword)
    else:
        return __encrypt_str(plaintext, keyword)
