def expenses(log_ID):  # Change parameter to log_ID
    global new_category

    while True:
        print("[?] Enter an expense (or 'q' to finish): £")
        user_exp = input()

        if user_exp.lower() == 'q':
            break  # Breaks the loop if the user is done entering expenses

        try:
            amount = float(user_exp)  # Convert user input to float
        except ValueError:
            print("[!] Invalid amount. Please enter a valid number.")
            continue  # It will skip to the next part if input is invalid

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
            # Write header only if the file is empty
            if f.tell() == 0:
                writer.writerow(["log ID", "amount", "category", "Additional category"])  # Write header
            # Write user data
            if category == "E":
                writer.writerow([log_ID, amount, new_category, ""])  # Write new category
            else:
                writer.writerow([log_ID, amount, category_name, ""])  # Write standard category

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
                            # sleep(1)
                            print("\n")
                            # menu(log_ID)  # Pass log_ID to the menu
                            user_found = True  # User found, break out of the loop
                            break
                if not user_found:
                    print("[!] Login failed! Invalid name or user ID.")
                    print("[!] Please try again.\n")  # Prompt to try again
        except FileNotFoundError:
            print(f"[!] The user {log_ID} does not exist.")
            print("[!] Login failed! Invalid name or user ID.")
            print("[!] Please try again.\n")  # Prompt to try again
            # self.login()
            break

login()