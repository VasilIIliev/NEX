import os
os.system("title NEX Text Encryption Tool")

#--------------------------------------------------------------------Menus-----------------------------------------------------------------------------------#

def banner():
    GREEN = "\033[92m"
    RESET = "\033[0m"
    font=f"""{GREEN}
 .-----------------. .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| | ____  _____  | || |  _________   | || |  ____  ____  | |
| ||_   \|_   _| | || | |_   ___  |  | || | |_  _||_  _| | |
| |  |   \ | |   | || |   | |_  \_|  | || |   \ \  / /   | |
| |  | |\ \| |   | || |   |  _|  _   | || |    > `' <    | |
| | _| |_\   |_  | || |  _| |___/ |  | || |  _/ /'`\ \_  | |
| ||_____|\____| | || | |_________|  | || | |____||____| | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
 {RESET}"""
    print(font)
    print(f" {GREEN}                 NEX Text Encryption Tool  \n\n\n")

def main_menu():
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

def show_encryption_menu():
    print("\nSelect Encryption Method:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Polyalphabetic")
    print("4. Transposition Cipher")
    print("5. Stream Cipher")
    print("6. Go Back")

def show_decryption_menu():
    print("\nSelect Decryption Method:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Polyalphabetic")
    print("4. Transposition Cipher")
    print("5. Stream Cipher")
    print("6. Go Back")

#---------------------------------------------------------------------Menus-----------------------------------------------------------------------------------#
#------------------------------------------------------------------------Caesar-------------------------------------------------------------------------------#

def caesar_cipher_encrypt():
        text = input("Enter text to encrypt: ")
        shift = int(input("Enter shift value: "))

        encrypted_text = ""

        for char in text:

            if char.islower():
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                encrypted_text += new_char

            elif char.isupper():
                new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                encrypted_text += new_char
            else:
                encrypted_text += char

        print(f"Encrypted Text: {encrypted_text}")

def caesar_cipher_brute_force_decrypt():
    text = input("Enter text to decrypt: ")

    for shift in range(1, 26):
        decrypted_text = ""
        for char in text:
            if char.islower():
                new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                decrypted_text += new_char
            elif char.isupper():
                new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                decrypted_text += new_char
            else:
                decrypted_text += char

        print(f"Shift {shift}: {decrypted_text}")

def caesar_cipher_decrypt_with_shift():
    text = input("Enter text to decrypt: ")
    shift = int(input("Enter shift value: "))
    decrypted_text = ""
    for char in text:
        if char.islower():
            new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text += new_char
        elif char.isupper():
            new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += new_char
        else:
            decrypted_text += char
    print(f"Decrypted Text: {decrypted_text}")

#------------------------------------------------------------------------Caesar-------------------------------------------------------------------------------#
#------------------------------------------------------------------------Vigenere-----------------------------------------------------------------------------#

def vigenere_encrypt_plaintext_as_key():
    text = input("Enter text to encrypt: ").upper()
    key = input("Enter encryption key: ").upper()
    encrypted_text = ""
    key_index = 0
    for i in range(len(text)):
        if text[i].isalpha():
            if key_index < len(key):
                shift = ord(key[key_index]) - ord('A')
            else:
                shift = ord(text[key_index - len(key)]) - ord('A')
            new_char = chr(((ord(text[i]) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += new_char
            key_index += 1
        else:
            encrypted_text += text[i]
    print(f"Encrypted Text: {encrypted_text}")

def vigenere_decrypt_plaintext_as_key():
    text = input("Enter text to decrypt: ").upper()
    key = input("Enter decryption key: ").upper()
    decrypted_text = ""
    key_index = 0
    for i in range(len(text)):
        if text[i].isalpha():
            if key_index < len(key):
                shift = ord(key[key_index]) - ord('A')
            else:
                shift = ord(text[key_index - len(key)]) - ord('A')
            new_char = chr(((ord(text[i]) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += new_char
            key_index += 1
        else:
            decrypted_text += text[i]

    print(f"Decrypted Text: {decrypted_text}")

def vigenere_encrypt_repeating_key():
    text = input("Enter text to encrypt: ").upper()
    key = input("Enter encryption key: ").upper()
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += new_char
            key_index += 1
        else:
            encrypted_text += char
    print(f"Encrypted Text: {encrypted_text}")

def vigenere_decrypt_repeating_key():
    text = input("Enter text to decrypt: ").upper()
    key = input("Enter decryption key: ").upper()
    decrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += new_char
            key_index += 1
        else:
            decrypted_text += char
    print(f"Decrypted Text: {decrypted_text}")

#------------------------------------------------------------------------Vigenere-----------------------------------------------------------------------------#
#------------------------------------------------------------------------Poly alphabetic-----------------------------------------------------------------------#

def polyalphabetic_encrypt():
    text = input("Enter text to encrypt: ").upper()
    key = input("Enter encryption key: ").upper()
    encrypted_text = ""
    key_index = 0
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            new_char = chr(((ord(text[i]) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += new_char
            key_index += 1
        else:
            encrypted_text += text[i]
    print(f"Encrypted Text: {encrypted_text}")

def polyalphabetic_decrypt():
    text = input("Enter text to decrypt: ").upper()
    key = input("Enter decryption key: ").upper()
    decrypted_text = ""
    key_index = 0

    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            new_char = chr(((ord(text[i]) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += new_char
            key_index += 1
        else:
            decrypted_text += text[i]

    print(f"Decrypted Text: {decrypted_text}")

#------------------------------------------------------------------------Poly alphabetic-----------------------------------------------------------------------#
#------------------------------------------------------------------------Transposition------------------------------------------------------------------------#

def columnar_transposition_encrypt():
    text = input("Enter text to encrypt: ").replace(" ",
                                                    "").upper()  # Премахваме интервалите и правим всичко на главни букви
    key = int(input("Enter number of columns: "))

    # Намираме броя на редовете (по принцип не сме сигурни, че всеки ред ще е напълнен напълно)
    num_rows = len(text) // key + (1 if len(text) % key != 0 else 0)

    # Запълваме матрицата
    matrix = ['' for _ in range(num_rows)]
    for i in range(len(text)):
        row = i % num_rows
        matrix[row] += text[i]

    # Четем по колони
    encrypted_text = ''.join(matrix)
    print(f"Encrypted Text: {encrypted_text}")

def columnar_transposition_decrypt():
    text = input("Enter text to decrypt: ").replace(" ",
                                                    "").upper()  # Премахваме интервалите и правим всичко на главни букви
    key = int(input("Enter number of columns: "))

    # Намираме броя на редовете
    num_rows = len(text) // key
    num_extra_chars = len(text) % key

    # Запълваме колоните
    matrix = ['' for _ in range(key)]
    for i in range(key):
        col_length = num_rows + (1 if i < num_extra_chars else 0)
        matrix[i] = text[:col_length]
        text = text[col_length:]

    # Четем по редове
    decrypted_text = ''
    for row in range(num_rows):
        for col in range(key):
            if row < len(matrix[col]):
                decrypted_text += matrix[col][row]

    print(f"Decrypted Text: {decrypted_text}")

def period_transposition_encrypt():
    text = input("Enter text to encrypt: ").replace(" ",
                                                    "").upper()  # Премахваме интервалите и правим всичко на главни букви
    period = int(input("Enter period (block size): "))

    # Разделяме текста на блокове
    blocks = [text[i:i + period] for i in range(0, len(text), period)]

    # Четем по колони (разделяме по букви на всеки блок)
    encrypted_text = ''
    for i in range(period):
        for block in blocks:
            if i < len(block):
                encrypted_text += block[i]

    print(f"Encrypted Text: {encrypted_text}")

def period_transposition_decrypt():
    text = input("Enter text to decrypt: ").replace(" ",
                                                    "").upper()  # Премахваме интервалите и правим всичко на главни букви
    period = int(input("Enter period (block size): "))

    # Разделяме текста на блокове
    num_blocks = len(text) // period
    blocks = ['' for _ in range(num_blocks)]

    # Попълваме блоковете по колони
    index = 0
    for i in range(period):
        for j in range(num_blocks):
            if index < len(text):
                blocks[j] += text[index]
                index += 1

    # Обединяваме блоковете, за да получим оригиналния текст
    decrypted_text = ''.join(blocks)

    print(f"Decrypted Text: {decrypted_text}")

#------------------------------------------------------------------------Transposition------------------------------------------------------------------------#
#------------------------------------------------------------------------Stream-------------------------------------------------------------------------------#

def stream_cipher_encrypt():
    text = input("Enter text to encrypt: ")
    key = input("Enter encryption key: ")
    stream = ''.join(chr(ord(key[i % len(key)]) ^ ord(text[i])) for i in range(len(text)))
    print(f"Encrypted Text: {stream}")

def stream_cipher_decrypt():
    encrypted_text = input("Enter text to decrypt: ")
    key = input("Enter decryption key: ")
    decrypted_text = ''.join(chr(ord(key[i % len(key)]) ^ ord(encrypted_text[i])) for i in range(len(encrypted_text)))
    print(f"Decrypted Text: {decrypted_text}")

#------------------------------------------------------------------------Stream-------------------------------------------------------------------------------#
banner()
while True:
    main_menu()
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            while True:
                show_encryption_menu()
                enc_choice = input("Enter your choice: ")
                match enc_choice:
                    case "1":
                        print("\nYou selected Caesar Cipher Encryption.\n")
                        caesar_cipher_encrypt()
                    case "2":
                        print("\nYou selected Vigenère Cipher Encryption.\n")
                        vigenere_choice_encrypt=int(input("Which cipher would you like to choose?"))
                        print("1. Vigenere cipher with repeating key")
                        print("2. Vigenere cipher with paintext as the key")
                        match vigenere_choice_encrypt:
                            case 1:
                                vigenere_encrypt_repeating_key()
                            case 2:
                                vigenere_encrypt_plaintext_as_key()
                            case _:
                                print("Invalid choice. Please try again.")
                    case "3":
                        print("\nYou selected Polyalphabetic Encryption.\n")
                        polyalphabetic_encrypt()
                    case "4":
                        print("You selected Transposition Cipher Encryption.")
                        transposition_choice_encrypt = input("Which cipher would you like to choose?")
                        print("1. Transposition cipher with columns")
                        print("2. Transposition cipher with period")
                        match transposition_choice_encrypt:
                            case 1:
                                columnar_transposition_encrypt()
                            case 2:
                                period_transposition_encrypt()
                            case _:
                                print("Invalid choice. Please try again.")
                    case "5":
                        print("You selected Stream Cipher Encryption.")
                        stream_cipher_encrypt()
                    case "6":
                        break
                    case _:
                        print("Invalid choice. Please try again.")

        case "2":
            while True:
                show_decryption_menu()
                dec_choice = input("Enter your choice: ")

                match dec_choice:
                    case "1":
                        print("You selected Caesar Cipher Decryption.")
                        while True:
                            caesar_choice = input("Do you know the shift value? (y/n): ").lower()
                            if caesar_choice not in ['y', 'n']:
                                print("Invalid choice. Please enter 'y' or 'n'.")
                            else:
                                match caesar_choice:
                                    case 'y':
                                        caesar_cipher_decrypt_with_shift()
                                        break
                                    case 'n':
                                        caesar_cipher_brute_force_decrypt()
                                        break
                    case "2":
                        print("You selected Vigenère Cipher Decryption.")
                        vigenere_choice_decrypt = input("Which cipher would you like to choose?")
                        print("1. Vigenere cipher with repeating key")
                        print("2. Vigenere cipher with paintext as the key")
                        match vigenere_choice_decrypt:
                            case 1:
                                vigenere_decrypt_repeating_key()
                            case 2:
                                vigenere_decrypt_plaintext_as_key()
                            case _:
                                print("Invalid choice. Please try again.")
                    case "3":
                        print("\nYou selected Polyalphabetic Decryption.\n")
                        polyalphabetic_decrypt()
                    case "4":
                        transposition_choice_decrypt = input("Which cipher would you like to choose?")
                        print("1. Transposition cipher with columns")
                        print("2. Transposition cipher with period")
                        match transposition_choice_decrypt:
                            case 1:
                                columnar_transposition_decrypt()
                            case 2:
                                period_transposition_decrypt()
                            case _:
                                print("Invalid choice. Please try again.")
                    case "5":
                        print("You selected Stream Cipher Decryption.")
                        stream_cipher_decrypt()
                    case "6":
                        break
                    case _:
                        print("Invalid choice. Please try again.")

        case "3":
            print("Exiting program. Goodbye!")
            break

        case _:
            print("Invalid choice. Please try again.")