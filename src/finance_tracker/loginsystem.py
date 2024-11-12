import os
import csv
import random
import datetime
from time import sleep

x = datetime.datetime.now()

# Print the current date and time
current_time = x.strftime("%d-%m-%y %H:%M:%S")

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
                writer.writerow(["Transaction ID", "Name", "Email", "Password"])  # Write email and password
                writer.writerow([user_id, name, email, password])


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

    while not op == "Yes" or "No":
        op = input("Do you have an existing account: ")

        if op == "yes":
            print("[#] Lets get you logged in")
            start.login()
        elif op == "no":
            print("[#] Lets create you an account")
            start.singup()


 
