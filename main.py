# This is Joseph Sinder's main.py file.

def encode(password):
    encoded_password = ''
    for i in range(0, len(password)):
        if int(password[i]) < 7:
            encoded_password += str((int(password[i]) + 3))
        else:
            encoded_password += str((int(password[i]) - 7))
    return encoded_password
