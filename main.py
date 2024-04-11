# This is Joseph Sinder's main.py file.

def encode(password):
    encoded_password = ''
    for i in range(0, len(password)):
        if int(password[i]) < 7:
            encoded_password += str((int(password[i]) + 3))
        else:
            encoded_password += str((int(password[i]) - 7))
    return encoded_password


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")


def decode(password):
    decoded_password = ''
    for char in password:
        decoded_password += str((int(char) + 7) % 10)
    return decoded_password


if __name__ == '__main__':
    code_running = True
    while code_running:
        print_menu()
        option = input("Please enter an option: ")
        if option == '1':
            password = input("Please enter your password to encode: ")
            new_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")
        elif option == '2':
            print(f"The encoded_password is {new_password}, and the original password is {decode(new_password)}.")
            print("")
        elif option == '3':
            code_running = False
        else:
            print("Invalid option, try again.")
            print("")