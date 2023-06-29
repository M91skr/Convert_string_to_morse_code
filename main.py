morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '.......', '.': '.-.-.-',
              ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
              '&': '.-..', ':': '---...', ';': '-.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.'}

final_message = ''

mors_char = []

output = 'Service not found'


def text_to_mors():
    """
    Function to convert text to Morse code
    In this function, a string containing text with English alphabet is received from the user. Then character to
    character is translated and finally the corresponding morse code is returned.
    :return:
    final_message is of type string and is the only thing the function returns
    """
    message = input('Please write your text:\n').upper()
    char_list = list(message)
    for char in char_list:
        for key in morse_code:
            if char == key:
                mors_char.append(morse_code[char])
                mors_char.append(' ')
            if char not in morse_code:
                raise TypeError(f'Variable {char} is not defined!')
    final_message = "".join(mors_char)
    return final_message


def mors_to_text():
    """
    Function to convert morse code to text
    In this function, a string containing Morse code is received from the user. Then character to character is
    translated and finally the output sentence/word is returned.
    :return:
    final_message is of type string and is the only thing the function returns
    """
    message = input('Please enter your morse code:\n')
    morse_list = message.strip().split(' ')
    for morse in morse_list:
        if morse in morse_code.values():
            """
            Converting a dictionary values help us to find the equivalent key based on the index
            Dictionary values and keys do not support look up by index.
            """
            index_of_char = list(morse_code.values()).index(morse)
            alpha = list(morse_code.keys())[index_of_char]
            mors_char.append(alpha)
        if morse not in morse_code.values():
            raise TypeError(f'Variable {morse} is not defined!')
    final_message = "".join(mors_char)
    return final_message


print('Hi, welcome!\nWith this program, you can convert your text to Morse code and vice versa.\nYou can use this '
      'program to convert a complete word or sentence.\nNote: Characters such as @, $, +, ... are not covered in this '
      'program and their textual equivalents should be used.')
srv = input("If you want text to convert, write 'T' and if you want Morse code to convert, write 'M':\n").upper()
if srv == 'T':
    output = text_to_mors()
elif srv == 'M':
    output = mors_to_text()
print(output)
