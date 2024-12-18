import os
import csv
import random
import datetime
import sys
import time
# from dis import log_ID
from time import sleep

from src.test.locate import user_id

logbook = []
user_income = 0
from datetime import datetime

# Now you can use datetime.now() directly
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
    quit()


def loading():
    msg = "Gatharing your data."

    for x in range(5):
        msg = msg + "."
        print(msg)
        sleep(1)
        os.system("cls")


def expenses(log_ID):  # Change parameter to log_ID
    # global new_category
    while True:
        print("[?] Enter an expense (or 'q' to finish): £")
        user_exp = input()


        if user_exp.lower() == 'q':
            break
        try:
            amount = float(user_exp)
        except ValueError:
            print("[!] Invalid amount. Please enter a valid number.")
            continue  #
        category = input(f"""[~~] What category would that be:
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
            logbook.append({'amount': amount, 'category': category_name})
            print(f"[^] Your {category_name} expense of £{amount:.2f} has been recorded.")
        elif category == "E":
            new_category = input("Enter category name: ")
            logbook.append({'amount': amount, 'category': new_category})
            print(f"[^] Your {new_category} expense of £{amount:.2f} has been recorded.")
        else:
            print("[!] Invalid choice. Please select a valid category.")
            continue  # Skip to the next iteration


        # Write the expense to the CSV file

        with open('user-expenses.csv', mode='a', newline='') as f:
            writer = csv.writer(f)

            if f.tell() == 0:
                writer.writerow(["log ID", "amount", "category", "Additional category"])
            if category == "E":
                writer.writerow([log_ID, amount, new_category, ""])
            else:
                writer.writerow([log_ID, amount, category_name, ""])



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


def menu(name_id):
    while True:  # Will continously keep showing the menu until the user chooses to exit it.

        choice = input("""
    ----                               ---- 

          [1*] Add Expenses
          [2*] View your budget
          [3*] Exit[E]   

    ----                              ----
    """)

        if choice == "1":
            expenses(name_id)
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

        while True:
            password = input("Enter password: ")
            conf_password = input("Confirm password: ")
            if password == conf_password:
                break  # Exit the loop if passwords match
            else:
                print("Passwords do not match! Please try again.")
        sleep(1)


        user_id = f"{random.randint(0, 999):03d}"

        print(f"Here's your user ID: {user_id}, you will need it to log back in")
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../transaction_record/logs/'))
        tranc_filename = os.path.join(base_dir, f"{user_id}_transactions.csv")
        os.makedirs(os.path.dirname(tranc_filename), exist_ok=True)

        with open(tranc_filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            # writer.writerow(["User ID", "Name"])  # Write header
            writer.writerow([user_id, name])  # Write user data

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        with open('database.csv', mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["User ID", "Name", "Email", "Password", "Date Created", "Income"])  # Write header
            writer.writerow([user_id, name, email, password, current_time, user_income])  # Write user data
        print("You have registered successfully!")
        loading()
        print("\n")
        self.login()

    def login(self):
        print("")
        while True:
            lg_name = input("[!] Please enter your name: ")
            log_ID = input("[!] Please enter your user ID: ")  # Store log_ID
            script_dir = os.path.dirname(__file__)  # Absolute dir the script is in
            rel_path = f"..\\transaction_record\\logs\\{log_ID.zfill(3)}_transactions.csv"
            abs_file_path = os.path.join(script_dir, rel_path)

            try:
                with open(abs_file_path, mode='r') as f:
                    reader = csv.reader(f)
                    user_found = False  # Flag to check if user is found
                    for row in reader:
                        if row:
                            user_id, name = row
                            if lg_name == name and log_ID == user_id:
                                print(f"Welcome {name}, you have logged in successfully!")
                                sleep(1)
                                print("\n")
                                menu(log_ID)  # Pass log_ID to the menu
                                user_found = True  # User found, break out of the loop
                                break

                    if not user_found:
                        print("[!] Login failed! Invalid name or user ID.")
                        print("[!] Please try again.\n")  # Prompt to try again
            except FileNotFoundError:
                print(f"[!] The user {log_ID} does not exist.")
                print("[!] Login failed! Invalid name or user ID.")
                print("[!] Please try again.\n")  # Prompt to try again
                self.login()
                break



if __name__ == "__main__":
    start = Start()
    print("Welcome to the personal expense tracker X")
    print("Made by: [Osazemen]\n ")

    user_income = input("[?] How much do you earn monthly: £ ")
    sleep(1)

    while True:  # Loop until the user successfully logs in or chooses to create an account
        op = input("[~]Do you already have an existing account (e to exit) : ").upper()

        while op not in ["YES", "NO","E"]:
            op = input("Please answer with 'Yes' or 'No': ").upper()

        if op == "YES":
            print("\n")
            print("[#] Let's get you logged in")
            if start.login():  # If login is successful
                break  # Exit the loop after successful login
        elif op == "NO":
            print("\n")
            print("[#] Let's create you an account")
            start.signup()
            print("\n")
        elif op == "E":
            break
        break
