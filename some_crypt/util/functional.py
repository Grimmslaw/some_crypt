def shift_with_wrap(char_to_shift: str, shift_amt: int, offset=65) -> str:
    char_to_shift = char_to_shift.upper()
    return chr((((ord(char_to_shift) - offset) + shift_amt) % 26) + offset)
