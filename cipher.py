from time import sleep

# Symmetric Encryption #
   # CAESER CIPHER #

def main():

    while True:
        message = define_message()
        key = define_key()
        option = define_enc_or_dec()
        if option == 1:
            crypted = encipher(message, key)
        elif option == 2:
            crypted = decipher(message, key)
        show_message(crypted)
        answer = input('Do you want to continue? [Y/N] ').upper()
        while answer not in 'YN':
            answer = input('Please, inform yes or not. [Y/N] ').upper()
        if answer == 'N':
            print('Thank you! ^^')
            break


def define_message():
    message = input('Type a message: ').upper()
    return message


def define_key():
    key = int(input('Type a key: [1-26] '))
    return key


def define_enc_or_dec():
    option = int(input('Choose one of the following options:\n'
                   '\t[1] Encipher\n'
                   '\t[2] Decipher\n'
                   'Inform your choice: '))
    return option


def encrypt(message, key, direction):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ""
    alph_length = len(alphabet)
    for char in message:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_message += alphabet[(char_index + (direction * key)) % alph_length]
        else:
            new_message += char
    return new_message


def encipher(message, key):
    return encrypt(message, key, 1)


def decipher(message, key):
    return encrypt(message, key, -1)


def show_message(message):
    print(f'------------------------\n'
          f'Message: {message}\n'
          f'------------------------')
    sleep(1)


if __name__ == '__main__':
    main()
