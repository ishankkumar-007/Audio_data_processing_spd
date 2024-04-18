from winsound import PlaySound
from time import sleep

morse_code_dictionary = {'A': '.-/', 'B': '-.../',
                         'C': '-.-./', 'D': '-../', 'E': './',
                         'F': '..-./', 'G': '--./', 'H': '..../',
                         'I': '../', 'J': '.---/', 'K': '-.-/',
                         'L': '.-../', 'M': '--/', 'N': '-./',
                         'O': '---/', 'P': '.--./', 'Q': '--.-/',
                         'R': '.-./', 'S': '.../', 'T': '-/',
                         'U': '..-/', 'V': '...-/', 'W': '.--/',
                         'X': '-..-/', 'Y': '-.--/', 'Z': '--../',
                         '1': '.----/', '2': '..---/', '3': '...--/',
                         '4': '....-/', '5': '...../', '6': '-..../',
                         '7': '--.../', '8': '---../', '9': '----./',
                         '0': '-----/', ',': '--..--/', '.': '.-.-.-/',
                         '?': '..--../', '/': '-..-./', '-': '-....-/',
                         '(': '-.--./', ')': '-.--.-/', ' ': '!', '': '/'}

morse_code_to_alphabet_dictionary = {
    x: y for y, x in morse_code_dictionary.items()}

md, mad = morse_code_dictionary, morse_code_to_alphabet_dictionary


def valid_morse(message):
    char_code_list = message.split(" ")
    return all(char_code in mad for char_code in char_code_list)


def encode():
    text = input("Please input your text here.\n=")
    result = ""
    try:
        for char in text.upper():
            result += md[char] + " "
    except KeyError:
        result = "invalid charecter input!!!"

    return result


def decode():
    code = input("Enter your code here.\n=")
    result = ""
    if not valid_morse(code):
        result = "Your code was not valid or not in my knowladge. Please try again!!!"

    for single_char in code.split(" "):
        result += mad[single_char]

    return result.capitalize()


while True:
    ask = input(
        "Do you want to encode or decode?\nTo encode press 1\nTo decode press 2\n=")

    if ask.isdigit():
        ask = int(ask)

        if ask not in [1, 2]:
            print("Invalid inpput!!!\nTry Again!!!")
            continue

        elif ask == 1:
            result = encode()

        elif ask == 2:
            result = decode()
    break


print(result)

path = "C:\\Users\\user\\Desktop\\"

for i in result:
    if i == ".":
        PlaySound(path+"dot.wav", 0)
    elif i == "-":
        PlaySound(path + "dash.wav", 0)
    elif i == "/":
        sleep(0.25)
    elif i == "!":
        sleep(0.75)