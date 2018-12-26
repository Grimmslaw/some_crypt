#!/usr/bin/env python3

# ==> STL Imports
from importlib import import_module

# ==> Core/Local Imports
from args.args import parse
from some_crypt.util.file_io import read_txt_file


def encrypt(cipher_module, target: str,
            key: int or str, target_type: str,
            strip_frmt=False) -> str:
    assert target_type in ['string', 'file']

    if target_type is 'file':
        plaintext = read_txt_file(target)
    else:
        plaintext = target

    return cipher_module.encrypt(plaintext, key, strip_frmt=strip_frmt)


def decrypt(cipher_module, target: str, key: int or str, target_type: str, strip_frmt=True) -> str:
    # TODO:
    pass


def main():
    argv = parse()
    assert argv.mode in ['encrypt', 'decrypt']

    cipher_module = import_module(f".{argv.cipher}", "some_crypt.ciphers")
    res = globals()[argv.mode](cipher_module, argv.target, argv.key, argv.target_type, argv.strip_frmt)

    if argv.output is None:
        print(res)
    else:
        # TODO: write to argv.output location
        pass


if __name__ == "__main__":
    main()
