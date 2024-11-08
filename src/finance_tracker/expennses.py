import time
import sys
import os
from time import sleep
logbook = []

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

    # print("%sGoodBye!" % msg)def endscreeen():
    #     msg = "Exciting."
    #     for x in range(5):
    #         msg = msg + "."
    #         print(msg)
    #         sleep(1)
    #         os.system("cls")
    #
    #     print("%sGoodBye!" % msg)



def get_next_serial_number(base_name, extension):

    # List all files in the current directory

    files = os.listdir('.')

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

    sleep(1) # Adds a loading
    loading()

    print(f"\n[!] Remaining Budget: £{budgetRem:.2f}")
    
    print("\n[^] Budget Summary:")
    print(f"[^] Income: £{user_income_float:.2f}")
    print(f"[^] Total Expenses: £{total:.2f}")
    
    if budgetRem < 0:
        print("[!!] You're over budget. Consider reducing your expenses.")
    else:
        savingsRec = budgetRem * 0.5
        print(f"[^] You're currently under budget. Consider saving £{savingsRec:.2f}, which is 50% of remaining budget.")

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

user_income = 0
 
if __name__ == "__main__": # It checks weather the script is being run directly or being imported.
    
    writeSpc("[?]How much do you earn monthly:  ")
    user_income = input("£ ")
    menu()