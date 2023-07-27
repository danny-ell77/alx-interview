#!/usr/bin/python3
"""UTF-8 Validator"""


def validUTF8(data):
    """Validate UTF-8"""
    num_bytes = 0

    for num in data:
        # Check the first two bits of the byte to identify the number of bytes in the current character
        if num_bytes == 0:
            if num >> 7 == 0:
                num_bytes = 1
            elif num >> 5 == 0b110:
                num_bytes = 2
            elif num >> 4 == 0b1110:
                num_bytes = 3
            elif num >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False
            num_bytes -= 1
        else:
            # Check that the current byte is a continuation byte (first two bits are '10')
            if num >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If all bytes have been successfully checked, return True
    return num_bytes == 0
