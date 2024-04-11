# This is Joseph Sinder's main.py file.

def encode(password):
    encoded_password = ''
    for i in range(0, len(password)):
        if int(password[i]) < 7:
            encoded_password += str((int(password[i]) + 3))
        else:
            encoded_password += str((int(password[i]) - 7))
    return encoded_password

def decode(password):
    decoded_password = ''
    for char in password:
        decoded_password += str((int(char) + 7) % 10)
    return decoded_password

