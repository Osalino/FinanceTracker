import time
import sys
from sys import stdout
from time import sleep
import random
import csv 
import os
# from time import date
# import datetime


def write(str, eol="\n"):
  for char in str:
    time.sleep(.1)
    sys.stdout.write(char)
    sys.stdout.flush()
  sys.stdout.write(eol) 
  sys.stdout.flush()


def add_income(income):  
    with open('logtracker.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'income']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'income': income})


def income(user_income):
    # print("Initialised income")
    print("Your current income is : £0")
    time.sleep(1)
    user_income = input("[+]Enter your monthly income: £")
    add_income(user_income)
    user_income = money

new = income(user_income)

def expense():
    
    print("Welcome to your  expenses")
    while True:
        user_exp = input("Enter your expenses: £")
        category = input("""What category would that be:

                         [A.] Food
                         [B.] Utilites
                         [C.] Transport
                         [D.] Entertainment
                         [E.] Add another category
                         """)
        if category == "A":
            print("a")
        

    


def budgetsum():
    print("Initialised  budget sum")

def exit():
    print("Initialised exit func")
    quit()

def menu():
    print("""
    ----                               ---- # Menu
          [1*] Add current Income    
          [2*] Add Expenses
          [3*] View your budget
          [4*] Exit[E]   
                        
    ----                              ----
    """)


def start():

    write("Welcome to your personal expense tracker X")
    write("Made by: [Osazemen]\n ")

    number = random.randint(0000,9000)

    user = input("[~]Enter your name: ")
    age = input("[~]Please enter your age: \n")
    
    write(f"Hello {user}, I would recommend you to add a pin for your account security\n")
    security = input("[!]Would you like a pin [y/n] \n").capitalize()

    while security != "Y" and security != "N":
        write("[!]Invalid input, please try again")
        security = input("[!]Would you like a pin [y/n] \n").capitalize()

        if  security == "Y":
            write(f"Here's your security pin : {number} \n")
            write(f"Please remember your pin for future use \n")
            pin = int(input("Enter pin to comfirm"))
            if pin == number:
                write("[!]Pin set successfully")
                menu()
                
        elif  security == "N":
            pin = None
            menu()
   


def login():
    write("Welcome to your personal expense tracker X")
    user = input("[~]Enter your name: ")
    pin = input("[~]Enter your pin: ")

    #vertify in a csv files


        

