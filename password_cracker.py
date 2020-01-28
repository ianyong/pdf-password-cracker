import sys
import os
import pikepdf
import string
import itertools

digits = string.digits
alphabet = string.ascii_letters
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
chars = string.digits + string.ascii_letters
password_length = 0
password_list = []
found = False

def check_file(filename):
    if not os.path.isfile(filename):
        print("File does not exist")
        return False
    elif not filename.endswith(".pdf"):
        print("Specified file is not a PDF document")
        return False
    else:
        return True

def set_constraints():
    global password_length
    constraints = sys.argv[2]
    command = False
    for char in constraints:
        if char == '/':
            command = True
        else:
            password_length += 1
            if command == False:
                password_list.append(char)
            else:
                command = False
                if char == 'd':
                    password_list.append(digits)
                elif char == 'a':
                    password_list.append(alphabet)
                elif char == 'u':
                    password_list.append(uppercase)
                elif char == 'l':
                    password_list.append(lowercase)
                elif char == 'c':
                    password_list.append(chars)
                else:
                    print("Invalid constraints")
                    return False
    return True

def crack_password(filename):
    def recurse(index, guess):
        global found
        if found:
            return
        if index >= password_length:
            print(guess)
            try:
                pikepdf.Pdf.open(filename, password=guess)
                print("Password: " + guess)
                found = True
            except:
                pass
        else:
            valid_chars = password_list[index]
            for char in valid_chars:
                recurse(index + 1, guess + char)
    try:
        pikepdf.Pdf.open(filename)
        print("PDF file is not encrypted.")
    except:
        global password_length
        print("Brute forcing password...")
        if len(sys.argv) > 2:
            if set_constraints():
                recurse(0, "")
                if found == False:
                    print("Password not found with set constraints")
        else:
            while True:
                for guess in itertools.product(chars, repeat = password_length):
                    guess = ''.join(guess)
                    print(guess)
                    try:
                        pikepdf.Pdf.open(filename, password=guess)
                        print("Password: " + guess)
                        return
                    except:
                        pass
                password_length += 1

if len(sys.argv) < 2:
    print("Please specify a PDF file as argument")
else:
    filename = sys.argv[1]
    if check_file(filename):
        crack_password(filename)