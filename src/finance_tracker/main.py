import os
import csv
import random
import datetime
import sys
import time
from time import sleep

logbook = []
user_income = 0


x = datetime.datetime.now()

# Print the current date and time
current_time = x.strftime("%d-%m-%y %H:%M:%S")


def writeSpc(str, eol=""):
    for char in str:
        time.sleep(.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()


def write(str, eol="\n"):
    for char in str:
        time.sleep(.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write(eol)
    sys.stdout.flush()


def endscreeen():
    msg = "Exiting"
    for x in range(5):
        msg = msg + "."
        print(msg)
        sleep(1)
        os.system("cls")


def loading():
    msg = "Gatharing your data."

    for x in range(5):
        msg = msg + "."
        print(msg)
        sleep(1)
        os.system("cls")

def expenses():
    while True:
        print("[?]Enter an expense (or 'q' to finish): £")
        user_exp = input()

        if user_exp.lower() == 'q':
            break  # Breaks the loop if the user is done entering expenses

        try:
            amount = float(user_exp)  # Convert user input to float
        except ValueError:
            print("[!]Invalid amount. Please enter a valid number.")
            continue  # it will skip to the next part if input is invalid

        category = input(f"""[~~]What category would that be:
            -------                                        -----

                            [A.] Food
                            [B.] Utilities
                            [C.] Transport
                            [D.] Entertainment
                            [E.] Add another category

           -------                                        -----
                            """).capitalize()

        if category in ["A", "B", "C", "D"]:
            category_name = {
                "A": "Food",
                "B": "Utilities",
                "C": "Transport",
                "D": "Entertainment"
            }[category]
            logbook.append({'amount': amount, 'category': category_name})  # Store amount as a number
            print(f"[^]Your {category_name} expense of £{amount:.2f} has been recorded.")
        elif category == "E":
            new_category = input("Enter category name: ")
            logbook.append({'amount': amount, 'category': new_category})
            print(f"[^]Your {new_category} expense of £{amount:.2f} has been recorded.")
        else:
            print("[!]Invalid choice. Please select a valid category.")


def budget(user_income):
    try:
        user_income_float = float(user_income)
    except ValueError:
        print("[!] Invalid income. Please enter a valid number.")
        return

    total = sum(expense['amount'] for expense in logbook)  # Sums the amounts into the logbook

    budgetRem = user_income_float - total

    sleep(1)  # Adds a loading
    loading()

    print(f"\n[!] Remaining Budget: £{budgetRem:.2f}")

    print("\n[^] Budget Summary:")
    print(f"[^] Income: £{user_income_float:.2f}")
    print(f"[^] Total Expenses: £{total:.2f}")

    if budgetRem < 0:
        print("[!!] You're over budget. Consider reducing your expenses.")
    else:
        savingsRec = budgetRem * 0.5
        print(
            f"[^] You're currently under budget. Consider saving £{savingsRec:.2f}, which is 50% of remaining budget.")

    print("\n[~] Expense Breakdown:")
    category_totals = {}
    for expense in logbook:
        category = expense['category']
        category_totals[category] = category_totals.get(category, 0) + expense['amount']  # Corrected this line

    for category, total in category_totals.items():
        print(f"{category}: £{total:.2f}")


def menu():
    while True:  # Will continously keep showing the menu until the user chooses to exit it.
        choice = input("""
    ----                               ---- 

          [1*] Add Expenses
          [2*] View your budget
          [3*] Exit[E]   

    ----                              ----
    """)

        if choice == "1":
            expenses()
        elif choice == "2":
            budget(user_income)
        elif choice.lower() == "3" or choice.lower() == "e":
            endscreeen()
            break
        else:
            write("[!]Invalid choice")


class Start:
    def __init__(self):
        self.users = {}

    def signup(self):

        print("Welcome to the personal expense tracker X")
        print("Made by: [Osazemen]\n ")

        name = input("Enter your name: ")
        email = input("Enter email address: ")
        password = input("Enter password: ")
        conf_password = input("Confirm password: ")

        sleep(1)

        loading()

        if password == conf_password:
            user_id = f"{random.randint(0, 999):03d}"
            print(f"Heres you user ID: {user_id}, you will need it to log back in")

            # tranc_filename = f"../data/users/{user_id}_transactions.csv"

            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../transaction_record/logs/'))
            tranc_filename = os.path.join(base_dir, f"{user_id}_transactions.csv")

            os.makedirs(os.path.dirname(tranc_filename), exist_ok=True)

            with open(tranc_filename, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Transaction ID", "name"])  # Write email and hashed password
                writer.writerow([user_id, name])  # Write email and hashed password

            with open('database.csv', mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Transaction ID", "Name", "Email", "Password", "Date Created"])  # Write email and password
                writer.writerow([user_id, name, email, password, current_time])

            print("You have registered successfully!")
            self.login()
        else:
            print("Passwords do not match!")

    def login(self):
        print("Welcome to your personal expense tracker X")
        print("Made by: [Osazemen]\n ")

        lg_name = input("[!] Please enter your name: ")
        log_ID = input("[!] Please enter your user ID: ")

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = f"..\\transaction_record\\logs\\{log_ID.zfill(3)}_transactions.csv"
        abs_file_path = os.path.join(script_dir, rel_path)

        # login_filename = f'..\\users\\{log_ID.zfill(3)}_transactions.csv'
        #

        # print(f"Trying to open file: {login_filename}")
        print(f"Trying to open file: {abs_file_path}")

        try:
            # with open(login_filename, mode='r') as f:
            with open(abs_file_path, mode='r') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
                    if row:
                        user_id, name = row
                        if lg_name == name and log_ID == user_id:
                            print(f"Welcome {name} you have logged in successfully!")
                            sleep(1)
                            print("\n")
                            return

        except FileNotFoundError:
            # print(f"[!] The file {login_filename} does not exist.")
            print(f"[!] The file {abs_file_path} does not exist.")
            return None

        print("Login failed! Invalid name or user ID.")
        return None


if __name__ == "__main__":
    start = Start()
    print("Welcome to the personal expense tracker X")
    print("Made by: [Osazemen]\n ")

    sleep(1)

    op = input("Do you have an existing account: ").upper()

    while op != "YES" and op != "NO":
        op = input("Please answer with 'Yes' or 'No': ").upper()
    if op == "YES":
        print("[#] Let's get you logged in")
        start.login()
        writeSpc("[?]How much do you earn monthly:  ")
        user_income = input("£ ")
        menu()

    elif op == "NO":
        print("[#] Let's create you an account")
        start.signup()
