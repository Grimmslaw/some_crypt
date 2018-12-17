#!/usr/bin/env python3
from args.args import parse
from util.file_io import read_txt_file


def encrypt(cipher_module, target: str, key: int or str, target_type: str) -> str:
    # print(f"Encrypting '{target}' with {cipher_module.__name__.split('.')[-1]} and key: '{key}'")
    assert target_type in ['string', 'file']

    if target_type is 'file':
        plaintext = read_txt_file(target)
    else:
        plaintext = target

    return cipher_module.encrypt(plaintext, key)


def decrypt(cipher_module, target: str, key: int or str, target_type: str) -> str:
    # TODO:
    pass


def main():
    # TODO: sanitize inputs
    argv = parse()
    res = globals()[argv.mode](globals()[argv.cipher], argv.target, argv.key)


if __name__ == "__main__":
    main()
