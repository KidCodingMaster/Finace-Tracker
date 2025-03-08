def encrypt(string):
    string = list(string)

    for i in range(len(string)):
        string[i] = str(ord(string[i])) + "-"

    string = "".join(string)

    return str(string)[:-1]


def decrypt(string):
    string = string.split("-")

    for i in range(len(string)):
        string[i] = "".join(chr(int(string[i])))

    return "".join(string)
