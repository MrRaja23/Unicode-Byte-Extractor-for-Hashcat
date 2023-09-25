# MIT License
#
# Copyright (c) 2023 https://github.com/Nielymmah
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def unicode_to_hexstring(input_string):
    byte1_string = []  # Initialize a list to store byte1 values
    byte2_string = []  # Initialize a list to store byte2 values

    # Iterate through each character in the input string
    for char in input_string:
        # Encode the character to bytes using UTF-8 encoding
        char_bytes = char.encode('utf-8')

        # Split the bytes into two parts (byte1 and byte2)
        byte1 = char_bytes[0]
        byte2 = char_bytes[1] if len(char_bytes) > 1 else b'\x00'

        # Convert each byte to a hexadecimal string and append to the respective list
        byte1_string.append(f'{byte1:02X}')
        byte2_string.append(f'{byte2:02X}')

    # Join the hexadecimal strings of byte1 and byte2 and return as a tuple
    return ''.join(byte1_string), ''.join(byte2_string)

def remove_duplicates(hex_string):
    # Convert the hexadecimal string to a list of bytes
    bytes_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

    # Remove duplicate bytes while preserving the order
    unique_bytes = []
    for byte in bytes_list:
        if byte not in unique_bytes:
            unique_bytes.append(byte)

    # Join the unique bytes into a single hexadecimal string
    return ''.join(unique_bytes)

# Input Unicode string
unicode_string = "é¢¡£¤¥¦§¨©ª«¬­®¯°±²³´µ¶¹¸º»¼½¾¿ÀÁÂÃÄ×£"

# Get hexadecimal representations of byte1 and byte2
byte1_hex, byte2_hex = unicode_to_hexstring(unicode_string)

# Remove duplicates from both byte1 and byte2 hexadecimal strings
unique_byte1 = remove_duplicates(byte1_hex)
unique_byte2 = remove_duplicates(byte2_hex)

# Print the unique byte1 and byte2 values
print("Unique-Byte1:", unique_byte1)
print("Unique-Byte2:", unique_byte2)

# Use case "hashcat.exe -m 0 md5.hash -a 3 -1 "byte1" -2 "byte2" -3 ?1?2 --hex-charset 'ikn?3w?3myk?3y!' -o SolvedMD5.txt" 
# Specify two mask and a third combining the first two for use in --hex-charset mask
