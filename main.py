import shelve
from encryt import encrypt, decrypt
from matplotlib import pyplot as plt


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

    print("Wrong password!")
    return False


def interact(username):
    with shelve.open("finance_data.db") as db:
        if db.get(username) is None:
            db[username] = {"expenses": [], "income": []}
            print(f"Welcome, {username}!")
        else:
            print(f"Welcome back, {username}!")

    while True:
        action = input("Enter 'help' to see commands: ")
        if action == "help":
            print("Commands: logout, exit, add, view")
        elif action == "logout":
            print("Logged out!")
            main()
        elif action == "exit":
            print("Goodbye!")
            exit()
        elif action == "add":
            add = input("What do you want to add? (income/expense) ")
            try:
                amount = float(input("Enter the amount: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            description = input("Enter the description: ")
            with shelve.open("finance_data.db") as db:
                if add == "income":
                    db[username]["income"].append(
                        {"amount": amount, "description": description}
                    )
                elif add == "expense":
                    db[username]["expenses"].append(
                        {"amount": amount, "description": description}
                    )
                else:
                    print("Invalid input!")
        elif action == "view":
            plot = input("Do you want to plot the data? (yes/no) ")
            if plot == "yes":
                with shelve.open("finance_data.db") as db:
                    expenses = db[username]["expenses"]
                    income = db[username]["income"]
                    x = [i["description"] for i in expenses]
                    y = [i["amount"] for i in expenses]
                    plt.plot(x, y)
                    plt.show()
            elif plot == "no":
                with shelve.open("finance_data.db") as db:
                    expenses = db[username]["expenses"]
                    income = db[username]["income"]
                    print("Expenses:")
                    for i in expenses:
                        print(f"Amount: {i['amount']}, Description: {i['description']}")
                    print("Income:")
                    for i in income:
                        print(f"Amount: {i['amount']}, Description: {i['description']}")
            else:
                print("Invalid input!")
        else:
            print("Invalid command!")


def main():
    signup_or_login = input("Do you want to signup or login? ")

    if signup_or_login.lower() == "signup":
        username = input("Username: ")
        password = input("Password: ")

        if signup(username, password):
            interact(username)
    elif signup_or_login.lower() == "login":
        username = input("Username: ")
        password = input("Password: ")

        if login(username, password):
            interact(username)
    else:
        print("Please enter 'signup' or 'login'")


if __name__ == "__main__":
    main()
