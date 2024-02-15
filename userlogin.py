import json
import re

def write_json(new_user, filename="users.json"):
    with open(filename, "r+") as file:
        filedata = json.load(file)
        filedata["Users"].append(new_user)
        file.seek(0)
        json.dump(filedata, file, indent=4)
    print("Account created successfully!")


def password_requirements():
    print("Your password must contain the following:")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character")
    print("- Minimum length of 8 characters")


def is_valid_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(pattern.match(password))


def is_username_taken(username, filename="users.json"):
    with open(filename, "r") as file:
        data = json.load(file)
        usernames = [user["username"] for user in data["Users"]]
        return username in usernames


def main():
    print("Welcome to your Personal Finance tracker! Create a new account to access personalized data on your finances!")
    intro = input("To create a new account please enter 1, to exit please enter 2: ")

    if intro == "1":
        username = input("Enter your new username: ")

        while is_username_taken(username):
            print("This username is already taken. Please try again.")
            username = input("Enter your new username: ")

        password_requirements()
        password = input("Enter your new password: ")

        while not is_valid_password(password):
            print("Invalid password. Please try again.")
            password = input("Enter your new password: ")

        new_user = {
            "username": username,
            "password": password
        }

        write_json(new_user)

    elif intro == "2":
        print("Exiting program. Goodbye!")
        return


if __name__ == "__main__":
    main()
