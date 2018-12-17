#!/usr/bin/env python3
from ciphers.caesar import encrypt
from ciphers.vigenere import encrypt


def main():
    pt_str_list = ["abc", "abc efg", "abcefg.", "abc efg.", "Abc", "Abc efg", "Abcefg.", "Abc efg."]
    key_str_list = ["yz", "YZ", "Yz", "wxyz", "key", "Key", "KEY"]
    op_counter = 0
    for _pt in pt_str_list:
        encrypt(_pt, 1)
        op_counter += 1
        encrypt(_pt, 1, strip_frmt=True)
        op_counter += 1
        encrypt(_pt, 15)
        op_counter += 1
        encrypt(_pt, 15, strip_frmt=True)
        op_counter += 1
        encrypt(_pt, 28)
        op_counter += 1
        encrypt(_pt, 28, strip_frmt=True)
        op_counter += 1
        for _key in key_str_list:
            encrypt(_pt, _key)
            op_counter += 1
            encrypt(_pt, _key, strip_frmt=True)
            op_counter += 1
    print("\n----------")
    print(f"op_counter: {op_counter}")


if __name__ == '__main__':
    main()
