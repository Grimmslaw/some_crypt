from util.functional import shift_with_wrap


def __caesar_encrypt_str(plaintext_input, key: int) -> str:
    ciphertext = ""

    for letter in plaintext_input:
        if 65 <= ord(letter) <= 90:
            block = "upper"
        elif 97 <= ord(letter) <= 122:
            block = "lower"
        else:
            block = "other"

        if block == "lower":
            res = shift_with_wrap(letter, key).lower()
        elif block == "upper":
            res = shift_with_wrap(letter, key)
        else:
            res = letter

        ciphertext += res

    return ciphertext


def caesar_encrypt(plaintext_input, key: int):
    # TODO: make this a dispatcher
    return __caesar_encrypt_str(plaintext_input, key)
