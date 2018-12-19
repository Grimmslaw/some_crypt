import re
from ..util.functional import shift_with_wrap


def __encrypt_str(plaintext: str, key: int) -> str:
    """Encrypt a `str` using a caesar shift, retaining formatting"""
    ciphertext = ""

    for letter in plaintext:
        if 65 <= ord(letter) <= 90:
            # uppercase block
            ciphertext += shift_with_wrap(letter, key)
        elif 97 <= ord(letter) <= 122:
            # lowercase block
            ciphertext += shift_with_wrap(letter, key).lower()
        else:
            # any other block
            ciphertext += letter

    return ciphertext


def __encrypt_strip_frmt(plaintext: str, key: int) -> str:
    """Encrypt a `str` using a caesar shift, stripping formatting"""
    ciphertext = ""
    plaintext = (re.sub(r'[^a-zA-Z0-9]', "", plaintext)).upper()

    for letter in plaintext:
        if 65 <= ord(letter) <= 122:
            ciphertext += shift_with_wrap(letter, key)
        else:
            ciphertext += letter

    return ciphertext


def encrypt(plaintext: str, key: int, strip_frmt=False) -> str:
    """
    Encrypt `:plaintext:` using a Caesar shift of size `:key:`.\n

    By default this method retains formatting (case, spaces, punctuation).
    For example, `encrypt('Some words.', 2)` => `'Uqog yqtfu.'`.\n

    If `:strip_frmt:` is `True`, instead, formatting is stripped, returning
    an all-caps, no-spaces, no-punctuation `str`. For example,
    `encrypt('Some words.', 2, strip_frmt=True)` => `'UQOGYQTFU'`.

    :param str plaintext:
        the text to be encrypted
    :param int key:
        the amount to shift `:plaintext:`
    :param bool strip_frmt:
        [opt; def=False] whether to strip formatting from `:plaintext:`

    :return:
        the encrypted `str`
    """
    if not isinstance(key, int):
        try:
            key = int(key)
        except ValueError:
            raise

    if strip_frmt:
        return __encrypt_strip_frmt(plaintext, key)
    else:
        return __encrypt_str(plaintext, key)
