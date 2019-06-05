#!/usr/local/bin/python3

"""
Unicoder

Version:
    1.0.0

Copyright:
    2019, Tony Smith (@smittytone)

License:
    MIT (terms attached to this repo)
"""

##########################################################################
# Program library imports                                                #
##########################################################################

import sys

##########################################################################
# Application-specific constants                                         #
##########################################################################

APP_VERSION = "1.0.0"

##########################################################################
# Functions                                                              #
##########################################################################

def de_code(code):
    """
    Process the specified code.

    Args:
        code (str): The UTF-8 character code (eg. 'U+10348')

    Returns:
        bool: Whether the op was successful (True) or not (False)
    """

    if code:
        # Remove the 'U+', if present
        code_head = code[:2]
        if code_head == "U+": code = code[2:]

        # Pad the hex with zeroes as needed
        if len(code) % 2 != 0: code = "0" + code
        if len(code) == 2: code = "00" + code

        # How many bytes are required for the string?
        num_bytes = 1
        code_val = int(code, 16)
        if 0x80 <= code_val <= 0x7FFF: num_bytes = 2
        if 0x800 <= code_val <= 0xFFFF: num_bytes = 3
        if code_val >= 0x10000: num_bytes = 4
        if code_val >= 0x10FFFF:
            print("ERROR -- Invalid UTF-8 code supplied (U+" + code + ")")
            return False

        if num_bytes == 1:
            byte_1 = int(code[-2:], 16)
            print(output([byte_1]))

        if num_bytes == 2:
            byte_1 = 0xC0 + ((code_val & 0xF0) >> 6)
            byte_2 = 0x80 + (code_val & 0x3F)
            print(output([byte_1, byte_2]))

        if num_bytes == 3:
            byte_1 = 0xE0 + ((code_val & 0xF000) >> 12)
            byte_2 = 0x80 + ((code_val & 0x0FC0) >> 6)
            byte_3 = 0x80 + (code_val & 0x3F)
            print(output([byte_1, byte_2, byte_3]))

        if num_bytes == 4:
            byte_1 = 0xF0 + ((code_val & 0x1C0000) >> 19)
            byte_2 = 0x80 + ((code_val & 0x03F000) >> 12)
            byte_3 = 0x80 + ((code_val & 0x000FC0) >> 6)
            byte_4 = 0x80 + (code_val & 0x3F)
            print(output([byte_1, byte_2, byte_3, byte_4]))

        return True
    return False

def output(the_bytes, as_squirrel=True):
    """
    Format the output string.

    Args:
        the_bytes   (list): The individual integer byte values.
        as_squirrel (bool): Should we output as Squirrel code? Default: True

    Returns:
        str: The formatted output.
    """

    out_str = "local unicodeString=\""
    end_str = "\";"
    if as_squirrel is False:
        out_str = ""
        end_str = ""
    for a_byte in the_bytes:
        out_str += "\\x{0:02X}".format(a_byte)
    return out_str + end_str


def show_help():
    '''
    Display Unicoder's help information.
    '''

    print("Unicoder " + APP_VERSION)
    print(" ")
    print("Unicoder converts UTF-8 character codes, eg. 'U+20AC' for €, to hex strings")
    print("that can be transferred between systems, eg. in JSON.")
    print(" ")
    print("Usage:")
    print("    unicoder.py [-h] [<UTF-8_code_1> <UTF-8_code_2> ... <UTF-8_code_n>]")
    print(" ")
    print("Options:")
    print("    -h / --help - Print spasm help information (this screen).")
    print(" ")


##########################################################################
# Main entry point                                                       #
##########################################################################

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for index, item in enumerate(sys.argv):
            if index > 0:
                if item in ("-h", "--help"):
                    show_help()
                    sys.exit(0)
                elif item[0] == "-":
                    print("ERROR -- unknown option specified (" + item + ")")
                    sys.exit(1)
                else:
                    result = de_code(item)
                    if result is False:
                        sys.exit(1)
    else:
        print("ERROR -- no UTF-8 chracter specified (eg. 'U+20AC')")
        sys.exit(1)
