import shelve
from encryt import encrypt, decrypt


def username_exists(username):
    with shelve.open("username.db") as db:
        for i in db:
            if i == username:
                return True

    return False


def signup(username, password):
    if username_exists(username):
        print("Username already found!")
        return

    with shelve.open("username.db") as db:
        db[username] = encrypt(password)
        print("Signed up!")


def main():
    signup_or_login = input("Do you want to signup or login? ")

    if signup_or_login.lower() == "signup":
        username = input("Username: ")
        password = input("Password: ")

        signup(username, password)
    else:
        print("Please enter 'signup' or 'login'")


if __name__ == "__main__":
    main()
