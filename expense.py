import json
from datetime import datetime


def write_json(new_expense, filename = "expense_entries.json"):
    with open("expense_entries.json", "r+") as file:
        filedata = json.load(file)
        filedata["Expenses"].append(new_expense)
        file.seek(0)
        json.dump(filedata, file, indent = 4)
    print("Expense added successfully!")


def main():
    intro = input("To enter a new expense, please enter 1.\n" "To exit please enter 2 ")
    if intro == "1":
        while True:
            try:
                date = input("Enter the date of the expense in (YYYY/MM/DD) format please: ")
                datetime.strptime(date, "%Y/%m/%d")
                break
            except ValueError as e:
                print("Invalid format! Please enter the date in YYYY/MM/DD format.")

        while True:
            try:
                amount = input("Enter the amount spent with decimals (90 = 90.00): ")
                float(amount)
                break
            except ValueError:
                print("Invalid amount! Please enter a valid number.")

        while True:
            try:
                print("Choose a category for the expense (enter a number from 1-5): ")
                print("1. Home")
                print("2. Food")
                print("3. Personal")
                print("4. Work")
                print("5. Miscellaneous")
                print("6. Quit expense entry")

                choice = int(input("Enter the number corresponding to the category: "))

                if choice < 1 or choice > 6:
                    raise ValueError

                if choice == 1:
                    category = "Home"
                elif choice == 2:
                    category = "Food"
                elif choice == 3:
                    category = "Personal"
                elif choice == 4:
                    category = "Work"
                elif choice == 5:
                    category = "Miscellaneous"
                elif choice == 6:
                    confirm = input("Are you sure you want to exit? Any progress in this entry will be lost. (yes/no): ")
                    if confirm.lower() == "yes":
                        print("Exiting program. Goodbye!")
                        break
                    else:
                        continue

                break
            except ValueError:
                print("Invalid number! Please enter a number corresponding to the category chosen.")

        note = input("(Optional) Would you like to enter a note with this entry? If not press enter!")

        new_expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "note": note
        }

    elif intro == "2":
        print("Exiting program. Goodbye!")
        return

    write_json(new_expense)


if __name__ == "__main__":
    main()

