import shelve
from encryt import encrypt, decrypt


def username_exists(username):
    with shelve.open("username.db") as db:
        return username in db


def signup(username, password):
    if username_exists(username):
        print("Username already found!")
        return False

    with shelve.open("username.db") as db:
        db[username] = encrypt(password)
        print("Signed up!")
        return True


def login(username, password):
    if not username_exists(username):
        print("Username not found!")
        return False

    with shelve.open("username.db") as db:
        for i in db.values():
            if decrypt(i) == password:
                print("Successfully logged in!")
                return True
            
    print('Wrong password!')
    return False


def main():
    signup_or_login = input("Do you want to signup or login? ")

    if signup_or_login.lower() == "signup":
        username = input("Username: ")
        password = input("Password: ")

        signup(username, password)
    elif signup_or_login.lower() == "login":
        username = input("Username: ")
        password = input("Password: ")

        login(username, password)
    else:
        print("Please enter 'signup' or 'login'")


if __name__ == "__main__":
    main()
